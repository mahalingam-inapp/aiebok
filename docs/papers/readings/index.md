# Research Readings Catalog

50 primary-source summaries.

Expand a theme or use search (`/`) for a specific paper.

??? abstract "Alignment & safety (8)"
    | Paper | Authors | Year | Summary |
    | --- | --- | --- | --- |
    | [Learning to Summarize from Human Feedback](rlhf-preference.md) | Stiennon et al. | 2020 | Early large-scale RLHF for summarization quality. |
    | [Constitutional AI: Harmlessness from AI Feedback](constitutional-ai.md) | Bai et al. | 2022 | Principle-guided critique and revision for safer assistants. |
    | [Training Language Models to Follow Instructions](instructgpt.md) | Ouyang et al. | 2022 | RLHF aligns models to human preferences on instruction following. |
    | [Training a Helpful and Harmless Assistant](helpful-harmless.md) | Bai et al. | 2022 | Preference modeling balances helpfulness and harmlessness. |
    | [Direct Preference Optimization](dpo.md) | Rafailov et al. | 2023 | Optimize preferences without explicit reward modeling. |
    | [Self-Instruct: Aligning Language Models with Self-Generated Instructions](self-instruct.md) | Wang et al. | 2023 | Bootstrap instruction data from a seed set. |
    | [OWASP Top 10 for LLM Applications](jailbreak-taxonomy.md) | OWASP | 2024 | Taxonomy of LLM application risks including injection. |
    | [Survey of Attacks and Defenses in LLM Security (representative)](jailbreak-survey.md) | Various | 2024 | Catalog of prompt injection and tool abuse patterns. |

??? abstract "Foundations & architecture (9)"
    | Paper | Authors | Year | Summary |
    | --- | --- | --- | --- |
    | [Efficient Estimation of Word Representations in Vector Space](word2vec.md) | Mikolov et al. | 2013 | Introduced skip-gram and CBOW dense word vectors learned from co-occurrence. |
    | [Sequence to Sequence Learning with Neural Networks](seq2seq.md) | Sutskever et al. | 2014 | Encoder–decoder LSTM architecture for variable-length input/output mapping. |
    | [Distilling the Knowledge in a Neural Network](knowledge-distillation.md) | Hinton et al. | 2015 | Train smaller students to mimic teacher soft targets. |
    | [Neural Machine Translation by Jointly Learning to Align and Translate](attention-paper.md) | Bahdanau et al. | 2015 | Additive attention let decoders focus on relevant encoder states. |
    | [Attention Is All You Need](transformer.md) | Vaswani et al. | 2017 | Self-attention transformer replaced recurrence for sequence modeling. |
    | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](moe.md) | Shazeer et al. | 2017 | Conditional computation activates subsets of experts per token. |
    | [Deep contextualized word representations (ELMo)](elmo.md) | Peters et al. | 2018 | Contextual embeddings from biLM layers improve downstream NLP. |
    | [BERT: Pre-training of Deep Bidirectional Transformers](bert.md) | Devlin et al. | 2019 | Masked language modeling plus next-sentence prediction for bidirectional context. |
    | [Knowledge Neurons in Pretrained Transformers](knowledge-neurons.md) | Dai et al. | 2022 | Localized parameters correlate with factual recall. |

??? abstract "RAG, tools & agents (9)"
    | Paper | Authors | Year | Summary |
    | --- | --- | --- | --- |
    | [Dense Passage Retrieval for Open-Domain QA](dpr.md) | Karpukhin et al. | 2020 | Dual-encoder dense retrieval competitive with BM25 on open QA. |
    | [Retrieval-Augmented Generation for Knowledge-Intensive NLP](rag.md) | Lewis et al. | 2020 | Retrieve documents at generation time to ground outputs. |
    | [RAGAS: Automated Evaluation of Retrieval Augmented Generation](ragas.md) | Es et al. | 2023 | Faithfulness and context precision metrics for RAG pipelines. |
    | [ReAct: Synergizing Reasoning and Acting](react.md) | Yao et al. | 2023 | Interleave chain-of-thought with tool actions and observations. |
    | [Toolformer: Language Models Can Teach Themselves to Use Tools](toolformer.md) | Schick et al. | 2023 | Self-supervised API call insertion during pretraining. |
    | [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](graph-rag.md) | Edge et al. | 2024 | Graph structure over corpus supports global summarization queries. |
    | [Model Context Protocol Specification](mcp-spec.md) | Anthropic | 2024 | Standard for tools, resources, and prompts between clients and servers. |
    | [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](swebench.md) | Jimenez et al. | 2024 | Repository-level coding agent benchmark with tests. |
    | [WebArena: A Realistic Web Environment for Agents](agent-benchmark-webarena.md) | Zhou et al. | 2024 | Benchmark for autonomous web agents on realistic tasks. |

