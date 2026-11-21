# LLM Adaptation and Inference Engineer Capstone

Choose a small task with one predictable output convention and one case that depends on fresh evidence. Use [LLM Adaptation and Inference Lab](../../courses/llm-adaptation-inference/index.md) for the offline experiment and checkpoint transfer.

## Milestones

1. Freeze the task, checkpoint or fixture, training examples, and held-out workload. Establish a base prompt and a retrieval-assisted baseline.
2. Train a low-rank correction while preserving the base weights. Use a compatible open-weight checkpoint for the checkpoint experiment and report task behavior and held-out loss.
3. Measure compressed payload size, quality, and repeated latency on the same machine. Separate measured results from modeled serving costs and explain when you would revert.

## Rubric

| Evidence | Complete when |
|---|---|
| Experimental design | Versions, data splits, baseline definitions, and hardware are recorded. |
| Adaptation | Train affects the intended parameters and all candidates face the same held-out task. |
| Inference decision | The report measures quality and size, reports observed timing variability, and justifies a deployment choice. |

[Back to the learning path](llm-adaptation-inference-engineer.md)
