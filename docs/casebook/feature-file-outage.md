# A feature file takes down a healthy service

## What Cloudflare reported

In November 2025, Cloudflare described a failure that affected core network traffic. An upstream change caused a generated feature file to grow beyond the size downstream software could accept. The file propagated across the network. Cloudflare stopped distributing it and restored an earlier version. [Cloudflare incident report, 18 November 2025](https://blog.cloudflare.com/18-november-2025-outage/)

## What if the model never changed?

Imagine an AI support service whose access filters depend on a generated index descriptor. The model endpoint is healthy and its version is unchanged. An updated descriptor crosses a consumer limit and several teams lose access. An incident review that looks only for a new model version will miss the dependency that changed.

Add rollout gates around generated artifacts. Give the consumer a schema and size contract, run the same validation before publishing, and expose a small test cohort first. Track artifact version at the request boundary. When alarms begin, establish the earliest observable change and compare a stable cohort with an affected cohort.

Your incident commander is at a decision point. An older compatible artifact is available, but the exact cause remains uncertain. Write down what is observed, who can restore the older artifact, and which user-facing test would prove that recovery worked. Keep the cause hypothesis separate from the immediate action. Reopen the evidence once traffic is stable and assign a person to test that class of failure in the next release.

[Deploy and Operate an AI Service](../courses/operating-ai-services/index.md) · [AI Reliability and Release Engineering](../courses/ai-reliability-release/index.md) · [Casebook](index.md)
