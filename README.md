# Healthcare Clinical Workflow Analyst

An open-source Agent Skill for structured, safety-aware analysis of healthcare operations and health IT workflows.

It helps an AI agent examine AS-IS and TO-BE workflows, stakeholder responsibilities, requirements, interoperability, medication technology, downtime, risks, acceptance criteria, and validation without inventing local policy or replacing clinical governance.

## Use cases

- EHR and clinical application workflow analysis
- Pharmacy systems and medication-use workflows
- Automated dispensing cabinet implementation or optimization
- Barcode medication administration safety review
- Smart infusion pump workflow and integration analysis
- Interface, data, downtime, go-live readiness, and UAT planning

It is not a clinical decision-support system and must not be used for patient-specific diagnosis, treatment selection, prescribing, or dosing.

## Install

Place the `healthcare-clinical-workflow-analyst` directory in the skills directory supported by your agent environment. Invoke it explicitly as `$healthcare-clinical-workflow-analyst`, or allow normal automatic discovery.

## Package structure

- `SKILL.md`: activation, method, boundaries, output behavior, and quality checks
- `KNOWLEDGE_BASE.md`: core healthcare workflow and informatics domain model
- `references/`: focused topic guidance loaded only when relevant
- `templates/`: reusable analysis artifacts
- `examples/`: realistic demonstrations with explicit assumptions
- `evals/`: trigger cases, behavior cases, and scoring rubric
- `tests/validate_package.py`: deterministic package integrity test
- `PROJECT_SCOPE.md`: product boundaries and release gates
- `SOURCES.md`: authoritative evidence registry

## Validate

Run:

```bash
python tests/validate_package.py
```

The package should also pass the platform skill validator before release.

## Release status

Draft RC2 for personal testing. Adds explicit handling of stakeholder reports versus verified causes, locally approved reporting definitions, ADC controlled-substance scope, and existing downtime evidence. Example outputs are demonstrations, not proof that a live workflow, system, device, or organization is safe, compliant, or implementation-ready. Structural checks and limited AI forward tests do not establish v1.0 release readiness.

## License

MIT. See `LICENSE`.
