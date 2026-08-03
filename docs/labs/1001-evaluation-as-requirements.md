# Lab 10.1 — Evaluation as Requirements

## Objective

Write a 30-case evaluation set from real workflow risks.

## Prerequisites

Book [Evaluation, Safety, and Governance](../books/10-evaluation-safety-and-governance/index.md), chapter 1.

## Run

```bash
python labs/1001-evaluation-as-requirements/main.py
python -m pytest labs/1001-evaluation-as-requirements/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
