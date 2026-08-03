# Caching

**Purpose:** Reference card for **caching** used across AIEBOK books and knowledge areas.

## Core explanation

Caching stores prompt prefixes, embeddings, or completions to cut latency and cost. Cache keys must include model version and prompt hash to avoid stale wrong answers.

## Example

Caching the system prompt KV states saves compute on every request with identical instructions.

## Evidence of understanding

Measure cache hit rate and verify cache invalidation when prompt version changes.

## Trade-offs

No mechanism is universal. Compare caching against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
