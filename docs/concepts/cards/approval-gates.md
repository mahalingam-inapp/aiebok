# Approval Gates

**Purpose:** Reference card for **approval gates** used across AIEBOK books and knowledge areas.

## Core explanation

Approval gates pause execution until authorized humans confirm high-impact actions. They convert autonomy into supervised autonomy.

## Example

Production deploy agent waits for manager click before kubectl apply.

## Evidence of understanding

Verify gate cannot be bypassed via prompt injection or direct tool URL.

## Trade-offs

No mechanism is universal. Compare approval gates against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
