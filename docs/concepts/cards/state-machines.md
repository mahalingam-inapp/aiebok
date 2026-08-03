# State Machines

**Purpose:** Reference card for **state machines** used across AIEBOK books and knowledge areas.

## Core explanation

State machines model allowed statuses and transitions explicitly, making illegal steps unrepresentable. They clarify where agents pause, resume, or terminate.

## Example

Ticket automation states: open → pending_approval → resolved with defined transition triggers.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Draw state diagram and verify code rejects all undefined transitions in tests.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare state machines against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Agency](../../concepts/cards/agency.md)
- [Autonomy](../../concepts/cards/autonomy.md)
- [Control](../../concepts/cards/control.md)
- [Workflows](../../concepts/cards/workflows.md)

## Related chapters

- [01 Agent Or Workflow](../../books/08-agent-systems/01-agent-or-workflow.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
