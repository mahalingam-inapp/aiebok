# Forward-Deployed AI Engineer Capstone

A simulated venue operator wants a faster intake process for maintenance tickets. Its existing staff queue handles all routing. Deliver a shadow pilot that proposes routes, keeps restricted cases in the manual queue, and gives the operator a clear way to pause the pilot. Start from the [Customer Pilot Engineering workbook](../../courses/customer-pilot-engineering/index.md).

## Milestones

1. Document the workflow, actor, owner, median manual time, and acceptance thresholds. Clarify one ambiguous request by writing an assumption and how you would confirm it with the operator.
2. Map a versioned customer payload into a working integration. Add a new topic, a malformed input, a timeout, and a successful replay to the fixtures.
3. Compare both workflows on the same cases. Demo the exception path and show how the operator checks, pauses, and resumes the pilot.

## Rubric

| Evidence | Complete when |
|---|---|
| Discovery | The baseline, acceptance threshold, constraints, and owning person are explicit. |
| Implementation | A reviewer can run the adapter and see correct behavior for malformed, restricted, and repeated requests. |
| Acceptance and handoff | The recommendation follows the measurements and includes a smoke case, fallback, stop rule, and named owner. |

[Back to the learning path](forward-deployed-ai-engineer.md)
