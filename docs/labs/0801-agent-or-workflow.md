# Lab 8.1 — Agent or Workflow?

## Objective

Model the same task as a workflow and as an agent, then compare.

## Prerequisites

Book [Agent Systems](../books/08-agent-systems/index.md), chapter 1.

## Run

```bash
python labs/0801-agent-or-workflow/main.py
python -m pytest labs/0801-agent-or-workflow/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
