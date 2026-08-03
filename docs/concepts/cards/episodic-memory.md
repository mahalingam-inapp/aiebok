# Episodic Memory

**Purpose:** Reference card for **episodic memory** used across AIEBOK books and knowledge areas.

## Core explanation

Episodic memory stores past run trajectories—what was tried, what failed—for future reference within or across sessions.

## Example

Remembering last week's failed migration path prevents repeating the same broken sequence.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Retrieve relevant episodes for similar goals and measure retry avoidance rate.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare episodic memory against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Checkpoints](../../concepts/cards/checkpoints.md)
- [Compensation](../../concepts/cards/compensation.md)
- [Idempotency](../../concepts/cards/idempotency.md)
- [Recovery](../../concepts/cards/recovery.md)

## Related chapters

- [03 Agent Memory And Recovery](../../books/08-agent-systems/03-agent-memory-and-recovery.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
