"""Generate starter notebooks and downloadable technical course workbooks."""
from __future__ import annotations

import json
from pathlib import Path

from applied_courses import APPLIED_COURSES
from chapter_catalog import get_knowledge_check, get_worked_example
from course_catalog import TECHNICAL_COURSES
from generate_books import BOOKS, SAMPLE_FILES, WORKED_SCENARIOS, course_slug
from generate_expansion import lab_slug
from generate_maturity_content import STARTER_LABS
from lab_notebook_templates import BUILDERS, _code, _md, cells_for
from lecture_cases import CASES, lecture_case
from textbook_readings import READINGS
from topic_knowledge import get_topic_entry

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
NOTEBOOKS = ROOT / "docs" / "labs" / "notebooks"
COURSE_NOTEBOOKS = ROOT / "docs" / "assets" / "notebooks"
CASE_NOTEBOOK = COURSE_NOTEBOOKS / "undercover-harness.ipynb"

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
        case = CASES[number]
        cells.append(_md(f"## Practice case · {case.title}\n\n{case.opening}\n\nThe workplace scenario is fictional."))
        for section, (title, check) in enumerate(zip(course.sections, course.checks, strict=True)):
            cells.append(_md(f"## {title}"))
            start = section * 2
            for lecture, chapter in enumerate(book["chapters"][start:start + 2], start + 1):
                title, summary, topics, practice, principle = chapter
                lab = LABS / lab_slug(number, lecture, title) / "main.py"
                concepts = "\n\n".join(
                    "\n\n".join((f"**{topic}**", *get_topic_entry(topic)[:2]))
                    for topic in topics
                )
                example = get_worked_example(number, lecture, title, summary, topics, WORKED_SCENARIOS[number - 1])
                question, diagnosis, baseline, answer = get_knowledge_check(number, lecture, topics)
                cells.extend([
                    _md(
                        f"### Lecture {lecture:02d} · {title}\n\n{summary}\n\n"
                        f"{lecture_case(number, lecture, level=4)}\n\n"
                        f"#### Read the mechanism\n\n{concepts}\n\n"
                        f"#### Worked example\n\n{example}\n\n"
                        f"**Predict before running.** {principle} Identify the input you would hold fixed and the observation that would change your decision."
                    ),
                    _code(lab.read_text(encoding="utf-8")),
                    _md(
                        f"#### Interpret and apply\n\n{practice}\n\n"
                        "Change one input, record the prediction before running again, and compare with the unchanged output. "
                        "If a result disappoints, record which intermediate stage first diverged.\n\n"
                        f"1. {question}\n2. {diagnosis}\n3. {baseline}\n\n"
                        f"<details><summary>Check your reasoning</summary>\n\n{answer}\n\n</details>"
                    ),
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
        case = CASES[course.slug]
        cells.append(_md(f"## Practice case · {case.title}\n\n{case.opening}\n\nThe workplace scenario is fictional."))
        number = 0
        for section, lectures in course.sections:
            cells.append(_md(f"## {section}"))
            for lecture in lectures:
                number += 1
                cells.extend([
                    _md(f"### Lecture {number:02d} · {lecture.title}\n\n"
                        f"{lecture.outcome}\n\n{lecture_case(course.slug, number, level=4)}\n\n"
                        f"#### How it works\n\n{lecture.explanation}\n\n##{READINGS[course.slug][number - 1]}\n\n"
                        f"#### Worked example\n\n{lecture.example}\n\n"
                        f"#### Try it\n\n{lecture.practice}"),
                    _code(next(examples).strip()),
                    _md(f"**Compare your result**\n\n{lecture.answer}"),
                ])
        if next(examples, None) is not None:
            raise ValueError(f"{course.slug} has more code blocks than lectures.")
        cells.append(_md(f"## Course project\n\n{course.project}\n\n{course.standard}"))
        write_ipynb(COURSE_NOTEBOOKS / f"{course.slug}.ipynb", cells)


def write_claims_notebook() -> None:
    script = (LABS / "undercover-harness" / "main.py").read_text(encoding="utf-8")
    setup, _, rest = script.partition("\ndef checkpoint(")
    persistence, _, fixtures = rest.partition("\n# Keep these expectations")
    evaluation, _, _ = fixtures.partition("\ndef main()")
    write_ipynb(CASE_NOTEBOOK, [
        _md("# UnderCover-inspired claims harness\n\n"
            "A fictional adjuster needs to decide what evidence to ask for after a travel delay. "
            "The policy in force on the incident date supplies the evidence requirements. "
            "This local exercise uses Python and SQLite 3.35 or later. All claims and policies are synthetic."),
        _md("## Propose the next step\n\n"
            "The agent has one typed policy lookup. The harness chooses the route and evidence. "
            "Predict what happens when the same carrier notice is used before and after the revision date."),
        _code(setup.strip()),
        _code('for date in ("2025-06-01", "2026-06-01"):\n'
              '    print(propose(Claim("sample", date, "delay", ("carrier_notice",))))'),
        _md("## Checkpoint, reopen, and approve\n\n"
            "An approval binds the proposal revision. The database serializes approval with writes and keeps an idempotent note. "
            "The role value is a fixture. A real service derives the reviewer identity from authentication."),
        _code("def checkpoint(" + persistence.rstrip()),
        _code('from pathlib import Path\nfrom tempfile import TemporaryDirectory\n\n'
              'with TemporaryDirectory() as folder:\n'
              '    db = str(Path(folder) / "claims.db")\n'
              '    with closing(open_store(db)) as store:\n'
              '        revision = checkpoint(store, propose(Claim("sample", "2026-06-01", "delay", ("carrier_notice",))))\n'
              '    with closing(open_store(db)) as resumed:\n'
              '        assert approve(resumed, "sample", revision, "agent") == "forbidden"\n'
              '        assert approve(resumed, "sample", revision, "reviewer") == "recorded"\n'
              '    with closing(open_store(db)) as resumed:\n'
              '        assert approve(resumed, "sample", revision, "reviewer") == "replay ignored"\n'
              '        print(resumed.execute("SELECT count(*) FROM approved_note").fetchone()[0], "note")'),
        _md("## Compare the harness with a manual baseline\n\n"
            "Score the proposed route, source, and requested documents separately. Keep the cases fixed for both candidates. "
            "The manual baseline sometimes gives the right next step. It misses the cases that need a dated evidence decision or an explicit pause."),
        _code("# Keep these expectations" + evaluation.rstrip()),
        _code('baseline, candidate = evaluate(manual_baseline), evaluate(propose)\n'
              'print("Baseline:", baseline["passed"], "/", baseline["total"])\n'
              'for row in candidate["cases"]:\n'
              '    print(row["id"], row["observed"], "pass:", row["pass"])\n'
              'assert candidate["critical_pass"] and candidate["passed"] >= baseline["passed"]'),
        _md("## Practice\n\n"
            "Add a case on the new policy’s exact effective date. Then create a second proposal for the same claim, request approval for the old revision, and verify that it adds no note.\n\n"
            "<details><summary>Compare your result</summary>\n\n"
            "On 2026-01-01 the source should be `delay-v2`. The old revision should return `stale or unknown`. "
            "Keep these checks apart from proposals for future model or tool changes. A production trial would require a representative held-out workload and an authenticated reviewer.\n\n</details>"),
    ])


def update_notebooks_index() -> None:
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Jupyter Notebooks",
        "",
        "Technical and applied workbooks pair a practice case with worked explanations, executable demonstrations, and exercises. "
        "They contain their own sample data and can run outside the repository.",
        "",
        "Open the [HarborLink interactive workbook](../interactive-workbook.md) to run a single case across the curriculum in your browser.",
        "For a second end-to-end case, use the [UnderCover claims harness practicum](../../guides/undercover-harness.md) and its downloadable notebook.",
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
        "Browse [course workbooks and Jupyter setup](notebooks/index.md), run the [HarborLink interactive workbook](interactive-workbook.md), or use the [lab catalog](catalog.md) for individual lecture scripts.",
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
        write_ipynb(LABS / slug / "lab.ipynb", cells_for(slug))
        count += 1
    write_course_notebooks()
    write_practicum_notebooks()
    write_claims_notebook()
    update_notebooks_index()
    update_labs_index()
    print(f"Generated {len(TECHNICAL_COURSES) + len(APPLIED_COURSES)} course workbooks, {count} starter lab notebooks, and the claims practicum.")


if __name__ == "__main__":
    main()
