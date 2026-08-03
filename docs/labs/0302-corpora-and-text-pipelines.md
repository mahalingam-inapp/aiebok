# Lab 3.2 — Corpora and Text Pipelines

## Objective

Build a normalization pipeline and test it on multilingual and adversarial text.

## Prerequisites

Book [Language and Representation](../books/03-language-and-representation/index.md), chapter 2.

## Run

```bash
python labs/0302-corpora-and-text-pipelines/main.py
python -m pytest labs/0302-corpora-and-text-pipelines/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
