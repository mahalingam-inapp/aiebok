# 1.6 — Engineering with Uncertainty

*Book 1: Foundations of Intelligence · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- No AI background required
- Comfort reading simple Python
- Basic algebra

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Translate uncertain predictions into decisions with thresholds, costs, calibration, fallback behavior, and human oversight.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why engineering with uncertainty matters using the chapter scenario, not abstract definitions alone.
- Trace how **calibration** and **decision thresholds** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to human review.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Prediction and decision are separate layers; consequences belong in the decision layer.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["State model"]
  N1["State model"] --> N2["Search or learn"]
  N2["Search or learn"] --> N3["Decision"]
  N3["Decision"] --> N4["Feedback"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **engineering with uncertainty** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Calibration

Calibration means predicted probabilities align with observed frequencies—70% confidence should be right about 70% of the time. Uncalibrated scores mislead threshold and cost decisions. See the [Calibration concept card](../../concepts/cards/calibration.md).

**Example:** A medical triage model with miscalibrated probabilities causes undertriage when 0.9 confidence actually means 0.6 accuracy.

**Evidence of understanding:** Plot a reliability diagram and report expected calibration error before setting production thresholds.

### Decision Thresholds

Decision thresholds turn continuous scores into actions—approve, escalate, or abstain. They encode business costs and should be tuned on validation data, not defaults. See the [Decision Thresholds concept card](../../concepts/cards/decision-thresholds.md).

**Example:** Raising a fraud threshold reduces false positives but increases missed fraud; the optimum depends on chargeback cost.

**Evidence of understanding:** Sweep thresholds on a validation set and plot precision-recall against expected dollar cost.

### Expected Cost

Expected cost combines probabilities of outcomes with their business costs to rank decisions. It makes asymmetric errors explicit instead of hiding them in accuracy. See the [Expected Cost concept card](../../concepts/cards/expected-cost.md).

**Example:** Approving a loan when P(default)=0.08 is cheap only if the expected loss is below the interest margin.

**Evidence of understanding:** Compute expected cost for three threshold settings and pick the minimum on a labeled validation set.

### Abstention

Abstention lets a system refuse or defer when confidence is insufficient, routing cases to humans or safer paths. It prevents forced wrong answers on ambiguous inputs. See the [Abstention concept card](../../concepts/cards/abstention.md).

**Example:** A benefits bot abstains on incomplete forms instead of guessing eligibility that triggers appeals.

**Evidence of understanding:** Measure coverage (non-abstain rate) versus accuracy on handled cases and set abstention to hit a risk target.

### Human Review

Human review inserts expert judgment for high-impact or low-confidence decisions. Designing the queue—what gets reviewed, SLA, feedback loop—determines ROI. See the [Human Review concept card](../../concepts/cards/human-review.md).

**Example:** Loan officers review only applications where the model score falls in the 0.4–0.6 band, covering 12% of volume at 3× higher fraud catch.

**Evidence of understanding:** Track review queue depth, override rate, and post-review error rate weekly.

## Worked example

**Book scenario:** A support team must route incidents without mistaking fluent descriptions for reliable decisions.

**Situation:** The classifier outputs P1 probability 0.72; policy must decide whether to page on-call given asymmetric costs of false alarms vs missed outages.

**Baseline:** Always page when probability > 0.5 regardless of cost or calibration.

**Application:** Plot reliability diagram, pick threshold minimizing expected cost (false page $200 vs missed outage $50k), add abstention band sending borderline tickets to human triage.

**Test cases:** (1) Normal: calibrated 0.9 on confirmed outage. (2) Boundary: 0.55 after Platt scaling on small val set. (3) Adversarial: model overconfident on marketing "urgency" language.

**Measurement:** Expected cost curve vs threshold, ECE calibration error, and page rate at chosen policy.

**Design question:** Why should threshold selection happen in a decision layer separate from the scoring model?

## Chapter hook

Run this short snippet first to anchor **engineering with uncertainty** before the book-level sample:

```python
scores = [0.92, 0.61, 0.48, 0.33]
COST = {"fp": 200, "fn": 50000}
def expected_cost(threshold):
    decisions = [s >= threshold for s in scores]
    truth = [True, True, False, False]
    fp = sum(d and not t for d, t in zip(decisions, truth))
    fn = sum(not d and t for d, t in zip(decisions, truth))
    return fp * COST["fp"] + fn * COST["fn"]
for t in [0.5, 0.6, 0.7, 0.8]:
    print(f"threshold={t} expected_cost={expected_cost(t)}")
```

Predict the printed values, then change one line tied to **calibration** or **decision thresholds** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/01-search-planning.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/01-search-planning.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    A* should reach the same shortest path as breadth-first search while often expanding fewer states when the heuristic is informative.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **calibration** and **decision thresholds**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Design a decision policy for a high-cost false-positive scenario.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without calibration and record quality, latency, and failure cases.
2. **Mechanism:** Add decision thresholds while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when engineering with uncertainty earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 1.6 — engineering with uncertainty:

1. Draft cases in `test_lab.py` or `specs/lab-0106.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 1.6](../../labs/0106-engineering-with-uncertainty.md)


## Architecture lens

For a production design in **Foundations of Intelligence**, make the following explicit for **engineering with uncertainty**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns calibration versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the expected cost boundary expose? |
| **Evidence** | Which eval slices prove engineering with uncertainty meets requirements before and after each release? |
| **Security** | What untrusted data crosses the human review boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover calibration or decision thresholds | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | engineering with uncertainty is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in human review without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream calibration behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Translate uncertain predictions into decisions with thresholds, costs, calibration, fallback behavior, and human oversight. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of engineering with uncertainty without explicit calibration.
- **Today:** Engineering teams implement engineering with uncertainty as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but human review and governance constraints will still require explicit design.
- **What survives:** Prediction and decision are separate layers; consequences belong in the decision layer.

## Knowledge check

1. What goes wrong if you tune decision thresholds on the training set?
2. How would miscalibration appear in an incident paging policy?
3. What baseline policy ignores model scores entirely?

??? question "Answer guidance"
    Q1: Threshold overfits noise, inflates false pages on holdout months. Q2: High scores on non-outages in reliability diagram. Q3: Always-page or keyword-only paging with fixed rules.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain calibration without jargon and give a counterexample.**
       *Proficient answer:* calibration means predicted probabilities align with observed frequencies—70% confidence should be right about 70% of the time. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare decision thresholds with human review using quality, cost, latency, and risk.**
       *Proficient answer:* decision thresholds turn continuous scores into actions—approve, escalate, or abstain; human review inserts expert judgment for high-impact or low-confidence decisions. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after decision thresholds; authorization before any side effect or retrieval of restricted data; observability at the transition engineering with uncertainty introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Prediction and decision are separate layers; consequences belong in the decision layer.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Russell & Norvig — Artificial Intelligence: A Modern Approach
- Sutton & Barto — Reinforcement Learning: An Introduction

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
