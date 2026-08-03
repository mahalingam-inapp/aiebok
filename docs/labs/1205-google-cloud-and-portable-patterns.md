# Lab 12.5 — Google Cloud and Portable Patterns

## Objective

Map the design to Google Cloud and identify the migration boundary.

## Prerequisites

Book [Cloud and Enterprise AI Architecture](../books/12-cloud-and-enterprise-ai-architecture/index.md), chapter 5.

## Run

```bash
python labs/1205-google-cloud-and-portable-patterns/main.py
python -m pytest labs/1205-google-cloud-and-portable-patterns/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
