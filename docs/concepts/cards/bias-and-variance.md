# Bias And Variance

**Purpose:** Reference card for **bias and variance** used across AIEBOK books and knowledge areas.

## Core explanation

Bias is systematic underfitting from overly simple models; variance is sensitivity to training noise from overly complex ones. Tuning trades these errors against compute and data volume.

## Example

A linear model underfits nonlinear fraud patterns (high bias); a huge tree overfits small samples (high variance).

## Evidence of understanding

Plot error versus model capacity and identify the knee where validation error stops improving.

## Trade-offs

No mechanism is universal. Compare bias and variance against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
