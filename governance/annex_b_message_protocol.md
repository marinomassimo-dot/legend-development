---
artifact: LEGEND governance — ANNEX B · MESSAGE PROTOCOL
governance_version: 3.1.1
status: FROZEN
normative: yes
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
plan_defined_parameters: ACK timeout (B.3); HEARTBEAT cadence (B.3) — see plan_defined_parameters.md
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered. Where the annex delegates a value to Plan, that value is
> defined in [`plan_defined_parameters.md`](plan_defined_parameters.md) and never inline here.

---

## ANNEX B — MESSAGE PROTOCOL

### B.1 · Envelope

`MESSAGE_ID / TASK_ID / ACTOR_ID (identità) / FROM (ref runtime, routing) / TO (ref) / TYPE / STATE_CHANGE: yes|no / DURABLE_POINTER`.

### B.2 · Tipi

```
TASK_ASSIGNMENT · TASK_ACK · TASK_CLAIM · STATUS_UPDATE · BLOCKER · TASK_COMPLETE · TASK_CANCEL · HANDOFF
DISSENT · ORCHESTRATOR_CHALLENGE
REVIEW_REQUEST · REVIEW_OPENED · REVIEW_RESULT · UNRESOLVED_CONFLICT
SESSION_LEARNING · GOVERNANCE_UPDATE · HUMAN_REQUIRED · OPERATOR_OVERRIDE · HEARTBEAT
```

### B.3 · Affidabilità

ACK obbligatorio su `STATE_CHANGE: yes` entro timeout (Plan); assente → reinvio (dedup via MESSAGE_ID); secondo fallimento → BLOCKER.

```
GUARANTEE:  un messaggio state-changing non ACKato non è mai assunto consegnato
FAILURE:    ACK emesso ma lavoro mai partito (classi misurate: turno troncato, permission prompt); duplicati post-reinvio
DETECTION:  HEARTBEAT + assenza di TASK_CLAIM/STATUS entro finestra; MESSAGE_ID deduplica
RECOVERY:   DIAGNOSE (Annex F.4) — mai classificare come rifiuto un guasto di runtime
```

HEARTBEAT attore→Orchestrator a cadenza fissa (Plan); alimenta il timeout DOWN. BROADCAST con ricevuta nel roster; senza ACK niente assegnazioni sulle aree toccate.

### B.4 · Anti-flooding

Cambi di stato, decisioni, blocchi, esiti review, learning → messaggi. Chatter → locale. Dentro un'interazione autorizzata (§20.3) dialogo diretto libero; a Orchestrator solo apertura/esito/conflitto irrisolto.

### B.5 · Mappa nominale A2A **[v3.1.1, E5b — convertibilità, NON rinomina]**

```
ASSIGNED≈submitted · IN_PROGRESS≈working · AWAITING_APPROVAL/BLOCKED≈input-required ·
COMPLETE≈completed · CANCELLED≈canceled · REJECTED(ACK)≈rejected · (failure→failed via RETRY_POLICY on_exhaust)
```

Documentazione di corrispondenza per interop futura; il vocabolario LEGEND resta invariato.
