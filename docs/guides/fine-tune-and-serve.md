# Fine-Tune and Serve a Small Model

## Goal

LoRA adaptation with eval, registry, and rollback.

## Overview

Adapt a small open-weight model with LoRA, evaluate against a baseline, register the artifact, and serve it behind a versioned endpoint with rollback. Data cards and eval reports make the adaptation auditable.

## Architecture

Training reads a versioned dataset with a data card describing provenance and limitations. LoRA adapters train against a frozen base; checkpoints register in a local model registry. Eval compares adapter vs base on task-specific metrics. Serving loads base plus adapter with health checks and a rollback pointer to the prior version.

## Prerequisites

Complete the matching [guided book](../books/11-training-serving-and-ai-operations/index.md) and related labs.

## Build phases

### 1. Data card

**Goal:** Document dataset provenance, composition, and known biases.

**Steps:**
   - Record sources, collection method, PII handling, and license.
   - Summarize label distribution and known gaps.
   - Version dataset with checksum; link to training config.
   - Add acceptance checklist: consent, deduplication, held-out test split.

**Acceptance:**
   - Data card complete for all fields required by team template.
   - Dataset checksum matches manifest referenced in training config.
   - Held-out test split never used in training runs.

   **Commands:**

   ```bash
   python data/build_card.py --dataset data/train.jsonl --out data/DATA_CARD.md
   python data/verify_split.py --train data/train.jsonl --test data/test.jsonl
   ```
### 2. LoRA train

**Goal:** Train a low-rank adapter on the frozen base model.

**Steps:**
   - Configure LoRA rank, target modules, learning rate, and epochs.
   - Train on local GPU or CPU with reduced batch for smoke runs.
   - Save adapter weights and training log with git sha and data version.
   - Run smoke inference on three prompts before eval.

**Acceptance:**
   - Training reproducible from config file and pinned base model hash.
   - Adapter size small relative to base; loads independently.
   - Smoke inference produces coherent output on task-specific prompts.

   **Commands:**

   ```bash
   python train/lora.py --config configs/lora.yaml --out artifacts/adapter-v1
   python infer/smoke.py --base models/tiny-llm --adapter artifacts/adapter-v1
   ```
### 3. Eval report

**Goal:** Demonstrate adapter improvement over base without regressions.

**Steps:**
   - Run held-out test set through base and adapter.
   - Compute task metrics and slice breakdowns.
   - Check for catastrophic forgetting on general prompts.
   - Write eval report JSON and human-readable summary.

**Acceptance:**
   - Adapter beats base on primary metric by pre-defined margin.
   - No slice regresses more than agreed tolerance vs base.
   - Report archived with adapter version and dataset checksum.

   **Commands:**

   ```bash
   python eval/compare_models.py --base models/tiny-llm --adapter artifacts/adapter-v1 --test data/test.jsonl
   python eval/report.py --results results/compare.json --out reports/lora_eval.md
   ```
### 4. Serving endpoint

**Goal:** Serve adapter behind a versioned API with rollback.

**Steps:**
   - Implement loader that composes base model plus LoRA adapter.
   - Expose /v1/complete with model version header and health check.
   - Register version in local registry; keep previous version for rollback.
   - Document deploy, warm-up, and rollback commands.

**Acceptance:**
   - Health check passes; version endpoint returns active adapter id.
   - Rollback switches version in under one minute without rebuild.
   - Requests log model version and latency for monitoring.

   **Commands:**

   ```bash
   python serve/app.py --base models/tiny-llm --adapter artifacts/adapter-v1 --port 8080
   curl -s localhost:8080/health | python -m json.tool
   python serve/rollback.py --to adapter-v0
   ```

## Troubleshooting

- Adapter overfits: reduce epochs, increase dropout, or expand training diversity.
- Serving OOM: merge adapter for inference or quantize base; reduce concurrent requests.
- Eval gain not visible live: confirm serving loads correct adapter version and prompt matches eval.
- Data leakage: audit train/test splits for duplicate inputs and near-duplicates.

## Related patterns

- [Data Card Gate](../patterns/data-card-gate.md)
- [Feature Flag Model](../patterns/feature-flag-model.md)
- [Fallback Cascade](../patterns/fallback-cascade.md)
- [Eval Gated Release](../patterns/eval-gated-release.md)

## Related labs

- [1102 Post Training Methods](../labs/1102-post-training-methods.md)
- [1103 Dataset Engineering](../labs/1103-dataset-engineering.md)
- [1104 Inference Infrastructure](../labs/1104-inference-infrastructure.md)
- [1105 Deployment And Routing](../labs/1105-deployment-and-routing.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
