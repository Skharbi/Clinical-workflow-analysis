# Healthcare Clinical Workflow Analyst — Knowledge Base

**Version:** 1.1  
**Purpose:** Core domain model for healthcare workflow and health IT analysis  
**Last reviewed:** 2026-09-16

---

## 1. Core model

Healthcare technology operates inside a socio-technical system.

A workflow is not simply:

**User → Software → Result**

It may include:

**People + Process + Clinical decisions + Technology + Devices + Information + Physical environment + Policy + Communication + Exceptions**

Therefore, technology should not be analyzed separately from the clinical and operational workflow in which it operates.

---

## 2. Workflow decomposition

For relevant workflow steps, identify:

**Trigger → Actor → Action → System/Device → Information → Decision → Handoff → Exception → Outcome**

Not every workflow needs every element explicitly documented, but important elements should not be silently omitted.

### Trigger

What starts the workflow or step?

### Actor

Who performs or owns the activity?

### Action

What is done?

### System or device

Which technology participates?

### Information

What data or knowledge is needed?

### Decision

What determines the next action?

### Handoff

Where does responsibility or information move?

### Exception

What happens outside the normal path?

### Outcome

What ends the step or workflow?

---

## 3. Workflow levels

Healthcare workflow can occur at multiple levels.

### Individual

One person performs a task.

Example: a pharmacist verifies an order.

### Human-to-human

Responsibility or information passes between people.

Example: a nurse contacts pharmacy about an unavailable medication.

### Human-to-system

A user interacts with technology.

Example: a nurse scans a patient wristband.

### System-to-system

Information moves between technologies.

Example: an EHR sends an order to a pharmacy system.

### Departmental

A process spans operational teams.

Example: central pharmacy prepares and distributes medication to an inpatient unit.

### Enterprise

A workflow crosses multiple clinical and technical domains.

### External

The workflow crosses organizational boundaries.

---

## 4. Healthcare technology analysis model

For a relevant system, application, or device, assess:

- purpose;
- intended users;
- clinical or operational role;
- inputs;
- outputs;
- dependencies;
- interfaces;
- configuration dependencies;
- failure modes;
- monitoring;
- fallback;
- restoration;
- reconciliation;
- ownership.

Do not infer vendor-specific functionality without evidence.

---

## 5. Medication-use lifecycle

Medication-related workflows may span:

**Prescribing → Verification → Preparation → Dispensing → Distribution → Administration → Monitoring**

Additional processes may include:

- medication reconciliation;
- procurement;
- inventory;
- storage;
- compounding;
- repackaging;
- returns;
- waste;
- controlled substances;
- recall management;
- transitions of care;
- discharge medications.

A technology change at one stage can create downstream consequences elsewhere.

---

## 6. Closed-loop medication management

When applicable, analyze continuity across:

**Medication order → Verification → Preparation/Dispensing → Patient identification → Medication identification → Administration → Documentation → Monitoring**

Potential breaks include:

- missing or delayed interfaces;
- manual transcription;
- wrong patient context;
- incorrect medication mapping;
- incorrect or unreadable barcode;
- medication unavailable at the point of care;
- unsynchronized configuration;
- duplicate records;
- incomplete administration documentation;
- loss of safety controls during downtime.

The skill should identify gaps, not declare the loop clinically safe.

---

## 7. Automated dispensing cabinets

Typical ADC-related domains include:

- patient profile availability;
- verified order flow;
- profiled access;
- override workflows;
- user authentication and authorization;
- medication mapping;
- formulary and inventory configuration;
- stocking and replenishment;
- returns;
- discrepancy management;
- controlled substances;
- expiration management;
- emergency access;
- downtime;
- reporting and override monitoring.

A common conceptual flow is:

**EHR order → Pharmacy verification → Interface → ADC patient profile → Nurse access → Medication removal → Administration → Inventory update**

Actual architecture varies by vendor and organization and must be verified.

---

## 8. Barcode medication administration

Relevant BCMA domains include:

- patient identification;
- medication identification;
- active order context;
- timing;
- dose and route representation;
- scanner usability;
- barcode quality;
- reprinted or repackaged medication;
- wrong-patient prevention;
- override/bypass behavior;
- exception handling;
- network dependency;
- device failure;
- documentation;
- downtime.

The analysis should include both system failures and workarounds that users may create.

---

## 9. Smart infusion pumps

Relevant domains include:

- drug library;
- concentrations;
- dosing units;
- dose limits;
- care areas/profiles;
- pump configuration;
- network connectivity;
- library distribution;
- alarm behavior;
- EHR integration when applicable;
- device association;
- programming workflow;
- documentation;
- maintenance;
- downtime.

An integrated workflow may conceptually involve:

**EHR order → MAR/eMAR → Pump programming → Infusion → Pump status/result → EHR documentation**

Do not assume interoperability is present.

