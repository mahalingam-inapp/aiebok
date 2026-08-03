# Bounded Rationality

**Purpose:** Reference card for **bounded rationality** used across AIEBOK books and knowledge areas.

## Core explanation

Bounded rationality acknowledges limited compute, time, memory, and information—systems must satisfice within budgets. Production AI rarely has the luxury of exhaustive search or perfect retrieval.

## Example

An on-call copilot stops after three retrieval attempts within a 5-second latency SLO instead of searching until theoretical certainty.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Document the stopping budget and demonstrate a case where more compute would help but violates the SLO.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare bounded rationality against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Capability Decomposition](../../concepts/cards/capability-decomposition.md)
- [Feedback](../../concepts/cards/feedback.md)
- [Goal Directed Behavior](../../concepts/cards/goal-directed-behavior.md)
- [Rational Agents](../../concepts/cards/rational-agents.md)

## Related chapters

- [01 What Intelligence Means](../../books/01-foundations-of-intelligence/01-what-intelligence-means.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
