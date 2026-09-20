# Medication Technology Reference

Use for pharmacy automation, ADC, BCMA, smart pump, medication distribution, and closed-loop medication workflows.

## Medication-use lifecycle

**Prescribing → Verification → Preparation → Dispensing → Distribution → Administration → Monitoring**

Additional processes may include reconciliation, procurement, inventory, storage, returns, waste, controlled substances, recalls, and transitions of care.

## Event semantics

Keep workflow events distinct unless local policy, system behavior, and governance evidence explicitly support equivalence.

Examples:

- inventory decrement is not automatically medication administration;
- ADC removal is not automatically medication administration;
- preparation is not administration;
- dispensing is not administration;
- a device transaction is not automatically the authoritative clinical documentation event.

When one event is proposed to represent another, identify the source of truth, required user verification,
exception path, audit trail, downstream documentation effect, and approval/validation evidence.

## ADC

Assess as relevant:

- verified order flow;
- patient profiles;
- overrides;
- authentication;
- medication mapping;
- inventory;
- replenishment;
- controlled substances;
- returns;
- discrepancies;
- emergency access;
- downtime.

## BCMA

Assess as relevant:

- patient wristband;
- medication barcode;
- active order;
- scanner/device;
- wrong-patient prevention;
- exception workflow;
- bypass/override;
- documentation;
- network/device failure;
- downtime.

## Smart pumps

Assess as relevant:

- drug library;
- concentrations;
- units;
- dose limits;
- care area;
- pump configuration;
- network;
- library distribution;
- EHR integration;
- pump association;
- documentation;
- maintenance;
- downtime.

Do not assume vendor-specific behavior.
