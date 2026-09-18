# Demonstration: Automated Dispensing Cabinet Implementation

This synthetic example demonstrates analysis behavior. It is not a validated implementation plan.

## Scenario

A hospital plans to introduce ADCs on two inpatient units. Medication orders originate in the EHR and are verified by pharmacy. The organization wants faster access to first doses while preserving pharmacy verification and controlled-substance accountability. Vendor, interface, policy, network, and device details are not supplied.

## Evidence classification

| Statement | Class |
|---|---|
| EHR orders are pharmacy-verified | Known |
| ADCs will be installed on two inpatient units | Known |
| An electronic order interface will populate patient profiles | Inferred; validation required |
| Emergency access will use overrides | Assumed for analysis only |
| Controlled-substance witness rules | Unknown; local policy required |

## AS-IS summary

1. Prescriber enters order in the EHR.
2. Pharmacist verifies the order.
3. Pharmacy prepares or selects medication.
4. Medication is delivered to the unit.
5. Nurse receives, selects, administers, and documents the dose.
6. Exceptions are communicated manually; exact channels and escalation are unknown.

## Main findings

- The objective is partly defined, but baseline first-dose delay and success measures are missing.
- ADC use creates new dependencies on medication mapping, patient context, user authorization, inventory configuration, replenishment, and interface monitoring.
- Emergency access may bypass pharmacy verification and therefore requires explicit governance and monitoring.
- A fallback without restoration and transaction reconciliation would be incomplete.

## TO-BE concept

**EHR order → Pharmacy verification → Verified transaction → ADC patient profile → Authenticated nurse selection → Medication removal → Administration/documentation → Inventory transaction**

Exceptions include missing patient profile, delayed order, unavailable medication, interface outage, device/network failure, discrepancy, return, waste, and controlled-substance transaction. Actual system behavior must be confirmed.

## Example requirements

| ID | Type | Requirement | Rationale | Acceptance method |
|---|---|---|---|---|
| INT-001 | Integration | The solution shall make a pharmacy-verified medication order available in the correct patient context at the designated ADC. | Preserve order context | Integration and end-to-end test |
| CWR-001 | Clinical workflow | The workflow shall define authorized emergency access when the verified order is unavailable and shall record the user, patient context, medication, date/time, and reason. | Control exceptional access | Policy review and UAT |
| OPS-001 | Operational | The replenishment workflow shall assign ownership for stock selection, transport, loading, discrepancy resolution, and verification. | Avoid ambiguous ownership | Workflow simulation |
| DT-001 | Downtime | The downtime procedure shall define detection, notification, controlled fallback access, documentation, restoration, and reconciliation. | Preserve continuity | Downtime exercise |

## Example validation

- Verified order appears only in the intended patient and cabinet context.
- A missing mapping is rejected or routed to a monitored exception rather than silently misfiled.
- An unauthorized user cannot access the cabinet.
- Emergency access records the required audit information.
- Transactions completed during downtime are reconciled after restoration.

## Blocking questions

- What is the approved source of truth for patient, encounter, medication, and location data?
- What local policy governs overrides and controlled substances?
- How are interface failures detected, queued, retried, and owned?
- What evidence and authority are required for go-live approval?
