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

## Spec-driven habit (every lab)

Treat **Basic RAG** like a mini feature: write what "done" means before you tune code.

1. Add 2–3 acceptance rows to `specs/03-basic-rag.yaml` (normal / boundary / adversarial) matching the objective: *Wire retrieve → context → answer stages without an external LLM API*.
2. In **Cursor**, open `labs/03-basic-rag/` and ask the agent to read your spec before editing `main.py`.
3. With **OpenSpec**, run `/opsx:propose` for a change named `03-basic-rag-acceptance` and link `tasks.md` to your pytest file.

```bash
cursor labs/03-basic-rag/
python main.py && python -m pytest test_lab.py -q
```

Full tooling walkthrough: [spec-driven workflow](../../docs/getting-started/spec-driven-workflow.md).


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
