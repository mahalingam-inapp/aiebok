# Shadow acceptance and integration failures

[Customer Pilot Engineering](index.md) · Evaluate and hand off · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Exercise normal, ambiguous, restricted, and unavailable-dependency cases before live use.

## How it works

A shadow run records proposed actions while the original workflow retains control. Test the same inputs for both workflows and compare decisions and timing. Make failures easy to retry without duplicating the outcome.

## Worked example

When the routing dependency is unavailable, leave the ticket in manual triage. If an accepted request is delivered twice, return the existing route.

## Try it yourself

Compare the deterministic acceptance results. Add a replay for a successful request and a retry after dependency recovery.

[Download the workbook](../../assets/notebooks/customer-pilot-engineering.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The successful replay returns the same result and creates one record. A transient failure leaves room for a successful retry.

## Continue

[← Previous lecture](02-map-a-customer-data-contract.md) · [Course outline](index.md) · [Next lecture →](04-rollout-operator-handoff-and-stop-rules.md)
