# Lab — Agent Loop

## Objective

Run a bounded state machine with explicit plan/act/observe steps.

## Prerequisites

- Relevant [guided book](../../docs/books/08-agent-systems/index.md) chapters
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

Treat **Agent Loop** like a mini feature: write what "done" means before you tune code.

1. Add 2–3 acceptance rows to `specs/04-agent-loop.yaml` (normal / boundary / adversarial) matching the objective: *Run a bounded state machine with explicit plan/act/observe steps*.
2. In **Cursor**, open `labs/04-agent-loop/` and ask the agent to read your spec before editing `main.py`.
3. With **OpenSpec**, run `/opsx:propose` for a change named `04-agent-loop-acceptance` and link `tasks.md` to your pytest file.

```bash
cursor labs/04-agent-loop/
python main.py && python -m pytest test_lab.py -q
```

Full tooling walkthrough: [spec-driven workflow](../../docs/getting-started/spec-driven-workflow.md).


## Tasks

1. Diagram the state transitions for the default goal.
2. Add a step limit failure and verify graceful stop.
3. Insert one invalid action and define recovery behavior.
4. Log observations to a list you can inspect after the run.

## Reflection

- What broke first when you changed inputs?
- Which simpler baseline would you compare against in a design review?

## Extensions

- Add another test to `test_lab.py`
- Link your observations to a [concept card](../../docs/concepts/index.md)
