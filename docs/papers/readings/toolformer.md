# Toolformer: Language Models Can Teach Themselves to Use Tools

## Citation

Schick et al.. *Toolformer: Language Models Can Teach Themselves to Use Tools.* 2023. [https://arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761)

## One-sentence contribution

Self-supervised API call insertion during pretraining.

## Problem

LMs cannot natively perform arithmetic, look up current facts, or call external APIs—they hallucinate calculations and stale information. Teaching tool use typically required expensive human annotation of API call demonstrations.

## Prior art

ReAct and WebGPT used prompting or RL with human demonstrations. API-bank and similar datasets required manual curation. Fine-tuning on tool demonstrations was limited by dataset size and API coverage.

## Core idea

Schick et al. proposed self-supervised tool learning: start with a few human-written API call examples, then have the LM generate candidate API calls on unlabeled text. Filter candidates by whether the API result reduces perplexity on subsequent tokens—keeping only calls that measurably help prediction. Iteratively expand the training set with self-generated examples. APIs (calculator, QA, search, translation, calendar) are invoked via special tokens inserted inline during text generation.

## Evidence

- LM quality (perplexity) maintained while gaining tool-use capability—no degradation on standard LM benchmarks.
- Math QA (GSM8K subset): improved accuracy with calculator API vs. LM-only.
- Knowledge-intensive QA: search API reduced hallucination on date/entity questions.
- Self-supervised pipeline generated 1000s of training examples from ~12 human seeds.

## Limitations

- Limited to pre-defined API set—no dynamic tool discovery.
- Perplexity-based filtering is a proxy; some useful calls may be filtered out.
- Inference requires API execution infrastructure at each call site.
- Does not handle multi-step tool chains or error recovery robustly.

## Lasting impact

Toolformer demonstrated that tool use can be learned with minimal supervision, influencing function-calling fine-tuning in GPT-4, Claude, and open models. The self-supervised API learning pattern appears in modern agent training pipelines.

## Reproduction exercise

Fine-tune a 1–3B model on 200 examples of inline calculator calls (question → Calculate[expr] → result → answer). Evaluate on 30 arithmetic word problems vs. base model. Measure accuracy and count hallucinated numbers in outputs.

## Related chapters

- [04 Tools As Capability Boundaries](../../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md)
- [02 The Agent Loop](../../books/08-agent-systems/02-the-agent-loop.md)
- [05 Mcp And Integration Protocols](../../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md)

## Related concepts

- [Function Calling](../../concepts/cards/function-calling.md)
- [Tool Schemas](../../concepts/cards/tool-schemas.md)
- [Tool Discovery](../../concepts/cards/tool-discovery.md)
