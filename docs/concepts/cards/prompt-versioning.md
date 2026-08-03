# Prompt Versioning

**Purpose:** Reference card for **prompt versioning** used across AIEBOK books and knowledge areas.

## Core explanation

Prompt versioning tracks template changes with IDs, authors, and diffs like code. Unversioned prompt edits cause silent regressions impossible to roll back.

## Example

Prompt v2.3.1 changes abstention wording—eval must compare v2.3.0 versus v2.3.1 before deploy.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Store prompt hash on every trace and correlate with quality metrics by version.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare prompt versioning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [A B Tests](../../concepts/cards/a-b-tests.md)
- [Caching](../../concepts/cards/caching.md)
- [Context Traces](../../concepts/cards/context-traces.md)
- [Regression Evaluation](../../concepts/cards/regression-evaluation.md)

## Related chapters

- [06 Prompt And Context Operations](../../books/05-prompt-and-context-engineering/06-prompt-and-context-operations.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
