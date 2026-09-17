#!/usr/bin/env python3
"""Deterministic integrity checks for the skill source package."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "SKILL.md",
    "PROJECT_SCOPE.md",
    "KNOWLEDGE_BASE.md",
    "SOURCES.md",
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "agents/openai.yaml",
    "references/safety-and-human-factors.md",
    "references/evidence-and-uncertainty.md",
    "references/workflow-analysis.md",
    "references/interoperability-and-data.md",
    "references/medication-technology.md",
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

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
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

print(f"PASS: {len(actual)} required files present; package integrity checks succeeded")
