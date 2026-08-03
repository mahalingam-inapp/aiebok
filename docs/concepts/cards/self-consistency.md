# Self Consistency

**Purpose:** Reference card for **self consistency** used across AIEBOK books and knowledge areas.

## Core explanation

Self-consistency samples multiple reasoning paths and aggregates answers by majority vote. It improves reliability when individual samples are noisy.

## Example

Five chain-of-thought samples that agree on '42' outweigh one outlier '41'.

## Evidence of understanding

Compare accuracy of majority vote versus single sample at equal total token budget.

## Trade-offs

No mechanism is universal. Compare self consistency against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
