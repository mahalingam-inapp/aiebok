# Dense Passage Retrieval for Open-Domain QA

## Citation

Karpukhin et al.. *Dense Passage Retrieval for Open-Domain QA.* 2020. [https://arxiv.org/abs/2004.04906](https://arxiv.org/abs/2004.04906)

## One-sentence contribution

Dual-encoder dense retrieval competitive with BM25 on open QA.

## Problem

Open-domain QA requires retrieving relevant passages from millions of documents before answer extraction. BM25 lexical matching dominated but missed paraphrases and semantic equivalence ('LLM' vs. 'large language model').

## Prior art

BM25 and TF-IDF retrieval were fast and strong baselines. Earlier dense retrieval (ICT, ORQA) showed promise but required complex pre-training or did not match BM25 on standard benchmarks. Cross-encoder rerankers were accurate but too slow for first-stage retrieval.

## Core idea

Karpukhin et al. trained two independent BERT encoders—one for questions, one for passages—mapping each to a dense vector. Retrieval is approximate nearest neighbor search in passage embedding space. Training uses in-batch negatives (other passages in the batch as distractors) plus hard negatives mined from BM25 top-k that the retriever currently ranks highly but are wrong. This contrastive setup is simpler than joint retriever-reader training and scales to Wikipedia-scale indexes.

## Evidence

- Natural Questions (open-domain): top-20 passage retrieval accuracy 78.4% vs. BM25 59.1%.
- TriviaQA: top-20 accuracy 78.8% vs. BM25 66.8%.
- End-to-end QA (DPR + reader) beat ORQA and REALM on multiple benchmarks.
- Hard negative mining contributed ~7 points over in-batch negatives alone.

## Limitations

- Domain shift hurts—DPR fine-tuned on Wikipedia underperforms on biomedical or legal corpora without retraining.
- Dual encoders cannot model cross-attention between question and passage at retrieval time.
- Index staleness: new documents require re-embedding the entire corpus.
- Top-k selection is a hyperparameter; too few misses relevant docs, too many adds noise for the reader.

## Lasting impact

DPR established dual-encoder dense retrieval as the default first stage in RAG pipelines, replacing or augmenting BM25 in production search. Its training recipe is the foundation for embedding APIs and hybrid retrieval systems.

## Reproduction exercise

Fine-tune `facebook/dpr-question_encoder-single-nq-base` on 1000 NQ question-passage pairs from the BEIR benchmark subset. Evaluate recall@10 against BM25 on the same queries. Then compare end-to-end answer F1 with a frozen reader (any LLM) using DPR vs. BM25 retrieval.

## Related chapters

- [03 Retrieval](../../books/06-knowledge-and-retrieval-systems/03-retrieval.md)
- [04 Ranking And Context Selection](../../books/06-knowledge-and-retrieval-systems/04-ranking-and-context-selection.md)
- [05 Similarity And Vector Search](../../books/03-language-and-representation/05-similarity-and-vector-search.md)

## Related concepts

- [Dense Retrieval](../../concepts/cards/dense-retrieval.md)
- [Bm25](../../concepts/cards/bm25.md)
- [Hybrid Search](../../concepts/cards/hybrid-search.md)
