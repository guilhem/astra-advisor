# Native delegation and app tasks

Use this reference before dispatch. Review criteria live in [review](review.md);
requested usage and cost analysis lives in [cost receipts](cost-receipts.md).
Read those references only for the operation concerned.

## Native delegation

Use `collaboration.spawn_agent` only when the host exposes it. Choose among live
capabilities using the user's instructions, applicable `AGENTS.md`, and optional
[routing defaults](routing-defaults.md).

For substantial reviews, prefer `fork_turns: "all"` to retain discussed needs,
constraints, and accepted tradeoffs. Full forks inherit the parent's model and
effort; omit `model` and `reasoning_effort`. Explicit user and applicable
`AGENTS.md` routing instructions take precedence. When different settings are
required, use a compatible reduced-context fork with explicit model and effort,
and supply the relevant requirements and evidence. Never use inheritance to bypass
a restriction. Targeted checks may use reduced context when sufficient.

For other bounded delegates, pass the selected controls explicitly:

~~~text
model: <selected supported model>
reasoning_effort: <selected supported effort>
fork_turns: none
~~~

The live schema is authoritative. If a required tool, model, effort, or control is
missing, conflicting, unavailable, or cannot be established, do not dispatch that
assignment. Explain the limitation and continue permitted parent work. Never
silently substitute a model, effort, role, or fabricated tool. Do not infer available
models from pricing snapshots. Introspection can clarify omitted runtime metadata,
but cannot override the public tool contract.

Give each agent a short contract: objective, scope, constraints, expected result,
and success criterion. Include the relevant context and prior decisions; forward
routing constraints if further delegation is permitted. Writing agents need explicit
file ownership and must preserve concurrent edits. Exploration and review stay
read-only. Sequence dependent or overlapping work; avoid duplicating the parent's
implementation or verification. No fixed roles or agent count are required.

A successful dispatch is not completed work. Inspect results and validation evidence
before integration or acceptance. Report consequential selection choices and outcomes;
agent IDs and lifecycle details are available on request. Keep requested settings
distinct from runtime-observed settings. Disclose unobservable metadata and observed
mismatches; do not claim enforced read-only isolation without supporting evidence.

## Separately requested app tasks

Create a separate app task only when the user explicitly requests one; ordinary
subtasks use native delegation. Discover the available task tools and their current
schemas. For project targets, list projects first and follow the requested starting
state. Prefer a native Git worktree for a Git project within effective permissions.

Pass model and effort controls only when that host's schema supports them. Cloud
tools without those controls cannot satisfy a pinned request. Report that limitation
rather than silently substituting settings or using an API key, nested CLI, or
invented tool as a workaround. A future tool is usable only when its schema supports
the required controls.
