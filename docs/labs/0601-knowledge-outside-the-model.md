# Lab 6.1 — Knowledge Outside the Model

## Objective

Classify ten requirements by the correct knowledge mechanism.

## Prerequisites

Book [Knowledge and Retrieval Systems](../books/06-knowledge-and-retrieval-systems/index.md), chapter 1.

## Run

```bash
python labs/0601-knowledge-outside-the-model/main.py
python -m pytest labs/0601-knowledge-outside-the-model/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
