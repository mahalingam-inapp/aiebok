# Unit Tests

**Purpose:** Reference card for **unit tests** used across AIEBOK books and knowledge areas.

## Core explanation

Unit tests verify deterministic functions and components in isolation with fast feedback. They anchor quality while model behavior stays statistical.

## Example

Parser unit tests cover edge cases agents might not consider when editing.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Require ≥80% coverage on changed deterministic modules per PR policy.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare unit tests against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Adversarial Tests](../../concepts/cards/adversarial-tests.md)
- [Contract Tests](../../concepts/cards/contract-tests.md)
- [Eval Datasets](../../concepts/cards/eval-datasets.md)
- [Release Gates](../../concepts/cards/release-gates.md)

## Related chapters

- [04 Testing Ai Systems](../../books/09-ai-software-and-product-engineering/04-testing-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
