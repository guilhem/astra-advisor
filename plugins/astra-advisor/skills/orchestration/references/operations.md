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

Add known, mission-specific points of attention: relevant pitfalls, constraints to
preserve, and conditions that need the parent's decision. Do not invent a checklist
or solve every local uncertainty before dispatch. State whether direct read-only
advice is permitted and pass the applicable model and effort constraints; deciding
this within the authorized scope does not require another user approval.

A successful dispatch is not completed work. Inspect results and validation evidence
before integration or acceptance. Report consequential selection choices and outcomes;
agent IDs and lifecycle details are available on request. Keep requested settings
distinct from runtime-observed settings. Disclose unobservable metadata and observed
mismatches; do not claim enforced read-only isolation without supporting evidence.

## Optional advice

Consultation is optional and does not depend on the reminder hook. Leaving that
hook untrusted, disabling it, or removing it only removes the reminder; it adds no
consultation requirement or delegation permission.

- Ask the parent when the answer depends on project history, product intent, scope,
  ownership, or authorization. Preserve the parent's decision and acceptance role.
- For an isolated technical question, a delegate whose assignment permits it may
  consult a native read-only advisor directly. Use the capability and routing rules
  above, with explicit model and effort and `fork_turns: "none"`. Send only the
  question, evidence, attempts, recommendation, and relevant constraints. An advisor
  returns advice and uncertainty; it must not edit, take over the mission, or delegate
  again. Advice does not replace independent review or authorize scope changes.
- Reuse an available advisor for follow-ups on the same question when its context
  and settings remain suitable. Include useful advice and its evidence in the
  delegate's result for the parent. Continue independent work while awaiting advice.

Choose the route by the context needed and expected total work: briefing,
reasoning, tools, and integration. A new advisor with a short brief may avoid a
large parent context, while the parent may already know the answer. Neither route
is inherently cheaper; do not assume cache hits or measured savings. Routine
choices need no consultation. Repeated dependence on advice calls for reassessing
the brief or model, not an automatic chain of advisors.

If direct advice is prohibited or unavailable, use native parent messaging. If
that is also unavailable, report the unresolved point through the normal result;
do not guess on a blocked decision or use an external-call workaround. An agent
assigned only to advise returns its uncertainty instead of consulting another agent.

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
