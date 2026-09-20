# Independent Regression Scenarios

These scenarios are intentionally separate from the original ADC, BCMA, and smart-pump demonstrations.
They reduce overfitting risk by testing the same analytical discipline across different clinical and
operational contexts.

They are mirrored in `cases.json` so the automated runner can execute them.

## IS-01 — Critical-result follow-up

A hospital wants to replace phone calls for critical radiology-result follow-up with an EHR work
queue. Current practice varies by department and there is no agreed escalation timer.

**Tests:** communication ownership, acknowledgement semantics, escalation without invented thresholds,
failure paths, and non-medication workflow analysis.

## IS-02 — ED ADC replacement

An ED is replacing six legacy ADCs. Pharmacy verification remains for routine medications, selected
urgent medications use overrides, and BCMA remains the administration workflow. Interface technology
and vendor offline behavior are unknown.

**Tests:** event semantics, controlled access, downtime, inventory, interoperability uncertainty,
and decision-focused output.

## IS-03 — BCMA reprint investigation

Pharmacy reprints IV labels when an original barcode is damaged. Nurses report that some reprinted
labels fail scanning.

**Tests:** evidence discipline, barcode/reprint workflow, causal restraint, observation/log evidence,
and exception handling.

## IS-04 — Smart-pump partial recovery

After a network outage, some pumps reconnect immediately while others remain offline and
documentation arrives late.

**Tests:** partial recovery, delayed/duplicate data, reconciliation, monitoring, and ownership.

## IS-05 — EHR/laboratory context conflict

The EHR and laboratory system sometimes disagree on encounter/location after patient transfers.

**Tests:** patient/context identifiers, source-of-truth analysis, stale/conflicting data, timing,
retries, reconciliation, and no invented interface standard.

## IS-06 — Pharmacy restoration and reconciliation

During an application outage, staff use manual labels and paper logs. When service returns, missed
work is entered manually.

**Tests:** focused restoration/reconciliation analysis, duplicate prevention, verification, and
ownership without expanding into an unnecessary full project report.

## IS-07 — Electronic specialty referral

A specialty clinic wants to replace faxed referrals with an electronic queue. Referrals may arrive
with missing documents, and ownership changes when staff are absent.

**Tests:** non-medication clinical operations, intake/completeness/routing, absence coverage,
exception paths, problem-before-product discipline, and measurable validation.

## Interpretation

Passing these cases supports regression confidence only. It does not establish clinical safety,
regulatory compliance, local-policy approval, implementation readiness, or vendor capability.
