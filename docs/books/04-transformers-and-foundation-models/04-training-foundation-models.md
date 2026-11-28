# 4.4 — Training Foundation Models

<p class="study-position" data-course="04-transformers-and-foundation-models" data-lecture="04-training-foundation-models.md">Transformer blocks and training · Lecture 4 of 6</p>

[← The Transformer Block](03-the-transformer-block.md) · [Course outline](index.md#course-outline){ .study-overview } · [Inference and Sampling →](05-inference-and-sampling.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Sequence models and attention**

    - [Sequence Models Before Transformers](01-sequence-models-before-transformers.md)
    - [Attention](02-attention.md)

    **Transformer blocks and training**

    - [The Transformer Block](03-the-transformer-block.md)
    - **Training Foundation Models** (current)

    **Decoding and model selection**

    - [Inference and Sampling](05-inference-and-sampling.md)
    - [Model Families and Selection](06-model-families-and-selection.md)

*Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

[Download the course notebook](../../assets/notebooks/04-transformers-and-foundation-models.ipynb){ download } · Use the exercise under **Lecture 04**.

## Before you begin

- Courses 01–03 or equivalent experience
- Matrix multiplication intuition
- Neural-network basics

## Why this chapter exists

Study autoregressive, masked, and sequence-to-sequence objectives; data mixtures; scaling; checkpoints; and mixture-of-experts.

## Learn the task without seeing the answer key

The transcript collection contains meeting minutes and near-duplicate action-item exports. An evaluation set built from the same exports looks much cleaner than the actual meeting traffic.

Split by meeting series before creating windows, then deduplicate across splits. Keep evaluation examples from unseen teams and newer recordings. Otherwise a pretraining or fine-tuning comparison can reward memorization of workflow artifacts.

## Learning objectives

- Explain why training foundation models matters using the chapter scenario, not abstract definitions alone.
- Trace how **pretraining objectives** and **data mixtures** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to mixture of experts.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Pretraining compresses statistical regularities into parameters; it does not create a fact database.

## Mental model

```mermaid
flowchart LR
  N0["Tokens"] --> N1["Attention"]
  N1["Attention"] --> N2["Transformer layers"]
  N2["Transformer layers"] --> N3["Logits"]
  N3["Logits"] --> N4["Sampled token"]
```

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Pretraining Objectives

Pretraining objectives define self-supervised targets—causal LM, masked LM, denoising—that shape what models learn from raw text. Objective choice affects bidirectionality and use cases. See the [Pretraining Objectives concept card](../../concepts/cards/pretraining-objectives.md).

**Example:** Causal LM suits generation; masked LM suits understanding tasks before fine-tuning.

**Evidence of understanding:** Compare downstream task scores after pretraining two small models with different objectives.

### Data Mixtures

Data mixtures blend corpora—web, code, books, dialog—at tuned ratios during pretraining. Mixture proportions strongly affect capabilities and biases. See the [Data Mixtures concept card](../../concepts/cards/data-mixtures.md).

**Example:** Over-weighting code improves programming but may hurt conversational tone.

**Evidence of understanding:** Ablate one corpus slice from the mixture and measure task-specific eval deltas.

### Scaling Laws

Scaling laws relate model size, data, and compute to predictable loss improvements—guiding budget allocation. They are approximate and domain-dependent. See the [Scaling Laws concept card](../../concepts/cards/scaling-laws.md).

**Example:** Doubling parameters may yield diminishing returns if data quality does not scale similarly.

**Evidence of understanding:** Fit a loss-versus-compute curve on three model sizes and extrapolate budget for target loss.

### Checkpoints

Checkpoints persist durable agent state so interrupted runs resume without repeating side effects. See the [Checkpoints concept card](../../concepts/cards/checkpoints.md).

**Example:** After approval gate, checkpoint stores pending payment until human approves, then continues.

**Evidence of understanding:** Kill run mid-loop, restore checkpoint, verify idempotent tools are not duplicated.

### Mixture Of Experts

A sparse mixture-of-experts layer routes each token to a subset of expert feed-forward networks and combines their outputs. Resident weight memory, shared computation, and cross-device communication matter even when few experts are active. See the [Mixture Of Experts concept card](../../concepts/cards/mixture-of-experts.md).

**Example:** A layer with eight equally sized routed experts and top-2 routing uses two experts per token. A shared expert, if present, adds work for every token.

**Evidence of understanding:** Report active and resident parameters separately. Measure skew, overflow or queueing, and quality on realistic input bursts.

## Worked example

**Book scenario:** A team must explain why decoding settings change model output and latency.

**Situation:** Leadership asks for compute and data estimates to pretrain a tiny domain language model on internal policies without mistaking pretraining for a fact database.

**Baseline:** Assume memorizing all policies guarantees correct answers at inference.

**Application:** Estimate tokens in corpus, parameters for small GPT-style model, training steps given batch and context; distinguish pretraining objective (next-token) from downstream QA needs.

**Test cases:** (1) Normal: 10M tokens, 50M params. (2) Boundary: corpus dominated by duplicated templates. (3) Adversarial: contaminated eval documents inside pretrain mix.

**Measurement:** Tokens/param ratio, estimated GPU-hours, contamination check pass rate.

**Design question:** What evidence would show the model compressed statistical patterns rather than storing retrievable policy text verbatim?

## Follow the code

Run this short Python demonstration of **training foundation models**. Identify the input, the decision or calculation, and the printed result.

```python
CHAPTER = "4.4"
print("chapter hook:", CHAPTER)
tokens, params, epochs, batch = 10_000_000, 50_000_000, 1, 32
steps = tokens // (batch * 512)
ratio = tokens / params
print({"train_steps_approx": steps, "tokens_per_param": round(ratio, 2)})
print("note: pretrain learns distributions, not a queryable policy DB")
print("---")
print("change one input above, predict output, re-run")
```

Predict the result before you run it. Change one input, then explain the resulting difference using the mechanism from the worked example.

For a longer implementation, run the [course code sample](../../code-samples/04-attention-sampling.py). The query-aligned value receives more attention, and lower temperature concentrates the sampling distribution.

## Engineering practice

**Build:** Estimate compute and data requirements for a tiny language model.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without pretraining objectives and record quality, latency, and failure cases.
2. **Mechanism:** Add data mixtures while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when training foundation models earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

**Section checkpoint**

Draw the path through attention and the feed-forward block. Mark where training computes a loss.

Compare your prediction with the chapter demonstration and explain which input changed the result. The [course notebook](../../assets/notebooks/04-transformers-and-foundation-models.ipynb){ download } contains the runnable examples and a checked experiment. See [notebook setup](../../labs/notebooks/index.md) if you are new to Jupyter.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 4.4 — training foundation models:

1. Draft cases in `test_lab.py` or `specs/lab-0404.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 4.4](../../labs/0404-training-foundation-models.md)


## Architecture lens

For a production design in **Transformers and Foundation Models**, make the following explicit for **training foundation models**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns pretraining objectives versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the scaling laws boundary expose? |
| **Evidence** | Which eval slices prove training foundation models meets requirements before and after each release? |
| **Security** | What untrusted data crosses the mixture of experts boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover pretraining objectives or data mixtures | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | training foundation models is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in mixture of experts without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream pretraining objectives behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Study autoregressive, masked, and sequence-to-sequence objectives; data mixtures; scaling; checkpoints; and mixture-of-experts. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of training foundation models without explicit pretraining objectives.
- **Today:** Engineering teams implement training foundation models as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but mixture of experts and governance constraints will still require explicit design.
- **What survives:** Pretraining compresses statistical regularities into parameters; it does not create a fact database.

## Knowledge check

1. Why does pretraining not create a reliable fact database?
2. How does template duplication distort scaling estimates?
3. What baseline uses retrieval instead of pretraining for policy facts?

??? question "Answer guidance"
    Q1: Models interpolate and hallucinate; facts need grounding mechanisms. Q2: Effective tokens << raw tokens—inflated capacity estimates. Q3: RAG over authoritative policy index with same QA eval.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain pretraining objectives without jargon and give a counterexample.**
       *Proficient answer:* pretraining objectives define self-supervised targets—causal lm, masked lm, denoising—that shape what models learn from raw text. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare data mixtures with mixture of experts using quality, cost, latency, and risk.**
       *Proficient answer:* data mixtures blend corpora—web, code, books, dialog—at tuned ratios during pretraining; a sparse mixture-of-experts layer routes each token to a subset of expert feed-forward networks and combines their outputs. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after data mixtures; authorization before any side effect or retrieval of restricted data; observability at the transition training foundation models introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Pretraining compresses statistical regularities into parameters; it does not create a fact database.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Vaswani et al. — Attention Is All You Need
- Devlin et al. — BERT
- Brown et al. — Language Models are Few-Shot Learners

## Continue

[← The Transformer Block](03-the-transformer-block.md) · [Course outline](index.md#course-outline){ .study-overview } · [Inference and Sampling →](05-inference-and-sampling.md)
{: .study-directions .study-directions--footer }
