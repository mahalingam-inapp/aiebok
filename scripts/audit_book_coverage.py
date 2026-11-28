"""Fail when a generated book chapter lacks an instructional component."""
from pathlib import Path
import sys

from applied_courses import APPLIED_COURSES
from generate_learning_paths import lecture_filename
from no_code_courses import NO_CODE_COURSES

ROOT = Path(__file__).resolve().parents[1]
chapters = sorted((ROOT / "docs" / "books").glob("[0-9][0-9]-*/*[0-9]-*.md"))
required = {
    "motivation": "## Why this chapter exists",
    "objectives": "## Learning objectives",
    "prerequisites": "## Before you begin",
    "visual": "```mermaid",
    "core explanation": "## Core concepts",
    "worked example": "## Worked example",
    "code": "## Follow the code",
    "code block": "```python",
    "practice": "## Engineering practice",
    "architecture": "## Architecture lens",
    "failures": "## Failure clinic",
    "evolution": "## Evolution lens",
    "mastery": "## Mastery questions",
    "knowledge check": "## Knowledge check",
    "self assessment": "## Self-assessment rubric",
    "evidence route": "## Evidence and further study",
}
failures = []
for chapter in chapters:
    text = chapter.read_text(encoding="utf-8")
    for label, marker in required.items():
        if marker not in text:
            failures.append(f"{chapter.relative_to(ROOT)}: missing {label}")
    if len(text.split()) < 850:
        failures.append(f"{chapter.relative_to(ROOT)}: fewer than 850 words")

if len(chapters) != 78:
    failures.append(f"expected 78 chapters, found {len(chapters)}")

additional = 0
for course in (*APPLIED_COURSES, *NO_CODE_COURSES):
    lectures = (lecture for _, section in course.sections for lecture in section)
    for number, lecture in enumerate(lectures, 1):
        path = ROOT / "docs" / "courses" / course.slug / lecture_filename(number, lecture)
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        markers = ["## What you will learn", "## How it works", "## Worked example", "## Try it yourself"]
        markers += ["## Follow the code", "```python"] if course.workbook else ["### Follow the example"]
        for marker in markers:
            if marker not in text:
                failures.append(f"{path.relative_to(ROOT)}: missing {marker}")
        additional += 1

if failures:
    print("Book coverage audit failed:")
    print("\n".join(f"- {failure}" for failure in failures))
    sys.exit(1)
print(f"Lecture coverage audit passed for {len(chapters)} book chapters and {additional} other lectures.")
