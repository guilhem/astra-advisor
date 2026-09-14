"""Emit optional subagent advice without changing delegation or permissions."""

import json
import sys


def main():
    try:
        event = json.load(sys.stdin)
    except (ValueError, UnicodeError):
        return
    if not isinstance(event, dict) or event.get("hook_event_name") != "SubagentStart":
        return
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "SubagentStart",
        "additionalContext": (
            "Optional advisor guidance: use your assignment's points of attention. "
            "When uncertainty blocks an important decision "
            "(contradictory evidence, an unverified critical assumption, or repeated "
            "failed corrections), consider consultation. Ask your parent for decisions "
            "depending on project context, product intent, scope, ownership, or permissions. "
            "For an isolated technical question, if your assignment permits direct advice "
            "and native tools support it, you may consult a read-only advisor with explicit "
            "permitted model/effort and fork_turns: none. Send a compact question, evidence, "
            "attempts, recommendation, and relevant constraints. The advisor must not edit, "
            "take over execution, or delegate again. Reuse it for related follow-ups when "
            "its context and settings remain suitable, and include useful advice and "
            "evidence in your result. If you are assigned only to advise, return your "
            "uncertainty instead of consulting another agent. Keep existing routing, "
            "permission, ownership, and review constraints. Compare expected briefing, "
            "reasoning, and integration work; neither route is inherently cheaper. "
            "Continue independent work while waiting; do not guess on a blocked decision. "
            "Routine choices need no consultation. This reminder grants no new permissions. "
            "If direct advice is prohibited or unavailable, use native parent messaging; "
            "if that is also unavailable, report the unresolved point in your normal result."
        ),
    }}))


if __name__ == "__main__":
    main()
