# Requirements Engineering Reference

Use when creating, reviewing, or validating healthcare IT requirements.

## Core quality criteria

A requirement should be:

- necessary;
- unambiguous;
- feasible;
- testable;
- traceable;
- sufficiently specific.

## Requirement types

- Functional
- Clinical workflow
- Non-functional
- Integration
- Data
- Security/privacy
- Operational
- Downtime/business continuity
- Reporting/analytics

## Mandatory language

Use **shall** for mandatory requirements.

Avoid subjective terms unless measured.

## Traceability fields

Recommended:

- ID
- Type
- Requirement
- Source/Rationale
- Workflow Link
- Acceptance Method

## Example

Weak:

> The ADC should work quickly.

Improved:

> The ADC shall display the selected patient's active medication profile after successful nurse authentication and patient selection.

Only add a numeric performance threshold if supported by a requirement, benchmark, contract, policy, or validated operational need.
