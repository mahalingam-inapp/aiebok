# Evaluation, Safety, and Governance

Technical course 10 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Build evidence that AI systems meet task, safety, security, compliance, and business requirements.

[Start the first lecture](01-evaluation-as-requirements.md){ .md-button .md-button--primary }
[Download the course notebook](../../assets/notebooks/10-evaluation-safety-and-governance.ipynb){ .md-button download }

## Entry prerequisites

- Test experience with model-backed systems, or Courses 05–09
- Statistics intuition
- Threat-model basics

## Course outline

### Requirements and judgment

- [01 · Evaluation as Requirements](01-evaluation-as-requirements.md)
- [02 · Metrics and Human Judgment](02-metrics-and-human-judgment.md)

**Checkpoint**

Choose an error whose cost justifies a separate release criterion and define who labels it.

### Stage evaluation and security

- [03 · Evaluation by System Stage](03-evaluation-by-system-stage.md)
- [04 · Security of AI Systems](04-security-of-ai-systems.md)

**Checkpoint**

Write separate checks for retrieving evidence and for using it correctly in the final response.

### Risk and governance

- [05 · Responsible AI and Risk](05-responsible-ai-and-risk.md)
- [06 · Governance and Assurance](06-governance-and-assurance.md)

**Checkpoint**

State who may approve release and what evidence or failure blocks it.

## Notebook workshop

Compare aggregate accuracy with accuracy on a critical slice. Add passing general cases and observe why the critical gate should remain closed.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Create an evaluation and assurance package with datasets, rubrics, adversarial tests, release gates, and governance evidence.

Submit a short specification, an implementation or architecture, evidence from a baseline comparison, and one architecture decision record. Include one example that fails and explain how you would handle it.

## Suggested three-week schedule

- **Week 1:** Complete the first section and its checkpoint.
- **Week 2:** Complete the second section and start the project.
- **Week 3:** Complete the final section and the notebook workshop. Evaluate and review the project.

## Assessment

| Evidence | Weight |
|---|---:|
| Lecture knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Course project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- NIST AI Risk Management Framework
- OWASP guidance for LLM applications
- Task-specific evaluation research

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
