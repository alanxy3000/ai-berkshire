# AI Berkshire Antigravity CLI Guide

See [GEMINI.md](GEMINI.md) for the complete workspace rules, financial validation standards, and research quality rules.

## Key Antigravity CLI Rules

- **Workspace Skills**: Located in `.agents/skills/<skill_name>/SKILL.md`, automatically discovered by Antigravity CLI.
- **Date Check**: Run `date` before research; state data cutoff in the header.
- **Financial Validation**: Always use `python3 tools/financial_rigor.py` and `python3 tools/report_audit.py`.
- **Multi-Agent Execution**: Use `invoke_subagent` to parallelize multi-master research teams.
- **Reports**: Always organize company reports into `reports/{公司名}/`.

