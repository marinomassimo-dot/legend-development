---
record_type: OPERATOR_DECISION
id: DEC-20260926-DAILY-DEVELOPMENT-PUSH
date: 2026-09-26
authority: Operator mandate reported in the AQP handover of 2026-09-26
status: RATIFIED_BY_OPERATOR_MANDATE
applies_to:
  - framework/instruction/LEGEND_CORE.md (§21d, §21e)
  - scripts/test_stop_policy.py
  - framework/scripts/daily_push_check.py
---

# Daily development publication

The operator's AQP mandate removes the remote-name ambiguity that left work unpublished.
The development destination is identified by its repository URL,
`github.com/marinomassimo-dot/legend-development`; this clone names that destination both
`development` and `origin`. The public release destination remains reserved to the operator.
The operator authorises agents to fast-forward the development repository's one named ref,
including `main`, after the checks stated in §21d. No force push, history rewrite, private
material or publication to another destination is authorised.

This changes a reserved publication boundary and therefore records the operator decision,
not an autonomous interpretation by an actor. It does not waive the public release gate,
LINT, receipt verification, release regressions, or the report of branch, SHA, gate and actor.
The daily check reports unpublished work; it never pushes or changes a ref.

## Anchored text

`LEGEND_CORE.md` §21d from `DECISION AUTHORITY (HARD RULE, …)` through the last line of
`REVIEW`, excluding its leading provenance callout and any trailing newline: 63 lines,
sha256 `f028d1baf5f5c3898498bcb3e50191ad09af4ce48ac126ba56656e8c35d45335`.
`scripts/test_stop_policy.py` asserts the same text verbatim. §21e's RESERVED summary now
names the same boundary. The preceding 2026-09-08 digest remains in
`DEC-20260903-STOP-POLICY-AND-DECISION-AUTHORITY` as history.

## Execution and detection

`daily_push_check.py` runs locally at 19:45 Europe/Rome. It compares local refs to the
development remote without changing either, and writes a durable report that the
Orchestrator can inspect at session start. A report is a detection mechanism, not a
guarantee that a suspended agent, offline host or unregistered clone is observed.
