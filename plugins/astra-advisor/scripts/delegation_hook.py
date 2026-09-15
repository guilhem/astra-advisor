"""Advisory preflight for Astra delegation; never block or rewrite a tool call."""

import json
import re
import sys


def diagnose(event):
    if not isinstance(event, dict) or event.get("hook_event_name") != "PreToolUse":
        return {}
    if event.get("tool_name") not in ("Agent", "spawn_agent", "collaboration.spawn_agent"):
        return {}
    args = event.get("tool_input")
    if not isinstance(args, dict):
        return {}

    issues = []
    fork = args.get("fork_turns", "all")
    if fork == "all":
        for field in ("model", "reasoning_effort"):
            if field in args:
                issues.append(f"{field} must be omitted for an inherited full-context fork")
    elif isinstance(fork, str) and (fork == "none" or re.fullmatch(r"0*[1-9][0-9]*", fork)):
        for field in ("model", "reasoning_effort"):
            value = args.get(field)
            if not isinstance(value, str) or not value.strip():
                issues.append(f"{field} is not an explicit non-empty string for a reduced-context fork")
    else:
        issues.append('fork_turns must be "all", "none", or a positive integer string')
    if not issues:
        return {}

    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": (
                "Astra Advisor delegation advisory: " + "; ".join(issues) + ". "
                "Full-context forks inherit model and effort; reduced-context forks "
                "use explicit settings under the live tool schema and routing rules. "
                "This hook does not block, rewrite, or retry the call, or verify "
                "model availability or runtime settings."
            ),
        }
    }


if __name__ == "__main__":
    try:
        event = json.load(sys.stdin)
    except (ValueError, UnicodeError):
        print("Astra Advisor: invalid hook input; advisory skipped.", file=sys.stderr)
        event = None
    print(json.dumps(diagnose(event)))
