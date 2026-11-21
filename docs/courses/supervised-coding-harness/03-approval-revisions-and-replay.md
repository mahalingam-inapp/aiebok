# Approval, revisions and replay

[Supervised Coding-Agent Harnesses](index.md) · Approve and audit a change · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Bind an approval to the reviewed proposal and current revision.

## How it works

Approval is a decision about a specific candidate and the state against which it was tested. Compare the reviewed revision with the current revision before applying the change. Store a stable request ID and outcome so retries can return the previous result without repeating the action.

## Worked example

A reviewer approves the whitespace change at revision 1. Another edit lands before approval is applied. The old approval now needs a fresh review.

## Try it yourself

Try applying a good proposal before approval. Replay after applying it and then try the old review against a newer revision.

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Return a waiting result before approval, the recorded result on replay, and a stale result when a different request uses an older review.

## Continue

[← Previous lecture](02-constrain-proposals-and-run-checks.md) · [Course outline](index.md) · [Next lecture →](04-compare-workflow-traces-and-handoffs.md)
