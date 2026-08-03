# BERT: Pre-training of Deep Bidirectional Transformers

## Citation

Devlin et al.. *BERT: Pre-training of Deep Bidirectional Transformers.* 2019. [https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)

## One-sentence contribution

Masked language modeling plus next-sentence prediction for bidirectional context.

## Problem

Left-to-right language models (GPT) could not use future context for understanding tasks. ELMo used bidirectional LSTMs but with shallow concatenation rather than deep joint contextualization. NLU needed deep bidirectional representations.

## Prior art

GPT-1 trained left-to-right LM on BooksCorpus. ELMo concatenated forward and backward LSTM hidden states. ULMFiT showed fine-tuning pre-trained LMs helps classification. OpenAI's Transformer LM was unidirectional by design.

## Core idea

Devlin et al. pre-trained a deep Transformer encoder with two objectives: Masked Language Modeling (MLM)—randomly mask 15% of tokens and predict them from bidirectional context; and Next Sentence Prediction (NSP)—classify whether two segments are consecutive. Fine-tuning adds a task-specific head on top of [CLS] or token outputs for classification, QA, or NER. The key insight is that MLM enables every layer to attend to both directions without the autoregressive constraint.

## Evidence

- GLUE benchmark: 80.5 average score, +7.0 points over prior best at release.
- SQuAD v1.1 F1: 93.2—surpassed human performance on the reading comprehension metric.
- Ablation: MLM >> left-to-right LM for fine-tuning; bidirectional context is the key driver.
- BERT-Large (340M params) consistently beat BERT-Base (110M) across tasks.

## Limitations

- MLM pre-training/inference mismatch—[MASK] tokens never appear at fine-tune time (partially addressed by RoBERTa removing NSP and improving masking).
- Not generative out of the box; text generation requires separate decoding strategies.
- NSP contribution was later shown to be minimal or harmful (RoBERTa ablation).
- Expensive pre-training (4 Cloud TPUs for 4 days on BERT-Large)—reproduction barrier.

## Lasting impact

BERT established the pre-train-then-fine-tune paradigm for NLU and spawned RoBERTa, ALBERT, DeBERTa, and domain-specific variants. Its MLM objective remains a standard encoder pre-training recipe.

## Reproduction exercise

Fine-tune `bert-base-uncased` on the AG News classification subset (4 classes, 120k train) for 3 epochs. Compare accuracy against a TF-IDF + logistic regression baseline. Expect >90% vs. ~85% baseline. Log training time and note the gap between pre-trained and random-init Transformer.

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)
- [06 Model Families And Selection](../../books/04-transformers-and-foundation-models/06-model-families-and-selection.md)
- [02 Supervised Learning](../../books/02-machine-learning-systems/02-supervised-learning.md)

## Related concepts

- [Pretraining Objectives](../../concepts/cards/pretraining-objectives.md)
- [Fine Tuning](../../concepts/cards/fine-tuning.md)
- [Generalization](../../concepts/cards/generalization.md)
