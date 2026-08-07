# 10.1 — Evaluation as Requirements

*Book 10: Evaluation, Safety, and Governance · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–9
- Statistics intuition
- Threat-model basics

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Turn desired behavior into tasks, cases, metrics, rubrics, slices, thresholds, and explicit failure tolerances.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why evaluation as requirements matters using the chapter scenario, not abstract definitions alone.
- Trace how **task definitions** and **gold datasets** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to thresholds.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Evaluation is executable requirements for uncertain behavior.

## Mental model

```mermaid
flowchart LR
  N0["Requirements"] --> N1["Cases and threats"]
  N1["Cases and threats"] --> N2["Measures"]
  N2["Measures"] --> N3["Risk gate"]
  N3["Risk gate"] --> N4["Assurance record"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **evaluation as requirements** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Task Definitions

Task definitions specify input, expected output, constraints, and graders for eval cases. Vague tasks produce noisy, incomparable metrics. See the [Task Definitions concept card](../../concepts/cards/task-definitions.md).

**Example:** 'Summarize ticket' becomes 'Extract product, issue, sentiment JSON matching schema X'.

**Evidence of understanding:** Peer-review ten task definitions for ambiguity before adding to gold set.

### Gold Datasets

Gold datasets hold authoritative labels or reference outputs for evaluation. They require versioning, access control, and refresh cadence. See the [Gold Datasets concept card](../../concepts/cards/gold-datasets.md).

**Example:** 200 lawyer-reviewed contract clauses with gold entity spans versioned quarterly.

**Evidence of understanding:** Hash dataset version in every eval report; reject runs on unversioned snapshots.

### Rubrics

Rubrics score qualitative outputs against anchored criteria with examples at each level. They enable consistent human and LLM judging. See the [Rubrics concept card](../../concepts/cards/rubrics.md).

**Example:** Support reply rubric scores correctness, completeness, tone, citations on 1–4 scale.

**Evidence of understanding:** Calibrate two raters on 20 cases; report Cohen's kappa ≥ target before solo grading.

### Slices

Slices are subpopulations—language, tenant, risk tier—where aggregate metrics may hide failure. See the [Slices concept card](../../concepts/cards/slices.md).

**Example:** 95% overall accuracy can mask 60% on enterprise accounts.

**Evidence of understanding:** Report metrics on three production slices with separate release thresholds.

### Thresholds

Thresholds are minimum acceptable metric values for release or routing decisions. They encode risk appetite numerically. See the [Thresholds concept card](../../concepts/cards/thresholds.md).

**Example:** Faithfulness ≥ 0.92 and P0 safety 100% required for production promotion.

**Evidence of understanding:** Document threshold rationale and review quarterly with incident data.

## Worked example

**Book scenario:** A high-impact assistant may pass average quality while failing a safety-critical user slice.

**Situation:** A high-impact assistant may pass average quality while failing a safety-critical user slice—executive dashboards look green.

**Baseline:** Ten happy-path demo prompts as "eval."

**Application:** Derive 30 cases from real workflow risks (access grants, PII, abstention), assign rubrics, slices, pass thresholds, explicit tolerances for critical failures (zero tolerance on privilege escalation).

**Test cases:** (1) Normal: FAQ with citation. (2) Boundary: partial policy coverage. (3) Adversarial: combined injection plus privilege request.

**Measurement:** Pass rate overall and on critical slice, failure taxonomy, threshold gate decision.

**Design question:** Which case would you promote to blocking gate despite small sample size?

## Chapter hook

Run this short snippet first to anchor **evaluation as requirements** before the book-level sample:

```python
CHAPTER = "10.1"
print("chapter hook:", CHAPTER)
cases = [
    {"id": 1, "input": "reset password", "must": "link to policy"},
    {"id": 2, "input": "delete tenant", "must": "require approval"},
]
for case in cases:
    print(case["id"], case["must"])
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **task definitions** or **gold datasets** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/10-evaluation-slices.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/10-evaluation-slices.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The release gate depends on both overall performance and perfect performance in the high-risk slice.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **task definitions** and **gold datasets**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Write a 30-case evaluation set from real workflow risks.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without task definitions and record quality, latency, and failure cases.
2. **Mechanism:** Add gold datasets while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when evaluation as requirements earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 10.1 — evaluation as requirements:

1. Draft cases in `test_lab.py` or `specs/lab-1001.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 10.1](../../labs/1001-evaluation-as-requirements.md)


## Architecture lens

For a production design in **Evaluation, Safety, and Governance**, make the following explicit for **evaluation as requirements**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns task definitions versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the rubrics boundary expose? |
| **Evidence** | Which eval slices prove evaluation as requirements meets requirements before and after each release? |
| **Security** | What untrusted data crosses the thresholds boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover task definitions or gold datasets | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | evaluation as requirements is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in thresholds without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream task definitions behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Turn desired behavior into tasks, cases, metrics, rubrics, slices, thresholds, and explicit failure tolerances. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of evaluation as requirements without explicit task definitions.
- **Today:** Engineering teams implement evaluation as requirements as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but thresholds and governance constraints will still require explicit design.
- **What survives:** Evaluation is executable requirements for uncertain behavior.

## Knowledge check

1. Why is evaluation executable requirements for uncertain behavior?
2. How do slices differ from aggregate pass rates?
3. What eval baseline uses demo prompts only?

??? question "Answer guidance"
    Q1: Tests encode must-hold behaviors with measurable pass/fail. Q2: Slices isolate populations where harm concentrates. Q3: Handful of cherry-picked successes.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain task definitions without jargon and give a counterexample.**
       *Proficient answer:* task definitions specify input, expected output, constraints, and graders for eval cases. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare gold datasets with thresholds using quality, cost, latency, and risk.**
       *Proficient answer:* gold datasets hold authoritative labels or reference outputs for evaluation; thresholds are minimum acceptable metric values for release or routing decisions. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after gold datasets; authorization before any side effect or retrieval of restricted data; observability at the transition evaluation as requirements introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Evaluation is executable requirements for uncertain behavior.

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
