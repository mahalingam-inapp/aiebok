# Model Registry

**Purpose:** Reference card for **model registry** used across AIEBOK books and knowledge areas.

## Core explanation

A model registry stores versioned models with stage labels—staging, production, archived—and metadata for audit. It is the handoff point between ML and serving teams.

## Example

Promoting v3.2 to production requires passing eval gates linked in the registry entry.

## Evidence of understanding

Trace one production prediction back to registry version, training data hash, and eval report.

## Trade-offs

No mechanism is universal. Compare model registry against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
