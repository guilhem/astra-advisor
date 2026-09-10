# Optional routing defaults

Use these suggestions only where the user's instructions and applicable `AGENTS.md`
leave a routing choice open. They are preferences, not requirements or a model
allowlist. Apply partial overrides to the choices they address; do not reintroduce
an excluded model through a default or a review assignment.

- Suggested parent when the user asks what to select: `gpt-6-astra`, at their chosen
  effort. Always work with the actual selected parent; do not require a switch.
- Suggested delegate candidates: `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`.
  Users can prefer other live-supported models, including Astra. No role has a
  mandatory model, and this list is not a ranking.
- Choose model and effort together for the task's difficulty, risk, and context.
  No fixed effort, numerical weight, or subagent count is prescribed. Consider the
  expected cost of a successful result, including retries, when cost matters.

First filter candidates by live capabilities and explicit user restrictions, then
apply preferences to the suitable candidates. Interpret "prefer" as a preference
and "only" or an explicit model pin as a restriction. If a preference cannot be met,
explain the choice of another permitted candidate before dispatch. If a required
model or effort is unavailable, report the limitation and continue independent
parent work; do not silently replace it. If no suitable permitted candidate remains,
do not delegate. Never treat a pricing snapshot as a runtime model catalog.

The same selection rules apply to implementers and reviewers. They do not relax
review, permission, or evidence requirements in the orchestration workflow.
