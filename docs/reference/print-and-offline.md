# Print and Offline Study

AIEBOK is a **static MkDocs site** on GitHub Pages—no server-side code at runtime.

## Print the full site

Use **Print Site** in the navigation (added by the print-site plugin). It opens a print-friendly view of the current section. Your browser’s print dialog can save to PDF.

## Companion PDF

Download the generated companion PDF (books overview + glossary sample):

- [aiebok-companion.pdf](../assets/aiebok-companion.pdf)

The companion is rebuilt in CI on each deploy. It is not a full mirror of the website; use the site for labs, search, and notebooks.

## Starter lab notebooks

Repository links open in a new tab (↗). See [Hands-on start](../labs/start-here.md) for the recommended order.

| Lab | Notebook in repo |
|---|---|
| Cosine similarity | [`labs/01-cosine-similarity/lab.ipynb`](https://github.com/mahalingam-inapp/aiebok/blob/main/labs/01-cosine-similarity/lab.ipynb){target="_blank" rel="noopener"} |
| Semantic search | [`labs/02-semantic-search/lab.ipynb`](https://github.com/mahalingam-inapp/aiebok/blob/main/labs/02-semantic-search/lab.ipynb){target="_blank" rel="noopener"} |
| Basic RAG | [`labs/03-basic-rag/lab.ipynb`](https://github.com/mahalingam-inapp/aiebok/blob/main/labs/03-basic-rag/lab.ipynb){target="_blank" rel="noopener"} |
| Agent loop | [`labs/04-agent-loop/lab.ipynb`](https://github.com/mahalingam-inapp/aiebok/blob/main/labs/04-agent-loop/lab.ipynb){target="_blank" rel="noopener"} |
| Eval harness | [`labs/05-eval-harness/lab.ipynb`](https://github.com/mahalingam-inapp/aiebok/blob/main/labs/05-eval-harness/lab.ipynb){target="_blank" rel="noopener"} |

Notebooks are source files in the repository, not hosted on GitHub Pages. Clone the [repository](https://github.com/mahalingam-inapp/aiebok){target="_blank" rel="noopener"} or use Codespaces / the Dev Container (`.devcontainer/devcontainer.json` in the repository root), then open the path above in Jupyter.

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
