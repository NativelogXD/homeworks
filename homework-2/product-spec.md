# Product Specification: Mini Kanban Board

## 1. Overview
A lightweight, responsive, full-stack Kanban board application (`mini-kanban`) for visual task management.

## 2. Target Users & User Stories
- **As a user**, I want to see three distinct workflow columns: **To Do**, **In Progress**, and **Done**.
- **As a user**, I want to quickly add a new task with a title, description, and optional priority.
- **As a user**, I want to move a task easily between columns (e.g. To Do ➔ In Progress ➔ Done).
- **As a user**, I want to edit task details or delete tasks that are no longer needed.
- **As a user**, I want my tasks to persist in a database (SQLite) so my board retains its state across browser refreshes and server restarts.

## 3. Acceptance Criteria (Functional Requirements)
1. **Board Structure:** Always displays the three core Kanban columns:
   - `todo`: Tasks waiting to be started.
   - `in_progress`: Tasks currently being worked on.
   - `done`: Completed tasks.
2. **Task Creation:** Modal or inline form allowing users to submit a new task (validation: title is required, max 100 characters).
3. **Column Transition:** Buttons or drag-and-drop to update a task's status column.
4. **Data Persistence:** All CRUD operations are saved in a local SQLite database via FastAPI.
5. **Contract Adherence:** All HTTP operations strictly follow `openapi.yaml`.

## 4. Non-Goals (Out of Scope for MVP)
- User login / password authentication (single default board).
- File attachments or rich text markdown formatting in cards.
- Automated email notifications.
