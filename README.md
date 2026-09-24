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
`description`, `model`, and `reasoning_effort`. A marketplace installation does not
create a checkout in your current directory. If you do not already have one,
get the profiles from this repository:

~~~sh
git clone https://github.com/guilhem/astra-advisor.git
cd astra-advisor
~~~

From the checkout root, copy Astra's profiles into the shared directory without
replacing existing files:

~~~sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/subagent-router"
cp -n plugins/astra-advisor/routing/astra-*.json "${CODEX_HOME:-$HOME/.codex}/subagent-router/"
~~~

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
