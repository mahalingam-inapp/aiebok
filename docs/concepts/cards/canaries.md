# Canaries

**Purpose:** Reference card for **canaries** used across AIEBOK books and knowledge areas.

## Core explanation

Canaries route small traffic percentage to new versions before full rollout.

## Example

5% traffic to new embedding index for 24h comparing recall and latency.

## Evidence of understanding

Auto-rollback canary if error rate or primary metric degrades beyond bound.

## Trade-offs

No mechanism is universal. Compare canaries against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
