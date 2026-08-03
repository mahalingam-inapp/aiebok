# Workflows

**Purpose:** Reference card for **workflows** used across AIEBOK books and knowledge areas.

## Core explanation

Workflows are deterministic orchestrations with predefined steps, branches, and error handlers. They excel when paths are known and compliance requires repeatability.

## Example

Invoice approval always follows submit → manager → finance with explicit gates.

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

Measure success rate and change failure rate versus agent on identical structured tasks.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare workflows against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Agency](../../concepts/cards/agency.md)
- [Autonomy](../../concepts/cards/autonomy.md)
- [Control](../../concepts/cards/control.md)
- [State Machines](../../concepts/cards/state-machines.md)

## Related chapters

- [01 Agent Or Workflow](../../books/08-agent-systems/01-agent-or-workflow.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
