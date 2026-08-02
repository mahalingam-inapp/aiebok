# 3.4 — From Sparse Features to Embeddings

*Book 3: Language and Representation · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 1–2
- Vectors and dot products
- Basic text processing

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Move from one-hot vectors, n-grams, TF–IDF, and BM25 to learned dense representations.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain the problem that motivated from sparse features to embeddings.
- Connect the chapter's concepts into one causal mental model.
- Implement or design the bounded practice exercise.
- Evaluate quality, latency, cost, safety, and operational consequences.
- Distinguish enduring principles from current products and APIs.

!!! note "Enduring principle"
    Different representations preserve different relationships; no representation is universally best.

## Mental model

```mermaid
flowchart LR
  N0["Raw language"] --> N1["Tokens"]
  N1["Tokens"] --> N2["Representation"]
  N2["Representation"] --> N3["Similarity"]
  N3["Similarity"] --> N4["Retrieved meaning"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **from sparse features to embeddings** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read across the table before studying any row in isolation.

| Concept | Role in this chapter | Evidence of understanding |
|---|---|---|
| **One-Hot Vectors** | establishes the first representation or decision boundary | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Tf–Idf** | adds the main transformation or comparison | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Bm25** | connects the mechanism to the surrounding system | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Word Embeddings** | controls quality, efficiency, or behavior | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Sentence Embeddings** | exposes an important operating constraint or failure mode | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
## Worked example

**Book scenario:** Employees search for policies using vocabulary different from the source documents.

**Chapter focus:** Move from one-hot vectors, n-grams, TF–IDF, and BM25 to learned dense representations.

Apply this chapter in four moves:

1. Write the observable task and the simplest baseline before selecting a model or framework.
2. Locate where one-hot vectors and TF–IDF enter the book-level visual above.
3. Create one normal case, one boundary case, and one adversarial or failure case.
4. Compare the result using a task-quality measure plus latency, cost, and risk notes.

The design question is: **What evidence would show that from sparse features to embeddings addresses this chapter's problem better than the baseline?** Answer with measured observations rather than intuition alone.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/03-tokenization-vectors.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/03-tokenization-vectors.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The outage document should rank highest because it shares the query's weighted terms; the example also exposes the limits of lexical features.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **one-hot vectors** and **TF–IDF**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Implement TF–IDF and compare it with the included vector lab.

Work in three passes:

1. Establish the simplest deterministic or naive baseline.
2. Add the chapter mechanism while keeping inputs and evaluation fixed.
3. Compare outcomes, inspect failures, and document when the extra complexity is justified.

Capture the code or diagram, assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design, make the following explicit:

| Concern | Question to answer |
|---|---|
| Boundary | Which component owns this capability? |
| Contract | What are its inputs, outputs, errors, and version? |
| Evidence | How will quality be measured before and after release? |
| Security | What data, identity, permission, or misuse risk crosses the boundary? |
| Operations | What is traced, monitored, cached, retried, and rolled back? |
| Economics | Which resource drives latency and cost, and what is the budget? |

## Failure clinic

Do not debug only the final output. Reproduce the failure, preserve the full input and versioned configuration, inspect intermediate state, compare a baseline, and classify the cause. Typical categories are missing or biased data, representation loss, incorrect assumptions, weak retrieval or planning, ambiguous contracts, invalid output, excessive autonomy, authorization gaps, and evaluation mismatch.

## Evolution lens

- **Yesterday:** identify the earlier manual, symbolic, statistical, or single-model approach.
- **Today:** describe the current engineering pattern without tying the principle to one vendor.
- **Tomorrow:** look for better representations, automatic optimization, stronger verification, lower cost, and clearer control.
- **What survives:** Different representations preserve different relationships; no representation is universally best.

## Knowledge check

1. What problem would remain if one-hot vectors were removed from the system?
2. Which observation would distinguish a failure in TF–IDF from a failure in sentence embeddings?
3. What simpler alternative should be the baseline?

??? question "Answer guidance"
    A strong answer names an observable failure, traces it to a specific boundary in the chapter visual, and proposes a test that could disconfirm the explanation. The baseline should remove the chapter mechanism while holding the task and evaluation cases fixed.

## Mastery questions

1. Explain one-hot vectors without jargon and give a counterexample.
2. Compare TF–IDF with sentence embeddings using quality, cost, latency, and risk.
3. Design a minimal experiment that tests the chapter's central claim.
4. Identify which component should own validation, authorization, and observability.
5. State what would remain true if today's leading libraries and vendors disappeared.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Manning, Raghavan & Schütze — Introduction to Information Retrieval
- Mikolov et al. — Efficient Estimation of Word Representations in Vector Space

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
