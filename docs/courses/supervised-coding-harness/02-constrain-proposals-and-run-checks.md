# Constrain proposals and run checks

[Supervised Coding-Agent Harnesses](index.md) · Specify and verify a candidate · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Validate the shape and scope of a proposed change before running the acceptance suite.

## How it works

A model can propose a typed change request without receiving a shell or arbitrary file-writing capability. In the workbook, a proposal selects one registered formatter. The harness rejects unknown actions and runs the same fixtures against each candidate. The review record retains test details.

## Worked example

A known but incorrect formatter lowercases text while preserving doubled spaces. It passes some existing behaviors and still fails the added requirement.

## Try it yourself

Evaluate an unknown proposal and a known incorrect candidate. Compare the failure categories.

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    An unknown proposal fails validation. A known candidate should return concrete test failures for the reviewer.

## Continue

[← Previous lecture](01-write-an-acceptance-contract-for-a-change.md) · [Course outline](index.md) · [Next lecture →](03-approval-revisions-and-replay.md)
