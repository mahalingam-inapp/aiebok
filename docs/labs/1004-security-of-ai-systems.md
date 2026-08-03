# Lab 10.4 — Security of AI Systems

## Objective

Red-team a tool-enabled assistant and document mitigations.

## Prerequisites

Book [Evaluation, Safety, and Governance](../books/10-evaluation-safety-and-governance/index.md), chapter 4.

## Run

```bash
python labs/1004-security-of-ai-systems/main.py
python -m pytest labs/1004-security-of-ai-systems/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
