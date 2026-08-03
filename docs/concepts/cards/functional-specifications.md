# Functional Specifications

**Purpose:** Reference card for **functional specifications** used across AIEBOK books and knowledge areas.

## Core explanation

Functional specifications describe observable system behavior—inputs, outputs, errors—for builders and testers. They precede implementation and model choice.

## Example

Spec states: given valid invoice PDF, return JSON with vendor, total, date or structured error code.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Write acceptance examples as executable tests before coding.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare functional specifications against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Acceptance Criteria](../../concepts/cards/acceptance-criteria.md)
- [Evaluation Specs](../../concepts/cards/evaluation-specs.md)
- [Prompt Specs](../../concepts/cards/prompt-specs.md)
- [Tool Contracts](../../concepts/cards/tool-contracts.md)

## Related chapters

- [02 Specification Driven Development](../../books/09-ai-software-and-product-engineering/02-specification-driven-development.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
