# Learning Transferable Visual Models From Natural Language Supervision

## Citation

Radford et al.. *Learning Transferable Visual Models From Natural Language Supervision.* 2021. [https://arxiv.org/abs/2103.00020](https://arxiv.org/abs/2103.00020)

## One-sentence contribution

Contrastive image–text pretraining enables zero-shot vision tasks.

## Problem

Computer vision models required task-specific labeled datasets (ImageNet, COCO) and could not generalize to new categories without retraining. Vision needed the kind of transfer learning that pre-trained LMs gave NLP.

## Prior art

ImageNet supervised pre-training + fine-tuning was the standard. Self-supervised methods (SimCLR, MoCo) learned representations but still needed fine-tuning for downstream tasks. Vision-language models (VSE, VilBERT) existed but were small-scale.

## Core idea

Radford et al. pre-trained dual encoders (image ViT, text Transformer) on 400M image-text pairs from the web using contrastive learning: maximize cosine similarity of matched pairs, minimize similarity of in-batch negatives. At inference, classify by embedding candidate text labels and picking the highest-similarity match—zero-shot without any task-specific training. The shared embedding space aligns visual and textual concepts.

## Evidence

- Zero-shot ImageNet: 76.2% top-1 accuracy—matching original ResNet-50 supervised baseline.
- Zero-shot transfer competitive with fine-tuned models on 30+ datasets (CIFAR, STL-10, etc.).
- Prompt engineering for class names ('a photo of a {label}') improved zero-shot by 3–5 points.
- ViT-L/14 at 336px resolution: 87.8% zero-shot ImageNet—approaching supervised SOTA.

## Limitations

- Zero-shot requires careful prompt engineering for class names.
- Fine-grained classification (breed-level, medical imaging) underperforms supervised specialists.
- Training data bias (web scrapes) propagates into embedding space.
- No native generative capability—CLIP classifies but cannot generate images (led to diffusion conditioning).

## Lasting impact

CLIP enabled zero-shot vision deployment and became the text encoder for Stable Diffusion, DALL-E 2, and multimodal LLMs. Contrastive image-text pre-training is now standard for vision foundation models.

## Reproduction exercise

Load `openai/clip-vit-base-patch32`, embed 20 images and their text descriptions. Compute pairwise cosine similarities and verify matched pairs rank highest. Run zero-shot classification on 10 CIFAR-10 images using class name prompts.

## Related chapters

- [01 Vision And Document Intelligence](../../books/13-multimodal-and-frontier-systems/01-vision-and-document-intelligence.md)
- [03 Image And Video Generation](../../books/13-multimodal-and-frontier-systems/03-image-and-video-generation.md)
- [03 Unsupervised And Representation Learning](../../books/02-machine-learning-systems/03-unsupervised-and-representation-learning.md)

## Related concepts

- [Vision Encoders](../../concepts/cards/vision-encoders.md)
- [Multimodal Models](../../concepts/cards/multimodal-models.md)
- [Cosine Similarity](../../concepts/cards/cosine-similarity.md)
