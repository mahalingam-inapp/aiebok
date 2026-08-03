# Resources

**Purpose:** Reference card for **resources** used across AIEBOK books and knowledge areas.

## Core explanation

MCP resources expose readable data—files, records, configs—to clients with URI identifiers. Resource access must respect same authorization as APIs.

## Example

resource://policy/2024 exposes the PDF bytes; listing must not leak unauthorized URIs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Enumerate resources as unprivileged user and confirm restricted URIs are absent.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare resources against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Authentication](../../concepts/cards/authentication.md)
- [Mcp](../../concepts/cards/mcp.md)
- [Tool Discovery](../../concepts/cards/tool-discovery.md)
- [Transports](../../concepts/cards/transports.md)

## Related chapters

- [05 Mcp And Integration Protocols](../../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
