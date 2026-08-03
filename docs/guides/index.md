# Build Guides

**13 end-to-end projects** from spec to evidence.

Each row lists the goal, phased deliverables, and primary book track.

Expand a theme or use search (`/`) for a specific guide.

??? abstract "Agents & automation (2)"
    | Guide | Goal | Phases | Book track |
    | --- | --- | --- | --- |
    | [Bounded Agent Assistant](bounded-agent-assistant.md) | Multi-step agent with typed tools, checkpoints, and approval. | State machine → Tool schemas → Human approval → Checkpoint store → Eval traces | `08-agent-systems` |
    | [Coding Agent Workspace](coding-agent-workspace.md) | Repo instructions, skills, and review gates for AI coding. | AGENTS.md → Skills → CI checks → Review rubric | `09-ai-software-and-product-engineering` |

??? abstract "Evaluation & safety (3)"
    | Guide | Goal | Phases | Book track |
    | --- | --- | --- | --- |
    | [Model Selection Harness](model-selection-harness.md) | Vendor-neutral benchmark report for task-specific model choice. | Task dataset → Candidate models → Cost/latency log → Selection ADR | `04-transformers-and-foundation-models` |
    | [Eval-Gated Release Pipeline](eval-gated-release.md) | CI harness with slices, thresholds, and rollback evidence. | Gold cases → Slice metrics → Release gate → Canary plan | `10-evaluation-safety-and-governance` |
    | [Red-Team Security Harness](red-team-security-harness.md) | Prompt injection and tool abuse tests in CI. | Attack set → Mitigations → Incident runbook | `10-evaluation-safety-and-governance` |

??? abstract "Product & context engineering (3)"
    | Guide | Goal | Phases | Book track |
    | --- | --- | --- | --- |
    | [Context Engine With Tests](context-engine-with-tests.md) | Versioned prompts, memory policy, token budgets, regression tests. | Context builder → Section budgets → Prompt versions → Eval dataset | `05-prompt-and-context-engineering` |
    | [Structured Extraction API](structured-extraction-api.md) | Schema-validated extraction behind a REST boundary. | JSON Schema → Validator → Repair loop → Adversarial tests | `05-prompt-and-context-engineering` |
    | [Spec-to-Production AI Feature](spec-to-production-feature.md) | Discovery through spec, implementation, eval, and rollout. | Problem brief → Executable spec → Feature flag rollout | `09-ai-software-and-product-engineering` |

??? abstract "Retrieval & knowledge (3)"
    | Guide | Goal | Phases | Book track |
    | --- | --- | --- | --- |
    | [Enterprise RAG End to End](enterprise-rag-end-to-end.md) | Ship authorized hybrid RAG with citations and stage evals. | Ingestion manifest → Hybrid retrieval → Reranker → Grounded generation → Citation validator → Release gate | `06-knowledge-and-retrieval-systems` |
    | [Hybrid Search Engine](hybrid-search-engine.md) | Lexical + dense retrieval with fusion and offline eval. | BM25 index → Vector index → RRF fusion → recall@k eval | `06-knowledge-and-retrieval-systems` |
    | [Multi-Tenant Retrieval Platform](multi-tenant-retrieval.md) | Tenant-scoped indexes, ACL filters, and audit logs. | Tenant metadata → AuthZ filters → Isolation tests | `12-cloud-and-enterprise-ai-architecture` |

??? abstract "Training & multimodal (2)"
    | Guide | Goal | Phases | Book track |
    | --- | --- | --- | --- |
    | [Fine-Tune and Serve a Small Model](fine-tune-and-serve.md) | LoRA adaptation with eval, registry, and rollback. | Data card → LoRA train → Eval report → Serving endpoint | `11-training-serving-and-ai-operations` |
    | [Multimodal Document Pipeline](multimodal-document-pipeline.md) | OCR, layout, extraction with provenance. | Parse/OCR → Field eval → Provenance metadata | `13-multimodal-and-frontier-systems` |

