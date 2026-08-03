# KA 12 — Evaluation, Safety & Security

## Purpose

Measure and constrain behavior.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Evaluation as Requirements** — read [chapter](../books/10-evaluation-safety-and-governance/01-evaluation-as-requirements.md), run [lab](../labs/1001-evaluation-as-requirements.md), lesson page [L-12-evaluation-safety-01](../lessons/12-evaluation-safety-01.md)
2. **Metrics and Human Judgment** — read [chapter](../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md), run [lab](../labs/1002-metrics-and-human-judgment.md), lesson page [L-12-evaluation-safety-02](../lessons/12-evaluation-safety-02.md)
3. **Evaluation by System Stage** — read [chapter](../books/10-evaluation-safety-and-governance/03-evaluation-by-system-stage.md), run [lab](../labs/1003-evaluation-by-system-stage.md), lesson page [L-12-evaluation-safety-03](../lessons/12-evaluation-safety-03.md)
4. **Security of AI Systems** — read [chapter](../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md), run [lab](../labs/1004-security-of-ai-systems.md), lesson page [L-12-evaluation-safety-04](../lessons/12-evaluation-safety-04.md)
5. **Responsible AI and Risk** — read [chapter](../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md), run [lab](../labs/1005-responsible-ai-and-risk.md), lesson page [L-12-evaluation-safety-05](../lessons/12-evaluation-safety-05.md)
6. **Governance and Assurance** — read [chapter](../books/10-evaluation-safety-and-governance/06-governance-and-assurance.md), run [lab](../labs/1006-governance-and-assurance.md), lesson page [L-12-evaluation-safety-06](../lessons/12-evaluation-safety-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Evaluation as Requirements | Evaluation is executable requirements for uncertain behavior. | Apply without baseline or slice eval |
| Metrics and Human Judgment | Every metric encodes a theory of quality; validate that theory against real decisions. | Apply without baseline or slice eval |
| Evaluation by System Stage | Stage-specific evaluation makes failures diagnosable and improvements attributable. | Apply without baseline or slice eval |
| Security of AI Systems | Treat models and retrieved content as untrusted components inside ordinary security bounda | Apply without baseline or slice eval |

## Core topics

- [rubrics](../concepts/cards/rubrics.md)
- [slices](../concepts/cards/slices.md)
- [prompt injection](../concepts/cards/prompt-injection.md)

## Guided resources

- Primary book: [Evaluation, Safety, and Governance](../books/10-evaluation-safety-and-governance/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Build eval and red-team package for release gates.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
