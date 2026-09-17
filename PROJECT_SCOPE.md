# Healthcare Clinical Workflow Analyst — Project Scope

**Version:** 1.1  
**Project status:** Foundation / pre-evaluation  
**Project type:** Open-source Agent Skill  
**Domain:** Healthcare informatics, clinical workflow, medication-use technology, and health IT implementation  
**Last reviewed:** 2026-09-16

---

## 1. Purpose

The Healthcare Clinical Workflow Analyst is a reusable Agent Skill that helps AI agents analyze healthcare technology workflows in a structured, safe, traceable, and implementation-oriented manner.

It is intended to improve consistency in healthcare informatics analysis by supplying a repeatable method for workflow discovery, requirements development, risk analysis, interoperability review, downtime planning, and validation.

The skill is not a clinical decision-support system.

---

## 2. Problem

Generic AI systems can produce plausible healthcare workflow analysis while still:

- jumping to a solution before defining the problem;
- describing software features rather than the end-to-end workflow;
- mixing current-state and future-state processes;
- missing physical workflow, handoffs, cognitive work, or exceptions;
- inventing local policy, system behavior, integration architecture, or vendor capability;
- failing to distinguish fact from assumption;
- producing requirements that are vague or untestable;
- ignoring downtime, restoration, or reconciliation;
- overlooking patient-safety, medication-safety, and human-factors implications;
- overproducing generic reports when a focused artifact is required.

This project exists to make healthcare workflow analysis more repeatable, evidence-aware, transparent, and operationally useful.

---

## 3. Product outcome

When appropriately triggered, the skill should help an AI agent:

1. define the problem, objective, scope, and constraints;
2. distinguish known facts, inference, assumptions, and unknowns;
3. model the relevant AS-IS workflow;
4. identify stakeholders and responsibilities;
5. identify workflow pain points and failure points;
6. design a TO-BE workflow when requested;
7. derive traceable, specific, and testable requirements;
8. identify relevant safety and operational risks;
9. identify data and interoperability dependencies;
10. analyze downtime and exception handling;
11. define acceptance criteria and validation scenarios;
12. expose unresolved questions without inventing answers;
13. maintain traceability from objective to validation;
14. leave final clinical, technical, legal, regulatory, and governance decisions to qualified humans.

---

## 4. Target users

### Primary

- Clinical informaticists
- Pharmacy informaticists
- Health informaticians
- Healthcare business analysts
- Clinical application analysts
- Healthcare IT analysts
- Pharmacy automation specialists
- Medication-safety professionals
- Implementation specialists
- Solution consultants
- Digital health teams
- Healthcare project managers

### Secondary

- Physicians
- Pharmacists
- Nurses
- Allied health professionals
- Biomedical/clinical engineering teams
- Integration teams
- Infrastructure and network teams
- Quality and patient-safety teams
- Cybersecurity and privacy teams
- Healthcare administrators
- Health technology vendors

Stakeholders must be selected from the scenario. The skill must not mechanically insert every possible role.

---

## 5. In-scope capabilities

### Workflow analysis

- AS-IS workflow discovery
- TO-BE workflow design
- Task, decision, handoff, and exception mapping
- Human-system interaction
- Physical and cognitive workflow
- Workaround identification
- Failure-path analysis
- Workflow optimization

### Requirements engineering

- Functional requirements
- Clinical workflow requirements
- Non-functional requirements
- Integration requirements
- Data requirements
- Operational requirements
- Security/privacy considerations
- Reporting/analytics requirements
- Downtime requirements
- Acceptance criteria

### Healthcare technology domains

Examples include:

- EHR and clinical applications
- CPOE
- Clinical decision support workflow
- Pharmacy information systems
- Automated dispensing cabinets
- Pharmacy robotics and carousel systems
- BCMA
- Smart infusion pumps
- Medication administration technology
- Clinical device connectivity
- Interfaces, APIs, HL7 v2, and FHIR
- Clinical system upgrades
- Post-go-live optimization
- Downtime and recovery
- Workflow incident analysis

The list is illustrative, not exhaustive.

---

## 6. Out of scope

The skill must not independently:

- diagnose a patient;
- recommend patient-specific treatment;
- prescribe medication;
- choose a patient-specific medication or dose;
- certify a workflow as clinically safe;
- provide regulatory approval;
- certify compliance;
- certify a medical device;
- perform formal cybersecurity certification;
- replace local policy review;
- replace clinical governance;
- replace technical architecture review;
- replace formal validation or user acceptance testing;
- make autonomous clinical decisions.

It may identify risks, missing controls, gaps, or areas requiring expert review.

---

## 7. Operating model

The skill uses progressive disclosure.

### `SKILL.md`

Contains:

