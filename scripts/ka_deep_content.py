"""Rich knowledge-area pages with lesson sequences and mechanism tables."""
from __future__ import annotations

import re
from pathlib import Path

from generate_books import BOOKS, slug
from topic_knowledge import normalize

DOCS = Path(__file__).resolve().parents[1] / "docs"
CONCEPTS = DOCS / "concepts" / "cards"


def lab_slug(book_no: int, chapter_no: int, title: str) -> str:
    return f"{book_no:02d}{chapter_no:02d}-{slug(title)}"[:48].strip("-")


def concept_md_link(topic: str) -> str:
    key = normalize(topic)
    if (CONCEPTS / f"{key}.md").exists():
        return f"../concepts/cards/{key}.md"
    featured = DOCS / "concepts" / f"{key}.md"
    if featured.exists():
        return f"../concepts/{key}.md"
    return f"../concepts/cards/{key}.md"

# (ka_file, title, purpose, book_no, project, extra_topics, lessons as chapter indices 1-based)
KA_SPECS: list[tuple[str, str, str, int, str, list[str], list[int]]] = [
    ("00-foundations", "KA 00 — Foundations", "Build vocabulary for intelligence, search, learning, and decisions.", 1, "Compare rule, search, and learned solvers on one bounded task.", ["A*", "feedback", "calibration"], [1, 2, 3, 4, 5, 6]),
    ("01-machine-learning", "KA 01 — Machine Learning", "Train, validate, and operate predictive systems.", 2, "Ship a prediction service with error analysis and monitoring.", ["baselines", "cross-validation", "drift"], [1, 2, 3, 4, 5, 6]),
    ("02-language-representation", "KA 02 — Language & Representation", "Make language computable for search and models.", 3, "Build lexical and semantic search baselines.", ["BM25", "word embeddings", "ANN indexes"], [1, 2, 3, 4, 5, 6]),
    ("03-transformers", "KA 03 — Transformers", "Understand attention, blocks, training, and inference.", 4, "Implement attention and compare decoder configurations.", ["multi-head attention", "KV cache", "scaling laws"], [1, 2, 3, 4, 5, 6]),
    ("04-models", "KA 04 — Models", "Select and benchmark model families for tasks.", 4, "Write a vendor-neutral model selection report.", ["model routing", "instruction tuning", "open weights"], [4, 5, 6, 1, 2, 3]),
    ("05-prompt-context", "KA 05 — Prompt & Context", "Engineer reliable inputs, state, and outputs.", 5, "Build a context engine with regression tests.", ["JSON Schema", "prompt injection", "context windows"], [1, 2, 3, 4, 5, 6]),
    ("06-knowledge-systems", "KA 06 — Knowledge Systems", "Ground answers with retrievable evidence.", 6, "Deliver hybrid RAG with citations and stage evals.", ["RAG", "hybrid search", "rerankers"], [1, 2, 3, 4, 5, 6]),
    ("07-reasoning", "KA 07 — Reasoning Systems", "Apply search, planning, and verification at inference.", 7, "Build planner–tool–verifier workflow.", ["planning", "verifiers", "MCP"], [1, 2, 3, 4, 5, 6]),
    ("08-tools-integration", "KA 08 — Tools & Integration", "Connect models to software safely.", 7, "Wrap APIs as typed tools with auth and audit.", ["function calling", "tool schemas", "MCP"], [4, 5, 6, 1, 2, 3]),
    ("09-agents", "KA 09 — Agents", "Design bounded autonomous loops.", 8, "Ship a checkpointed agent with eval traces.", ["plan-act-observe", "checkpoints", "approval gates"], [1, 2, 3, 4, 5, 6]),
    ("10-ai-software-engineering", "KA 10 — AI Software Engineering", "Apply SDLC rigor to AI features.", 9, "Deliver spec-to-test AI feature with release evidence.", ["functional specifications", "contract tests", "evaluation specs"], [1, 2, 3, 4, 5, 6]),
    ("11-ai-coding", "KA 11 — AI Coding Ecosystem", "Collaborate with coding agents effectively.", 9, "Complete a bounded repo task with review evidence.", ["skills", "repo instructions", "code review"], [2, 3, 4, 5, 6, 1]),
    ("12-evaluation-safety", "KA 12 — Evaluation, Safety & Security", "Measure and constrain behavior.", 10, "Build eval and red-team package for release gates.", ["rubrics", "slices", "prompt injection"], [1, 2, 3, 4, 5, 6]),
    ("13-model-training", "KA 13 — Model Training", "Adapt models with curated data.", 11, "Fine-tune and evaluate a small model.", ["LoRA", "SFT", "data curation"], [1, 2, 3, 4, 5, 6]),
    ("14-infrastructure", "KA 14 — Infrastructure & Deployment", "Serve models efficiently.", 11, "Load-test inference configurations.", ["quantization", "batching", "KV cache"], [4, 5, 6, 1, 2, 3]),
    ("15-aiops", "KA 15 — AI Operations", "Observe, release, and recover AI systems.", 11, "Instrument requests and inject failure drills.", ["tracing", "canaries", "FinOps"], [5, 6, 1, 2, 3, 4]),
    ("16-enterprise-architecture", "KA 16 — Enterprise Architecture", "Design governed AI platforms.", 12, "Produce reference architecture and ADRs.", ["identity", "multi-tenancy", "AI gateways"], [1, 2, 3, 4, 5, 6]),
    ("17-multimodal", "KA 17 — Multimodal AI", "Compose text, vision, audio, and documents.", 13, "Build document intelligence pipeline with provenance.", ["OCR", "vision encoders", "provenance"], [1, 2, 3, 4, 5, 6]),
    ("18-frontier", "KA 18 — Frontier AI", "Evaluate emerging capabilities with evidence.", 13, "Reproduce one claim versus strong baselines.", ["reproduction", "benchmarks", "ablations"], [5, 6, 1, 2, 3, 4]),
    ("19-product-engineering", "KA 19 — AI Product Engineering", "Deliver useful human-centered products.", 9, "Prototype and experiment with adoption guardrails.", ["user research", "uncertainty UX", "ROI"], [1, 5, 6, 2, 3, 4]),
]


