# Bpe

**Purpose:** Reference card for **bpe** used across AIEBOK books and knowledge areas.

## Core explanation

Byte-pair encoding iteratively merges frequent symbol pairs to build a subword vocabulary from corpus statistics. It balances compression and interpretability for LLM tokenizers.

## Example

Training BPE on code-heavy corpora merges operators like '=>' into single tokens, saving context budget.

## Evidence of understanding

Train a toy BPE on 1MB text and report compression ratio versus character count.

## Trade-offs

No mechanism is universal. Compare bpe against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
