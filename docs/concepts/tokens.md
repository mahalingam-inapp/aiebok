# Tokens

**Purpose:** Convert raw content into discrete units a language model can process and generate.

**Prerequisites:** Text encoding, vocabulary, probability.

## Intuition

A token is not necessarily a word. It may be a character, punctuation mark, common word, or word fragment. A tokenizer maps content to integer IDs; the model maps those IDs to vectors.

## Why this exists

Models require a finite input vocabulary. Subword methods balance character-level flexibility with word-level efficiency and allow unfamiliar words to be composed from known pieces.

## Engineering consequences

- Limits, prices, and throughput are commonly measured in tokens.
- Different tokenizers produce different lengths for code, languages, and unusual text.
- Truncation can silently remove crucial instructions or evidence.
- Output token budgets affect completeness and latency.

## Practice

Tokenize the same paragraph in three languages and a code sample. Compare token-to-character ratios and estimate context cost.

## Misconceptions

- Tokens are not always words.
- A larger context window does not ensure the model uses all content well.
- Token count is only one latency factor.

## What survives

Learned systems need a representation boundary between raw input and internal computation—even if future models use different units.
