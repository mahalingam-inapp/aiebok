# Verifiers

**Purpose:** Reference card for **verifiers** used across AIEBOK books and knowledge areas.

## Core explanation

Verifiers check candidate outputs with independent logic—unit tests, schemas, calculators—not the same model that generated them.

## Example

A Python assert verifies JSON plan steps include all required migration phases.

## Evidence of understanding

Report verifier catch rate on intentionally corrupted candidate outputs.

## Trade-offs

No mechanism is universal. Compare verifiers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
