# Knowledge Freshness

**Purpose:** Reference card for **knowledge freshness** used across AIEBOK books and knowledge areas.

## Core explanation

Knowledge freshness measures how current stored facts are relative to the real world. Stale indexes cause confident wrong answers until re-ingestion catches up.

## Example

A travel policy updated yesterday is invisible if the index last synced last month.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Track max document age in retrieved sets and alert when any source exceeds SLA staleness.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare knowledge freshness against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Fine Tuning](../../concepts/cards/fine-tuning.md)
- [Grounding](../../concepts/cards/grounding.md)
- [Retrieval](../../concepts/cards/retrieval.md)
- [Structured Data](../../concepts/cards/structured-data.md)

## Related chapters

- [01 Knowledge Outside The Model](../../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
