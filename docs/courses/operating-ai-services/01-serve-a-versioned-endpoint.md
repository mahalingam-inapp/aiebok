# Serve a versioned endpoint

[Deploy and Operate an AI Service](index.md) · Package and observe · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Expose a local HTTP endpoint with explicit version and health behavior.

## How it works

A model service has an externally testable contract and versioned implementation. Readiness answers whether the service may receive traffic. A smoke test sends a known request across the same transport the caller uses and checks the response and version.

## Worked example

A policy helper returns an answer or handoff plus the requested and served versions. A separate health endpoint lets routing detect an unavailable process.

## Try it yourself

Run the in-process application smoke check. Use the loopback HTTP smoke client in the final lecture to test the same contract through the network stack.

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The response identifies the active version and health succeeds without invoking a model.

## Continue

[Course outline](index.md) · [Next lecture →](02-fallback-trace-fields-and-durable-telemetry.md)
