# Authorization

**Purpose:** Reference card for **authorization** used across AIEBOK books and knowledge areas.

## Core explanation

Authorization ensures retrieved and acted-upon data respects user permissions—not just authentication. RAG without authZ leaks restricted documents into answers.

## Example

An employee should not retrieve executive compensation docs via semantic search without role checks.

## When to use

Use for any system combining untrusted user content, tools, or external retrieval.

## When not to use

Do not treat a single prompt rule as sufficient without tests and monitoring.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run queries as low-privilege users and confirm zero restricted chunks appear in context.

## Common failure modes

- Prompt injection via retrieved or pasted content
- Tool abuse exfiltrating secrets
- Missing authorization on retrieval paths

## Trade-offs

No mechanism is universal. Compare authorization against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Adaptive Rag](../../concepts/cards/adaptive-rag.md)
- [Audit](../../concepts/cards/audit.md)
- [Context Poisoning](../../concepts/cards/context-poisoning.md)
- [Data Residency](../../concepts/cards/data-residency.md)

## Related chapters

- [05 Context Failure And Security](../../books/05-prompt-and-context-engineering/05-context-failure-and-security.md)
- [06 Advanced And Enterprise Rag](../../books/06-knowledge-and-retrieval-systems/06-advanced-and-enterprise-rag.md)
- [02 Identity Data And Trust Boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
