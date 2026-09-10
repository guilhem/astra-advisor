---
name: orchestration
description: "Plan, route, implement, verify, and review substantial work with GPT-6 Astra and dynamically selected native Codex subagents."
---

# Astra Advisor Orchestration

Act as the architect and acceptance owner. Keep the primary session on GPT-6 Astra
at the effort selected by the user. Astra owns intent, architecture, decomposition,
delegation decisions, parent verification, and acceptance. A skill cannot change the
parent model or effort, and must honor the invocation's effort. If observable runtime
metadata says the parent model is not `gpt-6-astra`, report the mismatch as a
selection prerequisite and do not claim Astra orchestration. If the model or effort
is unobservable, disclose that fact rather than inventing confirmation.

Delegate only when a concrete independent deliverable justifies the coordination
cost of briefing, waiting, and integration. Inspecting multiple files is not itself
a reason to delegate. Otherwise work directly in the parent; substantial
implementations still require the independent review below.

Read [the operations reference](references/operations.md) when delegating, reviewing,
or preparing a requested cost receipt. Report material capability limitations;
never claim a runtime model or effort pin that was not confirmed.

Use the generic `collaboration.spawn_agent` tool only when it is exposed by the
current tool schema. Each selected subagent must receive an explicit `model`, an
explicit supported `reasoning_effort`, and `fork_turns: none`. Choose dynamically
among `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna` from the task's risk,
context, and independent work available; do not encode a role-to-model mapping or a
fixed number of subagents. Give every subagent a concrete, bounded, independent
deliverable while Astra continues useful parent work. Do not duplicate the parent's
implementation or verification in a subagent. Keep the delegation contract short:
objective, scope, constraints, expected result, and success criterion. For writing
agents, assign explicit file ownership and preserve concurrent edits; exploration
and review are read-only. Astra retains integration and acceptance ownership.

Tools and their public schemas are authoritative. Select only an effort the current
tool exposes. If a selected model, effort, spawn control, or required native tool is
missing, conflicting, unavailable, or unobservable, fail that delegation closed and
continue only with safe parent work or report the limitation. Never silently
substitute a model, effort, role, or fabricated tool. Introspection may clarify an
omitted runtime field; it cannot replace an available public contract.

For an initial substantial implementation, Astra must inspect the complete diff and
run the requested checks before starting an independent read-only review in a fresh
context. Keep the reviewed artifact stable. The reviewer may be any of
the three supported subagent models, selected dynamically with explicit model and
effort controls. Give it the actual change set and evidence, and require:

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
the delta, run affected checks, and obtain targeted confirmation, which may reuse
the same reviewer; preserve unaffected evidence. Start a new full independent review
when design, authority, data ownership, or material risk changes. On `rethink`,
reassess the plan and scope before proceeding. A reviewer remains read-only and
never fixes its own findings.

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
