---
artifact: LEGEND governance — ANNEX H · AUTHORITY MATRIX & GOVERNANCE_VERSION
governance_version: 3.1.1
status: FROZEN
normative: yes
change_class: MAJOR — H.1 is marked [MAJOR]; any modification requires the full gate 3
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
replicated_into: the common AUTHORITY & ROUTING section of every worktree CLAUDE.md (body §35.2)
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered. Body §7 and §35.2 require this matrix to be replicated into
> each worktree's CLAUDE.md; the replica is a copy, and this file is the source.

---

## ANNEX H — AUTHORITY MATRIX & GOVERNANCE_VERSION

### H.1 · Authority matrix **[MAJOR]**

| Decisione | Authority |
|---|---|
| Task / priorità / riassegnazione / generation | Orchestrator |
| Conclusione scientifica | Scientist responsabile (soggetta a review, mai a ordine) |
| Livello Ladder (≥ floor) e reviewer | Orchestrator |
| Integrazione strutturale / candidate | Plan |
| Rifiuto integrazione per provenance/schema | Plan (INTEGRATION_BLOCK) |
| Epistemic / method review | Mirror |
| Classificazione MAJOR dubbia | Mirror (fail-closed) |
| CANONICAL_BATCH_COMMIT | Orchestrator (unico, lease ACTIVE) |
| WORK_COMMIT | ogni attore, solo proprio branch, granularità milestone |
| Spese / MAJOR approval / governance | Operatore |
| Strategia complessiva | Operatore |
| Classificazione HUMAN_REQUIRED ordinaria | Orchestrator |
| Aggiudicazione challenge | Orchestrator (con rationale) |
| Composizione APPLICABLE_GOVERNANCE_FINGERPRINT [v3.1.1] | Plan (modifica governata) |
| Lifecycle learning: epistemico Mirror, durevolezza Plan | — |
| Modifica rubrica/metodi di Mirror | mai Mirror da solo (G.2) |
| Promozione BOOTSTRAP_CONTROLLER → Orchestrator | protocollo Annex I (mai autoassunzione) |

### H.2 · GOVERNANCE_VERSION E FINGERPRINT **[v3.1.1]**

Corrente: **3.1.1**. Macro-upgrade → incremento versione + GOVERNANCE_UPDATE con ACK; mismatch su area → assegnazioni sospese. In rehydration: dichiarazione versione + verifica fingerprint. Ruoli dei due livelli: `GOVERNANCE_VERSION` = audit globale; `APPLICABLE_GOVERNANCE_FINGERPRINT` = compatibilità del resume per attore/classe di task (composizione: Plan; schema: A.6). Colonne `Governance version ACK` e `Fingerprint` nell'inventory.
