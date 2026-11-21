# Why GitHub paused queued work

## What GitHub reported

In October 2018, a network partition and database failover left GitHub displaying some stale or inconsistent information. The response team paused webhook delivery and Pages builds while it restored a consistent database state. When processing resumed, some queued webhook events had already expired. The team paused that processing again and adjusted the retention window. [GitHub’s post-incident analysis](https://github.blog/news-insights/company-news/oct21-post-incident-analysis/)

## Bring the choice to a workflow with human approval

Imagine a fictional service that sends schedule notices after a coordinator approves changes. The service recovers after a database failure. The queue contains a notice for an approved change, a notice whose approval is still pending, and a duplicate of a notice already sent. The live system is healthy enough to take new requests. Should the worker process the whole backlog?

Review each pending effect in the context of its durable record. An approved notice should still reference the same change and be within its useful time window. A pending notice waits for review. A duplicate should return the previous outcome where the delivery contract allows it. An expired notice may need a new decision rather than a retry.

Decide how people will see the state. A coordinator who sees “processing” all afternoon may send the notice manually. Messages such as “approved and queued,” “delivery uncertain,” and “expired, needs review” let that person choose the appropriate next step. Define the checks that permit replay and the role responsible for ambiguous outcomes before restarting the queue.

[Reasoning and Tool Use](../books/07-reasoning-and-tool-use/index.md) · [Agent Systems](../books/08-agent-systems/index.md) · [Durable Agent Runtime and MCP](../courses/durable-agent-tool-runtime/index.md) · [Casebook](index.md)
