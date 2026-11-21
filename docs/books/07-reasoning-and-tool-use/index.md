# Reasoning and Tool Use

Technical course 07 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Understand when inference-time search, planning, verification, and external tools improve task outcomes.

[Start the first lecture](01-reasoning-as-search.md){ .md-button .md-button--primary }
[Download the course notebook](../../assets/notebooks/07-reasoning-and-tool-use.ipynb){ .md-button download }

## Entry prerequisites

- Courses 01 and 04–06 or equivalent experience
- Search and planning
- Typed software interfaces

## Course outline

### Search and planning

- [01 · Reasoning as Search](01-reasoning-as-search.md)
- [02 · Planning](02-planning.md)

**Checkpoint**

Specify the goal, allowed actions, and stop condition for a small research workflow.

### Verification and tool contracts

- [03 · Verification and Critique](03-verification-and-critique.md)
- [04 · Tools as Capability Boundaries](04-tools-as-capability-boundaries.md)

**Checkpoint**

Pass a complete plan and then swap two dependent steps. Compare the verifier's decisions.

### Integrations and reasoning cost

- [05 · MCP and Integration Protocols](05-mcp-and-integration-protocols.md)
- [06 · Reasoning-System Economics](06-reasoning-system-economics.md)

**Checkpoint**

List the minimum tool fields and estimate the budget for one verification retry.

## Notebook workshop

Construct a plan that contains every step but places the final review too early. Compare it with the valid plan.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Build a research workflow with a planner, typed tools, evidence store, verifier, and bounded recovery.

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

- Yao et al. — ReAct
- Primary protocol specifications for the tool interfaces studied

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
