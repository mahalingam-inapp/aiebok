# Model Architecture and Decision Systems Capstone

HarborLink needs to answer policy questions, summarize equipment logs, and assign a limited number of maintenance slots. These are three different jobs. Build one decision record that identifies what the model computes, which serving strategy runs it, and which policy acts on the output.

## Build and compare

1. **Model architecture.** Compare a dense reference with top-1 and top-2 expert routing under both an evenly distributed and a bursty workload. Report resident weights, active expert weights, overflow, and estimated cross-device payload. State what a real expert-parallel benchmark would need to measure.
2. **Inference policy.** Freeze tasks and verify the outputs. Compare a fixed budget and a bounded cascade. Report verified successes, escalations, cost per verified success, and warm and cold p95 latency separately. Label fixture estimates and live measurements.
3. **Decision policy.** Use a prediction or risk estimate as input to a capacity-constrained assignment. Compare a simple threshold and the constrained policy. Include an infeasible case and show who receives it for review. If you evaluate from logs, report overlap, effective sample size, and where conclusions are unsupported.
4. **Release decision.** Set a quantitative stop rule for a critical workload, a fallback, and a named operational owner. Explain which evidence supports a shadow run and what would still be needed for rollout.

## Submit

- Three reproducible experiments and a paired results table
- A diagram showing the boundaries between token routing, request routing, verification, and action selection
- One failure from each experiment and how you would investigate it
- A release decision with conditions to proceed, hold, or revert

Use the three course workbooks for the local implementation. A live model run is optional. Pin the checkpoint, runtime, hardware, prompts, decode options and workload conditions if you run one.

## Review rubric

The work passes when the experiments can be rerun, measurements and estimates are labeled, and the release decision follows from the fixed gates. Verify one low-confidence or infeasible case by tracing it from model output to the responsible reviewer. A policy with an unsupported action should produce an explicit hold, even when aggregate results look favorable.

[Return to the learning path](model-architecture-decision-engineer.md)
