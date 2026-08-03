# Problem Framing

**Purpose:** Reference card for **problem framing** used across AIEBOK books and knowledge areas.

## Core explanation

Problem framing defines the unit of prediction, target label, decision, population, and time boundary before choosing algorithms. Most ML failures are mis-specified problems, not wrong models.

## Example

Predicting 'will this ticket reopen within 7 days' differs from 'summarize this ticket'—only the first is a measurable ML task.

## Evidence of understanding

Write the prediction unit, label definition, and decision rule; verify each is observable in production logs.

## Trade-offs

No mechanism is universal. Compare problem framing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
