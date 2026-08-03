# Cosine Similarity

**Purpose:** Reference card for **cosine similarity** used across AIEBOK books and knowledge areas.

## Core explanation

Cosine similarity measures the angle between vectors, ignoring magnitude—standard for normalized embeddings in retrieval.

## Example

Two policy summaries of different lengths can match semantically when cosine is high despite different norms.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Verify identical rankings after L2-normalizing embeddings versus raw cosine computation.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare cosine similarity against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ann Indexes](../../concepts/cards/ann-indexes.md)
- [Dot Product](../../concepts/cards/dot-product.md)
- [Metadata Filtering](../../concepts/cards/metadata-filtering.md)
- [Nearest Neighbors](../../concepts/cards/nearest-neighbors.md)

## Related chapters

- [05 Similarity And Vector Search](../../books/03-language-and-representation/05-similarity-and-vector-search.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
