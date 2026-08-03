# Knowledge Neurons in Pretrained Transformers

## Citation

Dai et al.. *Knowledge Neurons in Pretrained Transformers.* 2022. [https://arxiv.org/abs/2104.08696](https://arxiv.org/abs/2104.08696)

## One-sentence contribution

Localized parameters correlate with factual recall.

## Problem

Factual knowledge in pre-trained LMs is distributed across billions of parameters with no clear localization. Understanding where and how facts are stored is prerequisite to knowledge editing, unlearning, and interpretability.

## Prior art

Probing classifiers detected encoded information in hidden states but did not identify causal mechanisms. Memorization studies found LMs recall training data but not which components enable recall.

## Core idea

Dai et al. identify 'knowledge neurons' in Transformer FFN layers: individual feed-forward dimensions whose activation correlates with expressing a specific fact (e.g., 'Paris is the capital of France'). Method: (1) prompt the model with a fact expression; (2) compute attribution scores for each FFN neuron; (3) select top neurons as knowledge neurons. Causal test: suppressing (zeroing) those neurons reduces the model's ability to express the fact; amplifying them increases recall. Knowledge is localized but distributed—a fact may involve 5–20 neurons across layers.

## Evidence

- LAMA benchmark: suppressing identified knowledge neurons reduced factual recall accuracy by 30–50% for targeted facts.
- Cross-lingual facts share neurons across languages (English 'Paris' and French 'Paris' activate overlapping neurons).
- Editing fact by modifying neuron activations changed model predictions without full fine-tuning.
- Neurons are sparse—<1% of FFN dimensions account for most factual recall.

## Limitations

- Neuron-fact mapping is imprecise—suppression affects related facts (side effects).
- Method works best for simple relational facts; complex reasoning not localized.
- Multilingual and multi-hop facts have messier neuron distributions.
- Causal claims depend on intervention methodology—correlation vs. causation debated.

## Lasting impact

Knowledge neurons research launched the field of LM knowledge editing (ROME, MEMIT) and informed interpretability work on FFN layers as key-value stores.

## Reproduction exercise

Using a small LM (GPT-2 or Pythia-1B), select 10 facts from LAMA. Compute integrated gradients attribution on FFN layers for each fact. Identify top-5 neurons, suppress them, and measure prediction probability drop. Compare against random neuron suppression.

## Related chapters

- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)
- [01 Knowledge Outside The Model](../../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md)
- [02 From Symbols To Statistics](../../books/01-foundations-of-intelligence/02-from-symbols-to-statistics.md)

## Related concepts

- [Neurons And Layers](../../concepts/cards/neurons-and-layers.md)
- [Knowledge Representation](../../concepts/cards/knowledge-representation.md)
- [Behavior Versus Knowledge](../../concepts/cards/behavior-versus-knowledge.md)
