# Testing and Validation Reference

Use when creating acceptance criteria, test scenarios, UAT, implementation readiness, or production validation.

## Test layers

- Functional
- Integration
- End-to-end workflow
- Negative
- Failure/downtime
- User acceptance
- Regression
- Production validation

## Acceptance criteria

Use observable outcomes.

Given/When/Then is useful when it improves precision.

## Test both normal and exception paths

Examples:

- expected transaction succeeds;
- required data is missing;
- wrong patient/context is selected;
- interface is unavailable;
- device is offline;
- duplicate event occurs;
- user lacks permission;
- recovery/reconciliation is required.

Do not claim validation has passed unless actual evidence is supplied.

## Execution record

For each test record ID, requirement/risk link, layer, preconditions, synthetic data, steps, expected
result, environment/configuration/version, actual result, evidence reference, tester, execution date,
status, and linked defect. Use Planned, Passed, Failed, or Blocked; Passed requires actual evidence.
Do not call document review or registry validation a live workflow/model test.
