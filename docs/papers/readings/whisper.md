# Robust Speech Recognition via Large-Scale Weak Supervision

## Citation

Radford et al.. *Robust Speech Recognition via Large-Scale Weak Supervision.* 2022. [https://arxiv.org/abs/2212.04356](https://arxiv.org/abs/2212.04356)

## One-sentence contribution

Multilingual ASR from weakly labeled audio at scale.

## Problem

ASR systems required clean, labeled audio in each target language and degraded on accents, background noise, and code-switching. Building multilingual speech recognition traditionally required separate models per language.

## Prior art

DeepSpeech, Wav2Vec 2.0, and supervised ASR models needed language-specific labeled data. Multilingual models existed but required careful language identification and language-specific fine-tuning.

## Core idea

Radford et al. trained a seq2seq Transformer on 680,000 hours of weakly labeled multilingual audio from the web (YouTube, podcasts). Labels are noisy (auto-generated subtitles, metadata)—the model learns from scale rather than label quality. Input: 30-second audio chunks as log-mel spectrograms. Output: text tokens including special tokens for language identification, timestamps, and task specification (transcribe vs. translate). A single model handles 99 languages.

## Evidence

- English ASR: competitive with supervised models (LibriSpeech WER ~2.7% on clean speech).
- Zero-shot transfer to unseen languages without fine-tuning.
- Robust to accents, background noise, and technical vocabulary from diverse training data.
- Translation mode: transcribe non-English audio directly to English text.

## Limitations

- Hallucination on silence or noise-only segments—model generates plausible but wrong text.
- Long-form audio requires chunking with potential boundary errors.
- Latency: full seq2seq decode is slower than streaming CTC models.
- Timestamp accuracy degrades on fast speech or overlapping speakers.

## Lasting impact

Whisper became the default open-source ASR, powering transcription services, voice agents, and accessibility tools. It demonstrated that weak supervision at scale beats careful labeling for speech.

## Reproduction exercise

Run `openai/whisper-base` on 10 audio clips (5 clean, 5 noisy) from LibriSpeech or recorded samples. Compare WER against ground truth. Test on a non-English clip to verify zero-shot multilingual capability.

## Related chapters

- [02 Speech And Audio](../../books/13-multimodal-and-frontier-systems/02-speech-and-audio.md)
- [01 Sequence Models Before Transformers](../../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md)
- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)

## Related concepts

- [Speech Recognition](../../concepts/cards/speech-recognition.md)
- [Multilingual Models](../../concepts/cards/multilingual-models.md)
- [Self Supervision](../../concepts/cards/self-supervision.md)
