# Subwords

**Purpose:** Reference card for **subwords** used across AIEBOK books and knowledge areas.

## Core explanation

Subword units split rare words into frequent pieces so models handle morphology and typos without huge vocabularies. Splitting affects cost, semantics, and cross-lingual behavior.

## Example

'unhappiness' may become ['un', 'happiness'] preserving morphemes better than character splits.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare token counts for 100 product names under word versus BPE tokenizers.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare subwords against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bpe](../../concepts/cards/bpe.md)
- [Sentencepiece](../../concepts/cards/sentencepiece.md)
- [Token Budgets](../../concepts/cards/token-budgets.md)
- [Vocabulary](../../concepts/cards/vocabulary.md)

## Related chapters

- [03 Tokenization](../../books/03-language-and-representation/03-tokenization.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
