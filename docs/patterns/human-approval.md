# Human Approval Gate

## Context

An AI proposes an action with financial, legal, safety, privacy, reputational, or irreversible consequences.

## Solution

Pause before execution and present the proposed action, target, evidence, uncertainty, side effects, and rollback options to an authorized reviewer. Bind approval to the exact action payload and expire it after changes or time.

## Failure modes

Approval fatigue, vague summaries, reviewers lacking context, stale approvals, and approval of one payload followed by execution of another.

## Engineering checks

- Risk-based rather than universal gating
- Identity and authorization of reviewer
- Immutable before/after payloads
- Time-bounded approval token
- Audit record and cancellation path
- Clear escalation when no reviewer responds
