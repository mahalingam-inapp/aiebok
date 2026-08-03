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

- Explain why from sparse features to embeddings matters using the chapter scenario, not abstract definitions alone.
- Trace how **one-hot vectors** and **TF–IDF** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to sentence embeddings.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

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

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### One-Hot Vectors

One-hot vectors encode categorical items as sparse binary indicators—simple but high-dimensional and semantically blind. They remain baselines for small categorical features. See the [One-Hot Vectors concept card](../../concepts/cards/one-hot-vectors.md).

**Example:** Encoding 10k product IDs as one-hot vectors is impractical; embeddings replace them at scale.

**Evidence of understanding:** Compare memory and lookup time for one-hot versus learned embedding on the same catalog size.

### TF–IDF

TF–IDF weights terms by local frequency and inverse document frequency, highlighting discriminative words in sparse retrieval. It is a strong lexical baseline before dense methods. See the [TF–IDF concept card](../../concepts/cards/tf-idf.md).

**Example:** Searching 'PTO accrual cap' ranks handbook sections containing rare terms 'accrual' and 'cap' highly.

**Evidence of understanding:** Measure recall@10 on 30 keyword-heavy queries against a dense baseline.

### BM25

BM25 ranks documents by weighted term frequency with length normalization and term-frequency saturation. Extra keyword repetition helps less over time compared to raw TF. See the [BM25 concept card](../../concepts/cards/bm25.md).

**Example:** A policy ID in the query should rank the exact section above generic overview pages.

**Evidence of understanding:** Report recall@k on identifier-heavy queries versus a dense-only retriever.

### Word Embeddings

Word embeddings map tokens to dense vectors where semantic similarity corresponds to geometric proximity. They enable arithmetic analogies and feed neural NLP stacks. See the [Word Embeddings concept card](../../concepts/cards/word-embeddings.md).

**Example:** 'King' − 'man' + 'woman' ≈ 'queen' in classic Word2Vec demonstrations of linear structure.

**Evidence of understanding:** Evaluate nearest neighbors for 20 domain terms and have experts rate relevance.

### Sentence Embeddings

Sentence embeddings encode whole utterances into vectors for semantic search and clustering. Quality depends on training objective and domain match. See the [Sentence Embeddings concept card](../../concepts/cards/sentence-embeddings.md).

**Example:** Embedding employee questions matches handbook paraphrases even without shared keywords.

**Evidence of understanding:** Benchmark recall@5 on paraphrase pairs with hard negative passages in the index.

## Worked example

**Book scenario:** Employees search for policies using vocabulary different from the source documents.

**Situation:** Employees query "work from home equipment stipend" but policies use "remote office allowance." Lexical search misses relevant paragraphs.

**Baseline:** BM25 over stemmed terms—weak on paraphrase.

**Application:** Implement TF–IDF vectors for policies, compare cosine retrieval vs BM25 on a 30-query eval set, then contrast with dense embedding lab results on hard paraphrases.

**Test cases:** (1) Normal: shared keyword "stipend." (2) Boundary: query with acronym only. (3) Adversarial: query matches wrong doc via high-IDF junk terms ("pursuant", "herein").

**Measurement:** Recall@5 for lexical vs dense on paraphrase slice; average query latency.

**Design question:** For which query types would you still prefer sparse TF–IDF over embeddings in production?

## Chapter hook

Run this short snippet first to anchor **from sparse features to embeddings** before the book-level sample:

```python
docs = {"a": "remote office allowance for home equipment", "b": "expense report submission deadline"}
query_terms = set("work from home equipment stipend".split())
def tfidf_score(q, doc):
    doc_terms = doc.lower().split()
    overlap = len(q & set(doc_terms))
    return overlap / (len(doc_terms) + 1)
scores = {k: tfidf_score(query_terms, v) for k, v in docs.items()}
print("ranking:", sorted(scores.items(), key=lambda x: -x[1]))
```

Predict the printed values, then change one line tied to **one-hot vectors** or **TF–IDF** and observe how the chapter mechanism moves.

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

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without one-hot vectors and record quality, latency, and failure cases.
2. **Mechanism:** Add tf–idf while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when from sparse features to embeddings earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design in **Language and Representation**, make the following explicit for **from sparse features to embeddings**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns one-hot vectors versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the bm25 boundary expose? |
| **Evidence** | Which eval slices prove from sparse features to embeddings meets requirements before and after each release? |
| **Security** | What untrusted data crosses the sentence embeddings boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover one-hot vectors or tf–idf | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | from sparse features to embeddings is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in sentence embeddings without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream one-hot vectors behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Move from one-hot vectors, n-grams, TF–IDF, and BM25 to learned dense representations. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of from sparse features to embeddings without explicit one-hot vectors.
- **Today:** Engineering teams implement from sparse features to embeddings as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but sentence embeddings and governance constraints will still require explicit design.
- **What survives:** Different representations preserve different relationships; no representation is universally best.

## Knowledge check

1. What relationships do sparse TF–IDF vectors preserve that dense embeddings may blur?
2. When does BM25 beat cosine on identical vocabulary?
3. What lexical baseline must dense retrieval beat on identifier queries?

??? question "Answer guidance"
    Q1: Exact term overlap and rare discriminators. Q2: Short queries with exact rare tokens and no paraphrase. Q3: BM25 or TF–IDF with same corpus and eval queries.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain one-hot vectors without jargon and give a counterexample.**
       *Proficient answer:* one-hot vectors encode categorical items as sparse binary indicators—simple but high-dimensional and semantically blind. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare TF–IDF with sentence embeddings using quality, cost, latency, and risk.**
       *Proficient answer:* tf–idf weights terms by local frequency and inverse document frequency, highlighting discriminative words in sparse retrieval; sentence embeddings encode whole utterances into vectors for semantic search and clustering. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after tf–idf; authorization before any side effect or retrieval of restricted data; observability at the transition from sparse features to embeddings introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Different representations preserve different relationships; no representation is universally best.

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
