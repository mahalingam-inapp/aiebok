# KA 17 — Multimodal AI

## Purpose

Compose text, vision, audio, and documents.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Vision and Document Intelligence** — read [chapter](../books/13-multimodal-and-frontier-systems/01-vision-and-document-intelligence.md), run [lab](../labs/1301-vision-and-document-intelligence.md), lesson page [L-17-multimodal-01](../lessons/17-multimodal-01.md)
2. **Speech and Audio** — read [chapter](../books/13-multimodal-and-frontier-systems/02-speech-and-audio.md), run [lab](../labs/1302-speech-and-audio.md), lesson page [L-17-multimodal-02](../lessons/17-multimodal-02.md)
3. **Image and Video Generation** — read [chapter](../books/13-multimodal-and-frontier-systems/03-image-and-video-generation.md), run [lab](../labs/1303-image-and-video-generation.md), lesson page [L-17-multimodal-03](../lessons/17-multimodal-03.md)
4. **Computer Use and Embodied Action** — read [chapter](../books/13-multimodal-and-frontier-systems/04-computer-use-and-embodied-action.md), run [lab](../labs/1304-computer-use-and-embodied-action.md), lesson page [L-17-multimodal-04](../lessons/17-multimodal-04.md)
5. **Long Context, World Models, and Continual Learning** — read [chapter](../books/13-multimodal-and-frontier-systems/05-long-context-world-models-and-continual-learning.md), run [lab](../labs/1305-long-context-world-models-and-continual-lea.md), lesson page [L-17-multimodal-05](../lessons/17-multimodal-05.md)
6. **How to Track the Frontier** — read [chapter](../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md), run [lab](../labs/1306-how-to-track-the-frontier.md), lesson page [L-17-multimodal-06](../lessons/17-multimodal-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Vision and Document Intelligence | Preserve spatial structure and provenance when converting visual documents into model cont | Apply without baseline or slice eval |
| Speech and Audio | Audio systems are temporal, identity-sensitive, and latency-constrained. | Apply without baseline or slice eval |
| Image and Video Generation | Generative quality includes controllability, consistency, provenance, safety, and workflow | Apply without baseline or slice eval |
| Computer Use and Embodied Action | Acting through interfaces adds uncertainty and irreversible side effects to ordinary agent | Apply without baseline or slice eval |

## Core topics

- [OCR](../concepts/cards/ocr.md)
- [vision encoders](../concepts/cards/vision-encoders.md)
- [provenance](../concepts/cards/provenance.md)

## Guided resources

- Primary book: [Multimodal and Frontier Systems](../books/13-multimodal-and-frontier-systems/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Build document intelligence pipeline with provenance.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
