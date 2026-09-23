# Retained squire

The parent keeps the user conversation, intent, architecture, approach, scope,
arbitration, correction decisions, integration, verification, and acceptance. The
squire is the parent's retained interface for information acquisition and routine
operational execution. It does not make parent-reserved decisions, expand scope, or
accept its own work. This boundary applies to the parent: the squire and its workers
use tools for their assigned missions without each creating another squire.

## Mission and return

Spawn the squire on first need with an autonomous brief and explicit supported model
and effort. Include the goal, known decisions, scope, authorization, constraints,
ownership, expected evidence, stopping condition, and decisions reserved to the
parent. Subsequent `send_input` messages give the next related goal and changed
context without replaying the conversation. Group the steps needed to answer one
question into a mission. The squire chooses tools, sources, order, and useful
parallelism within that mandate; it need not seek approval for each command. An
information request does not authorize a write. Writing workers receive explicit
file ownership and must preserve concurrent changes.

Return a usable answer per mission or consequential change, with facts and source
locators, inferences, uncertainty, contradictory evidence, limits, actions and
checks actually completed, and decisions needed from the parent. Date or identify
the revision of evidence that can change. Start with a concise synthesis and the
excerpts needed for the decision. Give full detail when requested or needed to
explain ambiguity; preserve consequential expert and reviewer reports in their
original wording, including dissent and caveats. Reuse source logs, diffs, and
reports; make a local appendix only when volume warrants it. Agent memory alone
does not preserve an exhaustive report through compaction or replacement. Mark
reused evidence separately from a fresh check.

If a finding invalidates the approach, report its evidence and consequences for
the parent's decision. The squire may recommend an option; it cannot authorize a
new scope. The parent launches any required independent acceptance reviewer, which
can inspect the artifact and original evidence. The squire may collect review
results but never substitutes for that reviewer or the parent's acceptance.

## Reuse, handoff, and capacity

Keep the squire open and reuse `send_input` for related research, monitoring, checks,
and follow-ups. A new user message or short lookup is not a reason to spawn again.
Replace it when a durable topic or repository change, unavailability, observed
model drift, or confused context makes continuity unhelpful. Give its successor the
still-valid decisions, useful evidence, pending work, and current ownership. Ask
the outgoing squire for a scoped full report when needed.

Before closing or replacing it, collect and finish descendant work, or cancel it
when authorized; closing an agent also closes its descendants. Do not retry an
action while its outcome is still running or uncertain. Close finished workers that
are no longer useful. The retained squire itself uses native agent capacity; close
it when no related continuation is expected or at the end of the conversation.

Use live native tool schemas for spawn, follow-up, wait, resume, and close. In the
runtime observed for this plan, spawn uses `fork_context`, while `send_input` and
`resume_agent` expose no model or effort controls. A configured depth is not proof
that nested delegation works. If the squire cannot spawn an appropriate worker or
advisor, it sends a ready brief to the parent; the parent performs that native
coordination action and relays the useful result. If no suitable delegate is
available, report the unperformed acquisition and continue independent authorized
work.

Keep requested model and effort distinct from recorded runtime settings. A role
name or agent self-description is not proof. Check exposed metadata at the first
follow-up in an unvalidated environment and after a configuration-changing event;
reuse that evidence while conditions remain stable. If a mismatch is observed, the
parent corrects dispatch. If metadata is unavailable, report that limit rather
than claiming confirmation. For a model-pinned agent closed in this runtime, use
a new explicit spawn with a resumption brief; do not rely on `resume_agent` to
preserve its settings.

One case observed on September 23, 2026 in Codex 0.156.1: an agent originally
recorded as `anthropic/claude-opus-5-5` / `high` ran a later turn as
`gpt-6-astra` / `max` after close, resume, and `send_input`. Two follow-ups without
closure retained Opus/high and Luna/max respectively. This is a dated observation,
not a general guarantee across hosts or resumes.
