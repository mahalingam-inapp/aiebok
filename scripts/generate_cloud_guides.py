"""Generate provider-neutral cloud capability guides with AWS/Azure/GCP mappings."""
from __future__ import annotations

from pathlib import Path

from catalog_helpers import _cell, classify_cloud_capability, render_grouped_table_catalog

ROOT = Path(__file__).resolve().parents[1]
CLOUD = ROOT / "docs" / "cloud"
CAPABILITIES = CLOUD / "capabilities"

# (slug, title, capability, aws, azure, gcp, when_to_use, pitfalls)
CAPABILITY_SPECS: list[tuple[str, str, str, str, str, str, str, str]] = [
    (
        "foundation-model-apis",
        "Foundation Model APIs",
        "Managed access to frontier and open models via HTTP with auth, quotas, and policy hooks.",
        "Amazon Bedrock",
        "Azure OpenAI / Azure AI Foundry model deployments",
        "Vertex AI Model Garden / Gemini API",
        "Use when you need fast time-to-value without operating GPU clusters.",
        "Vendor lock-in, region availability gaps, and opaque model version changes.",
    ),
    (
        "embedding-apis",
        "Embedding APIs",
        "Batch or online text embedding for retrieval, clustering, and classification.",
        "Bedrock Titan Embeddings, SageMaker endpoints",
        "Azure OpenAI embeddings, Azure AI Foundry",
        "Vertex text embedding models",
        "Use when retrieval quality depends on a maintained embedding model lifecycle.",
        "Dimension/version mismatches between index and query break retrieval silently.",
    ),
    (
        "vector-databases",
        "Vector Databases",
        "Approximate nearest-neighbor search at scale with metadata filtering.",
        "OpenSearch k-NN, Aurora pgvector, Bedrock Knowledge Bases",
        "Azure AI Search vector fields, Cosmos DB vector",
        "Vertex AI Vector Search, AlloyDB pgvector",
        "Use when dense retrieval must serve millions+ vectors with ACL filters.",
        "Recall/latency trade-offs and reindex cost during embedding model upgrades.",
    ),
    (
        "hybrid-search-services",
        "Hybrid Search Services",
        "Lexical + semantic ranking in one managed search product.",
        "OpenSearch hybrid queries, Kendra",
        "Azure AI Search semantic ranker + BM25",
        "Vertex AI Search",
        "Use for enterprise document search with identifiers and paraphrases.",
        "Semantic ranker latency and tuning complexity vs. self-managed RRF.",
    ),
    (
        "document-ingestion",
        "Document Ingestion Pipelines",
        "Parse, chunk, enrich, and index documents with provenance.",
        "Textract + Lambda + Step Functions, Bedrock KB ingestion",
        "Document Intelligence + Azure Functions + AI Search indexers",
        "Document AI + Cloud Functions + Vertex Search importers",
        "Use when source formats vary (PDF, HTML, tickets) and lineage matters.",
        "OCR errors and chunk-boundary mistakes propagate into RAG answers.",
    ),
    (
        "batch-inference",
        "Batch Inference",
        "Offline generation over large input sets with cost controls.",
        "Bedrock batch, SageMaker batch transform",
        "Azure ML batch endpoints",
        "Vertex batch prediction",
        "Use for backfills, eval runs, and nightly summarization jobs.",
        "Queue backlog monitoring and output validation at scale.",
    ),
    (
        "real-time-inference",
        "Real-Time Inference",
        "Low-latency online model serving behind autoscaling endpoints.",
        "SageMaker real-time endpoints, Bedrock InvokeModel",
        "Azure ML managed online endpoints, Azure OpenAI",
        "Vertex online prediction, Cloud Run + GPU",
        "Use for interactive assistants and synchronous APIs.",
        "Cold start, concurrency limits, and tail latency under burst traffic.",
    ),
    (
        "model-fine-tuning",
        "Model Fine-Tuning Services",
        "Managed post-training on private data with job tracking.",
        "Bedrock model customization, SageMaker training jobs",
        "Azure OpenAI fine-tuning, Azure ML fine-tune pipelines",
        "Vertex supervised fine-tuning / tuning jobs",
        "Use when prompt/RAG cannot meet style or format requirements.",
        "Overfitting small datasets and eval gaps before promotion.",
    ),
    (
        "model-registry",
        "Model Registry & Artifacts",
        "Versioned model packages, metrics, and promotion workflow.",
        "SageMaker Model Registry, ECR",
        "Azure ML registry, ACR",
        "Vertex Model Registry, Artifact Registry",
        "Use when multiple teams deploy models and rollback must be auditable.",
        "Registry drift if local experiments never get registered.",
    ),
    (
        "feature-stores",
        "Feature Stores",
        "Consistent offline/online features for ML and ranking systems.",
        "SageMaker Feature Store",
        "Azure ML feature store patterns",
        "Vertex Feature Store",
        "Use when training-serving skew breaks ranking or fraud models.",
        "Operational overhead unless feature reuse is organization-wide.",
    ),
    (
        "ml-pipelines",
        "ML & LLM Pipelines",
        "Orchestrated train/eval/deploy workflows with reproducible steps.",
        "SageMaker Pipelines, Step Functions",
        "Azure ML pipelines, MLflow",
        "Vertex Pipelines, Kubeflow on GKE",
        "Use when eval-gated promotion requires repeatable automation.",
        "Pipeline fragility if secrets, data paths, and versions are implicit.",
    ),
    (
        "serverless-ai",
        "Serverless AI Glue",
        "Event-driven functions for lightweight AI orchestration.",
        "Lambda + Bedrock",
        "Azure Functions + Azure OpenAI",
        "Cloud Functions / Cloud Run jobs + Vertex",
        "Use for webhooks, small transforms, and queue consumers.",
        "Timeout limits and cold starts for long LLM calls.",
    ),
    (
        "container-serving",
        "Container Model Serving",
        "Packaged inference servers (vLLM, TGI, Triton) on Kubernetes or managed containers.",
        "EKS + vLLM, ECS",
        "AKS + custom containers",
        "GKE + Cloud Run GPU",
        "Use when you need open-weight models, custom routing, or on-prem parity.",
        "You own patching, autoscaling, and GPU bin-packing efficiency.",
    ),
    (
        "gpu-compute",
        "GPU Compute for Training & Inference",
        "Accelerators for fine-tuning and self-hosted serving.",
        "EC2 P/G instances, SageMaker",
        "Azure NC/ND series, AmlCompute",
        "GCE A2/L4, Vertex training clusters",
        "Use when managed APIs are too expensive or too constrained.",
        "Capacity planning, spot interruption, and idle GPU cost.",
    ),
    (
        "identity-for-ai",
        "Identity for AI Workloads",
        "Authentication and authorization for humans, services, and agents.",
        "IAM roles, Identity Center, resource policies",
        "Microsoft Entra ID, managed identities",
        "Cloud IAM, workload identity",
        "Use before any production model or retrieval endpoint.",
        "Over-broad API keys shared across environments.",
    ),
    (
        "secrets-management",
        "Secrets & Key Management",
        "Store API keys, DB credentials, and encryption keys safely.",
        "Secrets Manager, KMS",
        "Key Vault",
        "Secret Manager, Cloud KMS",
        "Use for every external model provider credential.",
        "Secrets in environment variables logged by crash dumps.",
    ),
    (
        "private-networking",
        "Private Networking for AI",
        "VPC/VNet isolation, private endpoints, and egress control.",
        "VPC endpoints for Bedrock/SageMaker, PrivateLink",
        "Private endpoints for Azure OpenAI, VNet integration",
        "VPC-SC, Private Service Connect",
        "Use when data residency and exfiltration risk matter.",
        "Misconfigured DNS breaking managed service resolution.",
    ),
    (
        "observability-for-llms",
        "Observability for LLM Systems",
        "Traces, metrics, and logs for prompts, retrieval, tools, and outputs.",
        "CloudWatch, X-Ray, OpenTelemetry on Lambda/ECS",
        "Azure Monitor, Application Insights",
        "Cloud Logging, Cloud Trace, custom metrics",
        "Use from day one—debugging RAG without traces is guesswork.",
        "Logging raw prompts with PII into immutable log stores.",
    ),
    (
        "content-safety-filters",
        "Content Safety Filters",
        "Policy enforcement on inputs and outputs.",
        "Bedrock Guardrails, Comprehend moderation",
        "Azure AI Content Safety",
        "Vertex safety filters / Model Armor patterns",
        "Use for customer-facing assistants with abuse risk.",
        "False positives blocking legitimate enterprise content.",
    ),
    (
        "data-lake-for-ai",
        "Data Lake for AI Training & Eval",
        "Durable storage for corpora, eval sets, and experiment artifacts.",
        "S3 + Glue catalog",
        "ADLS Gen2 + Unity catalog patterns",
        "GCS + BigQuery external tables",
        "Use when datasets are large and shared across teams.",
        "Missing ACLs on buckets containing sensitive fine-tune data.",
    ),
    (
        "workflow-orchestration",
        "Workflow Orchestration",
        "Long-running AI workflows with retries and human steps.",
        "Step Functions, MWAA",
        "Logic Apps, Durable Functions",
        "Cloud Workflows, Composer",
        "Use for multi-step ingestion, eval, and approval flows.",
        "State machine sprawl without idempotent task design.",
    ),
    (
        "api-gateways",
        "API Gateways for AI Services",
        "Rate limits, auth, routing, and request logging at the edge.",
        "API Gateway, ALB",
        "API Management, Application Gateway",
        "Apigee, Cloud Endpoints",
        "Use when many clients hit shared model/retrieval backends.",
        "Gateway becomes a bottleneck without caching and routing rules.",
    ),
    (
        "cost-management",
        "Cost Management for AI",
        "Budgets, tagging, and unit economics for tokens and GPUs.",
        "Cost Explorer, budgets, SageMaker savings plans",
        "Cost Management + tags, reservations",
        "Billing budgets, CUDs, label-based chargeback",
        "Use when token spend is tied to product features.",
        "Untagged environments making per-feature cost invisible.",
    ),
    (
        "disaster-recovery",
        "Disaster Recovery for AI Services",
        "Backups, multi-region failover, and RPO/RTO for indexes and models.",
        "Cross-region S3 replication, multi-AZ endpoints",
        "Geo-redundant storage, paired regions",
        "Multi-region GCS, dual-region buckets",
        "Use when assistants are business-critical.",
        "Vector indexes rebuilt slowly without reindex runbooks.",
    ),
    (
        "compliance-audit",
        "Compliance & Audit for AI",
        "Immutable logs, data retention, and evidence for regulators.",
        "CloudTrail, Config, audit manager",
        "Activity logs, Purview",
        "Audit logs, Assured Workloads",
        "Use in regulated industries deploying copilots.",
        "Audit logs that omit retrieval document IDs.",
    ),
    (
        "edge-inference",
        "Edge & On-Device Inference",
        "Run smaller models close to users or devices.",
        "SageMaker Edge, IoT Greengrass patterns",
        "Azure IoT Edge, ONNX on devices",
        "Edge TPU / mobile deployment via TFLite",
        "Use for latency-sensitive or offline scenarios.",
        "Model size limits and update distribution complexity.",
    ),
]


