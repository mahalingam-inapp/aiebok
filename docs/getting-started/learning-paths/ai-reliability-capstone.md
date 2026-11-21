# AI Reliability and Release Engineer Capstone

Use a versioned local service and run a staged candidate rollout. Introduce a controlled dependency failure in the pilot cohort. Combine the [local deployment practicum](../../courses/operating-ai-services/index.md) with the [reliability workbook](../../courses/ai-reliability-release/index.md).

## Milestones

1. Specify a user-facing service objective, observation window, minimum sample, error-budget and cost thresholds, and rollback authority.
2. Run stable and candidate requests. Localize the failure using stage traces, assess user impact, and make an explicit hold or rollback decision.
3. Restore the baseline, check both normal and affected cohorts, and write the incident timeline with an owned follow-up that can be verified.

## Rubric

| Evidence | Complete when |
|---|---|
| Release plan | Service objectives and gates are defined before rollout and cohorts can be distinguished. |
| Diagnosis | The report identifies the earliest observed failure and separates measured impact from hypotheses. |
| Recovery | Smoke results verify service after rollback and the follow-up has an owner and completion criterion. |

[Back to the learning path](ai-reliability-release-engineer.md)
