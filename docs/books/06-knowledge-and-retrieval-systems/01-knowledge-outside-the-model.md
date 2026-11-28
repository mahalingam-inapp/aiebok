# 6.1 — Knowledge Outside the Model

<p class="study-position" data-course="06-knowledge-and-retrieval-systems" data-lecture="01-knowledge-outside-the-model.md">Knowledge strategy and ingestion · Lecture 1 of 6</p>

[Course outline](index.md#course-outline){ .study-overview } · [Document Ingestion →](02-document-ingestion.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Knowledge strategy and ingestion**

    - **Knowledge Outside the Model** (current)
    - [Document Ingestion](02-document-ingestion.md)

    **Retrieval and reranking**

    - [Retrieval](03-retrieval.md)
    - [Ranking and Context Selection](04-ranking-and-context-selection.md)

    **Grounded answers and enterprise constraints**

    - [RAG Generation and Citations](05-rag-generation-and-citations.md)
    - [Advanced and Enterprise RAG](06-advanced-and-enterprise-rag.md)

*Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

[Download the course notebook](../../assets/notebooks/06-knowledge-and-retrieval-systems.ipynb){ download } · Use the exercise under **Lecture 01**.

## Before you begin

- Courses 03–05 or equivalent experience
- Embeddings and search
- Structured model output

## Why this chapter exists

Decide among direct context, search, databases, knowledge graphs, RAG, fine-tuning, and deterministic rules.

## A policy is state that can change

An employee made a purchase on Sunday and asks on Tuesday. The latest policy alone gives the wrong number for one of those dates.

Persist effective dates outside the model and resolve which revision applies to the requested event. Hold the question fixed and change the event date. The evidence selection should change even if the model and prompt stay identical.

## Learning objectives

- Explain why knowledge outside the model matters using the chapter scenario, not abstract definitions alone.
- Trace how **knowledge freshness** and **grounding** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to fine-tuning.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Put knowledge in the component best suited to update, govern, query, and verify it.

## Mental model

```mermaid
flowchart LR
  N0["Sources"] --> N1["Ingest"]
  N1["Ingest"] --> N2["Retrieve and rerank"]
  N2["Retrieve and rerank"] --> N3["Generate"]
  N3["Generate"] --> N4["Cite and evaluate"]
```

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Knowledge Freshness

Knowledge freshness measures how current stored facts are relative to the real world. Stale indexes cause confident wrong answers until re-ingestion catches up. See the [Knowledge Freshness concept card](../../concepts/cards/knowledge-freshness.md).

**Example:** A travel policy updated yesterday is invisible if the index last synced last month.

**Evidence of understanding:** Track max document age in retrieved sets and alert when any source exceeds SLA staleness.

### Grounding

Grounding ties model statements to verifiable evidence—retrieved passages, database rows, tool outputs. Ungrounded generation is speculation presented as fact. See the [Grounding concept card](../../concepts/cards/grounding.md).

**Example:** Support answers should quote the ticket macro article that authorizes the refund step.

**Evidence of understanding:** Measure percent of claims with valid citations on a labeled answer set.

### Structured Data

Structured data lives in tables, APIs, and graphs with typed fields—better for precise queries than prose retrieval. Hybrid systems route quantitative questions to SQL, not RAG alone. See the [Structured Data concept card](../../concepts/cards/structured-data.md).

**Example:** 'How many open P1 incidents?' needs a database query, not semantic search over runbooks.

**Evidence of understanding:** Route ten numeric questions to structured tools and verify answers match ground truth.

### Retrieval

Retrieval selects candidate evidence from a corpus given a query before ranking and generation. It is candidate generation under relevance and policy constraints—not the final answer. See the [Retrieval concept card](../../concepts/cards/retrieval.md).

**Example:** Hybrid retrieval returns 20 chunks for reranking; generation never sees the full million-document index.

**Evidence of understanding:** Report recall@20 on a labeled query set before tuning downstream prompts.

### Fine-Tuning

Fine-tuning adapts pretrained weights with supervised or preference data when prompts and RAG cannot stabilize behavior. It trades generality and ops simplicity for targeted changes. See the [Fine-Tuning concept card](../../concepts/cards/fine-tuning.md).

**Example:** Support tone and escalation policy may need SFT when prompts drift across thousands of ticket types.

**Evidence of understanding:** Compare fine-tuned and prompt-only models on held-out behavioral eval with rollback plan.

## Worked example

**Book scenario:** An enterprise assistant must answer from authorized policies and cite the exact passages used.

**Situation:** An enterprise assistant must answer from authorized policies and cite exact passages—product debates RAG vs fine-tuning vs bigger context.

**Baseline:** Stuff entire policy PDF into prompt—expensive and still stale.

**Application:** Classify ten requirements (freshness, authorization, structured lookup, style, math) to correct mechanism: retrieval, SQL, tools, fine-tune, or rules; document governance for each.

**Test cases:** (1) Normal: weekly-updated FAQ. (2) Boundary: numeric entitlement needing database query. (3) Adversarial: requirement for legally provable citation from signed PDF page.

**Measurement:** Correct mechanism assignment vs expert review; projected cost and freshness SLA per choice.

**Design question:** Which requirement forces retrieval even if fine-tuning improves tone?

## Follow the code

Run this short Python demonstration of **knowledge outside the model**. Identify the input, the decision or calculation, and the printed result.

```python
CHAPTER = "6.1"
print("chapter hook:", CHAPTER)
requirements = [
    ("cite exact page", "RAG"),
    ("friendly tone", "prompt/finetune"),
    ("live headcount", "SQL tool"),
]
for req, mechanism in requirements:
    print({"requirement": req, "mechanism": mechanism})
print("---")
print("change one input above, predict output, re-run")
```

Predict the result before you run it. Change one input, then explain the resulting difference using the mechanism from the worked example.

For a longer implementation, run the [course code sample](../../code-samples/06-hybrid-rag.py). Documents appearing high in both rankings receive the strongest reciprocal-rank-fusion scores.

## Engineering practice

**Build:** Classify ten requirements by the correct knowledge mechanism.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without knowledge freshness and record quality, latency, and failure cases.
2. **Mechanism:** Add grounding while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when knowledge outside the model earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

**Section checkpoint**

Sketch source identifiers and chunk lineage for two versions of the same policy.

Compare your prediction with the chapter demonstration and explain which input changed the result. The [course notebook](../../assets/notebooks/06-knowledge-and-retrieval-systems.ipynb){ download } contains the runnable examples and a checked experiment. See [notebook setup](../../labs/notebooks/index.md) if you are new to Jupyter.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 6.1 — knowledge outside the model:

1. Draft cases in `test_lab.py` or `specs/lab-0601.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 6.1](../../labs/0601-knowledge-outside-the-model.md)


## Architecture lens

For a production design in **Knowledge and Retrieval Systems**, make the following explicit for **knowledge outside the model**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns knowledge freshness versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the structured data boundary expose? |
| **Evidence** | Which eval slices prove knowledge outside the model meets requirements before and after each release? |
| **Security** | What untrusted data crosses the fine-tuning boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover knowledge freshness or grounding | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | knowledge outside the model is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in fine-tuning without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream knowledge freshness behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Decide among direct context, search, databases, knowledge graphs, RAG, fine-tuning, and deterministic rules. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of knowledge outside the model without explicit knowledge freshness.
- **Today:** Engineering teams implement knowledge outside the model as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but fine-tuning and governance constraints will still require explicit design.
- **What survives:** Put knowledge in the component best suited to update, govern, query, and verify it.

## Knowledge check

1. Why put knowledge in the component best suited to update and verify it?
2. When does fine-tuning fail freshness requirements?
3. What baseline uses only larger context windows?

??? question "Answer guidance"
    Q1: Misplaced knowledge breaks governance and update paths. Q2: Weights lag policy changes; cannot cite reliably. Q3: Whole-corpus prompt stuffing without retrieval.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain knowledge freshness without jargon and give a counterexample.**
       *Proficient answer:* knowledge freshness measures how current stored facts are relative to the real world. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare grounding with fine-tuning using quality, cost, latency, and risk.**
       *Proficient answer:* grounding ties model statements to verifiable evidence—retrieved passages, database rows, tool outputs; fine-tuning adapts pretrained weights with supervised or preference data when prompts and rag cannot stabilize behavior. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after grounding; authorization before any side effect or retrieval of restricted data; observability at the transition knowledge outside the model introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Put knowledge in the component best suited to update, govern, query, and verify it.

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

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Document Ingestion →](02-document-ingestion.md)
{: .study-directions .study-directions--footer }
