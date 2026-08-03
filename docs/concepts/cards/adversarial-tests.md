# Adversarial Tests

**Purpose:** Reference card for **adversarial tests** used across AIEBOK books and knowledge areas.

## Core explanation

Adversarial tests probe injection, jailbreaks, edge inputs, and abuse scenarios. They belong in release gates for user-facing AI.

## Example

Prompt injection via ticket body attempting credential exfil must fail closed.

## Evidence of understanding

Maintain adversarial suite; require 100% pass on P0 cases before deploy.

## Trade-offs

No mechanism is universal. Compare adversarial tests against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
