## Spec-driven workflow

1. Read `specs/` or active `openspec/changes/<id>/` before coding.
2. Use **Cursor Plan** mode to review acceptance cases with the agent.
3. With **OpenSpec**: `/opsx:explore` → `/opsx:propose` → review → `/opsx:apply` → `/opsx:archive`.
4. Verify: `python -m pytest test_lab.py -q` (or project test command).

See [spec-driven workflow](docs/getting-started/spec-driven-workflow.md).
