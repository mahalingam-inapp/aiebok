# 11.3 — Dataset Engineering

*Book 11: Training, Serving, and AI Operations · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 2, 4, and 10
- Containers and APIs
- Performance measurement

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Curate, label, deduplicate, filter, balance, version, document, and protect training and evaluation data.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why dataset engineering matters using the chapter scenario, not abstract definitions alone.
- Trace how **data curation** and **synthetic data** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to data cards.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Data design is model behavior design.

## Mental model

```mermaid
flowchart LR
  N0["Data"] --> N1["Adapt"]
  N1["Adapt"] --> N2["Serve"]
  N2["Serve"] --> N3["Trace"]
  N3["Trace"] --> N4["Canary or rollback"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **dataset engineering** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Data Curation

Data curation selects, cleans, and balances training examples for quality over quantity. Garbage data teaches garbage behavior. See the [Data Curation concept card](../../concepts/cards/data-curation.md).

**Example:** Removing toxic and duplicate examples improves fine-tune safety more than doubling raw size.

**Evidence of understanding:** Document inclusion rules and manual audit sample of 100 rows pre-training.

### Synthetic Data

Synthetic data generates training examples via models or rules—useful when real data is scarce but risks model collapse if overused. See the [Synthetic Data concept card](../../concepts/cards/synthetic-data.md).

**Example:** GPT generates varied phrasings of intent labels to augment small classifier set.

**Evidence of understanding:** Compare fine-tune with synthetic augmentation versus real-only on held-out real eval.

### Deduplication

Deduplication removes near-duplicate training examples that inflate metrics and memorization. See the [Deduplication concept card](../../concepts/cards/deduplication.md).

**Example:** Duplicate FAQ pairs in SFT data cause verbatim regurgitation in deployment.

**Evidence of understanding:** Report duplicate rate before/after MinHash dedup on training corpus.

### Contamination

Contamination occurs when eval examples leak into training data, inflating benchmark scores. See the [Contamination concept card](../../concepts/cards/contamination.md).

**Example:** Near-duplicate test questions in fine-tune set invalidate held-out claims.

**Evidence of understanding:** Run n-gram or embedding overlap check between train and eval; zero high overlap pairs.

### Data Cards

Data cards document dataset sources, collection, demographics, limitations, and recommended uses—parallel to model cards. See the [Data Cards concept card](../../concepts/cards/data-cards.md).

**Example:** Fine-tune data card lists languages, date range, PII handling, and opt-out process.

**Evidence of understanding:** Publish data card with every dataset version in registry.

## Worked example

**Book scenario:** A service must route requests across models while controlling cost and retaining rollback.

**Situation:** Fine-tune dataset assembled from historical chats; legal discovers eval tickets leaked into training.

**Baseline:** Dump all logs into JSONL without dedup or contamination checks.

**Application:** Curate splits, deduplicate near-duplicates, filter PII, version dataset, write data card, run contamination scan against eval sets, document synthetic augmentation choices.

**Test cases:** (1) Normal: clean curated set. (2) Boundary: synthetic examples labeled as such. (3) Adversarial: near-duplicate paraphrases of eval cases in train.

**Measurement:** Contamination hits (target zero), dedup ratio, label error rate on audit sample.

**Design question:** Which check catches eval leakage that random splitting misses?

## Chapter hook

Run this short snippet first to anchor **dataset engineering** before the book-level sample:

```python
CHAPTER = "11.3"
print("chapter hook:", CHAPTER)
train = {"case-101", "case-102", "case-103"}
eval = {"case-103", "case-200"}
leak = train & eval
print({"leaked_ids": sorted(leak)})
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **data curation** or **synthetic data** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/11-model-router.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/11-model-router.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Low-risk simple work routes to the cheaper model; high-risk work routes to the higher-quality model.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **data curation** and **synthetic data**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Create a data card and contamination check for a small dataset.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without data curation and record quality, latency, and failure cases.
2. **Mechanism:** Add synthetic data while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when dataset engineering earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 11.3 — dataset engineering:

1. Draft cases in `test_lab.py` or `specs/lab-1103.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 11.3](../../labs/1103-dataset-engineering.md)


## Architecture lens

For a production design in **Training, Serving, and AI Operations**, make the following explicit for **dataset engineering**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns data curation versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the deduplication boundary expose? |
| **Evidence** | Which eval slices prove dataset engineering meets requirements before and after each release? |
| **Security** | What untrusted data crosses the data cards boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover data curation or synthetic data | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | dataset engineering is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in data cards without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream data curation behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Curate, label, deduplicate, filter, balance, version, document, and protect training and evaluation data. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of dataset engineering without explicit data curation.
- **Today:** Engineering teams implement dataset engineering as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but data cards and governance constraints will still require explicit design.
- **What survives:** Data design is model behavior design.

## Knowledge check

1. Why is data design model behavior design?
2. How does deduplication affect generalization estimates?
3. What dataset baseline uses random split only?

??? question "Answer guidance"
    Q1: Labels, balance, and contamination define what model learns. Q2: Duplicates inflate train metrics vs honest generalization. Q3: Train/test split without near-dup or ID checks.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain data curation without jargon and give a counterexample.**
       *Proficient answer:* data curation selects, cleans, and balances training examples for quality over quantity. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare synthetic data with data cards using quality, cost, latency, and risk.**
       *Proficient answer:* synthetic data generates training examples via models or rules—useful when real data is scarce but risks model collapse if overused; data cards document dataset sources, collection, demographics, limitations, and recommended uses—parallel to model cards. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after synthetic data; authorization before any side effect or retrieval of restricted data; observability at the transition dataset engineering introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Data design is model behavior design.

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
