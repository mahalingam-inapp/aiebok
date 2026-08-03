# Mcp

**Purpose:** Reference card for **mcp** used across AIEBOK books and knowledge areas.

## Core explanation

Model Context Protocol standardizes how clients discover tools, resources, and prompts from servers. It reduces bespoke integration code but not trust decisions.

## Example

An MCP server exposes filesystem read tools; the client still enforces path allowlists.

## Evidence of understanding

Connect a hostile client and verify server rejects out-of-scope resource requests.

## Trade-offs

No mechanism is universal. Compare mcp against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
