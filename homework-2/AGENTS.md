# AGENTS.md - Context & Rules for Mini Kanban Board

## Project Overview
`mini-kanban` is a full-stack task management application:
- `backend/`: FastAPI application running on Python with SQLite database, managed via `uv`.
- `frontend/`: React + Vite single-page application connecting to backend at `http://localhost:8000`.
- `openapi.yaml`: Contract defining all REST API endpoints.

## Developer Commands
- **Start Backend:**
  ```bash
  cd backend && uv run uvicorn main:app --reload
  ```
- **Start Frontend:**
  ```bash
  cd frontend && npm run dev
  ```
- **Run Tests:**
  ```bash
  cd backend && uv run pytest
  ```

## Mandatory Rules for AI Agents
1. **Never commit secrets, `.env`, `.agents/`, `.venv/` or databases (`*.db`, `*.sqlite3`).**
2. **Strict OpenAPI compliance:** All API endpoints must adhere to `openapi.yaml`.
3. **Keep business logic and database persistence clean and separated.**
