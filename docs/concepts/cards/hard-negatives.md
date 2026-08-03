# Hard Negatives

**Purpose:** Reference card for **hard negatives** used across AIEBOK books and knowledge areas.

## Core explanation

Hard negatives are plausible but incorrect passages that confuse retrievers—essential for training and evaluation realism. Easy negatives inflate metrics.

## Example

A chunk about vacation policy is a hard negative for a sick-leave query sharing HR vocabulary.

## Evidence of understanding

Include at least three hard negatives per query in eval sets and report recall drop versus easy-only sets.

## Trade-offs

No mechanism is universal. Compare hard negatives against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
