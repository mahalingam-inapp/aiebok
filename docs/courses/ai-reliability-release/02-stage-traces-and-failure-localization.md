# Stage traces and failure localization

[AI Reliability and Release Engineering](index.md) · Define and observe reliability · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Use structured events to locate the earliest divergence between candidate and baseline.

## How it works

Record the first failing stage and bounded latency signals for retrieval, generation, and validation. Separate infrastructure failures from poor answer quality and group by version and cohort.

## Worked example

Candidate users receive several timeouts during generation. Retrieval is fast for both cohorts, so the trace points investigation to the candidate dependency.

## Try it yourself

Run the failure aggregation and examine how the diagnosis changes if you move the injected failure to retrieval.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The dominant failing stage should follow the injection while stable traffic stays unaffected.

## Continue

[← Previous lecture](01-service-objectives-and-error-budget-burn.md) · [Course outline](index.md) · [Next lecture →](03-canary-cohorts-and-staged-gates.md)
