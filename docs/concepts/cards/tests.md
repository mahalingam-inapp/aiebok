# Tests

**Purpose:** Reference card for **tests** used across AIEBOK books and knowledge areas.

## Core explanation

Tests provide executable specifications for tools, plans, and outputs in reasoning pipelines. They turn vague correctness into pass/fail signals.

## Example

A migration plan test asserts rollback step exists before destructive changes.

## Evidence of understanding

Run test suite on every candidate plan and require 100% pass before execution.

## Trade-offs

No mechanism is universal. Compare tests against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
