# Context Windows

**Purpose:** Reference card for **context windows** used across AIEBOK books and knowledge areas.

## Core explanation

Context windows cap tokens the model attends to in one forward pass—prompt, evidence, tools, and output compete for this budget.

## Example

A 128k window still requires prioritization when ten long documents are retrieved.

## Evidence of understanding

Measure task quality versus tokens used and find the knee of the curve for your workload.

## Trade-offs

No mechanism is universal. Compare context windows against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
