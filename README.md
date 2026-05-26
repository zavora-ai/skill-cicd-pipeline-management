# CI/CD Pipeline Management Skill

> Pipeline operations for AI agents — monitor builds, debug failures from logs, trigger safe deployments, and manage release gates via mcp-cicd.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--cicd-green)](https://github.com/zavora-ai/mcp-cicd)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 8 CI/CD tools into **safe deployment workflows** — ensuring builds are green before deploying, failures are diagnosed efficiently, and reruns only happen when appropriate.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Debug Failure | 2-3 | Root cause from logs in seconds |
| Safe Deployment | 3 | CI verified → staging healthy → deploy |
| Smart Rerun | 2 | Only reruns if flaky, not genuine failures |
| Cancel | 1 | Abort stuck/wrong pipelines |

### Without this skill:
- Deploys happen with failing CI
- Failures rerun blindly without investigation
- No staging verification before production
- Log analysis requires manual digging

### With this skill:
- CI must pass before any deployment
- Failures diagnosed from logs (test? build? infra? flaky?)
- Staging health verified before production promotion
- Log patterns auto-classified (parse_logs.py)

## Installation

```bash
git clone https://github.com/zavora-ai/skill-cicd-pipeline-management.git \
  ~/.skills/skills/cicd-pipeline-management
```

## Requirements

**Required:** `mcp-cicd` (8 tools)

**Cross-MCP:**
- `mcp-github` — merge triggers pipeline, deploy after merge
- `mcp-slack` — build failure alerts, deploy notifications
- `mcp-itsm` — block deploys during active P1 incidents

## Folder Structure

```
cicd-pipeline-management/
├── SKILL.md                       # Decision tree + safety checklist
├── scripts/
│   └── parse_logs.py              # Log pattern classifier (test/build/auth/timeout)
├── references/
│   ├── tool-sequences.md          # 8 tools + deployment safety checklist
│   ├── cross-mcp-workflows.md     # CI/CD + GitHub + Slack + ITSM
│   └── examples.md                # Debug failure, safe deploy
├── README.md
└── LICENSE
```

## Example

**User:** "Why is the build failing?"

**Agent behavior:**
1. Gets latest failed run details
2. Fetches logs for the failed step
3. Classifies: test failure at auth_test.rs:45

**Result:**
```
❌ Build failing on feat/auth
Failed step: test
Error: auth_test.rs:45 — expected 200, got 401
Root cause: Genuine test failure (not flaky). Fix needed.
```

## Success Criteria

| Metric | Target |
|--------|--------|
| No blind deploys | CI always verified before deploying |
| Debug efficiency | Root cause in 2-3 tool calls |
| Smart reruns | Never rerun > 2x without investigating |
| Deploy safety | Staging verified before production |

## Scripts

### `parse_logs.py`
Classifies CI failure logs into categories with recommended actions:
```bash
python scripts/parse_logs.py "FAILED: test_payment_retry — assertion failed"
# → {"category": "test_failure", "action": "Fix failing test", "flaky": false}
```

## MCP Server Compatibility

| Tool | Purpose |
|------|---------|
| `list_pipeline_runs` | List by branch/status |
| `get_pipeline_run` | Run details (steps, timing) |
| `get_pipeline_logs` | Step-level logs |
| `rerun_pipeline` | Retry failed run |
| `list_artifacts` | Build outputs |
| `get_deployment_status` | Current deploy state |
| `trigger_deployment` | Deploy to environment |
| `cancel_pipeline` | Abort running pipeline |

## Related Skills

- [skill-github-development](https://github.com/zavora-ai/skill-github-development) — Merge → deploy flow
- [skill-slack-collaboration](https://github.com/zavora-ai/skill-slack-collaboration) — Build/deploy alerts

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
