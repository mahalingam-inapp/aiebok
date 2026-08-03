# Tool Schemas

**Purpose:** Reference card for **tool schemas** used across AIEBOK books and knowledge areas.

## Core explanation

Tool schemas define parameter names, types, required fields, and descriptions models use to construct calls. Ambiguous schemas cause systematic argument errors.

## Example

date_iso string format in schema prevents models passing 'next Tuesday' unparseably.

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

Measure argument validation failure rate per tool after schema revision.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare tool schemas against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Function Calling](../../concepts/cards/function-calling.md)
- [Idempotency](../../concepts/cards/idempotency.md)
- [Permissions](../../concepts/cards/permissions.md)
- [Timeouts](../../concepts/cards/timeouts.md)

## Related chapters

- [04 Tools As Capability Boundaries](../../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
