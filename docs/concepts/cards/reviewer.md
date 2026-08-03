# Reviewer

**Purpose:** Reference card for **reviewer** used across AIEBOK books and knowledge areas.

## Core explanation

Reviewer pattern inserts a critique pass before delivery or irreversible actions. Reviewers should use different prompts or models than generators.

## Example

Draft email reviewed for PII leakage before send tool invocation.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure defect catch rate with reviewer on versus off at equal total latency budget.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare reviewer against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Approval Gates](../../concepts/cards/approval-gates.md)
- [Planner Executor](../../concepts/cards/planner-executor.md)
- [Routing](../../concepts/cards/routing.md)
- [Supervisor Worker](../../concepts/cards/supervisor-worker.md)

## Related chapters

- [04 Agent Patterns](../../books/08-agent-systems/04-agent-patterns.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
