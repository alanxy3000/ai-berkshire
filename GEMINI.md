# AI Berkshire Antigravity CLI Guide

This repository contains value investment research workflows, reports, and shared financial validation tools based on the four-master framework: Warren Buffett, Charlie Munger, Duan Yongping, and Li Lu.

## Project Layout

- `.agents/skills/*/SKILL.md`: Native Antigravity CLI skill packages.
- `.agents/skills.json`: Workspace-level skills configuration.
- `tools/*.py`: Shared financial validation and data tools (`financial_rigor.py`, `report_audit.py`, `twstock_data.py`, `ashare_data.py`, etc.).
- `reports/`: Research outputs organized by company directory (e.g. `reports/{公司名}/...`).
- `tests/`: Automated tests for tools and validation logic.

## Antigravity CLI Integration

- **Automatic Skill Discovery**: Antigravity CLI automatically reads `.agents/skills/` (and `.agents/skills.json`) and discovers all skills via progressive disclosure.
- **Rules & Context**: Antigravity CLI automatically loads `GEMINI.md` and `AGENTS.md` at workspace startup.
- **Subagent Parallelism**: For team workflows (`investment-team`, `earnings-team`), leverage Antigravity's `invoke_subagent` tool to spawn independent subagents for the 4 master perspectives concurrently.

## Research Quality Rules (Highest Priority)

1. **Baseline Date**:
   - Always run the `date` command to confirm today's date before starting research.
   - Treat that date as the baseline for "latest" data (prices, market cap, most recent filings), and state the data cutoff date in the report header.
   - Never assume the current date from training data.

2. **Cross-Source Verification**:
   - Financial data must come from at least two independent sources when the skill requires verification.
   - Market cap must be verified manually: `Stock Price × Total Shares` compared against reported market cap.

3. **Financial Rigor**:
   - Use exact arithmetic tools for market cap, valuation, cross-source checks, and scenario analysis:
     `python3 tools/financial_rigor.py ...`
   - Run report audit tooling before treating generated research as publishable:
     `python3 tools/report_audit.py ...`

4. **Objectivity & Tone**:
   - Strictly distinguish between **facts** and **opinions**. Facts require data citations; opinions must be clearly labeled.
   - No preconceived stance (neither perma-bull nor perma-bear). Conclusions must be derived directly from data and facts.
   - Present both pros and cons: every major thesis must include counterarguments.
   - Clearly state "uncertain" or "insufficient data" when facts cannot be confirmed.
   - Language: Chinese, direct and incisive. Rating scale: ★1-5 (no half stars).

## Report Directory & Naming Conventions

All company-specific reports must be placed under `reports/{公司名}/`:

```
reports/
├── 腾讯/
│   ├── 腾讯-research-20260408.md
│   ├── 腾讯-earnings-2025Q4.md
│   ├── 腾讯-management-20260409.md
│   └── 腾讯-thesis.md
├── 拼多多/
│   ├── README.md
│   ├── 01-商业模式分析-段永平视角.md
│   ├── 02-财务估值分析-巴菲特视角.md
│   ├── 03-行业竞争分析-芒格视角.md
│   ├── 04-风险管理层评估-李录视角.md
│   └── 最终报告.md
├── 核电-industry-20260409.md        # Industry reports in reports/ root
├── AI算力-funnel-20260509.md        # Screening funnel in reports/ root
└── portfolio-latest.md              # Portfolio status in reports/ root (local only)
```

## /investment-team Report Structure

```
reports/{公司名}/
├── README.md                         # 研究框架概览+核心结论
├── 01-商业模式分析-段永平视角.md
├── 02-财务估值分析-巴菲特视角.md
├── 03-行业竞争分析-芒格视角.md
├── 04-风险管理层评估-李录视角.md
└── 最终报告.md                       # Team Lead 综合报告
```

