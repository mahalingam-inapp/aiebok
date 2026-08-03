# Baseline Workflow

**Purpose:** Reference card for **baseline workflow** used across AIEBOK books and knowledge areas.

## Core explanation

Baseline workflow documents how users solve the task today—time, errors, tools—before AI intervention. Improvement requires beating this baseline.

## Example

Manual ticket tagging takes 45s each; AI must beat accuracy and time with correction cost included.

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

Measure baseline task time and error rate on ten representative sessions.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare baseline workflow against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Feasibility](../../concepts/cards/feasibility.md)
- [Jobs To Be Done](../../concepts/cards/jobs-to-be-done.md)
- [Success Metrics](../../concepts/cards/success-metrics.md)
- [User Research](../../concepts/cards/user-research.md)

## Related chapters

- [01 Discovering The Right Problem](../../books/09-ai-software-and-product-engineering/01-discovering-the-right-problem.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
