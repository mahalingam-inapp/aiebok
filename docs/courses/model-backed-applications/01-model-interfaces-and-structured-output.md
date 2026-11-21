# Model interfaces and structured output

[Build and Evaluate a Model-Backed Application](index.md) · Implement the contract and baseline · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Validate a model response and distinguish response-format errors from provider failures.

## How it works

Define a small typed contract before choosing a model. Treat a response as untrusted input and validate each required field, value, and relationship. A malformed JSON reply and a provider timeout should both activate the fallback while remaining distinguishable in logs. Keep provider-specific code behind one callable.

## Worked example

A service desk assistant returns a status, a short answer, and source IDs. A reply with source_ids set to a string cannot satisfy the contract. A valid abstention has an empty answer and no sources.

## Try it yourself

Run the contract cases. Add a syntactically valid response with an unknown status and explain why JSON parsing alone accepts it.

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Reject the status during semantic validation and test that the handler returns the same public fallback without losing the failure category internally.

## Continue

[Course outline](index.md) · [Next lecture →](02-retrieval-evidence-and-citations.md)
