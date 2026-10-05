import React from 'react';
import TaskCard from './TaskCard';

export default function KanbanColumn({ columnKey, title, tasks, onMove, onDelete }) {
  return (
    <div className="column">
      <div className="column-header">
        <div className="column-title-group">
          <span className={`column-dot ${columnKey}`}></span>
          <span>{title}</span>
        </div>
        <span className="column-badge">{tasks.length}</span>
      </div>

      <div className="column-cards">
        {tasks.length === 0 ? (
          <div style={{ textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px', marginTop: '32px' }}>
            Sin tareas en esta columna
          </div>
        ) : (
          tasks.map((task) => (
            <TaskCard
              key={task.id}
              task={task}
              onMove={onMove}
              onDelete={onDelete}
            />
          ))
        )}
      </div>
    </div>
  );
}
