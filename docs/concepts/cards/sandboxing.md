# Sandboxing

**Purpose:** Reference card for **sandboxing** used across AIEBOK books and knowledge areas.

## Core explanation

Sandboxing isolates code execution, browsing, or file access in restricted environments with network and filesystem limits.

## Example

Python tool runs in container without egress except allowlisted APIs.

## Evidence of understanding

Attempt filesystem and network escapes in sandbox test suite monthly.

## Trade-offs

No mechanism is universal. Compare sandboxing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
