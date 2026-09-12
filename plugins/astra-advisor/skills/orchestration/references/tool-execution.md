# Tool execution tasks

Use this pattern for a bounded mission whose useful result can be specified before
execution. The parent retains decisions, authorization, and acceptance. This is
delegation guidance, not interception of every tool call.

## Choose the boundary

| Work | Route |
| --- | --- |
| Read a function or configuration to understand it and decide what to do next | Direct |
| Resolve an ambiguity in a delegate's evidence | Direct, or ask that delegate for a targeted follow-up |
| Inspect a deployment's logs and identify relevant failures | Delegate |
| Check a defined hypothesis or find whether a condition holds within a specified scope | Delegate |
| Execute an authorized command and verify its effect | Delegate |

Apply the skill's proportionality and host capability rules. Do not turn every
small lookup into a new agent, or read an entire dataset in the parent before
delegating its analysis. Group related commands into one mission. Use an existing
delegate for follow-ups on the same mission when its context remains relevant.

## Brief and execute

Use the assignment and capability contract in [operations](operations.md). Prefer
`gpt-5.6-luna` for straightforward execution and collection, subject to the existing
[routing rules](routing-defaults.md); choose effort for the task. More demanding
judgment uses those same routing rules, not a mandatory escalation sequence.

Supply only the relevant context with `fork_turns: "none"`. Include the goal,
target or working directory, optional commands, permitted effects, constraints,
and expected result. Honor explicitly required commands; otherwise the delegate
chooses suitable available tools within scope. Do not expand an inspection into
a repair or treat a supplied command as permission to exceed the authorized scope.

The assigned executor uses tools directly and does not delegate this mission
again. It reports missing access or capability through the normal result. Group
dependent steps in order and preserve the existing ownership rules for writes.
After an uncertain modifying outcome, inspect the state before retrying; if the
outcome cannot be established, report it rather than blindly repeating the action.

## Return the useful result

Return a concise answer to the goal, supporting evidence, actions actually taken,
and any errors or limits. Include relevant exit status, exact excerpts, and source
locators such as file lines, run IDs, or query scope as appropriate. Keep verbose
output out of the main thread unless requested; retain retrievable source or
artifact references for details, without exposing secrets.

Distinguish observed facts from interpretation and incomplete work. No match in
a partial search is not proof of absence; a failed command is not successful work.
The parent checks the evidence and requests targeted details when needed, without
automatically rereading the full collection or rerunning completed actions.
