# Find the failure hidden in the average

[Managing AI Delivery](index.md) · Own quality and risk · Lecture 1 of 4 · 20–30 min · No code

## What you will learn

Identify a critical user group or circumstance that needs its own evidence.

## How it works

A slice is a meaningful subset of cases, such as a language or request type. Aggregate accuracy can be high while a small group experiences frequent errors. Review slices with distinct consequences and report how many examples were checked.

## Worked example

A tool is correct on 95 of 100 tickets. If all five mistakes are urgent tickets, the overall score obscures the urgent-case failure.

## Try it yourself

A feature is correct on 99 of 100 outputs. The one wrong answer gives an incorrect emergency contact. What evidence would you ask for before expansion?

??? success "Compare your answer"
    Ask for a dedicated emergency-contact check, including current authorized source records and representative variations. Require that slice to pass its own criterion.

## Continue

[Course outline](index.md) · [Next lecture →](02-assign-decision-and-data-ownership.md)
