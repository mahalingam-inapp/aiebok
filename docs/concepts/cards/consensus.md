# Consensus

**Purpose:** Reference card for **consensus** used across AIEBOK books and knowledge areas.

## Core explanation

Consensus protocols align multiple agents on a decision before action—voting, debate, or judge model. Useful when single-agent judgment is unreliable.

## Example

Three agents vote on classification before automated ticket routing proceeds.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare accuracy of consensus versus single agent on ambiguous case set.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare consensus against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Coordination](../../concepts/cards/coordination.md)
- [Delegation](../../concepts/cards/delegation.md)
- [Role Isolation](../../concepts/cards/role-isolation.md)
- [Shared State](../../concepts/cards/shared-state.md)

## Related chapters

- [05 Multi Agent Systems](../../books/08-agent-systems/05-multi-agent-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
