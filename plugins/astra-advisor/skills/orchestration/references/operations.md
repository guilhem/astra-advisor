# Astra Advisor operations

This reference holds the operational details behind the short orchestration skill.
It describes capability selection and evidence rules; it does not define installed
roles, role files, task lanes, or an installer.

## Parent session

The primary session uses the model and effort selected by the user. Do not require
Astra, rewrite the parent configuration, or claim a model/effort pin without runtime
evidence. If metadata does not expose the model or effort, report the value as
unobservable and continue within the user's request without inventing confirmation.

## Dynamic native delegation

Use the generic `collaboration.spawn_agent` only if the current environment exposes
that tool and its schema. Select a model and effort for each concrete, bounded,
independent deliverable from the task's risk, context, and available work. Delegate
only if that result justifies briefing, waiting, and integration costs; multi-file
inspection alone does not. Work directly otherwise, while preserving independent
review for substantial implementation. Apply the user's instructions and applicable
`AGENTS.md` preferences before the [optional routing defaults](routing-defaults.md).

For substantial reviews, prefer `fork_turns: "all"` to retain the discussed needs,
constraints, and accepted tradeoffs. Under the current schema, full forks inherit
the parent's model and effort and do not accept overrides; omit `model` and
`reasoning_effort`. Explicit user and applicable `AGENTS.md` routing instructions
take precedence over this default. If they require different settings, use a
compatible reduced-context fork with explicit model and effort and supply the
relevant requirements and evidence. Never use inheritance to bypass a restriction.
When reporting settings, distinguish requested inheritance from runtime evidence.

Narrowly targeted checks may use reduced context when sufficient. For other bounded
delegates, pass the chosen values explicitly:

~~~text
model: <selected supported model>
reasoning_effort: <selected supported effort>
fork_turns: none
~~~

Keep the message to the objective, scope, constraints, expected result, and success
criterion, with only the context needed to act. Writing agents need explicit file
ownership; exploration and review are read-only. For example, the model and effort
below are illustrative and must be selected afresh for the actual task:

~~~json
{
  "task_name": "inspect_auth_boundary",
  "message": "Trace authentication in src/auth/ and its route callers. Read-only; stay within the existing auth contract. Return the enforcement path, file references, and any bypass evidence. Success: each caller is accounted for, with verified checks distinguished from untested risks.",
  "model": "gpt-5.6-luna",
  "reasoning_effort": "max",
  "fork_turns": "none"
}
~~~

The example does not prescribe a model, effort, task name, or number of subagents.
Use the current tool schema for any additional required fields and reject a request
whose selected controls cannot be enforced.

No predefined roles or installer are needed. User preferences may assign models to
task types or limit concurrency, within the live tool contract. Dispatch only work
whose files, interfaces, and acceptance evidence are clear;
keep useful planning, implementation, integration, or verification work in the
parent session while independent subagents run. Avoid assigning the same change or
check to both parent and subagent. Preserve concurrent edits and return each
subagent's actual result and evidence to the parent.

Inspect the current tool metadata when selecting and invoking a subagent; the plugin
does not maintain a capability allowlist. If the selected model, effort, explicit
spawn control, or required tool is unavailable, conflicting, or unobservable, fail
the affected delegation closed. Continue safe parent work when possible and report
the limitation; never silently substitute another model, effort, or tool.

## Evidence and review

The public spawn and thread metadata are authoritative for model and effort. Use
runtime introspection only to resolve a field that public metadata omitted, and report
the source of each value. Chosen values are not the same as runtime-confirmed values.

For an initial substantial implementation, the parent first inspects the complete
accumulated diff and runs the requested checks. It then starts an independent
read-only reviewer, preferably with a full fork as described above, keeping the
reviewed artifact stable. Even with inherited context, give a short assignment
naming the exact diff, accepted scope, interfaces, constraints, and verification
evidence. The reviewer must verify the parent's conclusions against the actual code
and distinguish user requirements from orchestrator assumptions. Conversation
history explains the choices; it does not establish their correctness. Ask it to return:

