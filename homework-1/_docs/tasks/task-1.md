# Task 1: Setup project and base models with a passing test

## Goal
Bootstrap the Django project with SQLite, configure the `chores` application, define the `FamilyMember` and `Chore` models with migrations, and establish automated unit tests that verify model creation and string representations.

## Acceptance criteria
- [ ] Django project is initialized with settings configured, SQLite database enabled, and `chores` registered in `INSTALLED_APPS`.
- [ ] `FamilyMember` model exists with fields `name` (CharField) and `role` (CharField), and its `__str__` method returns the name.
- [ ] `Chore` model exists with fields `title` (CharField), `assigned_to` (ForeignKey to FamilyMember), `day_of_week` (choices Monday through Sunday), and `is_completed` (BooleanField, default False).
- [ ] Initial database migration exists in `chores/migrations/` and applies cleanly with `uv run python manage.py migrate`.
- [ ] Automated tests in `chores/tests.py` test `FamilyMember` creation, `Chore` creation, and `__str__` methods, passing cleanly with `uv run python manage.py test`.

## Out of scope
- Web views, templates, or HTML UI (deferred to issues #2, #3, #4).
- User login, authentication sessions, or passwords.

## Constraints
- Scope limited to `config/`, `chores/`, `pyproject.toml`, and `.gitignore`.
- Use `uv` for package management (`uv add django`).
- On Windows, always invoke Django commands via `uv run python manage.py` or `uv run python -m django`.
