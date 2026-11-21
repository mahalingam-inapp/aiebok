# Review an incident and decide when to resume

<p class="study-position" data-course="managing-ai-delivery" data-lecture="04-review-an-incident-and-decide-when-to-resume.md">Launch and respond · Lecture 4 of 4</p>

[← Plan a limited launch and rollback](03-plan-a-limited-launch-and-rollback.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Own quality and risk**

    - [Find the failure hidden in the average](01-find-the-failure-hidden-in-the-average.md)
    - [Assign decision and data ownership](02-assign-decision-and-data-ownership.md)

    **Launch and respond**

    - [Plan a limited launch and rollback](03-plan-a-limited-launch-and-rollback.md)
    - **Review an incident and decide when to resume** (current)

## What you will learn

Separate containment, learning, and the relaunch decision.

## Resume only after checking the original failure

A pilot route is paused after several urgent reports land in general intake. The supplier ships a configuration change and reports that its health check is green.

Ask for evidence that the original urgent cases now route correctly and that staff can handle a manual fallback. Record the decision and resume within a small cohort until operational evidence is available.

## How it works

Contain the failure first and preserve records needed to understand its impact. Identify the cause, add a test that would catch it, and verify the correction before resuming. Record who approves the relaunch and which limits still apply.

### A green health check answers a narrow question

After a failure, record what users saw, which work is in an uncertain state, and which stage first diverged from normal behavior. System availability and correct user outcomes are different questions. A healthy service may still be applying the wrong rule or using stale evidence.

Before resuming, reproduce the original failing cases using the proposed fix. Check the accepted outcome and the handoff for any open work. If a failure is consequential or poorly understood, restart with a smaller group and observe it under the actual release conditions. A staged recovery makes the result easier to interpret.

Write down what would cause the incident team to halt again. Assign one person to communicate affected cases and another, if needed, to verify that the recovery worked. Keeping those duties explicit prevents a technical fix from being mistaken for a complete resolution for the people who were affected.

## Worked example

An assistant sent an outdated notice. The team stopped the output, corrected the source selection, verified a case with conflicting versions, and asked the content owner to approve resumption.

## Try it yourself

A pilot generated summaries using superseded procedure documents. Give one containment action, one corrective test, and one condition for resuming.

??? success "Compare your answer"
    Pause affected summaries, test retrieval against a current and superseded document, and resume only after the current document is reliably selected and the responsible owner approves.

## Continue

[← Plan a limited launch and rollback](03-plan-a-limited-launch-and-rollback.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
