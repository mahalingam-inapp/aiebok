"""Generate deep-dive featured concept pages (embeddings.md tier)."""
from __future__ import annotations

from pathlib import Path

from concept_card_enrichments import card_enrichment
from generate_books import BOOKS, slug as book_slug
from topic_knowledge import TOPIC_FACTS, get_topic_entry, normalize

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ROOT / "docs" / "concepts"
LABS = ROOT / "labs"

# Hand-maintained featured pages — never overwrite
PRESERVE = {
    "tokens", "embeddings", "rag", "evaluation", "skills-harnesses", "attention",
    "kv-cache", "prompt-injection", "agents", "structured-output", "chunking",
    "reranking", "tool-calling", "fine-tuning",
}

NEW_FEATURED = [
    "bm25", "hybrid-search", "dense-retrieval", "planning", "mcp", "lora",
    "function-calling", "context-windows", "scaling-laws", "slices", "faithfulness",
    "multi-head-attention", "quantization", "model-routing", "sft", "dpo",
    "retrieval", "test-time-compute", "human-evaluation", "json-schema",
    "tracing", "canaries", "prompting", "supervisor-worker", "backpropagation",
    "gradient-descent", "abstention", "calibration", "distillation",
]

CATEGORY_EVOLUTION = {
    "retrieval": "Yesterday: keywords and inverted indexes. Today: hybrid dense–lexical with rerankers. Tomorrow: agentic and graph-augmented retrieval. The durable principle is grounding generation in verifiable evidence.",
    "training": "Yesterday: task-specific training from scratch. Today: adapt foundation models with SFT, LoRA, and preferences. Tomorrow: continuous learning with governance. The durable principle is matching adaptation method to data and risk.",
    "inference": "Yesterday: batch GPU jobs. Today: streaming APIs with KV cache and routing. Tomorrow: speculative and edge-optimized decode. The durable principle is meeting latency and cost SLOs without silent quality loss.",
    "agents": "Yesterday: scripted workflows. Today: bounded loops with tools and checkpoints. Tomorrow: supervised multi-agent platforms. The durable principle is goal-directed action under explicit policy limits.",
    "evaluation": "Yesterday: offline accuracy. Today: slice-based gates and LLM judges with calibration. Tomorrow: continuous eval from production feedback. The durable principle is measuring what users and risk owners care about.",
    "security": "Yesterday: perimeter security only. Today: prompt injection and tool abuse testing in CI. Tomorrow: policy-as-code for AI paths. The durable principle is treating untrusted text and tools as hostile by default.",
    "default": "Yesterday: research prototypes. Today: measured production systems with eval gates. Tomorrow: tighter integration with enterprise governance. The durable principle is engineering under uncertainty with evidence.",
}

MISCONCEPTIONS = {
    "retrieval": [
        "Higher embedding dimension always improves results.",
        "Vector search replaces the need for metadata filters.",
        "If retrieval returns something, the answer must be correct.",
    ],
    "training": [
        "Fine-tuning fixes bad retrieval or missing data.",
        "More training steps always help.",
        "Open weights eliminate governance responsibilities.",
    ],
    "agents": [
        "More autonomy always improves outcomes.",
        "Tool access equals capability without risk.",
        "Agents replace the need for specifications and tests.",
    ],
    "default": [
        "Fluent language implies reliable behavior.",
        "One benchmark score generalizes to your product.",
        "Adding a model call is the same as adding a feature.",
    ],
}


def title_from_slug(s: str) -> str:
    return " ".join(w if w.isupper() and len(w) <= 4 else w.capitalize() for w in s.split("-"))


def find_lab_link(key: str) -> str | None:
    for book_no, book in enumerate(BOOKS, 1):
        for ch_no, chapter in enumerate(book["chapters"], 1):
            topics = [normalize(t) for t in chapter[2]]
            if key in topics:
                ls = f"{book_no:02d}{ch_no:02d}-{book_slug(chapter[0])}"[:48].strip("-")
                if (LABS / ls / "main.py").is_file():
                    return f"`python labs/{ls}/main.py`"
    starter = {
        "bm25": "02-semantic-search",
        "dense-retrieval": "02-semantic-search",
        "hybrid-search": "02-semantic-search",
        "retrieval": "03-basic-rag",
        "faithfulness": "03-basic-rag",
        "calibration": "05-eval-harness",
        "slices": "05-eval-harness",
        "supervisor-worker": "04-agent-loop",
        "planning": "04-agent-loop",
    }
    if key in starter and (LABS / starter[key] / "main.py").is_file():
        return f"`python labs/{starter[key]}/main.py`"
    return None


def render_featured(key: str) -> str:
    explanation, example, evidence = get_topic_entry(title_from_slug(key))
    extra = card_enrichment(key)
    from concept_card_enrichments import TOPIC_CATEGORY

    evo_key = TOPIC_CATEGORY.get(key, "default")
    misconceptions = MISCONCEPTIONS.get(evo_key, MISCONCEPTIONS["default"])
    misc_block = "\n".join(f"- {m}" for m in misconceptions)
    checklist = "\n".join(f"- {c}" for c in extra["checklist"])
    failures = "\n".join(f"- {f}" for f in extra["failure_modes"])
    lab = find_lab_link(key)
    code = f"Run {lab} from the repository root." if lab else "Find the matching chapter lab under `labs/` or a starter lab in the lab guide."

    return f"""# {title_from_slug(key)}

**Purpose:** {explanation.split('.')[0]}.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/{key}.md).

## Why this exists

{explanation}

## Core intuition

{example}

## Mechanics

1. Define the decision or system stage where {title_from_slug(key).lower()} applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

{checklist}

## Evidence of understanding

{evidence}

## Code practice

{code}

## When to use

{extra['when_to_use']}

## When not to use

{extra['when_not']}

## Common failure modes

{failures}

## Common misconceptions

{misc_block}

## Trade-offs

{title_from_slug(key)} improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

{CATEGORY_EVOLUTION[evo_key]}
"""


def generate() -> int:
    count = 0
    slugs = sorted(set(NEW_FEATURED) - PRESERVE)
    for key in slugs:
        if key not in TOPIC_FACTS:
            continue
        (CONCEPTS / f"{key}.md").write_text(render_featured(key), encoding="utf-8")
        count += 1

    featured = sorted(PRESERVE | set(slugs))
    lines = [
        "# Featured Concepts",
        "",
        "Deep-dive pages for high-leverage ideas. Every catalog topic also has a [concept card](cards/index.md).",
        "",
    ]
    for key in featured:
        if (CONCEPTS / f"{key}.md").is_file():
            lines.append(f"- [{title_from_slug(key)}]({key}.md)")
    (CONCEPTS / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return count


def main() -> None:
    n = generate()
    print(f"Generated {n} featured concept pages ({len(PRESERVE)} preserved).")


if __name__ == "__main__":
    main()
