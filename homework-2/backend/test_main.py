import pytest
from fastapi.testclient import TestClient
import os
import tempfile
import database
from main import app

@pytest.fixture(autouse=True)
def setup_test_db(monkeypatch):
    # Usa un archivo temporal SQLite para aislar completamente las pruebas
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        test_db_path = tmp.name

    monkeypatch.setattr(database, "DB_PATH", test_db_path)
    database.init_db(test_db_path)

    yield test_db_path

    if os.path.exists(test_db_path):
        try:
            os.remove(test_db_path)
        except OSError:
            pass

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_list_task():
    # Crear tarea
    payload = {
        "title": "Aprender FastAPI y uv",
        "description": "Estudiar el módulo 2 de AI Dev Tools Zoomcamp",
        "column": "todo"
    }
    create_res = client.post("/api/tasks", json=payload)
    assert create_res.status_code == 201
    created = create_res.json()
    assert created["id"] is not None
    assert created["title"] == payload["title"]
    assert created["column"] == "todo"

    # Listar tareas
    list_res = client.get("/api/tasks")
    assert list_res.status_code == 200
    tasks = list_res.json()
    assert len(tasks) == 1
    assert tasks[0]["id"] == created["id"]

def test_update_task_column():
    # Crear tarea
    create_res = client.post("/api/tasks", json={"title": "Tarea de prueba", "column": "todo"})
    task_id = create_res.json()["id"]

    # Mover a in_progress
    patch_res = client.patch(f"/api/tasks/{task_id}", json={"column": "in_progress"})
    assert patch_res.status_code == 200
    assert patch_res.json()["column"] == "in_progress"

    # Mover a done
    patch_done = client.patch(f"/api/tasks/{task_id}", json={"column": "done"})
    assert patch_done.status_code == 200
    assert patch_done.json()["column"] == "done"

def test_delete_task():
    create_res = client.post("/api/tasks", json={"title": "Para borrar", "column": "todo"})
    task_id = create_res.json()["id"]

    del_res = client.delete(f"/api/tasks/{task_id}")
    assert del_res.status_code == 200

    # Verificar que ya no exista
    list_res = client.get("/api/tasks")
    assert len(list_res.json()) == 0

def test_task_not_found():
    res = client.patch("/api/tasks/9999", json={"title": "No existe"})
    assert res.status_code == 404

    del_res = client.delete("/api/tasks/9999")
    assert del_res.status_code == 404
