# Registry scale — the decision, and one corrected measurement (2026-10-20)

> **Non-normative decision note**, beside
> [`registry_scale_decision_packet_20261020.md`](registry_scale_decision_packet_20261020.md).
> The packet is left exactly as it was measured; this note carries the decision taken on it and
> the one figure in it that re-measurement found false.

## The decision

**ORCHESTRATOR DECISION 2026-10-20** (the operator delegated it to the Orchestrator, who took it
on the packet's measurements): **adopt option A now, plus the discovery-ledger change-log move.
B (shard by record range), C (shard by year) and D (event store) are rejected. E (per-record
cold/hot history split) is deferred to the new trigger — to a measurement, not to a date.**

Reasoning, recorded so a later session can revert it knowingly:

- Nothing measured in the metabolic batch of 2026-10-19 costs anything because of file size:
  session context 0 bytes at every profile below FULL, a record lookup 0.83 s, a record-scoped
  edit 0.17 s, a depth screen 0.62 s, LINT 7.85 s over the whole repository.
- The one structural pain the batch really paid, repeatedly, was an append conflict at the end of
  one file between parallel branches — and sharding by record range does not cure it, because
  every new record lands in the last shard.
- Against that, any split costs about 20 tools, 26 tests and 370 linking documents, paid once, to
  buy nothing that was measured.
- A byte trigger that fires where no harm is measurable spends operator turns on a non-question,
  which is the bureaucratic weight the operator's principles forbid. So the trigger is re-founded
  on cost, not size.

## What A is, now that it is implemented

`framework/scripts/growth_anchors.py` no longer carries `REGISTRY_SIZE_TRIGGER_BYTES`. Two
measured per-surface budgets replace it, each with its rationale where it is defined, and
`growth_anchors.py check` prints the measured value beside the budget whether or not anything
fires:

| Axis | Budget | Measured 2026-10-20 (largest surface) | Rationale |
|---|---:|---:|---|
| `record_access_seconds` | 0.25 s | 0.008 s (papers, 1,541,499 bytes, 813 records) | a session's record lookup stays under ~2 s end to end — the latency at which measured behaviour changed before record-level access existed (sessions grepped instead of reading records) |
| `record_rewrite_seconds` | 0.25 s | 0.001 s (papers) | one batch's propagation stays under ~1 min of pure re-serialisation |

Watched surfaces: the paper registry, the literature log, the claim registry **and the discovery
ledger**, which had no scale anchor at all. LINT is deliberately not an axis: it is repo-wide,
cannot be attributed to one surface, and measuring it would mean running from inside the module
`legend_lint.py` itself imports. A deferral binds to the cost it was taken at and expires at
+25 %; from the third deferral of the same surface `acknowledge-scale` refuses unless
`--operator-decision` names the instruction it acts on (Mirror A7's condition, and the escalation
the module declared as a known gap when the byte trigger was written).

## The corrected measurement

🔴 The packet said the discovery ledger's `## Change-log` block was **470,808 bytes, 58 % of the
file**, and recommended moving it as the cheapest real size cut. **That figure was false.** It was
repeated from a comment in `registry_records.py` that described an earlier shape of the ledger,
when the change-log ran to the end of the file; it was not re-measured when the packet was
written, which is this author's defect and exactly the "a number describing another artefact is
derived, not copied" rule this repository already carries.

Measured on 2026-10-20, on the file:

| | Bytes | Share | Lead records inside |
|---|---:|---:|---:|
| `## Change-log` block | 2,871 | 0.36 % | 0 |
| the 24 dated `## Run …` / `## Failure mode …` / `## Nota …` sections | 669,319 | 84 % | **193 of 221** |
| whole file before the move | 797,603 | 100 % | 221 |

So the change-log move was done — it is genuine cold history and it is now in
`disease-models/wwox/research/discovery_ledger_history.md`, verbatim, with a pointer left in its
place — but it reduces the ledger by 2,612 bytes, not by 58 %. **The bulk of the ledger is its
dated run sections, and they hold most of its live leads**, so moving them would take current
material out of the current file. Cutting the ledger down needs the per-record split (option E),
which this same decision defers to the cost trigger. Nothing is pending on the operator.
