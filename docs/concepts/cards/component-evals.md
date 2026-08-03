# Component Evals

**Purpose:** Reference card for **component evals** used across AIEBOK books and knowledge areas.

## Core explanation

Component evals test retrieval, generation, tools, and UX stages independently before end-to-end runs. They localize failures.

## Example

Retrieval recall@10 evaluated separately from answer faithfulness on same queries.

## Evidence of understanding

Build failure attribution matrix mapping end-to-end misses to component scores.

## Trade-offs

No mechanism is universal. Compare component evals against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
