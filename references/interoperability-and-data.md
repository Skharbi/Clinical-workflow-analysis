# Interoperability and Data Reference

Use when multiple systems, applications, or devices exchange information.

## Interface analysis

Identify when known:

- source;
- destination;
- trigger/event;
- data;
- direction;
- timing;
- identifiers;
- terminology;
- source of truth;
- acknowledgement/error handling;
- monitoring;
- retry/reprocessing;
- reconciliation;
- failure ownership.

## Lifecycle and replay

Check relevant cancellations, amendments, patient/encounter/case changes or merges, duplicate replay,
out-of-order events, clock/timestamp interpretation, and stale-state policy. Identify what evidence
shows correct final state after retry and recovery. A successful acknowledgement does not by itself
prove correct clinical state. Propose negative scenarios without inventing message types or guarantees.

## Standards discipline

Do not assume:

- HL7 v2;
- FHIR;
- REST API;
- proprietary interface;
- middleware;
- a particular message type;
- a particular FHIR resource.

Select or discuss a standard only when supported by the implementation context.

## Data quality questions

- Is the data complete?
- Is it current?
- Is it mapped correctly?
- Is identity resolved?
- Is the authoritative source known?
- What happens when information conflicts?
- Who reconciles failures?
