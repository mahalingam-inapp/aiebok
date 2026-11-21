# Cloud and Enterprise AI Architecture

Technical course 12 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Design secure, governed, resilient AI platforms and map them to managed services without losing vendor-neutral reasoning.

[Start the first lecture](01-enterprise-ai-building-blocks.md){ .md-button .md-button--primary }
[Download the course notebook](../../assets/notebooks/12-cloud-and-enterprise-ai-architecture.ipynb){ .md-button download }

## Entry prerequisites

- Courses 05–11 or equivalent experience
- Cloud and identity fundamentals
- Architecture documentation

## Course outline

### Architecture and trust boundaries

- [01 · Enterprise AI Building Blocks](01-enterprise-ai-building-blocks.md)
- [02 · Identity, Data, and Trust Boundaries](02-identity-data-and-trust-boundaries.md)

**Checkpoint**

Sketch the logical model, search, compute, and identity capabilities before picking services.

### AWS and Azure implementations

- [03 · AWS Managed AI](03-aws-managed-ai.md)
- [04 · Azure Managed AI](04-azure-managed-ai.md)

**Checkpoint**

Compare the AWS and Azure mapping. Identify which identity and data controls require verification.

### Portability and operating model

- [05 · Google Cloud and Portable Patterns](05-google-cloud-and-portable-patterns.md)
- [06 · Enterprise Operating Model](06-enterprise-operating-model.md)

**Checkpoint**

Map the same design to Google Cloud and assign an owner for each operational control.

## Notebook workshop

Compare the logical keys in the provider maps. Identify a capability that would need its own abstraction and conformance test.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Produce a multi-cloud-capable enterprise AI reference architecture and five architecture decision records.

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

- Official AWS, Azure, and Google Cloud architecture and service documentation
- Organization security and data-governance standards

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
