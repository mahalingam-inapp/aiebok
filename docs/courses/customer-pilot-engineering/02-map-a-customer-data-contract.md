# Map a customer data contract

[Customer Pilot Engineering](index.md) · Discover and integrate · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Normalize a source payload and publish a versioned integration boundary.

## How it works

Map external fields to internal types and preserve provenance. Reject incomplete records before calling a downstream dependency. Agree who owns the upstream schema and define the service behavior if an unexpected version arrives.

## Worked example

A partner sends a customer ticket ID, topic, and audience flag. Normalize known topics and route any unrecognized topic to review.

## Try it yourself

Run the adapter for the bundled records. Add a case for a field with the wrong type.

[Download the workbook](../../assets/notebooks/customer-pilot-engineering.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Treat the malformed input as a rejected record. Leave the original source identifier available for support.

## Continue

[← Previous lecture](01-discovery-and-pilot-acceptance.md) · [Course outline](index.md) · [Next lecture →](03-shadow-acceptance-and-integration-failures.md)
