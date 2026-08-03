# Lab 1.2 — From Symbols to Statistics

## Objective

Implement a tiny rule engine and document where it becomes brittle.

## Prerequisites

Book [Foundations of Intelligence](../books/01-foundations-of-intelligence/index.md), chapter 2.

## Run

```bash
python labs/0102-from-symbols-to-statistics/main.py
python -m pytest labs/0102-from-symbols-to-statistics/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
