# Lab 11.2 — Post-Training Methods

## Objective

Fine-tune a small model and evaluate held-out behavior.

## Prerequisites

Book [Training, Serving, and AI Operations](../books/11-training-serving-and-ai-operations/index.md), chapter 2.

## Run

```bash
python labs/1102-post-training-methods/main.py
python -m pytest labs/1102-post-training-methods/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