~~~text
ASTRA REVIEW
VERDICT: ship | fix-first | rethink
REASON: <evidence-based reason>
FINDINGS: <precise findings or none>
RESIDUAL RISK: <remaining risk or none>
~~~

Treat `ship` as the only accepting verdict for substantial implementation; it may
include residual findings. Give every reviewer the accepted scope and this threshold:
`fix-first` requires a demonstrated in-scope blocking defect grounded in the user's
requirement or an existing supported contract. Non-blocking P2 and P3 findings alone
never start another correction or review cycle.

Batch blocking findings for parent correction. After a bounded correction, inspect
the delta, run affected checks, and request targeted confirmation, preferably from
the same reviewer via `collaboration.followup_task` when available. Preserve
unaffected evidence. Start a new full independent review
when design, authority, data ownership, or material risk changes, not simply because
the original implementation was substantial. On `rethink`, reassess the plan and
scope before claiming completion. Reviewers must not edit files or implement their
own fixes. Capture actual sandbox and permission metadata when exposed; do not
claim enforced read-only isolation unless observed. Small documentation and
mechanical changes need parent inspection, not an independent review gate.

For instruction changes, separate static consistency checks and scenario walkthroughs
from actual agent execution. A wording or link test does not establish behavior.
Report which affected scenarios were executed and which were only inspected;
do not invent runtime evidence.

## ChatGPT app and cloud boundaries

Native Codex subagents in the ChatGPT app are usable when the exposed tool schema
provides the needed controls. Separate app tasks require an explicit user request.
For an explicit Codex app project task, `mcp__codex_app__create_thread` supports
`model` and `thinking`; call `mcp__codex_app__list_projects` first, use a worktree by
default when the selected project is a Git repository, and use local otherwise.
Follow any explicit starting-state request exactly.

ChatGPT Work cloud `create_thread` does not accept `model` or `thinking`; omit both.
Cloud work therefore cannot currently promise arbitrary model or effort control. Do
not dispatch an incompatible model-pinned request there by default, and do not use an
API key, nested CLI, or fabricated tool as a workaround. A future native work tool is
usable only once its schema exposes the required controls.

## Reporting

Report meaningful decisions, results, changes, and blockers. Group related delegation
updates rather than emitting a route block or paired dispatch/completion receipts
for every agent. Provide agent IDs, selected model/effort, runtime evidence, and
lifecycle detail when requested. Keep requested settings separate from confirmed
settings; disclose observed mismatches and material capability limitations promptly.
A successful dispatch is not completed work. Parent acceptance requires its own
diff inspection and requested checks, not a subagent's assertion alone.

At completion, focus on the outcome, verification, and residual risk. No cost receipt
or unavailable-cost notice is required unless the user asks for one. Reuse existing
native traces when a receipt is requested; do not add continuous collection,
external inference CLIs, billing-account queries, or a dashboard to support it.

## API-equivalent receipt policy

When the user requests usage or cost details, use the existing Python standard
library calculator for API price estimates:
[calculator](../../../scripts/cost_receipt.py),
[pricing snapshot](../../../pricing/2026-09-04.json).
Resolve these paths relative to this installed reference, not a guessed cache version.
If no observed usage is accessible, report why it is unavailable; a fabricated input
or calculator run is unnecessary. Keep observed consumption, estimated API prices,
and demonstrated savings distinct. A savings claim needs comparable observed runs,
including coordination and corrections, with their scope, quality, and cost basis;
same-token repricing alone does not establish it.

Routing may use models absent from the pricing snapshot. Missing rates make the
affected estimate unavailable, not the model ineligible for delegation. The bundled
calculator's comparison baseline remains Astra regardless of the selected parent.

Use only non-overlapping observed usage with an explicit source. Cumulative telemetry
snapshots are not additive calls. Never sum a parent-inclusive aggregate with child
totals. Do not turn message lengths into claimed observed usage. Missing usage or
rates must remain unavailable, and partial coverage must state which work is missing.
Whole-task coverage requires every parent and subagent call, including failed attempts,
review, corrections, and final parent work. If the final response's tokens cannot yet
be observed, identify the receipt's cutoff and do not claim whole-task completeness.

