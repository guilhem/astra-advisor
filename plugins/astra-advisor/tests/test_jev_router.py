import contextlib
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch


PLUGIN = Path(__file__).resolve().parents[1]
SCRIPT = PLUGIN / "scripts/jev_router.py"
spec = importlib.util.spec_from_file_location("jev_router", SCRIPT)
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)


def answer(choice="sol"):
    probabilities = {key: 0.05 for key in (*router.PROFILES, "defer")}
    probabilities[choice] = 0.85
    return {"model": router.MODEL, "answers": {"route": {
        "type": "choice", "choice": choice, "probabilities": probabilities,
        "confidence": 0.85,
    }}, "usage": {"input_tokens": 10, "output_tokens": 2}}


def event(tool_input=None, **changes):
    return {"hook_event_name": "PreToolUse", "tool_name": "spawn_agent",
            "model": "active-parent-is-not-a-pin", "tool_input": tool_input or {"message": "Run tests"}, **changes}


class JevRouterTests(unittest.TestCase):
    def test_packaged_hook_runs_for_canonical_spawn(self):
        config = json.loads((PLUGIN / "hooks/hooks.json").read_text())
        self.assertEqual(set(config["hooks"]), {"PreToolUse"})
        group, = config["hooks"]["PreToolUse"]
        self.assertEqual(group["matcher"], "^spawn_agent$")
        handler, = group["hooks"]
        self.assertEqual(handler["type"], "command")
        self.assertEqual(handler["timeout"], 15)
        self.assertIn("scripts/jev_router.py", handler["command"])
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], input=json.dumps(event()), text=True,
            capture_output=True, env={**os.environ, "TYPESAFE_API_KEY": "", "JEV_API_KEY": ""},
            timeout=5,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr.strip(), "Astra Jev routing unavailable; using native spawn defaults.")
        stdout = io.StringIO()
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "key"}), \
             patch.object(router, "ask_jev", return_value=answer("sol")), \
             patch.object(sys, "stdin", io.StringIO(json.dumps(event()))), \
             contextlib.redirect_stdout(stdout):
            router.main()
        self.assertEqual(json.loads(stdout.getvalue())["hookSpecificOutput"]["updatedInput"],
                         {"message": "Run tests", "model": "gpt-6-sol", "reasoning_effort": "high"})

    def test_ignores_unrelated_and_unclassifiable_inputs_without_provider(self):
        cases = [
            None, [], {}, {"hook_event_name": "SubagentStart"},
            event(tool_name="Agent"), event(tool_name="multi_agent_v1__spawn_agent"),
            event({"message": " "}), event({"message": "Run", "model": "gpt-6-luna"}),
            event({"message": "Run", "model": ""}),
            event({"message": "Run", "reasoning_effort": "low"}),
            event({"message": "Run", "agent_type": "reviewer"}),
            event({"items": [{"type": "image", "image_url": "data:"}]}),
            event({"items": [{"type": "text", "text": "Run"}, {"type": "image"}]}),
            event({"message": "Run", "items": [{"type": "text", "text": "Tests"}]}),
            event({"items": [{"type": "text", "text": "  "}]}),
        ]
        with patch.object(router, "ask_jev", side_effect=AssertionError("provider called")):
            for candidate in cases:
                with self.subTest(candidate=candidate):
                    self.assertIsNone(router.route(candidate))

    def test_null_pins_and_text_items_route_once_preserving_all_arguments(self):
        original = {"items": [{"type": "text", "text": " Implement"}, {"type": "text", "text": "tests "}],
                    "model": None, "reasoning_effort": None, "fork_context": True,
                    "custom": {"keep": [1, 2]}}
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "preferred", "JEV_API_KEY": "alias"}), \
             patch.object(router, "ask_jev", return_value=answer("luna")) as ask:
            result = router.route(event(original))
        ask.assert_called_once_with("Implement\ntests", "preferred")
        self.assertEqual(result, {"hookSpecificOutput": {
            "hookEventName": "PreToolUse", "permissionDecision": "allow",
            "updatedInput": {**original, "model": "gpt-6-luna", "reasoning_effort": "max"},
        }})
        self.assertEqual(original["model"], None)
        low_confidence = answer("luna")
        low_confidence["answers"]["route"]["confidence"] = 0.01
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "", "JEV_API_KEY": "alias"}), \
             patch.object(router, "ask_jev", return_value=low_confidence) as ask:
            self.assertEqual(router.route(event())["hookSpecificOutput"]["updatedInput"]["model"], "gpt-6-luna")
        ask.assert_called_once_with("Run tests", "alias")

    def test_all_profiles_defer_invalid_and_provider_failure(self):
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "key"}):
            for choice, expected in router.PROFILES.items():
                with self.subTest(choice=choice), patch.object(router, "ask_jev", return_value=answer(choice)):
                    output = router.route(event())
                    self.assertEqual((output["hookSpecificOutput"]["updatedInput"]["model"],
                                      output["hookSpecificOutput"]["updatedInput"]["reasoning_effort"]), expected)
            with patch.object(router, "ask_jev", return_value=answer("defer")):
                self.assertIsNone(router.route(event()))
            for mutate in (
                lambda a: a["answers"]["route"].update(choice="unknown"),
                lambda a: a["answers"]["route"]["probabilities"].update(sol=float("nan")),
                lambda a: a["answers"]["route"]["probabilities"].update(sol=0.2),
                lambda a: a["answers"]["route"].update(confidence=1.1),
                lambda a: a.update(model="unexpected"),
            ):
                bad = copy.deepcopy(answer())
                mutate(bad)
                with self.subTest(bad=bad), patch.object(router, "ask_jev", return_value=bad), \
                     contextlib.redirect_stderr(io.StringIO()):
                    self.assertIsNone(router.route(event()))
            warning = io.StringIO()
            with patch.object(router, "ask_jev", side_effect=RuntimeError("SECRET and prompt")), \
                 contextlib.redirect_stderr(warning):
                self.assertIsNone(router.route(event()))
            self.assertEqual(warning.getvalue().strip(), "Astra Jev routing unavailable; using native spawn defaults.")


