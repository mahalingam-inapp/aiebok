# Delegation

**Purpose:** Reference card for **delegation** used across AIEBOK books and knowledge areas.

## Core explanation

Delegation assigns subtasks to specialized agents or tools with scoped permissions. Poor delegation boundaries cause duplicated work or authority gaps.

## Example

Legal sub-agent handles contract clauses; main agent cannot invoke legal tools directly.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Audit delegation graph for cycles and privilege escalation paths.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare delegation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Consensus](../../concepts/cards/consensus.md)
- [Coordination](../../concepts/cards/coordination.md)
- [Role Isolation](../../concepts/cards/role-isolation.md)
- [Shared State](../../concepts/cards/shared-state.md)

## Related chapters

- [05 Multi Agent Systems](../../books/08-agent-systems/05-multi-agent-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
