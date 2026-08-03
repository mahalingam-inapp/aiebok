"""Substantive reading summaries for the AIEBOK research paper catalog.

Imported by generate_maturity_content.py to enrich generated paper pages.
"""
from __future__ import annotations

from typing import TypedDict


class PaperDetail(TypedDict):
    problem: str
    prior_art: str
    core_idea: str
    evidence: list[str]
    limitations: list[str]
    impact: str
    reproduction: str
    related_chapters: list[str]
    related_concepts: list[str]


PAPER_DETAILS: dict[str, PaperDetail] = {
    "word2vec": {
        "problem": (
            "Classical NLP represented words as sparse one-hot vectors with no notion of semantic "
            "similarity—'cat' and 'dog' were as distant as 'cat' and 'finance.' The field needed "
            "dense, trainable word representations that capture distributional meaning from unlabeled text."
        ),
        "prior_art": (
            "Matrix factorization on co-occurrence counts (LSA, HAL) produced vectors but scaled poorly "
            "and treated all co-occurrences equally. Earlier neural language models (Collobert & Weston, "
            "word2vec predecessors) showed promise but trained too slowly for web-scale corpora."
        ),
        "core_idea": (
            "Mikolov et al. proposed two shallow architectures—CBOW predicts a word from surrounding "
            "context; skip-gram predicts context from a center word. Negative sampling replaces the "
            "full softmax with a small set of contrastive noise draws, making training tractable on "
            "billions of tokens. Hierarchical softmax offers an alternative speedup via a binary tree "
            "over the vocabulary. The result is a single dense vector per word type, learned entirely "
            "from local co-occurrence statistics without labeled data."
        ),
        "evidence": [
            "Semantic and syntactic word-analogy benchmark: skip-gram with negative sampling scored "
            "~70% on the Google analogy set (king−man+woman≈queen).",
            "Trained on Google News (~100B tokens); nearest-neighbor inspection shows coherent "
            "semantic clusters (countries, professions, verb tenses).",
            "Downstream NER and sentiment tasks improved when word2vec vectors replaced one-hot or "
            "random initialization.",
            "Skip-gram outperformed CBOW on rare words; CBOW was faster to train on frequent tokens.",
        ],
        "limitations": [
            "One vector per word type—polysemy ('bank' river vs. financial) is collapsed into a single point.",
            "No subword handling; out-of-vocabulary words require fallback to UNK or character models.",
            "Static embeddings do not adapt to sentence-level context (addressed later by ELMo, BERT).",
            "Training data bias (e.g., gender stereotypes in analogies) propagates directly into geometry.",
        ],
        "impact": (
            "word2vec made distributional semantics practical at scale and became the default "
            "initialization for neural NLP through 2016–2018. The skip-gram + negative sampling "
            "recipe survives in modern embedding APIs and as a pedagogical baseline for representation learning."
        ),
        "reproduction": (
            "Download a 100 MB Wikipedia dump, tokenize, and train skip-gram (vector size 300, window 5, "
            "5 negative samples) using Gensim or fastText. Evaluate on a 50-item analogy subset "
            "(capital cities, gender pairs). Compare against random vectors to confirm the geometry "
            "is non-trivial. Budget: one CPU hour."
        ),
        "related_chapters": [
            "../books/03-language-and-representation/04-from-sparse-features-to-embeddings.md",
            "../books/03-language-and-representation/05-similarity-and-vector-search.md",
            "../books/02-machine-learning-systems/03-unsupervised-and-representation-learning.md",
        ],
        "related_concepts": ["word-embeddings", "representation-learning", "n-grams"],
    },
    "seq2seq": {
        "problem": (
            "Mapping variable-length input sequences to variable-length outputs—machine translation, "
            "summarization, dialogue—required models that could read an entire source and generate "
            "a target of different length token by token."
        ),
        "prior_art": (
            "Phrase-based statistical MT (Koehn et al.) dominated with hand-engineered features and "
            "separate language/translation models. Earlier neural attempts used fixed-size windows "
            "or bag-of-words encodings that could not preserve word order or long dependencies."
        ),
        "core_idea": (
            "Sutskever et al. stacked two LSTMs: an encoder reads the input sequence and produces a "
            "fixed-size context vector from its final hidden state; a decoder LSTM generates the output "
            "sequence conditioned on that vector. Reversing the source sentence improved performance "
            "by placing words near the context boundary that align with early target tokens. Deep LSTMs "
            "(4 layers) with careful initialization and dropout regularization made the architecture "
            "trainable on large parallel corpora."
        ),
        "evidence": [
            "WMT'14 English→French: BLEU 34.8, beating the best statistical MT system (33.3) on the "
            "same data by a significant margin.",
            "Qualitative attention to the context vector showed the model learned meaningful "
            "source-target alignments without explicit alignment supervision.",
            "Ensemble of 5 models with beam search (width 2) and length normalization further "
            "improved results.",
            "Reversing input sequences alone contributed ~1–2 BLEU points—an unusually simple "
            "architectural trick with large effect.",
        ],
        "limitations": [
            "The fixed-size context vector is a bottleneck for long inputs; information from early "
            "encoder tokens is compressed and often lost.",
            "Sequential encoding/decoding prevents parallelization during training and inference.",
            "Exposure bias during training (teacher forcing) causes error accumulation at decode time.",
            "Required large parallel corpora; low-resource language pairs remained difficult.",
        ],
        "impact": (
            "Established the encoder–decoder template that attention and Transformers extended. "
            "Every modern NMT, summarization, and speech-to-text system traces lineage to this "
            "two-LSTM design."
        ),
        "reproduction": (
            "Train a 2-layer LSTM seq2seq on the small Multi30k German→English dataset (~30k pairs). "
            "Compare BLEU with and without source reversal. Use a single GPU for ~30 minutes. "
            "Inspect attention-free alignments by visualizing which encoder states the decoder "
            "hidden state is closest to at each step."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md",
            "../books/03-language-and-representation/01-why-language-is-hard.md",
            "../books/02-machine-learning-systems/04-neural-networks.md",
        ],
        "related_concepts": ["seq2seq", "lstms", "sampling"],
    },
    "attention-paper": {
        "problem": (
            "The seq2seq context vector bottleneck forced the decoder to reconstruct the entire source "
            "meaning from a single fixed-size vector, hurting translation quality on long sentences "
            "and making alignments opaque."
        ),
        "prior_art": (
            "Sutskever seq2seq used only the encoder's last hidden state. Earlier alignment models "
            "in statistical MT computed explicit source-target word alignments but were not "
            "differentiably integrated into neural decoders."
        ),
        "core_idea": (
            "Bahdanau et al. introduced additive (concat) attention: at each decode step the decoder "
            "computes an alignment score between its current state and every encoder hidden state, "
            "softmax-normalizes into weights, and forms a context vector as the weighted sum of "
            "encoder outputs. This lets the decoder focus on different source positions per target "
            "word—effectively learning a soft alignment. The attention context replaces the single "
            "fixed vector as the conditioning signal for each output token."
        ),
        "evidence": [
            "WMT'14 English→French: BLEU 28.45 (attention) vs. 26.75 (no attention) on the same "
            "architecture—roughly 6% relative gain from attention alone.",
            "Attention weight heatmaps visually match intuitive word alignments (e.g., English "
            "'zone' → French 'zone').",
            "Performance degradation on long sentences was substantially reduced compared to "
            "fixed-context seq2seq.",
            "Joint training of alignment and translation avoided the pipeline errors of statistical MT.",
        ],
        "limitations": [
            "Attention over all encoder states is O(n·m) in source and target length—expensive for "
            "very long documents.",
            "Still built on sequential RNNs; cannot parallelize encoder/decoder passes.",
            "Alignment weights are not guaranteed to be interpretable or sparse in all cases.",
            "Does not address the exposure bias or beam search approximation problems.",
        ],
        "impact": (
            "Attention became the standard conditioning mechanism for sequence models and the direct "
            "precursor to self-attention in Transformers. The idea that models should dynamically "
            "select relevant context per step is now universal in NLP and vision."
        ),
        "reproduction": (
            "Implement additive attention on top of a seq2seq baseline (same Multi30k setup). "
            "Plot attention heatmaps for 10 held-out sentence pairs. Measure BLEU delta with and "
            "without attention on sentences binned by source length (short vs. long). Expect the "
            "long-sentence bin to show the largest gain."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/02-attention.md",
            "../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md",
            "../books/03-language-and-representation/05-similarity-and-vector-search.md",
        ],
        "related_concepts": ["scaled-dot-product", "multi-head-attention", "seq2seq"],
    },
    "transformer": {
        "problem": (
            "Recurrent and convolutional sequence models process tokens sequentially, limiting "
            "training parallelization and making long-range dependency learning depend on many "
            "propagation steps through time."
        ),
        "prior_art": (
            "LSTM/GRU seq2seq with attention dominated NMT but required O(n) sequential steps. "
            "ConvS2S and ByteNet used convolutions for partial parallelization but still scaled "
            "path length with distance. No architecture had removed recurrence entirely while "
            "matching RNN quality."
        ),
        "core_idea": (
            "Vaswani et al. replaced recurrence with multi-head self-attention: each token attends "
            "to all others in the same layer, computing relevance via scaled dot-product scores. "
            "Positional encodings (sinusoidal or learned) inject order information since attention "
            "is permutation-invariant. Encoder and decoder stacks alternate self-attention, "
            "cross-attention (decoder→encoder), and position-wise feed-forward layers with residual "
            "connections and layer normalization. The design enables full parallelization over sequence "
            "length during training."
        ),
        "evidence": [
            "WMT'14 English→German: 28.4 BLEU—new state of the art, training in 3.5 days on 8 P100 GPUs "
            "vs. best published RNN results.",
            "English→French: 41.8 BLEU (single model, no ensemble)—large margin over prior work.",
            "Attention head analysis showed heads specialize (syntax, anaphora, positional).",
            "Training cost scaled better with sequence length than LSTM baselines due to parallelism.",
        ],
        "limitations": [
            "Self-attention memory and compute scale O(n²) with sequence length—prohibitive for "
            "very long documents without modifications.",
            "Positional encodings are weaker than explicit recurrence for some extrapolation tasks "
            "(length generalization).",
            "Requires large training data and careful warmup/regularization; small-data regimes "
            "favor pre-trained models over training from scratch.",
            "Cross-attention in the decoder still creates an encoder-decoder asymmetry that later "
            "decoder-only models (GPT) removed.",
        ],
        "impact": (
            "The Transformer became the universal backbone for language, vision, speech, and multimodal "
            "models. BERT, GPT, T5, ViT, and Whisper all inherit this block structure. 'Attention is "
            "all you need' accurately predicted a decade of architecture design."
        ),
        "reproduction": (
            "Implement a tiny Transformer (2 layers, 4 heads, d_model=128) on a copy task "
            "(reverse or duplicate sequences of length 10–20). Verify it converges where a bag-of-words "
            "baseline fails. Then fine-tune a HuggingFace 'tiny-random' Transformer on SST-2 sentiment "
            "to observe transfer from pre-trained weights vs. random init."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/03-the-transformer-block.md",
            "../books/04-transformers-and-foundation-models/02-attention.md",
            "../books/04-transformers-and-foundation-models/04-training-foundation-models.md",
        ],
        "related_concepts": ["multi-head-attention", "position", "residual-connections"],
    },
    "bert": {
        "problem": (
            "Left-to-right language models (GPT) could not use future context for understanding tasks. "
            "ELMo used bidirectional LSTMs but with shallow concatenation rather than deep joint "
            "contextualization. NLU needed deep bidirectional representations."
        ),
        "prior_art": (
            "GPT-1 trained left-to-right LM on BooksCorpus. ELMo concatenated forward and backward "
            "LSTM hidden states. ULMFiT showed fine-tuning pre-trained LMs helps classification. "
            "OpenAI's Transformer LM was unidirectional by design."
        ),
        "core_idea": (
            "Devlin et al. pre-trained a deep Transformer encoder with two objectives: Masked Language "
            "Modeling (MLM)—randomly mask 15% of tokens and predict them from bidirectional context; "
            "and Next Sentence Prediction (NSP)—classify whether two segments are consecutive. "
            "Fine-tuning adds a task-specific head on top of [CLS] or token outputs for classification, "
            "QA, or NER. The key insight is that MLM enables every layer to attend to both directions "
            "without the autoregressive constraint."
        ),
        "evidence": [
            "GLUE benchmark: 80.5 average score, +7.0 points over prior best at release.",
            "SQuAD v1.1 F1: 93.2—surpassed human performance on the reading comprehension metric.",
            "Ablation: MLM >> left-to-right LM for fine-tuning; bidirectional context is the key driver.",
            "BERT-Large (340M params) consistently beat BERT-Base (110M) across tasks.",
        ],
        "limitations": [
            "MLM pre-training/inference mismatch—[MASK] tokens never appear at fine-tune time "
            "(partially addressed by RoBERTa removing NSP and improving masking).",
            "Not generative out of the box; text generation requires separate decoding strategies.",
            "NSP contribution was later shown to be minimal or harmful (RoBERTa ablation).",
            "Expensive pre-training (4 Cloud TPUs for 4 days on BERT-Large)—reproduction barrier.",
        ],
        "impact": (
            "BERT established the pre-train-then-fine-tune paradigm for NLU and spawned RoBERTa, "
            "ALBERT, DeBERTa, and domain-specific variants. Its MLM objective remains a standard "
            "encoder pre-training recipe."
        ),
        "reproduction": (
            "Fine-tune `bert-base-uncased` on the AG News classification subset (4 classes, 120k train) "
            "for 3 epochs. Compare accuracy against a TF-IDF + logistic regression baseline. "
            "Expect >90% vs. ~85% baseline. Log training time and note the gap between pre-trained "
            "and random-init Transformer."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/04-training-foundation-models.md",
            "../books/04-transformers-and-foundation-models/06-model-families-and-selection.md",
            "../books/02-machine-learning-systems/02-supervised-learning.md",
        ],
        "related_concepts": ["pretraining-objectives", "fine-tuning", "generalization"],
    },
    "gpt3": {
        "problem": (
            "Task-specific fine-tuning required labeled datasets and separate model copies per task. "
            "Could a single large autoregressive model perform diverse tasks from natural language "
            "instructions and a few examples alone?"
        ),
        "prior_art": (
            "GPT-2 (1.5B) showed unsupervised LM pre-training produces some zero-shot ability. "
            "BERT required fine-tuning per task. T5 unified tasks as text-to-text but still needed "
            "fine-tuning. Prompt engineering on GPT-2 was anecdotal, not systematically evaluated."
        ),
        "core_idea": (
            "Brown et al. scaled the GPT architecture to 175B parameters trained on ~300B tokens "
            "and evaluated three regimes: zero-shot (task description only), one-shot (one example), "
            "and few-shot (several in-context examples prepended to the prompt). No gradient updates "
            " occur at inference—the model reads the prompt and continues generating. Scaling laws "
            "predicted that larger models would show sharper in-context learning curves, and the "
            "paper demonstrated this empirically across 10+ benchmarks."
        ),
        "evidence": [
            "Few-shot GPT-3 175B matched or exceeded fine-tuned BERT-Large on TriviaQA, COPA, and "
            "LAMBADA in some settings.",
            "Scaling from 125M to 175B showed smooth improvement in in-context learning ability—"
            "smaller models gained little from few-shot prompts.",
            "Human eval on news article generation: 175B rated more coherent than 13B.",
            "One-shot and few-shot consistently outperformed zero-shot, confirming examples matter.",
        ],
        "limitations": [
            "175B training cost (~$4.6M estimated) is not reproducible for most labs.",
            "In-context learning is inconsistent—prompt formatting, example order, and calibration "
            "swing results significantly.",
            "No built-in grounding, citation, or tool use; hallucination on factual queries.",
            "Few-shot performance still below dedicated fine-tuned models on many structured tasks.",
        ],
        "impact": (
            "GPT-3 shifted the field from fine-tuning to prompting and scaling, directly leading to "
            "ChatGPT, instruction tuning, and the current API-first AI product model. The in-context "
            "learning phenomenon remains an active research area."
        ),
        "reproduction": (
            "Using an API model (e.g., GPT-4o-mini), evaluate GSM8K with 0-shot vs. 5-shot CoT prompts. "
            "Fix the random seed for example selection and run 50 problems. Compare accuracy and "
            "token cost. Repeat with permuted example order to measure prompt sensitivity."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/05-inference-and-sampling.md",
            "../books/05-prompt-and-context-engineering/01-instructions-that-work.md",
            "../books/04-transformers-and-foundation-models/06-model-families-and-selection.md",
        ],
        "related_concepts": ["few-shot-examples", "prompting", "scaling-laws"],
    },
    "t5": {
        "problem": (
            "NLP tasks used incompatible formats—classification appended labels, QA extracted spans, "
            "MT used separate encoder-decoder heads. Transfer learning benefits were fragmented "
            "across task-specific architectures and loss functions."
        ),
        "prior_art": (
            "BERT used classification heads; GPT used continuation; BART used denoising autoencoder. "
            "Each required different fine-tuning code and evaluation harnesses. McCann et al.'s "
            "decaNLP attempted unification but with task-specific model modifications."
        ),
        "core_idea": (
            "Raffel et al. cast every NLP task as text-to-text: input and output are both strings "
            "(e.g., 'translate English to German: …' → German text; 'cola sentence: …' → 'acceptable'). "
            "Pre-training uses span corruption (replace random spans with sentinel tokens, predict "
            "corrupted spans)—a generalization of BERT's MLM suited to encoder-decoder. A single "
            "T5 model fine-tunes on any task by changing only the input/output string format, "
            "enabling systematic scaling studies across task, model size, and data."
        ),
        "evidence": [
            "SuperGLUE: T5-11B scored 89.3 average—state of the art at release with one framework.",
            "Systematic ablation across 50+ datasets in the 'C4' pre-training corpus study showed "
            "span corruption outperformed BERT-style MLM and language modeling for transfer.",
            "T5-11B matched or beat task-specific models on SQuAD, WMT, CNN/DailyMail summarization.",
            "Scaling from T5-Small (60M) to T5-11B showed predictable gains on held-out tasks.",
        ],
        "limitations": [
            "Text-to-text framing adds token overhead for simple tasks (binary classification as "
            "string generation is inefficient).",
            "C4 pre-training required significant compute; full reproduction is expensive.",
            "Encoder-decoder architecture is heavier at inference than decoder-only for generation tasks.",
            "Task prefix design affects performance—requires per-task prompt engineering at fine-tune time.",
        ],
        "impact": (
            "T5's text-to-text framework became the template for Flan-T5, UL2, and many multi-task "
            "models. The C4 dataset and systematic scaling methodology influenced open-data efforts "
            "and the design of instruction-tuning mixtures."
        ),
        "reproduction": (
            "Fine-tune `google/flan-t5-base` on 1000 SQuAD examples formatted as "
            "'question: … context: …' → answer span. Evaluate exact match on 200 held-out questions. "
            "Compare against extracting answer with a BERT QA head to see the text-to-text overhead."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/04-training-foundation-models.md",
            "../books/04-transformers-and-foundation-models/06-model-families-and-selection.md",
            "../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md",
        ],
        "related_concepts": ["pretraining-objectives", "fine-tuning", "seq2seq"],
    },
    "rag": {
        "problem": (
            "Parametric language models store knowledge in weights—they cannot cite sources, update "
            "facts without retraining, or reliably answer questions about niche or recent information. "
            "Pure generation hallucinates on knowledge-intensive tasks."
        ),
        "prior_art": (
            "kNN-LM (Khandelwal et al.) retrieved similar training sentences at inference. REALM "
            "jointly pre-trained retriever and LM but required expensive end-to-end training. "
            "Open-book QA systems pipelined retrieval and reading comprehension as separate stages "
            "without end-to-end differentiability."
        ),
        "core_idea": (
            "Lewis et al. combined a dense passage retriever (DPR-style dual encoder) with a "
            "BART seq2seq generator in a RAG-Sequence and RAG-Token variant. At inference, the "
            "retriever fetches top-k Wikipedia passages for the query; the generator conditions on "
            "these passages to produce the answer. The retriever and generator can be trained jointly "
            "with the generator loss providing a training signal to the retriever, or pre-trained "
            "components can be composed without joint training (RAG-Sequence treats retrieved docs "
            "as a single context; RAG-Token marginalizes over documents per token)."
        ),
        "evidence": [
            "Natural Questions: RAG-Token beat BART-Large and DPR+BERT pipeline on exact match and "
            "BLEU-style answer overlap.",
            "TriviaQA and WebQuestions: consistent gains over parametric-only BART baselines.",
            "Generated answers were more factual and specific—human eval preferred RAG outputs on "
            "Jeopardy-style questions.",
            "Ablation: retrieval mattered most on rare entities; parametric-only was competitive on "
            "common facts.",
        ],
        "limitations": [
            "Retriever and generator can be misaligned—retrieved passages may not contain the answer "
            "or may mislead the generator.",
            "Top-k retrieval adds latency (embedding search + reranking) at every query.",
            "No native citation mechanism—models may not attribute claims to specific passages.",
            "Wikipedia-only index limits domain-specific deployment without re-indexing.",
        ],
        "impact": (
            "RAG became the default architecture for enterprise Q&A, copilots, and grounded assistants. "
            "Every major cloud provider now ships a managed RAG stack tracing to this retrieve-then-generate pattern."
        ),
        "reproduction": (
            "Build a minimal RAG pipeline: chunk 50 pages of internal docs, embed with `sentence-transformers/all-MiniLM-L6-v2`, "
            "store in Chroma/FAISS, retrieve top-5 for 20 test questions, pass to an LLM with a "
            "'answer only from context' prompt. Measure answer correctness with and without retrieval "
            "on the same questions."
        ),
        "related_chapters": [
            "../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md",
            "../books/06-knowledge-and-retrieval-systems/03-retrieval.md",
            "../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md",
        ],
        "related_concepts": ["rag", "retrieval", "faithfulness"],
    },
    "dpr": {
        "problem": (
            "Open-domain QA requires retrieving relevant passages from millions of documents before "
            "answer extraction. BM25 lexical matching dominated but missed paraphrases and semantic "
            "equivalence ('LLM' vs. 'large language model')."
        ),
        "prior_art": (
            "BM25 and TF-IDF retrieval were fast and strong baselines. Earlier dense retrieval "
            "(ICT, ORQA) showed promise but required complex pre-training or did not match BM25 "
            "on standard benchmarks. Cross-encoder rerankers were accurate but too slow for first-stage retrieval."
        ),
        "core_idea": (
            "Karpukhin et al. trained two independent BERT encoders—one for questions, one for "
            "passages—mapping each to a dense vector. Retrieval is approximate nearest neighbor search "
            "in passage embedding space. Training uses in-batch negatives (other passages in the batch "
            "as distractors) plus hard negatives mined from BM25 top-k that the retriever currently "
            "ranks highly but are wrong. This contrastive setup is simpler than joint retriever-reader "
            "training and scales to Wikipedia-scale indexes."
        ),
        "evidence": [
            "Natural Questions (open-domain): top-20 passage retrieval accuracy 78.4% vs. BM25 59.1%.",
            "TriviaQA: top-20 accuracy 78.8% vs. BM25 66.8%.",
            "End-to-end QA (DPR + reader) beat ORQA and REALM on multiple benchmarks.",
            "Hard negative mining contributed ~7 points over in-batch negatives alone.",
        ],
        "limitations": [
            "Domain shift hurts—DPR fine-tuned on Wikipedia underperforms on biomedical or legal corpora without retraining.",
            "Dual encoders cannot model cross-attention between question and passage at retrieval time.",
            "Index staleness: new documents require re-embedding the entire corpus.",
            "Top-k selection is a hyperparameter; too few misses relevant docs, too many adds noise for the reader.",
        ],
        "impact": (
            "DPR established dual-encoder dense retrieval as the default first stage in RAG pipelines, "
            "replacing or augmenting BM25 in production search. Its training recipe is the foundation "
            "for embedding APIs and hybrid retrieval systems."
        ),
        "reproduction": (
            "Fine-tune `facebook/dpr-question_encoder-single-nq-base` on 1000 NQ question-passage pairs "
            "from the BEIR benchmark subset. Evaluate recall@10 against BM25 on the same queries. "
            "Then compare end-to-end answer F1 with a frozen reader (any LLM) using DPR vs. BM25 retrieval."
        ),
        "related_chapters": [
            "../books/06-knowledge-and-retrieval-systems/03-retrieval.md",
            "../books/06-knowledge-and-retrieval-systems/04-ranking-and-context-selection.md",
            "../books/03-language-and-representation/05-similarity-and-vector-search.md",
        ],
        "related_concepts": ["dense-retrieval", "bm25", "hybrid-search"],
    },
    "instructgpt": {
        "problem": (
            "Large LMs trained on internet text predict the next token, not what users actually want—they "
            "produce unhelpful, untruthful, or toxic outputs despite high fluency. Aligning model "
            "behavior to human intent required more than scale alone."
        ),
        "prior_art": (
            "GPT-3 could be prompted but was unreliable on instructions. Supervised fine-tuning (SFT) "
            "on demonstration data helped but did not scale and did not optimize for human preferences "
            "over multiple valid outputs. Earlier RLHF work (Christiano et al.) existed but not at LM scale."
        ),
        "core_idea": (
            "Ouyang et al. applied a three-stage pipeline: (1) SFT on human-written demonstrations "
            "for desired behavior; (2) train a reward model (RM) on human comparisons of model outputs—"
            "labelers rank which of several completions is better; (3) fine-tune the SFT model with PPO "
            "reinforcement learning, using the RM as the reward signal while constraining deviation "
            "from the SFT policy via a KL penalty. The RM captures preferences that are hard to specify "
            "as rules; PPO optimizes the policy toward higher reward."
        ),
        "evidence": [
            "1.3B InstructGPT preferred over 175B raw GPT-3 by human labelers on prompts—alignment "
            "beat scale.",
            "Truthfulness and harmlessness scores improved significantly vs. GPT-3 on held-out prompts.",
            "PPO + RM outperformed SFT alone and supervised fine-tuning on human-written completions.",
            "Labeler agreement with held-out researchers' preferences correlated with RM scores.",
        ],
        "limitations": [
            "Human labeling is expensive (~$600k+ for InstructGPT-scale data) and introduces labeler bias.",
            "PPO training is unstable—requires careful KL tuning, reward hacking monitoring.",
            "Reward model can be gamed (verbose, sycophantic outputs score well).",
            "Does not eliminate hallucination or jailbreaks—alignment is partial.",
        ],
        "impact": (
            "InstructGPT's RLHF pipeline became the template for ChatGPT, Claude, and virtually every "
            "aligned assistant. It shifted industry focus from raw LM benchmarks to human preference "
            "evaluation and safety metrics."
        ),
        "reproduction": (
            "Using TRL or a similar library, run SFT on 500 instruction-response pairs (Alpaca subset), "
            "then train a reward model on 200 preference pairs (chosen/rejected). Compare PPO-tuned vs. "
            "SFT-only outputs on 20 held-out prompts with a simple LLM-as-judge or human rating. "
            "Budget: single A100 for a few hours on a 1–3B model."
        ),
        "related_chapters": [
            "../books/11-training-serving-and-ai-operations/02-post-training-methods.md",
            "../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md",
            "../books/05-prompt-and-context-engineering/01-instructions-that-work.md",
        ],
        "related_concepts": ["sft", "instruction-tuning", "human-evaluation"],
    },
    "lora": {
        "problem": (
            "Full fine-tuning of multi-billion-parameter models requires storing optimizer states and "
            "gradients for every parameter—prohibitively expensive for most practitioners and "
            "deployment scenarios with many task-specific adapters."
        ),
        "prior_art": (
            "Adapters (Houlsby et al.) inserted small modules between layers. Prefix tuning prepended "
            "trainable tokens. BitFit updated only bias terms. All reduced trainable params but adapters "
            "added inference latency; prefix tuning limited context window."
        ),
        "core_idea": (
            "Hu et al. hypothesized that weight updates during fine-tuning have low intrinsic rank. "
            "Instead of updating the full weight matrix W, LoRA learns a low-rank decomposition "
            "ΔW = BA where B ∈ R^{d×r}, A ∈ R^{r×k}, with r << min(d,k). Only A and B are trained; "
            "base weights W stay frozen. At inference, ΔW can be merged into W (no latency overhead) "
            "or kept separate for hot-swapping adapters. Applied to attention projection matrices "
            "(W_q, W_k, W_v, W_o) in Transformer layers."
        ),
        "evidence": [
            "RoBERTa, DeBERTa, GPT-2: LoRA with r=4–8 matched full fine-tuning on GLUE, WikiSQL, "
            "SAMSum with <1% trainable parameters.",
            "GPT-3 175B: LoRA reduced trainable params by 10,000× vs. full fine-tuning with "
            "comparable MNLI and WikiSQL performance.",
            "No inference latency when merged; adapter swapping enables multi-tenant serving.",
            "Higher rank r improves quality but with diminishing returns beyond r=16 for most tasks.",
        ],
        "limitations": [
            "Rank r is a hyperparameter—too low underfits, too high approaches full fine-tuning cost.",
            "Not all tasks benefit equally; some complex reasoning tasks may need full fine-tune or higher rank.",
            "Merging adapters from different tasks is non-trivial (interference between LoRA matrices).",
            "Quantization + LoRA (QLoRA) adds compatibility constraints.",
        ],
        "impact": (
            "LoRA became the default parameter-efficient fine-tuning method, enabling the open-source "
            "fine-tuning ecosystem (Alpaca, thousands of HuggingFace adapters). Cloud providers offer "
            "LoRA training as a managed service."
        ),
        "reproduction": (
            "Fine-tune `mistral-7b` with LoRA (r=8, alpha=16) on 500 instruction pairs using PEFT library. "
            "Compare eval loss and task accuracy against full fine-tune on a 7B model if GPU memory allows, "
            "or against prompt-only baseline. Log trainable parameter count and peak GPU memory."
        ),
        "related_chapters": [
            "../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md",
            "../books/11-training-serving-and-ai-operations/02-post-training-methods.md",
            "../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md",
        ],
        "related_concepts": ["lora", "qlora", "fine-tuning"],
    },
    "react": {
        "problem": (
            "Chain-of-thought prompting improves reasoning but models cannot act on the world—look up "
            "facts, query databases, or execute code. Separate tool-use pipelines lacked unified "
            "reasoning traces that humans could inspect and debug."
        ),
        "prior_art": (
            "WebGPT used RL to train browsing. Toolformer self-supervised API calls during pretraining. "
            "CoT elicited reasoning but no actions. Traditional agents (ReAct predecessors) used "
            "separate planning and execution modules without language-model-native traces."
        ),
        "core_idea": (
            "Yao et al. interleaved three trace types in a single prompt trajectory: Thought "
            "(reasoning about the current state), Action (a tool call with structured input, e.g., "
            "Search[entity]), and Observation (the tool's returned result). The LM generates Thought "
            "and Action tokens; the environment (search engine, calculator, API) produces Observations "
            "appended to the context. This loop continues until the model emits a Final Answer. "
            "Few-shot exemplars of full Thought-Action-Observation trajectories teach the pattern "
            "without fine-tuning."
        ),
        "evidence": [
            "HotpotQA (multi-hop QA): ReAct outperformed CoT-only and action-only baselines on EM/F1.",
            "FEVER (fact verification): ReAct achieved higher label accuracy by retrieving evidence "
            "before committing to a verdict.",
            "AlfWorld (text-based embodied tasks): ReAct beat imitation learning and CoT on success rate.",
            "Human interpretability: trajectories were easier to debug than black-box tool pipelines.",
        ],
        "limitations": [
            "Prompt-fragile—small changes to exemplars or tool schemas degrade performance sharply.",
            "Error propagation: a bad early action poisons subsequent reasoning with wrong observations.",
            "No formal guarantees on tool use; models hallucinate actions or arguments.",
            "Latency scales with number of tool calls; each step requires a full LM forward pass.",
        ],
        "impact": (
            "ReAct established the Thought→Action→Observation loop used in LangChain, AutoGPT, "
            "and production agent frameworks. It bridged CoT reasoning and tool-augmented LLMs "
            "into a single inspectable trace format."
        ),
        "reproduction": (
            "Implement a 3-tool ReAct agent (calculator, Wikipedia search via API, final answer) "
            "on 20 HotpotQA questions using GPT-4o-mini. Compare accuracy against CoT-only (no tools). "
            "Log full trajectories and count how many failures come from wrong tool selection vs. "
            "wrong reasoning after correct retrieval."
        ),
        "related_chapters": [
            "../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md",
            "../books/08-agent-systems/02-the-agent-loop.md",
            "../books/07-reasoning-and-tool-use/02-planning.md",
        ],
        "related_concepts": ["plan-act-observe", "tool-schemas", "function-calling"],
    },
    "dpo": {
        "problem": (
            "RLHF requires training a separate reward model and running PPO—a complex, unstable "
            "pipeline with many hyperparameters. Simpler alignment methods that directly optimize "
            "preferences were needed for research reproducibility and production reliability."
        ),
        "prior_art": (
            "InstructGPT used SFT + RM + PPO. Earlier work optimized ranking losses but not at LM "
            "scale. SLiC and similar methods used contrastive losses but without the closed-form "
            "preference likelihood derivation."
        ),
        "core_idea": (
            "Rafailov et al. showed that the RLHF optimal policy has a closed-form solution under "
            "the Bradley-Terry preference model, yielding a simple classification loss: maximize "
            "log σ(β(log π_θ(y_w|x) - log π_θ(y_l|x))) where y_w and y_l are chosen/rejected "
            "responses and π_ref is the reference (SFT) policy implicit in the loss. DPO skips the "
            "reward model entirely—directly fine-tune the LM on preference pairs. β controls "
            "deviation from the reference policy (analogous to KL penalty in PPO)."
        ),
        "evidence": [
            "Sentiment control (IMDb): DPO matched PPO on human eval with simpler training.",
            "Summarization (Reddit TL;DR): DPO preferred over PPO and best-of-n baselines.",
            "Anthropic HH dialogue: DPO competitive with PPO on helpfulness/harmlessness.",
            "Training stability: DPO converged without PPO's reward hacking or KL collapse issues.",
        ],
        "limitations": [
            "Offline preferences only—cannot explore new responses during training like online RL.",
            "Distribution shift: policy moves away from reference, preferences may not generalize.",
            "β tuning is critical; wrong β causes overfitting to preferences or no learning.",
            "Does not handle multi-objective preferences or constraints as naturally as constrained RL.",
        ],
        "impact": (
            "DPO became the default alignment method for open-source models (Zephyr, Tulu, many "
            "HuggingFace models) due to simplicity and reproducibility. It largely replaced PPO "
            "in research settings."
        ),
        "reproduction": (
            "Run DPO on 200 preference pairs (Anthropic HH subset) with `mistral-7b-sft` using TRL. "
            "Compare win-rate against the SFT baseline on 30 held-out prompts using an LLM judge. "
            "Sweep β ∈ {0.1, 0.5, 1.0} and plot preference accuracy on a validation set."
        ),
        "related_chapters": [
            "../books/11-training-serving-and-ai-operations/02-post-training-methods.md",
            "../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md",
            "../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md",
        ],
        "related_concepts": ["dpo", "sft", "instruction-tuning"],
    },
    "chain-of-thought": {
        "problem": (
            "Large LMs fail multi-step reasoning tasks (arithmetic, commonsense, symbolic manipulation) "
            "when prompted to produce answers directly—even when individual steps are within capability."
        ),
        "prior_art": (
            "Standard few-shot prompting appended input→output pairs without intermediate steps. "
            "Scratchpad work (NYU, 2021) trained models to output reasoning traces but required "
            "fine-tuning. Program-aided methods used external solvers rather than LM-native reasoning."
        ),
        "core_idea": (
            "Wei et al. demonstrated that including few-shot exemplars with explicit intermediate "
            "reasoning steps ('Let's think step by step…') in the prompt causes LMs to generate "
            "similar step-by-step chains before the final answer. No fine-tuning required—purely "
            "an inference-time prompt change. The effect emerges primarily at sufficient scale "
            "(~100B+ parameters for robust CoT on GSM8K). CoT essentially elicits the model's "
            "latent multi-step computation by showing the desired output format."
        ),
        "evidence": [
            "GSM8K (math): PaLM 540B with CoT scored 57% vs. 18% with standard prompting.",
            "StrategyQA, Date Understanding, Sports Understanding: large gains on PaLM and Codex.",
            "CoT gains increase with model size—GPT-3 175B showed smaller CoT benefit than PaLM 540B.",
            "Self-consistency (sample multiple CoT paths, majority vote) further boosted GSM8K to 74%.",
        ],
        "limitations": [
            "Requires large models—CoT often hurts or adds no value for models <10B parameters.",
            "Exemplar selection and ordering significantly affect results; brittle in production.",
            "Generated reasoning can be plausible but wrong (unfaithful CoT)—steps don't always "
            "reflect actual computation.",
            "Increases output token count 3–5×, raising latency and cost.",
        ],
        "impact": (
            "CoT prompting became standard for reasoning tasks and a building block for ReAct, "
            "Tree of Thoughts, and test-time compute scaling. 'Let's think step by step' is now "
            "a default prompt engineering technique."
        ),
        "reproduction": (
            "Evaluate GPT-4o-mini on 50 GSM8K problems with direct prompting vs. 5-shot CoT "
            "exemplars. Measure accuracy and average output tokens. Add self-consistency (5 samples, "
            "majority vote) on 20 problems and compare cost-quality trade-off."
        ),
        "related_chapters": [
            "../books/07-reasoning-and-tool-use/01-reasoning-as-search.md",
            "../books/05-prompt-and-context-engineering/01-instructions-that-work.md",
            "../books/07-reasoning-and-tool-use/03-verification-and-critique.md",
        ],
        "related_concepts": ["few-shot-examples", "self-consistency", "test-time-compute"],
    },
    "scaling-laws": {
        "problem": (
            "Training large LMs is expensive; practitioners lacked principled guidance on how to "
            "allocate compute between model size, dataset size, and training duration to minimize loss."
        ),
        "prior_art": (
            "Empirical scaling in vision (Hestness et al.) showed power-law learning curves. "
            "Prior LM work (Kaplan's team at OpenAI, earlier) had scattered results without a "
            "unified framework. Ad hoc decisions dominated pretraining budgets."
        ),
        "core_idea": (
            "Kaplan et al. empirically measured language modeling loss across models spanning "
            "7 orders of magnitude in compute, finding smooth power-law relationships: "
            "L(N) ∝ N^{-α} for parameters, L(D) ∝ D^{-β} for dataset size, L(C) ∝ C^{-γ} for "
            "total compute. The exponents α, β, γ were fit from hundreds of training runs. "
            "Optimal allocation under a fixed compute budget favors scaling model size over data "
            "more aggressively than later Chinchilla work would suggest."
        ),
        "evidence": [
            "Loss curves were smooth power laws across 6+ orders of magnitude with no observed "
            "plateau—larger always helped within the tested range.",
            "Downstream task performance (e.g., HellaSwag) correlated with pretraining loss across scales.",
            "Optimal compute allocation formula predicted GPT-3 sizing reasonably well.",
            "Extrapolation from smaller runs predicted larger model loss within ~10% error.",
        ],
        "limitations": [
            "Chinchilla (2022) revised optimal token-to-parameter ratio—Kaplan favored larger models "
            "relative to data than is compute-optimal.",
            "Power laws are task-dependent; code and math may scale differently from general text.",
            "Does not account for data quality, architecture choices, or post-training effects.",
            "Extrapolation beyond measured range (to trillion-parameter models) is uncertain.",
        ],
        "impact": (
            "Scaling laws justified billion-dollar pretraining investments and shaped GPT-3/4, "
            "PaLM, and LLaMA sizing decisions. They remain the starting point for compute budgeting, "
            "even after Chinchilla refinements."
        ),
        "reproduction": (
            "Train 5 small GPT-2 variants (varying params 10M–400M) on the same OpenWebText subset "
            "for fixed token counts. Plot validation loss vs. parameters on log-log axes. Fit a "
            "power law and predict the 800M model's loss. Compare predicted vs. actual."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/04-training-foundation-models.md",
            "../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md",
            "../books/02-machine-learning-systems/05-evaluation-and-error-analysis.md",
        ],
        "related_concepts": ["scaling-laws", "training", "loss-functions"],
    },
    "chinchilla": {
        "problem": (
            "Kaplan scaling laws suggested allocating most compute to model size, leading to "
            "undertrained large models (e.g., Gopher 280B). The field needed revised guidance "
            "on the optimal balance between parameters and training tokens."
        ),
        "prior_art": (
            "Kaplan et al. (2020) scaling laws favored larger models. GPT-3, Gopher, and early "
            "LLaMA variants trained on fewer tokens per parameter than later models. Empirical "
            "evidence suggested some large models were compute-inefficient."
        ),
        "core_idea": (
            "Hoffmann et al. re-derived scaling laws with a corrected compute budget formulation "
            "and found that model size and training tokens should scale equally—roughly 20 tokens "
            "per parameter for compute-optimal training. They trained Chinchilla (70B params, "
            "1.4T tokens)—4× more data than Gopher (280B, 300B tokens)—and showed it outperformed "
            "Gopher on virtually every benchmark despite being 4× smaller. The key insight: most "
            "contemporary LMs were over-parameterized and under-trained."
        ),
        "evidence": [
            "Chinchilla 70B beat Gopher 280B on MMLU, HellaSwag, BigBench, and 15+ other benchmarks.",
            "Compute-optimal frontier: ~20 tokens/parameter across model sizes from 400M to 70B.",
            "Training smaller models on more data matched larger undertrained models at equal compute.",
            "Revised scaling exponents differed from Kaplan—equal scaling of N and D, not favoring N.",
        ],
        "limitations": [
            "Assumes fixed compute budget; inference cost favors smaller models even if training "
            "cost is equal.",
            "Data quality and mixture not modeled—20 tokens/parameter is an average, not universal.",
            "Does not address post-training (SFT, RLHF) compute allocation.",
            "Chinchilla weights were not released—impact is primarily on training recipes.",
        ],
        "impact": (
            "Chinchilla-optimal training became the standard for open models: LLaMA 2, Mistral, "
            "OLMo, and most post-2022 models train on ~20 tokens/parameter. It corrected a "
            "systematic inefficiency in the field's scaling strategy."
        ),
        "reproduction": (
            "Compare two training runs at equal FLOPs budget: (A) small model, many tokens vs. "
            "(B) large model, few tokens using nanoGPT or a similar framework. Evaluate perplexity "
            "on held-out text. Confirm that (A) matches or beats (B)—demonstrating the Chinchilla "
            "principle at small scale."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/04-training-foundation-models.md",
            "../books/11-training-serving-and-ai-operations/03-dataset-engineering.md",
            "../books/04-transformers-and-foundation-models/06-model-families-and-selection.md",
        ],
        "related_concepts": ["scaling-laws", "data-curation", "data-mixtures"],
    },
    "llama": {
        "problem": (
            "State-of-the-art LMs (GPT-3, PaLM, Chinchilla) were closed—weights unavailable, "
            "training data undisclosed. Researchers and engineers needed high-quality open models "
            "to reproduce, fine-tune, and deploy without API dependencies."
        ),
        "prior_art": (
            "GPT-3 and PaLM were API-only. OPT (Meta) and BLOOM (BigScience) released open weights "
            "but lagged closed models on quality. GPT-Neo/GPT-J were open but significantly weaker "
            "than frontier models."
        ),
        "core_idea": (
            "Touvron et al. trained decoder-only Transformers (7B–65B) on publicly available text "
            "only, using Chinchilla-optimal token counts and architectural choices tuned for "
            "inference efficiency (SwiGLU activations, rotary embeddings, pre-normalization). "
            "No proprietary data—training mixture curated from CommonCrawl, C4, GitHub, Wikipedia, "
            "Books, ArXiv, and Stack Exchange. Released weights under a research license, enabling "
            "the open fine-tuning ecosystem (Alpaca, Vicuna, thousands of derivatives)."
        ),
        "evidence": [
            "LLaMA-13B outperformed GPT-3 175B on most benchmarks despite 13× fewer parameters.",
            "LLaMA-65B competitive with Chinchilla 70B and PaLM 540B on MMLU, HellaSwag, BigBench.",
            "Inference efficiency: 7B model runnable on consumer hardware with quantization.",
            "Open release spawned 1000+ fine-tuned variants within months (Alpaca, Vicuna, WizardLM).",
        ],
        "limitations": [
            "Initial license restricted commercial use (relaxed in LLaMA 2).",
            "English-heavy training data; multilingual performance lags dedicated multilingual models.",
            "No alignment training in base LLaMA—requires SFT/RLHF for assistant use.",
            "Safety and toxicity not primary training objectives; base model can generate harmful content.",
        ],
        "impact": (
            "LLaMA catalyzed the open-weights revolution—local deployment, private fine-tuning, and "
            "research reproducibility at near-frontier quality. LLaMA 2/3 and derivatives (Mistral, "
            "Mixtral) continue this lineage."
        ),
        "reproduction": (
            "Download `meta-llama/Llama-3.2-1B` (or smallest available), run perplexity on a 1MB "
            "text sample, and compare against GPT-2-xl. Fine-tune with LoRA on 200 instruction pairs "
            "and evaluate on 20 held-out prompts vs. base model."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/06-model-families-and-selection.md",
            "../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md",
            "../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md",
        ],
        "related_concepts": ["open-weights", "quantization", "lora"],
    },
    "toolformer": {
        "problem": (
            "LMs cannot natively perform arithmetic, look up current facts, or call external APIs—they "
            "hallucinate calculations and stale information. Teaching tool use typically required "
            "expensive human annotation of API call demonstrations."
        ),
        "prior_art": (
            "ReAct and WebGPT used prompting or RL with human demonstrations. API-bank and similar "
            "datasets required manual curation. Fine-tuning on tool demonstrations was limited by "
            "dataset size and API coverage."
        ),
        "core_idea": (
            "Schick et al. proposed self-supervised tool learning: start with a few human-written "
            "API call examples, then have the LM generate candidate API calls on unlabeled text. "
            "Filter candidates by whether the API result reduces perplexity on subsequent tokens—"
            "keeping only calls that measurably help prediction. Iteratively expand the training "
            "set with self-generated examples. APIs (calculator, QA, search, translation, calendar) "
            "are invoked via special tokens inserted inline during text generation."
        ),
        "evidence": [
            "LM quality (perplexity) maintained while gaining tool-use capability—no degradation on "
            "standard LM benchmarks.",
            "Math QA (GSM8K subset): improved accuracy with calculator API vs. LM-only.",
            "Knowledge-intensive QA: search API reduced hallucination on date/entity questions.",
            "Self-supervised pipeline generated 1000s of training examples from ~12 human seeds.",
        ],
        "limitations": [
            "Limited to pre-defined API set—no dynamic tool discovery.",
            "Perplexity-based filtering is a proxy; some useful calls may be filtered out.",
            "Inference requires API execution infrastructure at each call site.",
            "Does not handle multi-step tool chains or error recovery robustly.",
        ],
        "impact": (
            "Toolformer demonstrated that tool use can be learned with minimal supervision, "
            "influencing function-calling fine-tuning in GPT-4, Claude, and open models. "
            "The self-supervised API learning pattern appears in modern agent training pipelines."
        ),
        "reproduction": (
            "Fine-tune a 1–3B model on 200 examples of inline calculator calls (question → "
            "Calculate[expr] → result → answer). Evaluate on 30 arithmetic word problems vs. "
            "base model. Measure accuracy and count hallucinated numbers in outputs."
        ),
        "related_chapters": [
            "../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md",
            "../books/08-agent-systems/02-the-agent-loop.md",
            "../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md",
        ],
        "related_concepts": ["function-calling", "tool-schemas", "tool-discovery"],
    },
    "constitutional-ai": {
        "problem": (
            "RLHF for harmlessness requires humans to label toxic/harmful outputs—a slow, expensive, "
            "and psychologically taxing process. Scaling safety alignment needed alternatives to "
            "human harm labels."
        ),
        "prior_art": (
            "InstructGPT/RLHF used human preference labels for helpfulness and harmlessness. "
            "Red-teaming collected adversarial prompts but reactively. Rule-based filters were "
            "brittle and over-blocked legitimate queries."
        ),
        "core_idea": (
            "Bai et al. introduced Constitutional AI (CAI): define a set of written principles "
            "(a 'constitution') and have the model self-critique its outputs against these principles, "
            "then revise to comply. The revised outputs become training data for RLAIF (RL from AI "
            "Feedback)—replacing human harm labels with AI-generated preference labels. "
            "Two phases: (1) supervised revision using critique→revision chains; (2) RLAIF "
            "preference training where AI compares revised vs. original outputs."
        ),
        "evidence": [
            "Helpful and harmless: CAI models matched RLHF on human eval with fewer human harm labels.",
            "RLAIF preferences correlated with human preferences on held-out harmlessness comparisons.",
            "Chain-of-thought critique improved revision quality over direct revision.",
            "Principle specificity mattered—vague principles produced inconsistent revisions.",
        ],
        "limitations": [
            "Principles can conflict (helpful vs. harmless tradeoffs require priority ordering).",
            "Models can game principles (sycophantic agreement, excessive hedging).",
            "AI feedback inherits model biases—errors in critique propagate to training.",
            "Does not address jailbreaks or adversarial inputs at inference time.",
        ],
        "impact": (
            "CAI/RLAIF became Anthropic's alignment methodology for Claude and influenced industry "
            "thinking on scalable safety. Principle-based alignment is now a standard alternative "
            "to pure human-label RLHF."
        ),
        "reproduction": (
            "Write 5 harmlessness principles. Prompt an LLM to critique 20 assistant responses "
            "against them, then revise. Compare original vs. revised on a toxicity classifier "
            "(e.g., Perspective API or a simple LLM judge). Measure revision rate and false-positive "
            "over-refusal on benign prompts."
        ),
        "related_chapters": [
            "../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md",
            "../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md",
            "../books/11-training-serving-and-ai-operations/02-post-training-methods.md",
        ],
        "related_concepts": ["instruction-tuning", "human-evaluation", "values"],
    },
    "moe": {
        "problem": (
            "Dense Transformer FFN layers activate all parameters for every token—scaling model "
            "capacity linearly increases compute per token. Conditional computation could activate "
            "only relevant subsets of parameters per input."
        ),
        "prior_art": (
            "Mixture of Experts literature (Jordan & Jacobs, 1994) existed but was hard to train "
            "at scale. GShard and Switch Transformer later simplified MoE for Transformers. "
            "Ensemble methods increased capacity but multiplied compute."
        ),
        "core_idea": (
            "Shazeer et al. introduced a Sparsely-Gated Mixture-of-Experts layer: replace the "
            "single FFN with N expert FFNs and a gating network that outputs a sparse weight "
            "vector per token. Each token activates only the top-k experts (typically k=1–2). "
            "A load-balancing auxiliary loss prevents collapse to a single expert. "
            "Total parameters scale with N, but compute per token scales with k—decoupling "
            "capacity from FLOPs."
        ),
        "evidence": [
            "137B MoE with 128 experts matched dense model quality on LM benchmark with ~10× "
            "less compute per token (k=2 of 128).",
            "1T parameter model with sparse activation trained successfully on Google infrastructure.",
            "Load-balancing loss was essential—without it, gating collapsed to 1–2 experts.",
            "MoE layers added at every other Transformer block balanced quality and routing overhead.",
        ],
        "limitations": [
            "Expert parallelism requires complex distributed training (all-to-all communication).",
            "Load imbalance causes some GPUs to idle while others are saturated.",
            "Routing instability during training—expert assignment shifts across checkpoints.",
            "Inference serving is harder: experts may reside on different devices, adding latency.",
        ],
        "impact": (
            "MoE became the architecture behind Mixtral, GPT-4 (rumored), and Google's Switch "
            "Transformer. It enables trillion-parameter models with manageable inference cost "
            "and is the primary scaling path beyond dense Transformers."
        ),
        "reproduction": (
            "Implement a 4-expert MoE FFN layer (top-1 routing) in a small Transformer using "
            "PyTorch. Train on a character-level LM task and compare perplexity against a "
            "dense FFN of equal total parameters. Monitor expert utilization histograms to "
            "verify load balancing."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/03-the-transformer-block.md",
            "../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md",
            "../books/04-transformers-and-foundation-models/04-training-foundation-models.md",
        ],
        "related_concepts": ["mixture-of-experts", "routing", "batching"],
    },
    "clip": {
        "problem": (
            "Computer vision models required task-specific labeled datasets (ImageNet, COCO) and "
            "could not generalize to new categories without retraining. Vision needed the kind of "
            "transfer learning that pre-trained LMs gave NLP."
        ),
        "prior_art": (
            "ImageNet supervised pre-training + fine-tuning was the standard. Self-supervised "
            "methods (SimCLR, MoCo) learned representations but still needed fine-tuning for "
            "downstream tasks. Vision-language models (VSE, VilBERT) existed but were small-scale."
        ),
        "core_idea": (
            "Radford et al. pre-trained dual encoders (image ViT, text Transformer) on 400M "
            "image-text pairs from the web using contrastive learning: maximize cosine similarity "
            "of matched pairs, minimize similarity of in-batch negatives. At inference, classify "
            "by embedding candidate text labels and picking the highest-similarity match—zero-shot "
            "without any task-specific training. The shared embedding space aligns visual and "
            "textual concepts."
        ),
        "evidence": [
            "Zero-shot ImageNet: 76.2% top-1 accuracy—matching original ResNet-50 supervised baseline.",
            "Zero-shot transfer competitive with fine-tuned models on 30+ datasets (CIFAR, STL-10, etc.).",
            "Prompt engineering for class names ('a photo of a {label}') improved zero-shot by 3–5 points.",
            "ViT-L/14 at 336px resolution: 87.8% zero-shot ImageNet—approaching supervised SOTA.",
        ],
        "limitations": [
            "Zero-shot requires careful prompt engineering for class names.",
            "Fine-grained classification (breed-level, medical imaging) underperforms supervised specialists.",
            "Training data bias (web scrapes) propagates into embedding space.",
            "No native generative capability—CLIP classifies but cannot generate images (led to diffusion conditioning).",
        ],
        "impact": (
            "CLIP enabled zero-shot vision deployment and became the text encoder for Stable Diffusion, "
            "DALL-E 2, and multimodal LLMs. Contrastive image-text pre-training is now standard for "
            "vision foundation models."
        ),
        "reproduction": (
            "Load `openai/clip-vit-base-patch32`, embed 20 images and their text descriptions. "
            "Compute pairwise cosine similarities and verify matched pairs rank highest. "
            "Run zero-shot classification on 10 CIFAR-10 images using class name prompts."
        ),
        "related_chapters": [
            "../books/13-multimodal-and-frontier-systems/01-vision-and-document-intelligence.md",
            "../books/13-multimodal-and-frontier-systems/03-image-and-video-generation.md",
            "../books/02-machine-learning-systems/03-unsupervised-and-representation-learning.md",
        ],
        "related_concepts": ["vision-encoders", "multimodal-models", "cosine-similarity"],
    },
    "whisper": {
        "problem": (
            "ASR systems required clean, labeled audio in each target language and degraded on "
            "accents, background noise, and code-switching. Building multilingual speech recognition "
            "traditionally required separate models per language."
        ),
        "prior_art": (
            "DeepSpeech, Wav2Vec 2.0, and supervised ASR models needed language-specific labeled data. "
            "Multilingual models existed but required careful language identification and "
            "language-specific fine-tuning."
        ),
        "core_idea": (
            "Radford et al. trained a seq2seq Transformer on 680,000 hours of weakly labeled "
            "multilingual audio from the web (YouTube, podcasts). Labels are noisy (auto-generated "
            "subtitles, metadata)—the model learns from scale rather than label quality. "
            "Input: 30-second audio chunks as log-mel spectrograms. Output: text tokens including "
            "special tokens for language identification, timestamps, and task specification "
            "(transcribe vs. translate). A single model handles 99 languages."
        ),
        "evidence": [
            "English ASR: competitive with supervised models (LibriSpeech WER ~2.7% on clean speech).",
            "Zero-shot transfer to unseen languages without fine-tuning.",
            "Robust to accents, background noise, and technical vocabulary from diverse training data.",
            "Translation mode: transcribe non-English audio directly to English text.",
        ],
        "limitations": [
            "Hallucination on silence or noise-only segments—model generates plausible but wrong text.",
            "Long-form audio requires chunking with potential boundary errors.",
            "Latency: full seq2seq decode is slower than streaming CTC models.",
            "Timestamp accuracy degrades on fast speech or overlapping speakers.",
        ],
        "impact": (
            "Whisper became the default open-source ASR, powering transcription services, voice "
            "agents, and accessibility tools. It demonstrated that weak supervision at scale "
            "beats careful labeling for speech."
        ),
        "reproduction": (
            "Run `openai/whisper-base` on 10 audio clips (5 clean, 5 noisy) from LibriSpeech or "
            "recorded samples. Compare WER against ground truth. Test on a non-English clip to "
            "verify zero-shot multilingual capability."
        ),
        "related_chapters": [
            "../books/13-multimodal-and-frontier-systems/02-speech-and-audio.md",
            "../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md",
            "../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md",
        ],
        "related_concepts": ["speech-recognition", "multilingual-models", "self-supervision"],
    },
    "speculative-decoding": {
        "problem": (
            "Autoregressive Transformer decoding generates one token at a time, bound by memory "
            "bandwidth loading the full model weights per token. Large models (70B+) achieve "
            "low token throughput even on high-end GPUs."
        ),
        "prior_art": (
            "Non-autoregressive decoding (parallel prediction) sacrificed quality. Knowledge "
            "distillation to smaller models lost capability. Batch inference helped throughput "
            "but not single-request latency."
        ),
        "core_idea": (
            "Leviathan et al. use a small draft model to autoregressively generate K candidate "
            "tokens cheaply, then run the large target model on all K+1 positions in a single "
            "parallel forward pass. Compare draft and target distributions token by token—accept "
            "matching tokens, reject at first mismatch and resample from a corrected distribution. "
            "Accepted tokens cost one target forward pass for K tokens; rejection rate determines "
            "speedup. Quality is identical to target-only decoding (lossless)."
        ),
        "evidence": [
            "2–3× speedup on T5-XXL and other models with no change in output distribution.",
            "Speedup increases with draft-target agreement—similar models achieve higher acceptance rates.",
            "Batch size 1 latency improved significantly; batch settings also benefit.",
            "Works with any draft/target pair where both share the same vocabulary.",
        ],
        "limitations": [
            "Requires a suitable draft model—too small drafts have low acceptance; too large adds overhead.",
            "Speedup is variable—adversarial or high-entropy text has lower acceptance rates.",
            "Memory: both models loaded simultaneously increases peak VRAM.",
            "Implementation complexity in serving frameworks (vLLM, TGI integration ongoing).",
        ],
        "impact": (
            "Speculative decoding is a standard inference optimization in vLLM, TensorRT-LLM, and "
            "production serving stacks. It enables practical latency for 70B+ models on single-GPU "
            "deployments with a small draft model."
        ),
        "reproduction": (
            "Implement basic speculative decoding with `google/gemma-2b` as draft and `google/gemma-7b` "
            "as target on 20 prompts. Measure tokens/second vs. target-only decoding. Log acceptance "
            "rate per prompt and correlate with output entropy."
        ),
        "related_chapters": [
            "../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md",
            "../books/04-transformers-and-foundation-models/05-inference-and-sampling.md",
            "../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md",
        ],
        "related_concepts": ["kv-cache", "latency", "distillation"],
    },
    "flash-attention": {
        "problem": (
            "Standard attention implementation materializes the full N×N attention matrix in GPU "
            "HBM (high-bandwidth memory), making attention memory-bound rather than compute-bound. "
            "Long sequences (4k+ tokens) exhaust GPU memory during training."
        ),
        "prior_art": (
            "Gradient checkpointing traded compute for memory. Sparse/linear attention approximations "
            "reduced memory but changed the computation. Kernel fusion attempts (xformers predecessors) "
            "had limited adoption."
        ),
        "core_idea": (
            "Dao et al. restructured attention computation to minimize HBM reads/writes using tiling: "
            "load blocks of Q, K, V into fast SRAM, compute attention scores and weighted values "
            "incrementally, and never materialize the full N×N matrix. The algorithm is IO-aware—"
            "analyzing memory hierarchy (SRAM vs. HBM) to minimize data movement. FlashAttention "
            "produces exact attention (not an approximation) with different memory access patterns. "
            "FlashAttention-2 further optimized work partitioning and warp scheduling."
        ),
        "evidence": [
            "2–4× training speedup on GPT-2 and BERT vs. standard PyTorch attention.",
            "Enabled 2× longer sequences on the same GPU memory budget.",
            "End-to-end BERT training 15% faster; GPT-2 training 3× faster at sequence length 1K.",
            "Exact attention—no quality difference vs. standard implementation.",
        ],
        "limitations": [
            "CUDA-specific implementation; AMD/TPU require separate ports.",
            "Head dimension constraints (typically ≤128) for optimal performance.",
            "Integration requires compatible model code (now standard in PyTorch 2.0+, HuggingFace).",
            "Does not reduce O(n²) compute—only memory and constant factors.",
        ],
        "impact": (
            "FlashAttention is the default attention implementation in PyTorch 2.0, HuggingFace "
            "Transformers, and every major training framework. It enabled the long-context models "
            "(32k, 128k tokens) that define the current generation."
        ),
        "reproduction": (
            "Benchmark attention on sequence lengths 512, 2048, 8192 using standard PyTorch vs. "
            "`flash_attn` on the same GPU. Measure peak memory and wall-clock time. Verify outputs "
            "are numerically identical (within fp16 tolerance)."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/02-attention.md",
            "../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md",
            "../books/04-transformers-and-foundation-models/03-the-transformer-block.md",
        ],
        "related_concepts": ["multi-head-attention", "long-context", "gpus"],
    },
    "rlhf-preference": {
        "problem": (
            "Automatic metrics (ROUGE, BLEU) poorly correlate with human judgment on summarization "
            "quality—optimizing ROUGE produces verbose, repetitive summaries. Human preferences "
            "needed to be incorporated into training objectives directly."
        ),
        "prior_art": (
            "Supervised fine-tuning on reference summaries. ROUGE/BLEU optimization produced "
            "metric-gaming artifacts. RL from human feedback (Christiano et al., 2017) existed "
            "for simple tasks but not at summarization scale."
        ),
        "core_idea": (
            "Stiennon et al. collected human comparisons of summary pairs (which is better?) for "
            "Reddit TL;DR posts. Trained a reward model (6B Transformer) to predict human preferences "
            "from comparison data. Fine-tuned a policy (GPT-3 1.3B) with PPO using the reward model "
            "as the objective, with a KL penalty to stay close to the SFT initialization. "
            "The key insight: preference comparisons are easier and more reliable for humans to "
            "provide than absolute quality scores or writing reference summaries."
        ),
        "evidence": [
            "Human eval: RLHF summaries preferred over SFT and ROUGE-optimized baselines.",
            "ROUGE scores did not predict human preference—ROUGE-optimized summaries were dispreferred.",
            "Reward model accuracy on held-out comparisons: ~70%—sufficient for PPO training signal.",
            "KL penalty was critical—without it, PPO collapsed to high-reward but low-quality outputs.",
        ],
        "limitations": [
            "Reward hacking: models learn to exploit RM weaknesses (length bias, format preferences).",
            "Human comparison data is expensive (~64k comparisons for this paper).",
            "RM accuracy ceiling (~70%) limits alignment quality.",
            "Summarization-specific—generalizing to dialogue, coding, etc. required follow-up work (InstructGPT).",
        ],
        "impact": (
            "This paper established the RM + PPO pipeline that InstructGPT and ChatGPT scaled to "
            "general instruction following. Preference learning over pointwise metrics became the "
            "standard alignment approach."
        ),
        "reproduction": (
            "Collect 50 pairwise summary preferences on news articles. Train a small reward model "
            "(BERT-base classifier) on chosen/rejected pairs. Compare RM-predicted rankings against "
            "held-out human judgments. Optionally run 100 steps of PPO on a 1B model and compare "
            "summaries before/after."
        ),
        "related_chapters": [
            "../books/11-training-serving-and-ai-operations/02-post-training-methods.md",
            "../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md",
            "../books/10-evaluation-safety-and-governance/01-evaluation-as-requirements.md",
        ],
        "related_concepts": ["human-evaluation", "sft", "rubrics"],
    },
    "self-instruct": {
        "problem": (
            "Instruction tuning requires large datasets of (instruction, response) pairs, typically "
            "written by humans. Scaling instruction data to improve zero-shot generalization was "
            "bottlenecked by annotation cost."
        ),
        "prior_art": (
            "Manual datasets: Super-NaturalInstructions (600+ tasks), P3, FLAN collection—all "
            "human-curated. Data augmentation existed but not for instruction generation specifically."
        ),
        "core_idea": (
            "Wang et al. bootstrap instruction data from a seed set of 175 human-written tasks: "
            "(1) prompt the LM to generate new instruction descriptions; (2) determine if each "
            "instruction is valid (classification); (3) generate input instances for the instruction; "
            "(4) filter low-quality instances; (5) generate responses. Iterate to expand the pool. "
            "The resulting 52k instruction dataset (Self-Instruct) fine-tunes the base LM, improving "
            "zero-shot performance on unseen tasks from Super-NaturalInstructions."
        ),
        "evidence": [
            "52k self-generated instructions improved zero-shot on 119 held-out tasks vs. base LM.",
            "Outperformed training on human-written instruction datasets of similar size.",
            "Alpaca (built on Self-Instruct methodology with GPT-3.5 as generator) went viral—"
            "demonstrating practical utility.",
            "Quality filtering was essential—unfiltered self-generated data hurt performance.",
        ],
        "limitations": [
            "Quality ceiling bounded by the generating model's capabilities.",
            "Repetitive or trivial instructions accumulate without diversity controls.",
            "Instruction complexity does not exceed the generator—no novel hard tasks emerge.",
            "Seed task selection biases the generated distribution.",
        ],
        "impact": (
            "Self-Instruct enabled Alpaca, Vicuna, and the open instruction-tuning ecosystem. "
            "Synthetic data generation for alignment is now standard practice in model training pipelines."
        ),
        "reproduction": (
            "Start with 10 seed instruction templates. Use GPT-4o-mini to generate 100 new instructions, "
            "filter for validity, generate instances and responses. Fine-tune a 1B model on the result "
            "and evaluate on 20 held-out tasks vs. base model zero-shot."
        ),
        "related_chapters": [
            "../books/11-training-serving-and-ai-operations/03-dataset-engineering.md",
            "../books/11-training-serving-and-ai-operations/02-post-training-methods.md",
            "../books/05-prompt-and-context-engineering/01-instructions-that-work.md",
        ],
        "related_concepts": ["synthetic-data", "instruction-tuning", "sft"],
    },
    "tree-of-thoughts": {
        "problem": (
            "Chain-of-thought follows a single reasoning path—no backtracking, exploration, or "
            "comparison of alternatives. Hard problems (puzzles, planning, creative writing) require "
            "deliberate search over multiple intermediate states."
        ),
        "prior_art": (
            "CoT elicited single-path reasoning. Beam search operated over tokens, not semantic "
            "states. Classical search (BFS, DFS, A*) required formal state representations "
            "incompatible with free-form LM generation."
        ),
        "core_idea": (
            "Yao et al. treat each intermediate reasoning step as a 'thought' node in a search tree. "
            "At each node, the LM generates candidate next thoughts. A evaluation function (LM "
            "self-evaluation or heuristic) scores each candidate. Search algorithms (BFS or DFS) "
            "explore the tree, pruning low-scoring branches. Backtracking occurs when all "
            "children of a node score poorly. This generalizes CoT from a single chain to a "
            "deliberate search process with LM-generated states and LM-generated evaluations."
        ),
        "evidence": [
            "Game of 24: ToT solved 74% vs. CoT 4% (GPT-4)—dramatic improvement on search-heavy task.",
            "Creative writing (coherent paragraph planning): ToT improved coherence scores in human eval.",
            "Mini crosswords: ToT with BFS outperformed greedy CoT on word fill rate.",
            "Self-evaluation as heuristic correlated with actual success on Game of 24.",
        ],
        "limitations": [
            "Token cost 5–20× higher than single CoT—each node requires generation + evaluation.",
            "Self-evaluation is unreliable for many tasks—external verifiers needed when available.",
            "Search hyperparameters (breadth, depth, branching factor) are task-specific.",
            "No general framework—each task requires designing thought decomposition and evaluation.",
        ],
        "impact": (
            "ToT established test-time compute scaling via search as a research direction, influencing "
            "o1-style reasoning models and best-of-N sampling strategies. It formalized the idea that "
            "inference-time search can substitute for model scale."
        ),
        "reproduction": (
            "Implement BFS-ToT on Game of 24 with 10 puzzles using GPT-4o-mini. Use 3-step "
            "thoughts (partial equations) with LM self-evaluation. Compare solve rate against "
            "standard CoT. Log total tokens used per puzzle."
        ),
        "related_chapters": [
            "../books/07-reasoning-and-tool-use/01-reasoning-as-search.md",
            "../books/07-reasoning-and-tool-use/02-planning.md",
            "../books/07-reasoning-and-tool-use/03-verification-and-critique.md",
        ],
        "related_concepts": ["backtracking", "test-time-compute", "self-consistency"],
    },
    "graph-rag": {
        "problem": (
            "Standard vector RAG retrieves local chunks similar to the query—it fails on global "
            "questions that require synthesizing information across an entire corpus ('What are the "
            "main themes in this dataset?' or 'How does entity X relate to entity Y across all documents?')."
        ),
        "prior_art": (
            "Naive chunk-and-embed RAG handled entity-specific queries but not corpus-wide synthesis. "
            "Knowledge graphs required manual schema design and entity resolution. Map-reduce summarization "
            "was expensive and lost detail."
        ),
        "core_idea": (
            "Edge et al. build a graph index in two phases: (1) extract entities and relationships "
            "from each text chunk using an LLM, forming a knowledge graph; (2) apply community "
            "detection (Leiden algorithm) to cluster related entities, then generate natural-language "
            "summaries for each community. At query time, map-reduce operates over community summaries "
            "for global queries, or graph traversal for local entity queries. This hierarchical structure "
            "captures both fine-grained entity facts and high-level corpus themes."
        ),
        "evidence": [
            "Podcast transcript corpus: Graph RAG produced more comprehensive answers on global "
            "sensemaking queries vs. naive RAG (human eval).",
            "Entity-specific queries: graph traversal retrieved relevant context missed by vector search alone.",
            "Community summaries captured themes not present in any single chunk.",
            "Indexing cost is higher than naive RAG but amortized over many queries.",
        ],
        "limitations": [
            "Graph extraction errors propagate—wrong entities or relations corrupt the index.",
            "Community detection parameters affect summary granularity; no universal settings.",
            "Indexing requires LLM calls per chunk for entity extraction—expensive for large corpora.",
            "Dynamic corpora require re-indexing; incremental updates are non-trivial.",
        ],
        "impact": (
            "Graph RAG became Microsoft's recommended pattern for enterprise RAG on document collections "
            "and influenced Neo4j, LangChain, and LlamaIndex graph retrieval modules. It addresses "
            "a real failure mode of production RAG systems."
        ),
        "reproduction": (
            "Index 20 news articles: extract entities/relations with an LLM, build a NetworkX graph, "
            "detect communities, summarize each. Ask 5 global questions ('What themes appear across "
            "these articles?') and compare Graph RAG answers against naive top-k chunk RAG."
        ),
        "related_chapters": [
            "../books/06-knowledge-and-retrieval-systems/06-advanced-and-enterprise-rag.md",
            "../books/06-knowledge-and-retrieval-systems/02-document-ingestion.md",
            "../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md",
        ],
        "related_concepts": ["graph-rag", "retrieval", "summarization"],
    },
    "mamba": {
        "problem": (
            "Transformer self-attention scales O(n²) in sequence length, limiting context windows "
            "and making long-document processing expensive at both training and inference time. "
            "Linear-time alternatives were needed without sacrificing quality."
        ),
        "prior_art": (
            "State space models (S4) achieved linear scaling but were time-invariant—treating all "
            "inputs uniformly. Linear attention variants (Performers, Linformer) approximated "
            "attention but often degraded quality. RWKV combined RNN and Transformer properties."
        ),
        "core_idea": (
            "Gu & Dao introduced selective state space models (SSMs) where the SSM parameters "
            "(Δ, B, C) are input-dependent functions rather than fixed. This selectivity lets the "
            "model decide what to remember and what to ignore per token—addressing the weakness of "
            "prior SSMs on discrete language tasks. Mamba eliminates the SSM's time-invariance "
            "while maintaining O(n) compute and O(1) memory per step at inference. A hardware-aware "
            "parallel scan algorithm enables efficient training."
        ),
        "evidence": [
            "Language modeling perplexity matched Transformers at scales up to 3B parameters on "
            "The Pile.",
            "5× higher throughput than Transformers at sequence length 8192 during generation.",
            "Selective mechanism ablation: input-dependent Δ was the critical component vs. time-invariant S4.",
            "Mamba-2 further unified SSM and attention perspectives with improved constants.",
        ],
        "limitations": [
            "Ecosystem immaturity—fewer pre-trained checkpoints, tools, and fine-tuning recipes vs. Transformers.",
            "Hybrid Mamba-Transformer models often outperform pure Mamba on downstream tasks.",
            "CUDA kernel dependency for efficient training; CPU inference is slow.",
            "Long-range recall benchmarks (Needle in Haystack) show mixed results vs. full attention.",
        ],
        "impact": (
            "Mamba proved that attention is not strictly necessary for language modeling quality, "
            "opening a research frontier in alternative sequence architectures. Mamba-2 and hybrid "
            "models (Jamba) are actively deployed in production."
        ),
        "reproduction": (
            "Train a tiny Mamba model (2 layers, d=256) on a character-level Shakespeare corpus "
            "using the `mamba-ssm` library. Compare training speed and perplexity against a "
            "Transformer of equal size at sequence lengths 512 and 2048."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md",
            "../books/04-transformers-and-foundation-models/03-the-transformer-block.md",
            "../books/13-multimodal-and-frontier-systems/05-long-context-world-models-and-continual-learning.md",
        ],
        "related_concepts": ["state-spaces", "long-context", "lstms"],
    },
    "jailbreak-survey": {
        "problem": (
            "Aligned LLMs remain vulnerable to adversarial inputs that bypass safety training—"
            "prompt injections, jailbreaks, and tool abuse in production systems. Engineers deploying "
            "LLM applications lack a systematic catalog of attack patterns and mitigations."
        ),
        "prior_art": (
            "Ad hoc red-teaming produced scattered examples (DAN prompts, base64 encoding). "
            "Academic adversarial ML focused on classification attacks, not generative LLM behavior. "
            "No industry-standard taxonomy connected attacks to defenses."
        ),
        "core_idea": (
            "Representative surveys (OWASP Top 10 for LLM Applications, Perez & Ribeiro, Greshake et al.) "
            "catalog attack categories: direct prompt injection (override system instructions), "
            "indirect injection (malicious content in retrieved documents or tool outputs), "
            "jailbreak templates (role-play, encoding, multi-turn escalation), model extraction, "
            "denial of service, and supply chain attacks. Defenses include input/output filtering, "
            "instruction hierarchy, tool sandboxing, privilege separation, and continuous red-teaming. "
            "The core principle: treat LLM inputs as untrusted and layer defenses."
        ),
        "evidence": [
            "OWASP LLM Top 10 (2023–2025): prompt injection ranked #1 risk across industry surveys.",
            "Indirect injection demonstrated on RAG systems: malicious web pages in retrieved context "
            "override assistant behavior (Greshake et al.).",
            "Automated jailbreak discovery (PAIR, TAP) finds bypasses faster than manual red-teaming.",
            "No single defense eliminates all attacks—defense-in-depth required.",
        ],
        "limitations": [
            "Arms race: new jailbreaks appear faster than defenses are deployed.",
            "Eval coverage gaps—no benchmark captures all attack categories.",
            "Defenses often reduce utility (over-refusal, latency from filtering).",
            "Tool abuse and multi-agent attack surfaces are still poorly understood.",
        ],
        "impact": (
            "OWASP LLM Top 10 and related surveys became the starting checklist for LLM security reviews "
            "in enterprise deployments. They shaped CI red-team harnesses and responsible-AI governance frameworks."
        ),
        "reproduction": (
            "Build a 20-case attack set covering 4 categories (direct injection, indirect via RAG, "
            "jailbreak template, tool abuse). Run against your assistant with and without input "
            "filtering. Score success rate per category. Document which attacks bypass which defenses."
        ),
        "related_chapters": [
            "../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md",
            "../books/05-prompt-and-context-engineering/05-context-failure-and-security.md",
            "../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md",
        ],
        "related_concepts": ["prompt-injection", "tool-abuse", "threat-modeling"],
    },
    "knowledge-neurons": {
        "problem": (
            "Factual knowledge in pre-trained LMs is distributed across billions of parameters with "
            "no clear localization. Understanding where and how facts are stored is prerequisite "
            "to knowledge editing, unlearning, and interpretability."
        ),
        "prior_art": (
            "Probing classifiers detected encoded information in hidden states but did not identify "
            "causal mechanisms. Memorization studies found LMs recall training data but not which "
            "components enable recall."
        ),
        "core_idea": (
            "Dai et al. identify 'knowledge neurons' in Transformer FFN layers: individual "
            "feed-forward dimensions whose activation correlates with expressing a specific fact "
            "(e.g., 'Paris is the capital of France'). Method: (1) prompt the model with a fact "
            "expression; (2) compute attribution scores for each FFN neuron; (3) select top neurons "
            "as knowledge neurons. Causal test: suppressing (zeroing) those neurons reduces the "
            "model's ability to express the fact; amplifying them increases recall. Knowledge is "
            "localized but distributed—a fact may involve 5–20 neurons across layers."
        ),
        "evidence": [
            "LAMA benchmark: suppressing identified knowledge neurons reduced factual recall accuracy "
            "by 30–50% for targeted facts.",
            "Cross-lingual facts share neurons across languages (English 'Paris' and French 'Paris' "
            "activate overlapping neurons).",
            "Editing fact by modifying neuron activations changed model predictions without "
            "full fine-tuning.",
            "Neurons are sparse—<1% of FFN dimensions account for most factual recall.",
        ],
        "limitations": [
            "Neuron-fact mapping is imprecise—suppression affects related facts (side effects).",
            "Method works best for simple relational facts; complex reasoning not localized.",
            "Multilingual and multi-hop facts have messier neuron distributions.",
            "Causal claims depend on intervention methodology—correlation vs. causation debated.",
        ],
        "impact": (
            "Knowledge neurons research launched the field of LM knowledge editing (ROME, MEMIT) "
            "and informed interpretability work on FFN layers as key-value stores."
        ),
        "reproduction": (
            "Using a small LM (GPT-2 or Pythia-1B), select 10 facts from LAMA. Compute integrated "
            "gradients attribution on FFN layers for each fact. Identify top-5 neurons, suppress "
            "them, and measure prediction probability drop. Compare against random neuron suppression."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/03-the-transformer-block.md",
            "../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md",
            "../books/01-foundations-of-intelligence/02-from-symbols-to-statistics.md",
        ],
        "related_concepts": ["neurons-and-layers", "knowledge-representation", "behavior-versus-knowledge"],
    },
    "ragas": {
        "problem": (
            "RAG systems lacked standardized, automated evaluation metrics—teams relied on ad hoc "
            "human review or generic NLG metrics (BLEU, ROUGE) that don't measure faithfulness "
            "to retrieved context."
        ),
        "prior_art": (
            "BLEU/ROUGE measured n-gram overlap with reference answers, not grounding in context. "
            "Human evaluation was expensive and not CI-friendly. TruLens and ARES existed but "
            "without wide adoption or reference-free operation."
        ),
        "core_idea": (
            "Es et al. define reference-free RAG metrics using LLM-as-judge: Faithfulness "
            "(are answer claims supported by retrieved context?), Answer Relevance (does the "
            "answer address the question?), Context Precision (are retrieved passages relevant?), "
            "and Context Recall (does retrieved context cover the answer?). Each metric uses "
            "a prompted LLM to classify or score specific aspects, enabling automated pipeline "
            "evaluation without gold-standard answers. Ragas provides a Python framework "
            "integrating these metrics into evaluation loops."
        ),
        "evidence": [
            "Faithfulness metric correlated with human judgment on RAG test sets (ρ > 0.7 on "
            "several datasets).",
            "Context Precision/Recall identified retrieval failures that end-to-end metrics missed.",
            "Reference-free operation enabled eval on production queries without labeled data.",
            "Adopted in LangChain, LlamaIndex, and CI pipelines for RAG regression testing.",
        ],
        "limitations": [
            "LLM judge bias—evaluator model preferences affect scores.",
            "Cost: each metric requires LLM calls; expensive at scale.",
            "Not ground truth—high faithfulness score does not guarantee correctness.",
            "Judge calibration varies across domains; legal/medical need domain-specific judges.",
        ],
        "impact": (
            "RAGAS became the de facto standard for RAG evaluation in development and CI, "
            "analogous to what ROUGE was for summarization but designed for grounding."
        ),
        "reproduction": (
            "Build a 10-question RAG pipeline over 20 documents. Compute Ragas faithfulness, "
            "answer relevance, and context precision using `ragas` library with GPT-4o-mini as judge. "
            "Deliberately inject one unfaithful answer and one irrelevant retrieval; verify metrics "
            "detect the degradation."
        ),
        "related_chapters": [
            "../books/10-evaluation-safety-and-governance/03-evaluation-by-system-stage.md",
            "../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md",
            "../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md",
        ],
        "related_concepts": ["faithfulness", "citation-precision", "component-evals"],
    },
    "olmo": {
        "problem": (
            "Most 'open' models released weights but hid training data, code, or logs—preventing "
            "true reproducibility and scientific study of how design choices affect outcomes."
        ),
        "prior_art": (
            "LLaMA released weights but not data or training code. Pythia (EleutherAI) opened "
            "some training details. BLOOM was open but underperformed frontier models. "
            "No model offered full pipeline transparency at competitive quality."
        ),
        "core_idea": (
            "Groeneveld et al. released everything: model weights (OLMo-7B), pre-training data "
            "(Dolma—3T tokens, fully documented), training code (Ai2's OLMo framework), training "
            "logs, evaluation harness, and model cards. Architectural choices (SwiGLU, RoPE, "
            "no bias terms) documented with ablation evidence. Dolma dataset composition and "
            "filtering pipeline fully described. The goal is enabling the scientific study of "
            "LM training rather than just deploying another checkpoint."
        ),
        "evidence": [
            "OLMo-7B competitive with LLaMA-2-7B on MMLU, GSM8K, and other standard benchmarks.",
            "Training curves and intermediate checkpoints published—enables studying learning dynamics.",
            "Dolma ablation studies showed impact of data filtering on downstream performance.",
            "Full reproducibility: independent teams replicated training within reported loss curves.",
        ],
        "limitations": [
            "Full training run requires significant compute (~800 A100-hours for 7B).",
            "Initial release limited to 7B scale—larger variants followed later.",
            "Dolma data, while documented, cannot be fully re-collected by external teams.",
            "Post-training (SFT, RLHF) not included in base OLMo—requires separate alignment work.",
        ],
        "impact": (
            "OLMo set a new standard for openness in LM research, influencing Allen AI's subsequent "
            "releases and raising expectations for what 'open' means in the field."
        ),
        "reproduction": (
            "Download OLMo-7B and Dolma sample. Fine-tune on 500 instruction pairs using the "
            "published training code. Compare eval metrics against LLaMA-2-7B fine-tuned on the "
            "same data. Inspect published training logs to identify loss anomalies."
        ),
        "related_chapters": [
            "../books/04-transformers-and-foundation-models/04-training-foundation-models.md",
            "../books/11-training-serving-and-ai-operations/03-dataset-engineering.md",
            "../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md",
        ],
        "related_concepts": ["open-weights", "data-provenance", "reproduction"],
    },
    "agent-benchmark-webarena": {
        "problem": (
            "Web agent benchmarks used simplified environments (MiniWoB++ synthetic HTML) or static "
            "datasets (Mind2Web snapshots) that did not capture the complexity of real websites—"
            "dynamic content, authentication, multi-step workflows."
        ),
        "prior_art": (
            "MiniWoB++: synthetic pages with simple DOM. WebShop: simulated e-commerce with "
            "limited catalog. Mind2Web: real website snapshots but offline (no live interaction). "
            "None tested agents on functional, stateful web applications."
        ),
        "core_idea": (
            "Zhou et al. built WebArena: four self-hosted, fully functional website replicas "
            "(e-commerce, forum, GitLab, map) with real backend state. Agents receive natural "
            "language goals ('Order a red t-shirt in size M') and interact via browser actions "
            "(click, type, navigate). Success is programmatically verified against backend state "
            "(order exists in database). 812 tasks span multi-step workflows requiring planning, "
            "grounding, and error recovery on realistic UIs."
        ),
        "evidence": [
            "GPT-4 agent: ~14% task success rate vs. human performance ~78%.",
            "Best published agent (with specialized prompting): ~30%—still far from human.",
            "Failure analysis: planning errors (40%), grounding errors (35%), timeout (25%).",
            "Tasks requiring authentication, form filling, and cross-site navigation most challenging.",
        ],
        "limitations": [
            "Self-hosted replicas, not live web—may miss real-world dynamic content and CAPTCHAs.",
            "Maintenance burden: website updates require benchmark updates.",
            "Task coverage limited to 4 site types—may not generalize to all web domains.",
            "Evaluation is binary success/fail—partial credit for near-misses not captured.",
        ],
        "impact": (
            "WebArena became the standard realistic web agent benchmark, used to evaluate GPT-4V, "
            "Claude, and research agents. It exposed the large gap between LLM capability and "
            "reliable autonomous web operation."
        ),
        "reproduction": (
            "Deploy WebArena locally (Docker). Run GPT-4o with a ReAct-style browser agent on "
            "10 e-commerce tasks. Log success rate, steps taken, and failure category. Compare "
            "against a human completing the same tasks for a baseline."
        ),
        "related_chapters": [
            "../books/08-agent-systems/04-agent-patterns.md",
            "../books/13-multimodal-and-frontier-systems/04-computer-use-and-embodied-action.md",
            "../books/08-agent-systems/06-operating-long-running-agents.md",
        ],
        "related_concepts": ["benchmarks", "task-success", "action-spaces"],
    },
    "mcp-spec": {
        "problem": (
            "Every LLM application implemented tool integration differently—custom JSON schemas, "
            "ad hoc auth, proprietary protocols. Tool providers had to build N integrations for "
            "N host applications, and developers could not swap tool backends without rewriting."
        ),
        "prior_art": (
            "OpenAI function calling defined a schema format but not a transport or discovery protocol. "
            "LangChain tools were Python-specific with no standard wire format. LSP (Language Server "
            "Protocol) inspired the idea of a standard protocol but was code-editor-specific."
        ),
        "core_idea": (
            "Anthropic's Model Context Protocol (MCP) defines a JSON-RPC 2.0 wire protocol between "
            "a host (LLM application) and servers (tool/data providers). Servers expose capabilities "
            "via three primitives: Tools (callable functions with JSON Schema inputs), Resources "
            "(readable data sources), and Prompts (templated prompt sequences). Discovery is dynamic—"
            "hosts query servers for available capabilities at connection time. Transport supports "
            "stdio (local) and SSE (remote). Auth and permissions are server-managed."
        ),
        "evidence": [
            "Adopted by Claude Desktop, Cursor, Zed, and growing server ecosystem (100+ MCP servers).",
            "Server implementations exist for GitHub, Slack, Postgres, filesystem, and web search.",
            "Dynamic discovery enables hosts to expose only relevant tools per context.",
            "Separation of concerns: tool providers build one MCP server; hosts integrate once.",
        ],
        "limitations": [
            "Early specification—breaking changes possible as protocol matures.",
            "Security model still evolving (server sandboxing, permission scopes, audit logging).",
            "Transport fragmentation (stdio vs. SSE vs. future options) complicates deployment.",
            "No standard for streaming tool results or long-running operations.",
        ],
        "impact": (
            "MCP is becoming the USB-C of LLM tool integration—one protocol connecting hosts to "
            "tools, resources, and prompts. It reduces integration friction and enables an "
            "ecosystem of reusable tool servers."
        ),
        "reproduction": (
            "Build a minimal MCP server exposing one tool (e.g., `get_weather(city)`) using the "
            "Python MCP SDK. Connect it to Claude Desktop or Cursor. Verify dynamic discovery, "
            "tool invocation, and error handling. Compare integration code against a bespoke "
            "function-calling implementation."
        ),
        "related_chapters": [
            "../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md",
            "../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md",
            "../books/08-agent-systems/02-the-agent-loop.md",
        ],
        "related_concepts": ["mcp", "tool-schemas", "portable-interfaces"],
    },
}
