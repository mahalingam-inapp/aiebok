# Two zones and one deletion boundary

## What Google Cloud reported

In May 2024, Google Cloud reported that an earlier provisioning error gave one of UniSuper’s private clouds a fixed term. The environment was then deleted when that term expired. The affected environment spanned two zones. Google Cloud says backups in separate object storage were unaffected and helped the teams restore service. [Google Cloud incident and recovery account](https://cloud.google.com/blog/products/infrastructure/details-of-google-cloud-gcve-incident)

## Think through who can still work

A zone failure and a shared deletion are different events from the operator’s point of view. In the first, another zone may still serve requests. In the second, redundancy across zones can disappear with the environment it depends on. For a recovery drill, draw a line around what an administrative action can affect. Then check which data and credentials are reachable outside that line.

Say you operate a policy assistant with current documents, user permissions, a vector index, and model evaluation artifacts. The whole serving environment disappears. Decide what to restore first.

- Restore authoritative documents and permissions before allowing open retrieval.
- Verify one request for each permission boundary on a fresh environment.
- Use an approved substitute such as read-only policy search while rebuilding the index, if that substitute meets the organization’s access requirements.

A restore test should end when the user can safely complete a real task again. Give a named operator permission to run it and set a timer. That reveals gaps that checking for a recent backup cannot.

[Cloud and Enterprise AI Architecture](../books/12-cloud-and-enterprise-ai-architecture/index.md) · [Casebook](index.md)