- activation conditions;
- execution method;
- safety boundaries;
- uncertainty rules;
- output behavior;
- quality checks.

### `KNOWLEDGE_BASE.md`

Contains the domain model and core healthcare informatics principles.

### `references/`

Contains narrower topic references that should be loaded only when relevant.

### `examples/`

Shows expected behavior on realistic scenarios.

### `evals/`

Tests whether the skill:

- triggers when it should;
- avoids triggering when it should not;
- improves output quality relative to a baseline;
- respects safety and uncertainty rules;
- produces usable artifacts.

---

## 8. Required analytical properties

A good output should be:

### Traceable

Requirements and controls must connect to a need, workflow step, stakeholder, problem, or risk.

### Specific

Avoid vague recommendations.

### Testable

Important requirements should have an observable validation method.

### Workflow-driven

The workflow comes before the feature list.

### Clinically aware

Technology must be analyzed in the context of clinical operations.

### Safety-aware

Potential harm pathways and loss of controls should be considered when relevant.

### Evidence-aware

Known facts must be separated from assumptions and inference.

### Human-governed

The skill supports decisions but does not become the final authority.

### Proportionate

The output should match the user's requested artifact and level of detail.

---

## 9. Data and privacy principles

The skill should:

- use the minimum information necessary;
- prefer fictional or de-identified examples;
- avoid requesting patient identifiers when not needed;
- never invent patient information;
- avoid exposing unnecessary sensitive organizational details;
- distinguish supplied local policy from generic best practice;
- flag privacy and security dependencies when they materially affect the workflow.

---

## 10. Evidence model

When external evidence is required, prefer:

1. applicable law or regulation;
2. official standards organizations;
3. government health agencies;
4. recognized patient-safety organizations;
5. professional societies;
6. peer-reviewed literature;
7. official vendor documentation;
8. supplied local organizational policy;
9. documented stakeholder evidence;
10. general web sources.

Local organizational policy and configuration may differ from external best practice.

The skill must not treat generic guidance as local policy.

---

## 11. MVP deliverables

Version 0.1.0 should include:

- production `SKILL.md`;
- project scope;
- knowledge base;
- evidence/source registry;
- modular references;
- reusable templates;
- three demonstration scenarios;
- trigger tests;
- behavior evals;
- scoring rubric;
- contribution guide;
- open-source license;
- README.

---

## 12. MVP demonstration scenarios

The first three scenarios should cover different combinations of workflow, medication safety, devices, integration, and downtime:

1. Automated dispensing cabinet implementation
2. BCMA safety review
3. Smart infusion pump integration

---

## 13. Evaluation requirements

The skill must be tested against a baseline without the skill.

At minimum, evaluate:

### Trigger accuracy

Does the skill activate for relevant workflow-analysis requests?

Does it remain inactive for patient-specific clinical treatment questions?

### Problem framing

Does it define the actual problem and scope before proposing a solution?

### Evidence discipline

Does it distinguish known, inferred, assumed, and unknown information?

### Workflow completeness

Does it include people, systems, devices, data, decisions, handoffs, exceptions, and outcome when relevant?

### Requirements quality

Are requirements specific, traceable, and testable?

### Safety coverage

Are clinically relevant safety and downtime concerns identified without making unsupported clinical judgments?

### Interoperability discipline

Does it avoid inventing standards, messages, resources, or architecture?

### Validation quality

Are acceptance criteria observable and meaningful?

### Usability

Is the output proportionate and operationally useful?

---

## 14. Release gate for v1.0

Do not label the project v1.0 until:

- the core eval suite has been executed;
- trigger and non-trigger cases have been tested;
- the skill shows material quality improvement over baseline on the majority of intended-use evals;
- no critical safety-boundary failure is observed;
- no repeated hallucination pattern is identified in system/vendor/policy assumptions;
- example outputs have been reviewed;
- documentation and installation instructions are complete.

A failed safety-boundary test blocks release regardless of aggregate score.

---

## 15. Future scope

Future specialist skills may be separated into their own packages:

- Medication Safety Workflow Reviewer
- Healthcare Requirements Analyst
- Clinical System Implementation Planner
- Healthcare Interoperability Reviewer
- Pharmacy Automation Analyst
- Clinical Downtime Planner
- Healthcare UAT Scenario Designer

The main skill should not become a single oversized prompt covering every health IT specialty.

---

## 16. Definition of success

The project succeeds when an independent user can install the skill, provide a previously unseen healthcare technology scenario, and receive a structured analysis that is:

- useful;
- traceable;
- uncertainty-aware;
- safety-aware;
- technically disciplined;
- proportionate;
- testable;
- clearly governed by human validation.

The goal is not impressive prose.

The goal is a repeatable healthcare informatics analysis capability.
