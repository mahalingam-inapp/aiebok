# Tool Abuse

**Purpose:** Reference card for **tool abuse** used across AIEBOK books and knowledge areas.

## Core explanation

Tool abuse exploits excessive permissions—delete, send email, SQL write—through manipulated agent behavior.

## Example

Agent tricked into mass email via send_campaign tool with broad scope.

## Evidence of understanding

Apply least privilege per tool; fuzz adversarial prompts expecting zero abusive executions.

## Trade-offs

No mechanism is universal. Compare tool abuse against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
