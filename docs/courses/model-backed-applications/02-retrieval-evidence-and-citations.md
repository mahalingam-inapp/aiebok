# Retrieval, evidence and citations

[Build and Evaluate a Model-Backed Application](index.md) · Implement the contract and baseline · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Build a retrieval baseline, measure top-k recall, and enforce evidence scope before ranking.

## How it works

Start with lexical retrieval over passages with stable IDs and explicit roles. Filter relevance candidates by permission before scoring, then check that model citations refer to the actual retrieved snippets. ID validation catches fabricated citations. Checking the answer against the passage is a separate step.

## Worked example

A travel-policy question may retrieve a correct current article and an unrelated reimbursement rule. Source IDs let you compare rankings against labeled expectations and inspect why the current article was missed.

## Try it yourself

Compare the results for an employee and a policy reviewer. Add a query with no answer in the allowed documents.

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The employee never sees reviewer-only passages. The no-answer case returns no citations, even if the question is phrased fluently.

## Continue

[← Previous lecture](01-model-interfaces-and-structured-output.md) · [Course outline](index.md) · [Next lecture →](03-grounding-checks-and-evaluation-slices.md)
