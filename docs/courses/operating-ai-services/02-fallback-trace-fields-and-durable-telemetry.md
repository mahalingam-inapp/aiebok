# Fallback, trace fields and durable telemetry

[Deploy and Operate an AI Service](index.md) · Package and observe · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Record provider failures and successful fallback without storing request text.

## How it works

A fallback may preserve availability while hiding primary failures from aggregate success. Measure the primary failure rate separately. Capture request ID, requested and served versions, elapsed time, and the fallback outcome. Persist the telemetry so the release gate can query it.

## Worked example

A candidate fails to answer during a dry run. The baseline serves it and the trace preserves the fact that a fallback occurred.

## Try it yourself

Trigger the bundled provider failure. Query the telemetry and check that sensitive request text is absent.

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The stored row should show the candidate as requested and baseline as served with a fallback flag.

## Continue

[← Previous lecture](01-serve-a-versioned-endpoint.md) · [Course outline](index.md) · [Next lecture →](03-canary-evaluation-and-rollout-decisions.md)
