# Lab 7.4 — Tools as Capability Boundaries

## Objective

Wrap a read-only API as a typed tool and fuzz its arguments.

## Prerequisites

Book [Reasoning and Tool Use](../books/07-reasoning-and-tool-use/index.md), chapter 4.

## Run

```bash
python labs/0704-tools-as-capability-boundaries/main.py
python -m pytest labs/0704-tools-as-capability-boundaries/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
