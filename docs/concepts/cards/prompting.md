# Prompting

**Purpose:** Reference card for **prompting** used across AIEBOK books and knowledge areas.

## Core explanation

Prompting steers model behavior at inference via instructions and examples without weight updates. It is the fastest iteration path when context fits.

## Example

Adding 'cite sources' instruction improves citation rate without retraining.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare prompt variants on behavioral eval with fixed model weights.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare prompting against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Behavior Versus Knowledge](../../concepts/cards/behavior-versus-knowledge.md)
- [Fine Tuning](../../concepts/cards/fine-tuning.md)
- [Model Selection](../../concepts/cards/model-selection.md)
- [Rag](../../concepts/cards/rag.md)

## Related chapters

- [01 Choosing Adaptation](../../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
