# competitive-traffic-growth-expert


**Works with:** ChatGPT / Codex, Claude / Claude Code, Antigravity, Cursor, WorkBuddy, Doubao, DeepSeek, Kimi / Kimi Code CLI, MiniMax / MiniMax Code, Zhipu, Tencent Yuanbao, and other AI products that support file uploads or Agent Skills.

Turn a sector topic, competitor list, and multi-channel traffic data into an openable, traceable, and reusable `XXX Sector Competitor Analysis.xlsx` workbook. This skill is built for traffic growth operators, SEM teams, market-entry research, and competitor review workflows. It does not stop at a research plan; it delivers an Excel report that can be used for stakeholder reporting, retrospectives, and the next round of growth experiments.

## 30-Second Preview

You: Analyze the AI video sector. Competitors include Runway, Higgsfield, Liblib, HeyGen, and Pika.

Agent:

- Generates `AI Video Sector Competitor Analysis.xlsx`
- Writes an executive summary under 500 Chinese characters
- Identifies the leader, dark horse, key channels, and next actions
- Breaks down Direct / Organic Search / Paid Search / Referral / Organic Social / Paid Social traffic
- Marks every key metric with its source and definition
- Provides at least one falsifiable growth experiment

## What Is This?

**Competitive Traffic Growth Expert** is a practical guide and execution skill for creating sector competitor analysis reports from scratch. It is designed for junior SEM operators, traffic growth teams, market analysts, and business owners. It covers sector framing, competitor definition, data-source inventory, metric validation, channel analysis, country/region analysis, social traffic breakdown, growth opportunity diagnosis, Excel report generation, and next-step experiment design.

It is not a generic SWOT template. It is an execution-oriented skill for the workflow: “give me a sector + competitors + raw data, and produce an openable `.xlsx` report.” Use it for stakeholder reporting, campaign retrospectives, market-entry decisions, competitor monitoring, and growth strategy planning.

## Why Is It Different from a Generic Competitor Analysis Template?

- **Works without paid data:** When only public sources are available, it creates a public-evidence report instead of inventing traffic, bounce rate, or channel-share numbers.
- **Keeps inference separate from facts:** Every key number must trace back to input data, tool exports, or public sources.
- **Ready for reporting:** Uses conclusion-first section titles, a table-plus-chart rhythm, a concise executive summary, and next-step experiment recommendations.
- **Built for batch reuse:** `task_id` isolates each task, so one failed task does not block other reports.

## Counterintuitive Takeaway

**Not every competitor analysis should start by buying Semrush or Similarweb.**

If budget is limited, use the data you already have first: ad-platform exports, GA or first-party analytics, Search Console, social dashboards, public websites, app stores, ad libraries, SEO pages, and manual validation records. These sources are often enough to produce a first version of a decision-ready competitor growth report.

Professional tools are useful for filling gaps in traffic scale, keyword data, backlinks, and channel estimates. They should not replace analytical judgment. This skill prioritizes traceable data you provide; when data is incomplete, it labels facts, calculations, and inferences separately and tells you which data to collect next.

## Who It Is For

- **Growth executors:** SEM, SEO, paid acquisition, and traffic operators who need fast competitor analysis and campaign retrospectives.
- **Market and strategy analysts:** Teams that need to understand sector structure, country opportunities, and competitor growth paths.
- **Business owners:** Decision makers who need to decide whether to enter a sector and which competitors to track first.
- **Startup teams:** Teams without complete data sources that still need a first report they can present.

## When Not to Use It

- You want deterministic conclusions without any competitors, data, or public evidence.
- You want the agent to fabricate Similarweb, Semrush, or ad-platform data.
- You only need a short text summary instead of an Excel workbook.
- You only need brand-positioning analysis, without traffic, channels, countries, or growth experiments.

## What You Get

- A real, openable `{Sector} Sector Competitor Analysis.xlsx` workbook
- An executive summary under 500 Chinese characters covering leaders, dark horses, key acquisition channels, and next actions
- Seven-part analysis covering scale, trends, engagement quality, channels, social, countries, and strategy
- Source definitions, raw data details, and validation records
- At least one falsifiable growth action recommendation
- A batch result manifest for multi-sector, multi-country, or monthly updates

## Content Checklist

