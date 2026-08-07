# 4.6 — Model Families and Selection

*Book 4: Transformers and Foundation Models · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 1–3
- Matrix multiplication intuition
- Neural-network basics

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Compare base, instruction, reasoning, code, embedding, reranking, reward, safety, speech, vision, and diffusion models.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why model families and selection matters using the chapter scenario, not abstract definitions alone.
- Trace how **instruction tuning** and **reasoning models** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to model routing.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Select models as replaceable components against requirements, not by reputation.

## Mental model

```mermaid
flowchart LR
  N0["Tokens"] --> N1["Attention"]
  N1["Attention"] --> N2["Transformer layers"]
  N2["Transformer layers"] --> N3["Logits"]
  N3["Logits"] --> N4["Sampled token"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **model families and selection** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Instruction Tuning

Instruction tuning fine-tunes models on prompt–response pairs covering diverse tasks, improving zero-shot instruction following. It shapes helpfulness and format compliance. See the [Instruction Tuning concept card](../../concepts/cards/instruction-tuning.md).

**Example:** After instruction tuning, models follow 'respond in JSON' without task-specific fine-tuning.

**Evidence of understanding:** Compare instruction-following score on 50 held-out prompts before and after tuning.

### Reasoning Models

Reasoning models allocate extra inference compute—long chains, self-checks—for math, code, and planning tasks. They trade latency and cost for accuracy on hard problems. See the [Reasoning Models concept card](../../concepts/cards/reasoning-models.md).

**Example:** A reasoning model may emit scratchpad steps before the final answer on a budget word problem.

**Evidence of understanding:** Measure accuracy and tokens used versus a base model on a reasoning benchmark.

### Multimodal Models

Multimodal models ingest text, images, audio, or video in shared architectures for joint understanding or generation. Modality alignment and tokenization differ per input type. See the [Multimodal Models concept card](../../concepts/cards/multimodal-models.md).

**Example:** A vision-language model answers questions about chart images in earnings reports.

**Evidence of understanding:** Evaluate field extraction accuracy on 50 document images with ground-truth labels.

### Open Weights

Open-weights models publish parameters for local deployment, fine-tuning, and inspection—versus API-only access. They shift control, compliance, and operational burden to your team. See the [Open Weights concept card](../../concepts/cards/open-weights.md).

**Example:** Self-hosting Llama enables air-gapped inference but requires GPU ops and security patching.

**Evidence of understanding:** Document license terms, hardware requirements, and eval parity versus API baseline before adoption.

### Model Routing

Model routing directs requests to appropriate models by task, risk, cost, or latency policy. See the [Model Routing concept card](../../concepts/cards/model-routing.md).

**Example:** Regex on ticket category routes billing to fine-tuned small model, general to large.

**Evidence of understanding:** Log route decisions; compare blended cost and quality versus single-model baseline.

## Worked example

**Book scenario:** A team must explain why decoding settings change model output and latency.

**Situation:** Platform team must pick among base, instruction-tuned, code, embedding, and reranker models for the policy assistant—vendor marketing overwhelms requirements.

**Baseline:** Choose the largest model name on the leaderboard regardless of task.

**Application:** Define task-specific dataset (QA, citation, routing), benchmark candidates on accuracy/latency/cost slices, document when to route simple queries to small instruct model and hard ones to reasoning model.

**Test cases:** (1) Normal: straightforward policy lookup. (2) Boundary: query needing reranker after retrieval. (3) Adversarial: benchmark prompt leaked in training data inflates scores.

**Measurement:** Task success by model tier, $/1k requests, rollback time when swapping models.

**Design question:** Which requirement would force a dedicated reranker instead of a larger generative model?

## Chapter hook

Run this short snippet first to anchor **model families and selection** before the book-level sample:

```python
tasks = {"lookup": 0.95, "cite": 0.88, "route": 0.91}
models = {"small-instruct": 0.01, "large-reason": 0.08}
def route(task, risk):
    if risk == "low" and tasks[task] > 0.9:
        return "small-instruct"
    return "large-reason"
for risk in ("low", "high"):
    print({"risk": risk, "model": route("lookup", risk), "cost_per_1k": models[route("lookup", risk)]})
```

Predict the printed values, then change one line tied to **instruction tuning** or **reasoning models** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/04-attention-sampling.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/04-attention-sampling.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The query-aligned value receives more attention, and lower temperature concentrates the sampling distribution.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **instruction tuning** and **reasoning models**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Benchmark candidate models on a task-specific dataset.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without instruction tuning and record quality, latency, and failure cases.
2. **Mechanism:** Add reasoning models while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when model families and selection earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 4.6 — model families and selection:

1. Draft cases in `test_lab.py` or `specs/lab-0406.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 4.6](../../labs/0406-model-families-and-selection.md)


## Architecture lens

For a production design in **Transformers and Foundation Models**, make the following explicit for **model families and selection**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns instruction tuning versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the multimodal models boundary expose? |
| **Evidence** | Which eval slices prove model families and selection meets requirements before and after each release? |
| **Security** | What untrusted data crosses the model routing boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover instruction tuning or reasoning models | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | model families and selection is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in model routing without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream instruction tuning behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Compare base, instruction, reasoning, code, embedding, reranking, reward, safety, speech, vision, and diffusion models. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of model families and selection without explicit instruction tuning.
- **Today:** Engineering teams implement model families and selection as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but model routing and governance constraints will still require explicit design.
- **What survives:** Select models as replaceable components against requirements, not by reputation.

## Knowledge check

1. Why select models against requirements rather than reputation?
2. When does an embedding model replace a generative model in the stack?
3. What baseline routes everything to one flagship model?

??? question "Answer guidance"
    Q1: Leaderboard tasks rarely match enterprise slices or governance constraints. Q2: Pure retrieval/ranking steps need vectors or cross-encoders, not generation. Q3: Single largest LLM for all endpoints.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain instruction tuning without jargon and give a counterexample.**
       *Proficient answer:* instruction tuning fine-tunes models on prompt–response pairs covering diverse tasks, improving zero-shot instruction following. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare reasoning models with model routing using quality, cost, latency, and risk.**
       *Proficient answer:* reasoning models allocate extra inference compute—long chains, self-checks—for math, code, and planning tasks; model routing directs requests to appropriate models by task, risk, cost, or latency policy. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after reasoning models; authorization before any side effect or retrieval of restricted data; observability at the transition model families and selection introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Select models as replaceable components against requirements, not by reputation.

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

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
