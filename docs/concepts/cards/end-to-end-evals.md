# End To End Evals

**Purpose:** Reference card for **end to end evals** used across AIEBOK books and knowledge areas.

## Core explanation

End-to-end evals measure full pipeline outcomes on realistic inputs including latency and cost.

## Example

User question to cited answer passes only if retrieval, generation, and citation all succeed.

## Evidence of understanding

Run weekly end-to-end suite with production config hash in report.

## Trade-offs

No mechanism is universal. Compare end to end evals against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
