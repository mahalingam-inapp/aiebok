# Feedback

**Purpose:** Reference card for **feedback** used across AIEBOK books and knowledge areas.

## Core explanation

Feedback closes the loop: outcomes from actions update beliefs, models, or policies for subsequent decisions. Without feedback channels, the same mistakes repeat indefinitely.

## Example

Misrouted tickets returned by engineers should update routing features so the error rate on that category is trackable week over week.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Identify one feedback signal, where it is stored, and measure how many days until it influences the next decision.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare feedback against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bounded Rationality](../../concepts/cards/bounded-rationality.md)
- [Capability Decomposition](../../concepts/cards/capability-decomposition.md)
- [Goal Directed Behavior](../../concepts/cards/goal-directed-behavior.md)
- [Rational Agents](../../concepts/cards/rational-agents.md)

## Related chapters

- [01 What Intelligence Means](../../books/01-foundations-of-intelligence/01-what-intelligence-means.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
