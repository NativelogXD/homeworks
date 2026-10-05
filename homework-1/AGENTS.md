Commands

- `uv sync` - install dependencies
- `uv run python manage.py test` - run test suite
- `uv run python manage.py runserver` - start Django development server

Rules

- Dependencies are added in `pyproject.toml`. Do not add one without asking
- Commit regularly
- On Windows, always invoke Django commands via `uv run python manage.py` or `uv run python -m django`

Documents

- `_docs/process.md` - how work is organized
- `_docs/plan.md` - master product specification
- `_docs/task-template.md` - template for grooming issues
