# Approval Gates

**Purpose:** Reference card for **approval gates** used across AIEBOK books and knowledge areas.

## Core explanation

Approval gates pause execution until authorized humans confirm high-impact actions. They convert autonomy into supervised autonomy.

## Example

Production deploy agent waits for manager click before kubectl apply.

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

Verify gate cannot be bypassed via prompt injection or direct tool URL.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare approval gates against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Planner Executor](../../concepts/cards/planner-executor.md)
- [Reviewer](../../concepts/cards/reviewer.md)
- [Routing](../../concepts/cards/routing.md)
- [Supervisor Worker](../../concepts/cards/supervisor-worker.md)

## Related chapters

- [04 Agent Patterns](../../books/08-agent-systems/04-agent-patterns.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
