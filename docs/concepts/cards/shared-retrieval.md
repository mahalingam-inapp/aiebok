# Shared Retrieval

**Purpose:** Reference card for **shared retrieval** used across AIEBOK books and knowledge areas.

## Core explanation

Shared retrieval services provide governed indexes, embedding pipelines, and search APIs reused across products.

## Example

Enterprise policy index serves HR bot and IT bot with tenant filters from one platform team.

## When to use

Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.

## When not to use

Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Measure index freshness SLA and per-tenant isolation in platform tests.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare shared retrieval against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Gateways](../../concepts/cards/ai-gateways.md)
- [Model Catalog](../../concepts/cards/model-catalog.md)
- [Platform Engineering](../../concepts/cards/platform-engineering.md)
- [Tool Registry](../../concepts/cards/tool-registry.md)

## Related chapters

- [01 Enterprise Ai Building Blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
