# Evaluation

**Purpose:** Turn desired AI behavior and acceptable risk into repeatable evidence.

## Evaluation stack

1. Define users, tasks, conditions, and failure severity.
2. Create representative and adversarial cases.
3. Establish simple baselines.
4. Select deterministic metrics, rubric judgments, and human review.
5. Record versions, prompts, evidence, latency, cost, and errors.
6. Compare with uncertainty and inspect slices, not just averages.
7. Set release gates and monitor online outcomes.

## LLM judges

Use judges for scalable rubric application, not as unquestionable ground truth. Calibrate them against humans, randomize ordering, control verbosity bias, record judge versions, and inspect disagreements.

## Practice

Run the [evaluation harness lab](../labs/eval-harness.md). Add a regression that passes average score but fails a high-risk slice; design the correct release gate.

## Common failure

Optimizing a public benchmark or single aggregate number can improve the score while degrading the actual product. Good evaluation is a model of real use and real harm.
