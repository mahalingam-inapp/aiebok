# Code Review

**Purpose:** Reference card for **code review** used across AIEBOK books and knowledge areas.

## Core explanation

Code review evaluates correctness, security, and maintainability of changes—including agent-written code. It remains accountability gate before merge.

## Example

Reviewer checks agent did not skip auth on new endpoint despite passing happy-path tests.

## Evidence of understanding

Measure post-merge incident rate for agent-authored versus human-authored merges.

## Trade-offs

No mechanism is universal. Compare code review against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
