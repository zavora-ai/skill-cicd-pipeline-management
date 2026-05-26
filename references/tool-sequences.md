# CI/CD Tool Sequences Reference

## Tool Inventory (mcp-cicd, 8 tools)

| Tool | Risk | Purpose |
|------|------|---------|
| `list_pipeline_runs` | read | List runs by branch/status |
| `get_pipeline_run` | read | Run details (steps, timing) |
| `get_pipeline_logs` | read | Step-level logs for debugging |
| `rerun_pipeline` | write | Retry a failed run |
| `list_artifacts` | read | Build outputs |
| `get_deployment_status` | read | Current deployment state |
| `trigger_deployment` | write | Deploy to environment |
| `cancel_pipeline` | write | Abort running pipeline |

## Sequence: Debug Failure (2-3 calls)

```
1. get_pipeline_run(id: "run_123")
   → {status: "failed", failed_step: "test", duration: "3m 42s", branch: "feat/auth"}

2. get_pipeline_logs(run_id: "run_123", step: "test")
   → {logs: "FAILED: src/auth_test.rs:45 — assertion failed: expected 200, got 401"}

3. Diagnose: Test failure in auth module. Not infra, not flaky — genuine bug.
```

## Sequence: Safe Deployment (3 calls)

```
1. list_pipeline_runs(branch: "main", status: "success", limit: 1)
   → {id: "run_200", commit: "abc123", status: "success"} — CI green ✅

2. get_deployment_status(env: "staging")
   → {version: "v2.3.0", status: "healthy", last_deploy: "2h ago"}

3. trigger_deployment(env: "production", version: "v2.3.1", run_id: "run_200")
   → {deployment_id: "dep_456", status: "in_progress"}
```

## Sequence: Rerun with Investigation (2 calls)

```
1. get_pipeline_logs(run_id: "run_123", step: "test")
   → Analyze: is this flaky (intermittent) or genuine?

2. If flaky (seen before, timing-dependent):
   rerun_pipeline(run_id: "run_123")
   → {new_run_id: "run_124", status: "running"}

   If genuine: DON'T rerun. Report root cause.
```

## Deployment Safety Checklist

| Check | Tool | Required |
|-------|------|----------|
| CI passes | `list_pipeline_runs(status: "success")` | ✅ Always |
| Staging healthy | `get_deployment_status(env: "staging")` | ✅ Always |
| No active incidents | (cross-MCP: ITSM) | ✅ For production |
| User confirmation | Ask user | ✅ For production |
