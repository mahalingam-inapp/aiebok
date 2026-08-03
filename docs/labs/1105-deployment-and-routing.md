# Lab 11.5 — Deployment and Routing

## Objective

Write a deployment ADR comparing hosted and self-hosted inference.

## Prerequisites

Book [Training, Serving, and AI Operations](../books/11-training-serving-and-ai-operations/index.md), chapter 5.

## Run

```bash
python labs/1105-deployment-and-routing/main.py
python -m pytest labs/1105-deployment-and-routing/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
