# Hybrid Search

**Purpose:** Reference card for **hybrid search** used across AIEBOK books and knowledge areas.

## Core explanation

Hybrid search combines lexical and dense signals—often via reciprocal rank fusion—when neither alone covers identifiers and paraphrases.

## Example

Fusion surfaces policy IDs lexically while keeping semantic matches for informal phrasing.

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

Show a query where lexical-only and dense-only each miss but fusion succeeds.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare hybrid search against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bm25](../../concepts/cards/bm25.md)
- [Dense Retrieval](../../concepts/cards/dense-retrieval.md)
- [Parent Child Retrieval](../../concepts/cards/parent-child-retrieval.md)
- [Query Rewriting](../../concepts/cards/query-rewriting.md)

## Related chapters

- [03 Retrieval](../../books/06-knowledge-and-retrieval-systems/03-retrieval.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
