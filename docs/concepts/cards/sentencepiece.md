# Sentencepiece

**Purpose:** Reference card for **sentencepiece** used across AIEBOK books and knowledge areas.

## Core explanation

SentencePiece trains subword models directly on raw text without pre-tokenization, simplifying multilingual pipelines. It supports unigram and BPE objectives with shared vocabularies.

## Example

One SentencePiece model covers Japanese and English in a single vocabulary for multilingual search.

## Evidence of understanding

Compare segmentation consistency across languages on parallel sentences.

## Trade-offs

No mechanism is universal. Compare sentencepiece against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
