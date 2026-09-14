# Astra Advisor

**Your selected model plans the work, chooses useful bounded delegation dynamically,
and owns verification and acceptance.**

Astra Advisor is a Codex plugin for capability-routed software delivery. Give it
the goal, constraints, and repository context; it decides whether independent work
should run alongside the parent session and chooses a supported native subagent
model and effort for each bounded deliverable.

## Cloud limitation

ChatGPT Work cloud `create_thread` must omit `model` and
`thinking`, so it cannot currently promise arbitrary model or effort control. Astra
does not dispatch a model-pinned request there by default. Native Codex subagents are usable
where the current tool schema exposes the needed controls.

## Go deeper

I write [Attention Heads](https://attentionheads.substack.com/) — deep,
evidence-backed writing on AI, cognition, and agentic engineering. The **Agentic
Engineering Field Notes** series covers the craft of using AI. [Subscribe](https://attentionheads.substack.com/subscribe?utm_source=github&utm_medium=readme&utm_campaign=astra-advisor)
to get new posts in your inbox.

## Quick start

Install the plugin in a current Codex CLI or ChatGPT desktop app with plugins
enabled. Start a fresh task after installation with your preferred parent model and
effort supported by the current Codex host:

~~~sh
codex plugin marketplace add DannyMac180/astra-advisor --ref main
codex plugin add astra-advisor@astra-advisor
~~~

Start a task with:

~~~text
Use $astra-advisor:orchestration to plan, build, verify, and review this work.
~~~

## How routing works

The parent remains the architect and acceptance owner at the model and effort
selected by the user. The skill never changes the parent session or
claims runtime settings without evidence.

Use tools directly to understand context and decide the next step. Prefer delegation
for a bounded action, observation, or lookup with a clear goal and expected result:
for example, inspect deployment logs, check a defined hypothesis, or execute an
authorized command and verify its effect. Intent determines the boundary, not output
size or the number of tools. The result must justify briefing, waiting, and integration.
The [tool execution reference](plugins/astra-advisor/skills/orchestration/references/tool-execution.md)
defines the brief and concise, evidence-backed return. Straightforward missions
prefer Luna under the existing routing rules; this is not automatic tool interception
or a measured cost-saving guarantee.

When delegation helps, the parent uses the exposed generic `collaboration.spawn_agent`
tool. Substantial reviews prefer
`fork_turns: "all"` to retain the discussed needs, constraints, and tradeoffs. Full
forks inherit the parent model and effort, so both overrides are omitted. Explicit
user and applicable `AGENTS.md` routing instructions take precedence: if different
settings are required, use a compatible reduced-context fork with those settings
and supply the relevant requirements and evidence. Narrowly targeted checks may
also use reduced context when sufficient. Other bounded delegates receive explicit
`model`, `reasoning_effort`, and `fork_turns: "none"`. The parent chooses
among live-supported models using your routing preferences, task risk, context,
and independent work. There are no predefined role TOMLs or companion installer.
The parent gives each subagent a short contract: objective, scope, constraints,
expected result, and success criterion, plus explicit file ownership when writing.
It adds known points of attention and decisions to bring back to the parent, and
states whether direct read-only advice is permitted. A local uncertainty need not
prevent delegation when the goal, ownership, and validation are clear; advice is
optional and does not make an unsuitable model a suitable choice.
When advice is permitted, its constraints travel in the brief even without the hook.
The parent continues useful work while the delegate runs and owns integration.

The [routing reference](plugins/astra-advisor/skills/orchestration/references/routing-defaults.md)
contains optional model suggestions, not an allowlist. Live tool metadata determines
which models and efforts are available.

If a selected model, effort, control, or tool is unavailable, conflicting, or
unobservable, the parent fails that delegation closed and reports the limitation. It does
not silently substitute a model, effort, role, or fabricated tool. Chosen values and
runtime-confirmed values are reported separately.

For an initial substantial implementation, the parent inspects the complete diff and runs
the requested checks, then sends the stable change set to an independent read-only
reviewer, preferably with a full fork as described above. Even with inherited context,
a short assignment identifies the diff, accepted scope, and evidence. The reviewer
verifies conclusions against the code and distinguishes requirements from assumptions.
Acceptance requires `ship`, which may include residual
findings. `fix-first` requires a demonstrated in-scope blocking defect; non-blocking
findings alone do not start another correction or review cycle.

After a bounded correction, the parent inspects the delta, runs affected checks, and
obtains targeted confirmation, preferably from the same reviewer. Unaffected evidence
remains valid. Changes to design, authority, data ownership, or material risk require
a new full independent review. `rethink` requires reassessing the plan and scope.
Small documentation and mechanical changes need parent inspection.

## Customize model routing with AGENTS.md

No plugin-specific configuration file is needed. Add your preferences to your
personal `~/.codex/AGENTS.md` (or the `AGENTS.md` in your configured `CODEX_HOME`),
or to your project's `AGENTS.md`. Project guidance overrides conflicting personal
guidance; more specific applicable directory guidance takes precedence. If an
`AGENTS.override.md` is present, Codex uses it instead of `AGENTS.md` in that
directory. See [Codex instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

The skill applies explicit user instructions and applicable `AGENTS.md` guidance
before its routing defaults. Override only the choices you need; the remaining
defaults still apply. For example, add this personal preference section:

~~~md
## Astra Advisor model preferences

- Prefer gpt-5.6-sol at medium effort for well-scoped implementation and reviews.
- Prefer gpt-5.6-luna at high effort for small, straightforward independent tasks.
- Prefer gpt-6-astra for ambiguity, architecture, and difficult diagnosis.
- Choose effort for the task; do not change the user's selected parent model or effort.
~~~

A project can narrow those choices without copying the whole section:

~~~md
## Astra Advisor model preferences

- For this repository, use only gpt-6-astra at high effort for delegated reviews.
~~~

These are examples, not additional plugin defaults. "Prefer" allows another suitable
permitted choice with an explanation; "only" is a restriction. An unavailable required
model or effort blocks that delegation, not independent parent work. Preferences
cannot grant tool access or change the running parent model or effort.

Keep customizations in your instruction files rather than the installed plugin cache,
so plugin updates do not overwrite them. Start a fresh Codex session after editing,
then ask: "Which routing preferences apply here, and which instruction supplies them?"
The parent also passes relevant routing constraints to delegates that may delegate further.

## Optional advice hook

The bundled `SubagentStart` hook reminds new subagents of the optional
[advice routing](plugins/astra-advisor/skills/orchestration/references/operations.md#optional-advice).
Bring decisions requiring project context or authority to the parent. For an isolated
technical question, an assignment may permit direct consultation of a read-only
advisor with a compact brief and suitable model/effort. Reuse a suitable advisor for
related follow-ups; it cannot edit, take over execution, or delegate further.
The delegate returns useful advice and evidence with its result.

Choose by the context needed and total expected work, including briefing and
integration. Neither consulting the parent nor starting a new advisor is always
cheaper. Consultation remains optional and preserves independent review and existing
routing and permission constraints.

To enable the reminder, review and trust this hook in Codex `/hooks`. No environment
variable or additional configuration is required. Leave the hook untrusted,
disable it in `/hooks`, or remove its configuration to stop future injections.
Previously injected context remains in existing agents; start a fresh task to
remove it. Without the hook, the skill and optional advice routing still work;
no consultation is required and the hook grants no delegation permission.

When enabled, it applies to new subagents even outside explicit skill invocations.
It emits only a short context message: no model calls, edits, retries, or telemetry.
If direct advice is prohibited or unavailable, use native parent messaging; if
that is also unavailable, report the unresolved point through the normal result.

The [hook configuration](plugins/astra-advisor/hooks/hooks.json) uses Codex's
[documented hook interface](https://learn.chatgpt.com/docs/hooks).
Local tests exercise the packaged command, event filtering, and context-only output;
live host discovery, trust, context injection, and any quality or cost benefit
still need validation in a fresh Codex task.

## Progress and cost details on request

Updates focus on consequential decisions, results, changes, and blockers. Related
updates can be grouped without mandatory route blocks or paired agent receipts.
Detailed agent IDs, requested settings, and runtime evidence are available on request;
observed mismatches and material capability limitations are still reported.

Ask for usage or cost details to get an API-equivalent receipt from the existing
calculator and available native evidence. No receipt or unavailable-cost notice is
required otherwise. The receipt separates observed consumption from estimated USD
prices and distinguishes whole-task, delegated-only, and partial coverage. Missing
parent or reviewer usage prevents a whole-task claim. Without observed usage, report
why it is unavailable; do not add telemetry infrastructure or invent token counts.

The calculator can reprice the same observed tokens entirely at Astra. The difference
is a **same-token API price comparison**. It does not measure what an
all-Astra run would actually consume, actual net task savings, quality, speed, or a
change to ChatGPT subscription charges or usage credits. No subagents means no
delegation savings. Reasoning effort does not multiply the token price. Demonstrated
savings require comparable observed runs, including coordination and corrections,
with their scope, quality, and cost basis.

The [pricing snapshot](plugins/astra-advisor/pricing/2026-09-04.json) records official
source URLs and standard short-context USD rates per million tokens, verified by
the recording coordinator on September 4, 2026. These are historical estimates;
Sol pricing is promotional and may change. The calculator rejects unsupported
long-context, service-tier, and cache-write cases instead of assuming standard rates.
It conservatively supports at most 128,000 input tokens per call; this is an
implementation support boundary, not a claimed official pricing threshold.

Try the clearly labeled illustrative workload (not a receipt for your task):

~~~sh
python3 plugins/astra-advisor/scripts/cost_receipt.py plugins/astra-advisor/examples/illustrative-usage.json
sh plugins/astra-advisor/scripts/verify.sh
~~~

The calculator emits JSON and accepts `--pricing PATH` for another verified snapshot.
Custom model choices do not change its Astra comparison baseline. A model missing
from the pricing snapshot remains eligible for routing; its cost estimate is unavailable.
Its input lists agents and unique atomic calls, usage provenance, coverage assertions,
and explicit pricing eligibility. It validates cached-input and reasoning-output
subsets, refuses overlapping aggregates, and keeps unknown usage separate from zero.
See the [cost receipt reference](plugins/astra-advisor/skills/orchestration/references/cost-receipts.md)
for the input contract and receipt policy.

## ChatGPT app tasks

Separate app tasks require an explicit user request. For an explicit Codex app task,
`mcp__codex_app__create_thread` supports `model` and `thinking`; call
`mcp__codex_app__list_projects` first for project targets, use a worktree by default
for Git projects, and use local otherwise. Cloud `create_thread` omits both controls,
so the bounded limitation above applies. Do not use an API key, nested CLI, or
invented tool as a workaround.

## Updating

~~~sh
codex plugin marketplace upgrade astra-advisor
codex plugin add astra-advisor@astra-advisor
~~~

For local development, install this checkout as a marketplace:

~~~sh
cd /absolute/path/to/astra-advisor
codex plugin marketplace add /absolute/path/to/astra-advisor
codex plugin add astra-advisor@astra-advisor
~~~

Read only the reference needed for the current operation:

- [Native delegation and app tasks](plugins/astra-advisor/skills/orchestration/references/operations.md)
- [Bounded tool execution tasks](plugins/astra-advisor/skills/orchestration/references/tool-execution.md)
- [Independent review and correction confirmation](plugins/astra-advisor/skills/orchestration/references/review.md)
- [Usage and cost receipts, when requested](plugins/astra-advisor/skills/orchestration/references/cost-receipts.md)

Ordinary delegation and review do not load the cost receipt procedure.
