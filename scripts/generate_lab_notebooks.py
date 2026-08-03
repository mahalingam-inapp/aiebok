"""Generate Jupyter notebooks for starter labs.

Outputs:
- labs/<slug>/lab.ipynb — guided notebook (clone repo, Codespaces, or local Jupyter)
- docs/labs/notebooks/index.md — links to notebook files in the repository
"""
from __future__ import annotations

import json
from pathlib import Path

from lab_notebook_templates import BUILDERS
from generate_maturity_content import STARTER_LABS

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
NOTEBOOKS = ROOT / "docs" / "labs" / "notebooks"

REPO_BLOB = "https://github.com/mahalingam-inapp/aiebok/blob/main"
REPO_ROOT = "https://github.com/mahalingam-inapp/aiebok"


def repo_link(label: str, url: str) -> str:
    """Markdown link that opens the repository in a new tab (attr_list + site JS)."""
    return f'[{label}]({url}){{target="_blank" rel="noopener"}}'


def write_ipynb(slug: str, title: str) -> Path:
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
        "cells": BUILDERS[slug](),
    }
    path = LABS / slug / "lab.ipynb"
    path.write_text(json.dumps(nb, indent=2) + "\n", encoding="utf-8")
    return path


def notebook_href(slug: str) -> str:
    return f"{REPO_BLOB}/labs/{slug}/lab.ipynb"


def update_notebooks_index() -> None:
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Starter Lab Notebooks",
        "",
        "Guided notebooks live in the repository under `labs/` (not on the static GitHub Pages site). "
        "Clone the "
        + repo_link("repository", REPO_ROOT)
        + ", open a Codespace, or use the Dev Container, "
        "then open the notebook path below.",
        "",
        "!!! tip \"New here?\"",
        "    Follow the [hands-on start](../start-here.md) page for the recommended lab order.",
        "",
        "| Lab | Notebook in repo |",
        "|---|---|",
    ]
    for slug, title, *_ in STARTER_LABS:
        path = f"labs/{slug}/lab.ipynb"
        lines.append(f"| {title} | {repo_link(f'`{path}`', notebook_href(slug))} |")
    (NOTEBOOKS / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_labs_index() -> None:
    index = ROOT / "docs" / "labs" / "index.md"
    lines = [
        "# Lab Guide",
        "",
        "**New?** Start with **[Hands-on start](start-here.md)** — five starter labs in order with book chapters and notebook links.",
        "",
        "**78 chapter labs** plus five foundational starter labs with notebooks. "
        "See [catalog.md](catalog.md) for the full list.",
        "",
        "## Starter labs (with notebooks)",
        "",
        "| Starter | Concept | Run | Notebook |",
        "|---:|---|---|---|",
    ]
    for slug, title, *_ in STARTER_LABS:
        path = f"labs/{slug}/lab.ipynb"
        lines.append(
            f"| {slug.split('-')[0]} | {title} | "
            f"`python labs/{slug}/main.py` | "
            f"{repo_link(f'`{path}`', notebook_href(slug))} |"
        )
    text = "\n".join(lines) + "\n"
    text += """
Chapter labs follow `labs/BBCC-topic/main.py` where `BB` is book number and `CC` is chapter number.

## Lab standard

Every chapter lab includes `main.py`, `test_lab.py`, README, and a docs page aligned to the matching book chapter.
Starter labs add a guided `lab.ipynb` in the repository for Jupyter or Codespaces.
"""
    index.write_text(text, encoding="utf-8")


def main() -> None:
    count = 0
    for slug, title, *_ in STARTER_LABS:
        if slug not in BUILDERS or not (LABS / slug / "main.py").is_file():
            continue
        write_ipynb(slug, title)
        count += 1
    update_notebooks_index()
    update_labs_index()
    print(f"Generated {count} starter lab notebooks.")


if __name__ == "__main__":
    main()
