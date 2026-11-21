# Foundations of Intelligence

Technical course 01 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Understand intelligence as search, learning, representation, decision-making, and feedback before studying language models.

[Start the first lecture](01-what-intelligence-means.md){ .md-button .md-button--primary .study-start data-course="01-foundations-of-intelligence" }
[Download the course notebook](../../assets/notebooks/01-foundations-of-intelligence.ipynb){ .md-button download }

## Practice case · The alarms at 2 a.m.

Priya is the overnight dispatcher for a regional transit agency. Last Friday, two reports about an elevator outage went into a low-priority queue. A separate report sounded urgent because it was written in all caps. The operations lead wants a smarter dispatcher. Priya wants disabled riders to reach a working station and wants the on-call engineer to receive fewer false alarms.

This fictional case continues through the lectures.

For a documented comparison, read [What changed for customer support workers](../../casebook/support-assistants.md).

## Entry prerequisites

- No AI background required
- Comfort reading simple Python
- Basic algebra

## Course outline

### Goals and representations

- [01 · What Intelligence Means](01-what-intelligence-means.md){ .study-lecture data-lecture="01-what-intelligence-means.md" }
- [02 · From Symbols to Statistics](02-from-symbols-to-statistics.md){ .study-lecture data-lecture="02-from-symbols-to-statistics.md" }

**Checkpoint**

Write a support-routing goal and identify an example where a fixed keyword rule misroutes a request.

### Search and mathematics

- [03 · Search, Planning, and Decisions](03-search-planning-and-decisions.md){ .study-lecture data-lecture="03-search-planning-and-decisions.md" }
- [04 · The Mathematics Engineers Need](04-the-mathematics-engineers-need.md){ .study-lecture data-lecture="04-the-mathematics-engineers-need.md" }

**Checkpoint**

Trace BFS and A* on the same grid. Record both path length and states expanded.

### Learning and decisions

- [05 · Learning and Generalization](05-learning-and-generalization.md){ .study-lecture data-lecture="05-learning-and-generalization.md" }
- [06 · Engineering with Uncertainty](06-engineering-with-uncertainty.md){ .study-lecture data-lecture="06-engineering-with-uncertainty.md" }

**Checkpoint**

Assign separate costs to a wrong route and a human review. Specify when review becomes cheaper.

## Notebook workshop

Cover the route with a blocked cell and compare the path returned by each search. Record when the heuristic saves work.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Build and compare a rule-based solver, a search-based solver, and a learned predictor for one bounded problem.

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

- Russell & Norvig — Artificial Intelligence: A Modern Approach
- Sutton & Barto — Reinforcement Learning: An Introduction

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
