# ReAct: Synergizing Reasoning and Acting

## Citation

Yao et al.. *ReAct: Synergizing Reasoning and Acting.* 2023. [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)

## One-sentence contribution

Interleave chain-of-thought with tool actions and observations.

## Problem

Chain-of-thought prompting improves reasoning but models cannot act on the world—look up facts, query databases, or execute code. Separate tool-use pipelines lacked unified reasoning traces that humans could inspect and debug.

## Prior art

WebGPT used RL to train browsing. Toolformer self-supervised API calls during pretraining. CoT elicited reasoning but no actions. Traditional agents (ReAct predecessors) used separate planning and execution modules without language-model-native traces.

## Core idea

Yao et al. interleaved three trace types in a single prompt trajectory: Thought (reasoning about the current state), Action (a tool call with structured input, e.g., Search[entity]), and Observation (the tool's returned result). The LM generates Thought and Action tokens; the environment (search engine, calculator, API) produces Observations appended to the context. This loop continues until the model emits a Final Answer. Few-shot exemplars of full Thought-Action-Observation trajectories teach the pattern without fine-tuning.

## Evidence

- HotpotQA (multi-hop QA): ReAct outperformed CoT-only and action-only baselines on EM/F1.
- FEVER (fact verification): ReAct achieved higher label accuracy by retrieving evidence before committing to a verdict.
- AlfWorld (text-based embodied tasks): ReAct beat imitation learning and CoT on success rate.
- Human interpretability: trajectories were easier to debug than black-box tool pipelines.

## Limitations

- Prompt-fragile—small changes to exemplars or tool schemas degrade performance sharply.
- Error propagation: a bad early action poisons subsequent reasoning with wrong observations.
- No formal guarantees on tool use; models hallucinate actions or arguments.
- Latency scales with number of tool calls; each step requires a full LM forward pass.

## Lasting impact

ReAct established the Thought→Action→Observation loop used in LangChain, AutoGPT, and production agent frameworks. It bridged CoT reasoning and tool-augmented LLMs into a single inspectable trace format.

## Reproduction exercise

Implement a 3-tool ReAct agent (calculator, Wikipedia search via API, final answer) on 20 HotpotQA questions using GPT-4o-mini. Compare accuracy against CoT-only (no tools). Log full trajectories and count how many failures come from wrong tool selection vs. wrong reasoning after correct retrieval.

## Related chapters

- [04 Tools As Capability Boundaries](../../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md)
- [02 The Agent Loop](../../books/08-agent-systems/02-the-agent-loop.md)
- [02 Planning](../../books/07-reasoning-and-tool-use/02-planning.md)

## Related concepts

- [Plan Act Observe](../../concepts/cards/plan-act-observe.md)
- [Tool Schemas](../../concepts/cards/tool-schemas.md)
- [Function Calling](../../concepts/cards/function-calling.md)
