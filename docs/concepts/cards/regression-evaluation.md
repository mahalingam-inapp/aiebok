# Regression Evaluation

**Purpose:** Reference card for **regression evaluation** used across AIEBOK books and knowledge areas.

## Core explanation

Regression evaluation re-runs fixed test suites after prompt or context changes to catch quality drops. It complements aggregate monitoring with known hard cases.

## Example

A 30-case eval set includes injection attempts and acronym queries that must never regress.

## When to use

Use before every release, model swap, prompt change, or retrieval index migration.

## When not to use

Skip aggregate-only metrics when slices or safety cases can hide regressions.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Report worst-slice performance, not aggregate alone.

## Evidence of understanding

Block release if any P0 case fails or overall score drops more than two points.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare regression evaluation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [A B Tests](../../concepts/cards/a-b-tests.md)
- [Caching](../../concepts/cards/caching.md)
- [Context Traces](../../concepts/cards/context-traces.md)
- [Prompt Versioning](../../concepts/cards/prompt-versioning.md)

## Related chapters

- [06 Prompt And Context Operations](../../books/05-prompt-and-context-engineering/06-prompt-and-context-operations.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
