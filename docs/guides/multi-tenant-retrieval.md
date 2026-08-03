# Multi-Tenant Retrieval Platform

## Goal

Tenant-scoped indexes, ACL filters, and audit logs.

## Overview

Build retrieval infrastructure where every query is scoped to tenant identity, authorization filters, and auditable access. Isolation tests prove one tenant cannot retrieve another's documents.

## Architecture

Tenant metadata lives in a registry mapping tenant_id to index partitions, ACL policies, and quotas. The query API authenticates callers, resolves tenant context, and applies AuthZ filters before retrieval executes. Audit logs record query text hash, tenant, result ids, and principal. Isolation tests run cross-tenant negative cases in CI.

## Prerequisites

Complete the matching [guided book](../books/12-cloud-and-enterprise-ai-architecture/index.md) and related labs.

## Build phases

### 1. Tenant metadata

**Goal:** Model tenants, index partitions, and policy attachments.

**Steps:**
   - Define tenant record: tenant_id, plan, index_prefix, default_acl.
   - Register document sources with tenant_id and resource-level acl_tags.
   - Enforce quota fields: max documents, queries per minute.
   - Expose admin CLI to create tenants and attach policies.

**Acceptance:**
   - Every indexed chunk carries tenant_id and acl_tags in metadata.
   - Unknown tenant_id rejected at API boundary with 404.
   - Tenant registry changes audited with actor and timestamp.

   **Commands:**

   ```bash
   python tenants/register.py --tenant acme --plan standard
   python tenants/show.py --tenant acme
   ```
### 2. AuthZ filters

**Goal:** Apply authorization before search executes.

**Steps:**
   - Resolve principal roles and permitted acl_tags from token claims.
   - Inject mandatory filters into BM25 and vector queries.
   - Deny queries that specify tenant_id mismatched with token.
   - Return empty results rather than partial leaks on filter parse errors.

**Acceptance:**
   - Queries never return chunks whose acl_tags are not permitted for principal.
   - Cross-tenant filter injection attempts fail closed.
   - Filter application logged per request for audit.

   **Commands:**

   ```bash
   python search/query.py --tenant acme --token tests/fixtures/user.jwt --query "policy"
   python -m pytest tests/test_authz_filters.py -q
   ```
### 3. Isolation tests

**Goal:** Prove tenant boundaries with automated negative tests.

**Steps:**
   - Seed two tenants with overlapping topic but distinct documents.
   - Run queries as tenant A principal; assert zero results from tenant B.
   - Attempt filter bypass via crafted query parameters and document ids.
   - Include audit log assertion: no B chunk ids in A's access log.

**Acceptance:**
   - 100% pass on cross-tenant leakage test matrix.
   - Bypass attempts produce 403 or empty results, never mixed-tenant hits.
   - Isolation tests run on every index rebuild in CI.

   **Commands:**

   ```bash
   python -m pytest tests/test_tenant_isolation.py -q
   python eval/isolation_matrix.py --tenants acme,beta --out reports/isolation.json
   ```

## Troubleshooting

- Leaked chunk via mis-tagged ingestion: validate tenant_id at ingest and reject mismatched source paths.
- Empty results for valid users: debug acl_tag intersection between principal and document tags.
- Audit logs too verbose: log chunk id hashes and query fingerprint, not full document text.
- Index sharing across tenants: prefer partition prefixes or separate collections over filter-only isolation.

## Related patterns

- [Multi Tenant Retrieval](../patterns/multi-tenant-retrieval.md)
- [Metadata Filter First](../patterns/metadata-filter-first.md)
- [Human Approval Gate](../patterns/human-approval-gate.md)

## Related labs

- [1202 Identity Data And Trust Boundaries](../labs/1202-identity-data-and-trust-boundaries.md)
- [1201 Enterprise Ai Building Blocks](../labs/1201-enterprise-ai-building-blocks.md)
- [0606 Advanced And Enterprise Rag](../labs/0606-advanced-and-enterprise-rag.md)
- [1006 Governance And Assurance](../labs/1006-governance-and-assurance.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
