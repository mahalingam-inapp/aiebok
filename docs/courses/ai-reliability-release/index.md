# AI Reliability and Release Engineering

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Operate a staged model release using service objectives, trace diagnosis, and an incident exercise.

[Start the first lecture](01-service-objectives-and-error-budget-burn.md){ .md-button .md-button--primary .study-start data-course="ai-reliability-release" }

## Practice case · Four timeouts in a small rollout

Olivia is on call for an assistant that summarizes support tickets. A candidate version is handling a small cohort while the stable version serves everyone else. Several pilot requests are late and some need the manual queue. The rest of the system looks healthy.

This fictional case continues through the lectures.

For a documented comparison, read [A feature file takes down a healthy service](../../casebook/feature-file-outage.md).

## Entry prerequisites

HTTP, basic event metrics, and Deploy and Operate an AI Service or equivalent.

## Course outline

### Define and observe reliability

- [01 · Service objectives and error-budget burn](01-service-objectives-and-error-budget-burn.md){ .study-lecture data-lecture="01-service-objectives-and-error-budget-burn.md" } — Define a good request and calculate reliability and budget burn over a bounded window.
- [02 · Stage traces and failure localization](02-stage-traces-and-failure-localization.md){ .study-lecture data-lecture="02-stage-traces-and-failure-localization.md" } — Use structured events to locate the earliest divergence between candidate and baseline.

### Release and recover

- [03 · Canary cohorts and staged gates](03-canary-cohorts-and-staged-gates.md){ .study-lecture data-lecture="03-canary-cohorts-and-staged-gates.md" } — Use predeclared coverage, burn, latency, and cost thresholds to approve or hold a rollout.
- [04 · Rollback verification and incident review](04-rollback-verification-and-incident-review.md){ .study-lecture data-lecture="04-rollback-verification-and-incident-review.md" } — Restore stable routing, run a smoke check, and assemble a factual incident timeline.

## Workbook

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Run a staged rollout with an injected dependency failure. Diagnose from traces, roll back, and submit an incident review with follow-up owners.

**How to check your project**

Specify user-facing service objectives, compute error-budget burn, apply canary gates by cohort, and verify after rollback that the baseline serves successfully.

## Further study

- [Donner’s AI in Production](https://github.com/ed-donner/production)
- [Alex production capstone](https://github.com/ed-donner/alex/blob/main/gameplan.md)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
