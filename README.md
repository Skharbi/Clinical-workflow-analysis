# Healthcare Clinical Workflow Analyst

An open-source Agent Skill for structured, safety-aware analysis of healthcare operations and health IT workflows.

![Healthcare Clinical Workflow Analyst overview](assets/workflow-analyst-overview.svg)

It helps an AI agent examine AS-IS and TO-BE workflows, stakeholder responsibilities, requirements, interoperability, medication technology, downtime, risks, acceptance criteria, and validation without inventing local policy or replacing clinical governance.

Its project and business-analysis discipline is aligned with adaptable PMI and IIBA practices:
understand the need before selecting a solution, engage the right stakeholders, maintain requirement
traceability and change rationale, distinguish verification from acceptance, and evaluate outcomes.
Those practices complement healthcare safety and informatics guidance; they do not replace it.

## Use cases

- EHR and clinical application workflow analysis
- Pharmacy systems and medication-use workflows
- Automated dispensing cabinet implementation or optimization
- Barcode medication administration safety review
- Smart infusion pump workflow and integration analysis
- Interface, data, downtime, go-live readiness, and UAT planning

It is not a clinical decision-support system and must not be used for patient-specific diagnosis, treatment selection, prescribing, or dosing.

## Install in one command

For Codex, run:

```bash
npx -y skills add Skharbi/Clinical-workflow-analysis --skill healthcare-clinical-workflow-analyst --global --agent codex --yes
```

That is the complete installation. Restart Codex if it is already open, then use the skill normally or invoke it explicitly as `$healthcare-clinical-workflow-analyst`.

The same installer supports other compatible agents. Omit `--agent codex` to select the target interactively:

```bash
npx -y skills add Skharbi/Clinical-workflow-analysis
```

Requires Node.js and `npx`. Users who cannot run Node.js can download the repository ZIP and place the extracted `healthcare-clinical-workflow-analyst` folder in their agent's supported skills directory.

To update later:

```bash
npx skills update
```

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

Draft RC3 for personal testing. Adds PMI/IIBA-aligned need, value, stakeholder, requirements-life-cycle,
change-control, acceptance, and benefits-evaluation discipline while preserving healthcare safety and
human-governance boundaries. Example outputs are demonstrations, not proof that a live workflow,
system, device, or organization is safe, compliant, or implementation-ready. Structural checks and
limited AI forward tests do not establish v1.0 release readiness.

## License

MIT. See `LICENSE`.
