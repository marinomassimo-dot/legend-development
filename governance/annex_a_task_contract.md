---
artifact: LEGEND governance — ANNEX A · TASK CONTRACT
governance_version: 3.1.1
status: FROZEN
normative: yes
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
plan_defined_parameters: RETRY_POLICY on_exhaust default (A.1); APPLICABLE_GOVERNANCE_FINGERPRINT
  composition (A.6) — see plan_defined_parameters.md
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered. Where the annex delegates a value to Plan, that value is
> defined in [`plan_defined_parameters.md`](plan_defined_parameters.md) and never inline here.

---

## ANNEX A — TASK CONTRACT

### A.1 · TASK_ASSIGNMENT **[v3.1.1: +INTERACTION_MODE, +RETRY_POLICY, +MILESTONE_PLAN]**

```
TASK_ID / DIRECTIVE_VERSION (incrementa a ogni modifica, incl. OPERATOR_OVERRIDE con origin: OPERATOR)
GENERATION (incrementa a ogni riassegnazione) / OWNER (ACTOR_ID) / PRIORITY
OBJECTIVE / SCOPE / ACCEPTANCE_CRITERIA (verificabili) / DEPENDENCIES
REVIEW_REQUIREMENT (floor Ladder, Annex C)
INTERACTION_MODE: AUTONOMOUS_COMPLETE | QUESTIONS_ALLOWED | SINGLE_TURN        [E6]
RETRY_POLICY: max_attempts / classi di errore ritentabili /
              on_exhaust: REASSIGN | PARK | ESCALATE (default definito da Plan) [E7]
MILESTONE_PLAN: le milestone durevoli attese del task — ciascuna con l'evidenza
                durevole verificabile che deve lasciare (receipt, output, registry,
                checkpoint). Definisce la granularità di WORK_COMMIT e idempotenza [E2]
DELIVERABLE (artefatto + worktree/branch) / CURRENT_STATE (durable pointer)
```

### A.2 · TASK_ACK

`TASK_ID / DIRECTIVE_VERSION / GENERATION / ACCEPTED | REJECTED(motivo → CHALLENGE, Annex F)`. Nessun lavoro senza ACK; ACK assente entro timeout → reinvio (Annex B).

### A.3 · TASK_CLAIM

Assigned ≠ claimed. Dopo l'ACK, claim durevole prima di iniziare: `TASK_ID / GENERATION / ACTOR_ID / timestamp / durable pointer`. **Al più UN claim valido per TASK_ID + GENERATION.**

```
GUARANTEE:  unicità per costruzione organizzativa — single-assigner (Orchestrator) + claim record durevole
FAILURE:    doppio claim su riassegnazione concorrente o rehydration stale (nessun lock di filesystem)
DETECTION:  secondo claim su stessa TASK_ID+GENERATION → CLAIM_CONFLICT alla scrittura o alla riconciliazione di Plan
RECOVERY:   Orchestrator aggiudica; l'altro attore riceve TASK_CANCEL o nuova generation; duplicati censiti, mai persi in silenzio
```

### A.4 · TASK_GENERATION — anti-zombie

> Ownership versionata. Un attore reidratato MUST verificare generation, directive version **e compatibilità del checkpoint (A.6)** prima di riprendere. Stale → NON continuare, chiedere stato.

### A.5 · Stati del task **[v3.1.1: +AWAITING_APPROVAL]**

```
ASSIGNED → ACKED → CLAIMED → IN_PROGRESS → (BLOCKED | AWAITING_APPROVAL) → IN_PROGRESS
        → COMPLETE | CANCELLED | REASSIGNED(gen+1) | PARKED
```

`AWAITING_APPROVAL` (E3, ≈ A2A input-required): il task si parcheggia al punto esatto con checkpoint (A.6) e riprende senza rifare lavoro (A.7). Ogni transizione è stato durevole + evento (Annex J).

### A.6 · CHECKPOINT — oggetto formale **[v3.1.1, E1 con correzione fingerprint]**

```
CHECKPOINT_ID / ACTOR_ID / TASK_ID + DIRECTIVE_VERSION + GENERATION
APPLICABLE_GOVERNANCE_FINGERPRINT: hash degli artefatti di governance PERTINENTI
    all'attore/classe di task — ROLE_CONTRACT_HASH + annessi/sezioni applicabili,
    secondo la COMPOSIZIONE DEFINITA DA PLAN per ruolo/classe di task
GOVERNANCE_VERSION: (solo audit — NON decide la compatibilità)
MILESTONES_REACHED: riferimenti al MILESTONE_PLAN con evidenza durevole per ciascuna
DURABLE_POINTERS / TIMESTAMP
```

Trigger di scrittura: a ogni milestone durevole raggiunta; prima di rotazione (§36.4 corpo); al passaggio in AWAITING_APPROVAL o PARKED.

**Regola del rifiuto (pattern MAF):** la rehydration che trova directive_version, generation o **fingerprint** incompatibili NON riprende — segnala e chiede stato a Orchestrator. Una modifica di governance NON pertinente (fingerprint invariato) non invalida il checkpoint anche se GOVERNANCE_VERSION è cambiata: la versione globale è audit, il fingerprint è compatibilità.

```
GUARANTEE:  nessuna ripresa silenziosa sotto contratto o regole pertinenti superate;
            nessuna invalidazione inutile per modifiche non pertinenti
FAILURE:    (a) checkpoint non scritto prima del crash → si riparte dall'ultimo valido (perdita accettata);
            (b) composizione del fingerprint mal calibrata: troppo larga → invalidazioni inutili,
                troppo stretta → ripresa sotto regole cambiate
DETECTION:  (a) checkpoint assente/vecchio alla rehydration; (b) Mirror monitora il tasso di
            invalidazioni e i casi di ripresa poi contestati
RECOVERY:   (a) richiesta stato a Orchestrator → conferma o nuovo contratto;
            (b) Plan ricalibra la composizione del fingerprint (modifica governata)
```

### A.7 · RESUME IDEMPOTENTE **[v3.1.1, E2 con correzione milestone]**

> *Completed work is not repeated.* Prima di rieseguire un passo dopo resume/retry, l'attore verifica nello stato durevole se l'evidenza della milestone esiste già; se esiste, salta e registra `RESUMED_FROM_MILESTONE`.

**Il confine di idempotenza è la MILESTONE DUREVOLE SIGNIFICATIVA** (definita nel MILESTONE_PLAN), NON ogni operazione mutante. Un passo significativo deve lasciare stato durevole verificabile; il WORK_COMMIT raggruppa milestone coerenti alla granularità del piano — vietato il commit noise quanto il lavoro volatile. Il pattern receipt-ledger ("il ledger decide se un paper è letto") è il caso fondativo.

```
GUARANTEE:  niente doppio lavoro sulle milestone già durevoli
FAILURE:    lavoro completato ma non ancora durevole al crash → verrà rifatto (caso base accettato);
            milestone troppo grosse → più lavoro rifatto; troppo fini → commit noise
DETECTION:  esistenza dell'evidenza nello stato durevole; Mirror osserva il rapporto rifatto/totale
RECOVERY:   skip + RESUMED_FROM_MILESTONE; Plan/Orchestrator ricalibrano il MILESTONE_PLAN nei contratti successivi
```
