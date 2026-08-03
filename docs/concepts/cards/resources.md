# Resources

**Purpose:** Reference card for **resources** used across AIEBOK books and knowledge areas.

## Core explanation

MCP resources expose readable data—files, records, configs—to clients with URI identifiers. Resource access must respect same authorization as APIs.

## Example

resource://policy/2024 exposes the PDF bytes; listing must not leak unauthorized URIs.

## Evidence of understanding

Enumerate resources as unprivileged user and confirm restricted URIs are absent.

## Trade-offs

No mechanism is universal. Compare resources against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
