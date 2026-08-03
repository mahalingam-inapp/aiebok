# Fallbacks

**Purpose:** Reference card for **fallbacks** used across AIEBOK books and knowledge areas.

## Core explanation

Fallbacks switch to alternate models, cached answers, or human handoff when primary path fails.

## Example

If primary API 503, serve smaller local model with degraded-quality banner.

## Evidence of understanding

Chaos-test primary failure; verify fallback activates within SLA with metric logged.

## Trade-offs

No mechanism is universal. Compare fallbacks against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