try:
    import httpx2
    import typesafe_sdk
except ImportError:
    httpx2 = None
    typesafe_sdk = None


@unittest.skipUnless(typesafe_sdk is not None, "typesafe-sdk not installed; CI installs requirements.txt")
class SdkTransportTests(unittest.TestCase):
    def run_transport(self, statuses):
        requests = []
        statuses = iter(statuses)

        def handler(request):
            requests.append(request)
            status = next(statuses)
            if status == 200:
                return httpx2.Response(200, json=answer("sol"))
            return httpx2.Response(status, json={"error": {"message": "SECRET remote failure"}})

        original_client = typesafe_sdk.TypeSafeClient

        def client_factory(**kwargs):
            self.assertEqual(kwargs["retry"].max_retries, 2)
            self.assertEqual(kwargs["retry"].timeout, 10.0)
            return original_client(**kwargs, transport=httpx2.MockTransport(handler))

        stderr = io.StringIO()
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "test-key"}), \
             patch.object(typesafe_sdk, "TypeSafeClient", side_effect=client_factory), \
             contextlib.redirect_stderr(stderr):
            result = router.route(event({"message": "Run existing tests", "fork_context": False}))
        return result, requests, stderr.getvalue()

    def test_real_sdk_request_and_403_does_not_retry(self):
        result, requests, stderr = self.run_transport([200])
        self.assertEqual(len(requests), 1)
        body = json.loads(requests[0].content)
        self.assertEqual(body["state"], {"mission": "Run existing tests"})
        self.assertEqual(body["questions"], {"route": router.RUBRIC})
        self.assertEqual(result["hookSpecificOutput"]["updatedInput"], {
            "message": "Run existing tests", "fork_context": False,
            "model": "gpt-6-sol", "reasoning_effort": "high"})
        self.assertEqual(stderr, "")
        result, requests, stderr = self.run_transport([403])
        self.assertIsNone(result)
        self.assertEqual(len(requests), 1)
        self.assertNotIn("SECRET", stderr)

    def test_real_sdk_transient_retry_then_success_and_exhaustion(self):
        result, requests, stderr = self.run_transport([503, 200])
        self.assertEqual(len(requests), 2)
        self.assertEqual(result["hookSpecificOutput"]["updatedInput"]["model"], "gpt-6-sol")
        self.assertEqual(stderr, "")
        result, requests, stderr = self.run_transport([503, 503, 503])
        self.assertIsNone(result)
        self.assertEqual(len(requests), 3)
        self.assertNotIn("SECRET", stderr)


if __name__ == "__main__":
    unittest.main()
