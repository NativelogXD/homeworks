import os
import tempfile
from fastapi.testclient import TestClient
import pytest

# Ensure cross-platform DB URL if not already set by environment
if not os.environ.get("RELAY_DATABASE_URL") and not os.environ.get("DATABASE_URL"):
    default_db_path = os.path.join(tempfile.gettempdir(), "agent-relay-integration.db").replace("\\", "/")
    os.environ["RELAY_DATABASE_URL"] = f"sqlite:///{default_db_path}"

import main
from database import Base, engine


@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


def test_agent_task_flow_integration():
    """Integration test verifying full agent task lifecycle:
    register -> send (queued) -> claim (processing) -> complete -> check (completed).
    """
    with TestClient(main.app) as client:
        # 1. Register sender (Alice)
        alice_res = client.post("/api/v1/agents", json={"name": "alice"})
        assert alice_res.status_code == 201
        alice_data = alice_res.json()
        alice_headers = {"Authorization": f"Bearer {alice_data['token']}"}

        # 2. Register recipient (Bob)
        bob_res = client.post("/api/v1/agents", json={"name": "bob"})
        assert bob_res.status_code == 201
        bob_data = bob_res.json()
        bob_headers = {"Authorization": f"Bearer {bob_data['token']}"}

        # 3. Alice sends a task to Bob
        task_res = client.post(
            "/api/v1/tasks",
            headers=alice_headers,
            json={"to": bob_data["agent_id"], "input": "calculate 2 + 2"},
        )
        assert task_res.status_code == 201
        task = task_res.json()
        task_id = task["task_id"]
        assert task["status"] == "queued"

        # 4. Bob claims the task
        claim_res = client.post(
            "/api/v1/tasks/claim",
            headers=bob_headers,
            json={"worker_id": "bob-worker-1", "wait_seconds": 0},
        )
        assert claim_res.status_code == 200
        claim = claim_res.json()
        assert claim["task_id"] == task_id
        assert "claim_token" in claim
        claim_token = claim["claim_token"]

        # Alice verifies task is in 'processing' status
        check_proc = client.get(f"/api/v1/tasks/{task_id}", headers=alice_headers)
        assert check_proc.status_code == 200
        assert check_proc.json()["status"] == "processing"

        # 5. Bob completes the task
        comp_res = client.post(
            f"/api/v1/tasks/{task_id}/complete",
            headers=bob_headers,
            json={"claim_token": claim_token, "output": "4"},
        )
        assert comp_res.status_code == 200
        assert comp_res.json()["status"] == "completed"

        # 6. Alice queries the final task status
        final_res = client.get(f"/api/v1/tasks/{task_id}", headers=alice_headers)
        assert final_res.status_code == 200
        final_data = final_res.json()
        assert final_data["status"] == "completed"
        assert final_data["output"] == "4"
