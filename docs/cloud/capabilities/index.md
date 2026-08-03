# Cloud Capability Guides

Provider-neutral capability pages with dated AWS, Azure, and Google Cloud mappings.

Verify product names, regions, limits, and pricing in official documentation before production use.

Expand a category or use search (`/`).

??? abstract "MLOps & pipelines (5)"
    | Capability | Summary |
    | --- | --- |
    | [Model Registry & Artifacts](model-registry.md) | Versioned model packages, metrics, and promotion workflow. |
    | [Feature Stores](feature-stores.md) | Consistent offline/online features for ML and ranking systems. |
    | [ML & LLM Pipelines](ml-pipelines.md) | Orchestrated train/eval/deploy workflows with reproducible steps. |
    | [Serverless AI Glue](serverless-ai.md) | Event-driven functions for lightweight AI orchestration. |
    | [Workflow Orchestration](workflow-orchestration.md) | Long-running AI workflows with retries and human steps. |

??? abstract "Models & inference (8)"
    | Capability | Summary |
    | --- | --- |
    | [Foundation Model APIs](foundation-model-apis.md) | Managed access to frontier and open models via HTTP with auth, quotas, and policy hooks. |
    | [Embedding APIs](embedding-apis.md) | Batch or online text embedding for retrieval, clustering, and classification. |
    | [Batch Inference](batch-inference.md) | Offline generation over large input sets with cost controls. |
    | [Real-Time Inference](real-time-inference.md) | Low-latency online model serving behind autoscaling endpoints. |
    | [Model Fine-Tuning Services](model-fine-tuning.md) | Managed post-training on private data with job tracking. |
    | [Container Model Serving](container-serving.md) | Packaged inference servers (vLLM, TGI, Triton) on Kubernetes or managed containers. |
    | [GPU Compute for Training & Inference](gpu-compute.md) | Accelerators for fine-tuning and self-hosted serving. |
    | [Edge & On-Device Inference](edge-inference.md) | Run smaller models close to users or devices. |

??? abstract "Platform, security & governance (9)"
    | Capability | Summary |
    | --- | --- |
    | [Identity for AI Workloads](identity-for-ai.md) | Authentication and authorization for humans, services, and agents. |
    | [Secrets & Key Management](secrets-management.md) | Store API keys, DB credentials, and encryption keys safely. |
    | [Private Networking for AI](private-networking.md) | VPC/VNet isolation, private endpoints, and egress control. |
    | [Observability for LLM Systems](observability-for-llms.md) | Traces, metrics, and logs for prompts, retrieval, tools, and outputs. |
    | [Content Safety Filters](content-safety-filters.md) | Policy enforcement on inputs and outputs. |
    | [API Gateways for AI Services](api-gateways.md) | Rate limits, auth, routing, and request logging at the edge. |
    | [Cost Management for AI](cost-management.md) | Budgets, tagging, and unit economics for tokens and GPUs. |
    | [Disaster Recovery for AI Services](disaster-recovery.md) | Backups, multi-region failover, and RPO/RTO for indexes and models. |
    | [Compliance & Audit for AI](compliance-audit.md) | Immutable logs, data retention, and evidence for regulators. |

??? abstract "Retrieval & data (4)"
    | Capability | Summary |
    | --- | --- |
    | [Vector Databases](vector-databases.md) | Approximate nearest-neighbor search at scale with metadata filtering. |
    | [Hybrid Search Services](hybrid-search-services.md) | Lexical + semantic ranking in one managed search product. |
    | [Document Ingestion Pipelines](document-ingestion.md) | Parse, chunk, enrich, and index documents with provenance. |
    | [Data Lake for AI Training & Eval](data-lake-for-ai.md) | Durable storage for corpora, eval sets, and experiment artifacts. |

