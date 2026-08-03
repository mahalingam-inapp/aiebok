# Diversity

**Purpose:** Reference card for **diversity** used across AIEBOK books and knowledge areas.

## Core explanation

Diversity in context selection avoids redundant passages that waste tokens on repeated facts. Maximal marginal relevance is a common heuristic.

## Example

Three chunks saying the same PTO limit add no value; one plus related exceptions is better.

## Evidence of understanding

Compare unique fact coverage at fixed token budget with and without MMR selection.

## Trade-offs

No mechanism is universal. Compare diversity against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
