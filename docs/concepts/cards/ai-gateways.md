# Ai Gateways

**Purpose:** Reference card for **ai gateways** used across AIEBOK books and knowledge areas.

## Core explanation

AI gateways centralize model access with auth, rate limits, logging, routing, and policy enforcement for enterprise teams.

## Example

All Bedrock and OpenAI calls flow through gateway applying PII scrub and budget caps.

## Evidence of understanding

Block direct model endpoint access; verify 100% traffic appears in gateway logs.

## Trade-offs

No mechanism is universal. Compare ai gateways against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
