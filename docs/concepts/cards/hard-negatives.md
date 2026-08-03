# Hard Negatives

**Purpose:** Reference card for **hard negatives** used across AIEBOK books and knowledge areas.

## Core explanation

Hard negatives are plausible but incorrect passages that confuse retrievers—essential for training and evaluation realism. Easy negatives inflate metrics.

## Example

A chunk about vacation policy is a hard negative for a sick-leave query sharing HR vocabulary.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Include at least three hard negatives per query in eval sets and report recall drop versus easy-only sets.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare hard negatives against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Embedding Evaluation](../../concepts/cards/embedding-evaluation.md)
- [Multilingual Models](../../concepts/cards/multilingual-models.md)
- [Re Indexing](../../concepts/cards/re-indexing.md)
- [Vector Governance](../../concepts/cards/vector-governance.md)

## Related chapters

- [06 Embedding Systems In Production](../../books/03-language-and-representation/06-embedding-systems-in-production.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
