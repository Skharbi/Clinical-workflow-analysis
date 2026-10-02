# Downtime and Continuity Reference

Use when workflow depends on critical technology.

## Model

**Normal operation → Failure detection → Communication → Fallback → Documentation → Restoration → Reconciliation**

## Consider as relevant

- EHR outage;
- interface/API outage;
- network failure;
- authentication failure;
- device outage;
- power failure;
- printing failure;
- barcode/scanner failure;
- delayed messages;
- partial functionality.

## Key questions

- How is failure recognized?
- Who is notified?
- Which controls are lost?
- What is the safe fallback?
- How is work documented?
- How is normal operation restored?
- How is manual/downtime work reconciled?
- Who verifies reconciliation?

A fallback plan without restoration and reconciliation is incomplete.

## Entry and recovery gates

Identify who declares degraded/downtime operation, which functions remain usable, required fallback
resources, backlog priority, and who authorizes return to normal service. Reconcile manual records
and queued transactions using verified identity/context, duplicate prevention, exception ownership,
and an evidence record. Do not replay stale or conflicting transactions blindly. Connectivity
restoration alone is insufficient while clinically consequential conflicts remain unresolved.
Do not invent recovery-time targets or vendor offline behavior.
