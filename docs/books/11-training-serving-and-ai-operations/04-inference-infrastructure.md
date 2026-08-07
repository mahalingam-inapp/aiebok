# 11.4 — Inference Infrastructure

*Book 11: Training, Serving, and AI Operations · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 2, 4, and 10
- Containers and APIs
- Performance measurement

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Connect accelerators, memory, quantization, model formats, servers, batching, streaming, caches, and speculative decoding.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why inference infrastructure matters using the chapter scenario, not abstract definitions alone.
- Trace how **GPUs** and **quantization** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to kv cache.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Inference performance is a queueing and memory problem as much as a model problem.

## Mental model

```mermaid
flowchart LR
  N0["Data"] --> N1["Adapt"]
  N1["Adapt"] --> N2["Serve"]
  N2["Serve"] --> N3["Trace"]
  N3["Trace"] --> N4["Canary or rollback"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **inference infrastructure** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### GPUs

GPUs accelerate matrix operations for training and inference; memory capacity limits model size and batch. See the [GPUs concept card](../../concepts/cards/gpus.md).

**Example:** 80GB GPU runs 70B quantized; 24GB fits 7B fine-tune with QLoRA.

**Evidence of understanding:** Profile GPU utilization and memory headroom during peak inference load.

### Quantization

Quantization reduces weight precision—INT8, INT4—to cut memory and increase throughput with small quality trade-offs. See the [Quantization concept card](../../concepts/cards/quantization.md).

**Example:** AWQ 4-bit model runs 2× faster with <1 point eval drop on some tasks.

**Evidence of understanding:** Benchmark task metric and tokens/sec for FP16 versus INT4 on production hardware.

### vLLM

vLLM is a high-throughput inference server using PagedAttention for efficient KV cache memory management. See the [vLLM concept card](../../concepts/cards/vllm.md).

**Example:** vLLM serves Llama-8B at higher concurrent requests than naive HuggingFace pipeline.

**Evidence of understanding:** Load-test vLLM versus baseline server at equal hardware; report throughput and p95 latency.

### Batching

Batching groups requests to amortize GPU kernel overhead, improving throughput at possible latency cost. Continuous batching in servers interleaves sequences of different lengths. See the [Batching concept card](../../concepts/cards/batching.md).

**Example:** Batch size 32 may double throughput versus batch 1 but increase p95 latency for short prompts.

**Evidence of understanding:** Load-test at concurrency 1, 8, and 32; report throughput and p95 latency.

### Kv Cache

The KV cache stores key and value tensors for prior tokens during autoregressive decoding, avoiding recomputation of the prefix. Memory grows linearly with context length. See the [Kv Cache concept card](../../concepts/cards/kv-cache.md).

**Example:** Streaming chat reuses cached states for system prompt and prior turns, cutting latency after the first token.

**Evidence of understanding:** Compare tokens-per-second with and without KV cache on a 2k-token prefix.

## Worked example

**Book scenario:** A service must route requests across models while controlling cost and retaining rollback.

**Situation:** Self-hosted inference must serve onboarding assistant peaks; latency spikes when concurrency jumps.

**Baseline:** Single-process model server batch size 1.

**Application:** Load-test at concurrency 1/4/8/16, measure tokens/sec and p95 latency, explore quantization trade-offs, estimate KV cache memory from context length distribution.

**Test cases:** (1) Normal: steady 4 concurrent. (2) Boundary: context exactly at cache limit. (3) Adversarial: all requests unique prefixes—cache useless.

**Measurement:** Throughput curve, p95 latency, GPU memory headroom, $/1M tokens.

**Design question:** At what concurrency does queueing dominate over compute?

## Chapter hook

Run this short snippet first to anchor **inference infrastructure** before the book-level sample:

```python
CHAPTER = "11.4"
print("chapter hook:", CHAPTER)
batch_sizes = [1, 4, 8]
for b in batch_sizes:
    throughput = b / (1 + 0.1 * (b - 1))
    print(f"batch={b} relative_throughput={throughput:.2f}")
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **GPUs** or **quantization** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/11-model-router.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/11-model-router.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Low-risk simple work routes to the cheaper model; high-risk work routes to the higher-quality model.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **GPUs** and **quantization**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Load-test a local model at several concurrency levels.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without gpus and record quality, latency, and failure cases.
2. **Mechanism:** Add quantization while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when inference infrastructure earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 11.4 — inference infrastructure:

1. Draft cases in `test_lab.py` or `specs/lab-1104.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 11.4](../../labs/1104-inference-infrastructure.md)


## Architecture lens

For a production design in **Training, Serving, and AI Operations**, make the following explicit for **inference infrastructure**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns gpus versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the vllm boundary expose? |
| **Evidence** | Which eval slices prove inference infrastructure meets requirements before and after each release? |
| **Security** | What untrusted data crosses the kv cache boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover gpus or quantization | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | inference infrastructure is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in kv cache without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream gpus behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Connect accelerators, memory, quantization, model formats, servers, batching, streaming, caches, and speculative decoding. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of inference infrastructure without explicit gpus.
- **Today:** Engineering teams implement inference infrastructure as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but kv cache and governance constraints will still require explicit design.
- **What survives:** Inference performance is a queueing and memory problem as much as a model problem.

## Knowledge check

1. Why is inference a queueing and memory problem?
2. When does KV cache stop helping?
3. What infra baseline ignores batching?

??? question "Answer guidance"
    Q1: Requests wait in queues; memory bounds batch and context. Q2: Unique prefixes every request—no reuse. Q3: Serial single-request server at scale.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain GPUs without jargon and give a counterexample.**
       *Proficient answer:* gpus accelerate matrix operations for training and inference; memory capacity limits model size and batch. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare quantization with KV cache using quality, cost, latency, and risk.**
       *Proficient answer:* quantization reduces weight precision—int8, int4—to cut memory and increase throughput with small quality trade-offs; the kv cache stores key and value tensors for prior tokens during autoregressive decoding, avoiding recomputation of the prefix. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after quantization; authorization before any side effect or retrieval of restricted data; observability at the transition inference infrastructure introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Inference performance is a queueing and memory problem as much as a model problem.

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
