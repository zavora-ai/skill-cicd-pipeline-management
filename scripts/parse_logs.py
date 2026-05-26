#!/usr/bin/env python3
"""Parse CI/CD logs to extract failure reason and suggest action."""
import json, sys, re

PATTERNS = [
    (r"FAILED.*test", "test_failure", "Fix failing test or mark as flaky if intermittent"),
    (r"error\[E\d+\]|cannot find", "compile_error", "Fix compilation error"),
    (r"timeout|timed out", "timeout", "Increase timeout or optimize slow step"),
    (r"permission denied|403|401", "auth_error", "Check credentials and permissions"),
    (r"no space|disk full", "resource_error", "Clean up disk or increase runner size"),
    (r"rate limit|429", "rate_limit", "Add retry with backoff or reduce parallelism"),
]

def parse(log_text):
    for pattern, category, action in PATTERNS:
        if re.search(pattern, log_text, re.IGNORECASE):
            return {"category": category, "action": action, "flaky": category == "timeout"}
    return {"category": "unknown", "action": "Review logs manually", "flaky": False}

if __name__ == "__main__":
    print(json.dumps(parse(sys.argv[1] if len(sys.argv) > 1 else ""), indent=2))
