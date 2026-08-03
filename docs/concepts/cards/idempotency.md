# Idempotency

**Purpose:** Reference card for **idempotency** used across AIEBOK books and knowledge areas.

## Core explanation

Idempotent tools produce the same effect when called repeatedly with the same idempotency key. Agents retry safely only when tools support this.

## Example

create_ticket with idempotency key 'abc' must not spawn duplicate tickets on retry.

## Evidence of understanding

Call the same tool twice with identical keys and verify single side effect.

## Trade-offs

No mechanism is universal. Compare idempotency against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
