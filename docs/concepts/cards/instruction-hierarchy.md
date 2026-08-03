# Instruction Hierarchy

**Purpose:** Reference card for **instruction hierarchy** used across AIEBOK books and knowledge areas.

## Core explanation

Instruction hierarchy ranks system, developer, and user messages so lower-priority text cannot override safety or policy. It is essential when untrusted content appears in context.

## Example

Retrieved web pages must not outrank the system prompt forbidding credential disclosure.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Inject conflicting instructions at each level and verify system policy wins.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare instruction hierarchy against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Constraints](../../concepts/cards/constraints.md)
- [Delimiters](../../concepts/cards/delimiters.md)
- [Few Shot Examples](../../concepts/cards/few-shot-examples.md)
- [Roles](../../concepts/cards/roles.md)

## Related chapters

- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
