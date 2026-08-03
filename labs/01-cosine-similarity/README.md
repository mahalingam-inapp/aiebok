# Lab — Cosine Similarity

## Objective

Compute cosine similarity from first principles and rank paraphrase candidates.

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

1. Predict ranked output before running `main.py`.
2. Add orthogonal and zero-vector cases to `test_lab.py`.
3. Compare cosine vs dot product on unnormalized vectors.
4. Document when magnitude should matter for your retrieval task.

## Reflection

- What broke first when you changed inputs?
- Which simpler baseline would you compare against in a design review?

## Extensions

- Add another test to `test_lab.py`
- Link your observations to a [concept card](../../docs/concepts/index.md)
