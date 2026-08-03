# Prompt Specs

**Purpose:** Reference card for **prompt specs** used across AIEBOK books and knowledge areas.

## Core explanation

Prompt specs version instructions, constraints, examples, and expected behaviors like API contracts. They enable review and regression unlike ad hoc prompts.

## Example

Prompt spec defines abstention when confidence low and JSON schema for outputs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Diff prompt spec versions in CI and run regression eval on every change.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare prompt specs against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Acceptance Criteria](../../concepts/cards/acceptance-criteria.md)
- [Evaluation Specs](../../concepts/cards/evaluation-specs.md)
- [Functional Specifications](../../concepts/cards/functional-specifications.md)
- [Tool Contracts](../../concepts/cards/tool-contracts.md)

## Related chapters

- [02 Specification Driven Development](../../books/09-ai-software-and-product-engineering/02-specification-driven-development.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