def render_capability(spec: tuple[str, str, str, str, str, str, str, str]) -> str:
    slug, title, capability, aws, azure, gcp, when_to_use, pitfalls = spec
    return f"""# {title}

## Capability

{capability}

## When to use

{when_to_use}

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | {aws} |
| Azure | {azure} |
| Google Cloud | {gcp} |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

{pitfalls}

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
"""


def generate() -> int:
    CAPABILITIES.mkdir(parents=True, exist_ok=True)
    groups: dict[str, list[list[str]]] = {}
    for spec in CAPABILITY_SPECS:
        slug = spec[0]
        (CAPABILITIES / f"{slug}.md").write_text(render_capability(spec), encoding="utf-8")
        groups.setdefault(classify_cloud_capability(slug), []).append(
            [f"[{spec[1]}]({slug}.md)", _cell(spec[2], 120)]
        )

    index = render_grouped_table_catalog(
        "Cloud Capability Guides",
        [
            "Provider-neutral capability pages with dated AWS, Azure, and Google Cloud mappings.",
            "",
            "Verify product names, regions, limits, and pricing in official documentation before production use.",
            "",
            "Expand a category or use search (`/`).",
        ],
        groups,
        ["Capability", "Summary"],
    )
    (CAPABILITIES / "index.md").write_text(index, encoding="utf-8")

    # Update cloud index with link to capabilities catalog
    index = (CLOUD / "index.md").read_text(encoding="utf-8")
    if "capabilities/index.md" not in index:
        index = index.rstrip() + "\n\n## Capability guides\n\nSee the [capability guide catalog](capabilities/index.md) for 26 provider-neutral pages.\n"
        (CLOUD / "index.md").write_text(index, encoding="utf-8")

    return len(CAPABILITY_SPECS)


def main() -> None:
    count = generate()
    print(f"Generated {count} cloud capability guides.")


if __name__ == "__main__":
    main()
