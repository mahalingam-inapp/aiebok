# OWASP Top 10 for LLM Applications

## Citation

OWASP. *OWASP Top 10 for LLM Applications.* 2024. [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## One-sentence contribution

Taxonomy of LLM application risks including injection.

## Problem

Teams lacked a shared vocabulary for prompt injection and jailbreak attacks.

## Prior art

Ad hoc lists of attacks in blog posts without systematic coverage.

## Core idea

Taxonomies classify attacks by mechanism—direct injection, indirect via retrieval, tool abuse, multimodal payloads—and map mitigations.

## Evidence

- OWASP LLM Top 10 and industry red-team catalogs consolidate common patterns.
- Enterprises adopt taxonomies for test case libraries.

## Limitations

- Taxonomies lag novel attacks
- Mitigations are rarely complete

## Lasting impact

Standardized red-team planning and CI attack suites.

## Reproduction exercise

Map 10 known attacks to OWASP categories; add any missing coverage to your eval suite.

## Related chapters

- [04 Security Of Ai Systems](../../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md)
- [05 Context Failure And Security](../../books/05-prompt-and-context-engineering/05-context-failure-and-security.md)

## Related concepts

- [Prompt Injection](../../concepts/cards/prompt-injection.md)
- [Adversarial Tests](../../concepts/cards/adversarial-tests.md)
- [Threat Modeling](../../concepts/cards/threat-modeling.md)
