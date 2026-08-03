# Position

**Purpose:** Reference card for **position** used across AIEBOK books and knowledge areas.

## Core explanation

Position information tells transformers token order since self-attention is permutation-invariant without it. Methods include sinusoidal, learned, and rotary (RoPE) encodings.

## Example

Rotary embeddings encode relative position in Q/K products for long-context models.

## Evidence of understanding

Shuffle token order without position encodings and observe catastrophic perplexity increase.

## Trade-offs

No mechanism is universal. Compare position against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
