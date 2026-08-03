# Structured Output

**Purpose:** Reference card for **structured output** used across AIEBOK books and knowledge areas.

## Core explanation

Structured output forces models to emit machine-parseable formats—JSON, XML, tool calls—via prompting or constrained decoding. Parsers must still validate because models can violate schema.

## Example

An invoice extractor returns JSON fields consumed directly by ERP ingestion.

## Evidence of understanding

Measure schema pass rate on 200 adversarial and normal inputs post-generation.

## Trade-offs

No mechanism is universal. Compare structured output against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