??? abstract "Scale, open models & efficiency (15)"
    | Paper | Authors | Year | Summary |
    | --- | --- | --- | --- |
    | [Language Models are Unsupervised Multitask Learners](gpt2.md) | Radford et al. | 2019 | Decoder-only LM scales to strong zero-shot behavior. |
    | [Exploring the Limits of Transfer Learning](t5.md) | Raffel et al. | 2020 | Text-to-text framework unifies NLP tasks under one seq2seq objective. |
    | [Language Models are Few-Shot Learners](gpt3.md) | Brown et al. | 2020 | Scale and in-context examples enable task behavior without fine-tuning. |
    | [Scaling Laws for Neural Language Models](scaling-laws.md) | Kaplan et al. | 2020 | Loss scales predictably with compute, parameters, and data. |
    | [RoFormer: Enhanced Transformer with Rotary Position Embedding](rope.md) | Su et al. | 2021 | Rotary embeddings encode relative position in attention. |
    | [PaLM: Scaling Language Modeling with Pathways](palm.md) | Chowdhery et al. | 2022 | Large-scale training with pathways and sparse MoE elements. |
    | [Training Compute-Optimal Large Language Models](chinchilla.md) | Hoffmann et al. | 2022 | Optimal training balances model size and token count. |
    | [GQA: Training Generalized Multi-Query Transformer Models](gqa.md) | Ainslie et al. | 2023 | Grouped-query attention reduces KV cache footprint. |
    | [LLaMA: Open and Efficient Foundation Language Models](llama.md) | Touvron et al. | 2023 | High-quality open-weights models trained on public data mixtures. |
    | [Mistral 7B](mistral.md) | Jiang et al. | 2023 | Efficient open model with sliding-window attention. |
    | [Orca: Progressive Learning from Complex Explanation Traces](orca.md) | Mukherjee et al. | 2023 | Distill reasoning traces from stronger teachers. |
    | [Towards Monosemanticity (Sparse Autoencoders)](sparse-autoencoder.md) | Anthropic | 2023 | Sparse autoencoders extract interpretable features. |
    | [Mixtral of Experts](mixtral.md) | Jiang et al. | 2024 | Sparse MoE open model with strong quality/FLOP. |
    | [Nemotron family technical report](nemotron.md) | NVIDIA | 2024 | Documented training and alignment pipeline for Nemotron models. |
    | [OLMo: Accelerating the Science of Language Models](olmo.md) | Groeneveld et al. | 2024 | Fully open pipeline for reproducible LM research. |

??? abstract "Training, inference & reasoning (9)"
    | Paper | Authors | Year | Summary |
    | --- | --- | --- | --- |
    | [Learning Transferable Visual Models From Natural Language Supervision](clip.md) | Radford et al. | 2021 | Contrastive image–text pretraining enables zero-shot vision tasks. |
    | [LoRA: Low-Rank Adaptation of Large Language Models](lora.md) | Hu et al. | 2021 | Train low-rank adapters while freezing base weights. |
    | [Chain-of-Thought Prompting Elicits Reasoning](chain-of-thought.md) | Wei et al. | 2022 | Few-shot reasoning exemplars improve multi-step task performance. |
    | [FlashAttention: Fast and Memory-Efficient Exact Attention](flash-attention.md) | Dao et al. | 2022 | IO-aware attention algorithm reduces memory and speeds training/inference. |
    | [Robust Speech Recognition via Large-Scale Weak Supervision](whisper.md) | Radford et al. | 2022 | Multilingual ASR from weakly labeled audio at scale. |
    | [Fast Inference from Transformers via Speculative Decoding](speculative-decoding.md) | Leviathan et al. | 2023 | Draft model proposes tokens; target model verifies in parallel. |
    | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](mamba.md) | Gu & Dao | 2023 | Selective SSMs offer recurrent-like efficiency with strong quality. |
    | [QLoRA: Efficient Finetuning of Quantized LLMs](qlora.md) | Dettmers et al. | 2023 | 4-bit base model plus LoRA enables accessible fine-tuning. |
    | [Tree of Thoughts: Deliberate Problem Solving with LLMs](tree-of-thoughts.md) | Yao et al. | 2023 | Search over intermediate reasoning states improves hard tasks. |

