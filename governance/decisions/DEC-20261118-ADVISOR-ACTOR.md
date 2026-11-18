---
record_type: OPERATOR_DECISION
id: DEC-20261118-ADVISOR-ACTOR
title: A distinct ACTOR_ID `advisor` for the ADV host, separate from `orchestrator`, inside the same campaign
date: 2026-11-18
authority: >
  Operator, mandate to Harness Engineering of 2026-11-18 ("decisione esplicita dell'operatore: introdurre ACTOR_ID advisor per l'host ADV,
  distinto da ACTOR_ID orchestrator, mantenendo campagna, storia, lavoro attivo e autorizzazioni esistenti"). No further approval is required.
status: RATIFIED
change_class: MINOR
change_class_rationale: >
  It adds an actor identity and its role contract; it changes no scientific guarantee, no gate and no reserved decision (LEGEND_CORE §21d). Harness change at T0 (§21e).
---

# DEC-20261118-ADVISOR-ACTOR

**Decision.** ACTOR_ID `advisor` is the Strategic Advisor *host* (the ADV session); ACTOR_ID `orchestrator` stays the operative Orchestrator (the IT session);
`plan`, the Scientists and Mirror keep their identities. The read-only Strategic Advisor analyst is not an actor.

**Contract.** `roles/advisor.md` states the perimeter and points to the common sources; it copies nothing from `roles/orchestrator.md`.

**Campaign and history.** The campaign `advisor_pilot_20261113` is unchanged. The standing record `ORCH-ADV-FOLLOWTHROUGH-20261114` keeps its TASK_ID and its events; it moves
under `ledger/tasks/advisor/` with an `ACTOR_HISTORY` entry. Events written as `orchestrator` stay `orchestrator`. No `ORCH-*` task id is renamed.

**Routing.** A recipient that is an ACTOR_ID resolves to the one live session carrying the `MANDATE_BOUND` marker (or the live `SESSION_BINDING`) of an open record of that actor; two sessions
give AMBIGUOUS and none is chosen (`mandate_watch.py route`).

**Reversal.** `roles/advisor.md` "Reverting the assignment": move the record back, restore ACTOR_ID and OWNER, add a history entry. Nothing produced is deleted.
