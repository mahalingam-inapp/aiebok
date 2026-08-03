# Gold Datasets

**Purpose:** Reference card for **gold datasets** used across AIEBOK books and knowledge areas.

## Core explanation

Gold datasets hold authoritative labels or reference outputs for evaluation. They require versioning, access control, and refresh cadence.

## Example

200 lawyer-reviewed contract clauses with gold entity spans versioned quarterly.

## Evidence of understanding

Hash dataset version in every eval report; reject runs on unversioned snapshots.

## Trade-offs

No mechanism is universal. Compare gold datasets against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
