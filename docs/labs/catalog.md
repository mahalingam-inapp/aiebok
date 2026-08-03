# Lab Catalog

**83 labs** — 78 chapter labs below plus 5 starter labs on [Hands-on start](start-here.md).

Each row links the lab doc, runnable entrypoint, and chapter practice objective.

??? abstract "Book 01 — Foundations of Intelligence (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 1.1 | [What Intelligence Means](0101-what-intelligence-means.md) | `labs/0101-what-intelligence-means/main.py` | Create a capability map for a familiar human task. |
    | 1.2 | [From Symbols to Statistics](0102-from-symbols-to-statistics.md) | `labs/0102-from-symbols-to-statistics/main.py` | Implement a tiny rule engine and document where it becomes brittle. |
    | 1.3 | [Search, Planning, and Decisions](0103-search-planning-and-decisions.md) | `labs/0103-search-planning-and-decisions/main.py` | Implement breadth-first search and A* on the same maze. |
    | 1.4 | [The Mathematics Engineers Need](0104-the-mathematics-engineers-need.md) | `labs/0104-the-mathematics-engineers-need/main.py` | Compute dot products, cosine similarity, softmax, and one gradient update by hand. |
    | 1.5 | [Learning and Generalization](0105-learning-and-generalization.md) | `labs/0105-learning-and-generalization/main.py` | Fit increasingly flexible models to a small noisy dataset and plot errors. |
    | 1.6 | [Engineering with Uncertainty](0106-engineering-with-uncertainty.md) | `labs/0106-engineering-with-uncertainty/main.py` | Design a decision policy for a high-cost false-positive scenario. |

??? abstract "Book 02 — Machine Learning Systems (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 2.1 | [Problems, Data, and Baselines](0201-problems-data-and-baselines.md) | `labs/0201-problems-data-and-baselines/main.py` | Create a dataset split that respects time and entity boundaries. |
    | 2.2 | [Supervised Learning](0202-supervised-learning.md) | `labs/0202-supervised-learning/main.py` | Implement linear and logistic regression before using a library. |
    | 2.3 | [Unsupervised and Representation Learning](0203-unsupervised-and-representation-learning.md) | `labs/0203-unsupervised-and-representation-learning/main.py` | Cluster a dataset, visualize it, and explain why clusters are not automatically meaningful categories. |
    | 2.4 | [Neural Networks](0204-neural-networks.md) | `labs/0204-neural-networks/main.py` | Train a small network and inspect gradients and learning curves. |
    | 2.5 | [Evaluation and Error Analysis](0205-evaluation-and-error-analysis.md) | `labs/0205-evaluation-and-error-analysis/main.py` | Write an error taxonomy and compare two models with confidence intervals. |
    | 2.6 | [The ML Lifecycle](0206-the-ml-lifecycle.md) | `labs/0206-the-ml-lifecycle/main.py` | Write a release checklist and a rollback plan for a prediction service. |

??? abstract "Book 03 — Language and Representation (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 3.1 | [Why Language Is Hard](0301-why-language-is-hard.md) | `labs/0301-why-language-is-hard/main.py` | Annotate ten ambiguous requests with possible interpretations and missing context. |
    | 3.2 | [Corpora and Text Pipelines](0302-corpora-and-text-pipelines.md) | `labs/0302-corpora-and-text-pipelines/main.py` | Build a normalization pipeline and test it on multilingual and adversarial text. |
    | 3.3 | [Tokenization](0303-tokenization.md) | `labs/0303-tokenization/main.py` | Write a toy byte-pair tokenizer and compare segmentations. |
    | 3.4 | [From Sparse Features to Embeddings](0304-from-sparse-features-to-embeddings.md) | `labs/0304-from-sparse-features-to-embeddings/main.py` | Implement TF–IDF and compare it with the included vector lab. |
    | 3.5 | [Similarity and Vector Search](0305-similarity-and-vector-search.md) | `labs/0305-similarity-and-vector-search/main.py` | Run the cosine and semantic-search labs, then add hybrid scoring. |
    | 3.6 | [Embedding Systems in Production](0306-embedding-systems-in-production.md) | `labs/0306-embedding-systems-in-production/main.py` | Create a retrieval evaluation set with realistic queries and hard negatives. |

