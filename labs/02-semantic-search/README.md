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
