# Faithfulness

**Purpose:** Reference card for **faithfulness** used across AIEBOK books and knowledge areas.

## Core explanation

Faithfulness checks that generated statements are entailed by retrieved evidence, not hallucinated additions. It is separate from fluency or user satisfaction.

## Example

Correct tone but wrong deductible amount is unfaithful despite readable prose.

## Evidence of understanding

Use NLI or human rubric on 100 answers; require faithfulness ≥ threshold for release.

## Trade-offs

No mechanism is universal. Compare faithfulness against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
