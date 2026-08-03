# Prompt Injection

**Purpose:** Recognize and mitigate hostile instructions embedded in untrusted content that a model may follow instead of trusted system policy.

**Prerequisites:** Prompt and context engineering, retrieval systems, tool calling, authorization.

## Why prompt injection matters

Models treat all text in context as potential instructions. Retrieved web pages, emails, tickets, and user uploads can contain directives like “ignore previous instructions” that override intended behavior, exfiltrate secrets, or trigger unauthorized tool calls.

## Core intuition

Prompt injection is not a single bug—it is a boundary failure between **trusted instructions** and **untrusted data**. Defenses combine instruction hierarchy, input sanitization, tool authorization, output validation, and human approval for high-impact actions.

## Mechanics

1. **Identify trust zones:** system policy, developer instructions, tool outputs, retrieved documents, user input.
2. **Mark untrusted content** with delimiters and metadata; never let it appear as authoritative policy.
3. **Constrain actions:** typed tools, allowlists, read-only defaults, and confirmation for side effects.
4. **Validate outputs** against schema and policy before execution or display.
5. **Test adversarially** with malicious retrieved text and indirect injection via third-party content.

## Engineering checklist

- Red-team with direct and indirect injection cases in retrieved and pasted content.
- Separate secrets from model-visible context; assume anything in context may leak.
- Log which sources contributed to each decision for incident response.
- Treat “helpful” model compliance with hostile instructions as a failed test, not success.

## Trade-offs

Stronger isolation and approval flows reduce risk but add latency and friction. Over-sanitization can remove legitimate evidence needed for grounded answers.

## Common misconceptions

- System prompts alone do not guarantee immunity.
- Filtering keywords is insufficient against paraphrased or encoded attacks.
- Tool schemas without authorization still allow abuse if the model selects dangerous arguments.

## Evolution lens

Yesterday: single-user chat with minimal retrieval. Today: RAG and tool-enabled assistants with explicit trust boundaries. Tomorrow: stronger policy engines and provenance-aware context. The durable principle is treating external content as data, never as authority.
