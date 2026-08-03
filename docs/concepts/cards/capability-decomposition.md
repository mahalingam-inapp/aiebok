# Capability Decomposition

**Purpose:** Reference card for **capability decomposition** used across AIEBOK books and knowledge areas.

## Core explanation

Capability decomposition splits intelligence into perception, memory, learning, planning, and action so teams can own, test, and debug each part. Without it, fluent outputs hide which capability failed.

## Example

Incident routing can fail in classification while generation still reads naturally—decomposition exposes the failing box.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Draw a capability map and mark which component owns each failure from a real incident postmortem.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare capability decomposition against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bounded Rationality](../../concepts/cards/bounded-rationality.md)
- [Feedback](../../concepts/cards/feedback.md)
- [Goal Directed Behavior](../../concepts/cards/goal-directed-behavior.md)
- [Rational Agents](../../concepts/cards/rational-agents.md)

## Related chapters

- [01 What Intelligence Means](../../books/01-foundations-of-intelligence/01-what-intelligence-means.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
