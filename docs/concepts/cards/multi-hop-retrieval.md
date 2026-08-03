# Multi Hop Retrieval

**Purpose:** Reference card for **multi hop retrieval** used across AIEBOK books and knowledge areas.

## Core explanation

Multi-hop retrieval gathers evidence across sequential lookups when no single passage contains the answer. Orchestration must avoid error propagation from early hops.

## Example

Finding budget owner requires hop one: project ID → department; hop two: department → approver.

## Evidence of understanding

Measure end-to-end accuracy and per-hop recall on labeled multi-hop questions.

## Trade-offs

No mechanism is universal. Compare multi hop retrieval against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
