# Permissions

**Purpose:** Reference card for **permissions** used across AIEBOK books and knowledge areas.

## Core explanation

Permissions bind tools and data access to authenticated identities and roles. Models must not bypass authorization by guessing URLs or parameters.

## Example

delete_user tool requires admin role verified server-side, not in the prompt.

## Evidence of understanding

Attempt privileged tool calls as low-privilege identity and expect denial.

## Trade-offs

No mechanism is universal. Compare permissions against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
