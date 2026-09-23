# Independent review

For initial substantial implementation, the parent launches an independent
read-only acceptance reviewer on the stable integrated diff. Give it the user's
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
Preserve unaffected evidence. Renew full review only when design, authority,
ownership, or material risk changes. `rethink` means reassess plan and scope.
Small documentation and mechanical edits need parent assessment.

For instruction changes, distinguish static checks and scenario walkthroughs from
actual agent execution; wording checks do not prove behavior.
