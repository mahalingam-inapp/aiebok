# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

## Citation

Jimenez et al.. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?.* 2024. [https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)

## One-sentence contribution

Repository-level coding agent benchmark with tests.

## Problem

Coding agents needed realistic benchmarks beyond toy function synthesis.

## Prior art

HumanEval measured short function completion but not repository-level engineering.

## Core idea

SWE-bench tasks require agents to fix real GitHub issues in full repositories with tests as verification.

## Evidence

- Showed large gap between human engineers and early agents.
- Drove research in coding agents, planning, and tool use.

## Limitations

- Contamination and memorization risks
- Compute cost to evaluate

## Lasting impact

Primary benchmark narrative for AI coding agents.

## Reproduction exercise

Run one SWE-bench-lite instance in a sandbox; record steps, cost, and test outcome.

## Related chapters

- [03 Ai Native Development Workflow](../../books/09-ai-software-and-product-engineering/03-ai-native-development-workflow.md)
- [04 Agent Patterns](../../books/08-agent-systems/04-agent-patterns.md)

## Related concepts

- [Ai Coding Agents](../../concepts/cards/ai-coding-agents.md)
- [Benchmarks](../../concepts/cards/benchmarks.md)
