# Adversarial Tests

**Purpose:** Reference card for **adversarial tests** used across AIEBOK books and knowledge areas.

## Core explanation

Adversarial tests probe injection, jailbreaks, edge inputs, and abuse scenarios. They belong in release gates for user-facing AI.

## Example

Prompt injection via ticket body attempting credential exfil must fail closed.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Maintain adversarial suite; require 100% pass on P0 cases before deploy.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare adversarial tests against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Contract Tests](../../concepts/cards/contract-tests.md)
- [Eval Datasets](../../concepts/cards/eval-datasets.md)
- [Release Gates](../../concepts/cards/release-gates.md)
- [Unit Tests](../../concepts/cards/unit-tests.md)

## Related chapters

- [04 Testing Ai Systems](../../books/09-ai-software-and-product-engineering/04-testing-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
