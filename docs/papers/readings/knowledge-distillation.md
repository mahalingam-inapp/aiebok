# Distilling the Knowledge in a Neural Network

## Citation

Hinton et al.. *Distilling the Knowledge in a Neural Network.* 2015. [https://arxiv.org/abs/1503.02531](https://arxiv.org/abs/1503.02531)

## One-sentence contribution

Train smaller students to mimic teacher soft targets.

## Problem

Large teacher models are costly at inference; teams need smaller deployable students.

## Prior art

Manual compression and pruning lost quality unpredictably.

## Core idea

Distillation trains a smaller student to match teacher logits or intermediate signals on a dataset, preserving behavior with fewer parameters.

## Evidence

- Classic Hinton distillation improved small models on classification.
- Modern LLM distillation uses synthetic data from teachers for instruction following.

## Limitations

- Student caps at teacher quality
- Distribution shift if teacher data mismatches production

## Lasting impact

Core technique for edge deployment and cost reduction.

## Reproduction exercise

Distill a tiny classifier from a larger sklearn/neural teacher on MNIST or text classification subset.

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)
- [04 Neural Networks](../../books/02-machine-learning-systems/04-neural-networks.md)

## Related concepts

- [Distillation](../../concepts/cards/distillation.md)
- [Sft](../../concepts/cards/sft.md)
- [Model Routing](../../concepts/cards/model-routing.md)
