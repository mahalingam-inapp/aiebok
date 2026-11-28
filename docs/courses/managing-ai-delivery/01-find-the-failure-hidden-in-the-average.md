# Find the failure hidden in the average

<p class="study-position" data-course="managing-ai-delivery" data-lecture="01-find-the-failure-hidden-in-the-average.md">Own quality and risk · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Assign decision and data ownership →](02-assign-decision-and-data-ownership.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Own quality and risk**

    - **Find the failure hidden in the average** (current)
    - [Assign decision and data ownership](02-assign-decision-and-data-ownership.md)

    **Launch and respond**

    - [Plan a limited launch and rollback](03-plan-a-limited-launch-and-rollback.md)
    - [Review an incident and decide when to resume](04-review-an-incident-and-decide-when-to-resume.md)

## What you will learn

Identify a critical user group or circumstance that needs its own evidence.

## The same average hides two experiences

The trial gets 90 of 100 reports right. It misses 4 of 10 urgent reports and 6 of 90 routine reports.

Compare the urgent miss rate of 40% with roughly 7% for routine reports. The overall score does not describe either group. Require a separately justified decision for urgent routing.

## How it works

A slice is a meaningful subset of cases, such as a language or request type. Aggregate accuracy can be high while a small group experiences frequent errors. Review slices with distinct consequences and report how many examples were checked.

### Ask whose experience the average represents

An overall rate weights groups by how often they occur in the sample. Routine reports in a large queue can conceal repeated errors on a smaller group. Start by listing the cases for which failure carries a different consequence or requires a different recovery process.

If a trial routes 86 of 90 routine reports and 6 of 10 urgent reports correctly, the total is 92 of 100. An urgent reporter sees a 60% observed success rate. The small urgent sample makes that estimate uncertain, and it is already a reason to collect better evidence before delegation. Write counts alongside percentages.

Avoid slicing only after noticing a surprising number. Predeclare the groups you must protect, the expected result, and who reviews the case. Continue to inspect new clusters of errors during operation. A reviewer looking at the actual misroutes can often distinguish a missing intake field from a poor decision rule faster than a dashboard can.

## Worked example

A tool is correct on 95 of 100 tickets. If all five mistakes are urgent tickets, the overall score obscures the urgent-case failure.

### Follow the example

**Given:** A team reports ‘pilot complete’ and shares an encouraging screenshot without the case set.

**Walkthrough:** Request the versioned inputs, current workflow, comparison results, and approval record. Tie the milestone to evidence the next reviewer can reproduce.

## Try it yourself

A feature is correct on 99 of 100 outputs. The one wrong answer gives an incorrect emergency contact. What evidence would you ask for before expansion?

??? success "Compare your answer"
    Ask for a dedicated emergency-contact check, including current authorized source records and representative variations. Require that slice to pass its own criterion.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Assign decision and data ownership →](02-assign-decision-and-data-ownership.md)
{: .study-directions .study-directions--footer }
