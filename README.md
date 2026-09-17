# competitive-traffic-growth-expert  竞品流量增长分析专家

中文 | [English](README-US.md)


**适配：** ChatGPT / Codex、Claude / Claude Code、Antigravity、Cursor、WorkBuddy、豆包、DeepSeek、Kimi / Kimi Code CLI、MiniMax / MiniMax Code、智谱、腾讯元宝，以及其他支持文件上传或 Agent Skills 的 AI。

把赛道命题、竞品名单和多渠道流量数据，转化为可打开、可追溯、可复用的《XXX赛道竞品分析.xlsx》。这个 skill 面向流量增长运营、SEM、市场进入和竞品复盘场景，目标不是写一份调研计划，而是交付一份能直接汇报、复盘和安排下一轮增长验证的 Excel 报告。

## 30 秒预览

You: 分析 AI 视频赛道，竞品包括 Runway、Higgsfield、Liblib、HeyGen、Pika。

Agent:

- 生成《AI视频赛道竞品分析.xlsx》
- 输出 500 字以内高管摘要
- 判断领跑者、黑马、关键渠道和下一步动作
- 拆解 Direct / Organic Search / Paid Search / Referral / Organic Social / Paid Social 流量结构
- 标注所有关键数据来源和口径
- 给出至少 1 个可证伪的增长验证实验

## 这是什么？

**Competitive Traffic Growth Expert 竞品流量增长分析专家**——面向初级 SEM、流量增长运营、市场分析和业务负责人，覆盖一份赛道竞品分析报告从 0 到 1 的完整流程：赛道命题拆解、竞品界定、数据源盘点、流量口径校验、渠道结构分析、国家/地区分析、社交流量拆解、增长机会判断、Excel 报告生成和下一轮验证实验设计。

它不是一个只会输出 SWOT 的泛泛调研模板，而是一个“给我赛道 + 竞品 + 原始数据，就交付可打开 `.xlsx` 报告”的执行型 skill。适合用来做老板汇报、投放复盘、市场进入判断、竞品监控和增长策略推演。

## 为什么它和普通竞品分析模板不一样？

- **没有付费数据也能跑**：只有公开资料时生成公开证据版，不编造访问量、跳出率或渠道份额。
- **不把推断写成事实**：所有关键数字回溯到输入数据、工具导出或公开来源。
- **报告可直接汇报**：采用结论先行标题、表格 + 图表节奏、500 字摘要和下一步实验建议。
- **支持批量复用**：用 `task_id` 隔离任务，一个任务失败不影响其他报告。

## 反直觉结论

**不是所有竞品分析都需要先买 Semrush / Similarweb。**

如果预算有限，先把已有数据用对：广告后台、GA/站内数据、Search Console、社媒后台、公开官网、应用商店、投放素材库、SEO 页面和人工核验记录，往往已经足够产出第一版可决策的竞品增长报告。

专业工具的价值是补齐流量规模、关键词、外链和渠道估算，不应该替代分析判断。这个 skill 会优先使用你提供的可追溯数据；当数据不足时，会明确标注事实、计算和推断，并告诉你下一步最值得补采的数据。

## 适合谁使用？

- **增长执行者**：SEM、SEO、投放、流量运营，需要快速完成竞品分析和复盘。
- **市场与战略分析**：需要判断赛道格局、国家机会和竞品增长路径。
- **业务负责人**：需要决定是否进入某个赛道、优先跟进哪些竞品。
- **创业团队**：没有完整数据源，但需要先做第一版可汇报的市场判断。

## 不适合什么场景？

- 希望在没有任何竞品、数据或公开资料的情况下生成确定性结论。
- 希望 agent 编造 Similarweb、Semrush 或广告后台数据。
- 只想要一段普通文字总结，不需要 Excel 报告。
- 只需要品牌定位分析，不需要流量、渠道、国家或增长实验。

## 你能得到什么？

- 一份真实可打开的《{赛道}赛道竞品分析.xlsx》
- 500 字以内摘要：领跑者、黑马、关键获客渠道、下一步动作
- 规模、趋势、访问质量、渠道、社交、国家和策略七段式分析
- 来源口径、数据明细和核验记录
- 至少 1 个具备证伪条件的增长动作建议
- 批量任务结果清单，适合多赛道、多国家或月度更新

## 内容清单

