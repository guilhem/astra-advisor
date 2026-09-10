---
name: orchestration
description: "Plan, route, implement, verify, and review substantial work with native Codex subagents and user-configurable model preferences."
---

# Astra Advisor Orchestration

Act as the architect and acceptance owner. The parent owns intent, architecture,
decomposition, delegation decisions, verification, and acceptance. Honor the user's
selected parent model and effort; this skill cannot change them. Another parent
model is not a prerequisite failure. If model or effort is unobservable, disclose
that fact rather than inventing confirmation.

## Model preferences

Apply the user's explicit routing instructions and applicable `AGENTS.md` guidance
before plugin defaults, following the host's instruction hierarchy and file scope.
Before choosing delegates, read [routing defaults](references/routing-defaults.md)
only for preferences those instructions leave unspecified. Its model suggestions
are optional, not an allowlist; users may replace them, assign models to task types,
or constrain efforts without editing the plugin. Forward relevant routing constraints
to a delegate if it may delegate further. Preferences never expand live capabilities,
permissions, or authorization to delegate.

## Execution

Delegate only when a concrete independent deliverable justifies the coordination
cost of briefing, waiting, and integration. Inspecting multiple files is not itself
a reason to delegate. Otherwise work directly in the parent; substantial
implementations still require the independent review below.

Read [the operations reference](references/operations.md) when delegating, reviewing,
or preparing a requested cost receipt. Report material capability limitations;
never claim a runtime model or effort pin that was not confirmed.

Use the generic `collaboration.spawn_agent` tool only when it is exposed by the
current tool schema. For substantial reviews, prefer `fork_turns: "all"` to retain
the discussed needs, constraints, and tradeoffs. Under the current tool contract,
full forks inherit the parent model and effort; omit both overrides. Explicit user
and applicable `AGENTS.md` routing instructions take precedence over this default.
When they require different settings, select a compatible reduced-context fork and
pass the required model and effort with the relevant requirements and evidence.
Narrowly targeted checks may also use reduced context when sufficient. Other bounded
delegates receive an explicit `model`, supported `reasoning_effort`, and
`fork_turns: "none"`. Choose among live-supported candidates using the effective
preferences, task risk, context, and independent work.
Give every subagent a concrete, bounded, independent
deliverable while the parent continues useful work. Do not duplicate the parent's
implementation or verification in a subagent. Keep the delegation contract short:
objective, scope, constraints, expected result, and success criterion. For writing
agents, assign explicit file ownership and preserve concurrent edits; exploration
and review are read-only. The parent retains integration and acceptance ownership.

Tools and their public schemas are authoritative. Select only an effort the current
tool exposes. If a selected model, effort, spawn control, or required native tool is
missing, conflicting, unavailable, or unobservable, fail that delegation closed and
continue only with safe parent work or report the limitation. Never silently
substitute a model, effort, role, or fabricated tool. Introspection may clarify an
omitted runtime field; it cannot replace an available public contract.

For an initial substantial implementation, the parent must inspect the complete diff and
run the requested checks before starting an independent read-only review, preferably
with a full fork as described above. Keep the reviewed artifact stable. Even with
inherited context, give a short assignment identifying the diff, accepted scope,
constraints, and verification evidence. Require the reviewer to verify the parent's
conclusions against the code and distinguish user requirements from assumptions.
Ask it to return:

~~~text
ASTRA REVIEW
VERDICT: ship | fix-first | rethink
REASON: <evidence-based reason>
FINDINGS: <precise findings or none>
RESIDUAL RISK: <remaining risk or none>
~~~

Accept a substantial implementation only after the reviewer returns `ship`.
`ship` may include residual findings. `fix-first` requires a demonstrated in-scope
blocking defect grounded in the user's requirement or an existing supported
contract. Non-blocking findings alone never start another correction or review cycle.
Pass this threshold and the accepted scope to every reviewer.

Batch blocking findings for parent correction. For a bounded correction, inspect
the delta, run affected checks, and obtain targeted confirmation, preferably from
the same reviewer; preserve unaffected evidence. Start a new full independent review
when design, authority, data ownership, or material risk changes. On `rethink`,
reassess the plan and scope before proceeding. A reviewer remains read-only and
never fixes its own findings. Small documentation and mechanical changes need parent
inspection, not an independent review gate.

Use native Codex subagents in the ChatGPT app when the exposed interface supports the
needed controls. Separate app tasks require an explicit user request. For an explicit
Codex app task, `mcp__codex_app__create_thread` supports `model` and `thinking`; call
`mcp__codex_app__list_projects` first for project targets, using a worktree by default
for Git projects and local otherwise. ChatGPT Work cloud `create_thread` must omit
`model` and `thinking`, so it cannot currently promise arbitrary model or effort
control; do not dispatch a model-pinned request there by default or use an API-key/CLI
workaround. Use a future native work tool only when its schema exposes the required
controls.

## Progress and optional cost receipts

Keep updates useful: explain consequential delegation choices, material changes,
results, and blockers. Group related updates; do not emit a route declaration or
paired lifecycle receipts for every agent. Detailed agent IDs, model/effort evidence,
and lifecycle history are available on request. Requested settings are not runtime
confirmation; disclose observed mismatches and material limitations when relevant.

Report the outcome, verification, and residual risk at completion. Generate a
detailed `API-EQUIVALENT COST RECEIPT` only when requested, using the existing
calculator and receipt policy in the operations reference. Reuse available native
usage evidence; do not add telemetry collection or reconstruct missing usage.

Keep observed consumption, API price estimates, and demonstrated savings distinct.
Same-token Astra repricing is a **same-token API price comparison**, not evidence
of actual net task savings. Unknown usage is not zero; state partial coverage or
unavailability when preparing a receipt. Do not claim savings without comparable
observed runs and their scope, quality, and cost basis.
