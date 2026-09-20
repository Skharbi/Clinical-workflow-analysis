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

The default final analysis is displayed in this order:

1. **Decision Brief** — the problem, bottom line, expected change, primary concern, and next action.
2. **Workflow at a Glance** — current state versus target state and the main impact.
3. **Priority Findings** — only the findings that materially affect the decision.
4. **Open Decisions and Next Action** — blocking, important, and optimization items with a clear
   handoff.

"Final analysis" does not automatically mean "full report." Detailed requirements, risks, interfaces,
downtime, testing, stakeholder inventories, and implementation sections are added only when the user
asks for them or a specific detail is needed to explain a material blocker or safety issue.

Focused requests also stay focused: if the user asks for exactly five requirements, the skill returns
five requirements rather than expanding into a workflow report. Users can still request a
comprehensive report, PDF-ready/formal PDF output when the host supports file generation, or an
executive email summary.
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

The runner supports DeepSeek and OpenAI. Provider selection defaults to `auto`: DeepSeek is preferred
when `DEEPSEEK_API_KEY` is present, otherwise OpenAI is used when `OPENAI_API_KEY` is present.

```bash
python -m pip install --upgrade openai

# DeepSeek
export DEEPSEEK_API_KEY="..."
python evals/run_evals.py --suite smoke

# OpenAI fallback
export OPENAI_API_KEY="..."
python evals/run_evals.py --provider openai --suite smoke
```

Available suites are `smoke`, `full`, `trigger`, `behavior`, and `independent`. DeepSeek
defaults to `deepseek-flash`; OpenAI defaults to `gpt-5.6-luna`. Override either model with
`EVAL_MODEL` and `EVAL_JUDGE_MODEL`.

GitHub Actions runs deterministic validation on every pull request and push to `main`. When either
`DEEPSEEK_API_KEY` or `OPENAI_API_KEY` is configured, pull requests also run the live smoke suite.
Manual and weekly scheduled runs can execute the full suite and upload the machine-readable and
Markdown reports as workflow artifacts.

The package should also pass the platform skill validator before release.

## Release status

v1.0.6, proportional-output release candidate. It keeps the v1.0.5 multi-provider regression
pipeline and tightens two behaviors identified by the first full DeepSeek run: focused requests now
treat explicit artifact/count/format exclusions as hard output boundaries, and a request for a final
analysis no longer expands into a comprehensive report by default. EV-05 and EV-17 are promoted into
the smoke suite to prevent regression. Automated evaluation is regression evidence, not clinical
validation, compliance certification, or organizational approval.

## License

MIT. See `LICENSE`.
