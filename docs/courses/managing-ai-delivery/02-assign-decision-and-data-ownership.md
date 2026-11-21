# Assign decision and data ownership

<p class="study-position" data-course="managing-ai-delivery" data-lecture="02-assign-decision-and-data-ownership.md">Own quality and risk · Lecture 2 of 4</p>

[← Find the failure hidden in the average](01-find-the-failure-hidden-in-the-average.md) · [Course outline](index.md#course-outline){ .study-overview } · [Plan a limited launch and rollback →](03-plan-a-limited-launch-and-rollback.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Own quality and risk**

    - [Find the failure hidden in the average](01-find-the-failure-hidden-in-the-average.md)
    - **Assign decision and data ownership** (current)

    **Launch and respond**

    - [Plan a limited launch and rollback](03-plan-a-limited-launch-and-rollback.md)
    - [Review an incident and decide when to resume](04-review-an-incident-and-decide-when-to-resume.md)

## What you will learn

Name who owns release, data access, ongoing quality, and escalation.

## Three owners, three different decisions

The supplier knows the tool, the routing team owns the guidance, and residents need someone in the city to resolve mistakes. Each assumes another group signs off.

Name who can approve a policy change, who watches the rollout, and who can switch routing back to manual. Give residents a named point of contact or clearly staffed queue. A vendor escalation alone does not resolve today’s report.

## How it works

A release has several distinct decisions. The product owner weighs benefit, the data owner approves use, the reviewer judges evidence, and an operator can pause service. A named person or accountable role for each decision helps prevent gaps.

### Separate the authority to recommend, approve, and restore

Several teams can contribute to a service without having authority over the same decision. Policy owners define what is allowed. Operators handle queues and recovery. A product owner sets the scope of the pilot. Reviewers decide whether the evidence is sufficient to proceed, and users need a visible way to dispute or correct an outcome.

Build an ownership map around events, not an organization chart. Who approves a change to routing? Who can pause it at 5 p.m. on Friday? Who contacts a resident after a misroute? Assign names or staffed roles and offer a substitute when the primary person is unavailable.

Check that authority matches access. A named rollback owner with no ability to change the route cannot recover the service. A vendor engineer with broad configuration access cannot take responsibility for a city's service decision. Test the required action and the escalation route in a rehearsal so an incident is not the first time people discover either constraint.

## Worked example

For a staff assistant, HR can own policy data, a product manager can own pilot scope, and support operations can own monitoring and rollback.

## Try it yourself

An employee reports that a document appeared outside its intended audience. Name two roles that should act immediately and what each decides.

??? success "Compare your answer"
    The operator pauses access or switches to the fallback. The data owner assesses which documents and audiences were affected and decides how access should be restored.

## Continue

[← Find the failure hidden in the average](01-find-the-failure-hidden-in-the-average.md) · [Course outline](index.md#course-outline){ .study-overview } · [Plan a limited launch and rollback →](03-plan-a-limited-launch-and-rollback.md)
{: .study-directions .study-directions--footer }
