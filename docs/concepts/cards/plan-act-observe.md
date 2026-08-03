# Plan Act Observe

**Purpose:** Reference card for **plan act observe** used across AIEBOK books and knowledge areas.

## Core explanation

Plan–act–observe separates choosing the next action, executing it, and recording observations that update state.

## Example

Agent plans 'create draft', executes, observes 'draft id=7', then plans verification instead of repeating creation.

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

Log each cycle and show observations change subsequent plans, not identical repeats.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare plan act observe against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Budgets](../../concepts/cards/budgets.md)
- [Reflection](../../concepts/cards/reflection.md)
- [State](../../concepts/cards/state.md)
- [Termination](../../concepts/cards/termination.md)

## Related chapters

- [02 The Agent Loop](../../books/08-agent-systems/02-the-agent-loop.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
