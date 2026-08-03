# Lab 10.6 — Governance and Assurance

## Objective

Create a lightweight governance operating model for a mid-size company.

## Prerequisites

- Book 10: Evaluation, Safety, and Governance, chapter 6
- Python 3.10+

## Time estimate

45–60 minutes

## Run

```bash
python main.py
python -m pytest test_lab.py -q
```

## Tasks

1. Run `main.py` and predict the output before executing.
2. Modify one line tied to the chapter mechanism; observe the change.
3. Add one boundary case and one adversarial case as code or documented input.
4. Record latency or quality notes compared to a naive baseline.

## Expected observations

Output should be non-empty and change predictably when the chapter mechanism is altered.

## Reflection

- What failure mode appeared first when you stressed the baseline?
- Which metric would you use before adding complexity?

## Extensions

- Add a second test case to `test_lab.py`
- Link results to the matching [concept card](../../docs/concepts/cards/index.md)
