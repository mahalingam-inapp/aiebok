"""Learning-card grids for books, onboarding, and chapter overviews."""
from __future__ import annotations

from pathlib import Path

from site_stats import collect_site_stats, replace_marked_block

ROOT = Path(__file__).resolve().parents[1]


def _clip(text: str, limit: int = 110) -> str:
    clean = text.replace("\n", " ").strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1].rstrip() + "…"


def chapter_icon(chapter_no: int) -> str:
    if 1 <= chapter_no <= 9:
        return f":material-numeric-{chapter_no}-circle:"
    return ":material-book-open-page-variant:"


def render_chapter_cards(chapters: list[tuple[int, str, str, str]]) -> str:
    lines = ["## Chapter learning path", "", '<div class="grid cards" markdown>', ""]
    for chapter_no, title, summary, filename in chapters:
        lines.extend(
            [
                f"-   {chapter_icon(chapter_no)}{{ .lg .middle }} __{title}__",
                "",
                f"    {_clip(summary)}",
                "",
                f"    [Open chapter →]({filename})",
                "",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines)


BOOK_ICONS = [
    "brain", "chart-line", "text-box", "hub", "message-text", "database-search",
    "source-branch", "robot", "application-brackets", "shield-check", "server", "cloud", "rocket-launch",
]

BOOK_CLUSTERS = [
    ("Core foundations", "Books 01–03", "Intelligence, ML, and language representations", 1),
    ("Models & knowledge", "Books 04–06", "Transformers, context engineering, and RAG", 4),
    ("Agents & product", "Books 07–09", "Reasoning, tool use, agents, and AI product engineering", 7),
    ("Operate at scale", "Books 10–13", "Evaluation, training, cloud, and frontier systems", 10),
]


def render_book_cluster_cards(books: list[dict], slug_fn) -> str:
    lines = [
        "## Reading journey",
        "",
        "```mermaid",
        "flowchart LR",
        "  A[01–03 Foundations] --> B[04–06 Models & RAG]",
        "  B --> C[07–09 Agents & Product]",
        "  C --> D[10–13 Ops & Frontier]",
        "```",
        "",
        '<div class="grid cards" markdown>',
        "",
    ]
    for label, book_range, blurb, start in BOOK_CLUSTERS:
        first = books[start - 1]
        rel = f"{start:02d}-{slug_fn(first['title'])}/index.md"
        lines.extend(
            [
                f"-   :material-book-multiple:{{ .lg .middle }} __{label}__",
                "",
                f"    **{book_range}** — {_clip(blurb, 90)}",
                "",
                f"    [Open book {start:02d} →]({rel})",
                "",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines)


def render_book_catalog_cards(books: list[dict], slug_fn) -> str:
    lines = ["## All books", "", '<div class="grid cards" markdown>', ""]
    for book_no, book in enumerate(books, 1):
        icon = BOOK_ICONS[book_no - 1]
        rel = f"{book_no:02d}-{slug_fn(book['title'])}/index.md"
        lines.extend(
            [
                f"-   :material-{icon}:{{ .lg .middle }} __{book_no:02d} — {book['title']}__",
                "",
                f"    {_clip(book['goal'], 120)}",
                "",
                f"    [Book overview →]({rel})",
                "",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines)


def home_cards(stats) -> str:
    return f"""\
<div class="grid cards" markdown>

-   :material-map-legend:{{ .lg .middle }} __Start with orientation__

    Newcomer guide, first 30 minutes, and role-based learning paths.

    [Newcomer guide →](getting-started/newcomer-guide.md)

-   :material-book-open-variant:{{ .lg .middle }} __Read sequentially__

    {stats.books} guided books · {stats.chapters} chapters with diagrams and knowledge checks.

    [Book catalog →](books/index.md)

-   :material-flask:{{ .lg .middle }} __Build hands-on__

    {stats.starter_labs} starter labs + {stats.chapter_labs} chapter labs with notebooks and tests.

    [Hands-on start →](labs/start-here.md)

-   :material-card-search:{{ .lg .middle }} __Look up fast__

    {stats.concept_cards} concept cards, {stats.patterns_total} patterns, {stats.architectures} architecture studios.

    [Concept index →](concepts/index.md)

-   :material-school:{{ .lg .middle }} __Short lessons__

    {stats.total_lessons} guided lessons linked to chapters, objectives, and labs.

    [Lesson catalog →](lessons/index.md)

-   :material-cloud:{{ .lg .middle }} __Design for production__

    Patterns, cloud maps, and {stats.build_guides} build guides.

    [Pattern library →](patterns/index.md)

</div>"""


def start_here_cards(_stats) -> str:
    return """\
<div class="grid cards" markdown>

-   :material-compass:{{ .lg .middle }} __Learn sequentially__

    Follow guided books or knowledge-area maps chapter by chapter.

    [Book catalog →](../books/index.md)

-   :material-magnify:{{ .lg .middle }} __Look up a concept__

    Search the site or browse featured and A–Z concept cards.

    [Concept index →](../concepts/index.md)

-   :material-hammer-wrench:{{ .lg .middle }} __Build something__

    Run starter labs, chapter labs, and architecture studios in the repo.

    [Hands-on start →](../labs/start-here.md)

</div>"""


def newcomer_nav_cards(stats) -> str:
    return f"""\
<div class="grid cards" markdown>

-   :material-home:{{ .lg .middle }} __Start Here__

    Orientation, setup, and first-week plan.

    [You are here](newcomer-guide.md)

-   :material-bookshelf:{{ .lg .middle }} __Guided Books__

    {stats.books} books · {stats.chapters} chapters.

    [Book catalog →](../books/index.md)

-   :material-sitemap:{{ .lg .middle }} __Knowledge Areas__

    {stats.knowledge_areas} curriculum maps with lesson paths.

    [KA map →](../knowledge-areas/index.md)

-   :material-notebook:{{ .lg .middle }} __Guided Lessons__

    {stats.total_lessons} lessons ({stats.ka_lessons} KA + {stats.supplemental_lessons} supplemental).

    [Lesson catalog →](../lessons/index.md)

-   :material-lightbulb:{{ .lg .middle }} __Concepts__

    {stats.concept_cards} reference cards.

    [Featured concepts →](../concepts/index.md)

-   :material-puzzle:{{ .lg .middle }} __Patterns & Architectures__

    {stats.patterns_total} patterns · {stats.architectures} studios.

    [Pattern library →](../patterns/index.md)

-   :material-flask-outline:{{ .lg .middle }} __Labs__

    {stats.total_labs} runnable labs.

    [Hands-on start →](../labs/start-here.md)

-   :material-book-alphabet:{{ .lg .middle }} __Reference__

    Glossary, prerequisites, and question index.

    [Glossary →](../reference/glossary.md)

</div>"""


def inject_page_cards() -> None:
    stats = collect_site_stats()
    for path, marker, body in [
        (ROOT / "docs/index.md", "home-cards", home_cards(stats)),
        (ROOT / "docs/getting-started/index.md", "start-cards", start_here_cards(stats)),
        (ROOT / "docs/getting-started/newcomer-guide.md", "nav-cards", newcomer_nav_cards(stats)),
    ]:
        replace_marked_block(path, marker, body)


def main() -> None:
    inject_page_cards()
    print("Updated onboarding learning cards.")


if __name__ == "__main__":
    main()
