# KA 05 — Prompt & Context

## Purpose

Engineer reliable inputs, state, and outputs.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Instructions That Work** — read [chapter](../books/05-prompt-and-context-engineering/01-instructions-that-work.md), run [lab](../labs/0501-instructions-that-work.md), lesson page [L-05-prompt-context-01](../lessons/05-prompt-context-01.md)
2. **Structured Generation** — read [chapter](../books/05-prompt-and-context-engineering/02-structured-generation.md), run [lab](../labs/0502-structured-generation.md), lesson page [L-05-prompt-context-02](../lessons/05-prompt-context-02.md)
3. **Context Construction** — read [chapter](../books/05-prompt-and-context-engineering/03-context-construction.md), run [lab](../labs/0503-context-construction.md), lesson page [L-05-prompt-context-03](../lessons/05-prompt-context-03.md)
4. **Conversation and Memory** — read [chapter](../books/05-prompt-and-context-engineering/04-conversation-and-memory.md), run [lab](../labs/0504-conversation-and-memory.md), lesson page [L-05-prompt-context-04](../lessons/05-prompt-context-04.md)
5. **Context Failure and Security** — read [chapter](../books/05-prompt-and-context-engineering/05-context-failure-and-security.md), run [lab](../labs/0505-context-failure-and-security.md), lesson page [L-05-prompt-context-05](../lessons/05-prompt-context-05.md)
6. **Prompt and Context Operations** — read [chapter](../books/05-prompt-and-context-engineering/06-prompt-and-context-operations.md), run [lab](../labs/0506-prompt-and-context-operations.md), lesson page [L-05-prompt-context-06](../lessons/05-prompt-context-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Instructions That Work | A prompt is an interface specification for probabilistic behavior. | Apply without baseline or slice eval |
| Structured Generation | Free-form model output must become validated data before software trusts it. | Apply without baseline or slice eval |
| Context Construction | Context is a scarce, ordered working set—not a dumping ground. | Apply without baseline or slice eval |
| Conversation and Memory | Memory is selected state reconstructed for the next decision. | Apply without baseline or slice eval |

## Core topics

- [JSON Schema](../concepts/cards/json-schema.md)
- [prompt injection](../concepts/cards/prompt-injection.md)
- [context windows](../concepts/cards/context-windows.md)

## Guided resources

- Primary book: [Prompt and Context Engineering](../books/05-prompt-and-context-engineering/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Build a context engine with regression tests.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