??? abstract "Book 04 — Transformers and Foundation Models (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 4.1 | [Sequence Models Before Transformers](0401-sequence-models-before-transformers.md) | `labs/0401-sequence-models-before-transformers/main.py` | Train an n-gram model and inspect where local context fails. |
    | 4.2 | [Attention](0402-attention.md) | `labs/0402-attention/main.py` | Implement scaled dot-product attention and visualize weights. |
    | 4.3 | [The Transformer Block](0403-the-transformer-block.md) | `labs/0403-the-transformer-block/main.py` | Assemble one transformer block and test tensor shapes. |
    | 4.4 | [Training Foundation Models](0404-training-foundation-models.md) | `labs/0404-training-foundation-models/main.py` | Estimate compute and data requirements for a tiny language model. |
    | 4.5 | [Inference and Sampling](0405-inference-and-sampling.md) | `labs/0405-inference-and-sampling/main.py` | Build a sampling playground and compare decoding strategies. |
    | 4.6 | [Model Families and Selection](0406-model-families-and-selection.md) | `labs/0406-model-families-and-selection/main.py` | Benchmark candidate models on a task-specific dataset. |

??? abstract "Book 05 — Prompt and Context Engineering (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 5.1 | [Instructions That Work](0501-instructions-that-work.md) | `labs/0501-instructions-that-work/main.py` | Solve one task with weak and strong prompts and compare failures. |
    | 5.2 | [Structured Generation](0502-structured-generation.md) | `labs/0502-structured-generation/main.py` | Build an invoice extractor with schema validation and adversarial inputs. |
    | 5.3 | [Context Construction](0503-context-construction.md) | `labs/0503-context-construction/main.py` | Implement a context builder with explicit section budgets. |
    | 5.4 | [Conversation and Memory](0504-conversation-and-memory.md) | `labs/0504-conversation-and-memory/main.py` | Implement a conversation summarizer and memory scoring policy. |
    | 5.5 | [Context Failure and Security](0505-context-failure-and-security.md) | `labs/0505-context-failure-and-security/main.py` | Attack a context pipeline with malicious retrieved text and test defenses. |
    | 5.6 | [Prompt and Context Operations](0506-prompt-and-context-operations.md) | `labs/0506-prompt-and-context-operations/main.py` | Create a prompt change report with before/after evals. |

??? abstract "Book 06 — Knowledge and Retrieval Systems (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 6.1 | [Knowledge Outside the Model](0601-knowledge-outside-the-model.md) | `labs/0601-knowledge-outside-the-model/main.py` | Classify ten requirements by the correct knowledge mechanism. |
    | 6.2 | [Document Ingestion](0602-document-ingestion.md) | `labs/0602-document-ingestion/main.py` | Create an ingestion manifest and measure parse fidelity. |
    | 6.3 | [Retrieval](0603-retrieval.md) | `labs/0603-retrieval/main.py` | Implement lexical and vector baselines and calculate recall@k. |
    | 6.4 | [Ranking and Context Selection](0604-ranking-and-context-selection.md) | `labs/0604-ranking-and-context-selection/main.py` | Add reranking and measure quality versus latency. |
    | 6.5 | [RAG Generation and Citations](0605-rag-generation-and-citations.md) | `labs/0605-rag-generation-and-citations/main.py` | Build a citation validator that checks claim-to-source alignment. |
    | 6.6 | [Advanced and Enterprise RAG](0606-advanced-and-enterprise-rag.md) | `labs/0606-advanced-and-enterprise-rag/main.py` | Complete the enterprise RAG architecture studio and threat model. |

