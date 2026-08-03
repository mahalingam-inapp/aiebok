# Lab 3.6 — Embedding Systems in Production

## Objective

Create a retrieval evaluation set with realistic queries and hard negatives.

## Prerequisites

Book [Language and Representation](../books/03-language-and-representation/index.md), chapter 6.

## Run

```bash
python labs/0306-embedding-systems-in-production/main.py
python -m pytest labs/0306-embedding-systems-in-production/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
