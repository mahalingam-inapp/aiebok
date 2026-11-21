# Rollback verification and incident review

[AI Reliability and Release Engineering](index.md) · Release and recover · Lecture 4 of 4 · 45–60 min · Project practicum

## What you will learn

Restore stable routing, run a smoke check, and assemble a factual incident timeline.

## How it works

After a rollback, verify that new requests reach the expected version and that the service indicators recover. Record detection, decision, mitigation, and validation times. Write follow-up actions with an owner and verification criterion.

## Worked example

The on-call engineer pauses the candidate, confirms stable responses from the affected cohort, and records a follow-up to test dependency failure before the next release.

## Try it yourself

Run the scripted incident. Extend the report with one owner, one preventable failure, and a due condition.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The incident review distinguishes measured cause and impact from hypotheses and includes evidence that rollback restored service.

## Continue

[← Previous lecture](03-canary-cohorts-and-staged-gates.md) · [Course outline](index.md) · [Course project →](index.md#course-project)
