# Independent review

The public spawn and thread metadata are authoritative for model and effort. Use
runtime introspection only to resolve a field that public metadata omitted, and report
the source of each value. Chosen values are not the same as runtime-confirmed values.

For an initial substantial implementation, the parent first inspects the complete
accumulated diff and runs the requested checks. It then starts an independent
read-only reviewer, preferably with a full fork under [operations](operations.md), keeping the
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
