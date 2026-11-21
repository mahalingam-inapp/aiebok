# Write an acceptance contract for a change

[Supervised Coding-Agent Harnesses](index.md) · Specify and verify a candidate · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Turn a small change request into regression and acceptance examples.

## How it works

An acceptance case states an observable input and expected output. Freeze current behaviors you want to preserve before asking for a change, and keep acceptance cases independent from any particular implementation. A small fixture makes a failing example cheap to inspect.

## Worked example

A task-title formatter should now remove redundant spaces. Existing lowercasing and empty-title behavior still matter. Add a fixture for tabs and a case that captures the default title.

## Try it yourself

Write one legacy case and one case that fails with the baseline.

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The whitespace case should reproduce the new requirement. The legacy case should remain green after the change.

## Continue

[Course outline](index.md) · [Next lecture →](02-constrain-proposals-and-run-checks.md)
