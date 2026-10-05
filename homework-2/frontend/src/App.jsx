import React, { useState, useEffect } from 'react';
import KanbanColumn from './components/KanbanColumn';
import NewTaskModal from './components/NewTaskModal';

const API_BASE = '/api';

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [isBackendOnline, setIsBackendOnline] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  // Comprobar salud del backend y cargar tareas
  const fetchTasks = async () => {
    try {
      const healthRes = await fetch(`${API_BASE}/health`);
      if (healthRes.ok) {
        setIsBackendOnline(true);
        const tasksRes = await fetch(`${API_BASE}/tasks`);
        if (tasksRes.ok) {
          const data = await tasksRes.json();
          setTasks(data);
        }
      } else {
        setIsBackendOnline(false);
      }
    } catch (err) {
      setIsBackendOnline(false);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
    const interval = setInterval(fetchTasks, 4000);
    return () => clearInterval(interval);
  }, []);

  // Crear tarea
  const handleCreateTask = async (taskData) => {
    try {
      const res = await fetch(`${API_BASE}/tasks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(taskData)
      });
      if (res.ok) {
        const newTask = await res.json();
        setTasks((prev) => [...prev, newTask]);
      }
    } catch (err) {
      console.error('Error al crear tarea:', err);
    }
  };

  // Mover tarea de columna
  const handleMoveTask = async (taskId, newColumn) => {
    // Actualización optimista de UI
    setTasks((prev) =>
      prev.map((t) => (t.id === taskId ? { ...t, column: newColumn } : t))
    );

    try {
      await fetch(`${API_BASE}/tasks/${taskId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ column: newColumn })
      });
    } catch (err) {
      console.error('Error al mover tarea:', err);
      fetchTasks(); // Revertir en caso de fallo
    }
  };

  // Eliminar tarea
  const handleDeleteTask = async (taskId) => {
    setTasks((prev) => prev.filter((t) => t.id !== taskId));

    try {
      await fetch(`${API_BASE}/tasks/${taskId}`, {
        method: 'DELETE'
      });
    } catch (err) {
      console.error('Error al eliminar tarea:', err);
      fetchTasks();
    }
  };

  const todoTasks = tasks.filter((t) => t.column === 'todo');
  const inProgressTasks = tasks.filter((t) => t.column === 'in_progress');
  const doneTasks = tasks.filter((t) => t.column === 'done');

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <header className="header">
        <div className="brand">
          <div className="brand-icon">&#9638;</div>
          <span className="brand-title">Mini Kanban</span>
        </div>

        <div className="header-actions">
          <div className="api-status">
            <span className={`status-indicator ${isBackendOnline ? 'online' : 'offline'}`}></span>
            <span>{isBackendOnline ? 'FastAPI Online (8000)' : 'Desconectado'}</span>
          </div>

          <button className="btn btn-primary" onClick={() => setIsModalOpen(true)}>
            + Nueva Tarea
          </button>
        </div>
      </header>

      <main className="board-container">
        {isLoading ? (
          <div style={{ textAlign: 'center', marginTop: '64px', color: 'var(--text-muted)' }}>
            Cargando tablero...
          </div>
        ) : (
          <div className="board-columns">
            <KanbanColumn
              columnKey="todo"
              title="To Do"
              tasks={todoTasks}
              onMove={handleMoveTask}
              onDelete={handleDeleteTask}
            />
            <KanbanColumn
              columnKey="in_progress"
              title="In Progress"
              tasks={inProgressTasks}
              onMove={handleMoveTask}
              onDelete={handleDeleteTask}
            />
            <KanbanColumn
              columnKey="done"
              title="Done"
              tasks={doneTasks}
              onMove={handleMoveTask}
              onDelete={handleDeleteTask}
            />
          </div>
        )}
      </main>

      <NewTaskModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onCreate={handleCreateTask}
      />
    </div>
  );
}
