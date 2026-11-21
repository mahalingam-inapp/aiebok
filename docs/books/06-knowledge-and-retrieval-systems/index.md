# Knowledge and Retrieval Systems

Technical course 06 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Build grounded knowledge systems whose ingestion, retrieval, generation, and citations can be evaluated separately.

[Start the first lecture](01-knowledge-outside-the-model.md){ .md-button .md-button--primary }
[Download the course notebook](../../assets/notebooks/06-knowledge-and-retrieval-systems.ipynb){ .md-button download }

## Entry prerequisites

- Courses 03–05 or equivalent experience
- Embeddings and search
- Structured model output

## Course outline

### Knowledge strategy and ingestion

- [01 · Knowledge Outside the Model](01-knowledge-outside-the-model.md)
- [02 · Document Ingestion](02-document-ingestion.md)

**Checkpoint**

Sketch source identifiers and chunk lineage for two versions of the same policy.

### Retrieval and reranking

- [03 · Retrieval](03-retrieval.md)
- [04 · Ranking and Context Selection](04-ranking-and-context-selection.md)

**Checkpoint**

Compare two ranked lists and trace how reciprocal rank fusion combines them.

### Grounded answers and enterprise constraints

- [05 · RAG Generation and Citations](05-rag-generation-and-citations.md)
- [06 · Advanced and Enterprise RAG](06-advanced-and-enterprise-rag.md)

**Checkpoint**

Define pass cases for authorized evidence, no relevant evidence, and a citation to the wrong passage.

## Notebook workshop

Build rankings with one shared candidate. Test how agreement affects rank before evaluating citation faithfulness separately.

In the applied exercise for Lecture 05, you will evaluate grounded answers against an access boundary.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Deliver an enterprise RAG system with authorization, hybrid retrieval, reranking, citations, and stage-specific evaluation.

Submit a short specification, an implementation or architecture, evidence from a baseline comparison, and one architecture decision record. Include one example that fails and explain how you would handle it.

## Suggested three-week schedule

- **Week 1:** Complete the first section and its checkpoint.
- **Week 2:** Complete the second section and start the project.
- **Week 3:** Complete the final section and the notebook workshop. Evaluate and review the project.

## Assessment

| Evidence | Weight |
|---|---:|
| Lecture knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Course project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Lewis et al. — Retrieval-Augmented Generation
- Karpukhin et al. — Dense Passage Retrieval

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
