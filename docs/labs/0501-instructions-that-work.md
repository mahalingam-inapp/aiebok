# Lab 5.1 — Instructions That Work

## Objective

Solve one task with weak and strong prompts and compare failures.

## Prerequisites

Book [Prompt and Context Engineering](../books/05-prompt-and-context-engineering/index.md), chapter 1.

## Run

```bash
python labs/0501-instructions-that-work/main.py
python -m pytest labs/0501-instructions-that-work/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
