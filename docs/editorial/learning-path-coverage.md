# Learning Path Coverage Review

Reviewed 21 November 2026. The review followed the required courses and compared the stated completion outcomes with the lectures, hands-on material, and project evidence learners could produce. A runnable demonstration counts as practice. A path outcome requires a project brief and observable completion criteria.

## Conclusions by path

| Path | Gap found | Evidence learners can produce now |
|---|---|---|
| [AI for Everyone](../getting-started/learning-paths/00-ai-for-everyone.md) | Literacy and drafting exercises gave learners little practice comparing results with the original workflow. | A reviewed draft, safe-use checklist, and a three-case scorecard covering accuracy, review time, and when to stop. |
| [AI for Managers and Product Leaders](../getting-started/learning-paths/01-product-technical-leader.md) | The path covered pilot scope and launch decisions. Learners needed a way to connect those decisions with a small body of evidence. | A baseline comparison, quality and review criteria, and a pilot recommendation with an owner and a measurable pause condition. |
| [Software Engineer Building with AI](../getting-started/learning-paths/06-software-engineer.md) | Separate demonstrations explained structured outputs, RAG, and evals. The path needed one implementation connecting them. | A grounded assistant with response validation, permission-filtered retrieval, fallback, and separate retrieval and answer measurements. An optional local model runs through the same harness. |
| [Coding-Agent Specialist](../getting-started/learning-paths/02-coding-agent-specialist.md) | The theory covered agent loops, typed tools, and specification. Learners needed to observe a failed proposal and an approval applied to a specific revision. | A bounded formatter-change harness with regression evidence, approval, stale-revision handling, and an idempotent replay check. |
| [AI Systems Architect](../getting-started/learning-paths/03-software-architect.md) | Architecture studios and cloud maps supported design. The path lacked repeatable release and recovery evidence from a running service. | A versioned local endpoint, durable telemetry, canary decision, and rollback smoke test alongside an architecture decision and runbook. |
| [ML Engineer](../getting-started/learning-paths/04-ml-engineer.md) | The core had important training concepts and a rank-one toy exercise. It needed a complete dataset-to-artifact experiment with held-out decision evidence. | A trained text classifier with group-disjoint splits, a validation-selected threshold, slice and cost metrics, a serialized artifact, and serving and rollback evidence. |
| [AI Engineer](../getting-started/learning-paths/05-ai-engineer.md) | The capstone expected integration across the whole lifecycle. The core workbooks offered limited intermediate practice doing that integration. | Four project practicums precede a capstone that combines baseline comparisons, access and grounding checks, and demonstrated operations. |

## External benchmarks

- Donner's LLM Engineering repository links setup, progressively larger builds, and a final project that combines different model and application components. AIeBOK adopts the progression from a small baseline to integrated, tested behavior in the application and model practicums. [LLM Engineering](https://github.com/ed-donner/llm_engineering) · [Final project framework](https://github.com/ed-donner/llm_engineering/blob/main/week8/deal_agent_framework.py)
- The agents and UnderCover repositories offer framework comparisons, staged builds, and design work on harnesses, evals, observability, and human review. AIeBOK uses the same learning goals to motivate a supervised, deterministic change exercise and repeatable regression and replay cases. [Agents](https://github.com/ed-donner/agents) · [UnderCover](https://github.com/ed-donner/undercover)
- The production repository and Alex capstone emphasize real deployment steps, infrastructure troubleshooting, and staged validation. AIeBOK brings the release mechanics into a runnable local service with a clear transfer exercise to hosted infrastructure. [AI in Production](https://github.com/ed-donner/production) · [Alex capstone plan](https://github.com/ed-donner/alex/blob/main/gameplan.md)
- Choosing the Right LLM provides a focused companion for comparing model choices. AIeBOK extends comparison to both an engineering evaluation harness and a paper-based scorecard that includes review cost. [Choosing the Right LLM](https://github.com/ed-donner/choose_llm)

These repositories are further-study references. The AIeBOK lectures, code, and fixtures are original and grouped by project and learning objective.

## Scope of the practical coverage

The required workbooks are reproducible with small, synthetic data. The local service teaches release and recovery mechanics. Managed-cloud infrastructure provisioning, multi-framework implementations, and foundation-model fine-tuning on accelerators remain deeper study. Use the core [training course](../books/11-training-serving-and-ai-operations/index.md), [enterprise architecture course](../books/12-cloud-and-enterprise-ai-architecture/index.md), and [multimodal course](../books/13-multimodal-and-frontier-systems/index.md) alongside the external project guides for those extensions.
