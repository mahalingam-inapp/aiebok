# Retrieval-Augmented Generation for Knowledge-Intensive NLP

## Citation

Lewis et al.. *Retrieval-Augmented Generation for Knowledge-Intensive NLP.* 2020. [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)

## One-sentence contribution

Retrieve documents at generation time to ground outputs.

## Problem

Parametric language models store knowledge in weights—they cannot cite sources, update facts without retraining, or reliably answer questions about niche or recent information. Pure generation hallucinates on knowledge-intensive tasks.

## Prior art

kNN-LM (Khandelwal et al.) retrieved similar training sentences at inference. REALM jointly pre-trained retriever and LM but required expensive end-to-end training. Open-book QA systems pipelined retrieval and reading comprehension as separate stages without end-to-end differentiability.

## Core idea

Lewis et al. combined a dense passage retriever (DPR-style dual encoder) with a BART seq2seq generator in a RAG-Sequence and RAG-Token variant. At inference, the retriever fetches top-k Wikipedia passages for the query; the generator conditions on these passages to produce the answer. The retriever and generator can be trained jointly with the generator loss providing a training signal to the retriever, or pre-trained components can be composed without joint training (RAG-Sequence treats retrieved docs as a single context; RAG-Token marginalizes over documents per token).

## Evidence

- Natural Questions: RAG-Token beat BART-Large and DPR+BERT pipeline on exact match and BLEU-style answer overlap.
- TriviaQA and WebQuestions: consistent gains over parametric-only BART baselines.
- Generated answers were more factual and specific—human eval preferred RAG outputs on Jeopardy-style questions.
- Ablation: retrieval mattered most on rare entities; parametric-only was competitive on common facts.

## Limitations

- Retriever and generator can be misaligned—retrieved passages may not contain the answer or may mislead the generator.
- Top-k retrieval adds latency (embedding search + reranking) at every query.
- No native citation mechanism—models may not attribute claims to specific passages.
- Wikipedia-only index limits domain-specific deployment without re-indexing.

## Lasting impact

RAG became the default architecture for enterprise Q&A, copilots, and grounded assistants. Every major cloud provider now ships a managed RAG stack tracing to this retrieve-then-generate pattern.

## Reproduction exercise

Build a minimal RAG pipeline: chunk 50 pages of internal docs, embed with `sentence-transformers/all-MiniLM-L6-v2`, store in Chroma/FAISS, retrieve top-5 for 20 test questions, pass to an LLM with a 'answer only from context' prompt. Measure answer correctness with and without retrieval on the same questions.

## Related chapters

- [05 Rag Generation And Citations](../../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md)
- [03 Retrieval](../../books/06-knowledge-and-retrieval-systems/03-retrieval.md)
- [01 Knowledge Outside The Model](../../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md)

## Related concepts

- [Rag](../../concepts/cards/rag.md)
- [Retrieval](../../concepts/cards/retrieval.md)
- [Faithfulness](../../concepts/cards/faithfulness.md)