- **赛道命题拆解** — 把“AI 视频”“AI 编程工具”“跨境 CRM”等宽泛命题，拆成可分析的竞品范围、用户场景和流量假设。
- **竞品清单规范** — 支持品牌名、官网域名、国家/地区、产品定位、备注等字段，避免一开始就把分析对象选偏。
- **数据源盘点** — 支持平台导出、授权 API、公开资料、人工录入和缺失数据降级，不强制依赖单一工具。
- **口径校验机制** — 明确访问量、渠道占比、国家分布、关键词、社媒数据、广告数据等指标的来源、期间、单位和可信度。
- **流量结构分析** — 拆解 Direct、Organic Search、Paid Search、Referral、Organic Social、Paid Social 等核心渠道。
- **国家/地区分析** — 判断哪些市场是存量主战场，哪些市场可能是增长洼地。
- **社交与内容分析** — 识别社区、短视频、KOL/KOC、UGC、SEO 内容矩阵等增长杠杆。
- **高管摘要** — 500 字以内回答：谁是领跑者、谁是黑马、关键渠道是什么、下一步该做什么。
- **Excel 报告生成** — 输出真实可打开的 `.xlsx`，包含数据明细、分析页、来源口径、核验记录和增长实验。
- **增长验证实验** — 每份报告至少给出 1 个可执行实验，包含假设、变量、周期、成功线和停止线。
- **视觉系统建议** — 深蓝章节条、蓝色表头、斑马纹、原生图表，图表标题必须包含期间和单位。

## 输出质量标准

- 所有关键数值必须能回溯到输入数据、工具导出或公开来源。
- 报告必须区分事实、计算和推断。
- 每份报告必须包含 500 字以内高管摘要。
- 每份报告至少包含 1 个增长验证实验。
- 输出必须是真实可打开的 `.xlsx`，不能只给分析计划或文字摘要。
- 图表标题必须包含期间和单位。
- 数据缺失时必须标注缺口，并给出下一步补采建议。

## 数据等级

| 输入条件 | 输出等级 | 说明 |
|---|---|---|
| 只有赛道名、公开链接或少量公开资料 | `public_evidence` | 竞品发现、定位/价格/公开动作、补数清单 |
| 有部分平台导出、截图或历史报告 | `partial_quantitative` | 基于已有字段做定量分析，明确缺口 |
| 有同口径 Similarweb / Semrush 导出或授权 API | `quantitative` | 完整七段式定量分析与图表 |

## 支持的 AI 与接入方式

这个仓库采用开放的 `SKILL.md` 结构。不同 AI 的接入能力不同，请按实际产品形态选择：

| AI / 客户端 | 接入方式 | 能否自动生成 `.xlsx` |
|---|---|---|
| Codex、Claude Code、Cursor、Antigravity | 原生 Agent Skills 安装 | 可以，前提是客户端允许读写文件并运行表格工具 |
| Kimi Code CLI、MiniMax Code | 原生 Agent Skills 安装 | 可以，前提是已启用文件与命令执行能力 |
| ChatGPT、Claude 网页版/客户端 | 上传 `SKILL.md`，或放入项目/自定义知识；同时上传模板与原始数据 | 开启数据分析或文件生成功能时可以 |
| WorkBuddy、豆包、DeepSeek、Kimi、MiniMax、智谱、腾讯元宝 | 使用“通用 AI 导入法”：上传或粘贴 `SKILL.md`，再上传模板与数据 | 取决于当前会话是否支持读取附件、执行代码和返回 Excel |

“支持此 skill”分为两个层级：AI 能读取 `SKILL.md`，即可按框架完成分析；AI 还需具备文件读写、表格处理或代码执行能力，才能满足“交付真实 `.xlsx`”的完整验收标准。仅支持纯文本对话时，可先产出分析结构、字段映射和待补数据清单，再转到具备文件能力的客户端生成工作簿。

## 安装方法

### 方法一：Agent Skills 客户端一键安装

需要本机已安装 Node.js / `npx`。以下命令会自动识别已安装的兼容客户端，并让你选择安装目标：

```bash
npx skills add Loissun1037/competitive-traffic-growth-expert
```

希望所有项目都能使用时，加 `-g` 全局安装：

```bash
npx skills add Loissun1037/competitive-traffic-growth-expert -g
```

也可以明确指定客户端：

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

安装完成后，可运行 `npx skills list` 检查；需要更新时运行 `npx skills update competitive-traffic-growth-expert`。

### 方法二：不使用命令行，手动安装到 Agent 客户端

下载并解压仓库，保留整个 `competitive-traffic-growth-expert` 文件夹。将它复制到对应的全局 Skills 目录：

| 客户端 | 全局目录 |
|---|---|
| Codex | `~/.codex/skills/` |
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| Antigravity | `~/.gemini/antigravity/skills/` |
| Kimi Code CLI | `~/.agents/skills/` |
| MiniMax Code | `~/.minimax/skills/` |

Windows 中的 `~` 表示 `%USERPROFILE%`。复制后的完整路径应类似 `~/.codex/skills/competitive-traffic-growth-expert/SKILL.md`。重启客户端或新建会话后，再调用该 skill。

