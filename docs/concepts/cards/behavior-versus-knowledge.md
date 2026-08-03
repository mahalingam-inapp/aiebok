# Behavior Versus Knowledge

**Purpose:** Reference card for **behavior versus knowledge** used across AIEBOK books and knowledge areas.

## Core explanation

Behavior changes how the model acts—tone, format, policy—while knowledge is factual content. RAG adds knowledge; fine-tuning often shifts behavior.

## Example

Model knows refunds exist but needs SFT to always ask order ID first—that is behavior.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Classify ten requirements as behavior or knowledge and map to prompt, RAG, or fine-tune.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare behavior versus knowledge against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Fine Tuning](../../concepts/cards/fine-tuning.md)
- [Model Selection](../../concepts/cards/model-selection.md)
- [Prompting](../../concepts/cards/prompting.md)
- [Rag](../../concepts/cards/rag.md)

## Related chapters

- [01 Choosing Adaptation](../../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
