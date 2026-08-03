# Cloud Capability Guides

**26 provider-neutral capability pages** with dated AWS, Azure, and Google Cloud mappings.

Verify product names, regions, limits, and pricing in official documentation before production use.

Each row summarizes the capability, when to use it, and typical provider services.

Expand a category or use search (`/`).

??? abstract "MLOps & pipelines (5)"
    | Capability | Summary | When to use | Provider mapping |
    | --- | --- | --- | --- |
    | [Model Registry & Artifacts](model-registry.md) | Versioned model packages, metrics, and promotion workflow. | Use when multiple teams deploy models and rollback must be auditable. | AWS: SageMaker Model Registry, ECR · Azure: Azure ML registry, ACR · GCP: Vertex Model Registry, Artifact Registry |
    | [Feature Stores](feature-stores.md) | Consistent offline/online features for ML and ranking systems. | Use when training-serving skew breaks ranking or fraud models. | AWS: SageMaker Feature Store · Azure: Azure ML feature store patterns · GCP: Vertex Feature Store |
    | [ML & LLM Pipelines](ml-pipelines.md) | Orchestrated train/eval/deploy workflows with reproducible steps. | Use when eval-gated promotion requires repeatable automation. | AWS: SageMaker Pipelines, Step Functions · Azure: Azure ML pipelines, MLflow · GCP: Vertex Pipelines, Kubeflow on GKE |
    | [Serverless AI Glue](serverless-ai.md) | Event-driven functions for lightweight AI orchestration. | Use for webhooks, small transforms, and queue consumers. | AWS: Lambda + Bedrock · Azure: Azure Functions + Azure OpenAI · GCP: Cloud Functions / Cloud Run jobs + Vertex |
    | [Workflow Orchestration](workflow-orchestration.md) | Long-running AI workflows with retries and human steps. | Use for multi-step ingestion, eval, and approval flows. | AWS: Step Functions, MWAA · Azure: Logic Apps, Durable Functions · GCP: Cloud Workflows, Composer |

??? abstract "Models & inference (8)"
    | Capability | Summary | When to use | Provider mapping |
    | --- | --- | --- | --- |
    | [Foundation Model APIs](foundation-model-apis.md) | Managed access to frontier and open models via HTTP with auth, quotas, and policy hooks. | Use when you need fast time-to-value without operating GPU clusters. | AWS: Amazon Bedrock · Azure: Azure OpenAI / Azure AI Foundry model deployments · GCP: Vertex AI Model Garden / Gemini API |
    | [Embedding APIs](embedding-apis.md) | Batch or online text embedding for retrieval, clustering, and classification. | Use when retrieval quality depends on a maintained embedding model lifecycle. | AWS: Bedrock Titan Embeddings, SageMaker endpoints · Azure: Azure OpenAI embeddings, Azure AI Foundry · GCP: Vertex text embedding models |
    | [Batch Inference](batch-inference.md) | Offline generation over large input sets with cost controls. | Use for backfills, eval runs, and nightly summarization jobs. | AWS: Bedrock batch, SageMaker batch transform · Azure: Azure ML batch endpoints · GCP: Vertex batch prediction |
    | [Real-Time Inference](real-time-inference.md) | Low-latency online model serving behind autoscaling endpoints. | Use for interactive assistants and synchronous APIs. | AWS: SageMaker real-time endpoints, Bedrock InvokeModel · Azure: Azure ML managed online endpoints, Azure OpenAI · GCP: Vertex online prediction, Cloud Run + GPU |
    | [Model Fine-Tuning Services](model-fine-tuning.md) | Managed post-training on private data with job tracking. | Use when prompt/RAG cannot meet style or format requirements. | AWS: Bedrock model customization, SageMaker training jobs · Azure: Azure OpenAI fine-tuning, Azure ML fine-tune pipelines · GCP: Vertex supervised fine-tuning / tuning jobs |
    | [Container Model Serving](container-serving.md) | Packaged inference servers (vLLM, TGI, Triton) on Kubernetes or managed containers. | Use when you need open-weight models, custom routing, or on-prem parity. | AWS: EKS + vLLM, ECS · Azure: AKS + custom containers · GCP: GKE + Cloud Run GPU |
    | [GPU Compute for Training & Inference](gpu-compute.md) | Accelerators for fine-tuning and self-hosted serving. | Use when managed APIs are too expensive or too constrained. | AWS: EC2 P/G instances, SageMaker · Azure: Azure NC/ND series, AmlCompute · GCP: GCE A2/L4, Vertex training clusters |
    | [Edge & On-Device Inference](edge-inference.md) | Run smaller models close to users or devices. | Use for latency-sensitive or offline scenarios. | AWS: SageMaker Edge, IoT Greengrass patterns · Azure: Azure IoT Edge, ONNX on devices · GCP: Edge TPU / mobile deployment via TFLite |

