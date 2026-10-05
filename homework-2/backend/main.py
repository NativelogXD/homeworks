from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
from contextlib import asynccontextmanager
import database

# Asegura que la tabla exista al inicializar
database.init_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.init_db()
    yield

app = FastAPI(
    title="Mini Kanban Board API",
    description="Backend FastAPI para el tablero Kanban con SQLite",
    version="1.0.0",
    lifespan=lifespan
)

# Configuración de CORS para permitir la comunicación con el Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquemas Pydantic correspondientes a openapi.yaml
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    column: Literal["todo", "in_progress", "done"] = "todo"

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    column: Literal["todo", "in_progress", "done"] | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    column: Literal["todo", "in_progress", "done"]
    created_at: str

# Endpoints REST
@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/tasks", response_model=list[TaskResponse])
def list_tasks():
    return database.get_all_tasks()

@app.post("/api/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate):
    created = database.create_task(
        title=task_in.title,
        description=task_in.description,
        column=task_in.column
    )
    return created

@app.patch("/api/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_in: TaskUpdate):
    updated = database.update_task(
        task_id=task_id,
        title=task_in.title,
        description=task_in.description,
        column=task_in.column
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    success = database.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
