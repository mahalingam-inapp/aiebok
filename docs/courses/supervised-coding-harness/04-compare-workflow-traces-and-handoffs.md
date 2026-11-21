# Compare workflow traces and handoffs

[Supervised Coding-Agent Harnesses](index.md) · Approve and audit a change · Lecture 4 of 4 · 45–60 min · Project practicum

## What you will learn

Use a fixed suite to compare proposals and design a human handoff with useful evidence.

## How it works

Count validated proposals, test passes, approval waits, and applications separately. A trace should be detailed enough to reproduce the decision and compact enough for a reviewer to scan. In a framework, carry the proposal ID and revision through each transition and keep the executor boundary explicit.

## Worked example

Two candidates may look identical in a summary. A trace showing a failed whitespace case and a review approval against a specific revision distinguishes them.

## Try it yourself

Create a small report from the trace. Identify what the reviewer sees at each blocked stage.

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The report should name the failed check or approval state and the next responsible person. Keep the evidence tied to the exact candidate.

## Continue

[← Previous lecture](03-approval-revisions-and-replay.md) · [Course outline](index.md) · [Course project →](index.md#course-project)
