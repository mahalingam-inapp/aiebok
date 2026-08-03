# Lab 8.2 — The Agent Loop

## Objective

Extend the included agent loop with failures and checkpointing.

## Prerequisites

Book [Agent Systems](../books/08-agent-systems/index.md), chapter 2.

## Run

```bash
python labs/0802-the-agent-loop/main.py
python -m pytest labs/0802-the-agent-loop/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
