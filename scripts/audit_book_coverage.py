"""Fail when a generated book chapter lacks an instructional component."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
chapters = sorted((ROOT / "docs" / "books").glob("[0-9][0-9]-*/*[0-9]-*.md"))
required = {
    "motivation": "## Why this chapter exists",
    "objectives": "## Learning objectives",
    "prerequisites": "## Before you begin",
    "visual": "```mermaid",
    "core explanation": "## Core concepts",
    "worked example": "## Worked example",
    "code": "## Runnable code sample",
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

if failures:
    print("Book coverage audit failed:")
    print("\n".join(f"- {failure}" for failure in failures))
    sys.exit(1)
print(f"Book coverage audit passed for {len(chapters)} chapters and {len(required)} coverage dimensions.")
