# Adaptive Rag

**Purpose:** Reference card for **adaptive rag** used across AIEBOK books and knowledge areas.

## Core explanation

Adaptive RAG chooses retrieval depth, query rewrite, or no retrieval based on question type and confidence. It saves cost on simple queries while going deep on hard ones.

## Example

Greetings skip retrieval; compliance questions trigger hybrid search plus rerank.

## Evidence of understanding

Compare average latency and accuracy versus always-retrieve baseline on mixed query set.

## Trade-offs

No mechanism is universal. Compare adaptive rag against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
