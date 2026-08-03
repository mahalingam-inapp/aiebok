# Model Routing

**Purpose:** Reference card for **model routing** used across AIEBOK books and knowledge areas.

## Core explanation

Model routing directs requests to appropriate models by task, risk, cost, or latency policy.

## Example

Regex on ticket category routes billing to fine-tuned small model, general to large.

## Evidence of understanding

Log route decisions; compare blended cost and quality versus single-model baseline.

## Trade-offs

No mechanism is universal. Compare model routing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
