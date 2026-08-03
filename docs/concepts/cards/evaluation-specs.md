# Evaluation Specs

**Purpose:** Reference card for **evaluation specs** used across AIEBOK books and knowledge areas.

## Core explanation

Evaluation specs define datasets, metrics, slices, and release thresholds before shipping. They turn 'good enough' into numbers.

## Example

Eval spec: 200 cases, faithfulness ≥ 0.9, P0 safety cases 100% pass.

## Evidence of understanding

Block merge if eval spec checklist incomplete in release ticket.

## Trade-offs

No mechanism is universal. Compare evaluation specs against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
