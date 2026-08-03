"""Generate prerequisite and unlock reference views from curriculum metadata."""
from __future__ import annotations

from pathlib import Path

from generate_books import BOOKS, slug
from ka_deep_content import KA_SPECS, chapter_href

REFERENCE = Path(__file__).resolve().parents[1] / "docs" / "reference"


def generate_prerequisites() -> None:
    lines = [
        "# Prerequisites Map",
        "",
        "Suggested order before diving into advanced topics. Books are sequential within each row.",
        "",
    ]
    for book_no, book in enumerate(BOOKS, 1):
        book_slug = f"{book_no:02d}-{slug(book['title'])}"
        prereq = f"[Book {book_no - 1}](../books/{book_no - 1:02d}-{slug(BOOKS[book_no - 2]['title'])}/index.md)" if book_no > 1 else "None (entry path)"
        lines.append(f"## Book {book_no} — {book['title']}")
        lines.append("")
        lines.append(f"- **Prerequisite:** {prereq}")
        lines.append(f"- **Unlocks:** Book {book_no + 1} topics" if book_no < len(BOOKS) else "- **Unlocks:** Advanced guides and enterprise paths")
        lines.append(f"- **Start:** [Overview](../books/{book_slug}/index.md)")
        lines.append("")

    for ka_file, title, _, book_no, _, _, _ in KA_SPECS:
        book_slug = f"{book_no:02d}-{slug(BOOKS[book_no - 1]['title'])}"
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"- **Primary book:** [Book {book_no}](../books/{book_slug}/index.md)")
        lines.append(f"- **Lessons:** [Lesson catalog](../lessons/index.md) (filter `{ka_file}`)")
        lines.append("")

    (REFERENCE / "prerequisites.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_unlocks() -> None:
    lines = [
        "# Unlocks Map",
        "",
        "What each completed unit enables next in the curriculum.",
        "",
        "| Completed | Unlocks |",
        "|---|---|",
    ]
    for book_no, book in enumerate(BOOKS, 1):
        book_slug = f"{book_no:02d}-{slug(book['title'])}"
        if book_no < len(BOOKS):
            nxt = BOOKS[book_no]
            nxt_slug = f"{book_no + 1:02d}-{slug(nxt['title'])}"
            unlock = f"[{nxt['title']}](../books/{nxt_slug}/index.md)"
        else:
            unlock = "[Build guides](../guides/index.md), [cloud capabilities](../cloud/capabilities/index.md)"
        lines.append(f"| [Book {book_no}: {book['title']}](../books/{book_slug}/index.md) | {unlock} |")

    for ka_file, title, _, _, project, _, lesson_indices in KA_SPECS:
        first = lesson_indices[0]
        last = lesson_indices[-1]
        lines.append(f"| {title} (6 lessons) | Practice project: {project[:60]}… |")

    lines.extend([
        "",
        "## Cross-links",
        "",
        "- [Question index](question-index.md)",
        "- [Glossary](glossary.md)",
        "- [Guided lessons](../lessons/index.md)",
    ])
    (REFERENCE / "unlocks.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    generate_prerequisites()
    generate_unlocks()
    print("Generated prerequisites.md and unlocks.md.")


if __name__ == "__main__":
    main()
