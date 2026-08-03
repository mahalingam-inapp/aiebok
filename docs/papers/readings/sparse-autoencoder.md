# Towards Monosemanticity (Sparse Autoencoders)

## Citation

Anthropic. *Towards Monosemanticity (Sparse Autoencoders).* 2023. [https://transformer-circuits.pub/2023/monosemantic-features/index.html](https://transformer-circuits.pub/2023/monosemantic-features/index.html)

## One-sentence contribution

Sparse autoencoders extract interpretable features.

## Problem

Interpretability researchers sought human-understandable features inside dense activations.

## Prior art

Probing classifiers on neurons yielded mixed, unstable features.

## Core idea

Train sparse autoencoders on model activations to discover sparse, often monosemantic features that approximate internal representations.

## Evidence

- Anthropic and follow-up work showed interpretable features for concepts and safety-relevant behaviors.
- Features can be used to monitor or steer model behavior experimentally.

## Limitations

- Incomplete coverage of model computation
- Steering can have side effects

## Lasting impact

Revived feature-based interpretability for large models.

## Reproduction exercise

Run a public sparse autoencoder demo on a small model layer; inspect top activating tokens for one feature.

## Related chapters

- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)
- [05 Responsible Ai And Risk](../../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md)

## Related concepts

- [Neurons And Layers](../../concepts/cards/neurons-and-layers.md)