??? abstract "Platform, security & governance (9)"
    | Capability | Summary | When to use | Provider mapping |
    | --- | --- | --- | --- |
    | [Identity for AI Workloads](identity-for-ai.md) | Authentication and authorization for humans, services, and agents. | Use before any production model or retrieval endpoint. | AWS: IAM roles, Identity Center, resource policies · Azure: Microsoft Entra ID, managed identities · GCP: Cloud IAM, workload identity |
    | [Secrets & Key Management](secrets-management.md) | Store API keys, DB credentials, and encryption keys safely. | Use for every external model provider credential. | AWS: Secrets Manager, KMS · Azure: Key Vault · GCP: Secret Manager, Cloud KMS |
    | [Private Networking for AI](private-networking.md) | VPC/VNet isolation, private endpoints, and egress control. | Use when data residency and exfiltration risk matter. | AWS: VPC endpoints for Bedrock/SageMaker, PrivateLink · Azure: Private endpoints for Azure OpenAI, VNet integration · GCP: VPC-SC, Private Service Connect |
    | [Observability for LLM Systems](observability-for-llms.md) | Traces, metrics, and logs for prompts, retrieval, tools, and outputs. | Use from day one—debugging RAG without traces is guesswork. | AWS: CloudWatch, X-Ray, OpenTelemetry on Lambda/ECS · Azure: Azure Monitor, Application Insights · GCP: Cloud Logging, Cloud Trace, custom metrics |
    | [Content Safety Filters](content-safety-filters.md) | Policy enforcement on inputs and outputs. | Use for customer-facing assistants with abuse risk. | AWS: Bedrock Guardrails, Comprehend moderation · Azure: Azure AI Content Safety · GCP: Vertex safety filters / Model Armor patterns |
    | [API Gateways for AI Services](api-gateways.md) | Rate limits, auth, routing, and request logging at the edge. | Use when many clients hit shared model/retrieval backends. | AWS: API Gateway, ALB · Azure: API Management, Application Gateway · GCP: Apigee, Cloud Endpoints |
    | [Cost Management for AI](cost-management.md) | Budgets, tagging, and unit economics for tokens and GPUs. | Use when token spend is tied to product features. | AWS: Cost Explorer, budgets, SageMaker savings plans · Azure: Cost Management + tags, reservations · GCP: Billing budgets, CUDs, label-based chargeback |
    | [Disaster Recovery for AI Services](disaster-recovery.md) | Backups, multi-region failover, and RPO/RTO for indexes and models. | Use when assistants are business-critical. | AWS: Cross-region S3 replication, multi-AZ endpoints · Azure: Geo-redundant storage, paired regions · GCP: Multi-region GCS, dual-region buckets |
    | [Compliance & Audit for AI](compliance-audit.md) | Immutable logs, data retention, and evidence for regulators. | Use in regulated industries deploying copilots. | AWS: CloudTrail, Config, audit manager · Azure: Activity logs, Purview · GCP: Audit logs, Assured Workloads |

??? abstract "Retrieval & data (4)"
    | Capability | Summary | When to use | Provider mapping |
    | --- | --- | --- | --- |
    | [Vector Databases](vector-databases.md) | Approximate nearest-neighbor search at scale with metadata filtering. | Use when dense retrieval must serve millions+ vectors with ACL filters. | AWS: OpenSearch k-NN, Aurora pgvector, Bedrock Knowledge Bases · Azure: Azure AI Search vector fields, Cosmos DB vector · GCP: Vertex AI Vector Search, AlloyDB pgvector |
    | [Hybrid Search Services](hybrid-search-services.md) | Lexical + semantic ranking in one managed search product. | Use for enterprise document search with identifiers and paraphrases. | AWS: OpenSearch hybrid queries, Kendra · Azure: Azure AI Search semantic ranker + BM25 · GCP: Vertex AI Search |
    | [Document Ingestion Pipelines](document-ingestion.md) | Parse, chunk, enrich, and index documents with provenance. | Use when source formats vary (PDF, HTML, tickets) and lineage matters. | AWS: Textract + Lambda + Step Functions, Bedrock KB ingestion · Azure: Document Intelligence + Azure Functions + AI Search indexers · GCP: Document AI + Cloud Functions + Vertex Search importers |
    | [Data Lake for AI Training & Eval](data-lake-for-ai.md) | Durable storage for corpora, eval sets, and experiment artifacts. | Use when datasets are large and shared across teams. | AWS: S3 + Glue catalog · Azure: ADLS Gen2 + Unity catalog patterns · GCP: GCS + BigQuery external tables |

