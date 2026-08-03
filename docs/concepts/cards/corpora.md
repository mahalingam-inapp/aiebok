# Corpora

**Purpose:** Reference card for **corpora** used across AIEBOK books and knowledge areas.

## Core explanation

Corpora are curated text collections whose composition, licensing, and bias shape every downstream model. Provenance and consent determine legal and ethical use.

## Example

Training on public forums without filtering includes toxic threads that surface in generations.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Document source, license, date range, and language distribution in a corpus card.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare corpora against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Data Provenance](../../concepts/cards/data-provenance.md)
- [Normalization](../../concepts/cards/normalization.md)
- [Segmentation](../../concepts/cards/segmentation.md)
- [Unicode](../../concepts/cards/unicode.md)

## Related chapters

- [02 Corpora And Text Pipelines](../../books/03-language-and-representation/02-corpora-and-text-pipelines.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
