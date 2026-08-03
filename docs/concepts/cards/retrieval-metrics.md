# Retrieval Metrics

**Purpose:** Reference card for **retrieval metrics** used across AIEBOK books and knowledge areas.

## Core explanation

Retrieval metrics—recall@k, MRR, nDCG—measure candidate set quality before generation sees it.

## Example

High recall@20 with poor faithfulness suggests generation issue, not retrieval.

## Evidence of understanding

Report recall@5, @10, @20 on fixed query set each index version.

## Trade-offs

No mechanism is universal. Compare retrieval metrics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
