# Data Mixtures

**Purpose:** Reference card for **data mixtures** used across AIEBOK books and knowledge areas.

## Core explanation

Data mixtures blend corpora—web, code, books, dialog—at tuned ratios during pretraining. Mixture proportions strongly affect capabilities and biases.

## Example

Over-weighting code improves programming but may hurt conversational tone.

## Evidence of understanding

Ablate one corpus slice from the mixture and measure task-specific eval deltas.

## Trade-offs

No mechanism is universal. Compare data mixtures against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
