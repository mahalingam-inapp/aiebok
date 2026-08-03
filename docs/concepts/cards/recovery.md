# Recovery

**Purpose:** Reference card for **recovery** used across AIEBOK books and knowledge areas.

## Core explanation

Recovery restores consistent state after crashes, tool failures, or partial commits. It requires durable checkpoints and compensating actions.

## Example

After payment timeout, recovery verifies ledger state before retry or refund.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Inject crash at each step and verify recovery reaches consistent terminal state.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare recovery against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Action Spaces](../../concepts/cards/action-spaces.md)
- [Checkpoints](../../concepts/cards/checkpoints.md)
- [Compensation](../../concepts/cards/compensation.md)
- [Computer Use](../../concepts/cards/computer-use.md)

## Related chapters

- [03 Agent Memory And Recovery](../../books/08-agent-systems/03-agent-memory-and-recovery.md)
- [04 Computer Use And Embodied Action](../../books/13-multimodal-and-frontier-systems/04-computer-use-and-embodied-action.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
