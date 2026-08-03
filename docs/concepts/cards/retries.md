# Retries

**Purpose:** Reference card for **retries** used across AIEBOK books and knowledge areas.

## Core explanation

Retries re-invoke models or tools after transient failures or validation misses, with backoff and limits. Unbounded retries cause runaway cost and duplicate side effects.

## Example

Three retries with exponential backoff on 429 rate limits recover most requests without overload.

## Evidence of understanding

Cap retries at N and measure success rate versus total token spend.

## Trade-offs

No mechanism is universal. Compare retries against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
