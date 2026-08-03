# Hybrid Search

**Purpose:** Hybrid search combines lexical and dense signals—often via reciprocal rank fusion—when neither alone covers identifiers and paraphrases.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/hybrid-search.md).

## Why this exists

Hybrid search combines lexical and dense signals—often via reciprocal rank fusion—when neither alone covers identifiers and paraphrases.

## Core intuition

Fusion surfaces policy IDs lexically while keeping semantic matches for informal phrasing.

## Mechanics

1. Define the decision or system stage where hybrid search applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Show a query where lexical-only and dense-only each miss but fusion succeeds.

## Code practice

Run `python labs/0603-retrieval/main.py` from the repository root.

## When to use

Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.

## When not to use

Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Common misconceptions

- Higher embedding dimension always improves results.
- Vector search replaces the need for metadata filters.
- If retrieval returns something, the answer must be correct.

## Trade-offs

Hybrid Search improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: keywords and inverted indexes. Today: hybrid dense–lexical with rerankers. Tomorrow: agentic and graph-augmented retrieval. The durable principle is grounding generation in verifiable evidence.
