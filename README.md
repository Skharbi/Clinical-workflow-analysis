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

## What the user experiences

During discovery, the skill summarizes what it understands, shows what is complete or missing, asks
one material question at a time by default, and reassesses after every answer. It stops discovery as
soon as a responsible first-pass analysis is possible instead of trying to eliminate every unknown.

A full analysis is displayed in this order:

1. **Decision Brief** — the problem, bottom line, expected change, primary concern, and next action.
2. **Workflow at a Glance** — current state versus target state and the main impact.
3. **Priority Findings** — the most important findings, evidence status, and recommended action.
4. **Detailed Analysis** — only the workflow, requirements, risks, interfaces, downtime, and tests
   relevant to the scenario.
5. **Open Decisions and Next Action** — blocking, important, and optimization items with a clear
   handoff.

The skill does not use a fixed 15-section report when a shorter artifact will answer the question.
By default it keeps the final response decision-focused. Users can request a comprehensive report,
PDF-ready/formal PDF output when the host supports file generation, or an executive email summary.
Email sending requires an authorized mail capability and an explicit send request.

## Use it on ChatGPT mobile

**Not available yet.** The package is ready, but it must be submitted to and approved by OpenAI before people can install it in the ChatGPT mobile app. Mobile users will not need PowerShell or a terminal after publication.

## Install

Run the command on your **computer** in PowerShell, Windows Terminal, or a macOS/Linux terminal. Do not paste it into a ChatGPT conversation. [Node.js](https://nodejs.org/) must be installed.

### Codex

```powershell
npx -y skills add Skharbi/Clinical-workflow-analysis --skill healthcare-clinical-workflow-analyst --global --agent codex --yes
```

Restart Codex. The skill is ready.

### Claude Code

```powershell
npx -y skills add Skharbi/Clinical-workflow-analysis --skill healthcare-clinical-workflow-analyst --global --agent claude-code --yes
```

Restart Claude Code. The skill is ready.

## Package structure

- `plugin.json`: portable Agent Plugins manifest for ChatGPT and Codex distribution
- `skills/healthcare-clinical-workflow-analyst/SKILL.md`: activation, method, boundaries, output behavior, and quality checks
- `skills/healthcare-clinical-workflow-analyst/KNOWLEDGE_BASE.md`: core healthcare workflow and informatics domain model
- `skills/healthcare-clinical-workflow-analyst/references/`: focused topic guidance loaded only when relevant
- `skills/healthcare-clinical-workflow-analyst/templates/`: reusable analysis artifacts
- `skills/healthcare-clinical-workflow-analyst/examples/`: realistic demonstrations with explicit assumptions
- `skills/healthcare-clinical-workflow-analyst/evals/`: trigger cases, behavior cases, and scoring rubric
- `tests/validate_package.py`: deterministic package integrity test
- `PRIVACY.md`, `TERMS.md`, and `SUPPORT.md`: public submission policies and support route

## Validate

Deterministic package and registry checks require no API key:

```bash
python tests/validate_package.py
python evals/run_evals.py --validate-only
```

Live regression evaluation compares a generic baseline with the skill-assisted answer, scores both
against the repository rubric, blocks on critical failures, and writes `eval-results/results.json`
plus `eval-results/report.md`.

```bash
python -m pip install --upgrade openai
export OPENAI_API_KEY="..."
python evals/run_evals.py --suite smoke
python evals/run_evals.py --suite full
```

Available suites are `smoke`, `full`, `trigger`, `behavior`, and `independent`. The default
live model and judge model are `gpt-5.6-luna`; override them with `EVAL_MODEL` and
`EVAL_JUDGE_MODEL` when needed.

GitHub Actions runs deterministic validation on every pull request and push to `main`. When the
repository secret `OPENAI_API_KEY` is configured, pull requests also run the live smoke suite.
Manual and weekly scheduled runs can execute the full suite and upload the machine-readable and
Markdown reports as workflow artifacts.

The package should also pass the platform skill validator before release.

## Release status

v1.0.4, automated-evaluation release candidate. It keeps the v1.0.3 discovery, event-semantics,
decision-focused output, PDF/report, and executive-email safeguards while adding a machine-readable
evaluation registry, automated baseline-versus-skill scoring, trigger classification, critical-failure
release gates, GitHub Actions CI, and seven independent regression scenarios spanning medication and
non-medication clinical workflows. Automated evaluation is regression evidence, not clinical
validation, compliance certification, or organizational approval.

## License

MIT. See `LICENSE`.
