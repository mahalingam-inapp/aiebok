# Lab 12.2 — Identity, Data, and Trust Boundaries

## Objective

Threat-model an enterprise assistant across trust boundaries.

## Prerequisites

Book [Cloud and Enterprise AI Architecture](../books/12-cloud-and-enterprise-ai-architecture/index.md), chapter 2.

## Run

```bash
python labs/1202-identity-data-and-trust-boundaries/main.py
python -m pytest labs/1202-identity-data-and-trust-boundaries/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
