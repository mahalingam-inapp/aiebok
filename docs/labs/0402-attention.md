# Lab 4.2 — Attention

## Objective

Implement scaled dot-product attention and visualize weights.

## Prerequisites

Book [Transformers and Foundation Models](../books/04-transformers-and-foundation-models/index.md), chapter 2.

## Run

```bash
python labs/0402-attention/main.py
python -m pytest labs/0402-attention/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
