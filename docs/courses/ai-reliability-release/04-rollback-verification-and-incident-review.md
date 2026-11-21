# Rollback verification and incident review

<p class="study-position" data-course="ai-reliability-release" data-lecture="04-rollback-verification-and-incident-review.md">Release and recover · Lecture 4 of 4</p>

[← Canary cohorts and staged gates](03-canary-cohorts-and-staged-gates.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Define and observe reliability**

    - [Service objectives and error-budget burn](01-service-objectives-and-error-budget-burn.md)
    - [Stage traces and failure localization](02-stage-traces-and-failure-localization.md)

    **Release and recover**

    - [Canary cohorts and staged gates](03-canary-cohorts-and-staged-gates.md)
    - **Rollback verification and incident review** (current)

## What you will learn

Restore stable routing, run a smoke check, and assemble a factual incident timeline.

## Write the timeline while decisions are still clear

The candidate is disabled and the next test request succeeds. Olivia needs to prove that affected users are now served by the stable model and that the queue is recovering.

Check both cohorts, note the observed version and outcome, then record detection, decision, mitigation, and validation in order. Attach one owned follow-up with a concrete verification condition.

## How it works

After a rollback, verify that new requests reach the expected version and that the service indicators recover. Record detection, decision, mitigation, and validation times. Write follow-up actions with an owner and verification criterion.

### Close the loop from rollback to user recovery

Restore the prior serving version and verify the effect through a request representative of the affected cohort. Confirm version, result, latency, and whether any manual work remains queued. The rollback can restore new traffic while leaving older work that still needs reconciliation.

Build a timeline while evidence is available. Separate detection, decision, mitigation, verification, and follow-up. Preserve the observed impact and the source of each observation. If the cause is uncertain, label it and assign a way to investigate rather than treating a plausible story as a confirmed explanation.

A useful follow-up has an owner and a verification condition. “Add monitoring” is vague. “Alert when generation wait breaches the candidate gate on the replayed fixture” tells reviewers how to know the change works. Verify that people can still resolve delayed requests, not only that the graph returned to normal.

## Worked example

The on-call engineer pauses the candidate, confirms stable responses from the affected cohort, and records a follow-up to test dependency failure before the next release.

## Try it yourself

Run the scripted incident. Extend the report with one owner, one preventable failure, and a due condition.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The incident review distinguishes measured cause and impact from hypotheses and includes evidence that rollback restored service.

## Continue

[← Canary cohorts and staged gates](03-canary-cohorts-and-staged-gates.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
