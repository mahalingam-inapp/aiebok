# Plan a limited launch and rollback

<p class="study-position" data-course="managing-ai-delivery" data-lecture="03-plan-a-limited-launch-and-rollback.md">Launch and respond · Lecture 3 of 4</p>

[← Assign decision and data ownership](02-assign-decision-and-data-ownership.md) · [Course outline](index.md#course-outline){ .study-overview } · [Review an incident and decide when to resume →](04-review-an-incident-and-decide-when-to-resume.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Own quality and risk**

    - [Find the failure hidden in the average](01-find-the-failure-hidden-in-the-average.md)
    - [Assign decision and data ownership](02-assign-decision-and-data-ownership.md)

    **Launch and respond**

    - **Plan a limited launch and rollback** (current)
    - [Review an incident and decide when to resume](04-review-an-incident-and-decide-when-to-resume.md)

## What you will learn

Define the trial audience, stop condition, and fallback.

## Simulate the stop before expanding

A limited rollout can be paused by switching a queue configuration. The reviewer has never checked whether reports already in flight return to the manual queue.

Practice rollback with a test report submitted immediately before the switch. Confirm it is visible to staff and stays associated with its original identifier. Write down who owns the in-flight work.

## How it works

A limited launch exposes a feature to a controlled audience first. Decide which signals pause it, who monitors those signals, and what users experience after rollback. Validate the fallback before opening access.

### Roll back the effect, then verify recovery

A reversible launch gives one group the new behavior while the original process remains usable. Decide on the trigger, who can act, and how to verify recovery before admitting the first real case. Simply restoring a configuration does not establish that the work has returned to staff.

Use three probes in a rehearsal: a request that was already in flight, a new request after rollback, and a duplicate of one that has already completed. Confirm where each appears and what staff are expected to do next. The service may need to preserve identifiers and outcomes even while routing changes.

During a rollout, distinguish a correct result from one that was rescued by a human fallback. A dashboard that counts both as success can hide a growing manual queue. Keep fallback volume visible and agree on how much work the staffed team can handle before you expand the pilot.

## Worked example

A pilot covers one department. If a restricted document is shown to an unauthorized person, the operator immediately turns off the feature and returns users to the approved document portal.

## Try it yourself

Draft a launch scope and stop rule for the first week of a meeting-summary assistant.

??? success "Compare your answer"
    Limit the pilot to opted-in internal meetings. Pause if private content is distributed outside the participant list. Return to the established manual notes workflow.

## Continue

[← Assign decision and data ownership](02-assign-decision-and-data-ownership.md) · [Course outline](index.md#course-outline){ .study-overview } · [Review an incident and decide when to resume →](04-review-an-incident-and-decide-when-to-resume.md)
{: .study-directions .study-directions--footer }
