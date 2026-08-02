# Runnable Code Samples

These dependency-free Python samples expose the mechanisms used throughout the books. They favor clarity and observability over production completeness.

| Book | Sample | Demonstrates |
|---:|---|---|
| 1 | [Search and planning](01-search-planning.py) | BFS, A*, heuristics, expanded-state comparison |
| 2 | [Gradient descent](02-gradient-descent.py) | Loss, gradients, parameter updates, convergence |
| 3 | [Tokenization and vectors](03-tokenization-vectors.py) | Tokenization, TF–IDF, cosine ranking |
| 4 | [Attention and sampling](04-attention-sampling.py) | Q/K/V attention and temperature |
| 5 | [Context builder](05-context-builder.py) | Priorities, budgets, and trust labels |
| 6 | [Hybrid RAG](06-hybrid-rag.py) | Reciprocal-rank fusion |
| 7 | [Planner and verifier](07-planner-verifier.py) | Candidate plans and independent constraints |
| 8 | [Agent state machine](08-agent-state-machine.py) | State, budgets, approval, termination |
| 9 | [Specification-driven development](09-spec-driven-development.py) | Executable acceptance examples |
| 10 | [Evaluation slices](10-evaluation-slices.py) | Aggregate/slice metrics and risk gates |
| 11 | [Model router](11-model-router.py) | Quality, risk, complexity, and routing |
| 12 | [Cloud capability map](12-cloud-capability-map.py) | Logical architecture versus services |
| 13 | [Multimodal provenance](13-multimodal-provenance.py) | Source, page, modality, and confidence |

## Run everything

From the repository root:

```bash
for sample in examples/*/main.py; do
  python "$sample"
done
```

## Practice method

1. Predict the output before running the sample.
2. Run it unchanged and explain every line that affects the result.
3. Add one test and one failure case.
4. Replace the educational simplification with a mature library.
5. Compare behavior, performance, and operational complexity.

!!! warning "Educational scope"
    The samples omit production authentication, persistence, concurrency, telemetry, dependency management, and hardening unless those are the mechanism being taught.
