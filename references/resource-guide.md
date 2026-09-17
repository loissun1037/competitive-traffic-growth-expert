# Resource guide

This skill package is designed for reusable competitor traffic and growth reports. Treat bundled files as examples and scaffolding, not as live data.

## Files

| File | Role |
|---|---|
| `assets/竞品分析_批量输入模板.xlsx` | Blank input workbook for one or many sector-analysis tasks. Use row 5 machine headers as the stable schema. |
| `references/AI 视频赛道竞品分析_样例输出.xlsx` | Example final report. Use it to understand report pacing, section hierarchy, chart density, and executive wording. Do not reuse its sector conclusions. |
| `scripts/validate_input_template.py` | Lightweight schema checker for the input workbook. It checks required sheets and row-5 machine headers. |
| `evals/evals.json` | Suggested smoke-test prompts for future skill evaluation. |

## Updating the input template

Keep the template aligned with the `SKILL.md` “输入数据规范” section.

- Preserve the 15-sheet structure unless the skill instructions are updated at the same time.
- Preserve row 5 English machine headers for all input tables.
- Add optional guidance to `填写说明` rather than changing data headers when the new requirement is about report style or final output.
- Do not put example data into formal input rows. Examples belong in `填写说明` or `字段字典`.
- Run `python scripts/validate_input_template.py assets/竞品分析_批量输入模板.xlsx` after any template edit.

## Using the sample output

The sample report is included only as a visual and structural reference. It can help the agent match:

- a concise executive summary,
- conclusion-first section titles,
- table-plus-chart section rhythm,
- source-aware wording,
- action-oriented growth recommendations.

It must not be treated as evidence for a new sector. Competitors, rankings, channels, countries, and strategic recommendations must be regenerated from the current task’s data.

## Publishing notes

This package contains no credentials, API keys, paid-data exports, or crawler code. It assumes the user supplies authorized exports, public sources, or authorized API access at runtime.

Before publishing publicly, confirm that the sample report can be shared. If the sample includes confidential or licensed data, replace it with a sanitized sample or remove it and keep only the input template plus instructions.

