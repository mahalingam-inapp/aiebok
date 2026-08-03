"""Concept explanations for generated book chapters."""
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

ROLE_FRAMING = [
    "defines the initial boundary for what the system can represent or decide",
    "performs the main transformation that turns inputs into comparable candidates",
    "connects this mechanism to neighboring components in the pipeline",
    "governs quality, cost, latency, or safety trade-offs at runtime",
    "surfaces the constraint or failure mode engineers most often miss",
]


def normalize(topic: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")


def concept_link(topic: str) -> str | None:
    """Return a relative concept-card link when one exists."""
    key = normalize(topic)
    cards = {
        "embeddings": "../../concepts/embeddings.md",
        "word-embeddings": "../../concepts/embeddings.md",
        "sentence-embeddings": "../../concepts/embeddings.md",
        "rag": "../../concepts/rag.md",
        "retrieval": "../../concepts/rag.md",
        "dense-retrieval": "../../concepts/rag.md",
        "hybrid-search": "../../concepts/rag.md",
        "bm25": "../../concepts/rag.md",
        "tokens": "../../concepts/tokens.md",
        "tokenization": "../../concepts/tokens.md",
        "vocabulary": "../../concepts/tokens.md",
        "subwords": "../../concepts/tokens.md",
        "bpe": "../../concepts/tokens.md",
        "evaluation": "../../concepts/evaluation.md",
        "rubrics": "../../concepts/evaluation.md",
        "slices": "../../concepts/evaluation.md",
        "prompt-injection": "../../concepts/prompt-injection.md",
        "attention": "../../concepts/attention.md",
        "attention-masks": "../../concepts/attention.md",
        "scaled-dot-product": "../../concepts/attention.md",
        "kv-cache": "../../concepts/kv-cache.md",
        "agents": "../../concepts/agents.md",
        "agency": "../../concepts/agents.md",
        "plan-act-observe": "../../concepts/agents.md",
        "workflows": "../../concepts/agents.md",
        "skills": "../../concepts/skills-harnesses.md",
        "structured-output": "../../concepts/structured-output.md",
        "json-schema": "../../concepts/structured-output.md",
        "chunking": "../../concepts/chunking.md",
        "rerankers": "../../concepts/reranking.md",
        "reciprocal-rank-fusion": "../../concepts/reranking.md",
        "tool-calling": "../../concepts/tool-calling.md",
        "function-calling": "../../concepts/tool-calling.md",
        "mcp": "../../concepts/tool-calling.md",
        "lora": "../../concepts/fine-tuning.md",
        "qlora": "../../concepts/fine-tuning.md",
        "sft": "../../concepts/fine-tuning.md",
        "fine-tuning": "../../concepts/fine-tuning.md",
    }
    return cards.get(key)


@lru_cache(maxsize=1)
def _entries() -> dict[str, tuple[str, str, str]]:
    path = Path(__file__).with_name("concept_entries.json")
    raw = json.loads(path.read_text(encoding="utf-8"))
    return {k: tuple(v) for k, v in raw.items()}


def render_concept(topic: str, role_idx: int, chapter_summary: str) -> str:
    key = normalize(topic)
    explanation, example, evidence = _entries().get(
        key,
        (
            f"**{topic.title()}** {ROLE_FRAMING[role_idx % len(ROLE_FRAMING)]}.",
            f"Apply it in the chapter scenario and compare against a baseline that omits it.",
            "Name inputs, outputs, and one test that would falsify a wrong design.",
        ),
    )
    link = concept_link(topic)
    title = topic.title() if topic.islower() or " " in topic else topic
    ref = f" See the [{title} concept card]({link})." if link else ""
    return (
        f"### {title}\n\n"
        f"{explanation}{ref}\n\n"
        f"**Example:** {example}\n\n"
        f"**Evidence of understanding:** {evidence}"
    )


def render_core_concepts(topics: list[str], chapter_summary: str) -> str:
    blocks = [render_concept(topic, i, chapter_summary) for i, topic in enumerate(topics)]
    return (
        "The concepts form a system, not a vocabulary list. "
        "Read each section below before attempting the practice exercise.\n\n"
        + "\n\n".join(blocks)
    )
