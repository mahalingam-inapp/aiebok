# 10.3 — Evaluation by System Stage

*Book 10: Evaluation, Safety, and Governance · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–9
- Statistics intuition
- Threat-model basics

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Evaluate ingestion, retrieval, generation, tools, agents, UX, latency, cost, and business outcomes separately and together.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why evaluation by system stage matters using the chapter scenario, not abstract definitions alone.
- Trace how **component evals** and **retrieval metrics** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to end-to-end evals.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Stage-specific evaluation makes failures diagnosable and improvements attributable.

## Mental model

```mermaid
flowchart LR
  N0["Requirements"] --> N1["Cases and threats"]
  N1["Cases and threats"] --> N2["Measures"]
  N2["Measures"] --> N3["Risk gate"]
  N3["Risk gate"] --> N4["Assurance record"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **evaluation by system stage** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Component Evals

Component evals test retrieval, generation, tools, and UX stages independently before end-to-end runs. They localize failures. See the [Component Evals concept card](../../concepts/cards/component-evals.md).

**Example:** Retrieval recall@10 evaluated separately from answer faithfulness on same queries.

**Evidence of understanding:** Build failure attribution matrix mapping end-to-end misses to component scores.

### Retrieval Metrics

Retrieval metrics—recall@k, MRR, nDCG—measure candidate set quality before generation sees it. See the [Retrieval Metrics concept card](../../concepts/cards/retrieval-metrics.md).

**Example:** High recall@20 with poor faithfulness suggests generation issue, not retrieval.

**Evidence of understanding:** Report recall@5, @10, @20 on fixed query set each index version.

### Faithfulness

Faithfulness checks that generated statements are entailed by retrieved evidence, not hallucinated additions. It is separate from fluency or user satisfaction. See the [Faithfulness concept card](../../concepts/cards/faithfulness.md).

**Example:** Correct tone but wrong deductible amount is unfaithful despite readable prose.

**Evidence of understanding:** Use NLI or human rubric on 100 answers; require faithfulness ≥ threshold for release.

### Tool Success

Tool success rate tracks correct schema, auth, execution, and useful results from tool calls. It isolates integration failures from model reasoning. See the [Tool Success concept card](../../concepts/cards/tool-success.md).

**Example:** 60% tool success with high answer quality still blocks reliable agents.

**Evidence of understanding:** Log tool error taxonomy—validation, timeout, 403—and set minimum success rate gate.

### End-To-End Evals

End-to-end evals measure full pipeline outcomes on realistic inputs including latency and cost. See the [End-To-End Evals concept card](../../concepts/cards/end-to-end-evals.md).

**Example:** User question to cited answer passes only if retrieval, generation, and citation all succeed.

**Evidence of understanding:** Run weekly end-to-end suite with production config hash in report.

## Worked example

**Book scenario:** A high-impact assistant may pass average quality while failing a safety-critical user slice.

**Situation:** RAG assistant fails in production; team argues whether retrieval, generation, or tools caused it.

**Baseline:** End-to-end thumbs-up/down only.

**Application:** Build failure attribution matrix: ingestion, retrieval recall, rerank, generation faithfulness, tool success, UX; run component evals with frozen downstream gold inputs.

**Test cases:** (1) Normal: retrieval fails, generation good. (2) Boundary: all components pass component tests but E2E fails interaction. (3) Adversarial: metric gaming by overfitting reranker to eval queries.

**Measurement:** Component pass rates, attributed failure percentage, fix validation on targeted slice.

**Design question:** Which component eval would you run first given wrong citations but right topic?

## Chapter hook

Run this short snippet first to anchor **evaluation by system stage** before the book-level sample:

```python
CHAPTER = "10.3"
print("chapter hook:", CHAPTER)
matrix = {"retrieval": 0.6, "rerank": 0.8, "generation": 0.9}
symptom = "wrong doc cited"
if symptom == "wrong doc cited":
    first = min(matrix, key=matrix.get)
print("investigate first:", first)
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **component evals** or **retrieval metrics** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/10-evaluation-slices.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/10-evaluation-slices.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The release gate depends on both overall performance and perfect performance in the high-risk slice.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **component evals** and **retrieval metrics**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Build a failure attribution matrix for a RAG system.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without component evals and record quality, latency, and failure cases.
2. **Mechanism:** Add retrieval metrics while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when evaluation by system stage earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design in **Evaluation, Safety, and Governance**, make the following explicit for **evaluation by system stage**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns component evals versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the faithfulness boundary expose? |
| **Evidence** | Which eval slices prove evaluation by system stage meets requirements before and after each release? |
| **Security** | What untrusted data crosses the end-to-end evals boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover component evals or retrieval metrics | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | evaluation by system stage is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in end-to-end evals without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream component evals behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Evaluate ingestion, retrieval, generation, tools, agents, UX, latency, cost, and business outcomes separately and together. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of evaluation by system stage without explicit component evals.
- **Today:** Engineering teams implement evaluation by system stage as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but end-to-end evals and governance constraints will still require explicit design.
- **What survives:** Stage-specific evaluation makes failures diagnosable and improvements attributable.

## Knowledge check

1. Why evaluate stages separately and together?
2. How does failure attribution guide fixes?
3. What baseline evaluates end-to-end only?

??? question "Answer guidance"
    Q1: Isolates fixable boundaries vs interaction bugs. Q2: Low retrieval recall → fix index before tuning prompts. Q3: Single user satisfaction score.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain component evals without jargon and give a counterexample.**
       *Proficient answer:* component evals test retrieval, generation, tools, and ux stages independently before end-to-end runs. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare retrieval metrics with end-to-end evals using quality, cost, latency, and risk.**
       *Proficient answer:* retrieval metrics—recall@k, mrr, ndcg—measure candidate set quality before generation sees it; end-to-end evals measure full pipeline outcomes on realistic inputs including latency and cost. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after retrieval metrics; authorization before any side effect or retrieval of restricted data; observability at the transition evaluation by system stage introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Stage-specific evaluation makes failures diagnosable and improvements attributable.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- NIST AI Risk Management Framework
- OWASP guidance for LLM applications
- Task-specific evaluation research

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
