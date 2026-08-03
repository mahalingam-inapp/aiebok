# N Grams

**Purpose:** Reference card for **n grams** used across AIEBOK books and knowledge areas.

## Core explanation

N-gram models predict tokens from local history of n−1 prior tokens—simple, fast, and limited to short context. They remain baselines for compression and sanity checks.

## Example

A trigram model captures 'New York' but not dependencies spanning whole paragraphs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare perplexity of n-gram versus small neural LM on the same held-out corpus.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare n grams against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bottlenecks](../../concepts/cards/bottlenecks.md)
- [Lstms](../../concepts/cards/lstms.md)
- [Rnns](../../concepts/cards/rnns.md)
- [Seq2seq](../../concepts/cards/seq2seq.md)

## Related chapters

- [01 Sequence Models Before Transformers](../../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
