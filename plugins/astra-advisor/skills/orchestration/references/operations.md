# Native delegation and app tasks

Use this reference before dispatch. Squire missions and lifecycle live in
[squire](squire.md). Review criteria live in [review](review.md);
requested usage and cost analysis lives in [cost receipts](cost-receipts.md).
Read those references only for the operation concerned.

## Native delegation

Use the native `spawn_agent` tool exposed by the host. Choose among live
capabilities using the user's instructions, applicable `AGENTS.md`, and optional
[routing defaults](routing-defaults.md).

The parent launches acceptance review directly. Use the richest compatible parent
context supported by the live spawn schema to retain discussed needs, constraints,
and accepted tradeoffs. If that context inherits incompatible model or effort
settings, use a compatible reduced-context spawn with explicit settings and supply
the requirements and evidence. Never use inheritance to bypass a restriction.
Bounded technical reviews receive relevant requirements, interfaces, and evidence,
with explicit model and effort. Review purpose and criteria live in
[review](review.md).

For other bounded delegates, pass the selected controls explicitly:

~~~text
model: <selected supported model>
reasoning_effort: <selected supported effort>
fork_context: <live-supported reduced context setting>
~~~

The live schema is authoritative: this runtime's spawn exposes `fork_context`, not
`fork_turns`, and follow-up schemas do not expose model or effort controls. Check
the actual exposed tools before dispatch, including nested tools; a configured
depth alone does not establish nested delegation. If a required tool, model, effort,
or control is missing, conflicting, unavailable, or cannot be established, do not
dispatch that assignment. For an unavailable nested spawn, the delegate can give the parent a
ready brief for native coordination. Explain the limitation and continue permitted
work. Never silently substitute a model, effort, role, or fabricated tool. Do not
infer available models from pricing snapshots. Introspection can clarify omitted runtime metadata,
but cannot override the public tool contract.

Give each agent a short contract: objective, scope, constraints, ownership, expected
result, and success criterion. Include the relevant context and prior decisions;
forward routing constraints if further delegation is permitted. Writing agents need explicit
file ownership and must preserve concurrent edits. Exploration and review stay
read-only. The squire may dispatch workers only within an authorized mission; an
information request does not authorize implementation. Sequence dependent or
overlapping work and preserve ownership. No fixed worker count is required.

Add known, mission-specific points of attention: relevant pitfalls, constraints to
preserve, and conditions that need the parent's decision. Do not invent a checklist
or solve every local uncertainty before dispatch. State whether direct read-only
advice is permitted and pass the applicable model and effort constraints; deciding
this within the authorized scope does not require another user approval.
When permitting direct advice, include the Optional advice contract below in the
delegate's brief: read-only advice, no execution handoff or further delegation,
parent-reserved decisions, routing/capability constraints, and the unavailable-tool
fallback. Do not rely on inherited history, access to this reference, or hook
injection to convey that contract.

A successful dispatch is not completed work. Assess results and validation evidence
before integration or acceptance. Report consequential selection choices and outcomes;
agent IDs and lifecycle details are available on request. Keep requested settings
distinct from runtime-recorded settings; role names and self-identification do not
confirm a model. The parent corrects observed mismatches. Disclose unobservable
metadata; do not claim enforced read-only isolation without supporting evidence.

## Optional advice

Consultation is optional and does not depend on the reminder hook. Leaving that
hook untrusted, disabling it, or removing it only removes the reminder; it adds no
consultation requirement or delegation permission.

- Ask the parent when the answer depends on project history, product intent, scope,
  ownership, or authorization. Preserve the parent's decision and acceptance role.
- For an isolated technical question, a delegate whose assignment permits it may
  consult a native read-only advisor directly. Check live tools and schemas, then
  use explicit model and effort with a compatible reduced-context spawn. Send only
  the question, evidence, attempts, recommendation, and relevant constraints. An advisor
  returns advice and uncertainty; it must not edit, take over the mission, or delegate
  again or compensate for a routing mismatch by delegating. Advice does not replace
  independent review or authorize scope changes.
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
