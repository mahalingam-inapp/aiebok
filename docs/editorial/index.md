# Editorial Handbook

AIEBOK is maintained like an engineering standard: scoped, reviewed, versioned, testable, and dated.

## Publication workflow

Idea → content specification → draft → technical review → editorial review → code/link validation → preview → merge → scheduled review.

## Review roles

- **Author:** accuracy, examples, metadata, and source quality
- **Technical reviewer:** theory, code, claims, trade-offs, and security
- **Editor:** clarity, hierarchy, accessibility, consistency, and mobile reading
- **Maintainer:** scope, navigation, duplication, release, and review scheduling

## Definition of done

- The page has a clear audience and learning outcome.
- Claims are scoped; changing facts are dated and sourced.
- Prerequisites and related pages are linked.
- The enduring principle is separated from current implementations.
- Code was run and expected results are explained.
- Trade-offs, failure modes, evaluation, and security are present where relevant.
- Headings are hierarchical; paragraphs are mobile-readable; images have alt text.
- `python scripts/validate_content.py` and `mkdocs build --strict` pass.
