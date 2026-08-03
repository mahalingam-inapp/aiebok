# Prompt Versioning

**Purpose:** Reference card for **prompt versioning** used across AIEBOK books and knowledge areas.

## Core explanation

Prompt versioning tracks template changes with IDs, authors, and diffs like code. Unversioned prompt edits cause silent regressions impossible to roll back.

## Example

Prompt v2.3.1 changes abstention wording—eval must compare v2.3.0 versus v2.3.1 before deploy.

## Evidence of understanding

Store prompt hash on every trace and correlate with quality metrics by version.

## Trade-offs

No mechanism is universal. Compare prompt versioning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
