# Independent review

The public spawn and thread metadata are authoritative for model and effort. Use
runtime introspection only to resolve a field that public metadata omitted, and report
the source of each value. Chosen values are not the same as runtime-confirmed values.

## Acceptance review

For an initial substantial implementation, the parent inspects the integrated result
and ensures the requested checks have run, using direct or delegated execution as
appropriate. Start an independent read-only acceptance reviewer in a full
parent-context fork under [operations](operations.md), subject to its routing and
capability rules. Keep the reviewed artifact stable. Even with inherited context,
give a short assignment naming the exact accumulated diff, accepted scope, interfaces,
constraints, and verification evidence, including any technical review results.

The acceptance reviewer checks whether the delivered behavior answers the user's
need across the conversation, including corrections, constraints, and accepted
tradeoffs that a technical brief may omit. It inspects the complete diff and relevant
code and evidence for missing behavior, scope drift, and integration gaps. It must
distinguish user requirements from orchestrator assumptions and verify conclusions
against the artifact. Inherited history explains choices; it does not prove them
correct. This review informs the parent's final acceptance decision.

## Technical review

Delegate bounded code review when it adds useful independent evidence. Prefer a
less costly suitable model under the existing routing rules, with only the relevant
context and an explicit technical scope: correctness, regressions, security, or test
coverage as applicable. Use the requested or applicable code-review skill within
that assignment; orchestration retains dispatch and acceptance. A technical `ship`
applies only to its named scope and does not replace acceptance review. The acceptance
reviewer can also cover technical concerns when a separate delegate adds no value;
these purposes do not impose a fixed agent count or duplicate review of the same work.

## Verdict and corrections

Ask each reviewer to return a concise verdict with source locators for its evidence:

~~~text
ASTRA REVIEW
SCOPE: acceptance | technical (<named scope>)
VERDICT: ship | fix-first | rethink
REASON: <evidence-based reason>
FINDINGS: <precise findings or none>
RESIDUAL RISK: <remaining risk or none>
~~~

Acceptance review requires `ship` for substantial implementation; it may include
residual findings. Resolve demonstrated blockers from either review before acceptance.
Give every reviewer the accepted scope and this threshold:
`fix-first` requires a demonstrated in-scope blocking defect grounded in the user's
requirement or an existing supported contract. Non-blocking P2 and P3 findings alone
never start another correction or review cycle.

The parent uses the verdicts and evidence to decide acceptance, requesting targeted
source reads or follow-ups where needed. Keep bulk code inspection and logs in the
review agents rather than routinely loading them again in the parent.

Batch blocking findings for parent-owned correction. After a bounded correction, inspect
the delta, run affected checks, and request targeted confirmation, preferably from
the same reviewer via `collaboration.followup_task` when available. Preserve
unaffected evidence. Start a new full acceptance review
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
