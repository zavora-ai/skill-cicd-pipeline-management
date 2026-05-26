# CI/CD Skill Examples

## Example 1: "Why is the build failing?"

**Tool calls:**
```
1. list_pipeline_runs(branch: "feat/auth", status: "failed", limit: 1)
   → {id: "run_123", failed_step: "test"}
2. get_pipeline_logs(run_id: "run_123", step: "test")
   → "FAILED: auth_test.rs:45 — expected 200, got 401"
```

**Response:**
```
❌ Build failing on feat/auth

**Failed step:** test
**Error:** auth_test.rs:45 — expected 200, got 401
**Root cause:** Auth endpoint returning 401 instead of 200. Likely missing token in test setup.

This is a genuine test failure (not flaky). Fix needed before merge.
```

## Example 2: "Deploy to production"

**Tool calls:**
```
1. list_pipeline_runs(branch: "main", status: "success", limit: 1) → CI green ✅
2. get_deployment_status(env: "staging") → healthy ✅
3. trigger_deployment(env: "production", version: "v2.3.1")
```

**Response:**
```
🚀 Production deployment triggered

**Version:** v2.3.1
**CI:** ✅ Passing (run_200)
**Staging:** ✅ Healthy
**Status:** Deploying...

I'll monitor for 10 minutes. Will alert if health checks fail.
```
