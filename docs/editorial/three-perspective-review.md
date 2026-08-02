# Three-Perspective Publication Review

This review is maintained as a release artifact. It distinguishes topic coverage from a usable educational publication.

## Book-editor review

### Findings

- The first complete draft had a strong macro-structure but repeated the same explanatory scaffold too visibly.
- Several worked scenarios were book-level and did not clearly state the chapter-specific problem.
- Generated design questions were grammatically awkward.
- Code appeared without enough relevance and expected-observation guidance.
- Book introductions needed clearer entry requirements, pacing, and assessment expectations.

### Changes made

- Replaced repetitive concept paragraphs with a compact relationship table.
- Separated the recurring book scenario from the unique chapter focus.
- Rewrote the central design question as an evidence question.
- Added time budgets, expected observations, sample-to-chapter relevance, and shorter scan paths.
- Expanded every book introduction with prerequisites, a three-week schedule, assessment weighting, and anchor readings.

### Remaining editorial policy

New content must add a new explanation, example, or decision—not merely another heading. Repeated structures are allowed only when they help navigation or assessment.

## Faculty audit

### Findings

- Learning objectives existed, but prerequisite scaffolding and constructive alignment were weak.
- Mastery questions lacked answer guidance and scoring criteria.
- Projects were specified without assessment weights.
- Research and evidence routes were not attached to the books.
- “Complete coverage” was not enforced as a testable publication property.

### Changes made

- Added prerequisites to all chapters and book entry pages.
- Added formative knowledge checks with answer guidance.
- Added a four-level self-assessment rubric to every chapter.
- Added book-level project assessment weights and anchor readings.
- Added a coverage audit that fails when any chapter lacks motivation, objectives, visual explanation, core content, worked example, runnable code, practice, architecture, failure analysis, evolution, mastery, or sufficient depth.

### Faculty interpretation

The books now support guided self-study and course adaptation. An instructor can replace self-assessment with graded rubrics, discussion facilitation, and institution-specific policies without rewriting the conceptual spine.

## Student-experience audit

### Findings

- A student could see what to study but not always how long each mode should take.
- Code samples required running before the expected learning signal was clear.
- It was difficult to judge whether an answer was “good enough.”
- The path from a chapter to remediation or further study was implicit.

### Changes made

- Split chapter time into reading, worked example, practice, and review.
- Added “before you begin” guidance that supports just-in-time remediation.
- Added collapsible expected observations before students modify code.
- Added answer guidance and self-assessment evidence at four levels.
- Added a question index, glossary, code-sample library, and explicit continuation links.

## Release gate

A publication release passes only when:

1. All Markdown and internal links validate.
2. All seventy-eight chapters pass the twelve-dimension coverage audit.
3. Every runnable sample and starter lab exits successfully.
4. MkDocs builds in strict mode with every chapter in navigation.
5. The generated search index contains the book chapters and reference pages.
