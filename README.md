# Astra Advisor

Astra Advisor delegates software work through native Codex agents. The selected
parent model frames the task, interprets evidence, makes decisions, and accepts
the result. A retained squire handles related research and operational work;
independent read-only acceptance review checks substantial implementations.

## Set up

~~~sh
codex plugin marketplace add guilhem/astra-advisor --ref main
codex plugin add astra-advisor@astra-advisor
~~~

Start a task with:

~~~text
Use $astra-advisor:orchestration to build, verify, and review this work.
~~~

The [orchestration skill](plugins/astra-advisor/skills/orchestration/SKILL.md)
contains the delegation contract. Read its references only when needed:
[operations](plugins/astra-advisor/skills/orchestration/references/operations.md),
[squire](plugins/astra-advisor/skills/orchestration/references/squire.md),
[review](plugins/astra-advisor/skills/orchestration/references/review.md), and
[cost receipts](plugins/astra-advisor/skills/orchestration/references/cost-receipts.md).
Separate app tasks require an explicit request. Usage and cost receipts are
available on request; they distinguish observed usage from API price estimates.

## Optional model routing

The separate [codex-subagent-router](https://github.com/guilhem/codex-subagent-router)
plugin owns the Jev SDK, `TYPESAFE_API_KEY` in the Codex process environment,
and its trusted hook. Install and enable it separately if you want Jev to select model
and effort for unpinned native agent spawns. Astra itself needs no SDK or key.
The router reads JSON profiles from `${CODEX_HOME:-~/.codex}/subagent-router/*.json`.
The filename stem is the Jev Choice id; `defer` is reserved. Each profile has
`description`, `model`, and `reasoning_effort`.

Trust Astra's **Install Astra routing profiles** hook in Codex's hook settings,
then start a new session. Its `SessionStart` hook installs the three bundled
`astra-*.json` profiles automatically, using the system shell on macOS/Linux
and PowerShell on Windows. No checkout, SDK, or separate installer is needed.
Codex requires this trust step for
[plugin hooks](https://developers.openai.com/plugins/build/plugins).

Existing files are never replaced, including profiles you have customized.
Updates add missing profiles but leave existing ones unchanged; to restore a
bundled default, delete its installed file and start a new session. Disable
Astra's hook before removing its profiles if you want them to stay removed.

The three profiles route routine evidence and execution to Luna/max, ordinary
implementation and review to Sol/high, and complex diagnosis or high-risk work
to Opus/high. Native spawns with an explicit model, effort, or role bypass the
router. An empty or invalid profile catalog, `defer`, or provider failure leaves
native defaults in place. A selected model is not proof of the model that ran.
Follow explicit user and applicable `AGENTS.md` routing requirements; the
optional router cannot override them.

## Development

~~~sh
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
