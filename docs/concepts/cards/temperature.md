# Temperature

**Purpose:** Reference card for **temperature** used across AIEBOK books and knowledge areas.

## Core explanation

Temperature scales logits before softmax—lower sharpens the distribution (more deterministic), higher flattens it (more random). It is a primary creativity-versus-consistency knob.

## Example

Temperature 0.2 keeps support answers stable; 1.2 increases phrasing variety for marketing copy.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Plot entropy of next-token distribution versus temperature on a fixed prompt set.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare temperature against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Batching](../../concepts/cards/batching.md)
- [Kv Cache](../../concepts/cards/kv-cache.md)
- [Logits](../../concepts/cards/logits.md)
- [Sampling](../../concepts/cards/sampling.md)

## Related chapters

- [05 Inference And Sampling](../../books/04-transformers-and-foundation-models/05-inference-and-sampling.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
