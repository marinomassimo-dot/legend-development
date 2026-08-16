---
artifact: LEGEND governance — ANNEX C · REVIEW PROTOCOL
governance_version: 3.1.1
status: FROZEN
normative: yes
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered.

---

## ANNEX C — REVIEW PROTOCOL

### C.1 · Review Ladder con floor

`R0 · R1 PEER · R2 INDEPENDENT (semi-blind) · R3 TRIADIC · R4 METHOD (Mirror) · R5 CROSS-MODEL (Codex)`.

| Classe | Floor |
|---|---|
| osservazione L1 ordinaria | R0 |
| inferenza L2 importante | R1 |
| inferenza therapeutic-actionable | R2 |
| disaccordo scientifico persistente | R3 |
| processo inferenziale methodology-changing | R4 |
| casi cross-model specificati | R5 |

Derogabili solo verso l'ALTO; sotto il floor solo con rationale registrato.

### C.2 · Formato unico

```
REVIEW_ID / OBJECT (claim id / CANDIDATE_CONTENT_HASH / directive id) / LEVEL / REVIEWER / AUTHOR / ADJUDICATOR
STEELMAN (obbligatorio, prima delle obiezioni)
EVIDENCE_FOR / EVIDENCE_AGAINST / ALTERNATIVES_CONSIDERED / KEY_OBJECTIONS
VERDICT: CONFIRMED | WEAKENED | REFINED (+REFINED_FORMULATION) | REFUTED
REVIEWER_CONFIDENCE / RESIDUAL_UNCERTAINTY / EVIDENCE_NEEDED
WHAT_WOULD_CHANGE_MY_MIND (falsificatore dichiarato, obbligatorio)
AUTHOR_RESPONSE (obbligatoria; il silenzio non è accettazione)
```

CONFIRMED = "nessun difetto rilevato dato l'evidence bundle disponibile", non "vero".

### C.3 · Disciplina

Apertura solo via Orchestrator; rotazione; per review importanti AUTHOR ≠ REVIEWER ≠ ADJUDICATOR; reviewer senza evidenza contribuita; max 2 round → adjudication; cap una review attiva per Scientist; semi-blind = `independence by task framing, not by information barrier`; `DISAGREEMENT_UNRESOLVED` con spiegazione è esito legittimo.

### C.4 · Tre oggetti

`EVIDENCE → Scientist + Plan/provenance · INFERENCE → peer Scientist · SYSTEM → Mirror`.
