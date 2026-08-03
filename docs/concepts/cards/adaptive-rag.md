# Adaptive Rag

**Purpose:** Reference card for **adaptive rag** used across AIEBOK books and knowledge areas.

## Core explanation

Adaptive RAG chooses retrieval depth, query rewrite, or no retrieval based on question type and confidence. It saves cost on simple queries while going deep on hard ones.

## Example

Greetings skip retrieval; compliance questions trigger hybrid search plus rerank.

## When to use

Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.

## When not to use

Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Compare average latency and accuracy versus always-retrieve baseline on mixed query set.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare adaptive rag against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Authorization](../../concepts/cards/authorization.md)
- [Freshness](../../concepts/cards/freshness.md)
- [Graph Rag](../../concepts/cards/graph-rag.md)
- [Multi Hop Retrieval](../../concepts/cards/multi-hop-retrieval.md)

## Related chapters

- [06 Advanced And Enterprise Rag](../../books/06-knowledge-and-retrieval-systems/06-advanced-and-enterprise-rag.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
