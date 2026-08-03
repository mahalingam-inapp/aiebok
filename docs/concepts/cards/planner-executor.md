# Planner Executor

**Purpose:** Reference card for **planner executor** used across AIEBOK books and knowledge areas.

## Core explanation

Planner–executor splits strategic planning from tactical execution, often with different models or prompts. Plans can be validated before expensive actions.

## Example

Planner outputs step graph; executor calls tools one step at a time with verification.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure plan validity rate and end-to-end success versus monolithic agent.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare planner executor against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Approval Gates](../../concepts/cards/approval-gates.md)
- [Reviewer](../../concepts/cards/reviewer.md)
- [Routing](../../concepts/cards/routing.md)
- [Supervisor Worker](../../concepts/cards/supervisor-worker.md)

## Related chapters

- [04 Agent Patterns](../../books/08-agent-systems/04-agent-patterns.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
