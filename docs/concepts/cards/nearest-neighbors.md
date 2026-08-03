# Nearest Neighbors

**Purpose:** Reference card for **nearest neighbors** used across AIEBOK books and knowledge areas.

## Core explanation

Nearest-neighbor search returns the closest vectors to a query by a chosen metric. Exact search is fine for small indexes; production scales require approximate methods.

## Example

Brute-force cosine over 10k chunks is fast; at 10M you need ANN indexes with recall trade-offs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure recall@10 of ANN versus exact search on a held-out query set.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare nearest neighbors against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ann Indexes](../../concepts/cards/ann-indexes.md)
- [Cosine Similarity](../../concepts/cards/cosine-similarity.md)
- [Dot Product](../../concepts/cards/dot-product.md)
- [Metadata Filtering](../../concepts/cards/metadata-filtering.md)

## Related chapters

- [05 Similarity And Vector Search](../../books/03-language-and-representation/05-similarity-and-vector-search.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
