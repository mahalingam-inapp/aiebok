# Lab 5.6 — Prompt and Context Operations

## Objective

Create a prompt change report with before/after evals.

## Prerequisites

Book [Prompt and Context Engineering](../books/05-prompt-and-context-engineering/index.md), chapter 6.

## Run

```bash
python labs/0506-prompt-and-context-operations/main.py
python -m pytest labs/0506-prompt-and-context-operations/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
