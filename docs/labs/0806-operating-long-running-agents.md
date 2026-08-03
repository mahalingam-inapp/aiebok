# Lab 8.6 — Operating Long-Running Agents

## Objective

Create an SLO and runbook for a day-long agent workflow.

## Prerequisites

Book [Agent Systems](../books/08-agent-systems/index.md), chapter 6.

## Run

```bash
python labs/0806-operating-long-running-agents/main.py
python -m pytest labs/0806-operating-long-running-agents/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