---

## 10. EHR and clinical applications

Relevant areas may include:

- registration;
- patient identity;
- encounters;
- ordering;
- medication management;
- documentation;
- results;
- clinical decision support;
- clinical communication;
- scheduling;
- access control;
- reporting;
- integration;
- downtime;
- configuration governance.

The workflow should be analyzed end to end rather than as isolated screens.

---

## 11. Interoperability model

When systems interact, determine when supported:

- source system;
- destination system;
- data exchanged;
- direction;
- trigger/event;
- timing expectation;
- identifier dependencies;
- terminology dependencies;
- source of truth;
- acknowledgement/error handling;
- monitoring;
- retry/reprocessing;
- reconciliation;
- ownership of failures.

Do not assume a specific integration standard solely because systems need to exchange data.

---

## 12. HL7 v2 awareness

HL7 v2 may be relevant to event-driven healthcare interfaces.

When relevant, ask:

- what business/clinical event occurs?
- which system is the source?
- which system is the destination?
- what information is exchanged?
- what acknowledgment behavior exists?
- how are failures queued or retried?
- how are code mappings managed?
- how is patient identity reconciled?
- who monitors failures?

Do not invent message types, segments, fields, or local conventions without evidence.

---

## 13. FHIR awareness

FHIR represents healthcare information through modular resources and standardized exchange patterns.

Potentially relevant resources may include:

- Patient
- Practitioner
- Organization
- Location
- Encounter
- Medication
- MedicationRequest
- MedicationAdministration
- Observation
- DiagnosticReport
- Device
- ServiceRequest
- CarePlan
- Provenance
- AuditEvent

Do not recommend FHIR automatically.

First determine:

- system capability;
- supported FHIR version;
- implementation guide;
- use case;
- existing architecture;
- vendor capability;
- authentication/authorization model;
- terminology requirements;
- operational constraints.

FHIR is an interoperability standard, not a complete security architecture.

---

## 14. Data model

For significant data elements, consider:

- source;
- owner;
- authoritative system;
- format;
- identifier;
- terminology/code system;
- timing;
- destination;
- validation;
- update lifecycle;
- retention when relevant;
- reconciliation.

If multiple systems contain the same information, determine which system is authoritative rather than assuming.

---

## 15. Requirements engineering

A strong requirement should be:

- necessary;
- unambiguous;
- feasible;
- testable;
- traceable;
- appropriately implementation-neutral.

For mandatory requirements, use **shall**.

Avoid vague terms such as:

- fast;
- easy;
- user-friendly;
- seamless;
- adequate;
- appropriate;
- efficient;
- quickly;

unless the term is made measurable.

### Example

Weak:

> The system should be user friendly.

Stronger:

> Authorized nurses shall be able to access the active medication profile for the selected patient after successful authentication.

A measurable response-time or usability target may be added only if supported.

---

## 16. Traceability model

When the task is broad enough, maintain:

**Objective → Problem/Need → Workflow Step → Requirement → Risk/Control → Acceptance Criterion → Validation Evidence**

Requirements that have no identifiable source or rationale should be challenged.

---

## 17. Stakeholder model

Possible stakeholder categories include:

### Clinical

- physicians;
- pharmacists;
- nurses;
- allied health professionals.

### Informatics

- clinical informatics;
- pharmacy informatics;
- nursing informatics.

### Technology

- application analysts;
- interface engineers;
- infrastructure teams;
- network engineers;
- cybersecurity;
- device integration teams.

### Operations

- pharmacy operations;
- nursing operations;
- clinical departments;
- supply chain.

### Governance

- quality;
- patient safety;
- medication safety;
- privacy;
- information security;
- change control.

### External

- vendors;
- implementation partners;
- support providers.

Only include stakeholders supported by the scenario.

---

## 18. Safety reasoning

For clinically relevant workflows, consider:

- wrong patient;
- wrong medication or item;
- wrong clinical context;
- missing information;
- stale information;
- delayed information;
- duplicate activity;
- incorrect mapping/configuration;
- manual transcription;
- workarounds;
- bypasses;
- alert burden;
- cognitive overload;
- interface failure;
- device/system mismatch;
- loss of controls during downtime;
- delayed care;
- hidden failure.

The skill may identify potential hazards and missing controls.

It must not independently certify the workflow as safe.

---

## 19. Human factors

Technology can introduce new error pathways.

Consider:

- cognitive load;
- excessive steps;
- repeated data entry;
- interruptions;
- task switching;
- display clarity;
- alert burden;
- physical placement of devices;
- workflow distance;
- handoff complexity;
- training dependency;
- workaround pressure.

Adding extra confirmation steps does not automatically improve safety.

---

## 20. Automation principle

Automation should preferably:

- remove unnecessary manual work;
- reduce duplicate entry;
- reduce transcription;
- improve information availability;
- improve traceability;
- detect exceptions;
- support standardization.

