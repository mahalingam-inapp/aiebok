# Model Catalog

**Purpose:** Reference card for **model catalog** used across AIEBOK books and knowledge areas.

## Core explanation

Model catalog lists approved models with risk tier, eval status, and allowed use cases for developers.

## Example

Catalog shows gpt-4o approved tier-2; llama-local approved tier-1 air-gapped only.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Reject deployment requests for models not in catalog with approved version.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare model catalog against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Gateways](../../concepts/cards/ai-gateways.md)
- [Platform Engineering](../../concepts/cards/platform-engineering.md)
- [Shared Retrieval](../../concepts/cards/shared-retrieval.md)
- [Tool Registry](../../concepts/cards/tool-registry.md)

## Related chapters

- [01 Enterprise Ai Building Blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