Cached input is a subset of total input. Output already contains reasoning tokens;
never add them a second time. Explicit per-call standard short-context eligibility
is required; unknown or unsupported long-context, service-tier, or cache-write pricing
must not silently inherit standard rates. Effort is recorded without a rate multiplier.

The snapshot records USD per million tokens and official source URLs, with a
2026-09-04 verification date supplied by the recording coordinator. It is a historical
snapshot, not a live-price guarantee; Sol rates are promotional. Disclose the snapshot
date and freshness when showing an estimate. Use a newly verified versioned snapshot
if current prices are required. Do not silently change historical receipts.

~~~text
API-EQUIVALENT COST RECEIPT
usage: <observed source and cutoff, partial, or unavailable with reason>
scope: <whole task only if complete; delegated-only or observed subset otherwise>
pricing: <snapshot date; historical USD estimate; Sol promotional if applicable>
routed: <USD estimate or unavailable>
same-token Astra repricing: <USD or unavailable>
same-token API price difference: <USD and percentage where valid, or unavailable>
limits: This is not a measured all-Astra counterfactual, actual net task savings,
        or a change in ChatGPT subscription charges or usage credits.
~~~

When no subagents ran, state `no delegation savings`. When no usage is exposed,
state `unavailable: native tools did not expose observed token usage`; never show
zero cost. Keep any illustrative fixture result visibly separate from live usage.

## Calculator input and execution

Run `python3 cost_receipt.py INPUT.json [--pricing PATH]` using the installed
calculator path above. It emits a JSON receipt; exit 0 includes calculated, partial,
and unavailable outcomes, while invalid input or pricing exits 2. Inspect the
receipt status instead of treating exit 0 as proof of complete usage.

The version 1 input contains:

- `schema_version: 1`, `task_id`, and `coverage` with `scope` (`whole_task` or
  `delegated_only`), `agent_roster_complete`, and `final_parent_usage_cutoff` booleans.
- `agents`: unique `agent_id`, `role` (`parent`, `delegate`, or `reviewer`), and
  `calls_complete`. Declare missing agents rather than omitting them to improve coverage.
- `calls`: globally unique `call_id`, declared `agent_id`, `model`, optional `effort`,
  and `aggregation: "atomic"`. Supply `usage.kind`, a non-empty `usage.source`, and
  `input_tokens`, `cached_input_tokens`, and `output_tokens` when known. Optional
  `reasoning_tokens` is already included in output. Missing values stay unknown.
- Each call also declares `context: "standard"` and `service_tier: "standard"`, with
  `context_source` and `service_tier_source` set to `observed` or `assumed`. If runtime
  tier metadata is null, a clearly disclosed standard-price scenario is permitted;
  never relabel that assumption as observed billing. Known nonstandard regimes
  are unsupported. Do not assume a workload eligible when evidence contradicts it.

See the [illustrative input](../../../examples/illustrative-usage.json) for an
executable fixture, distinct from observed task usage. Receipts preserve assumptions,
usage provenance, and per-agent coverage. Delegated-only scope includes reviewers;
whole-task scope needs an authoritative complete roster, complete calls for each
agent, a parent, and final parent usage. Solo work does not require an invented
reviewer. False completeness flags keep the result partial or unavailable.

For cumulative native telemetry, retain each snapshot as source evidence, skip exact
repeats, and derive atomic records only when the cumulative delta matches the
reported last-call usage for every token field. If events are missing, counters reset,
or aggregate ownership is unclear, mark that coverage unavailable rather than
inventing calls. Keep preparation-turn usage separate from the implementation turn
when that is the declared task scope.

The bundled calculator conservatively caps each call at 128,000 input tokens. This
is an implementation support boundary, not an official model pricing threshold.
Missing cache counts remain unknown; provide an explicit zero only when supported
by the usage source. Unknown usage fields are rejected to avoid ignoring cache writes.
