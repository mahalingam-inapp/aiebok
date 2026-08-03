# Vocabulary

**Purpose:** Reference card for **vocabulary** used across AIEBOK books and knowledge areas.

## Core explanation

Vocabulary is the set of tokens a model or index recognizes; out-of-vocabulary items become unknown or split subwords. Size trades coverage against memory and sparsity.

## Example

A 32k BPE vocabulary handles common English and code fragments but may fragment rare product SKUs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure OOV rate on production queries and track how subword splits affect identifier retrieval.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare vocabulary against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bpe](../../concepts/cards/bpe.md)
- [Sentencepiece](../../concepts/cards/sentencepiece.md)
- [Subwords](../../concepts/cards/subwords.md)
- [Token Budgets](../../concepts/cards/token-budgets.md)

## Related chapters

- [03 Tokenization](../../books/03-language-and-representation/03-tokenization.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
