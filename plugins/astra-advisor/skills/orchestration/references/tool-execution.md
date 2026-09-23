# Tool execution tasks

Use this pattern for a bounded mission whose useful result can be specified before
execution. The parent retains decisions, authorization, and acceptance. Use the
[retained squire](squire.md) for the mission and its related follow-ups.

## Choose the boundary

| Work | Route |
| --- | --- |
| Read a function or configuration to understand it and decide what to do next | Squire |
| Resolve an ambiguity in a delegate's evidence | Ask the squire or relevant delegate for a follow-up |
| Inspect deployment logs, documentation, or a short search result | Squire |
| Check a hypothesis or verify an effect | Squire |
| Apply an authorized, fully specified action with known target, parameters, and effect | Parent may execute directly |

Delegate all acquisition, including trivial contextual lookups. Group related
commands into one mission rather than directing each command. The parent reasons
over returned evidence; unexpected facts requiring investigation go back to the
squire. The parent may load necessary instructions and perform native coordination.

## Brief and execute

Use the assignment and capability contract in [operations](operations.md) and
the optional [routing rules](routing-defaults.md). Choose for the mission without
a mandatory escalation sequence.

Supply only the relevant context using the host's exposed capabilities. Include the goal,
target or working directory, optional commands, permitted effects, constraints,
ownership, and expected result. Honor explicitly required commands; otherwise the
delegate chooses suitable available tools within scope. Do not expand an inspection into
a repair or treat a supplied command as permission to exceed the authorized scope.

The assigned executor uses tools directly and retains execution of the mission.
When the assignment permits it, it may seek narrow read-only advice under
[optional advice](operations.md#optional-advice); it must not hand off execution.
It reports missing access or capability through the normal result. Group
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