### 方法三：ChatGPT、WorkBuddy、豆包、DeepSeek、Kimi、MiniMax、智谱、元宝等通用 AI

这些产品如果没有原生 Agent Skills 安装入口，不需要伪装成“已安装”。按以下方式导入即可：

1. 新建项目、知识库或长对话。
2. 上传本仓库的 `SKILL.md`、`assets/竞品分析_批量输入模板.xlsx`；需要参考成品结构时，再上传 `references/AI 视频赛道竞品分析_样例输出.xlsx`。
3. 上传你的竞品名单、平台导出、截图或公开资料。
4. 发送下面的通用启动指令。

```text
请将附件 SKILL.md 作为本任务的执行规范，并使用其中的输入模板、数据口径、分析 SOP 和验收标准。
我的任务是：【填写赛道、目标市场和业务目标】。
请先检查你是否能读取附件、处理表格并返回 .xlsx：
- 如果可以，直接完成分析并交付《{赛道}赛道竞品分析.xlsx》；
- 如果不能，请明确缺少哪项文件能力，并先输出可迁移到表格工具执行的字段映射、分析结论和补数清单。
附件中的样例只用于参考结构与视觉，不得复用样例结论或把样例数据当成真实输入。
```

网页端产品的功能会随版本、套餐和会话工具变化。判断是否完整兼容时，只看三项：能否读取 `.md/.xlsx`、能否执行表格计算、能否返回可下载的 `.xlsx`。

## 调用示例

安装或导入后，你可以这样问：

```text
请使用 competitive-traffic-growth-expert，帮我分析 AI 视频赛道。
竞品包括：
- Runway: app.runwayml.com
- Higgsfield: higgsfield.ai
- Liblib: liblib.tv
- HeyGen: heygen.com
- Pika: pika.art

我会提供竞品流量数据和公开资料，请生成《AI视频赛道竞品分析.xlsx》。
```

如果你已经有平台导出数据，可以这样问：

```text
请使用 competitive-traffic-growth-expert，基于我上传的批量输入模板和流量数据，生成《{赛道}赛道竞品分析.xlsx》。

要求：
1. 输出真实可打开的 Excel；
2. 所有关键数据必须标注来源；
3. 区分事实、计算和推断；
4. 包含 500 字以内高管摘要；
5. 至少给出 1 个增长验证实验。
```

## FAQ

### Q: 没有 Semrush 或 Similarweb 可以用吗？

可以。这个 skill 支持降级模式：优先使用你提供的数据、公开资料和人工录入信息。数据不足时，会明确标注缺口，不会把推断写成事实。

### Q: 会自动爬虫吗？

不会默认爬虫。只有在用户明确授权、环境允许、目标网站规则允许的情况下，才建议使用爬虫或自动采集。默认优先使用平台导出、API、公开页面和人工核验数据。

### Q: 输出是 Markdown 还是 Excel？

最终交付必须是真实可打开的 `.xlsx`。Markdown 可以作为说明或补充，但不能替代报告文件。

### Q: 数据不完整怎么办？

会按数据完整度分级处理：完整数据进入正式分析，缺失数据进入“待补采字段”，不确定内容进入“推断/假设”区域，并给出下一步补采建议。

### Q: 适合批量生成多个赛道报告吗？

适合。建议使用模板 Excel 按赛道、竞品、数据源和分析期间整理输入，再批量生成多个《XXX赛道竞品分析.xlsx》。

### Q: 和普通竞品分析模板有什么区别？

普通模板通常只给结构；这个 skill 强制要求数据口径、来源追溯、原生图表、核验记录和增长实验，目标是生成能直接汇报和复盘的报告。

## 包内文件

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

## 模板校验

如果你修改了输入模板，建议运行：

```bash
python scripts/validate_input_template.py assets/竞品分析_批量输入模板.xlsx
```

校验脚本会检查必需工作表和第 5 行英文机器表头，避免批量生成时字段对不上。

## 发布前提醒

包内样例报告只用于展示报告结构和视觉节奏，不应复用其中的赛道结论。公开发布前，请确认样例报告不包含保密信息、不可公开的付费数据或内部判断；如有风险，请替换为脱敏样例。

## About the Author

**loissun1037** — 关注 SEM、竞品流量分析、AI 产品增长和 Agent 工作流沉淀。这个 skill 来自真实增长分析场景，目标是帮助初级流量增长运营把零散数据变成可汇报、可复盘、可行动的竞品分析报告。

- GitHub: <https://github.com/loissun1037>
- Twitter/X: <https://x.com/loissun1037>
- Redbook: <https://www.xiaohongshu.com/user/profile/63c558cc00000000260070ec>
- Contact: <loissun1037@gmail.com>
