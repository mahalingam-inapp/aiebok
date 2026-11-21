# Service objectives and error-budget burn

[AI Reliability and Release Engineering](index.md) · Define and observe reliability · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Define a good request and calculate reliability and budget burn over a bounded window.

## How it works

A service objective uses outcomes a user cares about, such as a valid, grounded result delivered under a latency bound. The error budget is the allowed fraction of bad requests. Burn rate compares the observed bad fraction with that allowance.

## Worked example

With a 99% objective, a 5% bad rate burns error budget at five times the sustainable rate.

## Try it yourself

Compute objectives for the fixture cohorts. Change the latency threshold and decide which failures count.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A successful transport can still be a bad outcome if the result is invalid or late. State the denominator and report low sample counts.

## Continue

[Course outline](index.md) · [Next lecture →](02-stage-traces-and-failure-localization.md)
