# Data Residency

**Purpose:** Reference card for **data residency** used across AIEBOK books and knowledge areas.

## Core explanation

Data residency restricts processing and storage to approved geographic regions for legal compliance.

## Example

EU customer prompts and indexes stay in eu-west inference and storage only.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Validate data plane region tags on every storage and inference resource.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare data residency against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Audit](../../concepts/cards/audit.md)
- [Authorization](../../concepts/cards/authorization.md)
- [Identity](../../concepts/cards/identity.md)
- [Multi Tenancy](../../concepts/cards/multi-tenancy.md)

## Related chapters

- [02 Identity Data And Trust Boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
