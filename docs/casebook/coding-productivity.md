# Two studies measured two different coding jobs

## Compare the tasks, then compare the numbers

GitHub reported that participants with Copilot finished a controlled task faster. The task was to implement a JavaScript HTTP server. METR’s early-2025 randomized study followed experienced developers on issues from mature repositories they already knew. METR reported 19% longer completion time with AI tools allowed in that particular study. These studies used different tools, tasks, participant populations, and measurements. [GitHub’s controlled Copilot study](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness-/) · [METR’s early-2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

## Bring the question back to the team

Imagine you own a shared billing repository. A teammate uses an assistant to draft five small changes in an hour. Two reviewers spend the afternoon checking policy assumptions and untangling oversized diffs. A second teammate uses the same tool to write fixture setup for one change, with a narrower diff and an easier review.

Which change are you buying? An initial prototype and a correct patch in an established system have different costs. A useful trial tracks both types of work and records how long it takes to reach an accepted result. Include failed attempts, rework, the person doing the review, and defects found later. Use task-level comparisons before aggregating.

Ask the team to define an accepted result before the trial begins. For a new service it might be a working demo with tests. For a billing patch it might mean passing the domain checks, a reviewed diff, and no regressions in the next release. The purchasing decision should follow the work you actually need to improve.

[AI Software and Product Engineering](../books/09-ai-software-and-product-engineering/index.md) · [Supervised Coding-Agent Harnesses](../courses/supervised-coding-harness/index.md) · [Casebook](index.md)
