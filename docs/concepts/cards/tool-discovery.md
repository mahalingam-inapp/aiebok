# Tool Discovery

**Purpose:** Reference card for **tool discovery** used across AIEBOK books and knowledge areas.

## Core explanation

Tool discovery lets clients list available tools and schemas at runtime instead of hardcoding integrations. Discovery responses must be filtered by permission.

## Example

A client sees only search_docs, not admin_delete, when connected with read-only scope.

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

Compare discovered tool list across role configurations in automated tests.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare tool discovery against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Authentication](../../concepts/cards/authentication.md)
- [Mcp](../../concepts/cards/mcp.md)
- [Resources](../../concepts/cards/resources.md)
- [Transports](../../concepts/cards/transports.md)

## Related chapters

- [05 Mcp And Integration Protocols](../../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
