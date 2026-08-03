# Dependencies

**Purpose:** Reference card for **dependencies** used across AIEBOK books and knowledge areas.

## Core explanation

Dependencies constrain execution order—step B requires output or state from step A. Violating them causes flaky failures or data corruption.

## Example

Sending customer emails before database migration commits references wrong product IDs.

## Evidence of understanding

Topological sort the plan and simulate; flag any out-of-order execution.

## Trade-offs

No mechanism is universal. Compare dependencies against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