- **Sector framing** — Turns broad topics such as “AI video,” “AI coding tools,” and “cross-border CRM” into analyzable competitor scope, user scenarios, and traffic hypotheses.
- **Competitor-list standardization** — Supports brand name, official domain, country/region, product positioning, and notes, so the analysis target is clear from the start.
- **Data-source inventory** — Supports platform exports, authorized APIs, public sources, manual entry, and fallback modes for missing data without forcing one paid tool.
- **Metric validation** — Defines sources, periods, units, and confidence levels for visits, channel share, country split, keywords, social metrics, and ad metrics.
- **Traffic-channel analysis** — Breaks down Direct, Organic Search, Paid Search, Referral, Organic Social, and Paid Social.
- **Country/region analysis** — Identifies mature markets, growth gaps, and countries worth follow-up.
- **Social and content analysis** — Identifies communities, short-video channels, KOL/KOC signals, UGC loops, and SEO content matrices.
- **Executive summary** — Answers within 500 Chinese characters: who leads, who is rising, which channels matter, and what to do next.
- **Excel report generation** — Produces an openable `.xlsx` with data details, analysis pages, source definitions, validation records, and growth experiments.
- **Growth experiment** — Includes at least one executable experiment with hypothesis, variable, period, success threshold, and stop-loss threshold.
- **Visual system guidance** — Uses dark-blue section bars, blue table headers, zebra striping, native charts, and chart titles that include period and unit.

## Output Quality Standards

- Every key number must trace back to input data, tool exports, or public sources.
- The report must distinguish facts, calculations, and inferences.
- Every report must include an executive summary under 500 Chinese characters.
- Every report must include at least one growth experiment.
- The output must be a real, openable `.xlsx`, not just a plan or text summary.
- Chart titles must include period and unit.
- Missing data must be labeled clearly, with recommendations for what to collect next.

## Data Levels

| Available inputs | Output level | What it means |
|---|---|---|
| Only a sector name, public links, or sparse public sources | `public_evidence` | Competitor discovery, positioning, pricing, public actions, and data gap list |
| Partial platform exports, screenshots, or prior reports | `partial_quantitative` | Quantitative analysis for available fields, with explicit gaps |
| Aligned Similarweb / Semrush exports or authorized API access | `quantitative` | Complete seven-part quantitative report and charts |

## Supported AI Products and Access Modes

This repository uses the open `SKILL.md` structure. Choose the access mode that matches your AI product:

| AI / client | Access mode | Can it generate `.xlsx` automatically? |
|---|---|---|
| Codex, Claude Code, Cursor, Antigravity | Native Agent Skills installation | Yes, when the client can read/write files and run spreadsheet tools |
| Kimi Code CLI, MiniMax Code | Native Agent Skills installation | Yes, when file and command execution are enabled |
| ChatGPT, Claude web/desktop | Upload `SKILL.md`, or add it to project/custom knowledge; upload the template and raw data as well | Yes, when data analysis or file generation is enabled |
| WorkBuddy, Doubao, DeepSeek, Kimi, MiniMax, Zhipu, Tencent Yuanbao | Use the universal AI import method: upload or paste `SKILL.md`, then upload the template and data | Depends on whether the current session can read attachments, execute code, and return Excel files |

Compatibility has two levels. Any AI that can read `SKILL.md` can follow the analysis framework. To satisfy the complete acceptance standard of delivering a real `.xlsx`, the AI must also support file I/O, spreadsheet processing, or code execution. A text-only chat can still produce the analysis structure, field mapping, and missing-data checklist for transfer to a file-capable client.

## Installation

### Option 1: One-command installation for Agent Skills clients

Node.js / `npx` must be available locally. The following command detects compatible installed clients and lets you select a target:

```bash
npx skills add Loissun1037/competitive-traffic-growth-expert
```

Add `-g` to make the skill available across projects:

```bash
npx skills add Loissun1037/competitive-traffic-growth-expert -g
```

You can also target a client explicitly:

```bash
# ChatGPT Codex / Codex CLI / Codex App
npx skills add Loissun1037/competitive-traffic-growth-expert -g -a codex

# Claude Code
npx skills add Loissun1037/competitive-traffic-growth-expert -g -a claude-code

# Cursor
npx skills add Loissun1037/competitive-traffic-growth-expert -g -a cursor

# Google Antigravity
npx skills add Loissun1037/competitive-traffic-growth-expert -g -a antigravity

# Kimi Code CLI
npx skills add Loissun1037/competitive-traffic-growth-expert -g -a kimi-code-cli

# MiniMax Code
npx skills add Loissun1037/competitive-traffic-growth-expert -g -a minimax-code
```

Run `npx skills list` to verify installation. Run `npx skills update competitive-traffic-growth-expert` to update it later.

### Option 2: Manual installation for Agent clients

Download and extract the repository, keeping the complete `competitive-traffic-growth-expert` folder. Copy it to the matching global Skills directory:

| Client | Global directory |
|---|---|
| Codex | `~/.codex/skills/` |
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| Antigravity | `~/.gemini/antigravity/skills/` |
| Kimi Code CLI | `~/.agents/skills/` |
| MiniMax Code | `~/.minimax/skills/` |

On Windows, `~` means `%USERPROFILE%`. The resulting path should look like `~/.codex/skills/competitive-traffic-growth-expert/SKILL.md`. Restart the client or open a new session before invoking the skill.

### Option 3: ChatGPT, WorkBuddy, Doubao, DeepSeek, Kimi, MiniMax, Zhipu, Yuanbao, and other general AI products

