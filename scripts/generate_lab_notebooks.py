"""Generate starter notebooks and downloadable technical course workbooks."""
from __future__ import annotations

import json
from pathlib import Path

from applied_courses import APPLIED_COURSES
from course_catalog import TECHNICAL_COURSES
from generate_books import BOOKS, SAMPLE_FILES, course_slug
from generate_expansion import lab_slug
from generate_maturity_content import STARTER_LABS
from lab_notebook_templates import BUILDERS, _code, _md

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
NOTEBOOKS = ROOT / "docs" / "labs" / "notebooks"
COURSE_NOTEBOOKS = ROOT / "docs" / "assets" / "notebooks"

REPO_BLOB = "https://github.com/mahalingam-inapp/aiebok/blob/main"
REPO_ROOT = "https://github.com/mahalingam-inapp/aiebok"


def repo_link(label: str, url: str) -> str:
    """Markdown link that opens the repository in a new tab (attr_list + site JS)."""
    return f'[{label}]({url}){{target="_blank" rel="noopener"}}'


def write_ipynb(path: Path, cells: list[dict]) -> None:
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
        "cells": [
            {"id": f"cell-{number:02d}", **cell}
            for number, cell in enumerate(cells, 1)
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(nb, indent=2) + "\n", encoding="utf-8")


def write_course_notebooks() -> None:
    for number, (book, course, sample) in enumerate(zip(BOOKS, TECHNICAL_COURSES, SAMPLE_FILES, strict=True), 1):
        slug = course_slug(number, book["title"])
        cells = [
            _md(
                f"# Course notebook — {book['title']}\n\n"
                f"{book['goal']}\n\n"
                "Use Python 3.10 or later. All inputs are included and the workbook runs without API keys. "
                "Each lecture demonstration is a small model of the lecture mechanism. "
                "Run it, compare the result with your prediction, and use the section checkpoint to record what you learned."
            )
        ]
        for section, (title, check) in enumerate(zip(course.sections, course.checks, strict=True)):
            cells.append(_md(f"## {title}"))
            start = section * 2
            for lecture, chapter in enumerate(book["chapters"][start:start + 2], start + 1):
                title, summary, _, practice, principle = chapter
                lab = LABS / lab_slug(number, lecture, title) / "main.py"
                cells.extend([
                    _md(
                        f"### Lecture {lecture:02d} · {title}\n\n{summary}\n\n"
                        f"**Predict before running.** {principle} Identify one input that influences the printed result. "
                        "Change that input, rerun the cell, and explain the difference.\n\n"
                        f"**Apply the concept.** {practice}"
                    ),
                    _code(lab.read_text(encoding="utf-8")),
                ])
            cells.append(_md(f"**Section checkpoint.** {check}"))

        implementation = (ROOT / "docs" / "code-samples" / sample).read_text(encoding="utf-8").splitlines()
        # CLI examples use an exit status to signal failure. Let a notebook report an assertion instead.
        if implementation[-1].startswith("raise SystemExit("):
            status = implementation[-1].removeprefix("raise SystemExit(").removesuffix(")")
            implementation[-1] = f"assert ({status}) == 0"
        cells.extend([
            _md(f"## Course workshop\n\n{course.experiment}\n\nRun the reference implementation, then run the checks below it."),
            _code("\n".join(implementation)),
            _md("### Verify and extend\n\nRun the assertions. Then change one assumption and add a check for the predicted behavior."),
            _code(course.verification.strip() + "\nprint('Workshop checks passed')"),
        ])
        if course.applied:
            exercise = course.applied
            cells.extend([
                _md(f"## Applied exercise for Lecture {exercise.lecture:02d} — {exercise.title}\n\n{exercise.instructions}"),
                _code(exercise.code.strip()),
            ])
        cells.extend([
            _md(
                f"## Course project\n\n{book['project']}\n\n"
                "Keep your baseline, results, and one failure case so someone else can review the decision you made."
            ),
        ])
        write_ipynb(COURSE_NOTEBOOKS / f"{slug}.ipynb", cells)


