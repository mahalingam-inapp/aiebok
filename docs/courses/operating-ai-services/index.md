# Deploy and Operate an AI Service

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Exercise a versioned service, fallback, canary, telemetry, and rollback in a local deployment.

[Start the first lecture](01-serve-a-versioned-endpoint.md){ .md-button .md-button--primary }

## Entry prerequisites

Python, HTTP, and evaluation basics. Familiarity with model-backed applications is helpful.

## Course outline

### Package and observe

- [01 · Serve a versioned endpoint](01-serve-a-versioned-endpoint.md) — Expose a local HTTP endpoint with explicit version and health behavior.
- [02 · Fallback, trace fields and durable telemetry](02-fallback-trace-fields-and-durable-telemetry.md) — Record provider failures and successful fallback without storing request text.

### Release and recover

- [03 · Canary evaluation and rollout decisions](03-canary-evaluation-and-rollout-decisions.md) — Compare gated evidence and identify a canary that must pause.
- [04 · Rollback and production handoff](04-rollback-and-production-handoff.md) — Persist a version-pointer rollback and verify it through a local HTTP smoke test.

## Workbook

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Ship a local service and a release packet with an architecture decision, version routing, a smoke test, measured canary evidence, a telemetry schema, and an operator runbook.

**How to check your project**

Demonstrate repeatable smoke requests, fallback under injected provider failure, a blocked canary, and a saved rollback decision. Describe how health checks, secrets, and telemetry would map to a selected hosting platform.

## Further study

- [Cloud and Enterprise AI Architecture](../../books/12-cloud-and-enterprise-ai-architecture/index.md)
- [Evaluation-gated release guide](../../guides/eval-gated-release.md)
- [Staged cloud deployment from the Alex capstone](https://github.com/ed-donner/alex/blob/main/gameplan.md)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
