# Fast Inference from Transformers via Speculative Decoding

## Citation

Leviathan et al.. *Fast Inference from Transformers via Speculative Decoding.* 2023. [https://arxiv.org/abs/2211.17192](https://arxiv.org/abs/2211.17192)

## One-sentence contribution

Draft model proposes tokens; target model verifies in parallel.

## Problem

Autoregressive Transformer decoding generates one token at a time, bound by memory bandwidth loading the full model weights per token. Large models (70B+) achieve low token throughput even on high-end GPUs.

## Prior art

Non-autoregressive decoding (parallel prediction) sacrificed quality. Knowledge distillation to smaller models lost capability. Batch inference helped throughput but not single-request latency.

## Core idea

Leviathan et al. use a small draft model to autoregressively generate K candidate tokens cheaply, then run the large target model on all K+1 positions in a single parallel forward pass. Compare draft and target distributions token by token—accept matching tokens, reject at first mismatch and resample from a corrected distribution. Accepted tokens cost one target forward pass for K tokens; rejection rate determines speedup. Quality is identical to target-only decoding (lossless).

## Evidence

- 2–3× speedup on T5-XXL and other models with no change in output distribution.
- Speedup increases with draft-target agreement—similar models achieve higher acceptance rates.
- Batch size 1 latency improved significantly; batch settings also benefit.
- Works with any draft/target pair where both share the same vocabulary.

## Limitations

- Requires a suitable draft model—too small drafts have low acceptance; too large adds overhead.
- Speedup is variable—adversarial or high-entropy text has lower acceptance rates.
- Memory: both models loaded simultaneously increases peak VRAM.
- Implementation complexity in serving frameworks (vLLM, TGI integration ongoing).

## Lasting impact

Speculative decoding is a standard inference optimization in vLLM, TensorRT-LLM, and production serving stacks. It enables practical latency for 70B+ models on single-GPU deployments with a small draft model.

## Reproduction exercise

Implement basic speculative decoding with `google/gemma-2b` as draft and `google/gemma-7b` as target on 20 prompts. Measure tokens/second vs. target-only decoding. Log acceptance rate per prompt and correlate with output entropy.

## Related chapters

- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)
- [05 Inference And Sampling](../../books/04-transformers-and-foundation-models/05-inference-and-sampling.md)
- [05 Deployment And Routing](../../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md)

## Related concepts

- [Kv Cache](../../concepts/cards/kv-cache.md)
- [Latency](../../concepts/cards/latency.md)
- [Distillation](../../concepts/cards/distillation.md)
