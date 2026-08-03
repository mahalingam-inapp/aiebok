# Chain-of-Thought Prompting Elicits Reasoning

## Citation

Wei et al.. *Chain-of-Thought Prompting Elicits Reasoning.* 2022. [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)

## One-sentence contribution

Few-shot reasoning exemplars improve multi-step task performance.

## Problem

Large LMs fail multi-step reasoning tasks (arithmetic, commonsense, symbolic manipulation) when prompted to produce answers directly—even when individual steps are within capability.

## Prior art

Standard few-shot prompting appended input→output pairs without intermediate steps. Scratchpad work (NYU, 2021) trained models to output reasoning traces but required fine-tuning. Program-aided methods used external solvers rather than LM-native reasoning.

## Core idea

Wei et al. demonstrated that including few-shot exemplars with explicit intermediate reasoning steps ('Let's think step by step…') in the prompt causes LMs to generate similar step-by-step chains before the final answer. No fine-tuning required—purely an inference-time prompt change. The effect emerges primarily at sufficient scale (~100B+ parameters for robust CoT on GSM8K). CoT essentially elicits the model's latent multi-step computation by showing the desired output format.

## Evidence

- GSM8K (math): PaLM 540B with CoT scored 57% vs. 18% with standard prompting.
- StrategyQA, Date Understanding, Sports Understanding: large gains on PaLM and Codex.
- CoT gains increase with model size—GPT-3 175B showed smaller CoT benefit than PaLM 540B.
- Self-consistency (sample multiple CoT paths, majority vote) further boosted GSM8K to 74%.

## Limitations

- Requires large models—CoT often hurts or adds no value for models <10B parameters.
- Exemplar selection and ordering significantly affect results; brittle in production.
- Generated reasoning can be plausible but wrong (unfaithful CoT)—steps don't always reflect actual computation.
- Increases output token count 3–5×, raising latency and cost.

## Lasting impact

CoT prompting became standard for reasoning tasks and a building block for ReAct, Tree of Thoughts, and test-time compute scaling. 'Let's think step by step' is now a default prompt engineering technique.

## Reproduction exercise

Evaluate GPT-4o-mini on 50 GSM8K problems with direct prompting vs. 5-shot CoT exemplars. Measure accuracy and average output tokens. Add self-consistency (5 samples, majority vote) on 20 problems and compare cost-quality trade-off.

## Related chapters

- [01 Reasoning As Search](../../books/07-reasoning-and-tool-use/01-reasoning-as-search.md)
- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)
- [03 Verification And Critique](../../books/07-reasoning-and-tool-use/03-verification-and-critique.md)

## Related concepts

- [Few Shot Examples](../../concepts/cards/few-shot-examples.md)
- [Self Consistency](../../concepts/cards/self-consistency.md)
- [Test Time Compute](../../concepts/cards/test-time-compute.md)
