"""Generate Jupyter notebooks and static HTML exports for starter labs.

Outputs:
- labs/<slug>/lab.ipynb — runnable notebook (GitHub / Codespaces / local)
- docs/labs/notebooks/<slug>.html — static HTML for GitHub Pages (no Jupyter server)
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
NOTEBOOKS = ROOT / "docs" / "labs" / "notebooks"

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
                "- See the [lab guide](../index.md) for the full catalog.\n",
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


def export_html(ipynb: Path, slug: str) -> None:
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
    out = NOTEBOOKS / f"{slug}.html"
    subprocess.run(
        [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "html",
            "--output",
            str(out.with_suffix("")),
            str(ipynb),
        ],
        check=True,
        capture_output=True,
        text=True,
    )


def update_notebooks_index() -> None:
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Starter Lab Notebooks",
        "",
        "Static HTML exports for GitHub Pages (no Jupyter server required). "
        "Download `.ipynb` from each lab directory under `labs/` for interactive use.",
        "",
    ]
    for slug, title in STARTER_LABS:
        lines.append(f"- [{title}]({slug}.html) — also `labs/{slug}/lab.ipynb`")
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
            f"[HTML](notebooks/{slug}.html) · "
            f"`labs/{slug}/lab.ipynb` |"
        )
    # Fix github link - use relative path to repo instead
    text = "\n".join(lines) + "\n"
    text += """
Chapter labs follow `labs/BBCC-topic/main.py` where `BB` is book number and `CC` is chapter number.

## Lab standard

Every chapter lab includes `main.py`, `test_lab.py`, README, and a docs page aligned to the matching book chapter.
Starter labs add `lab.ipynb` plus a static HTML export for browser viewing on GitHub Pages.
"""
    index.write_text(text, encoding="utf-8")


def main() -> None:
    count = 0
    for slug, title in STARTER_LABS:
        if not (LABS / slug / "main.py").is_file():
            continue
        ipynb = write_ipynb(slug, title)
        export_html(ipynb, slug)
        count += 1
    update_notebooks_index()
    update_labs_index()
    print(f"Generated {count} starter lab notebooks and HTML exports.")


if __name__ == "__main__":
    main()
