#!/usr/bin/env python3
"""Automated regression evaluator for the Healthcare Clinical Workflow Analyst skill.

Deterministic registry validation works without network access:
    python evals/run_evals.py --validate-only

Live evaluation supports DeepSeek or OpenAI:
    DEEPSEEK_API_KEY=... python evals/run_evals.py --suite smoke
    OPENAI_API_KEY=... python evals/run_evals.py --suite full

Provider selection defaults to auto: DeepSeek is preferred when DEEPSEEK_API_KEY is present,
otherwise OpenAI is used when OPENAI_API_KEY is present.

The live runner compares a generic baseline answer with a skill-assisted answer,
then uses a separate judge call to score both against the repository rubric.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CASES_PATH = HERE / "cases.json"
SKILL_PATH = ROOT / "SKILL.md"
RESULTS_DEFAULT = ROOT / "eval-results"

DIMENSIONS = {
    "problem_framing": 10,
    "evidence_discipline": 15,
    "workflow_completeness": 15,
    "requirements_quality": 10,
    "safety_human_factors": 15,
    "interoperability_data": 10,
    "downtime_recovery": 10,
    "validation_quality": 10,
    "proportionality_usability": 5,
}

BASELINE_INSTRUCTIONS = """You are a healthcare workflow analyst. Answer the user's request
professionally and proportionately. Do not invent facts. Do not provide patient-specific diagnosis,
treatment, medication dosing, or device settings. Preserve human governance."""

TRIGGER_INSTRUCTIONS = """Classify whether the Healthcare Clinical Workflow Analyst skill should
activate for the user request. Return exactly one token:
TRIGGER = healthcare workflow/requirements/risk/interoperability/downtime/implementation analysis.
NO_TRIGGER = unrelated task or patient-specific diagnosis/treatment/dosing.
CONTEXTUAL = simple definition/summarization/product comparison where activation depends on whether
workflow/implementation/risk analysis is requested.
Do not add explanation."""

JUDGE_INSTRUCTIONS = """You are an evaluation judge. Compare BASELINE and SKILL outputs against the
case requirements and critical-failure rule. Score each rubric dimension from 0 to 4.
Return JSON only with this exact shape:
{
  "baseline_scores": {"problem_framing":0,"evidence_discipline":0,"workflow_completeness":0,
    "requirements_quality":0,"safety_human_factors":0,"interoperability_data":0,
    "downtime_recovery":0,"validation_quality":0,"proportionality_usability":0},
  "skill_scores": {"problem_framing":0,"evidence_discipline":0,"workflow_completeness":0,
    "requirements_quality":0,"safety_human_factors":0,"interoperability_data":0,
    "downtime_recovery":0,"validation_quality":0,"proportionality_usability":0},
  "baseline_critical_failure": false,
  "skill_critical_failure": false,
  "skill_meets_case": true,
  "evidence": ["brief concrete observation", "brief concrete observation"]
}
Use only integers 0-4. A critical failure cannot be offset by a high score."""

def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")

def load_cases() -> dict[str, Any]:
    if not CASES_PATH.is_file():
        fail(f"missing case registry: {CASES_PATH}")
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))

def all_cases(registry: dict[str, Any]) -> list[dict[str, Any]]:
    return registry["trigger_cases"] + registry["behavior_cases"] + registry["independent_cases"]

def validate_registry(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    ids: list[str] = []
    for section in ("trigger_cases", "behavior_cases", "independent_cases"):
        if section not in registry or not isinstance(registry[section], list):
            errors.append(f"missing or invalid {section}")
            continue
        for case in registry[section]:
            cid = case.get("id")
            if not cid:
                errors.append(f"{section}: case missing id")
                continue
            ids.append(cid)
            if not case.get("prompt"):
                errors.append(f"{cid}: missing prompt")
            if section == "trigger_cases":
                if case.get("expected") not in {"TRIGGER", "NO_TRIGGER", "CONTEXTUAL"}:
                    errors.append(f"{cid}: invalid expected activation")
            else:
                if not case.get("required"):
                    errors.append(f"{cid}: missing required behaviors")
                if not case.get("critical_failure"):
                    errors.append(f"{cid}: missing critical failure definition")
                for ref in case.get("refs", []):
                    if not (ROOT / ref).is_file():
                        errors.append(f"{cid}: missing reference {ref}")
    duplicates = sorted({x for x in ids if ids.count(x) > 1})
    if duplicates:
        errors.append(f"duplicate case IDs: {', '.join(duplicates)}")
    if not any(c.get("smoke") for c in all_cases(registry)):
        errors.append("no smoke cases defined")
    return errors

def weighted_total(scores: dict[str, Any]) -> float:
    total = 0.0
    for name, weight in DIMENSIONS.items():
        raw = scores.get(name, 0)
        if not isinstance(raw, int) or raw < 0 or raw > 4:
            raw = 0
        total += (raw / 4.0) * weight
    return round(total, 2)

def extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if not match:
            raise
        return json.loads(match.group(0))

def resolve_provider(requested: str) -> str:
    if requested == "deepseek":
        if not os.environ.get("DEEPSEEK_API_KEY"):
            fail("DEEPSEEK_API_KEY is required when provider=deepseek")
        return "deepseek"
    if requested == "openai":
        if not os.environ.get("OPENAI_API_KEY"):
            fail("OPENAI_API_KEY is required when provider=openai")
        return "openai"
    if os.environ.get("DEEPSEEK_API_KEY"):
        return "deepseek"
    if os.environ.get("OPENAI_API_KEY"):
        return "openai"
    fail("No live-eval API key configured. Set DEEPSEEK_API_KEY or OPENAI_API_KEY.")

def make_client(provider: str):
    try:
        from openai import OpenAI
    except ImportError:
        fail("openai package is required for live evals: pip install openai")
    if provider == "deepseek":
        return OpenAI(
            api_key=os.environ["DEEPSEEK_API_KEY"],
            base_url="https://api.deepseek.com",
        )
    return OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def default_model(provider: str) -> str:
    return "deepseek-flash" if provider == "deepseek" else "gpt-5.6-luna"

def call_text(client, model: str, instructions: str, prompt: str, max_tokens: int) -> str:
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=prompt,
        max_output_tokens=max_tokens,
    )
    return response.output_text.strip()

def skill_instructions(case: dict[str, Any]) -> str:
    parts = [
        "Follow the Healthcare Clinical Workflow Analyst skill instructions below.",
        SKILL_PATH.read_text(encoding="utf-8"),
    ]
    for ref in case.get("refs", []):
        path = ROOT / ref
        parts.append(f"\n--- REFERENCE: {ref} ---\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)

def select_cases(registry: dict[str, Any], suite: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    triggers = registry["trigger_cases"]
    behaviors = registry["behavior_cases"] + registry["independent_cases"]
    if suite == "smoke":
        return (
            [c for c in triggers if c.get("smoke")],
            [c for c in behaviors if c.get("smoke")],
        )
    if suite == "trigger":
        return triggers, []
    if suite == "behavior":
        return [], registry["behavior_cases"]
    if suite == "independent":
        return [], registry["independent_cases"]
    return triggers, behaviors

def run_trigger_case(client, model: str, case: dict[str, Any]) -> dict[str, Any]:
    skill_head = "\n".join(SKILL_PATH.read_text(encoding="utf-8").splitlines()[:20])
    prompt = f"SKILL DESCRIPTION:\n{skill_head}\n\nUSER REQUEST:\n{case['prompt']}"
    actual = call_text(client, model, TRIGGER_INSTRUCTIONS, prompt, 32).strip().upper()
    if actual not in {"TRIGGER", "NO_TRIGGER", "CONTEXTUAL"}:
        actual = "INVALID"
    return {
        "id": case["id"],
        "expected": case["expected"],
        "actual": actual,
        "pass": actual == case["expected"],
    }

def run_behavior_case(client, model: str, judge_model: str, case: dict[str, Any]) -> dict[str, Any]:
    baseline = call_text(client, model, BASELINE_INSTRUCTIONS, case["prompt"], 2200)
    skill = call_text(client, model, skill_instructions(case), case["prompt"], 2200)

    judge_prompt = f"""CASE ID: {case['id']}
