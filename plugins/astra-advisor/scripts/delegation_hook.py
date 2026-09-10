"""Advisory preflight for Astra delegation; never block or rewrite a tool call."""

import json
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
    for field in ("model", "reasoning_effort"):
        value = args.get(field)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"{field} is not an explicit non-empty string")
    if args.get("fork_turns") != "none":
        issues.append('fork_turns is not "none"')
    if not issues:
        return {}

    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": (
                "Astra Advisor delegation advisory: " + "; ".join(issues) + ". "
                "For Astra orchestration, select explicit model/effort from the live "
                'tool schema and use fork_turns="none". This call is unchanged and '
                "will proceed; do not claim these settings were enforced. "
                "Other delegation workflows may intentionally inherit settings."
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
