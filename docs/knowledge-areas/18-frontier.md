# KA 18 — Frontier AI

## Purpose

Evaluate emerging capabilities with evidence.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Long Context, World Models, and Continual Learning** — read [chapter](../books/13-multimodal-and-frontier-systems/05-long-context-world-models-and-continual-learning.md), run [lab](../labs/1305-long-context-world-models-and-continual-lea.md), lesson page [L-18-frontier-01](../lessons/18-frontier-01.md)
2. **How to Track the Frontier** — read [chapter](../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md), run [lab](../labs/1306-how-to-track-the-frontier.md), lesson page [L-18-frontier-02](../lessons/18-frontier-02.md)
3. **Vision and Document Intelligence** — read [chapter](../books/13-multimodal-and-frontier-systems/01-vision-and-document-intelligence.md), run [lab](../labs/1301-vision-and-document-intelligence.md), lesson page [L-18-frontier-03](../lessons/18-frontier-03.md)
4. **Speech and Audio** — read [chapter](../books/13-multimodal-and-frontier-systems/02-speech-and-audio.md), run [lab](../labs/1302-speech-and-audio.md), lesson page [L-18-frontier-04](../lessons/18-frontier-04.md)
5. **Image and Video Generation** — read [chapter](../books/13-multimodal-and-frontier-systems/03-image-and-video-generation.md), run [lab](../labs/1303-image-and-video-generation.md), lesson page [L-18-frontier-05](../lessons/18-frontier-05.md)
6. **Computer Use and Embodied Action** — read [chapter](../books/13-multimodal-and-frontier-systems/04-computer-use-and-embodied-action.md), run [lab](../labs/1304-computer-use-and-embodied-action.md), lesson page [L-18-frontier-06](../lessons/18-frontier-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Long Context, World Models, and Continual Learning | Frontier techniques should be decomposed into representation, memory, search, learning, an | Apply without baseline or slice eval |
| How to Track the Frontier | The durable skill is evaluating claims and mapping new mechanisms to established principle | Apply without baseline or slice eval |
| Vision and Document Intelligence | Preserve spatial structure and provenance when converting visual documents into model cont | Apply without baseline or slice eval |
| Speech and Audio | Audio systems are temporal, identity-sensitive, and latency-constrained. | Apply without baseline or slice eval |

## Core topics

- [reproduction](../concepts/cards/reproduction.md)
- [benchmarks](../concepts/cards/benchmarks.md)
- [ablations](../concepts/cards/ablations.md)

## Guided resources

- Primary book: [Multimodal and Frontier Systems](../books/13-multimodal-and-frontier-systems/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Reproduce one claim versus strong baselines.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
