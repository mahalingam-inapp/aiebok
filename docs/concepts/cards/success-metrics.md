# Success Metrics

**Purpose:** Reference card for **success metrics** used across AIEBOK books and knowledge areas.

## Core explanation

Success metrics tie releases to user-valued outcomes—task success, time saved, revenue—not model perplexity alone.

## Example

Deflect 20% of L1 tickets without increasing reopen rate defines success for support bot.

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

Pre-register primary and guardrail metrics before launch with target deltas.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare success metrics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Baseline Workflow](../../concepts/cards/baseline-workflow.md)
- [Feasibility](../../concepts/cards/feasibility.md)
- [Jobs To Be Done](../../concepts/cards/jobs-to-be-done.md)
- [User Research](../../concepts/cards/user-research.md)

## Related chapters

- [01 Discovering The Right Problem](../../books/09-ai-software-and-product-engineering/01-discovering-the-right-problem.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
