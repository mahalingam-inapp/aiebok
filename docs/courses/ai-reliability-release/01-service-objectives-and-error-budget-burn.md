# Service objectives and error-budget burn

<p class="study-position" data-course="ai-reliability-release" data-lecture="01-service-objectives-and-error-budget-burn.md">Define and observe reliability · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Stage traces and failure localization →](02-stage-traces-and-failure-localization.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Define and observe reliability**

    - **Service objectives and error-budget burn** (current)
    - [Stage traces and failure localization](02-stage-traces-and-failure-localization.md)

    **Release and recover**

    - [Canary cohorts and staged gates](03-canary-cohorts-and-staged-gates.md)
    - [Rollback verification and incident review](04-rollback-verification-and-incident-review.md)

## What you will learn

Define a good request and calculate reliability and budget burn over a bounded window.

## A user can receive a response and still lose time

A late summary eventually arrives, after an agent already opened a second ticket to work around the delay. Transport success stays green.

Define a good outcome in terms of valid and timely work. Use the cohort denominator and the agreed objective to estimate burn. Keep the observation window and sample size attached to the number.

## How it works

A service objective uses outcomes a user cares about, such as a valid, grounded result delivered under a latency bound. The error budget is the allowed fraction of bad requests. Burn rate compares the observed bad fraction with that allowance.

### Count a good request as the caller experiences it

A service-level indicator should define a usable result. For an assistant, that could require a valid answer or useful handoff within a deadline. A transport success with a late, malformed, or unsupported result might fail this definition. State the eligible population and observation window.

An objective of 99% good results allows 1% bad results in the chosen window. If the measured bad rate is 5%, the budget is being consumed at five times the allowed rate for that window. Burn expresses the pace of failure relative to the target, rather than the total incident impact on its own.

Check the cohort denominator and sample size. A small sample can be enough to reveal a severe problem, even though it gives a noisy estimate of the true rate. Decide when to alert, when to gather more evidence, and when a critical failure independently requires pausing.

## Worked example

With a 99% objective, a 5% bad rate burns error budget at five times the sustainable rate.

## Try it yourself

Compute objectives for the fixture cohorts. Change the latency threshold and decide which failures count.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A successful transport can still be a bad outcome if the result is invalid or late. State the denominator and report low sample counts.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Stage traces and failure localization →](02-stage-traces-and-failure-localization.md)
{: .study-directions .study-directions--footer }
