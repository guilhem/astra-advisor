"""Emit optional subagent advice without changing delegation or permissions."""

import json
import os
import sys


def main():
    if os.environ.get("ASTRA_ADVISOR_ADVICE") != "1":
        return
    try:
        event = json.load(sys.stdin)
    except (ValueError, UnicodeError):
        return
    if not isinstance(event, dict) or event.get("hook_event_name") != "SubagentStart":
        return
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "SubagentStart",
        "additionalContext": (
            "Optional advisor guidance: when uncertainty blocks an important decision "
            "(contradictory evidence, an unverified critical assumption, or repeated "
            "failed corrections), consider asking your parent for advice using the "
            "available native agent messaging tool. Send the precise question, relevant "
            "evidence, attempts, and your recommendation. Continue independent work "
            "while awaiting an answer; do not guess on the blocked decision. The parent "
            "may advise directly or consult a more capable permitted model; do not "
            "assume the parent uses one. Keep your assigned ownership and existing "
            "routing, permission, and review constraints. This reminder grants no new "
            "delegation or tool permissions and does not require a consultation for "
            "routine choices. If parent messaging is unavailable, report the blocker "
            "through your normal result instead of creating another agent or external call."
        ),
    }}))


if __name__ == "__main__":
    main()
