# Astra Advisor

Astra Advisor delegates software work through native Codex agents. The selected
parent model frames the task, interprets evidence, makes decisions, and accepts
the result. A retained squire handles related research and operational work;
independent read-only acceptance review checks substantial implementations.

## Set up

Install the plugin, then install the [TypeSafe Python SDK](https://pypi.org/project/typesafe-sdk/)
once in the Python environment used by the hook's `python3` command (Python 3.10+).
For an environment where `python3 -m pip` is available:

~~~sh
codex plugin marketplace add DannyMac180/astra-advisor --ref main
codex plugin add astra-advisor@astra-advisor
python3 -m pip install 'typesafe-sdk==0.7.1'
~~~

Set `TYPESAFE_API_KEY` in the Codex process environment; `JEV_API_KEY` is a
supported alias. The hook never loads a workspace `.env` file or transcript for
credentials. Review and enable the plugin's `PreToolUse` hook in Codex `/hooks`,
then start a fresh session. The hook runs only when trusted and enabled by the user.
It needs no separate service, custom installer, or `jev_codex` workflow installation.
The small Jev adapter is attributed to `jev_codex` in its source.

Start a task with:

~~~text
Use $astra-advisor:orchestration to build, verify, and review this work.
~~~

If your personal `AGENTS.md` still requires `model` and `reasoning_effort` on
every spawn, replace that rule to activate Jev routing. The plugin does not edit your
personal instructions. A short replacement is:

~~~md
The parent only delegates and interprets: frame the objective, constraints, and
expected result; delegate research, execution, and verification; reuse agents;
interpret evidence and own decisions and acceptance. Omit model and
reasoning_effort on native spawns unless intentionally pinned. Let Jev route
unpinned spawns when its trusted hook is enabled.
~~~

## Routing and fallback

The hook matches native `spawn_agent` calls and reads the original `tool_input`.
If either `model` or `reasoning_effort` is non-null, it leaves the input untouched:
explicit settings win. With both absent or null, Jev receives only the mission
text and may choose Luna/max, Sol/high, Opus/high, or defer. An explicit
`agent_type` also leaves the original input untouched, preserving native role
settings. Codex still validates model availability after a rewrite. A Jev choice
is a selected setting, not proof of the model that actually ran.

If the SDK or key is missing, Jev defers, or routing errors, the original input
passes through to native inheritance/defaults. The SDK has at most two retries
within a 10-second retry budget; the hook has a 15-second timeout. An explicit
model or effort remains untouched even when Jev is unavailable. The plugin does
not promise that every Jev choice is available on every Codex host.

The [orchestration skill](plugins/astra-advisor/skills/orchestration/SKILL.md)
contains the delegation contract. Read its references only when needed:
[operations](plugins/astra-advisor/skills/orchestration/references/operations.md),
[squire](plugins/astra-advisor/skills/orchestration/references/squire.md),
[review](plugins/astra-advisor/skills/orchestration/references/review.md), and
[cost receipts](plugins/astra-advisor/skills/orchestration/references/cost-receipts.md).
Separate app tasks require an explicit request. Usage and cost receipts are
available on request; they distinguish observed usage from API price estimates.

## Development

~~~sh
python3 -m pip install -r plugins/astra-advisor/requirements.txt
sh plugins/astra-advisor/scripts/verify.sh
~~~

For a local checkout, install its path as a marketplace:

~~~sh
codex plugin marketplace add /absolute/path/to/astra-advisor
codex plugin add astra-advisor@astra-advisor
~~~

To update an installed plugin:

~~~sh
codex plugin marketplace upgrade astra-advisor
codex plugin add astra-advisor@astra-advisor
~~~

## Go deeper

I write [Attention Heads](https://attentionheads.substack.com/) about AI,
cognition, and agentic engineering. [Subscribe](https://attentionheads.substack.com/subscribe?utm_source=github&utm_medium=readme&utm_campaign=astra-advisor)
for the Agentic Engineering Field Notes.
