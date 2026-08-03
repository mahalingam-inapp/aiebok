# Diffusion

**Purpose:** Reference card for **diffusion** used across AIEBOK books and knowledge areas.

## Core explanation

Diffusion models generate images by iterative denoising from noise, conditioning on text or layout.

## Example

Marketing generates product hero images from prompt plus brand color conditioning.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

FID or human preference eval versus baseline; scan outputs for policy violations.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare diffusion against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Conditioning](../../concepts/cards/conditioning.md)
- [Latent Space](../../concepts/cards/latent-space.md)
- [Provenance](../../concepts/cards/provenance.md)
- [Video Generation](../../concepts/cards/video-generation.md)

## Related chapters

- [03 Image And Video Generation](../../books/13-multimodal-and-frontier-systems/03-image-and-video-generation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
