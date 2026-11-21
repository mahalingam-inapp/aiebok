# Compare workflow traces and handoffs

<p class="study-position" data-course="supervised-coding-harness" data-lecture="04-compare-workflow-traces-and-handoffs.md">Approve and audit a change · Lecture 4 of 4</p>

[← Approval, revisions and replay](03-approval-revisions-and-replay.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Specify and verify a candidate**

    - [Write an acceptance contract for a change](01-write-an-acceptance-contract-for-a-change.md)
    - [Constrain proposals and run checks](02-constrain-proposals-and-run-checks.md)

    **Approve and audit a change**

    - [Approval, revisions and replay](03-approval-revisions-and-replay.md)
    - **Compare workflow traces and handoffs** (current)

## What you will learn

Use a fixed suite to compare proposals and design a human handoff with useful evidence.

## Make the result make sense in the morning

The on-call engineer finds that three proposals were blocked. A log with only ‘false’ leaves the team guessing why.

Record the proposed revision, check result, owner, and next action. Distinguish an invalid proposal from pending approval and an applied replay so another colleague can safely continue.

## How it works

Count validated proposals, test passes, approval waits, and applications separately. A trace should be detailed enough to reproduce the decision and compact enough for a reviewer to scan. In a framework, carry the proposal ID and revision through each transition and keep the executor boundary explicit.

### Tell the next operator what actually happened

A compact trace can show the request, proposal, checks, decision owner, applied revision, and outcome. It gives the reviewer a way to understand a blocked effect without replaying every intermediate generation. Organize traces by stable request identity so retries can be followed across process restarts.

Compare traces from two workflows at the decision points. One may spend less time generating changes but produce more rejected proposals. Another may wait longer for review but lower the rate of surprises after execution. Include total completion time, reviewer effort, and unresolved work when judging the workflow.

A handoff should distinguish “check failed and needs a revised proposal,” “passed and waiting for a human,” and “already applied.” Those states imply different next steps. Test that a new operator can pick up the right action using the evidence in the trace, without needing access to hidden model reasoning.

## Worked example

Two candidates may look identical in a summary. A trace showing a failed whitespace case and a review approval against a specific revision distinguishes them.

## Try it yourself

Create a small report from the trace. Identify what the reviewer sees at each blocked stage.

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The report should name the failed check or approval state and the next responsible person. Keep the evidence tied to the exact candidate.

## Continue

[← Approval, revisions and replay](03-approval-revisions-and-replay.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
