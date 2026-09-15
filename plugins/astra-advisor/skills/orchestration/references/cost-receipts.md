# API-equivalent cost receipts

When the user requests usage or cost details, use the existing Python standard
library calculator for API price estimates:
[calculator](../../../scripts/cost_receipt.py),
[pricing snapshot](../../../pricing/2026-09-04.json).
Resolve these paths relative to this installed reference, not a guessed cache version.
If no observed usage is accessible, report why it is unavailable; a fabricated input
or calculator run is unnecessary. Keep observed consumption, estimated API prices,
and demonstrated savings distinct. A savings claim needs comparable observed runs,
including coordination and corrections, with their scope, quality, and cost basis;
same-token repricing alone does not establish it.

Routing may use models absent from the pricing snapshot. Missing rates make the
affected estimate unavailable, not the model ineligible for delegation. The bundled
calculator's comparison baseline remains Astra regardless of the selected parent.

Use only non-overlapping observed usage with an explicit source. Cumulative telemetry
snapshots are not additive calls. Never sum a parent-inclusive aggregate with child
totals. Do not turn message lengths into claimed observed usage. Missing usage or
rates must remain unavailable, and partial coverage must state which work is missing.
Whole-task coverage requires every parent and subagent call, including failed attempts,
review, corrections, and final parent work. If the final response's tokens cannot yet
be observed, identify the receipt's cutoff and do not claim whole-task completeness.

Cached input is a subset of total input. Output already contains reasoning tokens;
never add them a second time. Explicit per-call standard short-context eligibility
is required; unknown or unsupported long-context, service-tier, or cache-write pricing
must not silently inherit standard rates. Effort is recorded without a rate multiplier.

The snapshot records USD per million tokens and official source URLs, with a
2026-09-04 verification date supplied by the recording coordinator. It is a historical
snapshot, not a live-price guarantee; Sol rates are promotional. Disclose the snapshot
date and freshness when showing an estimate. Use a newly verified versioned snapshot
if current prices are required. Do not silently change historical receipts.

~~~text
API-EQUIVALENT COST RECEIPT
usage: <observed source and cutoff, partial, or unavailable with reason>
scope: <whole task only if complete; delegated-only or observed subset otherwise>
pricing: <snapshot date; historical USD estimate; Sol promotional if applicable>
routed: <USD estimate or unavailable>
same-token Astra repricing: <USD or unavailable>
same-token API price difference: <USD and percentage where valid, or unavailable>
limits: This is not a measured all-Astra counterfactual, actual net task savings,
        or a change in ChatGPT subscription charges or usage credits.
~~~

When no subagents ran, state `no delegation savings`. When no usage is exposed,
state `unavailable: native tools did not expose observed token usage`; never show
zero cost. Keep any illustrative fixture result visibly separate from live usage.

## Calculator input and execution

Run `python3 cost_receipt.py INPUT.json [--pricing PATH]` using the installed
calculator path above. It emits a JSON receipt; exit 0 includes calculated, partial,
and unavailable outcomes, while invalid input or pricing exits 2. Inspect the
receipt status instead of treating exit 0 as proof of complete usage.

The version 1 input contains:

- `schema_version: 1`, `task_id`, and `coverage` with `scope` (`whole_task` or
  `delegated_only`), `agent_roster_complete`, and `final_parent_usage_cutoff` booleans.
- `agents`: unique `agent_id`, `role` (`parent`, `delegate`, or `reviewer`), and
  `calls_complete`. Declare missing agents rather than omitting them to improve coverage.
- `calls`: globally unique `call_id`, declared `agent_id`, `model`, optional `effort`,
  and `aggregation: "atomic"`. Supply `usage.kind`, a non-empty `usage.source`, and
  `input_tokens`, `cached_input_tokens`, and `output_tokens` when known. Optional
  `reasoning_tokens` is already included in output. Missing values stay unknown.
- Each call also declares `context: "standard"` and `service_tier: "standard"`, with
  `context_source` and `service_tier_source` set to `observed` or `assumed`. If runtime
  tier metadata is null, a clearly disclosed standard-price scenario is permitted;
  never relabel that assumption as observed billing. Known nonstandard regimes
  are unsupported. Do not assume a workload eligible when evidence contradicts it.

See the [illustrative input](../../../examples/illustrative-usage.json) for an
executable fixture, distinct from observed task usage. Receipts preserve assumptions,
usage provenance, and per-agent coverage. Delegated-only scope includes reviewers;
whole-task scope needs an authoritative complete roster, complete calls for each
agent, a parent, and final parent usage. Solo work does not require an invented
reviewer. False completeness flags keep the result partial or unavailable.

For cumulative native telemetry, retain each snapshot as source evidence, skip exact
repeats, and derive atomic records only when the cumulative delta matches the
reported last-call usage for every token field. If events are missing, counters reset,
or aggregate ownership is unclear, mark that coverage unavailable rather than
inventing calls. Keep preparation-turn usage separate from the implementation turn
when that is the declared task scope.

The bundled calculator conservatively caps each call at 128,000 input tokens. This
is an implementation support boundary, not an official model pricing threshold.
Missing cache counts remain unknown; provide an explicit zero only when supported
by the usage source. Unknown usage fields are rejected to avoid ignoring cache writes.
