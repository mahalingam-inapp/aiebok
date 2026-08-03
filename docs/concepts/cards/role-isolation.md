# Role Isolation

**Purpose:** Reference card for **role isolation** used across AIEBOK books and knowledge areas.

## Core explanation

Role isolation restricts each agent to tools and data matching its role, limiting blast radius of compromise or error.

## Example

Billing agent cannot access HR records even if prompt requests it.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Attempt cross-role tool access in tests and expect hard denial.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare role isolation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Consensus](../../concepts/cards/consensus.md)
- [Coordination](../../concepts/cards/coordination.md)
- [Delegation](../../concepts/cards/delegation.md)
- [Shared State](../../concepts/cards/shared-state.md)

## Related chapters

- [05 Multi Agent Systems](../../books/08-agent-systems/05-multi-agent-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
