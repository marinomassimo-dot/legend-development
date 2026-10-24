# Discovery Ledger History — WWOX

> **Cold history of [`discovery_ledger_current.md`](discovery_ledger_current.md).** The ledger's
> dated action log — which lead was created, re-statused or corrected, when, and by which run —
> moved here **verbatim** on 2026-10-20 (Orchestrator decision of the N9 scale packet, harness
> task `PLAN-HARNESS-FROM-METABOLIC-BATCH-20261020`). **Read on demand, never at startup, and
> never a source of a current value**: a lead's current state is the lead's own record in
> `discovery_ledger_current.md`, and where this file and that one differ, that one is current.
> The pattern is the one already proven for
> [`working_model_history.md`](../registries/working_model_history.md) and
> [`state_history.md`](../../../framework/state/state_history.md).
>
> **Appended, never rewritten**, by whatever writes the ledger: a new change-log row is added to
> the table below. New LEADS go to the ledger itself, through
> [`discovery_lead.py`](../../../framework/scripts/discovery_lead.py).
>
> 🔴 **What this move is NOT.** It is not the size reduction the N9 packet estimated. That
> estimate (`~470,808 bytes, 58% of the file`) was repeated from a comment in
> `registry_records.py` describing an earlier shape of the ledger and was **false when the move
> was made**: measured on 2026-10-20 the `## Change-log` block is **2,871 bytes, 0.36%** of a
> 797,603-byte file. The ledger's bulk is its 24 dated `## Run …` sections (669,319 bytes, 84%),
> and **193 of its 221 lead records live inside them** — current material, not history, whose
> move would take live leads out of the current file. Cutting the ledger down therefore needs
> the per-record cold/hot split (option E of the packet), which that decision deferred to the
> measured-cost trigger, not this move. The corrected figures are in
> `governance/design_records/registry_scale_decision_20261020_note.md`.

---

## Change-log
| Data | Azione | Voce | Note |
|------|--------|------|------|
| 2026-06-28 | created | ledger | Bootstrap dal template; primo paper = Riccardi 2026 (PMID 42190144) |
| 2026-06-28 | created | DL-MECH-001..004, DL-MOL-001/002, DL-REPO-001 | da Riccardi 2026 (abstract) × CLAIM Breton 2021 |
| 2026-06-28 | created | H-001, H-002 | euristiche distillate |
| 2026-06-28 | created | NS-001..006 | next-search agenda |
| 2026-06-28 | created | DL-BIO-001/002, DL-MECH-005/006 | da referto genetico il record pubblico di variante (genotipo di riferimento) × pipeline strutturale AlphaFold3/AlphaMissense/SpliceAI — modelli da eseguire |
| 2026-06-28 | created | H-003, H-004 | euristiche: strumento-per-tipo-variante; mappare varianti sui dominî |
| 2026-06-28 | created | NS-007..010 | next-search: esecuzione modelli strutturali + correlazione dominio-fenotipo |
| 2026-06-28 | hop NS-002 | DL-MOL-003, DL-MECH-007, NS-011/012 | da Repudi & Aqeilan EMBO Mol Med 2021 (PMID 34268881): organoidi WOREE, asse Wnt, rescue WWOX ectopico |
| 2026-06-28 | assembly | DL-MOL-001 | belief medio→medio-alto, status open→maturing: convergenza Breton+GRIN2A+organoidi (3 fonti indipendenti) |
| 2026-06-28 | hop Wnt/catalisi | DL-MOL-003 (ribaltato), DL-MOL-004, DL-MECH-008, H-005/006/007, NS-013/014/015 | direzione Wnt risolta (Bouteille/Li/Celebi); sito catalitico SDR mappato (PMC4374002); litio→contro-indicato; +lead CRISPRa; conflitto contesto cancro-vs-neurone flaggato |
| 2026-07-03 | paper Obeid/Aqeilan 2026 OMTA gene therapy (supplemental S1–S8) + proof-of-concept 2021 (PMID 34747138) | DL-MOL-005, DL-MECH-009/010/011, H-008/009, NS-016/017/018/019 | gene replacement genotype-agnostic (maturing, belief alto mouse / medio il genotipo di riferimento); WPRE booster 3–16.7× + contraddizione review; neuron-specific driver non-cell-autonomous; gap-timing = domanda-cardine per il genotipo di riferimento. Assembly: belief MECH-007 confermato alto (3 livelli convergenti). Paper già canonico (PAPER Obeid 2026 + CLAIM 011) → nessun CC duplicato; segnalato solo upgrade preprint→published |
| 2026-07-03 | hop "compound Aldaz/Zhang" (richiesta dell'operatore) — ricerca PubMed + web | DL-REPO-002, DL-MECH-012, NS-020/021/022 | asse **neuroinfiammazione** WWOX (Aldaz, multi-tessuto) = ancora meccanicistica; lead REPO anti-infiammatorio riposizionato (direzione risolta: inibire); farmaco specifico + trial "Zhang/Baylor" **NON nel record pubblico** (probabile preclinico/foundation non pubblicato); ponte Baylor reale = Noebels/Seo (Neurology). Recovery via contatto diretto Aldaz (NS-020) |
| 2026-07-05 | deepdive PMID 30619736 | DL-MECH-018, NS-023/024 | WWOX full-length interactome normalizzato come probabile fonte primaria CLAIM 026/CORPUS P182; DVL2 + endomembrane trafficking + Acetyl-CoA diventano pannello sperimentale, non farmaco pronto |
| 2026-10-24 | append (`BATCH_20261019_016`, from `CC-20261021-SCIENTIST-C-R3-A51-ATTRIBUTION-01`) | `DL-THER-089` | Attribution and BLOCK-1 notes only, MINOR additive, record-scoped (14 insertions, 0 deletions). The candidate had been HELD since 2026-10-22 until the repaired manifests were audited by someone other than the producer; both audit files were verified first-hand (`locator_audit_R3_repairs_R3b_20261022.md`; `locator_audit_block1_sources_20261024.md`, 43 of 43 SUPPORTED, 0 adverse). Caveats carried with the claims (n = 3 under a one-sided Mann-Whitney with a P = 0.05 floor; no EEG in either arm). No claim created, reversed or narrowed; no dose, administration or suitability statement; every source NOT WWOX EVIDENCE; the Wnt-versus-MYC-versus-CDK attribution stays unresolved. ⚠️ This table carried no row between 2026-07-05 and this one, although the ledger grew throughout: the gap is pre-existing and is not repaired here. |

---
