# Make a ship, revise, or stop decision

<p class="study-position" data-course="ai-product-decisions" data-lecture="04-make-a-ship-revise-or-stop-decision.md">Set evidence and limits · Lecture 4 of 4</p>

[← Define success and guardrails](03-define-success-and-guardrails.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Find the right problem**

    - [Frame the decision before selecting a model](01-frame-the-decision-before-selecting-a-model.md)
    - [Compare rules, search, and generation](02-compare-rules-search-and-generation.md)

    **Set evidence and limits**

    - [Define success and guardrails](03-define-success-and-guardrails.md)
    - **Make a ship, revise, or stop decision** (current)

## What you will learn

State a decision based on pilot evidence and remaining uncertainty.

## Sign the limited decision you can defend

The pilot saves time on hours and directions. The preparation slice has too few cases and a missed handoff. The sponsor wants to expand to all inquiries.

Approve only the range supported by the evidence, if the appropriate owner agrees. Keep preparation questions with staff and collect a separate review set. Write the stop rule and who can invoke it.

### What Kavita takes to the sponsor

A sponsor might reasonably ask why the whole queue cannot use the tool if hours and directions went well. The answer is that the two types of work have different failure costs. One inconveniences a caller. The other may send them to the wrong place or leave them without a clear next step.

A short release memo could make that distinction concrete.

- **Approve** routine hours and directions for the trial audience, using the maintained directory.
- **Keep with staff** appointment preparation and ambiguous requests. The assistant gives callers the current contact route.
- **Pause if** any preparation question is presented as a confirmed answer during an audit. The front-desk lead owns the pause and the manual route.
- **Revisit after** a separate preparation trial shows correct referrals across the expected cases, and staff confirm the handoff is manageable.

The last line matters. A hold can be reviewed when someone knows what evidence would change the decision. A vague promise to revisit it leaves both the sponsor and staff guessing.

## How it works

Use the agreed thresholds. Report what was measured, which cases were underrepresented, and the next decision. A small pilot can justify a larger trial when uncertainty remains. It rarely establishes that a result will carry over to every team or workload.

### Write the decision while the evidence is fresh

A pilot decision should record scope, outcome, remaining uncertainty, and an owner. “The pilot worked” leaves the next operator unable to tell which tasks passed. “Continue with published hours and directions for this cohort” gives them a bounded action they can verify.

Read a sparse result carefully. Five correct answers about preparation are encouraging, but they say little about rare exceptions. If a mistake could leave a caller in the wrong queue, keep that slice with staff until you have better evidence. Record which cases are missing, who can supply them, and what result would justify revisiting the hold.

When you choose to pause, preserve the benefit evidence as well as the failure. The organization may still have a valuable directory or a better handoff even if one proposed form of automation is unsuitable. A clear decision memo helps separate a failed experiment from a judgment about all uses of the technology.

## Worked example

A pilot meets its time target and misses its accuracy guardrail. Hold rollout, inspect which cases failed, and rerun a targeted pilot after correcting those failures.

## Try it yourself

Your pilot meets both thresholds on 20 routine cases. It includes no urgent cases. What is the next decision?

??? success "Compare your answer"
    Consider a bounded expansion for routine cases. Keep urgent cases in the established process until they are evaluated separately.

## Continue

[← Define success and guardrails](03-define-success-and-guardrails.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
