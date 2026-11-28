"""Generate sectioned project courses and the role-based course sequences."""
import json
from pathlib import Path

from applied_courses import APPLIED_COURSES
from course_types import Course, Lecture
from course_catalog import PATHS, SPECIALIST_PATHS, TECHNICAL_COURSES
from generate_books import BOOKS, chapter_filename, course_slug, slug
from lecture_cases import CASES, course_case_intro, lecture_case
from no_code_courses import NO_CODE_COURSES
from practicum_code import lecture_cells
from worked_lecture_traces import WORKED_TRACES
from study_navigation import directions, lecture_outline, lecture_progress, outline_link, start_course
from textbook_readings import READINGS

DOCS = Path(__file__).resolve().parents[1] / "docs"
COURSES = DOCS / "courses"
PATH_PAGES = DOCS / "getting-started" / "learning-paths"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def lecture_filename(number: int, lecture: Lecture) -> str:
    return f"{number:02d}-{slug(lecture.title)}.md"


def write_course(course: Course) -> None:
    directory = COURSES / course.slug
    lectures = [lecture for _, group in course.sections for lecture in group]
    case = CASES[course.slug]
    if len(case.moments) != len(lectures):
        raise ValueError(f"Practice case must cover every lecture in {course.title}")
    readings = READINGS[course.slug]
    if len(readings) != len(lectures):
        raise ValueError(f"Extended readings must cover every lecture in {course.title}")
    titles = [lecture_filename(number, lecture) for number, lecture in enumerate(lectures, 1)]
    numbered_titles = [(lecture.title, filename) for lecture, filename in zip(lectures, titles, strict=True)]
    sections = iter(numbered_titles)
    groups = [(heading, [next(sections) for _ in group]) for heading, group in course.sections]
    mode = "Project practicum" if course.workbook else "No code"
    duration = "3–4 hours" if course.workbook else "About 2 hours"
    workbook = f"[Download the workbook](../../assets/notebooks/{course.slug}.ipynb){{ download }}"
    outline = []
    examples = lecture_cells(course)
    number = 0
    for section, group in course.sections:
        outline.append(f"### {section}\n")
        for lecture in group:
            filename = titles[number]
            number += 1
            moment = lecture_case(course.slug, number)
            progress = lecture_progress(course.slug, filename, section, number, len(titles))
            navigation = directions(numbered_titles, number)
            jump = lecture_outline(groups, filename)
            practice = (
                f"\n\n{workbook} and run through **Lecture {number:02d}** in order. "
                "See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed."
                if course.workbook else ""
            )
            trace = WORKED_TRACES.get(course.slug)
            walkthrough = f"\n\n{trace[number - 1]}" if trace else ""
            demonstration = ""
            if examples:
                setup = (
                    "Run this cell after the preceding cells in the course workbook."
                    if number > 1 else "Run this cell in Python 3.10 or later."
                )
                demonstration = (
                    f"## Follow the code\n\n{setup} "
                    "Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result."
                    f"\n\n```python\n{examples[number - 1]}\n```\n\n"
                )
            lesson_link = outline_link(f"{number:02d} · {lecture.title}", filename)
            outline.append(f"- {lesson_link} — {lecture.outcome}")
            write(directory / filename, f"""
# {lecture.title}

{progress}

{navigation}

{jump}

## What you will learn

{lecture.outcome}

{moment}

## How it works

{lecture.explanation}

{readings[number - 1]}

## Worked example

{lecture.example}{walkthrough}

{demonstration}## Try it yourself

{lecture.practice}{practice}

??? success "Compare your answer"
    {lecture.answer}

## Continue

{directions(numbered_titles, number, footer=True)}
""")
        outline.append("")
    outline_text = "\n".join(outline)
    workbook_section = (
        f"## Workbook\n\n{workbook}. Run the exercises in lecture order using "
        "the bundled sample data. Each lecture includes checks and a suggested variation.\n\n"
        if course.workbook else ""
    )
    resource_links = "\n".join(f"- [{title}]({href})" for title, href in course.resources)
    resources = f"\n\n## Further study\n\n{resource_links}" if resource_links else ""
    write(directory / "index.md", f"""
# {course.title}

{mode} · {len(course.sections)} sections · {len(titles)} lectures · {duration}, plus the project

{course.goal}

{start_course(course.slug, titles[0])}

{course_case_intro(case)}

## Entry prerequisites

{course.entry}

## Course outline

{outline_text}
{workbook_section}## Course project

{course.project}

**How to check your project**

{course.standard}{resources}

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
""")


def write_course_catalog() -> None:
    rows = [
        "# Courses", "",
        "Each course groups self-contained lectures into sections and ends with a project. "
        "For an ordered sequence matched to your role, choose a [learning path](../getting-started/learning-paths/index.md).",
        "", "## No-code courses", "",
    ]
    rows.extend(f"- [{course.title}]({course.slug}/index.md) — {course.goal}" for course in NO_CODE_COURSES)
    rows.extend(("", "## Technical project practicums", ""))
    rows.extend(f"- [{course.title}]({course.slug}/index.md) — {course.goal}" for course in APPLIED_COURSES)
    rows.extend(("", "## Technical courses", ""))
    rows.extend(
        f"- [{number:02d} · {book['title']}](../books/{course_slug(number, book['title'])}/index.md) — {book['goal']}"
        for number, book in enumerate(BOOKS, 1)
    )
    rows.extend(("", "[Notebook downloads and setup](../labs/notebooks/index.md) · [Real-world casebook](../casebook/index.md)"))
    write(COURSES / "index.md", "\n".join(rows))


