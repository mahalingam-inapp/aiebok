# Cosine Similarity

**Purpose:** Reference card for **cosine similarity** used across AIEBOK books and knowledge areas.

## Core explanation

Cosine similarity measures the angle between vectors, ignoring magnitude—standard for normalized embeddings in retrieval.

## Example

Two policy summaries of different lengths can match semantically when cosine is high despite different norms.

## Evidence of understanding

Verify identical rankings after L2-normalizing embeddings versus raw cosine computation.

## Trade-offs

No mechanism is universal. Compare cosine similarity against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
