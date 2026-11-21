# Textbook Content Audit

Reviewed on 21 November 2026. The audit covers the **142 lectures in the 29-course curriculum**. It distinguishes the 78 technical book chapters from the 64 lectures used for no-code courses and applied practicums.

## What the audit found

| Lecture group | Before | After |
|---|---:|---:|
| Technical book chapters | Median 1,739 words | Median 1,605 words |
| No-code and applied lectures | Median 232 words | Median 364 words |
| Explanation section in no-code and applied lectures | Median 38 words | Median 192 words |

Counts use rendered lecture text, including headings, captions, and exercises. They exclude code blocks, launch buttons, the lecture progress row, and the new course navigation. Medians are rounded to whole words. The audit also examined the sequence of explanation, practice, evidence, and feedback. Word count identifies thin material and does not certify that a lesson teaches its objective.

The short lectures often put an objective, a definition, a scenario, and an exercise back to back. A learner could see what to do without learning how to reason from the facts to the decision. The technical chapters had substantial explanations and code. Repeated remarks about prerequisites, diagrams, and book-level samples made the reading sequence feel procedural. The technical revision trims that boilerplate and keeps the concepts, runnable examples, and knowledge checks.

## Changes across the curriculum

Each of the 64 shorter lectures now develops its own method or mechanism. A reading should define the key distinction, use it on realistic inputs, and explain what changes at a boundary or why a plausible answer fails. Some worked examples use arithmetic, such as coverage and selective risk. Others follow a sequence, such as restoring a workflow after approval or verifying a citation against the particular revision the user could see.

| Test the approach with | What to look for |
|---|---|
| [Why confident answers can be wrong](../courses/ai-literacy/02-why-confident-answers-can-be-wrong.md) | The chapter explains why plausible wording is weak evidence and shows the practical cost of confusing “next update” with “reopening.” |
| [Measure selective risk and cost](../courses/model-selection-and-adaptation/03-measure-selective-risk-and-cost.md) | A threshold comparison makes accuracy, coverage, and review workload separate observations. |
| [Citation verification and freshness checks](../courses/retrieval-system-engineering/04-citation-verification-and-freshness-checks.md) | The chapter distinguishes a valid source identifier from evidence that actually supports the answer. |
| [Rollback verification and incident review](../courses/ai-reliability-release/04-rollback-verification-and-incident-review.md) | The chapter follows a rollback decision through the affected request and the remaining manual work. |

The [real-world casebook](../casebook/index.md) provides sourced examples. Fictional scenarios inside the lectures let learners reuse the reasoning under different conditions.

## Check a course as a learner

Start on a learning path, open a course, and use **Jump to a lecture** or the previous and next links. The course overview offers to resume the last opened lecture when browser storage is available. When a learner enters through a path, links lead back to it and from the course overview to the next course. The last lecture leads to the course project. The slides keep the presenter view concise, with the longer explanation on the lecture page.

A useful follow-up audit is to observe someone learning a new topic without help. Check whether they can explain the mechanism and complete the exercise using the reading, and note which assumptions still require outside context. The present audit checks coverage and structure across the catalog. It does not measure learner outcomes.
