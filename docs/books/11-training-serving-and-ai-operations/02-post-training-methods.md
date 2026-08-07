# 11.2 — Post-Training Methods

*Book 11: Training, Serving, and AI Operations · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 2, 4, and 10
- Containers and APIs
- Performance measurement

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Understand supervised fine-tuning, LoRA, QLoRA, preference data, RLHF, DPO, distillation, and model merging.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why post-training methods matters using the chapter scenario, not abstract definitions alone.
- Trace how **SFT** and **LoRA** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to distillation.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Adaptation trades generality and operational simplicity for targeted behavior.

## Mental model

```mermaid
flowchart LR
  N0["Data"] --> N1["Adapt"]
  N1["Adapt"] --> N2["Serve"]
  N2["Serve"] --> N3["Trace"]
  N3["Trace"] --> N4["Canary or rollback"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **post-training methods** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### SFT

Supervised fine-tuning trains on input–output pairs to imitate desired behaviors on similar tasks. See the [SFT concept card](../../concepts/cards/sft.md).

**Example:** SFT on 5k support replies teaches consistent empathy and escalation triggers.

**Evidence of understanding:** Compare SFT model to base plus prompt on held-out behavioral eval.

### LoRA

LoRA fine-tunes low-rank adapter matrices in attention layers, reducing trainable parameters versus full fine-tuning. See the [LoRA concept card](../../concepts/cards/lora.md).

**Example:** 7B model with LoRA learns domain tone on one GPU while base weights stay frozen.

**Evidence of understanding:** Report eval uplift, training cost, and adapter version at inference.

### QLoRA

QLoRA combines quantization of base weights with LoRA adapters for fine-tuning on consumer GPUs. See the [QLoRA concept card](../../concepts/cards/qlora.md).

**Example:** Fine-tune 13B on single 24GB card using 4-bit base plus LoRA adapters.

**Evidence of understanding:** Document quantization config and compare quality versus full-precision LoRA baseline.

### DPO

Direct Preference Optimization aligns models from pairwise preferences without explicit reward model training. See the [DPO concept card](../../concepts/cards/dpo.md).

**Example:** Prefer concise accurate answers over verbose wrong ones via DPO preference pairs.

**Evidence of understanding:** Win-rate versus base model on preference eval set ≥ target before deploy.

### Distillation

Distillation trains smaller student models to mimic larger teachers, trading capability for cost and speed. See the [Distillation concept card](../../concepts/cards/distillation.md).

**Example:** Student classifier matches teacher on 95% of eval at 5× lower latency.

**Evidence of understanding:** Measure student versus teacher gap on full eval and acceptable degradation threshold.

## Worked example

**Book scenario:** A service must route requests across models while controlling cost and retaining rollback.

**Situation:** Support assistant needs tighter adherence to escalation phrasing; base instruct model drifts on edge cases.

**Baseline:** Longer prompts only—context cost rises, drift remains.

**Application:** LoRA fine-tune on curated escalation dialogs, compare SFT vs DPO if preference data exists, evaluate held-out behavioral cases, document merge/deploy plan.

**Test cases:** (1) Normal: standard escalation wording. (2) Boundary: rare dual-escalation case. (3) Adversarial: overfitting to training templates hurts novel incidents.

**Measurement:** Behavioral eval pass rate, general capability regression suite, training GPU cost.

**Design question:** How much general capability regression is acceptable for a 5-point slice gain?

## Chapter hook

Run this short snippet first to anchor **post-training methods** before the book-level sample:

```python
CHAPTER = "11.2"
print("chapter hook:", CHAPTER)
methods = {"prompt": 0.82, "SFT": 0.91, "DPO": 0.93}
cost = {"prompt": 1, "SFT": 4, "DPO": 6}
target = 0.90
choice = min((m for m, s in methods.items() if s >= target), key=lambda m: cost[m])
print({"method": choice, "score": methods[choice]})
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **SFT** or **LoRA** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/11-model-router.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/11-model-router.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Low-risk simple work routes to the cheaper model; high-risk work routes to the higher-quality model.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **SFT** and **LoRA**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Fine-tune a small model and evaluate held-out behavior.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without sft and record quality, latency, and failure cases.
2. **Mechanism:** Add lora while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when post-training methods earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 11.2 — post-training methods:

1. Draft cases in `test_lab.py` or `specs/lab-1102.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 11.2](../../labs/1102-post-training-methods.md)


## Architecture lens

For a production design in **Training, Serving, and AI Operations**, make the following explicit for **post-training methods**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns sft versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the qlora boundary expose? |
| **Evidence** | Which eval slices prove post-training methods meets requirements before and after each release? |
| **Security** | What untrusted data crosses the distillation boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover sft or lora | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | post-training methods is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in distillation without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream sft behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Understand supervised fine-tuning, LoRA, QLoRA, preference data, RLHF, DPO, distillation, and model merging. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of post-training methods without explicit sft.
- **Today:** Engineering teams implement post-training methods as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but distillation and governance constraints will still require explicit design.
- **What survives:** Adaptation trades generality and operational simplicity for targeted behavior.

## Knowledge check

1. What trade does adaptation make against generality?
2. When prefer DPO over SFT?
3. What post-training baseline is prompt-only?

??? question "Answer guidance"
    Q1: Targeted behavior vs broader capability and ops complexity. Q2: Clear preference pairs on style/safety judgments. Q3: Zero-shot instruct with no weight updates.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain SFT without jargon and give a counterexample.**
       *Proficient answer:* supervised fine-tuning trains on input–output pairs to imitate desired behaviors on similar tasks. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare LoRA with distillation using quality, cost, latency, and risk.**
       *Proficient answer:* lora fine-tunes low-rank adapter matrices in attention layers, reducing trainable parameters versus full fine-tuning; distillation trains smaller student models to mimic larger teachers, trading capability for cost and speed. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after lora; authorization before any side effect or retrieval of restricted data; observability at the transition post-training methods introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Adaptation trades generality and operational simplicity for targeted behavior.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Hu et al. — LoRA
- Ouyang et al. — InstructGPT
- Official inference-server documentation

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
