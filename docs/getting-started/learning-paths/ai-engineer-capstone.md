# AI Engineer Capstone

Build a small, source-grounded assistant for an internal policy or support workflow. Use public or synthetic documents and cap the first version to one user group and one workflow. The assistant should return an answer with citations, decline when evidence is insufficient, and provide a clear handoff. A local implementation is sufficient.

Reuse the response and evaluation contract from [Build and Evaluate a Model-Backed Application](../../courses/model-backed-applications/index.md) and the version routing and smoke checks from [Deploy and Operate an AI Service](../../courses/operating-ai-services/index.md). Use your own workflow, cases, and release thresholds.

## Milestones

1. **Specify and baseline.** Define the user, intended outcome, allowed data, and failure tolerance. Create at least 20 labeled cases that include answerable, unanswerable, ambiguous, and access-restricted requests. Implement a simple keyword-search baseline and freeze the cases before iteration.
2. **Build and evaluate.** Run the candidate and baseline on the same cases. Report retrieval and answer results separately. Inspect citation correctness, abstention, and access decisions. Include two labeled failures and explain a design decision made from the evidence.
3. **Demonstrate operations.** Record request latency and component versions. Run a small canary with predeclared release thresholds. Simulate a failing dependency, show the fallback, and run a smoke test after rolling back. Record the release decision and its owner.

## Submit

- A runnable project with dependency and setup instructions
- The specification, cases, and reproducible baseline and candidate results
- A one-page architecture decision record and a brief operations runbook
- A short demo covering a correct answer, one failure, and the fallback

## Review rubric

| Area | Completion evidence |
|---|---|
| Problem framing | The workflow, baseline, access boundary, and release criteria are explicit. |
| Reproducibility | Another learner can run the system and evaluation from the submitted instructions. |
| Quality and safety | Citations, abstention, and access are measured separately. Restricted content is never surfaced in the labeled cases. |
| Operations | The demo shows fallback behavior, a canary decision, and a passing smoke test after rollback. The runbook identifies how and when to roll back. |
| Architecture defense | The decision record uses measured results to justify one trade-off against a simpler design. |

[AI Engineer learning path](05-ai-engineer.md)
