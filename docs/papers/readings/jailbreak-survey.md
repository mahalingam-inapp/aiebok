# Survey of Attacks and Defenses in LLM Security (representative)

## Citation

Various. *Survey of Attacks and Defenses in LLM Security (representative).* 2024. [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## One-sentence contribution

Catalog of prompt injection and tool abuse patterns.

## Problem

Aligned LLMs remain vulnerable to adversarial inputs that bypass safety training—prompt injections, jailbreaks, and tool abuse in production systems. Engineers deploying LLM applications lack a systematic catalog of attack patterns and mitigations.

## Prior art

Ad hoc red-teaming produced scattered examples (DAN prompts, base64 encoding). Academic adversarial ML focused on classification attacks, not generative LLM behavior. No industry-standard taxonomy connected attacks to defenses.

## Core idea

Representative surveys (OWASP Top 10 for LLM Applications, Perez & Ribeiro, Greshake et al.) catalog attack categories: direct prompt injection (override system instructions), indirect injection (malicious content in retrieved documents or tool outputs), jailbreak templates (role-play, encoding, multi-turn escalation), model extraction, denial of service, and supply chain attacks. Defenses include input/output filtering, instruction hierarchy, tool sandboxing, privilege separation, and continuous red-teaming. The core principle: treat LLM inputs as untrusted and layer defenses.

## Evidence

- OWASP LLM Top 10 (2023–2025): prompt injection ranked #1 risk across industry surveys.
- Indirect injection demonstrated on RAG systems: malicious web pages in retrieved context override assistant behavior (Greshake et al.).
- Automated jailbreak discovery (PAIR, TAP) finds bypasses faster than manual red-teaming.
- No single defense eliminates all attacks—defense-in-depth required.

## Limitations

- Arms race: new jailbreaks appear faster than defenses are deployed.
- Eval coverage gaps—no benchmark captures all attack categories.
- Defenses often reduce utility (over-refusal, latency from filtering).
- Tool abuse and multi-agent attack surfaces are still poorly understood.

## Lasting impact

OWASP LLM Top 10 and related surveys became the starting checklist for LLM security reviews in enterprise deployments. They shaped CI red-team harnesses and responsible-AI governance frameworks.

## Reproduction exercise

Build a 20-case attack set covering 4 categories (direct injection, indirect via RAG, jailbreak template, tool abuse). Run against your assistant with and without input filtering. Score success rate per category. Document which attacks bypass which defenses.

## Related chapters

- [04 Security Of Ai Systems](../../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md)
- [05 Context Failure And Security](../../books/05-prompt-and-context-engineering/05-context-failure-and-security.md)
- [04 Tools As Capability Boundaries](../../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md)

## Related concepts

- [Prompt Injection](../../concepts/cards/prompt-injection.md)
- [Tool Abuse](../../concepts/cards/tool-abuse.md)
- [Threat Modeling](../../concepts/cards/threat-modeling.md)
