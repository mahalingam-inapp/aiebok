# Transports

**Purpose:** Reference card for **transports** used across AIEBOK books and knowledge areas.

## Core explanation

MCP transports—stdio, SSE, HTTP—carry protocol messages between clients and servers. Choice affects latency, deployment, and security boundaries.

## Example

Stdio suits local IDE agents; SSE suits remote servers behind auth proxies.

## Evidence of understanding

Measure round-trip latency for tool call over each transport in your deployment.

## Trade-offs

No mechanism is universal. Compare transports against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
