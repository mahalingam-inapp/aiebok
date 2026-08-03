# Lab — Basic RAG

## Objective

Wire retrieve → context → answer stages without an external LLM API.

## Prerequisites

- Relevant [guided book](../../docs/books/06-knowledge-and-retrieval-systems/index.md) chapters
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

1. Trace retrieval scores for a query with no lexical overlap.
2. Add an abstention path when no evidence passes threshold.
3. Verify citations appear only when evidence is used.
4. Compare answer quality with k=1 vs k=2 retrieval.

## Reflection

- What broke first when you changed inputs?
- Which simpler baseline would you compare against in a design review?

## Extensions

- Add another test to `test_lab.py`
- Link your observations to a [concept card](../../docs/concepts/index.md)
