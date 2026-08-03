# 1.5 — Learning and Generalization

*Book 1: Foundations of Intelligence · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- No AI background required
- Comfort reading simple Python
- Basic algebra

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Distinguish memorization from generalization and training from inference. Understand data-generating processes, inductive bias, overfitting, underfitting, and distribution shift.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why learning and generalization matters using the chapter scenario, not abstract definitions alone.
- Trace how **training** and **inference** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to distribution shift.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    A system is useful when it performs under future conditions, not merely on its training examples.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["State model"]
  N1["State model"] --> N2["Search or learn"]
  N2["Search or learn"] --> N3["Decision"]
  N3["Decision"] --> N4["Feedback"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **learning and generalization** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Training

Training fits model parameters to data by minimizing a loss over many examples. It defines what behavior the model is rewarded for and must be separated from inference in operations. See the [Training concept card](../../concepts/cards/training.md).

**Example:** Fine-tuning a classifier on support tickets teaches phrasing patterns that inference-time prompts alone may not stabilize.

**Evidence of understanding:** Log training loss, validation loss, and one task metric per epoch and stop when validation degrades.

### Inference

Inference applies a trained model to new inputs to produce predictions or generations. Serving latency, cost, and correctness are measured here—not during training. See the [Inference concept card](../../concepts/cards/inference.md).

**Example:** A production chatbot runs inference on every user message; batching ten requests changes throughput but not the trained weights.

**Evidence of understanding:** Measure p50 and p95 latency for single and batched requests at fixed concurrency.

### Generalization

Generalization is performance on unseen data drawn from the deployment distribution, not memorization of training examples. The central engineering question is whether the system will work next month on real users. See the [Generalization concept card](../../concepts/cards/generalization.md).

**Example:** A memorizing model hits 100% on training tickets but fails on new product names never seen during training.

**Evidence of understanding:** Compare train and held-out slice metrics and require held-out performance above a release threshold.

### Bias And Variance

Bias is systematic underfitting from overly simple models; variance is sensitivity to training noise from overly complex ones. Tuning trades these errors against compute and data volume. See the [Bias And Variance concept card](../../concepts/cards/bias-and-variance.md).

**Example:** A linear model underfits nonlinear fraud patterns (high bias); a huge tree overfits small samples (high variance).

**Evidence of understanding:** Plot error versus model capacity and identify the knee where validation error stops improving.

### Distribution Shift

Distribution shift occurs when deployment data differs from training data in language, demographics, seasonality, or product mix. Models degrade silently when shift is unmonitored. See the [Distribution Shift concept card](../../concepts/cards/distribution-shift.md).

**Example:** A model trained pre-acquisition fails on the acquired company's ticket vocabulary until retrained or augmented.

**Evidence of understanding:** Monitor slice metrics weekly and alert when any slice drops more than five points from its baseline.

## Worked example

**Book scenario:** A support team must route incidents without mistaking fluent descriptions for reliable decisions.

**Situation:** A pilot ML classifier labels incident severity from historical tickets, but performance collapses after a product rename changes customer vocabulary.

**Baseline:** Memorize exact training phrases with a hash map—perfect on train, useless on deploy.

**Application:** Train/validation split by time, fit models of increasing capacity (linear → bigram → small neural), plot train vs validation error, and document distribution shift when product codenames change.

**Test cases:** (1) Normal: phrasing seen in training month. (2) Boundary: new product name with same failure semantics. (3) Adversarial: label noise—mis-tagged P3 tickets marked P1.

**Measurement:** Pre/post-rename F1, learning curves, and slice error on renamed-product tickets.

**Design question:** What evidence distinguishes overfitting from distribution shift on the rename slice?

## Chapter hook

Run this short snippet first to anchor **learning and generalization** before the book-level sample:

```python
data = [(1, 0), (2, 0), (3, 1), (4, 1), (5, 2)]
labels = [0, 0, 1, 1, 0]
def mse_line(m, b, pts):
    return sum((m*x + b - y)**2 for x, y in pts) / len(pts)
best = min(((m, b, mse_line(m, b, data)) for m in [0, 0.5, 1.0] for b in [0, 0.5]), key=lambda t: t[2])
holdout = [(6, 1), (7, 1)]
test_err = mse_line(best[0], best[1], holdout)
print({"fit": best[:2], "train_mse": round(best[2], 3), "holdout_mse": round(test_err, 3)})
```

Predict the printed values, then change one line tied to **training** or **inference** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/01-search-planning.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/01-search-planning.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    A* should reach the same shortest path as breadth-first search while often expanding fewer states when the heuristic is informative.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **training** and **inference**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Fit increasingly flexible models to a small noisy dataset and plot errors.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without training and record quality, latency, and failure cases.
2. **Mechanism:** Add inference while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when learning and generalization earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design in **Foundations of Intelligence**, make the following explicit for **learning and generalization**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns training versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the generalization boundary expose? |
| **Evidence** | Which eval slices prove learning and generalization meets requirements before and after each release? |
| **Security** | What untrusted data crosses the distribution shift boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover training or inference | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | learning and generalization is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in distribution shift without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream training behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Distinguish memorization from generalization and training from inference. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of learning and generalization without explicit training.
- **Today:** Engineering teams implement learning and generalization as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but distribution shift and governance constraints will still require explicit design.
- **What survives:** A system is useful when it performs under future conditions, not merely on its training examples.

## Knowledge check

1. What observable pattern indicates memorization rather than generalization on tickets?
2. How does a time-based split change your interpretation of validation error?
3. What is the minimal model family for a severity baseline?

??? question "Answer guidance"
    Q1: Zero training error with high validation error on paraphrased tickets. Q2: Random split hides temporal shift; time split surfaces rename failures. Q3: Linear or logistic model on bag-of-words.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain training without jargon and give a counterexample.**
       *Proficient answer:* training fits model parameters to data by minimizing a loss over many examples. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare inference with distribution shift using quality, cost, latency, and risk.**
       *Proficient answer:* inference applies a trained model to new inputs to produce predictions or generations; distribution shift occurs when deployment data differs from training data in language, demographics, seasonality, or product mix. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after inference; authorization before any side effect or retrieval of restricted data; observability at the transition learning and generalization introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* A system is useful when it performs under future conditions, not merely on its training examples.

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
