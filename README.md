# Astra Advisor

**GPT-6 Astra plans the work, chooses useful bounded delegation dynamically, and
owns verification and acceptance.**

Astra Advisor is a Codex plugin for capability-routed software delivery. Give Astra
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
enabled. Start a fresh task after installation and select GPT-6 Astra at any effort
supported by the current Codex host:

~~~sh
codex plugin marketplace add DannyMac180/astra-advisor --ref main
codex plugin add astra-advisor@astra-advisor
~~~

Start a task with:

~~~text
Use $astra-advisor:orchestration to plan, build, verify, and review this work.
~~~

## How routing works

Astra remains the architect and acceptance owner in the primary GPT-6 Astra session
at the effort selected by the user. The skill never changes the parent session or
claims runtime settings without evidence.

Delegate only when an independent result justifies briefing, waiting, and integration
costs. Inspecting several files alone is not a trigger. When delegation helps, Astra
uses the exposed generic `collaboration.spawn_agent` tool with an explicit `model`,
`reasoning_effort`, and `fork_turns: none`. It prefers `gpt-6-astra` for substantial
judgment and `gpt-5.6-luna` for bounded, less demanding work, including reviews.
Sol or Terra require an explicit user request or a concrete task-specific advantage.
Effort is chosen for the difficulty and expected cost per accepted result, including
retries; user choices and live capabilities take precedence.
There are no predefined role TOMLs, companion
installer, role-to-model mapping, or fixed subagent count cap. Astra gives each
subagent a short contract: objective, scope, constraints, expected result, and success
criterion, plus explicit file ownership when writing. Astra continues useful parent
work while it runs and owns integration.

Live tool metadata is authoritative. The current documented effort snapshot is:

| Model | Known efforts |
| --- | --- |
| `gpt-6-astra` | `low`, `medium`, `high`, `xhigh`, `max`, `ultra` |
| `gpt-5.6-sol` | `low`, `medium`, `high`, `xhigh`, `max`, `ultra` |
| `gpt-5.6-terra` | `low`, `medium`, `high`, `xhigh`, `max`, `ultra` |
| `gpt-5.6-luna` | `low`, `medium`, `high`, `xhigh`, `max` |

If a selected model, effort, control, or tool is unavailable, conflicting, or
unobservable, Astra fails that delegation closed and reports the limitation. It does
not silently substitute a model, effort, role, or fabricated tool. Chosen values and
runtime-confirmed values are reported separately.

For an initial substantial implementation, Astra inspects the complete diff and runs
the requested checks, then sends the stable change set to an independent read-only
reviewer in a fresh context. The reviewer can be any of the supported models at a
live-supported effort. Acceptance requires `ship`, which may include residual
findings. `fix-first` requires a demonstrated in-scope blocking defect; non-blocking
findings alone do not start another correction or review cycle.

After a bounded correction, Astra inspects the delta, runs affected checks, and
obtains targeted confirmation, which may reuse the same reviewer. Unaffected evidence
remains valid. Changes to design, authority, data ownership, or material risk require
a new full independent review. `rethink` requires reassessing the plan and scope.

## Delegation advisory hook (0.3.0)

The bundled [hook](plugins/astra-advisor/hooks/hooks.json) checks explicit delegation
controls before `spawn_agent` calls. Missing or empty `model` / `reasoning_effort`,
or `fork_turns` other than `"none"`, produces a short advisory in the parent's
context. Complete calls are silent. It does not block, rewrite, or retry calls,
enforce routing preferences, or establish runtime model/effort evidence.

This requires Python 3 and a Codex host supporting plugin hooks. After installing
or updating, review and trust the hook in Codex; installing the plugin alone does
not activate it. Trusted hooks run even when the orchestration skill is not invoked,
so other delegation workflows may receive the advisory too. See the
[official hook documentation](https://learn.chatgpt.com/docs/hooks).

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
Its input lists agents and unique atomic calls, usage provenance, coverage assertions,
and explicit pricing eligibility. It validates cached-input and reasoning-output
subsets, refuses overlapping aggregates, and keeps unknown usage separate from zero.
See the [operations reference](plugins/astra-advisor/skills/orchestration/references/operations.md)
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

For operational details, read
[the orchestration operations reference](plugins/astra-advisor/skills/orchestration/references/operations.md).
