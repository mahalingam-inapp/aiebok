# Dense Retrieval

**Purpose:** Reference card for **dense retrieval** used across AIEBOK books and knowledge areas.

## Core explanation

Dense retrieval embeds queries and documents into the same vector space and returns nearest neighbors by similarity.

## Example

A query about 'application unavailable' retrieves 'service is down' without lexical overlap.

## Evidence of understanding

Build a 30-query eval with paraphrases and hard negatives; report recall@5 and MRR.

## Trade-offs

No mechanism is universal. Compare dense retrieval against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
