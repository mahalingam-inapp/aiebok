"""Single source of truth for catalog sizes referenced across AIEBOK."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Hand-maintained pattern deep-dives not in PATTERN_SPECS
MANUAL_PATTERN_PAGES = ("planner-executor", "human-approval")


@dataclass(frozen=True)
class SiteStats:
    books: int
    chapters: int
    knowledge_areas: int
    ka_lessons: int
    supplemental_lessons: int
    total_lessons: int
    concept_cards: int
    featured_concepts: int
    glossary_terms: int
    patterns_generated: int
    patterns_manual: int
    patterns_total: int
    architectures: int
    paper_readings: int
    build_guides: int
    cloud_capabilities: int
    chapter_labs: int
    starter_labs: int
    total_labs: int
    code_samples: int
    progress_onboarding: int
    progress_total: int
    word_count_docs: int


def _word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def collect_site_stats() -> SiteStats:
    from generate_books import BOOKS
    from generate_cloud_guides import CAPABILITY_SPECS
    from generate_expansion import ARCH_SPECS, EXTRA_PATTERN_SPECS, PATTERN_SPECS
    from generate_featured_concepts import NEW_FEATURED, PRESERVE
    from generate_lessons import SUPPLEMENTAL
    from generate_maturity_content import ALL_PAPER_SPECS, BUILD_GUIDES, STARTER_LABS
    from guide_deep_content import GUIDE_DETAILS
    from ka_deep_content import KA_SPECS
    from topic_knowledge import TOPIC_FACTS

    books = len(BOOKS)
    chapters = sum(len(book["chapters"]) for book in BOOKS)
    ka_lessons = sum(len(spec[6]) for spec in KA_SPECS)
    supplemental = len(SUPPLEMENTAL)
    patterns_generated = len(PATTERN_SPECS) + len(EXTRA_PATTERN_SPECS)
    patterns_manual = len(MANUAL_PATTERN_PAGES)
    chapter_labs = chapters
    starter_labs = len(STARTER_LABS)
    progress_onboarding = 3

    word_count = 0
    for path in DOCS.rglob("*.md"):
        word_count += _word_count(path.read_text(encoding="utf-8"))

    code_samples = len(list((DOCS / "code-samples").glob("*.py")))

    return SiteStats(
        books=books,
        chapters=chapters,
        knowledge_areas=len(KA_SPECS),
        ka_lessons=ka_lessons,
        supplemental_lessons=supplemental,
        total_lessons=ka_lessons + supplemental,
        concept_cards=len(TOPIC_FACTS),
        featured_concepts=len(PRESERVE) + len(NEW_FEATURED),
        glossary_terms=len(TOPIC_FACTS),
        patterns_generated=patterns_generated,
        patterns_manual=patterns_manual,
        patterns_total=patterns_generated + patterns_manual,
        architectures=len(ARCH_SPECS),
        paper_readings=len(ALL_PAPER_SPECS),
        build_guides=len(BUILD_GUIDES) if BUILD_GUIDES else len(GUIDE_DETAILS),
        cloud_capabilities=len(CAPABILITY_SPECS),
        chapter_labs=chapter_labs,
        starter_labs=starter_labs,
        total_labs=chapter_labs + starter_labs,
        code_samples=code_samples,
        progress_onboarding=progress_onboarding,
        progress_total=progress_onboarding + chapters,
        word_count_docs=word_count,
    )


def format_word_count(n: int) -> str:
    if n >= 1_000_000:
        return f"approximately {n / 1_000_000:.1f} million"
    if n >= 10_000:
        thousands = round(n / 1000) * 1000
        return f"approximately {thousands:,}"
    return f"approximately {n:,}"


def replace_marked_block(path: Path, marker: str, body: str) -> bool:
    start = f"<!-- site-stats:{marker}:start -->"
    end = f"<!-- site-stats:{marker}:end -->"
    text = path.read_text(encoding="utf-8")
    if start not in text or end not in text:
        return False
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    replacement = f"{start}\n{body.rstrip()}\n{end}"
    path.write_text(pattern.sub(replacement, text, count=1), encoding="utf-8")
    return True