If a product has no native Agent Skills installer, use it as an imported instruction package instead of claiming a native installation:

1. Create a project, knowledge base, or long-running conversation.
2. Upload `SKILL.md` and `assets/竞品分析_批量输入模板.xlsx`. Upload `references/AI 视频赛道竞品分析_样例输出.xlsx` as well when you need an output-layout reference.
3. Upload your competitor list, platform exports, screenshots, or public sources.
4. Send the universal startup prompt below.

```text
Treat the attached SKILL.md as the execution specification for this task. Follow its input template, metric definitions, analysis SOP, and acceptance criteria.
My task is: [sector, target market, and business goal].
First check whether you can read attachments, process spreadsheets, and return an .xlsx file:
- If yes, complete the analysis and deliver `{Sector} Sector Competitor Analysis.xlsx`.
- If no, state which file capability is missing, then produce a field mapping, analysis conclusions, and data-gap checklist that can be transferred to a spreadsheet-capable tool.
The attached sample is only a structural and visual reference. Do not reuse its conclusions or treat sample data as real input.
```

Web-product capabilities vary by version, plan, and enabled session tools. Judge complete compatibility by three checks: can it read `.md/.xlsx`, can it perform spreadsheet calculations, and can it return a downloadable `.xlsx`?

## Invocation Examples

After installation or import, you can ask:

```text
Please use competitive-traffic-growth-expert to analyze the AI video sector.
Competitors include:
- Runway: app.runwayml.com
- Higgsfield: higgsfield.ai
- Liblib: liblib.tv
- HeyGen: heygen.com
- Pika: pika.art

I will provide competitor traffic data and public sources. Please generate `AI Video Sector Competitor Analysis.xlsx`.
```

If you already have platform exports, you can ask:

```text
Please use competitive-traffic-growth-expert. Based on my uploaded batch input template and traffic data, generate `{Sector} Sector Competitor Analysis.xlsx`.

Requirements:
1. Output a real, openable Excel workbook.
2. Mark the source of every key metric.
3. Separate facts, calculations, and inferences.
4. Include an executive summary under 500 Chinese characters.
5. Include at least one growth experiment.
```

## FAQ

### Q: Can I use it without Semrush or Similarweb?

Yes. The skill supports fallback modes: it prioritizes your own data, public sources, and manual entries. If data is missing, it labels the gaps clearly instead of presenting assumptions as facts.

### Q: Does it automatically scrape websites?

No. It does not scrape by default. Crawling or automated collection should be considered only when the user authorizes it, the environment allows it, and the target website rules allow it. By default, the skill prioritizes platform exports, APIs, public pages, and manual validation.

### Q: Is the output Markdown or Excel?

The final deliverable must be a real, openable `.xlsx`. Markdown can be used for notes or explanations, but it does not replace the report workbook.

### Q: What if the data is incomplete?

The skill handles different completeness levels. Complete data goes into formal analysis, missing fields go into the data-gap list, and uncertain content is labeled as inference or hypothesis with next-step collection suggestions.

### Q: Can it generate multiple sector reports in batch?

Yes. Use the template workbook to organize sector, competitor, data-source, and analysis-period fields, then generate multiple `XXX Sector Competitor Analysis.xlsx` reports in batch.

### Q: How is this different from a normal competitor analysis template?

Most templates only provide structure. This skill requires source definitions, traceable metrics, native charts, validation records, and growth experiments, so the output can be used for reporting and retrospectives.

## Package Contents

```text
competitive-traffic-growth-expert/
├── SKILL.md
├── README.md
├── README.en.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── 竞品分析_批量输入模板.xlsx
├── references/
│   ├── AI 视频赛道竞品分析_样例输出.xlsx
│   └── resource-guide.md
├── scripts/
│   └── validate_input_template.py
└── evals/
    └── evals.json
```

## Template Check

If you edit the input workbook, run:

```bash
python scripts/validate_input_template.py assets/竞品分析_批量输入模板.xlsx
```

The script checks required worksheets and row-5 English machine headers, so batch generation does not break because of schema drift.

## Publishing Note

The bundled sample report is a structural and visual reference only. Do not reuse its sector conclusions. Before publishing publicly, confirm that the sample report contains no confidential information, restricted paid-data exports, or internal judgments. Replace it with a sanitized sample if needed.

## About the Author

**loissun1037** — Focuses on SEM, competitor traffic analysis, AI product growth, and Agent workflow packaging. This skill comes from real growth-analysis workflows. Its goal is to help junior traffic growth operators turn scattered data into competitor analysis reports that can be presented, reviewed, and turned into follow-up growth experiments.

- GitHub: <https://github.com/loissun1037>
- Twitter/X: <https://x.com/loissun1037>
- Redbook: <https://www.xiaohongshu.com/user/profile/63c558cc00000000260070ec>
- Contact: <loissun1037@gmail.com>
