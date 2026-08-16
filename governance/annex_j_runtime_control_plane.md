---
artifact: LEGEND governance — ANNEX J · RUNTIME CONTROL PLANE
governance_version: 3.1.1
status: FROZEN
normative: yes
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
plan_defined_parameters: EVENT LEDGER one-writer design, option (a) or (b) (J.1) — see plan_defined_parameters.md
referenced_by: the CLAUDE.md of every worktree (J.0 is the consolidated guarantees table)
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered. J.0 is the table the body's transversal GUARANTEE rule points
> at: no document and no actor may describe these mechanisms in stronger vocabulary than the
> compensating protocol beside them.

---

## ANNEX J — RUNTIME CONTROL PLANE

### J.0 · GARANZIE NON POSSEDUTE — tabella normativa consolidata **[v3.1.1, E10]**

Referenziata dai CLAUDE.md. LEGEND file/worktree-based NON possiede:

| Garanzia assente | Protocollo compensativo (dettagli G/F/D/R) |
|---|---|
| Task checkout atomico (lock) | single-assigner + claim record + rilevazione conflitto (A.3) |
| Exactly-once / delivery garantita | ACK + dedup MESSAGE_ID + reinvio + DIAGNOSE (B.3, F.4) |
| Transactional workflow state con replay automatico | snapshot + restore documentato (D.4) + checkpoint/resume idempotente (A.6–A.7) |
| Failure detection + restart automatici | heartbeat + DOWN + riapertura operatore (§36 corpo) |
| RBAC enforced a runtime (attori interattivi) | authority matrix testuale + audit + event ledger (H.1, J.1) |
| Singleton garantito (compare-and-swap) | lease record + rilevazione doppio ACTIVE + stop condition (I.3) |

Vietato a qualsiasi documento o attore descrivere questi meccanismi con vocabolario più forte del protocollo compensativo.

### J.1 · ACTIVITY / EVENT LEDGER — append-only STRETTO **[v3.1.1, E8 con correzione]**

Evento:

```
EVENT_ID / timestamp / ACTOR_ID / TASK_ID / EVENT_TYPE / OBJECT / DURABLE_POINTER
CLOSES_EVENT_ID: (solo negli eventi di CHIUSURA — riferimento all'evento di apertura che chiudono)
```

Tipi minimi: `TASK_ASSIGNED, TASK_ACKED, TASK_CLAIMED, TASK_COMPLETE, TASK_CANCELLED, CHECKPOINT_WRITTEN, RESUMED_FROM_MILESTONE, REVIEW_OPENED, REVIEW_CLOSED, WORK_COMMIT, CANDIDATE_CREATED, BATCH_COMMITTED, BATCH_ABORTED, ACTOR_DOWN, ACTOR_ACTIVE, LEASE_ACQUIRED, LEASE_STALE, HUMAN_REQUIRED_OPENED, APPROVAL_RESOLVED, LEARNING_PROMOTED, GOVERNANCE_UPDATED, DISSENT_OPENED, CHALLENGE_ADJUDICATED`.

**Append-only rigoroso:** un evento già scritto NON viene MAI aggiornato — nemmeno per collegarlo alla sua chiusura. Il linkage apertura→esito vive nell'**evento di chiusura**, che porta `CLOSES_EVENT_ID` verso quello di apertura. Un campo `closed_by` può esistere SOLTANTO nella **vista derivata/replayed** costruita da Plan, mai nel ledger sorgente. "State changes by appending events, never by mutating."

**Sovranità:** la vista di runtime è ricostruibile per replay del ledger consolidato, ma **lo stato repo resta sovrano** — in conflitto vince il repo; il ledger è audit e analisi, mai seconda fonte di verità.

**Design one-writer (decisione di Plan):** (a) event file per-attore nel proprio worktree, consolidati da Plan in vista canonica derivata; oppure (b) eventi derivati da commit + messaggi ACKati. Requisito comune: append-only, nessun file condiviso multi-writer.

```
GUARANTEE:  eventi immutabili, attribuiti, con esiti tracciabili via CLOSES_EVENT_ID; replay possibile
FAILURE:    eventi mancanti (attore caduto prima dell'append); consolidamento in ritardo; apertura senza chiusura
DETECTION:  incrocio ledger ↔ stato durevole (gap = evento mancante); aperture senza chiusura oltre soglia
            → Mirror retrospettive
RECOVERY:   Plan ricostruisce dallo stato durevole marcando RECONSTRUCTED; le chiusure ricostruite
            portano anch'esse CLOSES_EVENT_ID
```

Uso primario: Mirror analizza il laboratorio dal ledger (non da 50 chat); autonomy ledger e review yield derivano da qui. Le chat restano la human inspection surface.

### J.2 · State machine attori e laboratorio

```
ATTORE: BOOTSTRAPPING → ACTIVE ⇄ (IDLE | RUNNING) ; RUNNING → BLOCKED | AWAITING_APPROVAL → ACTIVE
        ACTIVE → DEGRADED (rotazione) | DOWN (timeout) | PAUSED (operatore) | RETIRED
LAB:    BOOTSTRAP | OPERATIONAL | ORPHAN (cause: orchestrator DOWN) | SUSPENDED
```

ORPHAN è stato del LAB. Ogni transizione = evento (J.1) + roster durevole.

### J.3 · HUMAN_APPROVAL_QUEUE **[v3.1.1: esiti ricchi E3 + clausola E4]**

```
APPROVAL_ID / REQUESTED_BY (ACTOR_ID) / TYPE (MAJOR | SPEND | DESTRUCTIVE | GOVERNANCE | STRATEGIC)
OBJECT (es. CANDIDATE_CONTENT_HASH + BASE_HEAD; voce di spesa; operazione)
RATIONALE / REQUESTED_AT
STATE: PENDING | APPROVED | APPROVED_WITH_MODIFICATION | DENIED | REVISION_REQUESTED
RESOLUTION (chi, quando, note; per APPROVED_WITH_MODIFICATION: la modifica → nuova directive_version
            del task interessato; per DENIED: motivazione che torna all'attore richiedente)
```

Regole: ogni HUMAN_REQUIRED crea un oggetto in coda; il resto del laboratorio continua; il task interessato va in `AWAITING_APPROVAL` con checkpoint e riprende idempotente (A.5–A.7); il DAILY_BRIEF espone `PENDING HUMAN DECISIONS`; REVISION_REQUESTED su un candidate → Plan → nuovo hash → nuove review; l'approvazione cita l'hash esatto (gate 5).

> **APPROVAL ≠ AUTHORIZATION (E4):** l'approvazione autorizza l'intento, non bypassa i gate. L'esecuzione approvata resta soggetta a GATE 0–5, stop conditions e authority matrix. Un MAJOR approvato con root dirty resta NO BATCH.

### J.4 · COST_POLICY

```
DEFAULT_EXTERNAL_SPEND = 0
operazione a pagamento → HUMAN_APPROVAL (TYPE: SPEND) → BUDGET_ENVELOPE approvato
BUDGET_ENVELOPE: APPROVAL_ID / scopo / tetto / validità / consumo registrato (eventi J.1)
esaurimento o scadenza → nuova approvazione; MAI spesa fuori envelope
```

La stop condition sui costi è l'enforcement fail-closed di questa policy.
