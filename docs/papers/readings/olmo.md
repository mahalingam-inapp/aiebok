# OLMo: Accelerating the Science of Language Models

## Citation

Groeneveld et al.. *OLMo: Accelerating the Science of Language Models.* 2024. [https://arxiv.org/abs/2402.00838](https://arxiv.org/abs/2402.00838)

## One-sentence contribution

Fully open pipeline for reproducible LM research.

## Problem

Most 'open' models released weights but hid training data, code, or logs—preventing true reproducibility and scientific study of how design choices affect outcomes.

## Prior art

LLaMA released weights but not data or training code. Pythia (EleutherAI) opened some training details. BLOOM was open but underperformed frontier models. No model offered full pipeline transparency at competitive quality.

## Core idea

Groeneveld et al. released everything: model weights (OLMo-7B), pre-training data (Dolma—3T tokens, fully documented), training code (Ai2's OLMo framework), training logs, evaluation harness, and model cards. Architectural choices (SwiGLU, RoPE, no bias terms) documented with ablation evidence. Dolma dataset composition and filtering pipeline fully described. The goal is enabling the scientific study of LM training rather than just deploying another checkpoint.

## Evidence

- OLMo-7B competitive with LLaMA-2-7B on MMLU, GSM8K, and other standard benchmarks.
- Training curves and intermediate checkpoints published—enables studying learning dynamics.
- Dolma ablation studies showed impact of data filtering on downstream performance.
- Full reproducibility: independent teams replicated training within reported loss curves.

## Limitations

- Full training run requires significant compute (~800 A100-hours for 7B).
- Initial release limited to 7B scale—larger variants followed later.
- Dolma data, while documented, cannot be fully re-collected by external teams.
- Post-training (SFT, RLHF) not included in base OLMo—requires separate alignment work.

## Lasting impact

OLMo set a new standard for openness in LM research, influencing Allen AI's subsequent releases and raising expectations for what 'open' means in the field.

## Reproduction exercise

Download OLMo-7B and Dolma sample. Fine-tune on 500 instruction pairs using the published training code. Compare eval metrics against LLaMA-2-7B fine-tuned on the same data. Inspect published training logs to identify loss anomalies.

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)
- [03 Dataset Engineering](../../books/11-training-serving-and-ai-operations/03-dataset-engineering.md)
- [06 How To Track The Frontier](../../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md)

## Related concepts

- [Open Weights](../../concepts/cards/open-weights.md)
- [Data Provenance](../../concepts/cards/data-provenance.md)
- [Reproduction](../../concepts/cards/reproduction.md)
