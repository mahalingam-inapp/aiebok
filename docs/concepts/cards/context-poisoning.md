# Context Poisoning

**Purpose:** Reference card for **context poisoning** used across AIEBOK books and knowledge areas.

## Core explanation

Context poisoning inserts false or misleading evidence into retrieval or memory stores to manipulate outputs. Integrity controls on indexes and ingestion are defenses.

## Example

An attacker uploads a fake policy PDF to skew answers about refund eligibility.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Monitor ingest sources, sign documents, and detect anomalous embedding clusters post-ingest.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare context poisoning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Authorization](../../concepts/cards/authorization.md)
- [Instruction Conflict](../../concepts/cards/instruction-conflict.md)
- [Prompt Injection](../../concepts/cards/prompt-injection.md)
- [Provenance](../../concepts/cards/provenance.md)

## Related chapters

- [05 Context Failure And Security](../../books/05-prompt-and-context-engineering/05-context-failure-and-security.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
