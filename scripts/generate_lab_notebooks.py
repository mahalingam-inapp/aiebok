"""Generate Jupyter notebooks for starter labs.

Outputs:
- labs/<slug>/lab.ipynb — runnable notebook (clone repo, Codespaces, or local Jupyter)
- docs/labs/notebooks/index.md — links to notebook files in the repository
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
NOTEBOOKS = ROOT / "docs" / "labs" / "notebooks"

# GitHub blob links for notebooks (outside docs/ are not served by MkDocs Pages).
REPO_BLOB = "https://github.com/mahalingam-inapp/aiebok/blob/main"

STARTER_LABS = [
    ("01-cosine-similarity", "Cosine Similarity"),
    ("02-semantic-search", "Semantic Search"),
    ("03-basic-rag", "Basic RAG Stages"),
    ("04-agent-loop", "Bounded Agent Loop"),
    ("05-eval-harness", "Evaluation Harness"),
]


def notebook_cells(slug: str, title: str, readme: str, main_py: str) -> list[dict]:
    return [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"# Lab — {title}\n\n{readme.strip()}\n"],
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": main_py.strip().splitlines(keepends=True),
            "outputs": [],
            "execution_count": None,
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Next steps\n\n"
                "- Run `python -m pytest test_lab.py -q` from the lab directory.\n"
                "- Compare your predictions to actual output.\n"
                "- See the lab guide on the AIEBOK site for the full catalog.\n",
            ],
        },
    ]


def write_ipynb(slug: str, title: str) -> Path:
    lab_dir = LABS / slug
    readme = (lab_dir / "README.md").read_text(encoding="utf-8") if (lab_dir / "README.md").is_file() else ""
    main_py = (lab_dir / "main.py").read_text(encoding="utf-8")
    nb = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "cells": notebook_cells(slug, title, readme, main_py),
    }
    path = lab_dir / "lab.ipynb"
    path.write_text(json.dumps(nb, indent=2) + "\n", encoding="utf-8")
    return path


def notebook_href(slug: str) -> str:
    return f"{REPO_BLOB}/labs/{slug}/lab.ipynb"


def update_notebooks_index() -> None:
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Starter Lab Notebooks",
        "",
        "Notebooks live in the repository under `labs/` (not in the static GitHub Pages site). "
        "Clone the repo, open a Codespace, or use the Dev Container, then open the notebook path below.",
        "",
        "| Lab | Notebook in repo |",
        "|---|---|",
    ]
    for slug, title in STARTER_LABS:
        lines.append(f"| {title} | [`labs/{slug}/lab.ipynb`]({notebook_href(slug)}) |")
    (NOTEBOOKS / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_labs_index() -> None:
    index = ROOT / "docs" / "labs" / "index.md"
    lines = [
        "# Lab Guide",
        "",
        "**78 chapter labs** plus five foundational starter labs with notebooks. "
        "See [catalog.md](catalog.md) for the full list.",
        "",
        "## Starter labs (with notebooks)",
        "",
        "| Starter | Concept | Run | Notebook |",
        "|---:|---|---|---|",
    ]
    for slug, title in STARTER_LABS:
        lines.append(
            f"| {slug.split('-')[0]} | {title} | "
            f"`python labs/{slug}/main.py` | "
            f"[`labs/{slug}/lab.ipynb`]({notebook_href(slug)}) |"
        )
    text = "\n".join(lines) + "\n"
    text += """
Chapter labs follow `labs/BBCC-topic/main.py` where `BB` is book number and `CC` is chapter number.

## Lab standard

Every chapter lab includes `main.py`, `test_lab.py`, README, and a docs page aligned to the matching book chapter.
Starter labs also include `lab.ipynb` in the repository for Jupyter or Codespaces.
"""
    index.write_text(text, encoding="utf-8")


def main() -> None:
    count = 0
    for slug, title in STARTER_LABS:
        if not (LABS / slug / "main.py").is_file():
            continue
        write_ipynb(slug, title)
        count += 1
    update_notebooks_index()
    update_labs_index()
    print(f"Generated {count} starter lab notebooks.")


if __name__ == "__main__":
    main()
