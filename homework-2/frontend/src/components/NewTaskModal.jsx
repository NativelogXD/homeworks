import React, { useState } from 'react';

export default function NewTaskModal({ isOpen, onClose, onCreate }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [column, setColumn] = useState('todo');
  const [isSubmitting, setIsSubmitting] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title.trim()) return;

    setIsSubmitting(true);
    await onCreate({
      title: title.trim(),
      description: description.trim(),
      column
    });
    setIsSubmitting(false);
    setTitle('');
    setDescription('');
    setColumn('todo');
    onClose();
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h3 className="modal-title">Nueva Tarjeta Kanban</h3>
          <button className="icon-btn" onClick={onClose}>&times;</button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label">Título *</label>
            <input
              type="text"
              className="form-input"
              placeholder="Ej. Configurar base de datos SQLite"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
              autoFocus
            />
          </div>

          <div className="form-group">
            <label className="form-label">Descripción</label>
            <textarea
              className="form-textarea"
              rows={3}
              placeholder="Detalles adicionales o criterios de aceptación..."
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label className="form-label">Columna Inicial</label>
            <select
              className="form-select"
              value={column}
              onChange={(e) => setColumn(e.target.value)}
            >
              <option value="todo">To Do</option>
              <option value="in_progress">In Progress</option>
              <option value="done">Done</option>
            </select>
          </div>

          <div className="modal-footer">
            <button type="button" className="btn" style={{ background: 'transparent', color: 'var(--text-secondary)' }} onClick={onClose}>
              Cancelar
            </button>
            <button type="submit" className="btn btn-primary" disabled={isSubmitting}>
              {isSubmitting ? 'Guardando...' : 'Crear Tarjeta'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
