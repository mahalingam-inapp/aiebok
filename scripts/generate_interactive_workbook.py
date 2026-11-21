"""Build the standalone HarborLink workbook from local assets and the curriculum."""
from pathlib import Path
from string import Template
from html import escape
import json
import re

from applied_courses import APPLIED_COURSES
from course_catalog import PATHS
from generate_books import BOOKS
from generate_cloud_guides import CAPABILITY_SPECS
from generate_expansion import ARCH_SPECS, EXTRA_PATTERN_SPECS, PATTERN_SPECS
from generate_maturity_content import BUILD_GUIDES, STARTER_LABS
from ka_deep_content import KA_SPECS
from no_code_courses import NO_CODE_COURSES
from topic_knowledge import TOPIC_FACTS

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts" / "interactive_workbook"
OUTPUT = ROOT / "docs" / "assets" / "workbooks" / "harborlink.html"

# In lecture order. Every target is a runnable cell in the article.
BOOK_CELLS = (
    ("brief", "learning", "reason", "language", "learning", "evaluate"),
    ("brief", "learning", "language", "attention", "evaluate", "operations"),
    ("language", "corpus", "language", "language", "retrieve", "serving"),
    ("attention", "attention", "attention", "adapt", "attention", "evaluate"),
    ("context", "answer", "context", "workflow", "governance", "delivery"),
    ("corpus", "corpus", "retrieve", "retrieve", "answer", "enterprise"),
    ("reason", "reason", "answer", "workflow", "workflow", "operations"),
    ("workflow", "workflow", "workflow", "reason", "workflow", "operations"),
    ("brief", "delivery", "workflow", "evaluate", "serve", "delivery"),
    ("evaluate", "evaluate", "evaluate", "governance", "governance", "delivery"),
    ("adapt", "adapt", "corpus", "serving", "serve", "operations"),
    ("enterprise", "governance", "enterprise", "enterprise", "enterprise", "delivery"),
    ("modalities", "modalities", "modalities", "workflow", "frontier", "frontier"),
)
PRACTICE_CELLS = {
    "ai-literacy": ("brief", "answer", "serve", "governance"),
    "using-ai-at-work": ("brief", "answer", "workflow", "delivery"),
    "ai-product-decisions": ("brief", "reason", "evaluate", "delivery"),
    "managing-ai-delivery": ("evaluate", "governance", "operations", "operations"),
    "evaluating-ai-in-practice": ("evaluate", "evaluate", "operations", "delivery"),
    "model-selection-for-leaders": ("brief", "evaluate", "operations", "delivery"),
    "model-backed-applications": ("answer", "retrieve", "evaluate", "evaluate"),
    "supervised-coding-harness": ("delivery", "workflow", "workflow", "workflow"),
    "model-selection-and-adaptation": ("learning", "learning", "evaluate", "operations"),
    "operating-ai-services": ("serve", "operations", "operations", "operations"),
    "customer-pilot-engineering": ("brief", "corpus", "evaluate", "delivery"),
    "llm-evaluation-benchmarks": ("evaluate", "evaluate", "evaluate", "operations"),
    "retrieval-system-engineering": ("corpus", "retrieve", "retrieve", "answer"),
    "durable-agent-tool-runtime": ("workflow", "governance", "workflow", "workflow"),
    "llm-adaptation-inference": ("attention", "adapt", "adapt", "frontier"),
    "ai-reliability-release": ("operations", "operations", "operations", "operations"),
}
AREA_CELLS = (
    "brief", "learning", "language", "attention", "evaluate",
    "context", "retrieve", "reason", "workflow", "workflow",
    "delivery", "workflow", "governance", "adapt", "serving",
    "operations", "enterprise", "modalities", "frontier", "delivery",
)


def brief(text: str) -> str:
    return re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)[0]


def reference_markdown(folder: str, body_heading: str, pattern: str = "*.md") -> list[dict[str, str]]:
    entries = []
    for path in sorted((ROOT / "docs" / folder).glob(pattern)):
        if path.stem == "index":
            continue
        lines = path.read_text(encoding="utf-8")
        heading = re.search(r"^# (.+)$", lines, re.MULTILINE)
        body = re.search(rf"^{body_heading}\s*\n\s*([^#\n].*)", lines, re.MULTILINE)
        if heading:
            entries.append({"title": heading.group(1), "description": brief(body.group(1)) if body else ""})
    return entries


