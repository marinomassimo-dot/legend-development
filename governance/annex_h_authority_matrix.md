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

> **AMENDMENT 2026-09-05 — `DEC-20260905-AGILE-HARNESS-MODE`.** H.1 is amended by the operator;
> the amended rows follow the frozen table below and prevail over it where they conflict. The
> operating rule is [`LEGEND_CORE.md` §21e](../framework/instruction/LEGEND_CORE.md#21e-agile-operating-mode).

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

> **AMENDMENT 2026-09-05 — `DEC-20260905-AGILE-HARNESS-MODE` (operator decision, H.1 rows
> "Spese / MAJOR approval / governance" and "Strategia complessiva").** The table above is
> the frozen text. The rows below **replace** the corresponding rows above wherever they
> conflict; the rule itself lives in
> [`framework/instruction/LEGEND_CORE.md` §21e AGILE OPERATING MODE](../framework/instruction/LEGEND_CORE.md#21e-agile-operating-mode).
>
> | Decisione | Authority (as amended 2026-09-05) |
> |---|---|
> | Integrazione strutturale / candidate | the **author** lands its own task branch on `main` at task end; Harness Engineering (`plan`) lands harness changes at T0. No INTEGRATION_CANDIDATE required |
> | CANONICAL_BATCH_COMMIT | whoever holds the `BATCH_COMMIT` task, under `LINT`, one batch at a time — no lease |
> | WORK_COMMIT | every actor, on its task branch **or directly on `main`**; milestone granularity stands |
> | Landing on `main` (merge of own branch) | the author — no Mirror precondition, no HUMAN_APPROVAL, no gate |
> | Harness changes (framework/, governance/, roles/, scripts/, .claude/, deployment/, BOOTSTRAP.md, CLAUDE.md, AGENTS.md) | Harness Engineering (`plan`), at T0; anyone assigned by it |
> | Weekly harness scouting (GitHub, Hugging Face, Nature portfolio) | Junior Harness Engineer (`junior-harness`) proposes; Harness Engineering decides ADOPT / TRIAL / WATCH / REJECT |
> | Worktree provisioning and clean removal; `git branch -d` of a merged branch | every actor, for its own worktree and branches |
> | Spese / MAJOR approval / governance | Operatore — **unchanged** for spend and for §21d's RESERVED list; harness changes are not "MAJOR approval" items |
> | Epistemic / method review | Mirror — **ex post and on request**, never a precondition |

### H.2 · GOVERNANCE_VERSION E FINGERPRINT **[v3.1.1]**

Corrente: **3.1.1**. Macro-upgrade → incremento versione + GOVERNANCE_UPDATE con ACK; mismatch su area → assegnazioni sospese. In rehydration: dichiarazione versione + verifica fingerprint. Ruoli dei due livelli: `GOVERNANCE_VERSION` = audit globale; `APPLICABLE_GOVERNANCE_FINGERPRINT` = compatibilità del resume per attore/classe di task (composizione: Plan; schema: A.6). Colonne `Governance version ACK` e `Fingerprint` nell'inventory.
