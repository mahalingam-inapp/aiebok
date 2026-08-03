# Dot Product

**Purpose:** Reference card for **dot product** used across AIEBOK books and knowledge areas.

## Core explanation

Dot product measures alignment between vectors—used in attention scores and similarity when magnitudes carry signal. Scale affects ranking unless normalized.

## Example

Unnormalized dot products favor longer document embeddings; cosine similarity removes length bias.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare ranking order for ten queries using dot product versus cosine on the same vectors.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare dot product against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ann Indexes](../../concepts/cards/ann-indexes.md)
- [Cosine Similarity](../../concepts/cards/cosine-similarity.md)
- [Metadata Filtering](../../concepts/cards/metadata-filtering.md)
- [Nearest Neighbors](../../concepts/cards/nearest-neighbors.md)

## Related chapters

- [05 Similarity And Vector Search](../../books/03-language-and-representation/05-similarity-and-vector-search.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
