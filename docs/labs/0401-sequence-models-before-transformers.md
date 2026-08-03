# Lab 4.1 — Sequence Models Before Transformers

## Objective

Train an n-gram model and inspect where local context fails.

## Prerequisites

Book [Transformers and Foundation Models](../books/04-transformers-and-foundation-models/index.md), chapter 1.

## Run

```bash
python labs/0401-sequence-models-before-transformers/main.py
python -m pytest labs/0401-sequence-models-before-transformers/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
