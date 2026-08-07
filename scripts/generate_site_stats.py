"""Inject accurate catalog counts into docs and README from site_stats."""
from __future__ import annotations

from pathlib import Path

from site_stats import collect_site_stats, format_word_count, replace_marked_block

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    s = collect_site_stats()

    publication = f"""\
- {s.books} guided books
- {s.chapters} full study chapters
- {s.knowledge_areas} knowledge-area maps
- {s.total_lessons} guided lessons ({s.ka_lessons} knowledge-area + {s.supplemental_lessons} supplemental)
- {s.concept_cards} concept cards ({s.featured_concepts} featured deep-dives)
- {s.patterns_total} patterns ({s.patterns_generated} catalog + {s.patterns_manual} starter deep-dives)
- {s.architectures} architecture studios
- {s.build_guides} build guides · {s.cloud_capabilities} cloud capability guides
- {s.total_labs} labs ({s.chapter_labs} chapter + {s.starter_labs} starter) · {s.code_samples} code samples
- {format_word_count(s.word_count_docs)} words of deployable learning content in `docs/`"""

    readme = f"""\
- A complete {s.knowledge_areas}-knowledge-area curriculum ({s.books} books, {s.chapters} chapters)
- {s.concept_cards} concept cards, {s.patterns_total} patterns, {s.architectures} architecture studios
- {s.build_guides} build guides · {s.cloud_capabilities} cloud capability guides
- {s.starter_labs} runnable starter labs (+ {s.chapter_labs} chapter labs in the repo)
- Content templates and editorial quality system
- Link/configuration validation and GitHub Pages deployment
- A roadmap for growing the body of knowledge without turning it into an LMS"""

    concepts_intro = f"""\
Curated deep-dive pages plus **{s.concept_cards} reference cards** in [All Cards](cards/index.md) (collapsed A–Z groups). **{s.featured_concepts} featured** deep-dives are listed below."""

    labs_intro = f"""\
**New?** Start with **[Hands-on start](start-here.md)** — {s.starter_labs} starter labs in order with book chapters and notebook links.

**{s.chapter_labs} chapter labs** plus {s.starter_labs} foundational starter labs (**{s.total_labs} total**). See [catalog.md](catalog.md) for the full list."""

    cap_line = (
        f"See the [capability guide catalog](capabilities/index.md) "
        f"for **{s.cloud_capabilities}** provider-neutral pages."
    )

    updated: list[str] = []
    for path, marker, body in [
        (ROOT / "docs/index.md", "publication", publication),
        (ROOT / "README.md", "readme", readme),
        (ROOT / "docs/concepts/index.md", "intro", concepts_intro),
        (ROOT / "docs/labs/index.md", "intro", labs_intro),
        (ROOT / "docs/cloud/index.md", "cloud-capabilities", cap_line),
    ]:
        if replace_marked_block(path, marker, body):
            updated.append(str(path.relative_to(ROOT)))

    print(
        f"Site stats: {s.total_lessons} lessons, {s.patterns_total} patterns, "
        f"{s.total_labs} labs, {s.word_count_docs:,} words."
    )
    if updated:
        print("Updated:", ", ".join(updated))
    else:
        print("Warning: no marked sections found — add site-stats HTML comment markers to docs.")


if __name__ == "__main__":
    main()
