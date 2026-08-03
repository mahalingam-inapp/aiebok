# Bounded Rationality

**Purpose:** Reference card for **bounded rationality** used across AIEBOK books and knowledge areas.

## Core explanation

Bounded rationality acknowledges limited compute, time, memory, and information—systems must satisfice within budgets. Production AI rarely has the luxury of exhaustive search or perfect retrieval.

## Example

An on-call copilot stops after three retrieval attempts within a 5-second latency SLO instead of searching until theoretical certainty.

## Evidence of understanding

Document the stopping budget and demonstrate a case where more compute would help but violates the SLO.

## Trade-offs

No mechanism is universal. Compare bounded rationality against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
