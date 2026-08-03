# Lab 1.6 — Engineering with Uncertainty

## Objective

Design a decision policy for a high-cost false-positive scenario.

## Prerequisites

Book [Foundations of Intelligence](../books/01-foundations-of-intelligence/index.md), chapter 6.

## Run

```bash
python labs/0106-engineering-with-uncertainty/main.py
python -m pytest labs/0106-engineering-with-uncertainty/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