??? abstract "Book 07 — Reasoning and Tool Use (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 7.1 | [Reasoning as Search](0701-reasoning-as-search.md) | `labs/0701-reasoning-as-search/main.py` | Solve a constraint problem with explicit state search. |
    | 7.2 | [Planning](0702-planning.md) | `labs/0702-planning/main.py` | Build a planner that outputs a validated dependency graph. |
    | 7.3 | [Verification and Critique](0703-verification-and-critique.md) | `labs/0703-verification-and-critique/main.py` | Generate several candidates and select with an independent verifier. |
    | 7.4 | [Tools as Capability Boundaries](0704-tools-as-capability-boundaries.md) | `labs/0704-tools-as-capability-boundaries/main.py` | Wrap a read-only API as a typed tool and fuzz its arguments. |
    | 7.5 | [MCP and Integration Protocols](0705-mcp-and-integration-protocols.md) | `labs/0705-mcp-and-integration-protocols/main.py` | Implement a small local MCP server and test a hostile client request. |
    | 7.6 | [Reasoning-System Economics](0706-reasoning-system-economics.md) | `labs/0706-reasoning-system-economics/main.py` | Plot quality and cost for single-pass, best-of-N, and verifier loops. |

??? abstract "Book 08 — Agent Systems (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 8.1 | [Agent or Workflow?](0801-agent-or-workflow.md) | `labs/0801-agent-or-workflow/main.py` | Model the same task as a workflow and as an agent, then compare. |
    | 8.2 | [The Agent Loop](0802-the-agent-loop.md) | `labs/0802-the-agent-loop/main.py` | Extend the included agent loop with failures and checkpointing. |
    | 8.3 | [Agent Memory and Recovery](0803-agent-memory-and-recovery.md) | `labs/0803-agent-memory-and-recovery/main.py` | Persist and resume an interrupted multi-step run. |
    | 8.4 | [Agent Patterns](0804-agent-patterns.md) | `labs/0804-agent-patterns/main.py` | Implement two patterns and measure coordination overhead. |
    | 8.5 | [Multi-Agent Systems](0805-multi-agent-systems.md) | `labs/0805-multi-agent-systems/main.py` | Split a research task across workers and compare with one-agent parallel tools. |
    | 8.6 | [Operating Long-Running Agents](0806-operating-long-running-agents.md) | `labs/0806-operating-long-running-agents/main.py` | Create an SLO and runbook for a day-long agent workflow. |

??? abstract "Book 09 — AI Software and Product Engineering (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 9.1 | [Discovering the Right Problem](0901-discovering-the-right-problem.md) | `labs/0901-discovering-the-right-problem/main.py` | Write a problem brief with a non-AI alternative. |
    | 9.2 | [Specification-Driven Development](0902-specification-driven-development.md) | `labs/0902-specification-driven-development/main.py` | Write executable examples before implementation. |
    | 9.3 | [AI-Native Development Workflow](0903-ai-native-development-workflow.md) | `labs/0903-ai-native-development-workflow/main.py` | Run a bounded repository task with two assistants and compare review burden. |
    | 9.4 | [Testing AI Systems](0904-testing-ai-systems.md) | `labs/0904-testing-ai-systems/main.py` | Derive a test pyramid from an AI system architecture. |
    | 9.5 | [Human-Centered AI UX](0905-human-centered-ai-ux.md) | `labs/0905-human-centered-ai-ux/main.py` | Prototype a high-risk action flow with preview and approval. |
    | 9.6 | [Experiments, Adoption, and Value](0906-experiments-adoption-and-value.md) | `labs/0906-experiments-adoption-and-value/main.py` | Design a rollout with guardrails and decision thresholds. |

??? abstract "Book 10 — Evaluation, Safety, and Governance (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 10.1 | [Evaluation as Requirements](1001-evaluation-as-requirements.md) | `labs/1001-evaluation-as-requirements/main.py` | Write a 30-case evaluation set from real workflow risks. |
    | 10.2 | [Metrics and Human Judgment](1002-metrics-and-human-judgment.md) | `labs/1002-metrics-and-human-judgment/main.py` | Calibrate an automated judge against two human reviewers. |
    | 10.3 | [Evaluation by System Stage](1003-evaluation-by-system-stage.md) | `labs/1003-evaluation-by-system-stage/main.py` | Build a failure attribution matrix for a RAG system. |
    | 10.4 | [Security of AI Systems](1004-security-of-ai-systems.md) | `labs/1004-security-of-ai-systems/main.py` | Red-team a tool-enabled assistant and document mitigations. |
    | 10.5 | [Responsible AI and Risk](1005-responsible-ai-and-risk.md) | `labs/1005-responsible-ai-and-risk/main.py` | Write an impact assessment for a consequential use case. |
    | 10.6 | [Governance and Assurance](1006-governance-and-assurance.md) | `labs/1006-governance-and-assurance/main.py` | Create a lightweight governance operating model for a mid-size company. |

