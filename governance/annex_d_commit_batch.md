---
artifact: LEGEND governance — ANNEX D · COMMIT & BATCH
governance_version: 3.1.1
status: FROZEN
normative: yes
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
plan_defined_parameters: CANDIDATE_CONTENT_HASH deterministic definition (D.2) — see plan_defined_parameters.md
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered. Where the annex delegates a definition to Plan, that
> definition is in [`plan_defined_parameters.md`](plan_defined_parameters.md), never inline here.

---

## ANNEX D — COMMIT & BATCH

### D.1 · Tre tipi

```
WORK_COMMIT (ogni attore, proprio branch — obbligatorio, non canonico;
             granularità = MILESTONE_PLAN del task, A.1/A.7 — niente commit noise) [v3.1.1]
INTEGRATION_CANDIDATE (Plan — selezione + integrazione + validazione + manifest)
CANONICAL_BATCH_COMMIT (solo Orchestrator, root, gate 0–5)
```

### D.2 · CANDIDATE MANIFEST

```
CANDIDATE_ID / BASE_HEAD / SOURCE_COMMITS
CANDIDATE_CONTENT_HASH: hash del CONTENUTO (tree/patch deterministico definito da Plan) —
                        NON l'hash git del commit futuro
CHANGE_CLASS: ORDINARY | MAJOR
LINT_RESULT + pointer / PUBLICATION_GATE + pointer
MIRROR_REVIEW: n/a | PASS | FAIL + REVIEW_ID
HUMAN_APPROVAL: n/a | APPROVAL_ID (J.3) con hash approvato
SNAPSHOT_ID
```

**[MAJOR] Binding:** ogni approvazione si lega a `CANDIDATE_CONTENT_HASH + BASE_HEAD`; qualsiasi modifica materiale le invalida.

### D.3 · GATE 0 — ROOT STATE

`BASE_HEAD == atteso · root clean · GOVERNANCE_VERSION corretta · lease ACTIVE singleton · ONE_WRITER`. Un FAIL → NO BATCH, `BLOCKED_BY_GOVERNANCE`.

### D.4 · Transazione

`SNAPSHOT → APPLY EXACT CANDIDATE → POST-COMMIT VALIDATE → SUCCESS | BATCH_ABORTED → restore → record → nuovo candidate`. Vietata la riparazione manuale in root. **[v3.1.1, E4]** L'HUMAN_APPROVAL non bypassa questa sezione né i gate: approva l'intento, non l'esecuzione fuori regola.

### D.5 · Dimensione e deadlock

Smallest coherent auditable unit; finestre prevedibili come momento, non criterio. 2 FAIL Plan↔Mirror → Orchestrator convoca; se MAJOR → HUMAN_REQUIRED.