def chapter_href(book_no: int, chapter_no: int) -> tuple[str, str]:
    book = BOOKS[book_no - 1]
    ch = book["chapters"][chapter_no - 1]
    book_slug = f"{book_no:02d}-{slug(book['title'])}"
    ch_slug = f"{chapter_no:02d}-{slug(ch[0])}"
    return f"../books/{book_slug}/{ch_slug}.md", ch[0]


def render_ka_page(spec: tuple[str, str, str, int, str, list[str], list[int]]) -> str:
    ka_file, title, purpose, book_no, project, extra_topics, lesson_indices = spec
    book = BOOKS[book_no - 1]
    book_slug = f"{book_no:02d}-{slug(book['title'])}"
    topic_links = "\n".join(f"- [{t}]({concept_md_link(t)})" for t in extra_topics[:8])

    lesson_lines = []
    for i, ch_no in enumerate(lesson_indices, 1):
        href, ch_title = chapter_href(book_no, ch_no)
        ls = lab_slug(book_no, ch_no, ch_title)
        lesson_lines.append(
            f"{i}. **{ch_title}** — read [chapter]({href}), run [lab](../labs/{ls}.md), "
            f"lesson page [L-{ka_file}-{i:02d}](../lessons/{ka_file}-{i:02d}.md)"
        )

    mechanisms = []
    for ch_no in lesson_indices[:4]:
        ch = book["chapters"][ch_no - 1]
        mechanisms.append(f"| {ch[0]} | {ch[4][:90]} | Apply without baseline or slice eval |")

    mech_table = "\n".join(mechanisms)

    return f"""# {title}

## Purpose

{purpose}

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

{chr(10).join(lesson_lines)}

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
{mech_table}

## Core topics

{topic_links}

## Guided resources

- Primary book: [{book['title']}](../books/{book_slug}/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

{project}

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
"""


def all_ka_pages() -> dict[str, str]:
    return {spec[0]: render_ka_page(spec) for spec in KA_SPECS}
