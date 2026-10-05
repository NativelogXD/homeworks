import sqlite3
from datetime import datetime, timezone
import os

DB_PATH = os.environ.get("KANBAN_DB_PATH", "kanban.db")

def get_connection(db_path: str | None = None) -> sqlite3.Connection:
    target_path = db_path if db_path is not None else DB_PATH
    conn = sqlite3.connect(target_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: str | None = None) -> None:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT DEFAULT '',
            column TEXT NOT NULL CHECK(column IN ('todo', 'in_progress', 'done')),
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_all_tasks(db_path: str | None = None) -> list[dict]:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, column, created_at FROM tasks ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_task_by_id(task_id: int, db_path: str | None = None) -> dict | None:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, column, created_at FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def create_task(title: str, description: str = "", column: str = "todo", db_path: str | None = None) -> dict:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    now_iso = datetime.now(timezone.utc).isoformat()
    cursor.execute(
        "INSERT INTO tasks (title, description, column, created_at) VALUES (?, ?, ?, ?)",
        (title, description, column, now_iso)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {
        "id": new_id,
        "title": title,
        "description": description,
        "column": column,
        "created_at": now_iso
    }

def update_task(task_id: int, title: str | None = None, description: str | None = None, column: str | None = None, db_path: str | None = None) -> dict | None:
    current = get_task_by_id(task_id, db_path)
    if not current:
        return None

    new_title = title if title is not None else current["title"]
    new_desc = description if description is not None else current["description"]
    new_col = column if column is not None else current["column"]

    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, column = ? WHERE id = ?",
        (new_title, new_desc, new_col, task_id)
    )
    conn.commit()
    conn.close()

    return {
        "id": task_id,
        "title": new_title,
        "description": new_desc,
        "column": new_col,
        "created_at": current["created_at"]
    }

def delete_task(task_id: int, db_path: str | None = None) -> bool:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted
