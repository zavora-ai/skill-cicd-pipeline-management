# 🚀 Pipeline Status Report

**Generated:** {timestamp}
**Pipeline:** {pipeline_name}
**Trigger:** {trigger_type}

## Execution Summary

| Stage | Status | Duration |
|-------|--------|----------|
| {stage_1} | {status_1} | {duration_1} |
| {stage_2} | {status_2} | {duration_2} |
| {stage_3} | {status_3} | {duration_3} |
| {stage_4} | {status_4} | {duration_4} |

## Build Info

| Field | Value |
|-------|-------|
| Commit | {commit_sha} |
| Branch | {branch} |
| Author | {author} |
| Total Duration | {total_duration} |
| Artifact | {artifact_url} |

## Status Legend

- ✅ Passed — Stage completed successfully
- ❌ Failed — Stage errored
- ⏳ Running — In progress
- ⏭️ Skipped — Condition not met

---
*Tracked by {agent_name} • Run #{run_number}*
