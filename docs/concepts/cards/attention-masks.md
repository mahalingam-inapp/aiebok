# Attention Masks

**Purpose:** Reference card for **attention masks** used across AIEBOK books and knowledge areas.

## Core explanation

Attention masks zero out disallowed positions—future tokens in decoding, padding, or cross-segment boundaries. Masks enforce causality and ignore irrelevant tokens.

## Example

Causal masks prevent a language model from peeking at answer tokens during training.

## Evidence of understanding

Apply a causal mask and confirm no weight connects position i to j > i.

## Trade-offs

No mechanism is universal. Compare attention masks against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
