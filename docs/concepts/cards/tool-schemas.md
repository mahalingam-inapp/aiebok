# Tool Schemas

**Purpose:** Reference card for **tool schemas** used across AIEBOK books and knowledge areas.

## Core explanation

Tool schemas define parameter names, types, required fields, and descriptions models use to construct calls. Ambiguous schemas cause systematic argument errors.

## Example

date_iso string format in schema prevents models passing 'next Tuesday' unparseably.

## Evidence of understanding

Measure argument validation failure rate per tool after schema revision.

## Trade-offs

No mechanism is universal. Compare tool schemas against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
