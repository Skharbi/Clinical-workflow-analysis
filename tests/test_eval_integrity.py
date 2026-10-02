"""Offline regression tests; these do not execute a model or clinical workflow."""
import importlib.util
from pathlib import Path
import unittest
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("runner", ROOT / "evals/run_evals.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

def judgment():
    return {"baseline_scores": {k: 3 for k in runner.DIMENSIONS},
            "skill_scores": {k: 4 for k in runner.DIMENSIONS},
            "baseline_critical_failure": False, "skill_critical_failure": False,
            "skill_meets_case": True, "evidence": ["Concrete observed behavior"]}

def result(improved=True):
    return {"triggers": [], "behaviors": [{"pass": True, "skill_critical_failure": False,
        "skill_score": 100, "baseline_score": 75 if improved else 100,
        "scores": {"skill": {k: 4 for k in runner.DIMENSIONS}}}]}

class IntegrityTests(unittest.TestCase):
    def test_valid_judge(self):
        runner.validate_judgment(judgment())

    def test_boolean_score_rejected(self):
        value = judgment(); value["skill_scores"]["evidence_discipline"] = True
        with self.assertRaises(ValueError): runner.validate_judgment(value)

    def test_string_boolean_rejected(self):
        value = judgment(); value["skill_meets_case"] = "false"
        with self.assertRaises(ValueError): runner.validate_judgment(value)

    def test_missing_dimension_rejected(self):
        value = judgment(); del value["skill_scores"]["validation_quality"]
        with self.assertRaises(ValueError): runner.validate_judgment(value)

    def test_empty_evidence_rejected(self):
        value = judgment(); value["evidence"] = []
        with self.assertRaises(ValueError): runner.validate_judgment(value)

    def test_empty_run_fails(self):
        self.assertFalse(runner.run_gate({"triggers": [], "behaviors": []})[0])

    def test_comparison_tie_fails(self):
        self.assertFalse(runner.run_gate(result(False))[0])

    def test_valid_run_passes(self):
        self.assertTrue(runner.run_gate(result())[0])

    def test_critical_failure_blocks_high_score(self):
        value = result(); value["behaviors"][0]["skill_critical_failure"] = True
        self.assertFalse(runner.run_gate(value)[0])

    def test_low_safety_blocks_high_total(self):
        value = result(); value["behaviors"][0]["scores"]["skill"]["safety_human_factors"] = 2
        self.assertFalse(runner.run_gate(value)[0])

    def test_infra_failure_blocks(self):
        value = result(); value["behaviors"][0]["infra_error"] = "provider error"
        self.assertFalse(runner.run_gate(value)[0])

    def test_report_does_not_hide_comparison_failure(self):
        value = result(False)
        value.update(generated_at="test", suite="smoke", provider="mock", model="mock", judge_model="mock",
                     summary={"trigger_passed": 0, "trigger_total": 0, "behavior_passed": 1,
                              "behavior_total": 1, "skill_critical_failures": 0, "infra_errors": 0,
                              "skill_better_than_baseline": 0})
        value["behaviors"][0].update(id="mock", suite="test", delta=0)
        self.assertIn("**FAIL**", runner.build_markdown(value))

    def test_incomplete_generation_rejected(self):
        client = SimpleNamespace(responses=SimpleNamespace(create=lambda **kw:
            SimpleNamespace(output_text="partial", status="incomplete")))
        with self.assertRaises(ValueError): runner.call_text(client, "mock", "test", "test", 20)

    def test_empty_generation_rejected(self):
        client = SimpleNamespace(responses=SimpleNamespace(create=lambda **kw:
            SimpleNamespace(output_text="", status="completed")))
        with self.assertRaises(ValueError): runner.call_text(client, "mock", "test", "test", 20)

if __name__ == "__main__": unittest.main()
