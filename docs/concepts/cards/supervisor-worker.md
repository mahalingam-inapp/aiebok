# Supervisor Worker

**Purpose:** Reference card for **supervisor worker** used across AIEBOK books and knowledge areas.

## Core explanation

Supervisor–worker assigns subtasks to workers and integrates results, adding coordination overhead for parallelizable work.

## Example

Supervisor delegates research subtopics to three workers, then merges citations.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare wall time and error rate versus single agent with sequential tool calls.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare supervisor worker against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Approval Gates](../../concepts/cards/approval-gates.md)
- [Planner Executor](../../concepts/cards/planner-executor.md)
- [Reviewer](../../concepts/cards/reviewer.md)
- [Routing](../../concepts/cards/routing.md)

## Related chapters

- [04 Agent Patterns](../../books/08-agent-systems/04-agent-patterns.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
