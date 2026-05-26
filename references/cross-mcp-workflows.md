# CI/CD Cross-MCP Workflows

## CI/CD + Slack: Build Notifications
```
CICD: get_pipeline_run(id) → {status: "failed", branch: "main"}
SLACK: send_message(channel: "#engineering", text: "❌ Build failed on main. Step: test. @last-committer please investigate.")
```

## CI/CD + GitHub: Post-Merge Deploy
```
GITHUB: merge_pull_request(number: 42)
CICD: list_pipeline_runs(branch: "main", limit: 1) → wait for success
CICD: trigger_deployment(env: "staging")
SLACK: send_message(channel: "#deploys", text: "✅ PR #42 merged → staging deploy triggered")
```

## CI/CD + ITSM: Deploy Freeze During Incidents
```
ITSM: search_tickets(priority: "critical", status: "open") → active P1 exists
CICD: [BLOCK] trigger_deployment → "⚠️ Deploy blocked: active P1 incident INC-1001"
```
