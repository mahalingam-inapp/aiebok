# AI Software and Product Engineering

Technical course 09 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Use specifications, evaluations, secure development practices, and product discovery to deliver useful AI features.

[Start the first lecture](01-discovering-the-right-problem.md){ .md-button .md-button--primary .study-start data-course="09-ai-software-and-product-engineering" }
[Download the course notebook](../../assets/notebooks/09-ai-software-and-product-engineering.ipynb){ .md-button download }

## Practice case · The pull request nobody has time to review

Nadia’s scheduling team is asked to use a coding assistant to clear its backlog. The first demonstration creates a large change quickly. Reviewers now spend longer understanding the diffs and correcting edge cases. Nadia needs evidence that the entire workflow is getting better.

This fictional case continues through the lectures.

For a documented comparison, read [Two studies measured two different coding jobs](../../casebook/coding-productivity.md).

## Entry prerequisites

- Courses 05–08 or equivalent experience
- Software testing
- Product discovery basics

## Course outline

### Discovery and specifications

- [01 · Discovering the Right Problem](01-discovering-the-right-problem.md){ .study-lecture data-lecture="01-discovering-the-right-problem.md" }
- [02 · Specification-Driven Development](02-specification-driven-development.md){ .study-lecture data-lecture="02-specification-driven-development.md" }

**Checkpoint**

Write a baseline workflow and one measurable acceptance case before adding a model.

### Development and testing

- [03 · AI-Native Development Workflow](03-ai-native-development-workflow.md){ .study-lecture data-lecture="03-ai-native-development-workflow.md" }
- [04 · Testing AI Systems](04-testing-ai-systems.md){ .study-lecture data-lecture="04-testing-ai-systems.md" }

**Checkpoint**

Turn a rejection behavior into a test that fails for a plausible but incorrect answer.

### Experience and value

- [05 · Human-Centered AI UX](05-human-centered-ai-ux.md){ .study-lecture data-lecture="05-human-centered-ai-ux.md" }
- [06 · Experiments, Adoption, and Value](06-experiments-adoption-and-value.md){ .study-lecture data-lecture="06-experiments-adoption-and-value.md" }

**Checkpoint**

Name a user-facing fallback and a guardrail metric for a pilot.

## Notebook workshop

Add an out-of-scope case. Decide what an acceptable handoff looks like and check that the demonstration follows it.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Take one AI feature from problem discovery through a specification-driven implementation and evidence-based release.

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

- Repository contribution and test documentation
- Architecture Decision Record guidance and product experiment literature

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
