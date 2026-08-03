# Leases

**Purpose:** Reference card for **leases** used across AIEBOK books and knowledge areas.

## Core explanation

Leases grant temporary exclusive ownership of a resource—document, ticket, shard—preventing duplicate processing. Expired leases must reclaim safely.

## Example

Worker holds 60s lease on ticket; another worker picks up only after lease expiry.

## Evidence of understanding

Simulate worker death before lease expiry and verify safe reassignment.

## Trade-offs

No mechanism is universal. Compare leases against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
