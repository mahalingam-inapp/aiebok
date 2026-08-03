# Text To Speech

**Purpose:** Reference card for **text to speech** used across AIEBOK books and knowledge areas.

## Core explanation

Text-to-speech synthesizes natural audio from text with voice, prosody, and latency trade-offs.

## Example

IVR reads dynamic account balance with consistent brand voice under 500ms first byte.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

MOS evaluation and latency p95 on 50 test phrases monthly.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare text to speech against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Diarization](../../concepts/cards/diarization.md)
- [Speech Recognition](../../concepts/cards/speech-recognition.md)
- [Streaming Audio](../../concepts/cards/streaming-audio.md)
- [Voice Safety](../../concepts/cards/voice-safety.md)

## Related chapters

- [02 Speech And Audio](../../books/13-multimodal-and-frontier-systems/02-speech-and-audio.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
