# Unicode

**Purpose:** Reference card for **unicode** used across AIEBOK books and knowledge areas.

## Core explanation

Unicode assigns code points to characters across scripts; mishandling causes mojibake, broken tokens, and security bypasses via homoglyphs.

## Example

Normalizing NFC versus NFD changes string equality for accented characters in user names.

## Evidence of understanding

Run ingestion on ten multilingual samples and verify round-trip display matches source glyphs.

## Trade-offs

No mechanism is universal. Compare unicode against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
