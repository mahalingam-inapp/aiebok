# Shared State

**Purpose:** Reference card for **shared state** used across AIEBOK books and knowledge areas.

## Core explanation

Shared state stores variables visible to multiple agents—task boards, evidence pools. Consistency requires versioning or transactional updates.

## Example

Research evidence store accumulates URLs all workers cite; stale entries need TTL.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Verify concurrent writes do not lose updates using version counters or locks.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare shared state against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Consensus](../../concepts/cards/consensus.md)
- [Coordination](../../concepts/cards/coordination.md)
- [Delegation](../../concepts/cards/delegation.md)
- [Role Isolation](../../concepts/cards/role-isolation.md)

## Related chapters

- [05 Multi Agent Systems](../../books/08-agent-systems/05-multi-agent-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
