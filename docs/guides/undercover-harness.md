# UnderCover claims harness practicum

A traveler submits a carrier notice after a delay. An older policy required that notice alone, but the version in force on the incident date also requires an itinerary. The system prepares a document request for an adjuster to review. If policy lookup stalls, the claim pauses and the adjuster receives a clear status.

Ed Donner’s UnderCover uses a fictional travel insurer to teach agent harnesses, evaluation and observability, agentic RAG and MCP, durable human review, specialist agents, and cloud deployment. This practicum uses original fixtures and code to reproduce the design decisions locally. [Upstream project and curriculum](https://github.com/ed-donner/undercover)

[Download the Jupyter practicum](../assets/notebooks/undercover-harness.ipynb){ download } · [Open the lab source](https://github.com/mahalingam-inapp/aiebok/tree/main/labs/undercover-harness)

## Run the harness and its evals

From the AIeBOK repository root, use Python 3.10 or later with SQLite 3.35 or later. Install `requirements-notebooks.txt` for pytest and Jupyter.

```sh
python labs/undercover-harness/main.py demo
python labs/undercover-harness/main.py eval
python -m pytest labs/undercover-harness/test_lab.py -q
```

The demo records a local proposal and reports the revision awaiting review. Supply `--db /path/to/a/local.db` to retain the checkpoint across processes. The default store is in memory. The eval prints the observed route, policy, missing documents, per-case checks, and overall gate. The all-manual baseline passes 2 of 6 cases and the policy-aware harness passes 6 of 6. The fixtures demonstrate specified behaviors in a synthetic workload.

## Work through the decisions

1. **Intake and context.** Pass typed claim fields into a one-call policy tool. Choose the latest revision effective on the incident date. Use the source ID to explain which evidence was required and why. Unsupported categories or dates go to a human. Compare the historical and current delay fixtures before changing the tool boundary.
2. **Durable handoff.** Store the proposal before asking for approval. Reopen the database and approve the exact claim and revision as a simulated reviewer. Approval on an obsolete revision is rejected, and replay adds one note for that revision. A timed-out lookup returns a paused proposal and cannot produce an approved note. The note is local, and a person retains authority over correspondence, settlements, and coverage.
3. **Evaluation and observability.** Compare the same frozen inputs against both candidates. Score route, policy source, and required evidence separately. Block release if any critical case fails even when the aggregate looks good. Inspect the persisted state and command output for a failure trace. For a production adapter, add request ID, tool latency, failure class, policy version, and reviewer result to the trace while excluding claim document text.
4. **Specialists and proposed improvements.** Delegate read-only evidence and routing reviews to separate agents. Each gives the coordinator a policy ID, cited fields, and a recommended disposition. Let a coordinator reconcile disagreements before checkpointing. Propose policy or prompt changes offline, use development examples for iteration, run the frozen eval and replay tests, and record a human decision before promoting an artifact.
5. **Integration and release.** Put any replacement policy service behind the one-call adapter. In an MCP implementation, give the policy tool a typed read-only contract and keep approval in the trusted application. Add authenticated reviewer identity, claim-level access checks, a managed state store, timeout telemetry, a canary threshold, and a rollback drill before serving real claims. Treat remote effects as a separate delivery problem with their own idempotency key and reconciliation.

| Focus | Continue with |
| --- | --- |
| Harness and framework boundary | [Deploy and practice bounded agents](bounded-agent-assistant.md) · [Upstream harness brief](https://github.com/ed-donner/undercover/blob/main/labs/week1day5_product_HARNESS.md) |
| Agentic retrieval and context | [Enterprise RAG](enterprise-rag-end-to-end.md) · [Upstream context brief](https://github.com/ed-donner/undercover/blob/main/labs/week3day3_product_CONTEXT.md) |
| Durable state and specialist coordination | [Durable agent runtime](../courses/durable-agent-tool-runtime/index.md) · [Upstream durable brief](https://github.com/ed-donner/undercover/blob/main/labs/week2day3_product_DURABLE.md) · [Upstream swarm brief](https://github.com/ed-donner/undercover/blob/main/labs/week2day4_product_SWARM.md) |
| Evals, improvement, and readiness | [Eval-gated release](eval-gated-release.md) · [Upstream improvement brief](https://github.com/ed-donner/undercover/blob/main/labs/week2day5_product_IMPROVE.md) · [Upstream runtime brief](https://github.com/ed-donner/undercover/blob/main/labs/week3day4_product_RUNTIME.md) |
| Pilot and rollout ownership | [Forward Deployed AI Engineer path](../getting-started/learning-paths/forward-deployed-ai-engineer.md) · [Upstream security brief](https://github.com/ed-donner/undercover/blob/main/labs/week3day2_product_SECURE.md) |

## Practice with a coding agent

Use the [tool-specific implementation guides](coding-agents/index.md) to assign one read-only agent to trace version selection and another to trace SQLite retries. Ask them to return one defect hypothesis and a proposed test each. Have a single implementer add a boundary-day fixture or a regression test for denied approval. Rerun the eval and persistence tests. Keep tuning and held-out cases separate when comparing genuine improvements.