def curriculum() -> dict:
    courses = []
    for book, targets in zip(BOOKS, BOOK_CELLS, strict=True):
        lessons = [
            {"title": title, "description": brief(summary), "cell": cell, "topics": topics}
            for (title, summary, topics, _, _), cell in zip(book["chapters"], targets, strict=True)
        ]
        courses.append({"title": book["title"], "lessons": lessons})
    additional = (*NO_CODE_COURSES, *APPLIED_COURSES)
    if {course.slug for course in additional} != PRACTICE_CELLS.keys():
        raise ValueError("The workbook needs a cell map for every course.")
    for course in additional:
        lectures = (lecture for _, group in course.sections for lecture in group)
        lessons = [
            {"title": lecture.title, "description": brief(lecture.outcome), "cell": cell, "topics": []}
            for lecture, cell in zip(lectures, PRACTICE_CELLS[course.slug], strict=True)
        ]
        courses.append({"title": course.title, "lessons": lessons})
    identifiers = (*range(1, len(BOOKS) + 1), *(course.slug for course in additional))
    course_titles = {identifier: course["title"] for identifier, course in zip(identifiers, courses, strict=True)}
    areas = [
        {"title": spec[1], "description": spec[2], "cell": cell}
        for spec, cell in zip(KA_SPECS, AREA_CELLS, strict=True)
    ]
    references = {
        "Learning paths": [{"title": path.title, "description": f"{path.level} · {brief(path.outcome)}",
                            "topics": [course_titles[identifier] for identifier in path.courses]} for path in PATHS],
        "Capstones": reference_markdown("getting-started/learning-paths", r"# .+", "*-capstone.md"),
        "Topic guides": reference_markdown("lessons", "## Objective"),
        "Concepts": [
            {"title": key.replace("-", " "), "description": brief(explanation)}
            for key, (explanation, _, _) in sorted(TOPIC_FACTS.items())
        ],
        "Patterns": [
            {"title": row[1], "description": brief(row[2])}
            for row in (*PATTERN_SPECS, *EXTRA_PATTERN_SPECS)
        ] + [
            {"title": "Planner–Executor", "description": "Separate planning and execution with explicit contracts."},
            {"title": "Human Approval", "description": "Pause before an effect that needs a person's authorization."},
        ],
        "Architecture studios": [{"title": name, "description": brief(summary)} for _, name, summary in ARCH_SPECS],
        "Build guides": [{"title": name, "description": brief(summary)} for _, name, summary, *_ in BUILD_GUIDES],
        "Cloud capabilities": [{"title": name, "description": brief(summary)} for _, name, summary, *_ in CAPABILITY_SPECS],
        "Starter labs": [{"title": name, "description": brief(summary)} for _, name, summary, *_ in STARTER_LABS],
        "Real-world casebook": reference_markdown("casebook", r"## .+"),
        "Engineering workflow": [{"title": "Spec-driven workflow", "description": "Write acceptance cases and scope tool contracts before implementing a change. Use the evaluation results as release evidence.", "cell": "delivery"}],
        "Implementation practicums": [
            {"title": "Coding-agent workflows", "description": "Implement, delegate, and review AIeBOK changes in Codex, Cursor, OpenCode, or Claude Code.", "cell": "delivery"},
            {"title": "UnderCover claims harness", "description": "Compare a policy-aware claims proposal with manual triage. Checkpoint approvals and rerun fixed cases in the separate Python practicum.", "cell": "workflow"},
        ],
    }
    return {"courses": courses, "knowledgeAreas": areas, "references": references}


def main() -> None:
    metadata = curriculum()
    manifest = json.dumps(metadata, ensure_ascii=True, separators=(",", ":")).replace("<", "\\u003c")
    core = (SOURCE / "core.js").read_text(encoding="utf-8")
    runtime = "\n\n".join([core, *((SOURCE / file).read_text(encoding="utf-8") for file in ("engine.js", "cells.js", "ui.js"))])
    registered = set(re.findall(r'^register\("([^"]+)"', runtime, re.MULTILINE))
    mapped = {
        item["cell"]
        for group in [metadata["knowledgeAreas"], *(course["lessons"] for course in metadata["courses"]),
                      *metadata["references"].values()]
        for item in group if "cell" in item
    }
    if not mapped <= registered:
        raise ValueError(f"Workbook curriculum points to unknown cells: {sorted(mapped - registered)}")
    if "</script" in runtime.lower():
        raise ValueError("The workbook runtime cannot end its inline script.")
    template = Template((SOURCE / "page.html").read_text(encoding="utf-8"))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(template.substitute(
        manifest=manifest, runtime=runtime, core_code=escape(core), styles=(SOURCE / "style.css").read_text(encoding="utf-8")
    ), encoding="utf-8")
    lectures = sum(len(course["lessons"]) for course in metadata["courses"])
    print(f"Built HarborLink with {len(registered)} runnable cells and {lectures} lecture links.")


if __name__ == "__main__":
    main()
