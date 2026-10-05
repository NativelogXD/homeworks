- Tasks are GitHub issues, one at a time
- Read the acceptance criteria before starting and before closing
- Commit regularly

Roles

- PM - grooms a task before anyone implements it, follows `_docs/team/pm.md`
- Engineer - implements one groomed task, follows `_docs/team/software-engineer.md`
- QA - checks the result against acceptance criteria, follows `_docs/team/qa-engineer.md`

Lifecycle

1. PM grooms the task using `_docs/task-template.md` and updates the GitHub issue
2. Engineer implements the code and writes unit tests
3. QA runs the test suite and posts a PASS/FAIL comment on the GitHub issue
4. If FAIL, Engineer addresses the feedback
5. If PASS, orchestrator closes the GitHub issue and creates a milestone commit
