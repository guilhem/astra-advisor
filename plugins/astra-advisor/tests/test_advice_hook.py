import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


PLUGIN = Path(__file__).resolve().parents[1]


class AdviceHookTests(unittest.TestCase):
    def test_packaged_command_is_event_scoped_and_context_only(self):
        with tempfile.TemporaryDirectory(prefix="advisor hook ") as directory:
            plugin = Path(directory) / "plugin with spaces"
            shutil.copytree(PLUGIN / "scripts", plugin / "scripts")
            config = json.loads((PLUGIN / "hooks/hooks.json").read_text())
            self.assertEqual(set(config["hooks"]), {"SubagentStart"})
            groups = config["hooks"]["SubagentStart"]
            self.assertEqual(len(groups), 1)
            self.assertNotIn("matcher", groups[0])
            self.assertEqual(len(groups[0]["hooks"]), 1)
            handler = groups[0]["hooks"][0]
            self.assertEqual(handler["type"], "command")
            event = json.dumps({"hook_event_name": "SubagentStart", "agent_type": "worker"})
            cases = [(value, False) for value in (
                "", "{", "[]", "null", '"text"', "{}",
                '{"hook_event_name":"SessionStart"}',
            )]
            cases.append((event, True))
            for payload, emits_context in cases:
                with self.subTest(payload=payload):
                    env = dict(os.environ, PLUGIN_ROOT=str(plugin))
                    result = subprocess.run(
                        handler["command"], shell=True, cwd=directory, env=env,
                        input=payload, text=True, capture_output=True,
                        timeout=handler["timeout"],
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stderr, "")
                    if emits_context:
                        output = json.loads(result.stdout)
                        self.assertEqual(set(output), {"hookSpecificOutput"})
                        context = output["hookSpecificOutput"]
                        self.assertEqual(set(context), {"hookEventName", "additionalContext"})
                        self.assertEqual(context["hookEventName"], "SubagentStart")
                        self.assertTrue(context["additionalContext"].strip())
                    else:
                        self.assertEqual(result.stdout, "")
