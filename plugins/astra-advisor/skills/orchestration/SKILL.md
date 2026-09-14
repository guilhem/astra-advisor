---
name: orchestration
description: "Plan, route, implement, verify, and review software work, including bounded tool tasks, with native Codex subagents and user-configurable model preferences."
---

# Astra Advisor Orchestration

The parent owns intent, architecture, integration, verification, and acceptance.
Honor the user's selected parent model and effort; this skill cannot change them
or require Astra. User instructions and applicable `AGENTS.md` take precedence
over plugin preferences, subject to the host's instruction hierarchy.

## Choose the work and model

Use tools directly to understand context, resolve ambiguity, and decide the next
step. Prefer delegation when a bounded action, observation, or lookup has a clear
goal and expected result; read [tool execution](references/tool-execution.md) for
that pattern. Choose by intent, not output size or tool count alone. Delegate only
when the result justifies briefing, waiting, and integration. Keep useful parent
work alongside an independent assignment; do not duplicate implementation or checks.

Use [routing defaults](references/routing-defaults.md) only for choices the user and
`AGENTS.md` leave open. Model suggestions are preferences, not an allowlist. The
live tool schema determines supported controls; never silently substitute a
required model or effort. Preferences do not grant execution permissions.

## Load the procedure needed

- Before native delegation, read [operations](references/operations.md) for the
  assignment and capability contract. This includes requested app-task boundaries.
- For initial substantial implementation, inspect the integrated result and check
  evidence, and obtain independent acceptance review in a parent-context fork under
  [review](references/review.md). Delegate bounded technical review when useful.
  Acceptance requires `ship`; the parent retains the final decision. Small mechanical
  edits and documentation corrections need parent inspection, not an independent gate.
- For bounded corrections, use the same review reference for affected checks and
  targeted confirmation; preserve unaffected evidence and reuse the reviewer when
  appropriate. Renew full review only for changed design, authority, ownership, or
  material risk. Reviewers do not implement their own findings.
- For explicitly requested usage or cost details, read
  [cost receipts](references/cost-receipts.md). Ordinary delegation and review do not
  need that reference or a cost report.

## Finish the authorized work

Continue through relevant verification, in-scope blocking corrections, and requested
delivery; internal review is not a request for user approval. Ask only for missing
essential information, a material scope decision, or additional authorization.
Report limitations and continue independent permitted work when a capability is
unavailable. Never claim a required check or review passed without evidence.

Report the outcome, verification, and residual risk. Keep progress focused on
consequential choices, changes, results, and blockers; provide detailed agent or
usage receipts only on request. Requested settings are not runtime confirmation;
disclose observed mismatches and material limitations without inventing evidence.