??? abstract "Book 11 — Training, Serving, and AI Operations (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 11.1 | [Choosing Adaptation](1101-choosing-adaptation.md) | `labs/1101-choosing-adaptation/main.py` | Create a decision table for ten adaptation scenarios. |
    | 11.2 | [Post-Training Methods](1102-post-training-methods.md) | `labs/1102-post-training-methods/main.py` | Fine-tune a small model and evaluate held-out behavior. |
    | 11.3 | [Dataset Engineering](1103-dataset-engineering.md) | `labs/1103-dataset-engineering/main.py` | Create a data card and contamination check for a small dataset. |
    | 11.4 | [Inference Infrastructure](1104-inference-infrastructure.md) | `labs/1104-inference-infrastructure/main.py` | Load-test a local model at several concurrency levels. |
    | 11.5 | [Deployment and Routing](1105-deployment-and-routing.md) | `labs/1105-deployment-and-routing/main.py` | Write a deployment ADR comparing hosted and self-hosted inference. |
    | 11.6 | [LLMOps](1106-llmops.md) | `labs/1106-llmops/main.py` | Instrument a request and inject provider, retrieval, and validation failures. |

??? abstract "Book 12 — Cloud and Enterprise AI Architecture (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 12.1 | [Enterprise AI Building Blocks](1201-enterprise-ai-building-blocks.md) | `labs/1201-enterprise-ai-building-blocks/main.py` | Draw a logical platform architecture before naming products. |
    | 12.2 | [Identity, Data, and Trust Boundaries](1202-identity-data-and-trust-boundaries.md) | `labs/1202-identity-data-and-trust-boundaries/main.py` | Threat-model an enterprise assistant across trust boundaries. |
    | 12.3 | [AWS Managed AI](1203-aws-managed-ai.md) | `labs/1203-aws-managed-ai/main.py` | Map the enterprise RAG design to AWS and estimate managed-service trade-offs. |
    | 12.4 | [Azure Managed AI](1204-azure-managed-ai.md) | `labs/1204-azure-managed-ai/main.py` | Map the same RAG design to Azure and compare identity integration. |
    | 12.5 | [Google Cloud and Portable Patterns](1205-google-cloud-and-portable-patterns.md) | `labs/1205-google-cloud-and-portable-patterns/main.py` | Map the design to Google Cloud and identify the migration boundary. |
    | 12.6 | [Enterprise Operating Model](1206-enterprise-operating-model.md) | `labs/1206-enterprise-operating-model/main.py` | Create a responsibility matrix and platform roadmap. |

??? abstract "Book 13 — Multimodal and Frontier Systems (6)"
    | § | Lab | Run | Practice objective |
    | --- | --- | --- | --- |
    | 13.1 | [Vision and Document Intelligence](1301-vision-and-document-intelligence.md) | `labs/1301-vision-and-document-intelligence/main.py` | Extract fields from documents and evaluate field and page-level accuracy. |
    | 13.2 | [Speech and Audio](1302-speech-and-audio.md) | `labs/1302-speech-and-audio/main.py` | Build a transcript pipeline with timestamps and confidence handling. |
    | 13.3 | [Image and Video Generation](1303-image-and-video-generation.md) | `labs/1303-image-and-video-generation/main.py` | Design an evaluation rubric for generated campaign assets. |
    | 13.4 | [Computer Use and Embodied Action](1304-computer-use-and-embodied-action.md) | `labs/1304-computer-use-and-embodied-action/main.py` | Design a safe browser task with confirmation and recovery. |
    | 13.5 | [Long Context, World Models, and Continual Learning](1305-long-context-world-models-and-continual-lea.md) | `labs/1305-long-context-world-models-and-continual-lea/main.py` | Compare a frontier method with retrieval, explicit state, or fine-tuning baselines. |
    | 13.6 | [How to Track the Frontier](1306-how-to-track-the-frontier.md) | `labs/1306-how-to-track-the-frontier/main.py` | Write a one-page frontier assessment with confidence levels. |

