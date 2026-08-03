# Tests

**Purpose:** Reference card for **tests** used across AIEBOK books and knowledge areas.

## Core explanation

Tests provide executable specifications for tools, plans, and outputs in reasoning pipelines. They turn vague correctness into pass/fail signals.

## Example

A migration plan test asserts rollback step exists before destructive changes.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run test suite on every candidate plan and require 100% pass before execution.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare tests against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Best Of N](../../concepts/cards/best-of-n.md)
- [Critique](../../concepts/cards/critique.md)
- [Self Consistency](../../concepts/cards/self-consistency.md)
- [Verifiers](../../concepts/cards/verifiers.md)

## Related chapters

- [03 Verification And Critique](../../books/07-reasoning-and-tool-use/03-verification-and-critique.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
