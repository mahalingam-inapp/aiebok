# Lab 7.5 — MCP and Integration Protocols

## Objective

Implement a small local MCP server and test a hostile client request.

## Prerequisites

- Book 7: Reasoning and Tool Use, chapter 5
- Python 3.10+

## Time estimate

45–60 minutes

## Run

```bash
python main.py
python -m pytest test_lab.py -q
```

## Spec-driven habit (every lab)

Specification-driven development means **executable acceptance before implementation**—the same discipline whether you use [OpenSpec](https://openspec.dev/) in the repo or [Cursor](https://cursor.com/) in the editor.

1. **Write cases first** — Before changing `main.py`, write **three acceptance cases** for *MCP and Integration Protocols* (normal, boundary, adversarial) in `specs/lab-0705.yaml` or as pytest cases in `test_lab.py`. Goal: Implement a small local MCP server and test a hostile client request.
2. **Review the spec** — share `specs/` or your test list with a teammate or agent *before* large diffs.
3. **Implement to green** — run `python main.py` and `pytest test_lab.py -q`; spec failures block "done".

### Cursor (editor workflow)

```bash
# From repo root — open the lab folder with spec context
cursor labs/0705-*/
```

In Cursor **Agent** or **Plan** mode, paste a spec-first prompt:

```text
Read specs/lab-0705.yaml (or test_lab.py cases).
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
/opsx:propose Add acceptance spec for lab 7.5 — MCP and Integration Protocols
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
python -m pytest labs/0705-*/test_lab.py -q
/opsx:archive
```

See the full [spec-driven workflow guide](../../docs/getting-started/spec-driven-workflow.md) for copy-paste templates.


## Tasks

1. Run `main.py` and predict the output before executing.
2. Modify one line tied to the chapter mechanism; observe the change.
3. Add one boundary case and one adversarial case as code or documented input.
4. Record latency or quality notes compared to a naive baseline.

## Expected observations

Output should be non-empty and change predictably when the chapter mechanism is altered.

## Reflection

- What failure mode appeared first when you stressed the baseline?
- Which metric would you use before adding complexity?

## Extensions

- Add a second test case to `test_lab.py`
- Link results to the matching [concept card](../../docs/concepts/cards/index.md)
