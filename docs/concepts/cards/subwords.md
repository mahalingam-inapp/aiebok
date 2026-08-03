# Subwords

**Purpose:** Reference card for **subwords** used across AIEBOK books and knowledge areas.

## Core explanation

Subword units split rare words into frequent pieces so models handle morphology and typos without huge vocabularies. Splitting affects cost, semantics, and cross-lingual behavior.

## Example

'unhappiness' may become ['un', 'happiness'] preserving morphemes better than character splits.

## Evidence of understanding

Compare token counts for 100 product names under word versus BPE tokenizers.

## Trade-offs

No mechanism is universal. Compare subwords against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
