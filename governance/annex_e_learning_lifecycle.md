---
artifact: LEGEND governance — ANNEX E · LEARNING LIFECYCLE
governance_version: 3.1.1
status: FROZEN
normative: yes
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
plan_defined_parameters: role-specific ACTIVE_LESSONS size budgets (E.5) — see plan_defined_parameters.md
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered. Where the annex delegates a value to Plan, that value is
> defined in [`plan_defined_parameters.md`](plan_defined_parameters.md) and never inline here.

---

## ANNEX E — LEARNING LIFECYCLE

### E.1 · State machine

`OBSERVED → LOCAL → PROVISIONAL → VALIDATING → PROMOTED | REJECTED | SUPERSEDED | EXPIRED`

### E.2 · LEARNING_INDEX (durevolezza: Plan; cura epistemica: Mirror)

```
LEARNING_ID / ORIGIN_ACTOR / FIRST_OBSERVED / LAST_OBSERVED / EVIDENCE_COUNT
CONFIRMATION_CLASSES: {actor, session, class} con class ∈ ORIGINAL_OBSERVATION | REPLICATION | EXPOSURE_AFTER_BROADCAST
SCOPE / STATUS / OWNER / AFFECTED_WORKFLOW / EXPIRY_OR_REVIEW_DATE
```

Contano pienamente solo ORIGINAL_OBSERVATION e REPLICATION. Soglia BEST_PRACTICE_CANDIDATE: ≥2 conferme delle prime due classi, o 1 + validazione Mirror. Dedup: simile esistente → conferma con classe. Conflitti → Mirror aggiudica → SUPERSEDED motivato.

### E.3 · PROVISIONAL_OPERATIONAL_PRACTICE

`PRACTICE_ID / HYPOTHESIS / APPLIES_TO / STARTED / EVIDENCE_EXPECTED / SUCCESS_CRITERION / FAILURE_CRITERION / EXPIRY / ROLLBACK`. A scadenza: `PROMOTE | REJECT | EXTEND_WITH_REASON`. Mai provisional per sempre.

### E.4 · Change isolation (solo VALIDATING)

Preregistrare `prediction / metric / falsifier / rollback`. I LOCAL restano spontanei.

### E.5 · Active-learning compression — garanzie e budget **[v3.1.1, E9]**

`RAW ARCHIVE → Mirror clustering → ACTIVE LESSONS → role-specific subset → rehydration`.

Garanzie: (1) **RAW archive lossless** — il clustering non cancella mai i record originali; (2) ogni ACTIVE_LESSON porta **`derived_from: [LEARN-###, …]`** — Mirror non riscrive la storia. **Budget:** ogni subset role-specific ha un budget dimensionale definito da Plan; superato → Mirror comprime o retrocede lezioni (mai toccando il RAW). Modifiche materiali a clustering/selezione = MIRROR_METHOD_CHANGE (G.2).

```
GUARANTEE:  il contesto degli attori non ricresce silenziosamente; la provenance è sempre risalibile
FAILURE:    budget troppo stretto → lezioni utili escluse; compressione che perde sfumature
DETECTION:  errori ripetuti su pattern già appresi (Mirror retrospettive); richieste degli attori
RECOVERY:   ricalibrazione budget (Plan) o ricomposizione subset (Mirror, via G.2 se materiale)
```

### E.6 · Session Learning Record

`Session / Date / ACTOR_ID / Role / Task(id+ver+gen)` + `WORK COMPLETED / PROBLEMS / SOLUTION / LEARNING / MICRO-UPGRADE / IMPACT / CLASSIFICATION / SCOPE / EVIDENCE / LEARNING_ID (+CONFIRMATION_CLASS)`. Persistenza: WORK_COMMIT alla granularità delle milestone (A.7).
