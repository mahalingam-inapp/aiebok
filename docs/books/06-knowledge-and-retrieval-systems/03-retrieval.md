# 6.3 — Retrieval

*Book 6: Knowledge and Retrieval Systems · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 3–5
- Embeddings and search
- Structured model output

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Compare lexical, dense, sparse, hybrid, filtered, multi-query, parent-child, and late-interaction retrieval.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why retrieval matters using the chapter scenario, not abstract definitions alone.
- Trace how **BM25** and **dense retrieval** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to parent-child retrieval.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Retrieval is candidate selection under relevance and policy constraints.

## Mental model

```mermaid
flowchart LR
  N0["Sources"] --> N1["Ingest"]
  N1["Ingest"] --> N2["Retrieve and rerank"]
  N2["Retrieve and rerank"] --> N3["Generate"]
  N3["Generate"] --> N4["Cite and evaluate"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **retrieval** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### BM25

BM25 ranks documents by weighted term frequency with length normalization and term-frequency saturation. Extra keyword repetition helps less over time compared to raw TF. See the [BM25 concept card](../../concepts/cards/bm25.md).

**Example:** A policy ID in the query should rank the exact section above generic overview pages.

**Evidence of understanding:** Report recall@k on identifier-heavy queries versus a dense-only retriever.

### Dense Retrieval

Dense retrieval embeds queries and documents into the same vector space and returns nearest neighbors by similarity. See the [Dense Retrieval concept card](../../concepts/cards/dense-retrieval.md).

**Example:** A query about 'application unavailable' retrieves 'service is down' without lexical overlap.

**Evidence of understanding:** Build a 30-query eval with paraphrases and hard negatives; report recall@5 and MRR.

### Hybrid Search

Hybrid search combines lexical and dense signals—often via reciprocal rank fusion—when neither alone covers identifiers and paraphrases. See the [Hybrid Search concept card](../../concepts/cards/hybrid-search.md).

**Example:** Fusion surfaces policy IDs lexically while keeping semantic matches for informal phrasing.

**Evidence of understanding:** Show a query where lexical-only and dense-only each miss but fusion succeeds.

### Query Rewriting

Query rewriting transforms requests via expansion, decomposition, or HyDE before retrieval to close vocabulary gaps. See the [Query Rewriting concept card](../../concepts/cards/query-rewriting.md).

**Example:** Expanding 'PTO' to 'paid time off' helps lexical retrievers match handbook language.

**Evidence of understanding:** Compare recall@k with and without rewrite on acronym-heavy queries.

### Parent-Child Retrieval

Parent–child retrieval indexes small child chunks for precision but returns parent sections for generation context. See the [Parent-Child Retrieval concept card](../../concepts/cards/parent-child-retrieval.md).

**Example:** A child bullet may lack the section title needed for a correct answer unless parent is joined.

**Evidence of understanding:** Demonstrate failure with child-only context and fix by returning parent at generation time.

## Worked example

**Book scenario:** An enterprise assistant must answer from authorized policies and cite the exact passages used.

**Situation:** The enterprise assistant must retrieve authorized policy passages for hybrid employee queries mixing IDs and natural language.

**Baseline:** BM25 only—misses paraphrases; dense only—misses policy numbers.

**Application:** Implement lexical and vector baselines, compute recall@k on labeled set, add query rewriting and parent-child chunk retrieval for long policies.

**Test cases:** (1) Normal: "PTO accrual cap 240." (2) Boundary: parent doc updated but child chunks stale. (3) Adversarial: retrieved doc user lacks ACL to read.

**Measurement:** Recall@5 and MRR per query type; ACL-filtered recall (should exclude forbidden docs entirely).

**Design question:** When does parent-child retrieval beat flat chunking on update frequency?

## Chapter hook

Run this short snippet first to anchor **retrieval** before the book-level sample:

```python
CHAPTER = "6.3"
print("chapter hook:", CHAPTER)
docs = {"a": "PTO accrual cap is 240 hours", "b": "Leave policy overview"}
query = set("pto cap".split())
scores = {k: len(query & set(v.lower().split())) for k, v in docs.items()}
print("bm25_proxy:", sorted(scores.items(), key=lambda x: -x[1]))
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **BM25** or **dense retrieval** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/06-hybrid-rag.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/06-hybrid-rag.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Documents appearing high in both rankings receive the strongest reciprocal-rank-fusion scores.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **BM25** and **dense retrieval**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Implement lexical and vector baselines and calculate recall@k.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without bm25 and record quality, latency, and failure cases.
2. **Mechanism:** Add dense retrieval while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when retrieval earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 6.3 — retrieval:

1. Draft cases in `test_lab.py` or `specs/lab-0603.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 6.3](../../labs/0603-retrieval.md)


## Architecture lens

For a production design in **Knowledge and Retrieval Systems**, make the following explicit for **retrieval**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns bm25 versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the hybrid search boundary expose? |
| **Evidence** | Which eval slices prove retrieval meets requirements before and after each release? |
| **Security** | What untrusted data crosses the parent-child retrieval boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover bm25 or dense retrieval | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | retrieval is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in parent-child retrieval without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream bm25 behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Compare lexical, dense, sparse, hybrid, filtered, multi-query, parent-child, and late-interaction retrieval. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of retrieval without explicit bm25.
- **Today:** Engineering teams implement retrieval as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but parent-child retrieval and governance constraints will still require explicit design.
- **What survives:** Retrieval is candidate selection under relevance and policy constraints.

## Knowledge check

1. Why is retrieval candidate selection under policy constraints?
2. How does hybrid search help policy number plus paraphrase queries?
3. What single-channel baseline should hybrid beat?

??? question "Answer guidance"
    Q1: Must enforce relevance and authorization before generation. Q2: Lexical hits IDs, dense hits paraphrase—fusion covers both. Q3: BM25-only or dense-only on labeled 30-query set.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain BM25 without jargon and give a counterexample.**
       *Proficient answer:* bm25 ranks documents by weighted term frequency with length normalization and term-frequency saturation. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare dense retrieval with parent-child retrieval using quality, cost, latency, and risk.**
       *Proficient answer:* dense retrieval embeds queries and documents into the same vector space and returns nearest neighbors by similarity; parent–child retrieval indexes small child chunks for precision but returns parent sections for generation context. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after dense retrieval; authorization before any side effect or retrieval of restricted data; observability at the transition retrieval introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Retrieval is candidate selection under relevance and policy constraints.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Lewis et al. — Retrieval-Augmented Generation
- Karpukhin et al. — Dense Passage Retrieval

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
