# Rational Agents

**Purpose:** Reference card for **rational agents** used across AIEBOK books and knowledge areas.

## Core explanation

Rational agents choose actions that maximize expected utility toward a goal given perceived state and known constraints. The design question is whether the system's action policy aligns with business utility, not model confidence.

## Example

A lending assistant should prefer declining uncertain high-risk cases when false approvals cost more than false declines.

## When to use

Use when tasks require multi-step decisions, tool use, or recovery across variable inputs.

## When not to use

Skip when a deterministic workflow with fixed steps is clearer and safer.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Bound steps, cost, tools, and human approval for side effects.

## Evidence of understanding

Write the utility function and compare two candidate actions by expected cost, not by response fluency.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare rational agents against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bounded Rationality](../../concepts/cards/bounded-rationality.md)
- [Capability Decomposition](../../concepts/cards/capability-decomposition.md)
- [Feedback](../../concepts/cards/feedback.md)
- [Goal Directed Behavior](../../concepts/cards/goal-directed-behavior.md)

## Related chapters

- [01 What Intelligence Means](../../books/01-foundations-of-intelligence/01-what-intelligence-means.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
