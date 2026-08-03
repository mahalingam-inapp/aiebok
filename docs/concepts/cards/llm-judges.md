# Llm Judges

**Purpose:** Reference card for **llm judges** used across AIEBOK books and knowledge areas.

## Core explanation

LLM judges automate scoring using rubrics but must be calibrated against humans to avoid systematic bias.

## Example

GPT-4 judge scores faithfulness correlated 0.85 with human labels after calibration.

## Evidence of understanding

Sample 10% human audit of LLM judge scores each sprint; recalibrate if drift >5 points.

## Trade-offs

No mechanism is universal. Compare llm judges against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
