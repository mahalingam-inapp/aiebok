# Normalization

**Purpose:** Reference card for **normalization** used across AIEBOK books and knowledge areas.

## Core explanation

Text normalization lowercases, strips diacritics, standardizes whitespace, and canonicalizes equivalents before indexing or tokenization. Over-normalization destroys discriminative identifiers.

## Example

Collapsing hyphens in SKUs merges distinct product codes; preserving case matters for camelCase APIs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare retrieval recall with and without aggressive normalization on identifier-heavy queries.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare normalization against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Activations](../../concepts/cards/activations.md)
- [Backpropagation](../../concepts/cards/backpropagation.md)
- [Corpora](../../concepts/cards/corpora.md)
- [Data Provenance](../../concepts/cards/data-provenance.md)

## Related chapters

- [04 Neural Networks](../../books/02-machine-learning-systems/04-neural-networks.md)
- [02 Corpora And Text Pipelines](../../books/03-language-and-representation/02-corpora-and-text-pipelines.md)
- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
