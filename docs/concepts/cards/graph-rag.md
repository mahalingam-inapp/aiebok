# Graph Rag

**Purpose:** Reference card for **graph rag** used across AIEBOK books and knowledge areas.

## Core explanation

Graph RAG combines knowledge graphs with retrieval so multi-hop relations traverse explicit edges. It helps when answers require chained entity relationships.

## Example

'Which vendor supplies part X used in product Y?' may need graph traversal, not one vector search.

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

Compare multi-hop question accuracy versus flat chunk retrieval on ten linked-entity queries.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare graph rag against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Adaptive Rag](../../concepts/cards/adaptive-rag.md)
- [Authorization](../../concepts/cards/authorization.md)
- [Freshness](../../concepts/cards/freshness.md)
- [Multi Hop Retrieval](../../concepts/cards/multi-hop-retrieval.md)

## Related chapters

- [06 Advanced And Enterprise Rag](../../books/06-knowledge-and-retrieval-systems/06-advanced-and-enterprise-rag.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
