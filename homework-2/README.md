# Mini Kanban Board

A modern, responsive full-stack Kanban board for visual task management built with FastAPI, SQLite, and React + Vite.

## Architecture
- **Backend:** FastAPI, Python 3.11+, SQLite, managed with `uv`.
- **Frontend:** React 18, Vite.
- **Contract:** OpenAPI 3.0 specification (`openapi.yaml`).

## Getting Started

### Backend
```bash
cd backend
uv run uvicorn main:app --reload
```
API runs at: `http://localhost:8000`  
Swagger docs available at: `http://localhost:8000/docs`

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at: `http://localhost:5173`

### Tests
```bash
cd backend
uv run pytest
```
