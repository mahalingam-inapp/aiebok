# Lab — Semantic Search

## Objective

Build a hashing-vector search pipeline over a tiny document set.

## Prerequisites

- Relevant [guided book](../../docs/books/03-language-and-representation/index.md) chapters
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

Treat **Semantic Search** like a mini feature: write what "done" means before you tune code.

1. Add 2–3 acceptance rows to `specs/02-semantic-search.yaml` (normal / boundary / adversarial) matching the objective: *Build a hashing-vector search pipeline over a tiny document set*.
2. In **Cursor**, open `labs/02-semantic-search/` and ask the agent to read your spec before editing `main.py`.
3. With **OpenSpec**, run `/opsx:propose` for a change named `02-semantic-search-acceptance` and link `tasks.md` to your pytest file.

```bash
cursor labs/02-semantic-search/
python main.py && python -m pytest test_lab.py -q
```

Full tooling walkthrough: [spec-driven workflow](../../docs/getting-started/spec-driven-workflow.md).


## Tasks

1. Inspect token buckets and explain why paraphrases score higher than unrelated docs.
2. Add a hard-negative document that shares tokens but wrong intent.
3. Measure recall@1 on five hand-written queries.
4. List what breaks if you change embedding dimensions.

## Reflection

- What broke first when you changed inputs?
- Which simpler baseline would you compare against in a design review?

## Extensions

- Add another test to `test_lab.py`
- Link your observations to a [concept card](../../docs/concepts/index.md)
