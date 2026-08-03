# Lab — Eval Harness

## Objective

Score candidate outputs with slices and a release gate.

## Prerequisites

- Relevant [guided book](../../docs/books/10-evaluation-safety-and-governance/index.md) chapters
- Python 3.10+

## Time estimate

30–45 minutes

## Run

```bash
python main.py
python -m pytest test_lab.py -q
```

## Tasks

1. Add a failing general case and observe release block.
2. Add a failing safety case and confirm it blocks release even if average score is high.
3. Define one new slice with two cases in `main.py`.
4. Document which metric you would track in production.

## Reflection

- What broke first when you changed inputs?
- Which simpler baseline would you compare against in a design review?

## Extensions

- Add another test to `test_lab.py`
- Link your observations to a [concept card](../../docs/concepts/index.md)
