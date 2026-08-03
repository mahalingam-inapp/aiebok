# Vocabulary

**Purpose:** Reference card for **vocabulary** used across AIEBOK books and knowledge areas.

## Core explanation

Vocabulary is the set of tokens a model or index recognizes; out-of-vocabulary items become unknown or split subwords. Size trades coverage against memory and sparsity.

## Example

A 32k BPE vocabulary handles common English and code fragments but may fragment rare product SKUs.

## Evidence of understanding

Measure OOV rate on production queries and track how subword splits affect identifier retrieval.

## Trade-offs

No mechanism is universal. Compare vocabulary against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
