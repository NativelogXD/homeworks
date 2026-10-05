import React from 'react';

const COLUMN_ORDER = ['todo', 'in_progress', 'done'];

export default function TaskCard({ task, onMove, onDelete }) {
  const currentIndex = COLUMN_ORDER.indexOf(task.column);
  const canMoveLeft = currentIndex > 0;
  const canMoveRight = currentIndex < COLUMN_ORDER.length - 1;

  const formattedDate = new Date(task.created_at).toLocaleDateString(undefined, {
    month: 'short',
    day: 'numeric'
  });

  return (
    <div className="task-card">
      <div className="card-header">
        <h4 className="card-title">{task.title}</h4>
      </div>

      {task.description && (
        <p className="card-desc">{task.description}</p>
      )}

      <div className="card-footer">
        <span className="card-date">{formattedDate}</span>

        <div className="card-actions">
          {canMoveLeft && (
            <button
              className="icon-btn"
              title="Mover a la columna anterior"
              onClick={() => onMove(task.id, COLUMN_ORDER[currentIndex - 1])}
            >
              &#8592;
            </button>
          )}

          {canMoveRight && (
            <button
              className="icon-btn"
              title="Mover a la siguiente columna"
              onClick={() => onMove(task.id, COLUMN_ORDER[currentIndex + 1])}
            >
              &#8594;
            </button>
          )}

          <button
            className="icon-btn delete"
            title="Eliminar tarjeta"
            onClick={() => onDelete(task.id)}
          >
            &#128465;
          </button>
        </div>
      </div>
    </div>
  );
}
