# 10.2 — Metrics and Human Judgment

*Book 10: Evaluation, Safety, and Governance · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–9
- Statistics intuition
- Threat-model basics

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Combine exact metrics, semantic similarity, pairwise comparison, human review, LLM judges, calibration, and uncertainty.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why metrics and human judgment matters using the chapter scenario, not abstract definitions alone.
- Trace how **deterministic metrics** and **human evaluation** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to inter-rater agreement.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Every metric encodes a theory of quality; validate that theory against real decisions.

## Mental model

```mermaid
flowchart LR
  N0["Requirements"] --> N1["Cases and threats"]
  N1["Cases and threats"] --> N2["Measures"]
  N2["Measures"] --> N3["Risk gate"]
  N3["Risk gate"] --> N4["Assurance record"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **metrics and human judgment** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Deterministic Metrics

Deterministic metrics—exact match, F1 on spans, JSON validity—give reproducible scores without sampling variance. See the [Deterministic Metrics concept card](../../concepts/cards/deterministic-metrics.md).

**Example:** Schema validation pass rate is deterministic; helpfulness often is not.

**Evidence of understanding:** Prefer deterministic metrics for CI gates; use statistical metrics with confidence intervals for quality tracking.

### Human Evaluation

Human evaluation labels outputs quality when automation cannot capture nuance or safety. Design for rater training, agreement, and throughput. See the [Human Evaluation concept card](../../concepts/cards/human-evaluation.md).

**Example:** Lawyers label contract summaries for legal accuracy on 50 cases monthly.

**Evidence of understanding:** Track inter-rater agreement and adjudicate disagreements with gold committee.

### Llm Judges

LLM judges automate scoring using rubrics but must be calibrated against humans to avoid systematic bias. See the [Llm Judges concept card](../../concepts/cards/llm-judges.md).

**Example:** GPT-4 judge scores faithfulness correlated 0.85 with human labels after calibration.

**Evidence of understanding:** Sample 10% human audit of LLM judge scores each sprint; recalibrate if drift >5 points.

### Confidence Intervals

Confidence intervals quantify uncertainty in metric estimates from finite eval sets. Comparing models requires overlapping intervals or formal tests. See the [Confidence Intervals concept card](../../concepts/cards/confidence-intervals.md).

**Example:** Model A at 82% ± 3% versus Model B at 85% ± 4% may not be significantly different.

**Evidence of understanding:** Report 95% CI for primary metrics; require non-overlap for major release claims.

### Inter-Rater Agreement

Inter-rater agreement measures how consistently multiple human graders apply rubrics—Cohen's kappa, Krippendorff's alpha. See the [Inter-Rater Agreement concept card](../../concepts/cards/inter-rater-agreement.md).

**Example:** Low agreement on tone dimension means rubric needs refinement before scaling labeling.

**Evidence of understanding:** Compute kappa per rubric dimension; block scaling if below 0.6.

## Worked example

**Book scenario:** A high-impact assistant may pass average quality while failing a safety-critical user slice.

**Situation:** Automated metrics disagree with compliance reviewers on whether answers are "good enough."

**Baseline:** BLEU score on reference answers—misaligned with policy fidelity.

**Application:** Calibrate LLM judge against two human reviewers on 50 cases, measure inter-rater agreement, use pairwise comparisons for tie-breaks, report confidence intervals on pass rates.

**Test cases:** (1) Normal: all raters agree pass. (2) Boundary: judge-human disagreement. (3) Adversarial: judge favors fluent hallucination.

**Measurement:** Cohen's kappa judge-human, calibration drift over time, cost per human review hour.

**Design question:** When must human review override an automated judge pass?

## Chapter hook

Run this short snippet first to anchor **metrics and human judgment** before the book-level sample:

```python
CHAPTER = "10.2"
print("chapter hook:", CHAPTER)
human = [1, 0, 1, 1]
judge = [1, 1, 1, 0]
agree = sum(h == j for h, j in zip(human, judge)) / len(human)
print({"agreement": round(agree, 2)})
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **deterministic metrics** or **human evaluation** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/10-evaluation-slices.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/10-evaluation-slices.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The release gate depends on both overall performance and perfect performance in the high-risk slice.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **deterministic metrics** and **human evaluation**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Calibrate an automated judge against two human reviewers.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without deterministic metrics and record quality, latency, and failure cases.
2. **Mechanism:** Add human evaluation while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when metrics and human judgment earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 10.2 — metrics and human judgment:

1. Draft cases in `test_lab.py` or `specs/lab-1002.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 10.2](../../labs/1002-metrics-and-human-judgment.md)


## Architecture lens

For a production design in **Evaluation, Safety, and Governance**, make the following explicit for **metrics and human judgment**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns deterministic metrics versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the llm judges boundary expose? |
| **Evidence** | Which eval slices prove metrics and human judgment meets requirements before and after each release? |
| **Security** | What untrusted data crosses the inter-rater agreement boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover deterministic metrics or human evaluation | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | metrics and human judgment is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in inter-rater agreement without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream deterministic metrics behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Combine exact metrics, semantic similarity, pairwise comparison, human review, LLM judges, calibration, and uncertainty. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of metrics and human judgment without explicit deterministic metrics.
- **Today:** Engineering teams implement metrics and human judgment as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but inter-rater agreement and governance constraints will still require explicit design.
- **What survives:** Every metric encodes a theory of quality; validate that theory against real decisions.

## Knowledge check

1. Why does every metric encode a theory of quality?
2. How do confidence intervals change release decisions?
3. What metric baseline uses exact match on paraphrases?

??? question "Answer guidance"
    Q1: BLEU rewards n-grams not fidelity or safety. Q2: Wide CI on small slice means pass rate uncertain—gate may fail. Q3: Exact string match on reference answers.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain deterministic metrics without jargon and give a counterexample.**
       *Proficient answer:* deterministic metrics—exact match, f1 on spans, json validity—give reproducible scores without sampling variance. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare human evaluation with inter-rater agreement using quality, cost, latency, and risk.**
       *Proficient answer:* human evaluation labels outputs quality when automation cannot capture nuance or safety; inter-rater agreement measures how consistently multiple human graders apply rubrics—cohen's kappa, krippendorff's alpha. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after human evaluation; authorization before any side effect or retrieval of restricted data; observability at the transition metrics and human judgment introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Every metric encodes a theory of quality; validate that theory against real decisions.

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
