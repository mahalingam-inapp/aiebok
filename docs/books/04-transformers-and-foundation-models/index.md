# Book 4 — Transformers and Foundation Models

## Purpose

Understand the architecture, training, inference, and model families behind modern generative AI.

## Chapter learning path

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Sequence Models Before Transformers__

    Understand n-grams, recurrent networks, LSTMs, encoder–decoder models, bottlenecks, and why long-range depend…

    [Open chapter →](01-sequence-models-before-transformers.md)

-   :material-numeric-2-circle:{ .lg .middle } __Attention__

    Build attention from queries, keys, values, similarity scores, normalization, and weighted aggregation.

    [Open chapter →](02-attention.md)

-   :material-numeric-3-circle:{ .lg .middle } __The Transformer Block__

    Compose multi-head attention, feed-forward layers, residual paths, normalization, positional information, and…

    [Open chapter →](03-the-transformer-block.md)

-   :material-numeric-4-circle:{ .lg .middle } __Training Foundation Models__

    Study autoregressive, masked, and sequence-to-sequence objectives; data mixtures; scaling; checkpoints; and m…

    [Open chapter →](04-training-foundation-models.md)

-   :material-numeric-5-circle:{ .lg .middle } __Inference and Sampling__

    Trace logits, softmax, temperature, top-k, top-p, streaming, batching, KV cache, prefix cache, and speculativ…

    [Open chapter →](05-inference-and-sampling.md)

-   :material-numeric-6-circle:{ .lg .middle } __Model Families and Selection__

    Compare base, instruction, reasoning, code, embedding, reranking, reward, safety, speech, vision, and diffusi…

    [Open chapter →](06-model-families-and-selection.md)

</div>

## Entry prerequisites

- Books 1–3
- Matrix multiplication intuition
- Neural-network basics

## Book project

Implement a tiny transformer and create a vendor-neutral model selection report.

The project should include a short specification, runnable artifact or architecture, evaluation evidence, failure analysis, and at least one ADR. Prefer a small well-measured system over a large demo with unclear behavior.

## Suggested three-week schedule

- **Week 1:** Chapters 1–2, concept notes, and quick checks.
- **Week 2:** Chapters 3–4 and the runnable sample; begin the book project.
- **Week 3:** Chapters 5–6, failure analysis, project evaluation, and written reflection.

## Assessment

| Evidence | Weight |
|---|---:|
| Chapter knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Book project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Vaswani et al. — Attention Is All You Need
- Devlin et al. — BERT
- Brown et al. — Language Models are Few-Shot Learners

## Completion standard

You can explain the key mechanisms, complete the practice in every chapter, pass your own mastery review, and defend the project design against simpler alternatives.
