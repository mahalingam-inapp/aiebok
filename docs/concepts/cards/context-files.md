# Context Files

**Purpose:** Reference card for **context files** used across AIEBOK books and knowledge areas.

## Core explanation

Context files—.cursorrules, architecture docs—supply persistent project knowledge to coding agents. Stale context misleads worse than no context.

## Example

Architecture.md describes service boundaries so agent edits correct package.

## Evidence of understanding

Update context file when ADR changes and note version in agent traces.

## Trade-offs

No mechanism is universal. Compare context files against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
