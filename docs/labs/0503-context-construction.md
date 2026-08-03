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

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
