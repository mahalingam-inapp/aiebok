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

## Notebook

Open [`lab.ipynb`](lab.ipynb) for a guided, step-by-step version (sync your final code into `main.py`).

## Spec-driven habit (every lab)

Treat **Eval Harness** like a mini feature: write what "done" means before you tune code.

1. Add 2–3 acceptance rows to `specs/05-eval-harness.yaml` (normal / boundary / adversarial) matching the objective: *Score candidate outputs with slices and a release gate*.
2. In **Cursor**, open `labs/05-eval-harness/` and ask the agent to read your spec before editing `main.py`.
3. With **OpenSpec**, run `/opsx:propose` for a change named `05-eval-harness-acceptance` and link `tasks.md` to your pytest file.

```bash
cursor labs/05-eval-harness/
python main.py && python -m pytest test_lab.py -q
```

Full tooling walkthrough: [spec-driven workflow](../../docs/getting-started/spec-driven-workflow.md).


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
