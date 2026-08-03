# Freshness

**Purpose:** Reference card for **freshness** used across AIEBOK books and knowledge areas.

## Core explanation

Freshness policies define acceptable document age, re-ingest cadence, and TTL for cached answers. Regulated domains often require sub-daily updates for policy corpora.

## Example

Benefits enrollment answers must exclude documents marked superseded after open enrollment ends.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Reject or downgrade chunks where ingest_timestamp exceeds freshness SLA for the topic.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare freshness against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Adaptive Rag](../../concepts/cards/adaptive-rag.md)
- [Authorization](../../concepts/cards/authorization.md)
- [Graph Rag](../../concepts/cards/graph-rag.md)
- [Multi Hop Retrieval](../../concepts/cards/multi-hop-retrieval.md)

## Related chapters

- [06 Advanced And Enterprise Rag](../../books/06-knowledge-and-retrieval-systems/06-advanced-and-enterprise-rag.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
