# Bottlenecks

**Purpose:** Reference card for **bottlenecks** used across AIEBOK books and knowledge areas.

## Core explanation

Information bottlenecks force compressive representations—fixed-size context vectors or limited bandwidth channels. They create trade-offs between memory and expressiveness.

## Example

Early seq2seq used a single context vector for entire sentences, losing detail on long inputs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare output quality on 50-token versus 500-token inputs through a fixed bottleneck.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare bottlenecks against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Lstms](../../concepts/cards/lstms.md)
- [N Grams](../../concepts/cards/n-grams.md)
- [Rnns](../../concepts/cards/rnns.md)
- [Seq2seq](../../concepts/cards/seq2seq.md)

## Related chapters

- [01 Sequence Models Before Transformers](../../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