def notebook_href(slug: str) -> str:
    return f"{REPO_BLOB}/labs/{slug}/lab.ipynb"


def write_practicum_notebooks() -> None:
    for course in APPLIED_COURSES:
        source = ROOT / "scripts" / "practicum_examples" / f"{course.slug}.py"
        examples = iter(source.read_text(encoding="utf-8").split("\n# %%\n"))
        cells = [
            _md(f"# {course.title}\n\n{course.goal}\n\n"
                "Run the lecture cells in sequence with Python 3.10 or later. "
                "The default exercises use bundled data and require no model account.")
        ]
        number = 0
        for section, lectures in course.sections:
            cells.append(_md(f"## {section}"))
            for lecture in lectures:
                number += 1
                cells.extend([
                    _md(f"### Lecture {number:02d} · {lecture.title}\n\n"
                        f"{lecture.outcome}\n\n{lecture.practice}"),
                    _code(next(examples).strip()),
                    _md(f"**Compare your result**\n\n{lecture.answer}"),
                ])
        if next(examples, None) is not None:
            raise ValueError(f"{course.slug} has more code blocks than lectures.")
        cells.append(_md(f"## Course project\n\n{course.project}\n\n{course.standard}"))
        write_ipynb(COURSE_NOTEBOOKS / f"{course.slug}.ipynb", cells)


def update_notebooks_index() -> None:
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Jupyter Notebooks",
        "",
        "Each technical course has a downloadable workbook with lecture demonstrations and a checked course workshop. "
        "The workbooks contain their own sample data and can run outside the repository.",
        "",
        "## Set up Jupyter",
        "",
        f"1. Clone the {repo_link('repository', REPO_ROOT)} and create a Python virtual environment, "
        "or reopen the project in its Dev Container.",
        "2. In the activated environment, run `python -m pip install -r requirements-notebooks.txt`.",
        "3. Run `jupyter lab`, open the downloaded notebook, and choose the Python 3 kernel. "
        "Use **Restart Kernel and Run All Cells** to check the initial results.",
        "",
        "## Project practicum workbooks",
        "",
        "| Practicum | Notebook |",
        "|---|---|",
    ]
    for course in APPLIED_COURSES:
        lines.append(f"| [{course.title}](../../courses/{course.slug}/index.md) | [Download](../../assets/notebooks/{course.slug}.ipynb){{ download }} |")
    lines.extend([
        "",
        "## Technical core workbooks",
        "",
        "| Course | Notebook |",
        "|---|---|",
    ])
    for number, book in enumerate(BOOKS, 1):
        title = book["title"]
        slug = course_slug(number, title)
        lines.append(f"| [{title}](../../books/{slug}/index.md) | [Download](../../assets/notebooks/{slug}.ipynb){{ download }} |")
    lines.extend([
        "",
        "## Starter lab notebooks",
        "",
        "The starter labs use the companion Python tests in the repository. "
        "Follow [Hands-on Start](../start-here.md) and run the kernel from the repo root or the lab folder.",
        "",
        "| Lab | Notebook in repo |",
        "|---|---|",
    ])
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
        "Browse [course workbooks and Jupyter setup](notebooks/index.md), or use the [lab catalog](catalog.md) for individual lecture scripts.",
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
    for slug, *_ in STARTER_LABS:
        if slug not in BUILDERS or not (LABS / slug / "main.py").is_file():
            raise ValueError(f"Missing starter lab or notebook template: {slug}")
        write_ipynb(LABS / slug / "lab.ipynb", BUILDERS[slug]())
        count += 1
    write_course_notebooks()
    write_practicum_notebooks()
    update_notebooks_index()
    update_labs_index()
    print(f"Generated {len(TECHNICAL_COURSES) + len(APPLIED_COURSES)} course workbooks and {count} starter lab notebooks.")


if __name__ == "__main__":
    main()
