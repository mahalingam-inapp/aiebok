# Rational Agents

**Purpose:** Reference card for **rational agents** used across AIEBOK books and knowledge areas.

## Core explanation

Rational agents choose actions that maximize expected utility toward a goal given perceived state and known constraints. The design question is whether the system's action policy aligns with business utility, not model confidence.

## Example

A lending assistant should prefer declining uncertain high-risk cases when false approvals cost more than false declines.

## Evidence of understanding

Write the utility function and compare two candidate actions by expected cost, not by response fluency.

## Trade-offs

No mechanism is universal. Compare rational agents against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
