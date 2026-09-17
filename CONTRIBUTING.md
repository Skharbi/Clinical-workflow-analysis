# Contributing

Contributions should improve decision quality without turning the skill into a universal healthcare manual.

## Principles

- Preserve the boundaries in `PROJECT_SCOPE.md`.
- Keep `SKILL.md` concise and route detailed guidance to focused references.
- Distinguish external guidance from local policy and configuration.
- Do not add unsupported clinical thresholds, vendor behavior, interface details, or compliance claims.
- Prefer de-identified or synthetic examples.
- Add or update evaluations whenever behavior changes materially.

## Change process

1. State the workflow-analysis problem the change solves.
2. Modify the narrowest appropriate file.
3. Add a trigger, non-trigger, or behavior case when applicable.
4. Run `python tests/validate_package.py` and the platform skill validator.
5. Review the change against `evals/scoring-rubric.md`.

Safety-boundary failures block release even when aggregate evaluation results improve.
