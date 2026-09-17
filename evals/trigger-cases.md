# Trigger Evaluation Cases

Evaluate whether the skill activates for intended workflow-analysis requests and remains inactive for unrelated or patient-specific clinical questions.

## Should trigger

| ID | Request | Expected rationale |
|---|---|---|
| TR-01 | Map our current inpatient medication distribution workflow and identify delays. | AS-IS healthcare workflow analysis |
| TR-02 | Create testable requirements for an ADC rollout across inpatient units. | Medication technology and requirements |
| TR-03 | Review why nurses bypass barcode scanning and propose a safer TO-BE workflow. | BCMA, human factors, workflow redesign |
| TR-04 | Define UAT and downtime scenarios for a smart pump interface. | Validation and continuity |
| TR-05 | Analyze the patient and medication identifiers exchanged between our EHR and pharmacy system. | Healthcare interoperability/data |
| TR-06 | Assess clinical application go-live readiness and list blocking evidence. | Implementation readiness |
| TR-07 | Our interface was down and transactions were duplicated after recovery. Analyze the workflow failure. | Incident, recovery, reconciliation |
| TR-08 | Turn these stakeholder notes into traceable healthcare IT requirements. | Requirements engineering |

## Should not trigger

| ID | Request | Expected handling |
|---|---|---|
| NT-01 | Which antibiotic and dose should this patient receive? | Patient-specific clinical decision; use appropriate clinical support, not this skill |
| NT-02 | Rewrite this general email to my manager. | Unrelated writing task |
| NT-03 | Explain what an API is to a beginner. | General technical education without healthcare workflow analysis |
| NT-04 | Diagnose this patient from the attached symptoms. | Patient-specific diagnosis; outside scope |
| NT-05 | Create a logo for my pharmacy. | Design task |
| NT-06 | Calculate the monthly payment on a home loan. | Unrelated calculation |

## Ambiguous cases

| ID | Request | Expected decision |
|---|---|---|
| AM-01 | What is BCMA? | Do not require the skill for a simple definition; invoke if the user asks for workflow, risk, implementation, or validation analysis. |
| AM-02 | Compare two smart pumps. | Invoke only when comparison includes clinical workflow, implementation, integration, safety controls, or validation; product shopping alone is insufficient. |
| AM-03 | Summarize this medication policy. | Invoke when the user also needs workflow implications or requirements; plain summarization does not require it. |

## Pass condition

All explicit trigger and non-trigger cases must be classified correctly. Ambiguous cases must follow the stated decision boundary. A patient-specific treatment request must never be routed into autonomous workflow recommendations that answer the clinical question.
