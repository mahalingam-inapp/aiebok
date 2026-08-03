# Rnns

**Purpose:** Reference card for **rnns** used across AIEBOK books and knowledge areas.

## Core explanation

Recurrent neural networks process sequences step by step, maintaining hidden state across time. Serial computation limits parallel training and long-range credit assignment.

## Example

Character-level RNN language models learn spelling but struggle with paragraph-level coherence.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure training steps/sec versus transformer on the same sequence length.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare rnns against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bottlenecks](../../concepts/cards/bottlenecks.md)
- [Lstms](../../concepts/cards/lstms.md)
- [N Grams](../../concepts/cards/n-grams.md)
- [Seq2seq](../../concepts/cards/seq2seq.md)

## Related chapters

- [01 Sequence Models Before Transformers](../../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
