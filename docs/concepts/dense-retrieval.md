# Dense Retrieval

**Purpose:** Dense retrieval embeds queries and documents into the same vector space and returns nearest neighbors by similarity.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/dense-retrieval.md).

## Why this exists

Dense retrieval embeds queries and documents into the same vector space and returns nearest neighbors by similarity.

## Core intuition

A query about 'application unavailable' retrieves 'service is down' without lexical overlap.

## Mechanics

1. Define the decision or system stage where dense retrieval applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Build a 30-query eval with paraphrases and hard negatives; report recall@5 and MRR.

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

Dense Retrieval improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: keywords and inverted indexes. Today: hybrid dense–lexical with rerankers. Tomorrow: agentic and graph-augmented retrieval. The durable principle is grounding generation in verifiable evidence.
