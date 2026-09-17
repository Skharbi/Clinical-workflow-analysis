# Demonstration: BCMA Safety Review

This synthetic example demonstrates analysis behavior. It does not certify BCMA safety or compliance.

## Scenario

A hospital reports frequent barcode bypasses during inpatient medication administration. Staff state that some unit-dose packages do not scan reliably and shared workstations are sometimes unavailable. No event data, policy, device inventory, or direct observation is supplied.

## Evidence classification

| Statement | Class |
|---|---|
| Barcode bypasses are reported as frequent | Known as a stakeholder report; frequency unverified |
| Some packages do not scan reliably | Known as a stakeholder report; root cause unknown |
| Device availability contributes to bypasses | Inferred |
| Users are noncompliant | Unsupported; do not conclude |

## Review boundary

Start: medication is ready for administration. End: administration is documented and exceptions are resolved. Include patient identification, medication identification, order context, scanner/workstation availability, barcode quality, interruptions, bypass reasons, documentation, downtime, and follow-up.

## Risk pathways

| Finding | Potential impact | Evidence needed | Control direction |
|---|---|---|---|
| Unreadable barcode | Loss of automated medication identification | Scan-failure data and package samples | Barcode quality and repackaging control |
| Unavailable device | Workaround pressure and delayed documentation | Device-location and availability study | Device capacity/placement review |
| Generic bypass reason | Weak learning and accountability | Configuration and report review | Actionable reason taxonomy |
| Reprinted label changes encoded value | Order/medication mismatch risk | Label workflow observation and test | Governed reprint process |

## Example requirements

| ID | Type | Requirement | Acceptance method |
|---|---|---|---|
| CWR-001 | Clinical workflow | The workflow shall require positive patient identification and medication identification before routine administration documentation. | End-to-end UAT |
| OPS-001 | Operational | The organization shall define ownership and turnaround for medications that cannot be scanned at the point of care. | Workflow simulation |
| RPT-001 | Reporting | The solution shall support review of bypass events by unit, medication, reason, user role, and time period, subject to authorized access. | Report validation |
| DT-001 | Downtime | The procedure shall define safe fallback, documentation, restoration, and reconciliation when scanning or network capability is unavailable. | Downtime exercise |

## Validation scenarios

- Correct patient and medication scan permits continuation in the active order context.
- Wrong patient, wrong medication, inactive order, unreadable barcode, and offline scanner follow defined exception paths.
- A reprinted or repackaged medication is tested using the actual production workflow.
- Bypass activity is reportable and traceable to a reason without claiming causation from counts alone.

## Recommended next evidence

1. Observe administration across representative units and shifts.
2. Stratify scan failures by package source, medication, device, location, and workflow step.
3. Review approved policy, reason codes, training, device placement, and support ownership.
4. Test normal, negative, failure, recovery, and reconciliation paths.
