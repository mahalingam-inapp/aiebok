# Lab 2.6 — The ML Lifecycle

## Objective

Write a release checklist and a rollback plan for a prediction service.

## Prerequisites

Book [Machine Learning Systems](../books/02-machine-learning-systems/index.md), chapter 6.

## Run

```bash
python labs/0206-the-ml-lifecycle/main.py
python -m pytest labs/0206-the-ml-lifecycle/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
