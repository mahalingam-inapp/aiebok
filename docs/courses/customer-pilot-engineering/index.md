# Customer Pilot Engineering

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Turn an ambiguous customer request into an accepted, observable pilot with an operator handoff.

[Start the first lecture](01-discovery-and-pilot-acceptance.md){ .md-button .md-button--primary .study-start data-course="customer-pilot-engineering" }

## Practice case · Meet the people who fix the building

Inez is embedded with a facilities contractor. Earlier demos suggested AI could route almost every maintenance issue. The shift lead shows her unclassified tickets, a legacy form, and a queue that must keep working during a network failure. They agree on a limited trial with manual ownership intact.

This fictional case continues through the lectures.

For a documented comparison, read [What changed for customer support workers](../../casebook/support-assistants.md).

## Entry prerequisites

Python, JSON, and familiarity with a model-backed application and product discovery.

## Course outline

### Discover and integrate

- [01 · Discovery and pilot acceptance](01-discovery-and-pilot-acceptance.md){ .study-lecture data-lecture="01-discovery-and-pilot-acceptance.md" } — Translate a request into a workflow, baseline, and measurable acceptance criteria.
- [02 · Map a customer data contract](02-map-a-customer-data-contract.md){ .study-lecture data-lecture="02-map-a-customer-data-contract.md" } — Normalize a source payload and publish a versioned integration boundary.

### Evaluate and hand off

- [03 · Shadow acceptance and integration failures](03-shadow-acceptance-and-integration-failures.md){ .study-lecture data-lecture="03-shadow-acceptance-and-integration-failures.md" } — Exercise normal, ambiguous, restricted, and unavailable-dependency cases before live use.
- [04 · Rollout, operator handoff and stop rules](04-rollout-operator-handoff-and-stop-rules.md){ .study-lecture data-lecture="04-rollout-operator-handoff-and-stop-rules.md" } — Write a release recommendation grounded in measured outcomes and assign an operational owner.

## Workbook

[Download the workbook](../../assets/notebooks/customer-pilot-engineering.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Deliver a pilot for a simulated facilities team. Include the workflow baseline, an adapter, a replay-safe intake path, acceptance evidence, and a handoff.

**How to check your project**

Show an accepted request, unverifiable evidence, a temporary dependency failure, and a replay. Record the scope, pilot owner, stop rule, and what the customer needs to operate it.

## Further study

- [UnderCover claims harness practicum](../../guides/undercover-harness.md)
- [Donner’s UnderCover repository](https://github.com/ed-donner/undercover)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
