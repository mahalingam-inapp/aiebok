# Acceptance Criteria

**Purpose:** Reference card for **acceptance criteria** used across AIEBOK books and knowledge areas.

## Core explanation

Acceptance criteria are pass/fail conditions for feature completion—testable, unambiguous, tied to user value.

## Example

Given ambiguous date, system asks clarifying question rather than guessing—100% on test set.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Convert each criterion into an automated or manual test case with owner.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare acceptance criteria against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Evaluation Specs](../../concepts/cards/evaluation-specs.md)
- [Functional Specifications](../../concepts/cards/functional-specifications.md)
- [Prompt Specs](../../concepts/cards/prompt-specs.md)
- [Tool Contracts](../../concepts/cards/tool-contracts.md)

## Related chapters

- [02 Specification Driven Development](../../books/09-ai-software-and-product-engineering/02-specification-driven-development.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
