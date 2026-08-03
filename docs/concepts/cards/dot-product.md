# Dot Product

**Purpose:** Reference card for **dot product** used across AIEBOK books and knowledge areas.

## Core explanation

Dot product measures alignment between vectors—used in attention scores and similarity when magnitudes carry signal. Scale affects ranking unless normalized.

## Example

Unnormalized dot products favor longer document embeddings; cosine similarity removes length bias.

## Evidence of understanding

Compare ranking order for ten queries using dot product versus cosine on the same vectors.

## Trade-offs

No mechanism is universal. Compare dot product against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
