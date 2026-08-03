# Unicode

**Purpose:** Reference card for **unicode** used across AIEBOK books and knowledge areas.

## Core explanation

Unicode assigns code points to characters across scripts; mishandling causes mojibake, broken tokens, and security bypasses via homoglyphs.

## Example

Normalizing NFC versus NFD changes string equality for accented characters in user names.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run ingestion on ten multilingual samples and verify round-trip display matches source glyphs.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare unicode against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Corpora](../../concepts/cards/corpora.md)
- [Data Provenance](../../concepts/cards/data-provenance.md)
- [Normalization](../../concepts/cards/normalization.md)
- [Segmentation](../../concepts/cards/segmentation.md)

## Related chapters

- [02 Corpora And Text Pipelines](../../books/03-language-and-representation/02-corpora-and-text-pipelines.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
