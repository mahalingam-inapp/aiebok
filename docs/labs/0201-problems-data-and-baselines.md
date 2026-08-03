# Lab 2.1 — Problems, Data, and Baselines

## Objective

Create a dataset split that respects time and entity boundaries.

## Prerequisites

Book [Machine Learning Systems](../books/02-machine-learning-systems/index.md), chapter 1.

## Run

```bash
python labs/0201-problems-data-and-baselines/main.py
python -m pytest labs/0201-problems-data-and-baselines/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
