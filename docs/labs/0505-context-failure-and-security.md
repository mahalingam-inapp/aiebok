# Lab 5.5 — Context Failure and Security

## Objective

Attack a context pipeline with malicious retrieved text and test defenses.

## Prerequisites

Book [Prompt and Context Engineering](../books/05-prompt-and-context-engineering/index.md), chapter 5.

## Run

```bash
python labs/0505-context-failure-and-security/main.py
python -m pytest labs/0505-context-failure-and-security/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
