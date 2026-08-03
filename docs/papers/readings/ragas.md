# RAGAS: Automated Evaluation of Retrieval Augmented Generation

## Citation

Es et al.. *RAGAS: Automated Evaluation of Retrieval Augmented Generation.* 2023. [https://arxiv.org/abs/2309.15217](https://arxiv.org/abs/2309.15217)

## One-sentence contribution

Faithfulness and context precision metrics for RAG pipelines.

## Problem

RAG systems lacked standardized, automated evaluation metrics—teams relied on ad hoc human review or generic NLG metrics (BLEU, ROUGE) that don't measure faithfulness to retrieved context.

## Prior art

BLEU/ROUGE measured n-gram overlap with reference answers, not grounding in context. Human evaluation was expensive and not CI-friendly. TruLens and ARES existed but without wide adoption or reference-free operation.

## Core idea

Es et al. define reference-free RAG metrics using LLM-as-judge: Faithfulness (are answer claims supported by retrieved context?), Answer Relevance (does the answer address the question?), Context Precision (are retrieved passages relevant?), and Context Recall (does retrieved context cover the answer?). Each metric uses a prompted LLM to classify or score specific aspects, enabling automated pipeline evaluation without gold-standard answers. Ragas provides a Python framework integrating these metrics into evaluation loops.

## Evidence

- Faithfulness metric correlated with human judgment on RAG test sets (ρ > 0.7 on several datasets).
- Context Precision/Recall identified retrieval failures that end-to-end metrics missed.
- Reference-free operation enabled eval on production queries without labeled data.
- Adopted in LangChain, LlamaIndex, and CI pipelines for RAG regression testing.

## Limitations

- LLM judge bias—evaluator model preferences affect scores.
- Cost: each metric requires LLM calls; expensive at scale.
- Not ground truth—high faithfulness score does not guarantee correctness.
- Judge calibration varies across domains; legal/medical need domain-specific judges.

## Lasting impact

RAGAS became the de facto standard for RAG evaluation in development and CI, analogous to what ROUGE was for summarization but designed for grounding.

## Reproduction exercise

Build a 10-question RAG pipeline over 20 documents. Compute Ragas faithfulness, answer relevance, and context precision using `ragas` library with GPT-4o-mini as judge. Deliberately inject one unfaithful answer and one irrelevant retrieval; verify metrics detect the degradation.

## Related chapters

- [03 Evaluation By System Stage](../../books/10-evaluation-safety-and-governance/03-evaluation-by-system-stage.md)
- [05 Rag Generation And Citations](../../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md)
- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)

## Related concepts

- [Faithfulness](../../concepts/cards/faithfulness.md)
- [Citation Precision](../../concepts/cards/citation-precision.md)
- [Component Evals](../../concepts/cards/component-evals.md)
