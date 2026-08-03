# Lab 8.3 — Agent Memory and Recovery

## Objective

Persist and resume an interrupted multi-step run.

## Prerequisites

Book [Agent Systems](../books/08-agent-systems/index.md), chapter 3.

## Run

```bash
python labs/0803-agent-memory-and-recovery/main.py
python -m pytest labs/0803-agent-memory-and-recovery/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
