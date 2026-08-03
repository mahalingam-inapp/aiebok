# Pretraining Objectives

**Purpose:** Reference card for **pretraining objectives** used across AIEBOK books and knowledge areas.

## Core explanation

Pretraining objectives define self-supervised targets—causal LM, masked LM, denoising—that shape what models learn from raw text. Objective choice affects bidirectionality and use cases.

## Example

Causal LM suits generation; masked LM suits understanding tasks before fine-tuning.

## Evidence of understanding

Compare downstream task scores after pretraining two small models with different objectives.

## Trade-offs

No mechanism is universal. Compare pretraining objectives against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
