# Graph Rag

**Purpose:** Reference card for **graph rag** used across AIEBOK books and knowledge areas.

## Core explanation

Graph RAG combines knowledge graphs with retrieval so multi-hop relations traverse explicit edges. It helps when answers require chained entity relationships.

## Example

'Which vendor supplies part X used in product Y?' may need graph traversal, not one vector search.

## Evidence of understanding

Compare multi-hop question accuracy versus flat chunk retrieval on ten linked-entity queries.

## Trade-offs

No mechanism is universal. Compare graph rag against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
