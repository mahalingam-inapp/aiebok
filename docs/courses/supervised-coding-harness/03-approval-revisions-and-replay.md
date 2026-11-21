# Approval, revisions and replay

<p class="study-position" data-course="supervised-coding-harness" data-lecture="03-approval-revisions-and-replay.md">Approve and audit a change · Lecture 3 of 4</p>

[← Constrain proposals and run checks](02-constrain-proposals-and-run-checks.md) · [Course outline](index.md#course-outline){ .study-overview } · [Compare workflow traces and handoffs →](04-compare-workflow-traces-and-handoffs.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Specify and verify a candidate**

    - [Write an acceptance contract for a change](01-write-an-acceptance-contract-for-a-change.md)
    - [Constrain proposals and run checks](02-constrain-proposals-and-run-checks.md)

    **Approve and audit a change**

    - **Approval, revisions and replay** (current)
    - [Compare workflow traces and handoffs](04-compare-workflow-traces-and-handoffs.md)

## What you will learn

Bind an approval to the reviewed proposal and current revision.

## Approval expires when the reviewed payload changes

A reviewer approves a proposed revision in the morning. A later edit changes the payload before the worker applies it.

Bind approval to the exact reviewed revision and record a stable request identifier. A stale approval should cause a new review. A retry of an already applied version should return its recorded outcome.

## How it works

Approval is a decision about a specific candidate and the state against which it was tested. Compare the reviewed revision with the current revision before applying the change. Store a stable request ID and outcome so retries can return the previous result without repeating the action.

### Bind authorization to a specific revision

An approval for one revision is not general permission to apply later changes. Preserve the exact input, proposed effect, approval, and an operation identifier. Before applying, compare the current proposal with the approved revision. If it changed, ask for a new review.

Now suppose the worker applies a change but the acknowledgment is lost. A retry should return the recorded outcome when the system already completed that operation. Store completion alongside the relevant state change when the storage boundary permits it. An external action needs its own stable request identity and a way to reconcile uncertain outcomes.

Exercise two cases independently. Submitting a changed proposal after approval should wait. Resubmitting the completed operation should produce no second effect. Both cases can look like a duplicate request on arrival, but they need different handling. A trace should retain which revision and completion record the harness used.

## Worked example

A reviewer approves the whitespace change at revision 1. Another edit lands before approval is applied. The old approval now needs a fresh review.

## Try it yourself

Try applying a good proposal before approval. Replay after applying it and then try the old review against a newer revision.

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Return a waiting result before approval, the recorded result on replay, and a stale result when a different request uses an older review.

## Continue

[← Constrain proposals and run checks](02-constrain-proposals-and-run-checks.md) · [Course outline](index.md#course-outline){ .study-overview } · [Compare workflow traces and handoffs →](04-compare-workflow-traces-and-handoffs.md)
{: .study-directions .study-directions--footer }
