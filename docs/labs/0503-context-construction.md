# Lab 5.3 — Context Construction

## Objective

Implement a context builder with explicit section budgets.

## Prerequisites

Book [Prompt and Context Engineering](../books/05-prompt-and-context-engineering/index.md), chapter 3.

## Run

```bash
python labs/0503-context-construction/main.py
python -m pytest labs/0503-context-construction/test_lab.py -q
```

## Spec-driven habit (every lab)

Specification-driven development means **executable acceptance before implementation**—the same discipline whether you use [OpenSpec](https://openspec.dev/) in the repo or [Cursor](https://cursor.com/) in the editor.

1. **Write cases first** — Before changing `main.py`, write **three acceptance cases** for *Context Construction* (normal, boundary, adversarial) in `specs/lab-0503.yaml` or as pytest cases in `test_lab.py`. Goal: Implement a context builder with explicit section budgets.
2. **Review the spec** — share `specs/` or your test list with a teammate or agent *before* large diffs.
3. **Implement to green** — run `python main.py` and `pytest test_lab.py -q`; spec failures block "done".

### Cursor (editor workflow)

```bash
# From repo root — open the lab folder with spec context
cursor labs/0503-*/
```

In Cursor **Agent** or **Plan** mode, paste a spec-first prompt:

```text
Read specs/lab-0503.yaml (or test_lab.py cases).
Do not change main.py until we agree the acceptance cases cover normal, boundary, and adversarial inputs.
Then implement the smallest diff that makes pytest pass.
```

Optional project rules (`.cursor/rules/spec-driven-labs.mdc`):

```markdown
---
description: Spec-first lab workflow
globs: labs/**
---
- Read acceptance cases before editing main.py
- Add a failing test before fixing behavior
- Run: python -m pytest test_lab.py -q
```

### OpenSpec (repo workflow)

```bash
npm install -g @fission-ai/openspec@latest   # Node 20.19+
cd your-project
openspec init                              # creates openspec/specs/ + openspec/changes/
```

Propose a lab-scoped change (names vary slightly by assistant profile):

```text
/opsx:propose Add acceptance spec for lab 5.3 — Context Construction
```

Typical artifacts under `openspec/changes/<change-id>/`:

```text
proposal.md    # intent and scope
tasks.md       # checkbox implementation list
specs/         # ADDED/MODIFIED requirements (delta specs)
design.md      # optional technical notes
```

Apply after review:

```text
/opsx:apply
python -m pytest labs/0503-*/test_lab.py -q
/opsx:archive
```

See the full [spec-driven workflow guide](../getting-started/spec-driven-workflow.md) for copy-paste templates.


## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
