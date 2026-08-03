# Ann Indexes

**Purpose:** Reference card for **ann indexes** used across AIEBOK books and knowledge areas.

## Core explanation

Approximate nearest neighbor indexes—HNSW, IVF, LSH—trade recall for speed at million-plus scale. Index parameters must be tuned on representative queries.

## Example

HNSW with efSearch=100 may hit 98% recall@10 at 5ms versus 50ms exact on 1M vectors.

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

Plot latency versus recall@k for three index configurations on production query sample.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare ann indexes against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Cosine Similarity](../../concepts/cards/cosine-similarity.md)
- [Dot Product](../../concepts/cards/dot-product.md)
- [Metadata Filtering](../../concepts/cards/metadata-filtering.md)
- [Nearest Neighbors](../../concepts/cards/nearest-neighbors.md)

## Related chapters

- [05 Similarity And Vector Search](../../books/03-language-and-representation/05-similarity-and-vector-search.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
