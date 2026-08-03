# Mcp

**Purpose:** Reference card for **mcp** used across AIEBOK books and knowledge areas.

## Core explanation

Model Context Protocol standardizes how clients discover tools, resources, and prompts from servers. It reduces bespoke integration code but not trust decisions.

## Example

An MCP server exposes filesystem read tools; the client still enforces path allowlists.

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

Connect a hostile client and verify server rejects out-of-scope resource requests.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare mcp against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Authentication](../../concepts/cards/authentication.md)
- [Resources](../../concepts/cards/resources.md)
- [Tool Discovery](../../concepts/cards/tool-discovery.md)
- [Transports](../../concepts/cards/transports.md)

## Related chapters

- [05 Mcp And Integration Protocols](../../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
