# Lab 2.5 — Evaluation and Error Analysis

## Objective

Write an error taxonomy and compare two models with confidence intervals.

## Prerequisites

Book [Machine Learning Systems](../books/02-machine-learning-systems/index.md), chapter 5.

## Run

```bash
python labs/0205-evaluation-and-error-analysis/main.py
python -m pytest labs/0205-evaluation-and-error-analysis/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
