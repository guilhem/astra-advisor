# Independent review

For changes to behavior, supported contracts, or authority boundaries, or when
acceptance needs independent evidence, the parent launches an independent read-only
acceptance reviewer on the stable integrated diff. Give it the user's
need, accepted scope and tradeoffs, constraints, changed interfaces, and verification
evidence. It inspects the artifact and original evidence, rather than treating
inherited context or a worker report as proof. The squire does not replace this
reviewer. Bounded technical review is optional when it adds distinct evidence.

Ask reviewers for a concise `ship`, `fix-first`, or `rethink` verdict with source
locators, findings, and residual risk. Acceptance requires `ship`, which may include
residual findings. `fix-first` needs a demonstrated in-scope blocking defect against
the user requirement or a supported contract; non-blocking P2/P3 findings alone do
not start another correction cycle. The parent arbitrates and decides acceptance.
Reviewers do not implement their findings.

After a bounded correction, assess the delta from delegated evidence and affected
checks, then obtain targeted confirmation, preferably from the same reviewer.
Preserve unaffected evidence. Renew full review only when changed behavior,
contract, authority, or ownership falls outside the earlier review. `rethink`
means reassess plan and scope. Wording or presentation-only edits need parent
assessment and relevant checks; seek independent review if acceptance needs it.

For instruction changes, distinguish static checks and scenario walkthroughs from
actual agent execution; wording checks do not prove behavior.
