import json
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path


PLUGIN = Path(__file__).resolve().parents[1]
CONFIG = json.loads((PLUGIN / "hooks/hooks.json").read_text())
GROUP, = CONFIG["hooks"]["PreToolUse"]
HANDLER, = GROUP["hooks"]
CONTROLS = {"model": "gpt-6-astra", "reasoning_effort": "low", "fork_turns": "none"}


class DelegationHookTests(unittest.TestCase):
    def run_hook(self, payload):
        # Exercise the installed command from an unrelated cwd and a path with spaces.
        with tempfile.TemporaryDirectory(prefix="astra hook ") as directory:
            root = Path(directory) / "plugin with spaces"
            root.symlink_to(PLUGIN, target_is_directory=True)
            result = subprocess.run(
                HANDLER["command"], shell=True, cwd=directory,
                env={**os.environ, "PLUGIN_ROOT": str(root)},
                input=payload, text=True, capture_output=True,
                timeout=HANDLER["timeout"],
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def event(self, args, tool="spawn_agent", event="PreToolUse"):
        return json.dumps({"hook_event_name": event, "tool_name": tool, "tool_input": args})

    def test_complete_calls_are_silent_and_do_not_restrict_live_model_choices(self):
        for tool in ("Agent", "spawn_agent", "collaboration.spawn_agent"):
            self.assertIsNotNone(re.fullmatch(GROUP["matcher"], tool))
            for model in ("gpt-6-astra", "gpt-5.6-luna", "gpt-5.6-sol", "future-model"):
                with self.subTest(tool=tool, model=model):
                    self.assertEqual(self.run_hook(self.event({**CONTROLS, "model": model}, tool)), {})

    def test_incomplete_controls_only_add_context_without_echoing_input(self):
        cases = [({}, ("model", "reasoning_effort", "fork_turns"))]
        for field in ("model", "reasoning_effort", "fork_turns"):
            for value in (None, "", "  ", False, [], {}):
                cases.append(({**CONTROLS, field: value}, (field,)))
            cases.append(({key: value for key, value in CONTROLS.items() if key != field}, (field,)))
        cases.append(({**CONTROLS, "fork_turns": "all"}, ("fork_turns",)))
        for args, fields in cases:
            with self.subTest(args=args):
                output = self.run_hook(self.event({**args, "message": "PRIVATE TASK CONTENT"}))
                self.assertEqual(set(output), {"hookSpecificOutput"})
                specific = output["hookSpecificOutput"]
                self.assertEqual(set(specific), {"hookEventName", "additionalContext"})
                self.assertEqual(specific["hookEventName"], "PreToolUse")
                for field in fields:
                    self.assertIn(field, specific["additionalContext"])
                self.assertNotIn("PRIVATE TASK CONTENT", json.dumps(output))

    def test_unrelated_events_and_malformed_input_are_skipped(self):
        self.assertIsNone(re.fullmatch(GROUP["matcher"], "mcp__other__spawn_agent"))
        for payload in (
            self.event({}, tool="Bash"), self.event({}, event="SubagentStop"),
            self.event(None), self.event([]), "null", "[]", "{}", "", "{broken",
        ):
            with self.subTest(payload=payload):
                self.assertEqual(self.run_hook(payload), {})


if __name__ == "__main__":
    unittest.main()