def course_link(course: str | int, *, label: str | None = None) -> str:
    if isinstance(course, int):
        book = BOOKS[course - 1]
        return f"[{label or book['title']}](../../books/{course_slug(course, book['title'])}/index.md)"
    item = next(item for item in (*NO_CODE_COURSES, *APPLIED_COURSES) if item.slug == course)
    return f"[{label or item.title}](../../courses/{item.slug}/index.md)"


def write_paths() -> None:
    rows = [
        "# Learning Paths", "",
        "Choose a core path for your role or a specialist path for a specific project. "
        "Each path lists its courses in study order and describes the experience needed to start.",
        "", "## Core paths", "",
        "| Path | Technical level | Designed for |", "|---|---|---|",
    ]
    for path in PATHS:
        if path == SPECIALIST_PATHS[0]:
            rows.extend(("", "## Specialist paths", "", "| Path | Technical level | Designed for |", "|---|---|---|"))
        rows.append(f"| [{path.title}]({path.slug}.md) | {path.level} | {path.audience} |")
        sequence = "\n".join(f"{index}. {course_link(course)}{{ .study-path-course }}"
                             for index, course in enumerate(path.courses, 1))
        technical = any(isinstance(course, int) for course in path.courses)
        study = (
            "Plan for 10–12 hours per technical core course, 3–4 hours per practicum, and about two hours per no-code course, plus project work. "
            "Use the core course checkpoints to prepare for the applied workbooks."
            if technical else
            "Allow about two hours per course for the lectures and exercises, plus project work. "
            "Use the answer examples to review your work before progressing."
        )
        if not technical and any(course.slug in path.courses for course in APPLIED_COURSES):
            study = "Allow 3–4 hours per practicum for lectures and notebook exercises, plus project work."
            if any(course.slug in path.courses for course in NO_CODE_COURSES):
                study += " Allow about two hours for each no-code course."
        completion = path.outcome
        capstone = path.capstone
        if path.slug == "05-ai-engineer":
            capstone = "ai-engineer-capstone.md"
        if capstone:
            study += " Budget additional time for the capstone."
            completion += f" Follow the [capstone brief and rubric]({capstone})."
        write(PATH_PAGES / f"{path.slug}.md", f"""
# {path.title}

{path.level} · {len(path.courses)} courses

{path.audience}

## Entry prerequisites

{path.entry}

## Course sequence

{course_link(path.courses[0], label="Start this path")}{{ .md-button .md-button--primary .study-path-course }}

{sequence}

## Study pace

{study}

## Completion evidence

{completion}

[All learning paths](index.md) · [Course catalog](../../courses/index.md)
""")
    rows.extend(("", "[Learning path coverage](../../editorial/learning-path-coverage.md) · [Textbook content audit](../../editorial/textbook-audit.md)"))
    write(PATH_PAGES / "index.md", "\n".join(rows))


def write_navigation() -> None:
    config = DOCS.parent / "mkdocs.yml"
    content = config.read_text(encoding="utf-8")
    start = "  # curriculum:start\n"
    end = "  # curriculum:end"
    before, current = content.split(start, 1)
    _, after = current.split(end, 1)

    def label(text: str) -> str:
        return json.dumps(text, ensure_ascii=False)

    nav = [
        "  - Learning Paths:",
        "      - Overview: getting-started/learning-paths/index.md",
        *(f"      - {label(path.title)}: getting-started/learning-paths/{path.slug}.md" for path in PATHS if path not in SPECIALIST_PATHS),
        "      - AI Engineer Capstone: getting-started/learning-paths/ai-engineer-capstone.md",
        "      - Specialist Paths:",
        *(f"          - {label(path.title)}: getting-started/learning-paths/{path.slug}.md" for path in SPECIALIST_PATHS),
        "  - Courses:",
        "      - Course Catalog: courses/index.md",
        "      - Casebook: casebook/index.md",
    ]
    for group, courses in (("No-code Courses", NO_CODE_COURSES), ("Technical Project Practicums", APPLIED_COURSES)):
        nav.append(f"      - {group}:")
        for course in courses:
            directory = f"courses/{course.slug}"
            nav.extend([f"          - {label(course.title)}:", f"              - Overview: {directory}/index.md"])
            number = 0
            for section, lectures in course.sections:
                nav.append(f"              - {label(section)}:")
                for lecture in lectures:
                    number += 1
                    nav.append(f"                  - {label(lecture.title)}: {directory}/{lecture_filename(number, lecture)}")
    nav.append("      - Technical Courses:")
    for number, (book, course) in enumerate(zip(BOOKS, TECHNICAL_COURSES, strict=True), 1):
        directory = f"books/{course_slug(number, book['title'])}"
        nav.extend([f"          - {label(book['title'])}:", f"              - Overview: {directory}/index.md"])
        for index, section in enumerate(course.sections):
            nav.append(f"              - {label(section)}:")
            for chapter in range(index * 2 + 1, index * 2 + 3):
                title = book["chapters"][chapter - 1][0]
                nav.append(f"                  - {label(title)}: {directory}/{chapter_filename(chapter, title)}")
    write(config, before + start + "\n".join(nav) + "\n" + end + after)


def main() -> None:
    courses = (*NO_CODE_COURSES, *APPLIED_COURSES)
    for course in courses:
        write_course(course)
    write_course_catalog()
    write_paths()
    write_navigation()
    lecture_count = sum(len(group) for course in courses for _, group in course.sections)
    print(f"Generated {len(PATHS)} learning paths, {len(courses)} applied and no-code courses, and {lecture_count} lectures.")


if __name__ == "__main__":
    main()
