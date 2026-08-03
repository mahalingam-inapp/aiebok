# Lab 4.3 — The Transformer Block

## Objective

Assemble one transformer block and test tensor shapes.

## Prerequisites

Book [Transformers and Foundation Models](../books/04-transformers-and-foundation-models/index.md), chapter 3.

## Run

```bash
python labs/0403-the-transformer-block/main.py
python -m pytest labs/0403-the-transformer-block/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
