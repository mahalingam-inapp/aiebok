# Sentencepiece

**Purpose:** Reference card for **sentencepiece** used across AIEBOK books and knowledge areas.

## Core explanation

SentencePiece trains subword models directly on raw text without pre-tokenization, simplifying multilingual pipelines. It supports unigram and BPE objectives with shared vocabularies.

## Example

One SentencePiece model covers Japanese and English in a single vocabulary for multilingual search.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare segmentation consistency across languages on parallel sentences.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare sentencepiece against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bpe](../../concepts/cards/bpe.md)
- [Subwords](../../concepts/cards/subwords.md)
- [Token Budgets](../../concepts/cards/token-budgets.md)
- [Vocabulary](../../concepts/cards/vocabulary.md)

## Related chapters

- [03 Tokenization](../../books/03-language-and-representation/03-tokenization.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
