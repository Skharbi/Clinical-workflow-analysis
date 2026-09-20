#!/usr/bin/env python3
"""Deterministic integrity checks for the skill source package."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "healthcare-clinical-workflow-analyst"

REQUIRED = {
    "plugin.json",
    ".codex-plugin/plugin.json",
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "PRIVACY.md",
    "TERMS.md",
    "SUPPORT.md",
    "SUBMISSION.md",
    "assets/icon.svg",
    "assets/workflow-analyst-overview.svg",
    "SKILL.md",
    "PROJECT_SCOPE.md",
    "KNOWLEDGE_BASE.md",
    "SOURCES.md",
    "agents/openai.yaml",
    "references/safety-and-human-factors.md",
    "references/evidence-and-uncertainty.md",
    "references/workflow-analysis.md",
    "references/interoperability-and-data.md",
    "references/medication-technology.md",
    "references/project-and-business-analysis.md",
    "references/requirements-engineering.md",
    "references/testing-and-validation.md",
    "references/downtime-and-continuity.md",
    "templates/workflow-assessment.md",
    "templates/requirements-and-traceability.md",
    "templates/risk-validation-and-readiness.md",
    "examples/adc-implementation.md",
    "examples/bcma-safety-review.md",
    "examples/smart-pump-integration.md",
    "evals/trigger-cases.md",
    "evals/behavior-cases.md",
    "evals/scoring-rubric.md",
    "evals/cases.json",
    "evals/run_evals.py",
    "evals/independent-scenarios.md",
    "evals/FORWARD_TEST_V1.0.4.md",
    "skills/healthcare-clinical-workflow-analyst/SKILL.md",
    "skills/healthcare-clinical-workflow-analyst/PROJECT_SCOPE.md",
    "skills/healthcare-clinical-workflow-analyst/KNOWLEDGE_BASE.md",
    "skills/healthcare-clinical-workflow-analyst/SOURCES.md",
    "skills/healthcare-clinical-workflow-analyst/agents/openai.yaml",
    "skills/healthcare-clinical-workflow-analyst/assets/icon.svg",
    "skills/healthcare-clinical-workflow-analyst/assets/workflow-analyst-overview.svg",
    "skills/healthcare-clinical-workflow-analyst/references/safety-and-human-factors.md",
    "skills/healthcare-clinical-workflow-analyst/references/evidence-and-uncertainty.md",
    "skills/healthcare-clinical-workflow-analyst/references/workflow-analysis.md",
    "skills/healthcare-clinical-workflow-analyst/references/interoperability-and-data.md",
    "skills/healthcare-clinical-workflow-analyst/references/medication-technology.md",
    "skills/healthcare-clinical-workflow-analyst/references/project-and-business-analysis.md",
    "skills/healthcare-clinical-workflow-analyst/references/requirements-engineering.md",
    "skills/healthcare-clinical-workflow-analyst/references/testing-and-validation.md",
    "skills/healthcare-clinical-workflow-analyst/references/downtime-and-continuity.md",
    "skills/healthcare-clinical-workflow-analyst/templates/workflow-assessment.md",
    "skills/healthcare-clinical-workflow-analyst/templates/requirements-and-traceability.md",
    "skills/healthcare-clinical-workflow-analyst/templates/risk-validation-and-readiness.md",
    "skills/healthcare-clinical-workflow-analyst/examples/adc-implementation.md",
    "skills/healthcare-clinical-workflow-analyst/examples/bcma-safety-review.md",
    "skills/healthcare-clinical-workflow-analyst/examples/smart-pump-integration.md",
    "skills/healthcare-clinical-workflow-analyst/evals/trigger-cases.md",
    "skills/healthcare-clinical-workflow-analyst/evals/behavior-cases.md",
    "skills/healthcare-clinical-workflow-analyst/evals/scoring-rubric.md",
    "skills/healthcare-clinical-workflow-analyst/evals/cases.json",
    "skills/healthcare-clinical-workflow-analyst/evals/run_evals.py",
    "skills/healthcare-clinical-workflow-analyst/evals/independent-scenarios.md",
    "skills/healthcare-clinical-workflow-analyst/evals/FORWARD_TEST_V1.0.4.md",
    ".github/workflows/evals.yml",
    "tests/validate_package.py",
}


IGNORED_DIRECTORIES = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
}

IGNORED_FILES = {
    ".DS_Store",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def is_package_file(path: Path) -> bool:
    """Return whether a file belongs to the distributable skill package."""
    relative = path.relative_to(ROOT)
    return (
        path.is_file()
        and not any(part in IGNORED_DIRECTORIES for part in relative.parts)
        and path.name not in IGNORED_FILES
        and path.suffix != ".pyc"
    )


missing = sorted(path for path in REQUIRED if not (ROOT / path).is_file())
if missing:
    fail(f"missing required files: {', '.join(missing)}")

actual = {str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if is_package_file(path)}
if actual != REQUIRED:
    extra = sorted(actual - REQUIRED)
    missing_from_tree = sorted(REQUIRED - actual)
    fail(f"unexpected package tree; extra={extra}, missing={missing_from_tree}")

skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n"):
    fail("SKILL.md lacks YAML frontmatter")
if "name: healthcare-clinical-workflow-analyst" not in skill:
    fail("skill name is missing or inconsistent")
if re.search(r"\bTODO\b|\[TODO", skill, flags=re.IGNORECASE):
    fail("SKILL.md contains unfinished placeholders")

for path in sorted(ROOT.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        fail(f"empty Markdown file: {path.relative_to(ROOT)}")

for relative in (
    "SKILL.md",
    "PROJECT_SCOPE.md",
    "KNOWLEDGE_BASE.md",
    "SOURCES.md",
    "agents/openai.yaml",
    "references/safety-and-human-factors.md",
    "references/evidence-and-uncertainty.md",
    "references/workflow-analysis.md",
    "references/interoperability-and-data.md",
    "references/medication-technology.md",
    "references/project-and-business-analysis.md",
    "references/requirements-engineering.md",
    "references/testing-and-validation.md",
    "references/downtime-and-continuity.md",
    "templates/workflow-assessment.md",
    "templates/requirements-and-traceability.md",
    "templates/risk-validation-and-readiness.md",
    "examples/adc-implementation.md",
    "examples/bcma-safety-review.md",
    "examples/smart-pump-integration.md",
    "evals/trigger-cases.md",
    "evals/behavior-cases.md",
    "evals/scoring-rubric.md",
    "evals/cases.json",
    "evals/run_evals.py",
    "evals/independent-scenarios.md",
    "evals/FORWARD_TEST_V1.0.4.md",
):
    if (ROOT / relative).read_bytes() != (SKILL_ROOT / relative).read_bytes():
        fail(f"plugin skill copy is out of sync: {relative}")

print(f"PASS: {len(actual)} required files present; package integrity checks succeeded")
