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

    Choose a role-based path from no-code AI literacy to advanced engineering.

    [Learning paths →](getting-started/learning-paths/index.md)

-   :material-book-open-variant:{{ .lg .middle }} __Read sequentially__

    {stats.courses} courses with sectioned lectures, practice, and projects.

    [Course catalog →](courses/index.md)

-   :material-flask:{{ .lg .middle }} __Build hands-on__

    {stats.workbooks} course workbooks and {stats.starter_labs} starter notebooks.

    [Jupyter notebooks →](labs/notebooks/index.md)

-   :material-card-search:{{ .lg .middle }} __Look up fast__

    {stats.concept_cards} concept cards, {stats.patterns_total} patterns, {stats.architectures} architecture studios.

    [Concept index →](concepts/index.md)

-   :material-school:{{ .lg .middle }} __Explore by topic__

    {stats.total_lessons} topic guides linked to the curriculum.

    [Topic index →](lessons/index.md)

-   :material-cloud:{{ .lg .middle }} __Design for production__

    Patterns, cloud maps, and {stats.build_guides} build guides.

    [Pattern library →](patterns/index.md)

</div>"""


def start_here_cards(_stats) -> str:
    return """\
<div class="grid cards" markdown>

-   :material-compass:{{ .lg .middle }} __Learn sequentially__

    Choose a learning path or browse individual courses.

    [Course catalog →](../courses/index.md) · [Learning paths →](learning-paths/index.md)

-   :material-magnify:{{ .lg .middle }} __Look up a concept__

    Search the site or browse featured and A–Z concept cards.

    [Concept index →](../concepts/index.md)

-   :material-hammer-wrench:{{ .lg .middle }} __Build something__

    Run starter labs, chapter labs, and architecture studios in the repo.

    [Hands-on start →](../labs/start-here.md)

</div>"""


def inject_page_cards() -> None:
    stats = collect_site_stats()
    for path, marker, body in [
        (ROOT / "docs/index.md", "home-cards", home_cards(stats)),
        (ROOT / "docs/getting-started/index.md", "start-cards", start_here_cards(stats)),
    ]:
        replace_marked_block(path, marker, body)


def main() -> None:
    inject_page_cards()
    print("Updated onboarding learning cards.")


if __name__ == "__main__":
    main()
