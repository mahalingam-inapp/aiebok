# Print and Offline Study

AIEBOK is a **static MkDocs site** on GitHub Pages—no server-side code at runtime.

## Print the full site

Use **Print Site** in the navigation (added by the print-site plugin). It opens a print-friendly view of the current section. Your browser’s print dialog can save to PDF.

## Companion PDF

Download the generated companion PDF (books overview + glossary sample):

- [aiebok-companion.pdf](../assets/aiebok-companion.pdf)

The companion is rebuilt in CI on each deploy. It is not a full mirror of the website; use the site for labs, search, and notebooks.

## Starter lab notebooks

| Lab | Static HTML (Pages) | Notebook source |
|---|---|---|
| Cosine similarity | [HTML](../labs/notebooks/01-cosine-similarity.html) | `labs/01-cosine-similarity/lab.ipynb` |
| Semantic search | [HTML](../labs/notebooks/02-semantic-search.html) | `labs/02-semantic-search/lab.ipynb` |
| Basic RAG | [HTML](../labs/notebooks/03-basic-rag.html) | `labs/03-basic-rag/lab.ipynb` |
| Agent loop | [HTML](../labs/notebooks/04-agent-loop.html) | `labs/04-agent-loop/lab.ipynb` |
| Eval harness | [HTML](../labs/notebooks/05-eval-harness.html) | `labs/05-eval-harness/lab.ipynb` |

Static HTML needs no Jupyter server on GitHub Pages. Run notebooks locally, in Codespaces, or via the Dev Container (`.devcontainer/devcontainer.json` in the repository root).

## GitHub Codespaces / Dev Container

Open the repository in Codespaces or VS Code Dev Containers. The container installs Python dependencies and Jupyter support. Then:

```bash
mkdocs serve
jupyter lab labs/01-cosine-similarity/lab.ipynb
```

## What GitHub Pages does not run

- Python labs (run locally or in CI only)
- Jupyter kernels
- Database or vector index services

Design labs to use dependency-light `main.py` scripts, which keeps the static site portable.
