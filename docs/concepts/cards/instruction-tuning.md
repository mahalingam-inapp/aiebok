# Instruction Tuning

**Purpose:** Reference card for **instruction tuning** used across AIEBOK books and knowledge areas.

## Core explanation

Instruction tuning fine-tunes models on prompt–response pairs covering diverse tasks, improving zero-shot instruction following. It shapes helpfulness and format compliance.

## Example

After instruction tuning, models follow 'respond in JSON' without task-specific fine-tuning.

## Evidence of understanding

Compare instruction-following score on 50 held-out prompts before and after tuning.

## Trade-offs

No mechanism is universal. Compare instruction tuning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
