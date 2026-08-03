# Release Gates

**Purpose:** Reference card for **release gates** used across AIEBOK books and knowledge areas.

## Core explanation

Release gates block deployment until eval, security, and performance criteria pass. They encode organizational risk tolerance numerically.

## Example

No deploy if faithfulness drops >2 points or p95 latency exceeds SLO.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Automate gate checks in CI/CD with auditable pass/fail artifacts.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare release gates against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Adversarial Tests](../../concepts/cards/adversarial-tests.md)
- [Contract Tests](../../concepts/cards/contract-tests.md)
- [Eval Datasets](../../concepts/cards/eval-datasets.md)
- [Unit Tests](../../concepts/cards/unit-tests.md)

## Related chapters

- [04 Testing Ai Systems](../../books/09-ai-software-and-product-engineering/04-testing-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
