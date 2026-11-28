# Record a keep, revise, or stop decision

<p class="study-position" data-course="evaluating-ai-in-practice" data-lecture="04-record-a-keep-revise-or-stop-decision.md">Make a decision with evidence · Lecture 4 of 4</p>

[← Measure time and review burden](03-measure-time-and-review-burden.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Build the comparison**

    - [Pick cases that represent the real task](01-pick-cases-that-represent-the-real-task.md)
    - [Score evidence and omissions](02-score-evidence-and-omissions.md)

    **Make a decision with evidence**

    - [Measure time and review burden](03-measure-time-and-review-burden.md)
    - **Record a keep, revise, or stop decision** (current)

## What you will learn

Make a bounded recommendation with a named reviewer and a test for revisiting the decision.

## Make every recommendation conditional on what you saw

Routine notices pass and save time. The tool gets one time-sensitive notice wrong. Ben has too few cases to estimate how often that will happen.

Record a limited use decision for routine work and keep time-sensitive notices on the manual path. Say what extra evidence or workflow change would make you reconsider.

## How it works

Use the fixed criteria and record which cases support the decision. Keep a short note of what you tested, what failed, the allowed scope, and what evidence would change the decision. A three-case scorecard supports a small experiment and leaves uncertainty explicit.

### Make the result useful to the next decision maker

Put the actual evidence beside the recommendation: the tested tasks, denominators, rework, benefits, and harms. State whether you recommend continuing, revising, or stopping for each relevant task type. A responsible decision may keep the same tool for one purpose and pause it for another.

Name what would change your decision. A narrower prompt could reduce unconfirmed claims on late updates. A staffed review channel could make occasional handoffs acceptable. Ask for a rerun with previously unseen requests and a threshold that can be judged without inventing a new rule after seeing results.

Give a person ownership of the next run and keep the old workflow available. Good evaluation does not need a large deck of scores. It needs a clear statement of what was observed, who experienced the effect, and what action the evidence now permits.

## Worked example

An assistant saves time on routine notices and gives a misleading answer on an emergency closure. Keep emergency notices on the manual workflow and test routine notices with an assigned reviewer before any expansion.

### Follow the example

**Given:** Both workflows handle routine reminders. The assisted one turns an unconfirmed location into a published fact.

**Walkthrough:** Keep assisted drafting for confirmed reminders. Route unconfirmed locations to the organizer and specify a repeat test before revising the decision.

## Try it yourself

Write a decision for a workflow that saves time but has one sensitive-data failure. State what could make it safe to retry.

??? success "Compare your answer"
    Pause that workflow. Remove or protect the sensitive input, assign an accountable reviewer, and recheck the relevant failure cases before a bounded restart.

## Continue

[← Measure time and review burden](03-measure-time-and-review-burden.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