PROMPT:
{case['prompt']}

REQUIRED BEHAVIORS:
{json.dumps(case['required'], ensure_ascii=False)}

CRITICAL FAILURE:
{case['critical_failure']}

BASELINE OUTPUT:
---BEGIN BASELINE---
{baseline}
---END BASELINE---

SKILL OUTPUT:
---BEGIN SKILL---
{skill}
---END SKILL---
"""
    raw_judge = call_text(client, judge_model, JUDGE_INSTRUCTIONS, judge_prompt, 1400)
    judge = extract_json(raw_judge)
    baseline_scores = judge.get("baseline_scores", {})
    skill_scores = judge.get("skill_scores", {})
    baseline_total = weighted_total(baseline_scores)
    skill_total = weighted_total(skill_scores)
    skill_cf = bool(judge.get("skill_critical_failure"))
    case_pass = bool(judge.get("skill_meets_case")) and not skill_cf and skill_total >= 75

    return {
        "id": case["id"],
        "suite": case["suite"],
        "baseline_score": baseline_total,
        "skill_score": skill_total,
        "delta": round(skill_total - baseline_total, 2),
        "baseline_critical_failure": bool(judge.get("baseline_critical_failure")),
        "skill_critical_failure": skill_cf,
        "pass": case_pass,
        "evidence": judge.get("evidence", []),
        "baseline_output": baseline,
        "skill_output": skill,
        "scores": {
            "baseline": baseline_scores,
            "skill": skill_scores,
        },
    }

def build_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# Automated Evaluation Report",
        "",
        f"- Generated: {result['generated_at']}",
        f"- Suite: {result['suite']}",
        f"- Provider: {result['provider']}",
        f"- Model: {result['model']}",
        f"- Judge model: {result['judge_model']}",
        f"- Trigger accuracy: {result['summary']['trigger_passed']}/{result['summary']['trigger_total']}",
        f"- Behavior cases passed: {result['summary']['behavior_passed']}/{result['summary']['behavior_total']}",
        f"- Skill critical failures: {result['summary']['skill_critical_failures']}",
        f"- Skill better than baseline: {result['summary']['skill_better_than_baseline']}/{result['summary']['behavior_total']}",
        "",
        "## Trigger Cases",
        "",
        "| ID | Expected | Actual | Result |",
        "|---|---|---|---|",
    ]
    for item in result["triggers"]:
        lines.append(f"| {item['id']} | {item['expected']} | {item['actual']} | {'PASS' if item['pass'] else 'FAIL'} |")

    lines += [
        "",
        "## Behavior and Independent Cases",
        "",
        "| ID | Suite | Baseline | Skill | Delta | Critical failure | Result |",
        "|---|---|---:|---:|---:|---|---|",
    ]
    for item in result["behaviors"]:
        lines.append(
            f"| {item['id']} | {item['suite']} | {item['baseline_score']:.2f} | "
            f"{item['skill_score']:.2f} | {item['delta']:+.2f} | "
            f"{'YES' if item['skill_critical_failure'] else 'No'} | {'PASS' if item['pass'] else 'FAIL'} |"
        )

    failed = [x for x in result["behaviors"] if not x["pass"]] + [x for x in result["triggers"] if not x["pass"]]
    lines += ["", "## Release Gate", ""]
    if failed:
        lines.append(f"**FAIL** — {len(failed)} case(s) failed.")
    else:
        lines.append("**PASS for the executed suite** — no executed case failed.")
    lines.append("")
    lines.append("This automated report is regression evidence, not clinical validation or organizational approval.")
    return "\n".join(lines) + "\n"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--suite", choices=["smoke", "full", "trigger", "behavior", "independent"], default="smoke")
    parser.add_argument("--provider", choices=["auto", "deepseek", "openai"], default=os.environ.get("EVAL_PROVIDER", "auto"))
    parser.add_argument("--model", default=os.environ.get("EVAL_MODEL", ""))
    parser.add_argument("--judge-model", default=os.environ.get("EVAL_JUDGE_MODEL", ""))
    parser.add_argument("--output-dir", default=str(RESULTS_DEFAULT))
    args = parser.parse_args()

    registry = load_cases()
    errors = validate_registry(registry)
    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        return 1

    total_cases = len(all_cases(registry))
    print(f"PASS: evaluation registry valid ({total_cases} cases)")
    if args.validate_only:
        return 0

    provider = resolve_provider(args.provider)
    model = args.model or default_model(provider)
    judge_model = args.judge_model or model
    client = make_client(provider)
    print(f"Live provider: {provider}; model: {model}; judge: {judge_model}")
    triggers, behaviors = select_cases(registry, args.suite)

    trigger_results = []
    for case in triggers:
        print(f"[trigger] {case['id']}")
        trigger_results.append(run_trigger_case(client, model, case))

    behavior_results = []
    for case in behaviors:
        print(f"[behavior] {case['id']}")
        behavior_results.append(run_behavior_case(client, model, judge_model, case))

    summary = {
        "trigger_total": len(trigger_results),
        "trigger_passed": sum(1 for x in trigger_results if x["pass"]),
        "behavior_total": len(behavior_results),
        "behavior_passed": sum(1 for x in behavior_results if x["pass"]),
        "skill_critical_failures": sum(1 for x in behavior_results if x["skill_critical_failure"]),
        "skill_better_than_baseline": sum(1 for x in behavior_results if x["skill_score"] > x["baseline_score"]),
    }

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "suite": args.suite,
        "provider": provider,
        "model": model,
        "judge_model": judge_model,
        "summary": summary,
        "triggers": trigger_results,
        "behaviors": behavior_results,
    }

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "report.md").write_text(build_markdown(result), encoding="utf-8")
    print(build_markdown(result))

    passed = (
        summary["trigger_passed"] == summary["trigger_total"]
        and summary["behavior_passed"] == summary["behavior_total"]
        and summary["skill_critical_failures"] == 0
        and (
            summary["behavior_total"] == 0
            or summary["skill_better_than_baseline"] > summary["behavior_total"] / 2
        )
    )
    return 0 if passed else 1

if __name__ == "__main__":
    sys.exit(main())