Automation should not silently:

- replace clinical judgment;
- hide failure;
- introduce unverified information;
- eliminate justified safeguards;
- remove necessary human oversight.

---

## 21. Exception-based design

For high-volume workflows, routine cases should avoid unnecessary interaction where safe and appropriate.

Human attention should be directed toward:

- exceptions;
- risks;
- conflicts;
- missing information;
- failed interfaces;
- abnormal conditions.

This principle should never be used to remove required safeguards without validation.

---

## 22. Downtime and continuity

A critical workflow should consider:

**Normal operation → Failure detection → Communication → Fallback → Documentation → Restoration → Reconciliation**

Potential failure modes include:

- EHR outage;
- interface/API outage;
- network outage;
- device outage;
- authentication outage;
- power interruption;
- barcode/scanner failure;
- printing failure;
- server failure;
- delayed messages;
- partial functionality.

A downtime plan is incomplete if it explains only fallback and not restoration/reconciliation.

---

## 23. Testing model

Possible test layers include:

### Functional

Does the feature behave as specified?

### Integration

Do systems exchange the expected information?

### Workflow

Does the end-to-end process work?

### Negative

What happens with missing, invalid, duplicate, or conflicting data?

### Failure/downtime

What happens when a dependency is unavailable?

### User acceptance

Can intended users complete the required workflow?

### Regression

Did the change damage existing behavior?

### Production validation

Does the deployed configuration work in the target environment?

---

## 24. Scenario-based testing

Testing should include realistic end-to-end workflows and exception paths.

Example:

**Patient admitted → Medication ordered → Pharmacist verifies → Order reaches ADC → Nurse authenticates → Patient selected → Medication removed → Patient scanned → Medication scanned → Medication administered → Administration documented**

Exception variants may include:

- interface unavailable;
- medication unavailable;
- barcode unreadable;
- wrong patient selected;
- override attempted;
- ADC offline.

Do not treat this example as a universal local workflow.

---

## 25. Implementation lifecycle

A health IT project may progress through:

**Problem identification → Discovery → Current-state analysis → Requirements → Future-state design → Configuration/build → Testing → Training/readiness → Deployment → Go-live → Stabilization → Optimization**

Workflow analysis should continue after implementation because real-world use may reveal workarounds, new risks, and optimization opportunities.

---

## 26. Go-live readiness

Potential readiness domains include:

- validated configuration;
- validated interfaces;
- hardware readiness;
- network readiness;
- user provisioning;
- training;
- support model;
- escalation path;
- downtime process;
- mapping/data validation;
- workflow approval;
- cutover plan;
- rollback/contingency where relevant.

Passing software tests alone does not establish operational readiness.

---

## 27. Post-go-live monitoring

Potential measures include:

- workflow completion time;
- error rate;
- override rate;
- scan compliance;
- interface failure rate;
- support tickets;
- user adoption;
- workarounds;
- medication turnaround time;
- alert behavior;
- system availability;
- user feedback.

Measures should be tied to the implementation objective.

---

## 28. Evidence and uncertainty

Use four categories:

### Known

Explicitly supported by supplied or verified information.

### Inferred

Reasonably derived but not directly confirmed.

### Assumed

Temporarily adopted so analysis can continue.

### Unknown

Cannot be determined from available information.

Do not present inferred, assumed, or unknown information as known.

When missing information materially affects safety, architecture, workflow, compliance, or acceptance, flag it for validation.

---

## 29. No-hallucination rule

Do not invent:

- hospital policy;
- vendor functionality;
- system configuration;
- interface architecture;
- message structure;
- user permissions;
- clinical thresholds;
- medication policy;
- regulatory requirements;
- approvals.

Use:

**Insufficient information — validation required.**

or explicitly label an assumption.

---

## 30. Safety boundary

The skill may:

- identify potential risk;
- identify missing controls;
- identify workflow weakness;
- identify integration dependency;
- identify missing validation.

It must not independently:

- diagnose;
- prescribe;
- select patient-specific therapy;
- determine patient-specific medication dosing;
- declare clinical safety;
- certify compliance;
- approve a clinical workflow;
- replace governance.

---

## 31. Domain reasoning sequence

For a broad healthcare technology scenario, think in this order:

**Why** — What problem are we solving?  
**Who** — Who participates?  
**Now** — What happens today?  
**Risk** — Where can the workflow fail or cause harm?  
**Future** — What should happen instead?  
**Technology** — What technology supports the future state?  
**Information** — What data must move?  
**Requirements** — What must the solution accomplish?  
**Exceptions** — What happens when normal assumptions fail?  
**Validation** — How will we prove it works?  
**Operations** — How will it remain safe and effective after go-live?

Execution details and output behavior belong in `SKILL.md`; this knowledge base should remain a domain reference rather than a second prompt.
