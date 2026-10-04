# Literature Tracking Log

> **Public edition — de-identified.** Disease-level registry from public literature. All individual-linking data removed (names, geography, report/sample IDs, dates, parent-of-origin, cell-line ownership). Specific variants appear only as decoupled disease-model worked examples drawn from public literature, never as one persistent individual's inherited alleles. Some entries remain in their original language. Not medical advice.
## WWOX — Literature Tracking Log
**Version:** v1.5
**Date baseline:** 2026-03-28
**Last update:** 2026-09-22 — `BATCH_20260922_BIBLIO` (**traceability repair, no scientific change**): the `PAPER 011` record carried the wrong expansion of `OMTA` (*Methods & Clinical Development* is `omtm`, a different journal) **and** still declared *«PMID/DOI da confermare quando indicizzato su PubMed»* although PMID 42422765 / PMC13343157 / DOI 10.1016/j.omta.2026.201791 have been confirmed and recorded in [[paper_registry_current#PAPER 011]] since `BATCH_20260710_A`. Both corrected. **No screening decision, tier or status changed.** Prev: 2026-07-10 — URG_2026-07-09_001 category 5: LIT-0085 Maroni 2017 declassato `background_only / dependency-contaminated`; creato LIT-0401 per il primario ritirato PMID 28151481. Nessun claim baseline contaminato.

---

## Purpose
Procedural memory of the system. Tracks the lifecycle state of every paper that has entered the pipeline — including papers screened out, background-only, or not yet fully processed.

Serves to:
- prevent duplicate processing
- distinguish new papers from already-processed ones
- track when and how each paper was found
- link each paper to its operative state in the system

---

## Status vocabulary

| Status | Meaning |
|--------|---------|
| `discovered` | Found by discovery engine, not yet screened |
| `screened` | Quickly reviewed but not yet filtered |
| `filtered_in` | Passed quality + relevance filter, queued for processing |
| `filtered_out` | Excluded — reason logged |
| `processed` | Fully read, tagged, extracted |
| `claim_linked` | Associated with at least one claim in Claim Registry |
| `integrated` | Used to update or support Working Model |
| `flagged_for_review` | Triggered a review flag, not yet resolved |
| `background_only` | Archived as context, no operative function |
| `superseded` | Replaced by a stronger or more recent paper |
| `excluded_integrity` | **Retracted**; kept only as an audit trail of what was excluded and why; may not support any claim, premise or context. An expression of concern does **not** move a record here: it is carried by `PUBLICATION_INTEGRITY_HOLD` on the record itself |

---

## Deduplication rules

- Same PMID or DOI → update existing record, do not create new entry
- Preprint later published → upgrade single record, update identifier
- Title near-match without identifier → mark as `possible duplicate`, verify before processing
- Paper rediscovered via bibliography mining → add to discovery history of existing record, do not duplicate

---

## Record template

```
## LIT-[NNN]
**Short title:**
**Authors:**
**Year:**
**Source type:**
**Journal/source:**
**Identifier type:** PMID / DOI / Preprint DOI / Internal
**Identifier value:**
**Date discovered:**
**Date processed:**
**Discovery window:**
**Discovery source:** PubMed search / bibliography mining / Scholar pre-scan / manual
**Discovery query:**
**Status:**
**Primary pathway:**
**Genotype/model tag:**
**Transferability:**
**clinical relevance:**
**Claim links:**
**Working Model impact:**
**Report mentions:**
**Next action:**
**Flags:** safety / genotype caution / review trigger / high value human / background only / full text needed / bibliography mine
**Note:**
```

---

## Baseline records — papers from Paper Registry v1.0

---

## LIT-001
**Short title:** Steinberg 2024 organoids
**Authors:** Steinberg et al.
**Year:** 2024
**Source type:** preprint / organoid study
**Journal/source:** bioRxiv
**Identifier type:** Preprint DOI
**Identifier value:** pending
**Date discovered:** 2025-12
**Date processed:** 2025-12
**Discovery window:** 2025-W50
**Discovery source:** manual / uploaded file
**Discovery query:** manual ingestion
**Status:** integrated
**Primary pathway:** P1 / P3 / P7
**Genotype/model tag:** human organoid / WWOX-KO + WOREE-derived / early neurodevelopment / T2
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 002
**Working Model impact:** BLOCCO 2 + BLOCCO 1 support
**Report mentions:** multiple sessions
**Next action:** bibliography mine
**Flags:** high value human / bibliography mine / genotype caution
**Note:** Core paper. Genotype caution: KO ≠ Q230P. MYC overexpression key finding.

---

## LIT-002
**Short title:** Baryła 2022 metabolism review
**Authors:** Baryła / Kośla / Bednarek
**Year:** 2022
**Source type:** review
**Journal/source:** Journal of Molecular Medicine
**Identifier type:** DOI
**Identifier value:** 10.1007/s00109-022-02265-5
**Date discovered:** 2025-12
**Date processed:** 2025-12
**Discovery window:** 2025-W50
**Discovery source:** PubMed search
**Discovery query:** WWOX metabolism
**Status:** integrated
**Primary pathway:** P5
**Genotype/model tag:** review / mixed models / non-CNS specific / T2 conceptual
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Claim links:** 009
**Working Model impact:** BLOCCO 2 only
**Report mentions:** metabolic axis sessions
**Next action:** none
**Flags:** none
**Note:** Useful for HIF1A / PDK1 / ROS / ETC conceptual framework.

---

## LIT-003
**Short title:** Choi 2026 VABAM
**Authors:** Choi et al.
**Year:** 2026
**Source type:** short communication / case report
**Journal/source:** Pediatric Neurology
**Identifier type:** PMID
**Identifier value:** 41442931
**Date discovered:** 2026-03
**Date processed:** 2026-03-27
**Discovery window:** 2026-W13
**Discovery source:** PubMed search
**Discovery query:** WWOX gene 2026
**Status:** integrated
**Primary pathway:** P2 / P4
**Genotype/model tag:** human / pediatric / WWOX-DEE / T1
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** 001
**Working Model impact:** BLOCCO 1 safety — already integrated; CLAIM 001 ora conflicting evidence (aggiornato 2026-03-29)
**Report mentions:** 2026-03-27 flash report; weekly report 2026-03-29
**Next action:** none
**Flags:** safety / high value human
**Note:** Safety anchor. VABAM in 2 WWOX-DEE children on vigabatrin. CLAIM 001 ora conflicting evidence per ingresso di You 2024 e Chong 2023. Posizione clinica generale su vigabatrin invariata.

---

## LIT-004
**Short title:** Repudi 2021 Brain myelination
**Authors:** Repudi et al.
**Year:** 2021
**Source type:** murine mechanistic study
**Journal/source:** Brain
**Identifier type:** pending normalization
**Identifier value:** pending
**Date discovered:** 2025-12
**Date processed:** 2025-12
**Discovery window:** 2025-W50
**Discovery source:** PubMed search
**Discovery query:** WWOX myelination
**Status:** integrated
**Primary pathway:** P4
**Genotype/model tag:** mouse / neuronal deletion / non-null/null but close / T2
**Transferability:** T2
**clinical relevance:** MODERATE
**Claim links:** 003
**Working Model impact:** BLOCCO 2 / surveillance logic
**Report mentions:** myelination sessions
**Next action:** normalize identifier
**Flags:** none
**Note:** Justifies MRI + DTI. OPC present but maturation reduced.

---

## LIT-005
**Short title:** Repudi 2021 EMBO gene therapy
**Authors:** Repudi et al.
**Year:** 2021
**Source type:** preclinical gene therapy study
**Journal/source:** EMBO Molecular Medicine
**Identifier type:** pending normalization
**Identifier value:** pending
**Date discovered:** 2025-12
**Date processed:** 2025-12
**Discovery window:** 2025-W50
**Discovery source:** PubMed search
**Discovery query:** WWOX AAV gene therapy
**Status:** integrated
**Primary pathway:** P7
**Genotype/model tag:** mouse / Wwox-null / preclinical / T2
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 004
**Working Model impact:** strategic / trial-readiness support
**Report mentions:** gene therapy sessions
**Next action:** normalize identifier
**Flags:** bibliography mine
**Note:** Central for trial-readiness logic. Now complemented by Obeid 2026.

---

## LIT-006
**Short title:** Hussain 2019 GABA/glia
**Authors:** Hussain T, Kil H, Hattiangady B, Lee J, Kodali M, Shuai B, Attaluri S, Tome-Garcia J, Meghed M, Jang M-H, Shetty AK, Aldaz CM
**Year:** 2019
**Source type:** murine mechanistic study
**Journal/source:** Neurobiology of Disease 121:163–176
**Identifier type:** PMID
**Identifier value:** 30290271
**Date discovered:** 2025-12
**Date processed:** 2025-12
**Discovery window:** 2025-W50
**Discovery source:** PubMed search
**Discovery query:** WWOX interneurons GABA
**Status:** integrated
**Primary pathway:** P2 / P6
**Genotype/model tag:** mouse / Wwox-KO / T2
**Transferability:** T2
**clinical relevance:** MODERATE
**Claim links:** 005
**Working Model impact:** safety / modifier logic
**Report mentions:** GABA safety sessions
**Next action:** normalize identifier
**Flags:** none
**Note:** Do not overtranslate as absolute GABA prohibition. Structured caution.

---

## LIT-007
**Short title:** Hussain 2023 P47T
**Authors:** Hussain et al.
**Year:** 2023
**Source type:** variant-specific mechanistic study
**Journal/source:** pending normalization
**Identifier type:** pending normalization
**Identifier value:** pending
**Date discovered:** 2025-12
**Date processed:** 2025-12
**Discovery window:** 2025-W50
**Discovery source:** PubMed search
**Discovery query:** WWOX P47T neuroinflammation
**Status:** integrated
**Primary pathway:** P6 / P3
**Genotype/model tag:** mouse / P47T variant / T3 / genotype caution mandatory
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** 006 / 007
**Working Model impact:** genotype caution anchor
**Report mentions:** genotype sessions
**Next action:** normalize identifier
**Flags:** genotype caution
**Note:** Critical for establishing Q230P ≠ P47T rule.

---

## LIT-008
**Short title:** Aldaz/Banne clinical spectrum
**Authors:** Aldaz / Banne cluster
**Year:** 2019–2021
**Source type:** review / clinical spectrum
**Journal/source:** various
**Identifier type:** multiple / pending normalization
**Identifier value:** multiple / pending
**Date discovered:** 2025-12
**Date processed:** 2025-12
**Discovery window:** 2025-W50
**Discovery source:** manual / literature review
**Discovery query:** WWOX spectrum WOREE SCAR12
**Status:** integrated
**Primary pathway:** clinical spectrum
**Genotype/model tag:** human / review / T1 contextual
**Transferability:** T1 contextual
**clinical relevance:** MODERATE
**Claim links:** 008
**Working Model impact:** contextual background
**Report mentions:** clinical spectrum sessions
**Next action:** normalize identifiers
**Flags:** none
**Note:** Nosology anchor. Contextual, not directly therapeutic.

---

## LIT-009
**Short title:** NIH ODS mitochondrial supplements fact sheet
**Authors:** NIH ODS
**Year:** baseline
**Source type:** professional fact sheet
**Journal/source:** NIH
**Identifier type:** internal uploaded file
**Identifier value:** uploaded reference
**Date discovered:** 2025-12
**Date processed:** 2025-12
**Discovery window:** 2025-W50
**Discovery source:** manual / uploaded file
**Discovery query:** mitochondrial supplements
**Status:** background_only
**Primary pathway:** P5
**Genotype/model tag:** non-WWOX-specific / review / T3 indirect
**Transferability:** T3 indirect
**clinical relevance:** background only
**Claim links:** 009 supportive only
**Working Model impact:** none
**Report mentions:** metabolic support sessions
**Next action:** archive
**Flags:** background only
**Note:** Useful for supplement safety/dosing context, not causal WWOX logic.

---

## LIT-010
**Short title:** Druck/Aqeilan 2026 mutational signatures
**Authors:** Druck / Aqeilan / Aldaz et al.
**Year:** 2026
**Source type:** mechanistic / oncology-adjacent
**Journal/source:** Genes, Chromosomes and Cancer
**Identifier type:** PMID
**Identifier value:** PMID 41562193 · PMCID PMC12820907 · DOI 10.1002/gcc.70106
**Evidence depth:** full text reviewed (2026-06-28)
**Date discovered:** 2026-03-27
**Date processed:** 2026-03-27
**Discovery window:** 2026-W13
**Discovery source:** PubMed search
**Discovery query:** WWOX gene 2026
**Status:** background_only
**Primary pathway:** P7 / WWOX broader biology
**Genotype/model tag:** mouse / FHIT+WWOX loss / non-CNS / T3
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** background only
**Report mentions:** 2026-03-27 flash report; weekly report 2026-03-29
**Next action:** none
**Flags:** none
**Note:** Genomic instability / DNA damage response. No operative function for the reference genotype. Full text PMC recuperato 2026-06-28 (dossier staging/dossier_41562193.md). Decisione background_only riconfermata.

---

## Papers from Scholar pre-scan — 2026-03-28 run

---

## LIT-0011
**Short title:** Obeid 2026 neuron-specific gene therapy
**Authors:** Obeid et al.
**Year:** 2026
**Source type:** preclinical gene therapy study (peer-reviewed; era preprint bioRxiv)
**Journal/source:** Molecular Therapy Advances (OMTA — *Mol Ther Adv*) 2026;34 (Cell Press)
**Identifier type:** Journal (published) — era Preprint DOI
**Identifier value:** OMTA vol 34 (2026) — **identificatori confermati:** PMID 42422765 / PMCID PMC13343157 / DOI 10.1016/j.omta.2026.201791, *Mol Ther Adv* 2026;34(3):201791 (aggiornato preprint→published 2026-07-04, CC-2026-07-03-001; identificatori confermati e allineati a [[paper_registry_current#PAPER 011]] in `BATCH_20260922_BIBLIO`)
**Date discovered:** 2026-03-28
**Date screened:** 2026-03-28
**Date processed:** 2026-03-28
**Date last touched:** 2026-03-29
**Discovery source:** scholar_pre_scan_triage → full text reviewed 2026-03-29
**Priority:** high
**Quality status:** provisional-preprint
**Filter decision:** in
**Model type:** preclinical murine — Wwox-null severo
**Species:** mouse
**WWOX alteration type:** Wwox-null full KO
**Developmental stage:** neonatal ICV delivery
**Directness to the reference genotype:** moderate (full KO ≠ the reference genotype; design principles trasferibili)
**Transferability:** T2
**Over-inference risk:** moderate
**Clinical translation status:** mechanistically informative — P7 design principles
**Primary pathway:** P7
**Secondary pathway:** P4 / P6 indiretto
**clinical relevance:** HIGH
**Practical status:** strengthens rationale only
**Final decision label:** P7 design-principle paper
**Claim links:** 011
**Working Model impact:** BLOCCO 2 integrated; gene therapy context updated; gliosi come downstream di disfunzione neuronale (P6 ridimensionato)
**Status:** integrated
**Next action:** none — chiuso
**Flags:** preprint flag

---

## LIT-0012
**Short title:** Sapuppo 2026 WOREE syndrome plus
**Authors:** Sapuppo et al.
**Year:** 2026
**Source type:** human case report (peer-reviewed; versione published del preprint)
**Journal/source:** Current Issues in Molecular Biology 2026;48(5):449 (MDPI)
**Identifier type:** PMID / PMCID / DOI
**Identifier value:** PMID 42193054 · PMCID PMC13205014 · DOI 10.3390/cimb48050449
**Date discovered:** 2026-03-28
**Date screened:** 2026-03-28
**Date processed:** 2026-03-28
**Date last touched:** 2026-06-28
**Discovery source:** scholar_pre_scan_triage → full text reviewed 2026-03-29
**Priority:** medium-high
**Quality status:** provisional-preprint
**Filter decision:** in
**Model type:** single human case
**Species:** human
**WWOX alteration type:** exon 6–7 deletion + exon 8 frameshift
**Developmental stage:** neonatal-fatal
**Directness to the reference genotype:** high phenotypic / low therapeutic
**Transferability:** T1 phenotypic
**Over-inference risk:** high
**Clinical translation status:** descriptive only
**Primary pathway:** clinical spectrum / genotype-phenotype
**Secondary pathway:** none operative
**clinical relevance:** MODERATE
**Practical status:** supports spectrum reasoning only
**Final decision label:** phenotype refinement
**Claim links:** 012
**Working Model impact:** BLOCCO 2 integrated; EEG priority note added; MRI precoce normale non esclude rete severa
**Status:** integrated
**Next action:** none — chiuso
**Flags:** none (2026-06-28: identifier preprint normalizzato a published peer-reviewed; flag preprint rimosso)

---

## LIT-0013
**Short title:** Turkish DEE cohort 2025
**Authors:** Sunnetci-Akkoyunlu et al.
**Year:** 2025
**Source type:** human cohort study
**Journal/source:** Genes
**Identifier type:** PMID
**Identifier value:** 41153369
**Date discovered:** 2026-03-28
**Date screened:** 2026-03-28
**Date processed:** 2026-03-28
**Date last touched:** 2026-03-28
**Discovery source:** scholar_pre_scan_triage
**Priority:** low-medium
**Quality status:** acceptable
**Filter decision:** in
**Model type:** single-center DEE cohort
**Species:** human
**WWOX alteration type:** homozygous p.L239R in two siblings
**Developmental stage:** infantile DEE
**Directness to the reference genotype:** contextual
**Transferability:** T1 contextual
**Over-inference risk:** moderate
**Clinical translation status:** supportive descriptive context
**Primary pathway:** clinical spectrum / cohort context
**Secondary pathway:** weak P1 / weak P7 contextual
**clinical relevance:** LOW-MODERATE
**Practical status:** background-to-supportive
**Final decision label:** supportive context
**Claim links:** none
**Working Model impact:** no update required
**Status:** processed
**Next action:** no further action
**Flags:** low-yield flag
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-41153369-01` (tables read for the first time; earlier `FTR-20260921-41153369-01`, partial); manifest `deepdive_manifests/PMID41153369.json`; see `CC-20261003W3-A-L239R-01`

---

## New papers — autonomous PubMed search 2026-03-29

---

## LIT-0014
**Short title:** Gao 2025 WWOX-DEE genotype-phenotype cohort
**Authors:** Gao K, Riley LG, Raubenheimer J, Oliver KL, Wykes AD, Mentz J, Lee SJ, Pinner J, Cardamone M, Scheffer I, Gold WA
**Year:** 2025
**Source type:** cohort study / parent-reported registry
**Journal/source:** Neurology
**Identifier type:** PMID / DOI
**Identifier value:** PMID 40875931 / DOI 10.1212/WNL.0000000000213883
**Date discovered:** 2026-03-29
**Date screened:** 2026-03-29
**Date processed:** 2026-03-29
**Date last touched:** 2026-03-29
**Discovery source:** PubMed autonomous search — query "WWOX DEE seizure pediatric"
**Priority:** HIGH
**Quality status:** peer-reviewed — Neurology
**Filter decision:** in
**Model type:** human cohort — parent-reported registry
**Species:** human
**WWOX alteration type:** biallelic — N/N / N/M / M/M
**Developmental stage:** pediatric DEE
**Directness to the reference genotype:** HIGH — genotipo, spettro, natural history
**Transferability:** T1
**Over-inference risk:** moderate (survey parentale; bias sopravvivenza)
**Clinical translation status:** genotype-aware risk stratification
**Primary pathway:** clinical spectrum / genotype-phenotype / P2 / respiratory
**Secondary pathway:** none operative aggiuntivo
**clinical relevance:** HIGH
**Practical status:** risk stratification e natural history context
**Final decision label:** largest human cohort; genotype-aware stratification
**Claim links:** 013
**Working Model impact:** BLOCCO 2 in observation (CLAIM 013); genotype class N/M aggiunta a Identity section; surveillance respiratoria e oftalmica rafforzate; gene therapy rationale rafforzato (partial restoration sufficiente)
**Evidence depth:** full text reviewed (PDF fornito dall'operatore)
**Full text status:** found
**Status:** integrated
**Next action:** nessuno — CLAIM 013 in attesa validazione dell'operatore
**Flags:** high value human / review trigger (CLAIM 013 pending)
**Note:** 50 individui, 45 famiglie. Solo 3 associazioni FDR-significative: ipertonia (p=0.003), crisi (p=0.016), respiratorio (p=0.020) in N/N vs N/M e M/M. Q230P in 2 individui. Case ID 11 (N/M: null+Q230P) unico deceduto — causa sconosciuta. the reference genotype verosimilmente N/M.

---

## LIT-0015
**Short title:** Teplyshova 2024 adult WWOX-DEE
**Authors:** Teplyshova A, Sharkov A
**Year:** 2024
**Source type:** case report
**Journal/source:** Frontiers in Genetics
**Identifier type:** PMID / PMC / DOI
**Identifier value:** PMID 39507621 / PMC11537890 / DOI 10.3389/fgene.2024.1477466
**Date discovered:** 2026-03-29
**Date screened:** 2026-03-29
**Date processed:** 2026-03-29
**Date last touched:** 2026-03-29
**Discovery source:** PubMed autonomous search — query "WWOX DEE seizure pediatric"
**Priority:** medium
**Quality status:** acceptable — Frontiers in Genetics
**Filter decision:** in
**Model type:** single human case
**Species:** human
**WWOX alteration type:** omozigote p.Thr12Met (N-terminal)
**Developmental stage:** infantile onset → adulto (40 anni)
**Directness to the reference genotype:** moderate — genotipo diverso; utile per natural history
**Transferability:** T1 phenotypic
**Over-inference risk:** alto — paziente singolo, genotipo diverso
**Clinical translation status:** natural history long-span
**Primary pathway:** clinical spectrum / natural history
**Secondary pathway:** P4 long-term
**clinical relevance:** MODERATE
**Practical status:** natural history context only
**Final decision label:** natural history long-span support
**Claim links:** none
**Working Model impact:** BLOCCO 2 — supporto contestuale; nessun update BLOCCO 1
**Evidence depth:** full text reviewed (PMC open access)
**Full text status:** found — PMC11537890
**Status:** integrated
**Next action:** none
**Flags:** none
**Note:** Primo adulto documentato con WWOX-DEE (40 anni). Sopravvivenza possibile ma con progressione: epilessia → regressione motoria adolescenza → complicanze respiratorie severe. Genotipo omozigote missense N-terminal, diverso dal genotipo di riferimento.

---

## LIT-0016
**Short title:** You 2024 vigabatrin case WWOX
**Authors:** You Y, Wu W, Du Y, Hu J, Li B
**Year:** 2024
**Source type:** case report
**Journal/source:** Molecular Genetics & Genomic Medicine
**Identifier type:** PMID / PMC / DOI
**Identifier value:** PMID 39101447 / PMC11298992 / DOI 10.1002/mgg3.2500
**Date discovered:** 2026-03-29
**Date screened:** 2026-03-29
**Date processed:** 2026-03-29
**Date last touched:** 2026-03-29
**Discovery source:** PubMed autonomous search — query "WWOX DEE seizure pediatric"
**Priority:** HIGH — safety-relevant
**Quality status:** acceptable
**Filter decision:** in
**Model type:** single human case
**Species:** human
**WWOX alteration type:** omozigote splice site c.172+1G>C (null/null funzionale; proteina troncata da minigene)
**Developmental stage:** infantile (13 mesi)
**Directness to the reference genotype:** moderate — genotipo null/null ≠ the reference genotype compound het
**Transferability:** T1 (umano) — genotipo ≠ the reference genotype
**Over-inference risk:** alto — singolo caso, follow-up brevissimo, no MRI VABAM
**Clinical translation status:** tensione evidence su vigabatrin
**Primary pathway:** P2 — safety / AED
**clinical relevance:** MODERATE-HIGH — safety-relevant
**Practical status:** conflicting evidence — non pro-vigabatrin
**Final decision label:** tensione evidence vigabatrin
**Claim links:** 001 (conflicting evidence trigger)
**Working Model impact:** CLAIM 001 → conflicting evidence; posizione clinica generale su vigabatrin invariata
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-39101447-01`; manifest `deepdive_manifests/PMID39101447.json`
**Full text status:** found — PMC11298992
**Status:** integrated
**Next action:** none
**Flags:** safety / conflicting evidence
**Note:** VGB 200 mg/kg/die in 1 caso null/null → riduzione crisi; no MRI controllo VABAM; non invalida Choi 2026. Genotipo null/null ≠ the reference genotype (compound het missense + splice). Follow-up a 13 mesi.

---

## LIT-0017
**Short title:** Chong 2023 WOREE spectrum KD Q230P
**Authors:** Chong SC, Cao Y et al.
**Year:** 2023
**Source type:** case series
**Journal/source:** American Journal of Medical Genetics Part A
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36537114 / DOI 10.1002/ajmg.a.63074
**Date discovered:** 2026-03-29
**Date screened:** 2026-03-29
**Date processed:** 2026-03-29
**Date last touched:** 2026-03-29
**Discovery source:** PubMed autonomous search + Scholar Gateway full text retrieval
**Priority:** medium-high
**Quality status:** peer-reviewed — AJMG
**Filter decision:** in
**Model type:** case series — 5 pazienti WOREE (tutti null/null)
**Species:** human
**WWOX alteration type:** null/null (SNV splice + delezioni esoni)
**Developmental stage:** pediatrico — media 1 mese esordio crisi
**Directness to the reference genotype:** moderate — genotipo null/null ≠ the reference genotype; KD e meccanismo Q230P rilevanti
**Transferability:** T1 per KD e fenotipi clinici; T2 per meccanismi molecolari
**Over-inference risk:** moderato
**Clinical translation status:** KD support + Q230P mechanism + spectrum expansion
**Primary pathway:** P1 clinical / KD / P3 (Q230P SDR)
**Secondary pathway:** P5 (lattato P4)
**clinical relevance:** MODERATE-HIGH
**Practical status:** supporto contestuale
**Final decision label:** KD support + Q230P contextual mechanism
**Claim links:** 001 (dato misto) / 009 (supporto P5) / 013 (supporto contestuale)
**Working Model impact:** BLOCCO 2 — rafforza razionale KD; aggiunge meccanismo Q230P (instabilità proteica post-traduzionale); piccolo supporto P5 (lattato); valutazione visiva indicata (4/5 con deficit visivo)
**Evidence depth:** partial full text (Scholar Gateway, 47 chunk)
**Full text status:** not open access — partial recovery via Scholar Gateway
**Status:** integrated
**Next action:** none — se full text disponibile in futuro, upgrade completo
**Flags:** non open access
**Note:** KD associata a miglioramento crisi in 3/5 (P1, P2, P4). Raccomandazione: KD should be considered con cautela. Q230P/SDR: trascritto normale, proteina assente/instabile → compatibile con funzione residua parziale. Lattato lievemente elevato P4. Pancreatite ricorrente e sordità neurosensoriale come feature espansive. 2/5 deceduti a 2 anni.

---

## LIT-0018
**Short title:** Oliver 2023 WWOX-DEE epilettologia mortalità
**Authors:** Oliver KL, Trivisano M, Mandelstam SA, et al.
**Year:** 2023
**Source type:** multicenter cohort study
**Journal/source:** Epilepsia
**Identifier type:** PMID / PMC / DOI
**Identifier value:** PMID 36779245 / PMC10952634 / DOI 10.1111/epi.17542
**Date discovered:** 2026-03-29
**Date screened:** 2026-03-29
**Date processed:** 2026-03-29 (parziale — abstract + Scholar Gateway)
**Date last touched:** 2026-03-29
**Discovery source:** Scholar Gateway — emerso durante ricerca Chong 2023
**Priority:** HIGH — alta priorità prossima sessione
**Quality status:** peer-reviewed — Epilepsia / open access PMC
**Filter decision:** in
**Model type:** multicenter cohort — 13 pazienti, 12 famiglie, 5 centri
**Species:** human
**WWOX alteration type:** biallelic variants — N/N / N/M / M/M
**Developmental stage:** pediatrico / follow-up esteso
**Directness to the reference genotype:** HIGH
**Transferability:** T1
**Over-inference risk:** basso
**Clinical translation status:** sopravvivenza, epilettologia, natural history
**Primary pathway:** clinical spectrum / survival analysis / natural history
**Secondary pathway:** EEG pattern / MRI
**clinical relevance:** HIGH
**Practical status:** full text da estrarre nella prossima sessione
**Final decision label:** alta priorità — full text retrieval
**Claim links:** pending
**Working Model impact:** pending — potenzialmente alto (sopravvivenza, missense vs non-missense)
**Evidence depth:** abstract + Scholar Gateway frammenti
**Full text status:** found — PMC10952634 (open access)
**Status:** filtered_in
**Status note:** queued per full text
**Next action:** full text retrieval PMC10952634 — PRIMA PRIORITÀ PROSSIMA SESSIONE
**Flags:** high value human / review trigger / high priority
**Note:** Key finding (da abstract): presenza ≥1 missense aumenta sopravvivenza 5 anni da <50% a >75% (p=0.0085). Tipi crisi: focali 85%, spasmi 77%, toniche 69%. EEG: slow background, multifocal discharges frontali/temporo-occipitali. MRI: frontotemporal atrophy, hippocampal atrophy, thin corpus callosum. Sindromi: EIDEE 8/13, IESS 2, EIMFS 2. Distonia 11/13. Mortalità 35% — respiratorio causa principale.

---

## LIT-0019
**Short title:** Baryła 2025 WWOX-HIF1A ratio metabolism
**Authors:** Baryła I, Hammouz RY, Maciejek K, Bednarek AK
**Year:** 2025
**Source type:** research article
**Journal/source:** Biology (Basel)
**Identifier type:** PMID / PMC / DOI
**Identifier value:** PMID 41007296 / PMC12467568 / DOI 10.3390/biology14091151
**Date discovered:** 2026-03-29
**Date screened:** 2026-03-29
**Date processed:** 2026-03-29 (abstract-level)
**Date last touched:** 2026-03-29
**Discovery source:** PubMed autonomous search
**Priority:** low
**Quality status:** acceptable
**Filter decision:** in — background
**Model type:** bioinformatic / cancer context
**Species:** human (cancer datasets)
**WWOX alteration type:** WWOX expression analysis in multiple cancers
**Developmental stage:** adult / cancer
**Directness to the reference genotype:** very low — oncologico, non CNS pediatrico
**Transferability:** T3
**Over-inference risk:** alto
**Clinical translation status:** background conceptual only
**Primary pathway:** P5 — HIF1A / metabolismo
**clinical relevance:** BACKGROUND — rafforza concettualmente CLAIM 009
**Practical status:** background
**Final decision label:** background only
**Claim links:** 009 (supporto secondario)
**Working Model impact:** BLOCCO 2 — supporto secondario a CLAIM 009
**Evidence depth:** abstract-only
**Full text status:** found — PMC disponibile; lettura non prioritaria
**Status:** background_only
**Next action:** none
**Flags:** background only
**Note:** Stessi autori di Baryła 2022. WWOX sequestra HIF1A nel citoplasma; perdita di WWOX → HIF1A libero → shift glicolitico. Rafforza concettualmente il razionale per KD.

---

## LIT-0020
**Short title:** Yang 2025 WWOX cancer mechanisms review
**Authors:** Yang H, Liao B, Zhao J, Li Y
**Year:** 2025
**Source type:** review
**Journal/source:** Cancers (Basel)
**Identifier type:** PMID / PMC / DOI
**Identifier value:** PMID 41228229 / PMC12610808 / DOI 10.3390/cancers17213435
**Date discovered:** 2026-03-29
**Date screened:** 2026-03-29
**Date processed:** 2026-03-29 (abstract-only)
**Date last touched:** 2026-03-29
**Discovery source:** PubMed autonomous search
**Priority:** low-medium
**Quality status:** acceptable
**Filter decision:** in — queued
**Model type:** review / oncologico
**Species:** review / mixed
**WWOX alteration type:** WWOX in cancers — meccanismi oncosoppressori
**Developmental stage:** adulto / cancer
**Directness to the reference genotype:** very low — oncologico
**Transferability:** T3
**Over-inference risk:** alto
**Clinical translation status:** background conceptual — HIF1A, PI3K/AKT, NF-κB, Hippo/YAP
**Primary pathway:** P3 / P5 / P6 (indiretto)
**clinical relevance:** BACKGROUND — meccanicisticamente utile per completare P3/P5/P6
**Practical status:** queued per lettura media priorità
**Final decision label:** background indirect mechanistic support
**Claim links:** pending — eventuale supporto 009 e framework P3
**Working Model impact:** nessuno immediato
**Evidence depth:** abstract-only
**Full text status:** found — PMC12610808
**Status:** filtered_in
**Status note:** queued per lettura media priorità
**Next action:** full text reading — media priorità (dopo Oliver 2023)
**Flags:** none
**Note:** Pathway WWOX in cancro: HIF1A, PI3K/AKT, NF-κB, JAK-STAT, Hippo/YAP. Utile per framework indiretto P3/P5/P6.

---

## LIT-0021
**Short title:** Cheng 2020 GSK3β seizure axis
**Authors:** Cheng et al.
**Year:** 2020
**Source type:** murine mechanistic study
**Journal/source:** Acta Neuropathol Commun
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32000863 / DOI 10.1186/s40478-020-0883-3
**Date discovered:** 2026-04-10
**Date processed:** 2026-04-10
**Discovery window:** bootstrap-v1.0
**Discovery source:** corpus bootstrap review
**Discovery query:** corpus paper 93
**Status:** processed
**Primary pathway:** P3 / P4 / emerging GSK3β
**Genotype/model tag:** mouse / Wwox-null / severe developmental model / T2
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 015 / 016
**Working Model impact:** structural interpretation strengthened; no BLOCCO 1 change
**Report mentions:** bootstrap
**Next action:** prioritize full text extraction details
**Flags:** review trigger / full text needed
**Note:** Key paper for structural substrate and GSK3β node.

---

## LIT-0022
**Short title:** Iacomino 2020 migration
**Authors:** Iacomino et al.
**Year:** 2020
**Source type:** developmental translational study
**Journal/source:** Frontiers in Neuroscience
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32581702 / DOI 10.3389/fnins.2020.00644
**Date discovered:** 2026-04-10
**Date processed:** 2026-04-10
**Discovery window:** bootstrap-v1.0
**Discovery source:** corpus bootstrap review
**Discovery query:** corpus paper 97
**Status:** processed
**Primary pathway:** P3
**Genotype/model tag:** fetal human tissue + rat + hNPC / developmental deficiency / T2
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 014 / 015
**Working Model impact:** prenatal structure axis strengthened
**Report mentions:** bootstrap
**Next action:** full text extraction priority
**Flags:** high value human / full text needed
**Note:** Core migration/cortical layering paper.

---

## LIT-0023
**Short title:** Tochigi 2019 rat lde/lde
**Authors:** Tochigi et al.
**Year:** 2019
**Metadata correction (BATCH_20260806_002):** previously recorded as *"Kumada et al."*; the author is **Tochigi**. The paired `PAPER 021` record also carried an invented title naming *lissencephaly*, corrected in the same batch. Source: complete full-text read, receipt `FTR-20260806-31340538-01`.
**Source type:** rat developmental study
**Journal/source:** IJMS
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31340538 / DOI 10.3390/ijms20143596
**Date discovered:** 2026-04-10
**Date processed:** 2026-04-10
**Discovery window:** bootstrap-v1.0
**Discovery source:** corpus bootstrap review
**Discovery query:** corpus paper 163
**Status:** processed
**Primary pathway:** P4 / P3
**Genotype/model tag:** rat lde/lde / Wwox-deficient / T2
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 014 / 015
**Working Model impact:** structural + myelin axis support
**Report mentions:** bootstrap
**Next action:** none
**Flags:** none
**Note:** Key support for prenatal cortex hypomyelination axis.

---

## LIT-0024
**Short title:** Kośla 2019 hNPC differentiation
**Authors:** Kośla et al.
**Year:** 2019
**Source type:** human cell study
**Journal/source:** Frontiers in Cellular Neuroscience
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31543760 / DOI 10.3389/fncel.2019.00391
**Date discovered:** 2026-04-10
**Date processed:** 2026-04-10
**Discovery window:** bootstrap-v1.0
**Discovery source:** corpus bootstrap review
**Discovery query:** corpus paper 106
**Status:** processed
**Primary pathway:** P3
**Genotype/model tag:** human neural progenitor cells / differentiation / T2
**Transferability:** T2
**clinical relevance:** MODERATE-HIGH
**Claim links:** 014
**Working Model impact:** developmental support only
**Report mentions:** bootstrap
**Next action:** none
**Flags:** none
**Note:** Supports neuronal differentiation and developmental pathway framing.

---

## LIT-0025
**Short title:** Baryła 2022 IJMS WWOX/HIF1A axis
**Authors:** Baryła et al.
**Year:** 2022
**Source type:** mechanistic study
**Journal/source:** IJMS
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35328751 / DOI 10.3390/ijms23063326
**Date discovered:** 2026-04-10
**Date processed:** 2026-04-10
**Discovery window:** bootstrap-v1.0
**Discovery source:** corpus bootstrap review
**Discovery query:** corpus paper 64
**Status:** processed
**Primary pathway:** P5
**Genotype/model tag:** mixed / metabolic axis / T2 conceptual
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Claim links:** 009
**Working Model impact:** metabolic axis strengthened only
**Report mentions:** bootstrap
**Next action:** none
**Flags:** none
**Note:** Focused HIF1A-axis paper complementing Baryła 2022 review.

---

## LIT-0026
**Short title:** Abu-Remaileh 2014 HIF1A glucose metabolism
**Authors:** Abu-Remaileh et al.
**Year:** 2014
**Source type:** mechanistic study
**Journal/source:** Cell Death and Differentiation
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25012504 / DOI 10.1038/cdd.2014.95
**Date discovered:** 2026-04-10
**Date processed:** 2026-04-10
**Discovery window:** bootstrap-v1.0
**Discovery source:** corpus bootstrap review
**Discovery query:** corpus paper 144
**Status:** processed
**Primary pathway:** P5
**Genotype/model tag:** WWOX loss/downregulation / metabolic models / T2 conceptual
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Claim links:** 009
**Working Model impact:** strengthens HIF1A metabolic rationale
**Report mentions:** bootstrap
**Next action:** none
**Flags:** none
**Note:** Foundational HIF1A metabolic paper.

---

## LIT-0027
**Short title:** Piard 2019 EJPN exon 6 / Q230P
**Authors:** Piard et al.
**Year:** 2019
**Source type:** human case series
**Journal/source:** Eur J Paediatr Neurol
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30853297 / DOI 10.1016/j.ejpn.2019.02.003
**Date discovered:** 2026-04-10
**Date processed:** 2026-04-10
**Discovery window:** bootstrap-v1.0
**Discovery source:** corpus bootstrap review
**Discovery query:** corpus paper 151
**Status:** processed
**Primary pathway:** genotype-phenotype / exon 6 / Q230P logic
**Genotype/model tag:** human / severe early infantile encephalopathy / T1
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** 018 / 019
**Working Model impact:** genotype logic strengthened; no BLOCCO 1 change
**Report mentions:** bootstrap
**Next action:** full text desirable
**Flags:** high value human / full text needed
**Note:** Key for exon 6 skipping and Q230P compound-context interpretation.


## LIT-0205
**Short title:** Cell Commun Signal 2024 WWOX/TRAF2 switch
**Authors:** Chang et al.
**Year:** 2024
**Source type:** mechanistic stress-signaling study
**Journal/source:** Cell Communication and Signaling
**Identifier type:** PMID / DOI / PMC
**Identifier value:** PMID 39420317 / DOI 10.1186/s12964-024-01866-6 / PMC11487720
**Date discovered:** 2026-04-12
**Date screened:** 2026-04-18
**Date processed:** 2026-04-18
**Date last touched:** 2026-04-18
**Discovery source:** phase-2 corpus alignment → deep dive in current session
**Priority:** medium-low
**Quality status:** acceptable — peer-reviewed / open access
**Filter decision:** in
**Model type:** mechanistic cellular stress paradigm
**Species:** cell systems
**WWOX alteration type:** WWOX/TRAF2/TRADD/p53 complex dynamics under UV / cold shock
**Developmental stage:** non-developmental direct
**Directness to the reference genotype:** very low
**Transferability:** T3 mechanistic / indirect
**Over-inference risk:** high
**Clinical translation status:** paper-level mechanistic support only
**Primary pathway:** signaling organization / stress-contingent partner switching
**Secondary pathway:** weak support for CLAIM 028
**clinical relevance:** VERY LOW direct / LOW architectural
**Practical status:** processed — no structural propagation
**Final decision label:** secondary support only
**Claim links:** 028 supportive only
**Working Model impact:** none
**Evidence depth:** full text reviewed (PMC open access)
**Full text status:** found — PMC11487720
**Status:** processed
**Next action:** none
**Flags:** low-yield flag / context-specific paradigm / high over-inference risk
**Note:** Useful for WWOX-dependent nuclear relocalization of TRAF2 and context-sensitive partner-switching logic, but too idiosyncratic (UV/cold-shock/BCD paradigm) to justify new claim or working-model propagation.

## Papers excluded at baseline screening — 2026-03-27 run

---

## LIT-EX-001
**Short title:** Wang 2026 ferroptosis ALI
**Authors:** Wang et al.
**Year:** 2025/2026
**Source type:** murine mechanistic study
**Journal/source:** International Immunopharmacology
**Identifier type:** PMID
**Identifier value:** 41443103
**Date discovered:** 2026-03-27
**Status:** filtered_out
**Filter reason:** WWOX in lung epithelial ferroptosis — non-CNS, non-pediatric, non-WWOX-LoF neurodevelopmental
**Transferability:** T4
**clinical relevance:** VERY LOW
**Note:** Background only. No relevance for the reference genotype.

---

## LIT-EX-002
**Short title:** Yadav 2026 fusion genes cancer
**Authors:** Yadav et al.
**Year:** 2026
**Source type:** oncology RNA-seq
**Journal/source:** Nucleosides Nucleotides Nucleic Acids
**Identifier type:** PMID
**Identifier value:** 41661231
**Date discovered:** 2026-03-27
**Status:** filtered_out
**Filter reason:** WWOX_FUT1 fusion gene in liver/oral/ovarian cancer — irrelevant to WOREE / neurodevelopmental
**Transferability:** T4
**clinical relevance:** VERY LOW
**Note:** Excluded.

---

## LIT-EX-003
**Short title:** Corona 2026 MS pharmacogenomics
**Authors:** Corona et al.
**Year:** 2026
**Source type:** pharmacogenomics GWAS
**Journal/source:** Multiple Sclerosis
**Identifier type:** PMID
**Identifier value:** 41776383
**Date discovered:** 2026-03-27
**Status:** filtered_out
**Filter reason:** WWOX as marginal GWAS signal for glatiramer acetate response in MS — not WWOX-LoF, not pediatric, not neurodevelopmental
**Transferability:** T4
**clinical relevance:** VERY LOW
**Note:** Excluded.

---

## LIT-EX-004
**Short title:** Shenoy 2026 COVID PASC GWAS
**Authors:** Shenoy et al.
**Year:** 2026
**Source type:** GWAS / genomic epidemiology
**Journal/source:** Frontiers in Genetics
**Identifier type:** PMID
**Identifier value:** 41561974
**Date discovered:** 2026-03-27
**Status:** filtered_out
**Filter reason:** WWOX as marginal GWAS candidate in COVID-19/PASC — not WWOX-LoF, not pediatric neurodevelopmental
**Transferability:** T4
**clinical relevance:** VERY LOW
**Note:** Excluded.

---

## LIT-EX-005
**Short title:** Su 2026 Bcl-XL lysosome
**Authors:** Su et al.
**Year:** 2026
**Source type:** cell biology / oncology
**Journal/source:** Cells
**Identifier type:** PMID
**Identifier value:** 41677633
**Date discovered:** 2026-03-27
**Status:** superseded
**Superseded by:** [[literature_tracking_log_current#LIT-0165]] (same PMID, promoted). The pointer was written into `Status` by `CC-20261003W3-B-REGISTRY-01` and moved to this line by `BATCH_20261003_002` after Phase 5 returned `INVALID_LIT_STATUS`: the vocabulary takes the bare value, and nothing was dropped.
**Filter reason:** 🔴 **Duplicate identity and an outdated rationale, corrected 2026-10-03 (`CC-20261003W3-B-REGISTRY-01`).** The same PMID is also carried by [[literature_tracking_log_current#LIT-0165]], which is the record promoted to [[paper_registry_current#PAPER 144]]; this one is kept as history and is no longer the live record. On the substance: the cell systems are indeed non-CNS (MEF, HeLa, SCC-15), but the paper is NOT only a cancer-apoptosis result - two of its endpoints (mitochondrial membrane potential, ROS) are measured on a constitutive `Wwox` null versus wild type, and in that comparison WWOX loss is PROTECTIVE under serum starvation. Read on 2026-10-03 (`partial_fulltext_read`) (integrator amendment, `BATCH_20261003_002`): receipt `FTR-20261003-41677633-02`, dossier `research/fulltext_dossiers/PMID41677633.md`
**Transferability:** T4
**clinical relevance:** VERY LOW
**Note:** Excluded. Conceptually interesting for apoptosis/redox but not translatable.

---

## LIT-EX-006
**Short title:** Kılıç 2026 DRE genetics cohort
**Authors:** Kılıç et al.
**Year:** 2026
**Source type:** clinical cohort / genetics
**Journal/source:** Neurology India
**Identifier type:** PMID
**Identifier value:** 41510857
**Date discovered:** 2026-03-27
**Status:** background_only
**Filter reason:** WWOX listed among pathogenic DRE genes in WES cohort — useful as clinical context but no WWOX-specific data
**Transferability:** T3 contextual
**clinical relevance:** LOW
**Note:** Confirms WWOX as recognized DRE gene in WES panels. No actionable WWOX-specific information.

---

## Tracking log rules

1. Every paper entering the discovery pipeline must receive a LIT record before processing
2. Excluded papers must be logged with filter reason — not silently dropped
3. Same PMID/DOI: update existing record only
4. Preprint to publication: upgrade single record, note publication date and final identifier
5. Discovery history: if a paper is rediscovered, add the new discovery event to its record

---

## Weekly tracker — 2026-03-27 (first operational run)

| Metric | Count |
|--------|-------|
| Papers screened | 8 |
| Filtered in (processed) | 2 (LIT-003, LIT-010) |
| Filtered out | 5 (LIT-EX-001 to LIT-EX-005) |
| Background only | 1 (LIT-EX-006) |
| Baseline records pre-loaded | 9 (LIT-001 to LIT-009) |
| Safety signals | 0 new (LIT-003 already integrated) |
| Claims added | 0 new (LIT-010 pending) |
| Duplicates skipped | 0 |
| Next bibliography mine | LIT-001 (Steinberg) / LIT-005 (Repudi EMBO) / LIT-010 (Druck) |

---

## Weekly tracker — 2026-03-28 (Scholar pre-scan triage)

| Metric | Count |
|--------|-------|
| Papers from Scholar pre-scan | 3 |
| Filtered in (processed) | 3 (LIT-0011, LIT-0012, LIT-0013) |
| Filtered out | 0 |
| Safety signals | 0 |
| Claims added | 2 (CLAIM 011, CLAIM 012) |
| Reviews triggered | 1 (P7 wording — pending full Obeid extraction) |
| Direct updates | 0 |
| Working Model BLOCCO 1 changes | 0 |
| Duplicates skipped | 0 |
| Next actions | Full extraction Obeid 2026 / normalize Sapuppo identifier / normalize Turkish cohort identifier |

---

## Weekly tracker — 2026-03-29 (autonomous PubMed search + full text pass)

| Metric | Count |
|--------|-------|
| Papers from autonomous PubMed search | 8 nuovi + deduplication su già noti |
| Papers new and filtered in | 7 (LIT-0014 to LIT-0020) |
| Papers already known / duplicates | 10 (già in registro) |
| Papers filtered out (questa sessione) | 0 nuovi |
| Full texts reviewed | 4 (Gao 2025, Teplyshova 2024, You 2024, Obeid 2026 chiuso, Sapuppo 2026 chiuso) |
| Full texts partial (Scholar Gateway) | 1 (Chong 2023) |
| Safety signals nuovi | 0 nuovi (CLAIM 001 aggiornato a conflicting evidence) |
| Claims aggiunti | 1 (CLAIM 013 — in observation, the operator validation pending) |
| Claims aggiornati | 2 (CLAIM 001 → conflicting evidence; CLAIM 011/012 → integrated) |
| Working Model BLOCCO 1 changes | 0 operative (raffinamenti proposti in attesa validazione) |
| Working Model BLOCCO 2 changes | Major enrichment |
| Duplicates skipped | 10 |
| Safety override | Nessuno |
| Tier shift | Nessuno |
| Next priority | Oliver 2023 full text (PMC10952634) — PRIMA PRIORITÀ |

## LIT-0028
**Short title:** corpus paper 1
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34359949 / DOI 10.3390/cells10071781
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 1
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX and Its Binding Proteins in Neurodegeneration

---

## LIT-0029
**Short title:** corpus paper 2
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36271927 / DOI 10.1007/s00109-022-02265-5
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 2
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — processed 2026-10-03 (`FTR-20261003-36271927-01`) and recorded as [[paper_registry_current#PAPER 154]] by `CC-20261003W4-A-REGISTRY-01`; Baryła I et al. 2022, *J Mol Med* 100:1691; narrative review; earlier partial read `FTR-20260921-36271927-01`; the placeholder fields above are kept as history
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX and metabolic regulation in normal and pathological conditions

---

## LIT-0030
**Short title:** Steinberg 2021 — atlante dei modelli WWOX
**Authors:** Steinberg DJ, Aqeilan RI
**Year:** 2021
**Source type:** review narrativa / atlante di modelli — nessuna coorte sperimentale nuova
**Journal/source:** *Cells* 10(11):3082
**Identifier type:** PMID / PMCID / DOI
**Identifier value:** PMID 34831305 / PMCID PMC8623516 / DOI 10.3390/cells10113082
**Evidence depth:** complete_fulltext_read (2026-08-10) — receipt `FTR-20260810-34831305-03`, manifest `deepdive_manifests/PMID34831305.json`
**Registry record:** [[paper_registry_current#PAPER 063]] (promosso da `CORPUS-STUB-003`, BATCH_20260810_005)
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 3
**Status:** processed
**Primary pathway:** P3 / P4 / P7 — architettura causale fra modelli
**Genotype/model tag:** trasversale (ratto, topo globale/ipomorfo/condizionale/cell-targeted, organoidi, tessuto umano); nessun allele proprio
**Transferability:** MODERATE per l'architettura causale, LOW per la traduzione quantitativa
**clinical relevance:** HIGH come mappa di ricerca, BACKGROUND come evidenza di claim
**Claim links:** none
**Working Model impact:** none — sintesi, non replica indipendente
**Report mentions:** corpus alignment; CC-20260810-34831305-01
**Next action:** none — risolto per promozione
**Flags:** sintesi secondaria — non contare come corroborazione indipendente dei primari che elenca
**Note:** Title: WWOX-Related Neurodevelopmental Disorders: Models and Future Perspectives

---

## LIT-0031
**Short title:** corpus paper 4
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33255508 / DOI 10.3390/ijms21238922
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 4
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders

---

## LIT-0032
**Short title:** corpus paper 5
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30350478 / DOI 10.1002/gcc.22693
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 5
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX, the FRA16D gene: A target of and a contributor to genomic instability

---

## LIT-0033
**Short title:** corpus paper 6
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30158849 / DOI 10.3389/fnins.2018.00563
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 6
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none - screened and read on 2026-10-03 (`partial_fulltext_read`, per its receipt) (integrator amendment, `BATCH_20261003_002`) (intake wave 3, Scientist B); promoted to [[paper_registry_current#PAPER 150]] by `CC-20261003W3-B-REGISTRY-01`
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Phosphorylation, Signaling, and Role in Neurodegeneration

---

## LIT-0034
**Short title:** corpus paper 7
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32389029 / DOI 10.1177/1535370220924618
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 7
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — processed 2026-10-03 (`FTR-20261003-32389029-01`) and recorded as [[paper_registry_current#PAPER 153]] by `CC-20261003W4-A-REGISTRY-01`; Kośla K et al. 2020, *Exp Biol Med* 245:1122; narrative review, `partial_fulltext_read` (figure images unobtainable); the placeholder fields above are kept as history
**Flags:** corpus placeholder / not yet screened
**Note:** Title: The WWOX gene in brain development and pathology

---

## LIT-0035
**Short title:** corpus paper 8
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25538133 / DOI 10.1177/1535370214561590
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 8
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX: a fragile tumor suppressor

---

## LIT-0036
**Short title:** corpus paper 9
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35883580 / DOI 10.3390/cells11142137
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 9
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Controls Cell Survival, Immune Response and Disease Progression by pY33 to pS14 Transition

---

## LIT-0037
**Short title:** corpus paper 10
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 38542478 / DOI 10.3390/ijms25063507
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 10
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none - screened and read on 2026-10-03 (`partial_fulltext_read`, per its receipt) (integrator amendment, `BATCH_20261003_002`) (intake wave 3, Scientist B); promoted to [[paper_registry_current#PAPER 149]] by `CC-20261003W3-B-REGISTRY-01`
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Zfra Overrides WWOX in Suppressing the Progression of Neurodegeneration

---

## LIT-0038
**Short title:** corpus paper 11
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30370248 / DOI 10.3389/fonc.2018.00420
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 11
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 067]] (`BATCH_20260815_001`)
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Modeling WWOX Loss of Function in vivo: What Have We Learned?

---

## LIT-0039
**Short title:** corpus paper 12
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 18437686 / DOI 10.14670/HH-23.877
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 12
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX tumor suppressor gene

---

## LIT-0040
**Short title:** corpus paper 13
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33916893 / DOI 10.3390/cells10040824
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 13
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Neurological Disorders Associated with WWOX Germline Mutations - A Comprehensive Overview

---

## LIT-0041
**Short title:** corpus paper 14
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30211123 / DOI 10.3389/fonc.2018.00345
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 14
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Tumor Suppressor Gene in Breast Cancer, a Historical Perspective and Future Directions

---

## LIT-0042
**Short title:** corpus paper 15
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39500530 / DOI 10.1136/jitc-2024-010422
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 15
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX tuning of oleic acid signaling orchestrates immunosuppressive macrophage polarization and sensitizes hepatocellular carcinoma to immunotherapy

---

## LIT-0043
**Short title:** corpus paper 16
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 17458891 / DOI 10.1002/jcp.21099
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 16
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX in biological control and tumorigenesis

---

## LIT-0044
**Short title:** corpus paper 17
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 19708029 / DOI 10.1002/jcb.22298
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 17
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX: its genomics, partners, and functions

---

## LIT-0045
**Short title:** corpus paper 18
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33946771 / DOI 10.3390/cells10051051
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 18
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Molecular Functions of WWOX Potentially Involved in Cancer Development

---

## LIT-0046
**Short title:** corpus paper 19
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34210081 / DOI 10.3390/cells10071637
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 19
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Molecular Biology of the WWOX Gene That Spans Chromosomal Fragile Site FRA16D

---

## LIT-0047
**Short title:** corpus paper 20
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 24932569 / DOI 10.1016/j.bbcan.2014.06.001
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 20
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX at the crossroads of cancer, metabolic syndrome related traits and CNS pathologies

---

## LIT-0048
**Short title:** corpus paper 21
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25595185 / DOI 10.1177/1535370214565992
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 21
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX, large common fragile site genes, and cancer

---

## LIT-0049
**Short title:** corpus paper 22
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31075076 / DOI 10.1080/15384101.2019.1616998
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 22
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Decoding the link between WWOX and p53 in aggressive breast cancer

---

## LIT-0050
**Short title:** corpus paper 23
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25595186 / DOI 10.1177/1535370214565990
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 23
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX, the chromosomal fragile site FRA16D spanning gene: its role in metabolism and contribution to cancer

---

## LIT-0051
**Short title:** corpus paper 24
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36364214 / DOI 10.3390/molecules27217388
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 24
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Modulates ROS-Dependent Senescence in Bladder Cancer

---

## LIT-0052
**Short title:** corpus paper 25
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25681467 / DOI 10.1177/1535370214561953
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 25
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Alteration of WWOX in human cancer: a clinical view

---

## LIT-0053
**Short title:** corpus paper 26
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 17163164 / DOI 10.1007/978-1-4020-5133-3_14
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 26
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX, a chromosomal fragile site gene and its role in cancer

---

## LIT-0054
**Short title:** corpus paper 27
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 38182577 / DOI 10.1038/s41419-023-06378-8
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 27
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX promotes osteosarcoma development via upregulation of Myc

---

## LIT-0055
**Short title:** corpus paper 28
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39894307 / DOI 10.1016/j.bcp.2025.116790
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 28
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX-mediated p53/SAT1 and NRF2/FPN1 axis contribute to toosendanin-induced ferroptosis in hepatocellular carcinoma

---

## LIT-0056
**Short title:** corpus paper 29
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 20146584 / DOI 10.2217/fon.09.152
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 29
**Status:** processed
**Status note:** partial_fulltext_read
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001 — receipt `FTR-20260909-20146584-01`
**Note:** Title: WWOX gene and gene product: tumor suppression through specific protein interactions

---
**Evidence depth:** partial_fulltext_read — `FTR-20260909-20146584-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 085]]
**Batch note:** partial_fulltext_read — two NIHMS figure images unretrievable, tracked as FT-096

## LIT-0057
**Short title:** corpus paper 31
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33105088 / DOI 10.1165/rcmb.2020-0444ED
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 31
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Loss of Endothelial WWOX: A Risk Factor for ARDS in Smokers?

---

## LIT-0058
**Short title:** corpus paper 32
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27999774 / DOI 10.3389/fcell.2016.00141
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 32
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: HYAL-2-WWOX-SMAD4 Signaling in Cell Death and Anticancer Response

---

## LIT-0059
**Short title:** corpus paper 33
**Authors:** Dugan AJ, Nelson PT, Katsumata Y, et al.; Fardo DW
**Year:** 2022 (epub 2021-10-29)
**Source type:** primary research — locus-restricted genetic association meta-analysis (two adult autopsy cohorts)
**Journal/source:** *Neurobiol Aging* 2022;111:95-106
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34852950 / DOI 10.1016/j.neurobiolaging.2021.10.011
**Date discovered:** 2026-04-12
**Date processed:** 2026-10-03 (`FTR-20261003-34852950-01`, complete_fulltext_read)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 33
**Status:** processed
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW — common non-coding variants in adult neurodegeneration; no transfer to WWOX-DEE (corrected from HIGH by `CC-20261003W6-A-REGISTRY-01`)
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none owed; landed as [[paper_registry_current#PAPER 196]]
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Association between WWOX/MAF variants and dementia-related neuropathologic endophenotypes

---

## LIT-0060
**Short title:** corpus paper 34
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25416187 / DOI 10.1177/1535370214561952
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 34
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: The fragile site WWOX gene and the developing brain

---

## LIT-0061
**Short title:** corpus paper 37
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 24520212 / DOI 10.7150/ijbs.7727
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 37
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — processed 2026-10-03 (`FTR-20261003-24520212-01`) and recorded as [[paper_registry_current#PAPER 155]] by `CC-20261003W4-A-REGISTRY-01`; Li J et al. 2014, *Int J Biol Sci* 10:142; narrative review; the placeholder fields above are kept as history
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Common Chromosomal Fragile Site Gene WWOX in Metabolic Disorders and Tumors

---

## LIT-0062
**Short title:** corpus paper 38
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25476151 / DOI 10.1177/1535370214561587
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 38
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Roles of the WWOX in pathogenesis and endocrine therapy of breast cancer

---

## LIT-0063
**Short title:** AbuRemaileh 2019 — ablazione di WWOX nel muscolo scheletrico
**Authors:** Abu-Remaileh M, Aqeilan RI, et al.
**Year:** 2019
**Source type:** primario sperimentale — KO tessuto-specifico murino + knock-down in C2C12
**Journal/source:** *Molecular Metabolism* 22:132–140
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30755385 / DOI 10.1016/j.molmet.2019.01.010
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260810-30755385-01`
**Registry record:** [[paper_registry_current#PAPER 061]] (promosso da `CORPUS-STUB-039`, BATCH_20260810_003)
**Primary pathway:** P5 — metabolismo
**Genotype/model tag:** KO condizionale muscolo-scheletrico murino; non CNS, non allele WWOX-DEE
**Transferability:** T2 — meccanismo trasferibile, tessuto no
**clinical relevance:** INDIRECT
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 39
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX somatic ablation in skeletal muscles alters glucose metabolism

---

## LIT-0064
**Short title:** corpus paper 40
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27234396 / DOI 10.1186/2213-0802-1-15
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 40
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Role of WWOX and NF-kB in lung cancer progression

---

## LIT-0065
**Short title:** corpus paper 41
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 37248434 / DOI 10.1038/s41417-023-00626-x
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 41
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX binds MERIT40 and modulates its function in homologous recombination, implications in breast cancer

---

## LIT-0066
**Short title:** corpus paper 42
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35107375 / DOI 10.1128/jvi.02026-21
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 42
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX-Mediated Degradation of AMOTp130 Negatively Affects Egress of Filovirus VP40 Virus-Like Particles

---

## LIT-0067
**Short title:** corpus paper 43
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36621327 / DOI 10.1016/j.intimp.2022.109671
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 43
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX activates autophagy to alleviate lipopolysaccharide-induced acute lung injury by regulating mTOR

---

## LIT-0068
**Short title:** corpus paper 44
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 26499798 / DOI 10.1074/jbc.R115.676346
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 44
**Status:** processed
**Status note:** complete_fulltext_read
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001 — receipt `FTR-20260909-26499798-01`
**Note:** Title: Pleiotropic Functions of Tumor Suppressor WWOX in Normal and Cancer Cells

---
**Evidence depth:** complete_fulltext_read — `FTR-20260909-26499798-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 089]]
**Batch note:** secondary — review; primary only for its own Figure 2B

## LIT-0069
**Short title:** corpus paper 45
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 29310447 / DOI 10.1177/1535370217752350
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 45
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Phosphorylation/de-phosphorylation in specific sites of tumor suppressor WWOX and control of distinct biological events

---

## LIT-0070
**Short title:** Schrock 2017 — Wwox–Brca1 interaction and DNA-repair pathway choice
**Authors:** Schrock MS, Batar B, Lee J, Druck T, Ferguson B, Cho JH, Akakpo K, Hagrass H, Heerema NA, Xia F, Parvin JD, Aldaz CM, Huebner K
**Year:** 2017
**Source type:** primary research, experimental (cell biology + xenograft + public-database re-analysis)
**Journal/source:** *Oncogene* 36(16):2215-2227
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27869163 / DOI 10.1038/onc.2016.389
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 46
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260913-27869163-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260913-27869163-01`
**Primary pathway:** P6 — DDR / genome stability: DSB repair-pathway choice (HR/SSA vs NHEJ), WWOX–BRCA1 axis
**Genotype/model tag:** whole-body `Wwox−/−` mouse MEFs; human cancer/immortalised lines; no WWOX-DEE allele
**Transferability:** T3 — oncology cell biology, no neural or developmental system
**clinical relevance:** LOW — unchanged
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** corpus alignment · `CC-20260913-27869163-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260913-27869163-01`
**Note:** Title: Wwox-Brca1 interaction: role in DNA repair pathway choice
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-27869163-01`; manifest `deepdive_manifests/PMID27869163.json`
**Registry record:** [[paper_registry_current#PAPER 109]]

---

## LIT-0071
**Short title:** corpus paper 47
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 19609013
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 47
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX, the tumour suppressor gene affected in multiple cancers

---

## LIT-0072
**Short title:** Repudi 2021 EMBO gene therapy
**Authors:** Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI
**Year:** 2021
**Source type:** studio preclinico di terapia genica (AAV9-hSynI-WWOX, ICV neonatale)
**Journal/source:** *EMBO Molecular Medicine* 13(12):e14599
**Identifier type:** PMID / PMCID / DOI
**Identifier value:** PMID 34747138 / PMCID PMC8649866 / DOI 10.15252/emmm.202114599
**Evidence depth:** complete_fulltext_read (2026-08-10) — receipt `FTR-20260810-34747138-01`, manifest `deepdive_manifests/PMID34747138.json` (20 locator, 0 gap)
**Registry record:** [[paper_registry_current#PAPER 005]] — il record PAPER esisteva già dal 2026-07-05; `CORPUS-STUB-048` era il suo duplicato ed è marcato promosso in BATCH_20260810_005
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 48
**Status:** processed
**Primary pathway:** P7 — gene therapy readiness
**Genotype/model tag:** topo Wwox-null sistemico, trattamento a P0; non un allele WWOX-DEE
**Transferability:** T2 — design principle trasferibili, non dose né timing
**clinical relevance:** HIGH
**Claim links:** 004 · 003 (confine)
**Working Model impact:** qualifica CLAIM 004 con il comparatore mancante; nessun nuovo claim
**Report mentions:** corpus alignment; BATCH_20260810_005
**Next action:** none — risolto per promozione; restano dovuti `legend-locator-audit` e le figure dell'Appendix
**Flags:** il confronto WT-contro-rescued è **non tracciato** nei pannelli dove il rescue appare più forte — non citare *«normalizza»*
**Note:** Title: Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes

---

## LIT-0073
**Short title:** corpus paper 49
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36530994 / DOI 10.3389/fonc.2022.996820
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 49
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX-rs13338697 genotype predicts therapeutic efficacy of ADI-PEG 20 for patients with advanced hepatocellular carcinoma

---

## LIT-0074
**Short title:** corpus paper 50
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32300104 / DOI 10.1038/s41392-020-0136-8
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 50
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 068]] (`BATCH_20260815_001`)
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Pleiotropic tumor suppressor functions of WWOX antagonize metastasis

---

## LIT-0075
**Short title:** corpus paper 51
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25595191 / DOI 10.1177/1535370214566747
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 51
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Regulation of cell signaling and apoptosis by tumor suppressor WWOX

---

## LIT-0076
**Short title:** corpus paper 52
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 40327201 / DOI 10.1007/s10142-025-01601-5
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 52
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Twenty-five years of WWOX insight in cancer: a treasure trove of knowledge

---

## LIT-0077
**Short title:** Hussain 2023 P47T
**Authors:** Hussain T, Sanchez K, Crayton J, Saha D, Jeter C, Lu Y, Abba M, Seo R, Noebels JL, Fonken L, Aldaz CM
**Year:** 2023
**Source type:** variant-specific mechanistic study (mouse knock-in)
**Journal/source:** *Progress in Neurobiology* 223:102425
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36828035 / DOI 10.1016/j.pneurobio.2023.102425
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 53
**Status:** integrated
**Primary pathway:** P6 — neuroinflammation / glia
**Genotype/model tag:** P47T knock-in (WW1)
**Transferability:** T3 with genotype caution
**clinical relevance:** LOW
**Claim links:** 006, 007
**Working Model impact:** `BATCH_20260926_ALDAZ` (WM_v5.1): CLAIM 006 and CLAIM 007 narrowed
**Report mentions:** corpus alignment
**Next action:** none for CLAIM 006/007; remaining sections of the reading's candidate are queued (Purkinje/basket-cell claim, dismissals, reading debt)
**Flags:** registry records PAPER 007 (canonical) and PAPER 112 (duplicate, append-only)
**Note:** clinical relevance set to LOW as on `PAPER 007` by `BATCH_20260926_ALDAZ`; the corpus-alignment triage value HIGH is superseded. Title: WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice

---

## LIT-0078
**Short title:** corpus paper 54
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 22202011 / DOI 10.2741/e516
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 54
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Role of WWOX/WOX1 in Alzheimer's disease pathology and in cell death signaling

---

## LIT-0079
**Short title:** Ferguson 2013 — WWOX inibisce l'attività trascrizionale di SMAD3; legame via WW1
**Authors:** Ferguson BW, Gao X, Zelazowski MJ, Lee J, Jeter CR, Abba MC, Aldaz CM
**Year:** 2013
**Source type:** primary experimental — biologia cellulare, trascrittoma e co-IP/pull-down, con una coda di meta-analisi su dati pubblici
**Journal/source:** *BMC Cancer* 13:593
**Identifier type:** PMID / DOI
**Identifier value:** PMID 24330518 / DOI 10.1186/1471-2407-13-593 / PMCID PMC3871008
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 55
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-24330518-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-24330518-01`
**Primary pathway:** architettura di dominio / interpretazione delle varianti; secondaria: TGF-β/SMAD signalling
**Genotype/model tag:** linee mammarie umane, mutante di dominio WW1, nessun materiale neurale, nessun allele WWOX-DEE
**Transferability:** T3
**clinical relevance:** INDIRECT-LOW
**Claim links:** none — unchanged; the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** corpus alignment · `CC-20260914-24330518-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-24330518-01`
**Note:** Title: The cancer gene WWOX behaves as an inhibitor of SMAD3 transcriptional activity via direct binding
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-24330518-01`; manifest `deepdive_manifests/PMID24330518.json`
**Registry record:** [[paper_registry_current#PAPER 108]]

---

## LIT-0080
**Short title:** corpus paper 56
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33300063 / DOI 10.3892/mmr.2020.11754
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 56
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — processed 2026-10-03 (`FTR-20261003-33300063-01`) and recorded as [[paper_registry_current#PAPER 152]] by `CC-20261003W4-A-REGISTRY-01`; Zhao Y et al. 2020, *Mol Med Rep* 23:115; steady-state autophagy proteins only, ovarian cancer lines; the placeholder fields above are kept as history
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX promotes apoptosis and inhibits autophagy in paclitaxel-treated ovarian carcinoma cells

---

## LIT-0081
**Short title:** corpus paper 57
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 37324196 / DOI 10.7150/ijms.84364
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 57
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Polymorphisms as Predictors of the Biochemical Recurrence of Localized Prostate Cancer after Radical Prostatectomy

---

## LIT-0082
**Short title:** ChemBioChem 2020 WWOX–p73 phospho-binding
**Authors:** Shkedi et al.
**Year:** 2020
**Source type:** experimental biochemistry / quantitative binding study
**Journal/source:** *ChemBioChem*
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32185845 / DOI 10.1002/cbic.202000032
**Date discovered:** 2026-04-12
**Date processed:** 2026-04-17
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 58
**Status:** integrated
**Primary pathway:** signaling organization / PTM / partner affinity
**Genotype/model tag:** in vitro WWOX WW1 / Tyr33 phosphorylation / p73-derived peptide
**Transferability:** T2 conceptual / indirect
**clinical relevance:** LOW direct / HIGH architectural
**Claim links:** 028
**Working Model impact:** strengthens mechanistic support for CLAIM 028; no BLOCCO 1 change
**Report mentions:** corpus alignment; post-181–220 propagation
**Next action:** none immediate; use as anchor for PTM / partner-switching branch
**Flags:** full-text not confirmed open on primary site; abstract-level + secondary-access mechanistic extraction; tension-bearing with 2004 cell-based p73 literature
**Note:** Title: Phosphorylation of the WWOX Protein Regulates Its Interaction with p73. Quantitative binding study showing Tyr33 phosphorylation decreases affinity for a p73-derived peptide; strengthens context/partner dependence without closing full cellular p73 biology.

---

## LIT-0083
**Short title:** Piard 2019 Genet Med — WOREE phenotypic spectrum (20 additional cases)
**Authors:** Piard J, Hawkes L, Milh M, Villard L, Borgatti R, Romaniello R, Fradin M, Capri Y, Héron D, Nougues MC, Nava C, Tarta Arsene O, Shears D, Taylor J, Pagnamenta A, Taylor JC, Sogawa Y, Johnson D, Firth H, Vasudevan P, Jones G, Nguyen-Morel MA, Busa T, Roubertie A, van den Born M, Brischoux-Boucher E, Koenig M, Mignot C, Kini U, Philippe C
**Year:** 2019 (issue) / 2018-10-25 (online first) — one paper, two citable years
**Source type:** primary cohort + review
**Journal/source:** Genet Med 2019;21(6):1308-1318
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30356099 / DOI 10.1038/s41436-018-0339-3
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 59
**Status:** processed
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — promoted to [[paper_registry_current#PAPER 117]] 2026-09-27 (`BATCH_20260927_003`); erratum PMID 30783266 linked (administrative)
**Flags:** corpus placeholder / not yet screened
**Note:** Title: The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature

---

## LIT-0084
**Short title:** corpus paper 60
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35792847 / DOI 10.1684/epd.2022.1444
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 60
**Status:** processed
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — processed 2026-10-03 (`FTR-20261003-35792847-01`, `complete_fulltext_read`) and promoted to [[paper_registry_current#PAPER 171]] by `CC-20261003W5-B-REGISTRY-01`; Al Baradie R et al. 2022, *Epileptic Disord* 24(4):697-712; nine homozygous WOREE patients, family 2 probably already counted under PAPER 119; the placeholder fields above are kept as history
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Epilepsy in patients with WWOX-related epileptic encephalopathy (WOREE) syndrome

---

## LIT-0085
**Short title:** corpus paper 61
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 28045433 / DOI 10.3390/ijms18010075
**Date discovered:** 2026-04-12
**Date processed:** 2026-07-10 (integrity/dependency audit)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 61
**Status:** background_only
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — non usare come corroborazione; riaprire solo dopo audit indipendente fonte-per-fonte
**Flags:** dependency-contaminated / retracted-primary dependency / integrity exclusion / background only
**Note:** Title: Functions and Epigenetic Regulation of Wwox in Bone Metastasis from Breast Carcinoma. URG_2026-07-09_001: la review riusa dati del primario PMID 28151481 / DOI 10.1038/cddis.2016.403, ritirato nel 2022 (DOI 10.1038/s41419-022-04992-6) per problemi di integrità delle immagini western blot, e poggia su ulteriori fonti della stessa linea. Nessun claim canonico la usa.

---

## LIT-0086
**Short title:** corpus paper 62
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 40139278 / DOI 10.1016/j.nbd.2025.106887
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 62
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Influence of WWOX/MAF genes on cognitive performance in patients with Parkinson's disease

---

## LIT-0087
**Short title:** corpus paper 63
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34015398 / DOI 10.1016/j.canlet.2021.05.010
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 63
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX activation by toosendanin suppresses hepatocellular carcinoma metastasis through JAK2/Stat3 and Wnt/beta-catenin signaling

---

## LIT-0088
**Short title:** corpus paper 65
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 40198927 / DOI 10.1016/j.tice.2025.102885
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 65
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX attenuates the progression of gallbladder cancer by suppressing cellular glycolysis through the modulation of the P73/HIF-1alpha signaling pathway

---

## LIT-0089
**Short title:** corpus paper 66
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41443103 / DOI 10.1016/j.intimp.2025.116067
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 66
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX protects against ferroptosis to alleviate acute lung injury by mediating p53 deacetylation

---

## LIT-0090
**Short title:** corpus paper 67
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25432984 / DOI 10.1177/1535370214561588
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 67
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Role of WW domain proteins WWOX in development, prognosis, and treatment response of glioma

---

## LIT-0091
**Short title:** corpus paper 68
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 38203337 / DOI 10.3390/ijms25010167
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 68
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Mechanistic Investigation of WWOX Function in NF-kB-Induced Skin Inflammation in Psoriasis

---

## LIT-0092
**Short title:** corpus paper 69
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30622118 / DOI 10.1158/0008-5472.CAN-18-0614
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 69
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Inhibits Metastasis of Triple-Negative Breast Cancer Cells via Modulation of miRNAs

---

## LIT-0093
**Short title:** Carvalho 2022 — Zfra1-31 in neuroni iperglicemici
**Authors:** Carvalho C, Correia SC, Seiça R, Moreira PI (tutti Università di Coimbra)
**Year:** 2022
**Source type:** Article — primary
**Journal/source:** Cellular and Molecular Life Sciences 2022;79(9):487
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35984507 / DOI 10.1007/s00018-022-04508-7
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-21
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 70
**Status:** processed
**Status note:** promosso a [[paper_registry_current#PAPER 097]] (`BATCH_20260921_002`)
**Primary pathway:** P5 — metabolismo / mitocondri / redox
**Genotype/model tag:** WWOX wild-type; SH-SY5Y differenziate + ratti Goto-Kakizaki; nessun allele WWOX-DEE
**Transferability:** T3
**clinical relevance:** ~~HIGH~~ → **MODERATE** — declassata **dopo la lettura**: la rilevanza è di direzione terapeutica, non di meccanismo di malattia. `HIGH` era una stima di triage fatta sul titolo
**Claim links:** none — il record porta una lettura, non una claim
**Working Model impact:** none — nessuna claim, nessun movimento del modello
**Report mentions:** acquisizione `A9`; addendum di `peptide_intervention_audit_20260920.md`; `HYP-20260705-05`
**Next action:** none — letto e chiuso. **Non richiedere di nuovo questo paper**
**Flags:** letto da PDF fornito dall'operatore (PMC stub a corpo zero); ricevute `FTR-20260921-35984507-01` e `-02`; `figures: captions_only`
**Note:** Title: WWOX inhibition by Zfra1-31 restores mitochondrial homeostasis and viability of neuronal cells exposed to high glucose. 🔴 **Nessun braccio genetico su WWOX, nessun controllo con peptide inattivo, WWOX totale mai misurata benché `ABN413` sia elencato nei metodi.**

---

## LIT-0094
**Short title:** corpus paper 71
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 17690733 / DOI 10.5507/bp.2007.002
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 71
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX, a new potential tumor suppressor gene

---

## LIT-0095
**Short title:** corpus paper 72
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 28977834 / DOI 10.18632/oncotarget.17126
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 72
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Decreased WWOX expression promotes angiogenesis in osteosarcoma

---

## LIT-0096
**Short title:** corpus paper 73
**Authors:** Abu-Remaileh M, Khalaileh A, Pikarsky E, Aqeilan RI
**Year:** 2018
**Source type:** primary experimental (mouse conditional knockout, in vivo)
**Journal/source:** Cell Death & Disease 9:511
**Identifier type:** PMID / DOI
**Identifier value:** PMID 29724996 / DOI 10.1038/s41419-018-0510-4
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 73
**Status:** processed
**Status note:** complete_fulltext_read
**Primary pathway:** P5 — metabolism / HIF1α–glycolysis
**Genotype/model tag:** `Wwox^ΔHep` (Alb-Cre × Wwox^fl/fl), DEN-induced HCC, ± high-fat diet — not a WWOX-DEE allele
**Transferability:** T3
**clinical relevance:** INDIRECT
**Claim links:** CLAIM 025 (qualifying evidence; no new claim)
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** corpus alignment
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001 — receipt `FTR-20260909-29724996-01`
**Note:** Title: WWOX controls hepatic HIF1alpha to suppress hepatocyte proliferation and neoplasia

---
**Evidence depth:** complete_fulltext_read — `FTR-20260909-29724996-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 091]]
**Batch note:** primary experimental; Author Correction PMID 30470736 read as its own source. Descriptive fields completed in `BATCH_20260926_ALDAZ_R2` (`CC-20260913-29724996-03`) from `PAPER 091` and the deposit front matter; `clinical relevance` MED → INDIRECT so the log agrees with the identity record

## LIT-0097
**Short title:** Park 2022 — Wwox binding to the murine Brca1-BRCT domain and repair pathway choice
**Authors:** Park D, Gharghabi M, Reczek CR, Plow R, Yungvirt C, Aldaz CM, Huebner K
**Year:** 2022
**Source type:** primary research, experimental (mouse cell biology)
**Journal/source:** *Int J Mol Sci* 23(7):3729
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35409089 / DOI 10.3390/ijms23073729
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 74
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260913-35409089-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260913-35409089-01`
**Primary pathway:** P6 — DDR / genome stability: DSB end-resection timing; BRCA1-BRCT complex formation
**Genotype/model tag:** mouse MEFs (`Wwox−/−`, siWwox) and mouse tumour lines; no WWOX-DEE allele
**Transferability:** T3 — and it makes mouse→human transfer of this mechanism weaker (different binding surface in mouse)
**clinical relevance:** LOW
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** corpus alignment · `CC-20260913-35409089-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260913-35409089-01`
**Note:** Title: Wwox Binding to the Murine Brca1-BRCT Domain Regulates Timing of Brip1 and CtIP Phospho-Protein Interactions
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-35409089-01`; manifest `deepdive_manifests/PMID35409089.json`
**Registry record:** [[paper_registry_current#PAPER 111]]

---

## LIT-0098
**Short title:** corpus paper 75
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 21499303 / DOI 10.1038/onc.2011.115
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 75
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Wwox inactivation enhances mammary tumorigenesis

---

## LIT-0099
**Short title:** corpus paper 76
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36572673 / DOI 10.1038/s41419-022-05519-9
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 76
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 069]] (`BATCH_20260815_001`)
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Loss of tumor suppressor WWOX accelerates pancreatic cancer development through promotion of TGFbeta/BMP2 signaling

---

## LIT-0100
**Short title:** corpus paper 77
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 37897534 / DOI 10.1007/s00018-023-04950-1
**Date discovered:** 2026-04-12
**Date processed:** 2026-10-02 (partial full text; `FTR-20261002-37897534-01`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 77
**Status:** processed
**Status note:** read 2026-10-02 at `partial_fulltext_read` depth (receipt `FTR-20261002-37897534-01`); figure panels and the supplement are unread. Promoted to [[paper_registry_current#PAPER 130]] by `CC-20261002-INTAKE-WAVE-ORPHANS-01`; the triage fields below are kept as history
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID37897534.json`
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** figure panels and the supplement owed for a complete read
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Loss of fragile WWOX gene leads to senescence escape and genome instability

---

## LIT-0101
**Short title:** corpus paper 78
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27308416 / DOI 10.4161/23723548.2014.965640
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-11
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 78
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 072]] (`BATCH_20260815_001`)
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX loss activates aerobic glycolysis

---

## LIT-0102
**Short title:** corpus paper 79
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30214895 / DOI 10.3389/fonc.2018.00350
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 79
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Cancerous Protein Network That Inhibits the Tumor Suppressor Function of WWOX

---

## LIT-0103
**Short title:** corpus paper 80
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32096174 / DOI 10.26355/eurrev_202002_20154
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 80
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX regulates the Elf5/Snail1 pathway to affect epithelial-mesenchymal transition of ovarian carcinoma cells

---

## LIT-0104
**Short title:** corpus paper 81
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 26675548 / DOI 10.18632/oncotarget.6571
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-14
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 81
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 080]] (`BATCH_20260815_001`)
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX modulates the ATR-mediated DNA damage checkpoint response

---

## LIT-0105
**Short title:** corpus paper 82
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 16225988 / DOI 10.1016/j.canlet.2005.06.048
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 82
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Roles of FHIT and WWOX fragile genes in cancer

---

## LIT-0106
**Short title:** corpus paper 83
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33195192 / DOI 10.3389/fcell.2020.558432
**Date discovered:** 2026-04-12
**Date processed:** 2026-10-02 (partial full text; `FTR-20261002-33195192-01`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 83
**Status:** processed
**Status note:** read 2026-10-02 at `partial_fulltext_read` depth (receipt `FTR-20261002-33195192-01`); figure panels and the supplement, including Supplementary Figure S9, are unread. Promoted to [[paper_registry_current#PAPER 129]] by `CC-20261002-INTAKE-WAVE-ORPHANS-01`; the triage fields below are kept as history
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID33195192.json`
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** figure panels and the supplement (Suppl. Fig. S9 carries the total-ERK half of the pERK result) owed for a complete read
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Wwox Deficiency Causes Downregulation of Prosurvival ERK Signaling and Abnormal Homeostatic Responses in Mouse Skin

---

## LIT-0107
**Short title:** corpus paper 84
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34998176 / DOI 10.1016/j.dnarep.2021.103264
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 84
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Interaction of Wwox with Brca1 and associated complex proteins prevents premature resection at double-strand breaks

---

## LIT-0108
**Short title:** corpus paper 85
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30290271 / DOI 10.1016/j.nbd.2018.09.026
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 85
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Wwox deletion leads to reduced GABA-ergic inhibitory interneuron numbers and activation of microglia and astrocytes in mouse hippocampus

---

## LIT-0109
**Short title:** corpus paper 86
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 29200707 / DOI 10.4103/ijmpo.ijmpo_125_17
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 86
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX rs11644322 Polymorphism, Gemcitabine, and Pancreatic Cancer

---

## LIT-0110
**Short title:** corpus paper 87
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33914858 / DOI 10.1093/brain/awab174
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 87
**Status:** processed
**Primary pathway:** P4 — myelination / white matter
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — the live record for this DOI is [[paper_registry_current#PAPER 004]]; this row is kept as the discovery trace
**Flags:** corpus placeholder resolved 2026-10-03 by `CC-20261003R-REGISTRY-01` (propagated by `BATCH_20261003_005`); the duplicate identity on the same DOI, `CORPUS-STUB-087`, was already retired to a pointer by `BATCH_20261003_003` from the wave-4 twin `CC-20261003W4-B-REGISTRY-01`, so this candidate's own retirement op was **dropped as already propagated** and no second retirement was written. The reading itself lives on `PAPER 004` and its receipts; no depth marker is restated here, so this row adds no reading to any coverage denominator
**Note:** Title: Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects

---

## LIT-0111
**Short title:** McBride 2019 — Wwox deletion in mouse B cells: genomic instability and repair pathway choice
**Authors:** McBride KM, Kil H, Mu Y, Plummer JB, Lee J, Zelazowski MJ, Sebastian M, Abba MC, Aldaz CM
**Year:** 2019
**Source type:** primary research — conditional-knockout mouse cohort + primary-B-cell repair assays
**Journal/source:** *Front Oncol* 9:517
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31275852 / DOI 10.3389/fonc.2019.00517
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 88
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-31275852-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-31275852-01`
**Primary pathway:** genome stability / DNA damage response (repair pathway choice)
**Genotype/model tag:** murine B-lineage (Cd19-conditional cohort; whole-body null for the repair experiments); no WWOX disease allele; no neural material
**Transferability:** T3
**clinical relevance:** LOW — unchanged
**Claim links:** none — held for the claim batch
**Working Model impact:** none in this batch — the `CLAIM 029` sentence is held for the claim batch
**Report mentions:** corpus alignment · `CC-20260914-31275852-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-31275852-01`
**Note:** Title: Wwox Deletion in Mouse B Cells Leads to Genomic Instability, Neoplastic Transformation, and Monoclonal Gammopathies
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-31275852-01`; manifest `deepdive_manifests/PMID31275852.json`
**Registry record:** [[paper_registry_current#PAPER 110]]

---

## LIT-0112
**Short title:** corpus paper 89
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 23277037 / DOI 10.2741/s358
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 89
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Role of WWOX/WOX1 in Alzheimer's disease pathology and in cell death signaling (Schol Ed)

---

## LIT-0113
**Short title:** corpus paper 90
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39039877 / DOI 10.3760/cma.j.cn112140-20240229-00135
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 90
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Genotype and phenotype of WWOX gene related developmental and epileptic encephalopathy [Chinese]

---

## LIT-0114
**Short title:** Singla 2017 — lung WWOX knockdown causes neutrophilic alveolitis
**Authors:** Singla S, Chen J, Sethuraman S, Sysol JR, Gampa A, Zhao S, Machado RF
**Year:** 2017
**Source type:** primary experimental — murine airway siRNA knockdown plus an A549 mechanism arm
**Journal/source:** *Am J Physiol Lung Cell Mol Physiol* 312(6):L903-L911
**Identifier type:** PMID / DOI
**Identifier value:** PMID 28283473 / DOI 10.1152/ajplung.00034.2017
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 91
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-28283473-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-28283473-01`
**Primary pathway:** inflammatory signalling / lung — the corpus's only source for a positive pulmonary inflammatory phenotype
**Genotype/model tag:** wild-type C57BL/6 with acute intratracheal siRNA; no WWOX variant, no knockout, no neural material
**Transferability:** T3 — compartment-bound
**clinical relevance:** INDIRECT-LOW — 🔴 re-assigned from `LOW`, which was set at corpus alignment before the paper was opened: it is the hinge of the lung axis, so not peripheral; and one unreplicated siRNA at n = 3 per group in a non-neural compartment, so not clinically actionable
**Claim links:** none — the reading proposes none
**Working Model impact:** none directly — it corrects the **scope** the corpus attributed to this model (airway-delivered lung knockdown, not whole-body), not the model's content
**Report mentions:** corpus alignment · `CC-20260914-28283473-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-28283473-01`
**Note:** Title: Loss of lung WWOX expression causes neutrophilic inflammation
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-28283473-01`; manifest `deepdive_manifests/PMID28283473.json`
**Registry record:** [[paper_registry_current#PAPER 102]]

---

## LIT-0115
**Short title:** corpus paper 92
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34204827 / DOI 10.3390/cancers13122957
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 92
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Loses the Ability to Regulate Oncogenic AP-2gamma and Synergizes with Tumor Suppressor AP-2alpha in High-Grade Bladder Cancer

---

## LIT-0116
**Short title:** corpus paper 94
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39473747 / DOI 10.55730/1300-0144.5891
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 94
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Loss of WWOX contributes to cisplatin resistance in triple-negative breast cancer cells by modulating miR-182 and miR-214

---

## LIT-0117
**Short title:** Kołat 2023 — LINC01137/miR-186-5p/WWOX in carcinoma vescicale
**Authors:** Kołat D, Kałuzińska-Kołat Ż, Kośla K, Orzechowska M, Płuciennik E, Bednarek AK
**Year:** 2023
**Source type:** primario in vitro + in silico (rianalisi CAGE-seq + coorti pubbliche)
**Journal/source:** *Frontiers in Genetics* 14:1214968
**Identifier type:** PMID / DOI
**Identifier value:** PMID 37519886 / DOI 10.3389/fgene.2023.1214968
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-05
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 95
**Status:** processed
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260805-37519886-01`
**Registry record:** [[paper_registry_current#PAPER 060]] (promosso da `CORPUS-STUB-095`, BATCH_20260810_002)
**Primary pathway:** regolazione a RNA / ncRNA — contesto oncologico
**Genotype/model tag:** WWOX wild-type, linee di carcinoma vescicale umano
**Transferability:** T3 — indiretta; nessun contenuto neuronale, dello sviluppo o di variante
**clinical relevance:** LOW
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: LINC01137/miR-186-5p/WWOX: a novel axis identified from WWOX-related RNA interactome in bladder cancer

---

## LIT-0118
**Short title:** corpus paper 96
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 37974179 / DOI 10.1186/s12920-023-01731-4
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 96
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — processed 2026-10-03 (`FTR-20261003-37974179-01`, `complete_fulltext_read`) and promoted to [[paper_registry_current#PAPER 134]] by `CC-20261003-A-REGISTRY-01`; Dong XS et al. 2023, *BMC Med Genomics* 16:291; the placeholder fields above are kept as history
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Identification of compound heterozygous deletion of the WWOX gene in WOREE syndrome

---

## LIT-0119
**Short title:** corpus paper 98
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36257459 / DOI 10.1016/j.lfs.2022.121086
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 98
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Albendazole exerts an anti-hepatocellular carcinoma effect through a WWOX-dependent pathway

---

## LIT-0120
**Short title:** corpus paper 99
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34109992 / DOI 10.3892/or.2021.8108
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 99
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: RHBDD2-WWOX protein interaction during proliferative and differentiated stages in normal and breast cancer cells

---

## LIT-0121
**Short title:** corpus paper 100
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36979157 / DOI 10.3390/biology12030465
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 100
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Antineoplastic Nature of WWOX in Glioblastoma Is Mainly a Consequence of Reduced Cell Viability and Invasion

---

## LIT-0122
**Short title:** corpus paper 101 — **superseded placeholder; do not count as a separate paper and do not cite as unread**. This is the phase-2 corpus-alignment twin of [[paper_registry_current#CORPUS-STUB-101]]; promoting that stub implies retiring this row, which is why it is retired in the same batch and not left saying the paper is undiscovered
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41254692 / DOI 10.1186/s12967-025-07301-9
**Date discovered:** 2026-04-12
**Date processed:** 2026-10-04 — the reading landed at [[literature_tracking_log_current#LIT-0514]] / [[paper_registry_current#PAPER 222]] (`BATCH_20261004_002`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 101
**Status:** superseded
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Integrative multi-omics and Mendelian randomization identify WWOX and THBS2 as potential therapeutic targets in mature T/NK-cell lymphoma

---

## LIT-0123
**Short title:** corpus paper 102
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27550453 / DOI 10.1158/0008-5472.CAN-16-0621
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 102
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 065]] (`BATCH_20260815_001`)
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX and p53 Dysregulation Synergize to Drive the Development of Osteosarcoma

---

## LIT-0124
**Short title:** corpus paper 103
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 29085479 / DOI 10.3892/ol.2017.6747
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 103
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Correlation between osteosarcoma and the expression of WWOX and p53

---

## LIT-0125
**Short title:** corpus paper 104
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25245215 / DOI 10.1007/s00018-014-1724-y
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 104
**Status:** processed
**Status note:** complete_fulltext_read
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001 — receipt `FTR-20260909-25245215-01`
**Note:** Title: The common fragile site FRA16D gene product WWOX: roles in tumor suppression and genomic stability

---
**Evidence depth:** complete_fulltext_read — `FTR-20260909-25245215-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 088]]
**Batch note:** secondary — CMLS chapter 8, the field dedicated WWOX review

## LIT-0126
**Short title:** corpus paper 105
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27834355 / DOI 10.1038/cgt.2016.59
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 105
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX inhibits the invasion of lung cancer cells by downregulating RUNX2

---

## LIT-0127
**Short title:** Nunez 2006 — WWOX protein in normal human tissues (baseline expression atlas)
**Authors:** Nunez MI, Ludes-Meyers J, Aldaz CM
**Year:** 2006
**Source type:** primary descriptive immunohistochemistry atlas (>30 organs; one five-lane immunoblot); not an experiment
**Journal/source:** *J Mol Histol* 37(3-4):115-125
**Identifier type:** PMID / DOI
**Identifier value:** PMID 16941225 / DOI 10.1007/s10735-006-9046-5
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 107
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260913-16941225-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260913-16941225-01`
**Primary pathway:** baseline expression / tissue and cell-type distribution
**Genotype/model tag:** none — normal adult human tissue, no WWOX allele
**Transferability:** T2–T3, baseline only
**clinical relevance:** LOW (background)
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** corpus alignment · `CC-20260913-16941225-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260913-16941225-01`
**Note:** Title: WWOX protein expression in normal human tissues
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-16941225-01`; manifest `deepdive_manifests/PMID16941225.json`
**Registry record:** [[paper_registry_current#PAPER 106]]

---

## LIT-0128
**Short title:** Iatan 2014 — WWOX, HDL e metabolismo lipidico
**Authors:** Iatan I, Choi HY, Ruel I, et al.
**Year:** 2014
**Source type:** primario sperimentale + genetica umana (KO murino epatico e total-body; aplotipo intronico umano)
**Journal/source:** *Circulation: Cardiovascular Genetics* 7:491–504
**Identifier type:** PMID / DOI
**Identifier value:** PMID 24871327 / DOI 10.1161/CIRCGENETICS.113.000248
**Evidence depth:** complete_fulltext_read (2026-08-10) — manifest `deepdive_manifests/PMID24871327.json`
**Registry record:** [[paper_registry_current#PAPER 062]] (promosso da `CORPUS-STUB-108`, BATCH_20260810_004)
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 108
**Status:** processed
**Primary pathway:** P5 — metabolismo lipidico
**Genotype/model tag:** KO murino epatocita-specifico e total-body; aplotipo intronico umano senza saggio funzionale
**Transferability:** T3 — endpoint periferici, nessun endpoint neurale
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: The WWOX gene modulates high-density lipoprotein and lipid metabolism

---

## LIT-0129
**Short title:** corpus paper 109
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33612478 / DOI 10.18632/aging.202514
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 109
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Associations between TUBB-WWOX SNPs, their haplotypes, gene-gene, and gene-environment interactions and dyslipidemia

---

## LIT-0130
**Short title:** De La Cruz 2025 — Wwox P47T heterozygote sepsis and neuroinflammation (preprint)
**Authors:** De La Cruz P, Gomes M, Lockett A, Fisher A, Cook T, Smith P, Lloyd C, Twigg HL, Oblak A, Aldaz CM, Machado RF
**Year:** 2025
**Source type:** PREPRINT (bioRxiv v1, not peer reviewed) — primary experimental, mouse
**Journal/source:** bioRxiv, posted 2025-01-18
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39868255 / DOI 10.1101/2025.01.17.633677
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 110
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260913-39868255-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260913-39868255-01`
**Primary pathway:** P9 — immune / glia / inflammation (neuroinflammation); secondary: extrinsic inflammatory challenge
**Genotype/model tag:** mouse `Wwox WT/P47T` heterozygote + LPS; no WWOX-DEE allele of the reference class
**Transferability:** T3 — preprint, heterozygote, single 12 h endpoint
**clinical relevance:** MEDIUM as a hypothesis generator; LOW as evidence
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** corpus alignment · `CC-20260913-39868255-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260913-39868255-01`
**Note:** Title: Partial Wwox Loss of Function Increases Severity of Murine Sepsis and Neuroinflammation [PREPRINT bioRxiv]
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-39868255-01`; manifest `deepdive_manifests/PMID39868255.json`
**Registry record:** [[paper_registry_current#PAPER 114]]

---

## LIT-0131
**Short title:** corpus paper 111
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 37615513 / DOI 10.1002/ijc.34703
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 111
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Remote modulation of WWOX by an intronic variant associated with survival of Chinese gastric cancer patients

---

## LIT-0132
**Short title:** corpus paper 112
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33718178 / DOI 10.3389/fonc.2021.621060
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 112
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Fragile Gene WWOX Guides TFAP2A/TFAP2C-Dependent Actions Against Tumor Progression in Grade II Bladder Cancer

---

## LIT-0133
**Short title:** corpus paper 113
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 38499540 / DOI 10.1038/s41420-024-01878-8
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 113
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Unveiling the relationship between WWOX and BRCA1 in mammary tumorigenicity and in DNA repair pathway selection

---

## LIT-0134
**Short title:** corpus paper 114
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25411445 / DOI 10.1136/jmedgenet-2014-102748
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 114
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX-related encephalopathies: delineation of the phenotypical spectrum and emerging genotype-phenotype correlation

---

## LIT-0135
**Short title:** corpus paper 115
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25802472 / DOI 10.1177/1535370215574226
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 115
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Introduction to a thematic issue for WWOX

---

## LIT-0136
**Short title:** corpus paper 116
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35563688 / DOI 10.3390/cells11091382
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 116
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Determination of WWOX Function in Modulating Cellular Pathways Activated by AP-2alpha and AP-2gamma Transcription Factors in Bladder Cancer

---

## LIT-0137
**Short title:** corpus paper 117
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 24393846 / DOI 10.1016/j.bbrc.2013.12.133
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 117
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Wwox suppresses breast cancer cell growth through modulation of the hedgehog-GLI1 signaling pathway

---

## LIT-0138
**Short title:** corpus paper 119
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 16223882 / DOI 10.1073/pnas.0505485102
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 119
**Status:** processed
**Status note:** complete_fulltext_read
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001 — receipt `FTR-20260909-16223882-01`
**Note:** Title: WWOX gene restoration prevents lung cancer growth in vitro and in vivo

---
**Evidence depth:** complete_fulltext_read — `FTR-20260909-16223882-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 082]]
**Batch note:** background_only — reagent provenance; STANDING EXPRESSION OF CONCERN (PMID 28373548)

## LIT-0139
**Short title:** corpus paper 120
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 38563965 / DOI 10.1152/ajplung.00277.2023
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 120
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Endothelial knockdown of WWOX increases inflammation in ventilator-induced lung injury

---

## LIT-0140
**Short title:** corpus paper 121
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 22484428 / DOI 10.3892/mmr.2012.860
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 121
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX-mediated apoptosis in A549 cells mainly involves the mitochondrial pathway

---

## LIT-0141
**Short title:** corpus paper 122
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 23849374 / DOI 10.1016/j.oooo.2013.05.007
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 122
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX expression in giant cell lesions of the jaws

---

## LIT-0142
**Short title:** corpus paper 123
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27308504 / DOI 10.1080/23723556.2015.1008288
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 123
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX guards genome stability by activating ATM

---

## LIT-0143
**Short title:** corpus paper 124
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31752354 / DOI 10.3390/cancers11111818
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 124
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Possesses N-Terminal Cell Surface-Exposed Epitopes WWOX7-21 and WWOX7-11 for Signaling Cancer Growth Suppression

---

## LIT-0144
**Short title:** corpus paper 125
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 26390919 / DOI 10.1002/gcc.22286
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 125
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Tumor suppressor WWOX moderates the mitochondrial respiratory complex

---

## LIT-0145
**Short title:** corpus paper 126
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 28749468 / DOI 10.1038/cddis.2017.346
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 126
**Status:** processed
**Status note:** 🟢 **Enriched 2026-10-03 by `CC-20261003-C-REGISTRY-01`** from the stub state (*«not yet extracted»*, *«not yet screened»*) on a first-hand reading: Janczar S, Nautiyal J, Xiao Y, Curry E, Sun M, Zanini E, Paige AJW, Gabra H, *Cell Death Dis* 2017;8(7):e2955, primary research — cell-line experimental plus two public microarray survival cohorts. `partial_fulltext_read` — receipt `FTR-20261003-28749468-01`; manifest `deepdive_manifests/PMID28749468.json` (9 verbatim locators, PASS with artefact verification); dossier `research/fulltext_dossiers/PMID28749468.md`. Body, all eight figure images and the full supplementary legend set read; the nine-page supplementary figure PDF not inspected panel by panel; 52-item reference list enumerated and screened mechanically (`SCREENED_CLEAN`), not read. Primary pathway: ER stress / UPR (oncological context). Genotype/model tag: human ovarian carcinoma lines, PEO1 being a WWOX-null by homozygous deletion of exons 4-8; no WWOX allele of the reference genotype class and no neural material. Transferability: T3. clinical relevance: BACKGROUND. 🔴 Every quantified endpoint measures WWOX as **pro-death under stress**, so a «rescue» in this system means restoring the cell's ability to die — recorded in `CC-20261003-C-APOPTOSIS-DIRECTION-01`, which also qualifies `DL-MECH-023` because Figures 5c-5e carry no significance marker and the KIRA6 viability increment is the same in the WWOX-expressing and WWOX-null clones. Not medical advice.
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX sensitises ovarian cancer cells to paclitaxel via modulation of the ER stress response

---

## LIT-0146
**Short title:** corpus paper 127
**Authors:** not yet extracted
**Year:** unknown
**Source type:** corpus placeholder
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39420317 / DOI 10.1186/s12964-024-01866-6
**Date discovered:** 2026-04-12
**Date processed:** superseded by LIT-0205 on 2026-04-18
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 127
**Status:** superseded
**Primary pathway:** signaling organization / stress-contingent partner switching
**Genotype/model tag:** placeholder only
**Transferability:** T3 mechanistic / indirect
**clinical relevance:** LOW
**Claim links:** 028 supportive only
**Working Model impact:** none
**Report mentions:** corpus alignment; session deep dive 2026-04-18
**Next action:** none — upgraded to LIT-0205
**Flags:** corpus placeholder / superseded
**Note:** Title: Dissociation of the nuclear WWOX/TRAF2 switch renders UV/cold shock-mediated nuclear bubbling cell death at low temperatures. Preserved for lossless corpus alignment; full processed record now lives in LIT-0205.

---

## LIT-0147
**Short title:** corpus paper 128
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33455117
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 128
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Methylation of WWOX gene promotes proliferation of osteosarcoma cells

---

## LIT-0148
**Short title:** corpus paper 129
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30154439 / DOI 10.1038/s41467-018-05852-8
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 129
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Loss of Wwox drives metastasis in triple-negative breast cancer by JAK2/STAT3 axis

---

## LIT-0149
**Short title:** Ludes-Meyers 2003 — WWOX/FRA16D cancer gene (antibody-chain terminus)
**Authors:** Ludes-Meyers JH, Bednarek AK, Popescu NC, Bedford M, Aldaz CM
**Year:** 2003
**Source type:** review-shaped article carrying its own primary data — 8 figures, 0 tables, ~56 references; PubMed declares `['Journal Article']` with no Review tag
**Journal/source:** *Cytogenet Genome Res* 100(1-4):101-110
**Identifier type:** PMID / DOI
**Identifier value:** PMID 14526170 / DOI 10.1159/000072844
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 130
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260913-14526170-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260913-ALDAZ-B004-01`
**Primary pathway:** none — methodological / reagent provenance; it measures no pathway
**Genotype/model tag:** none — human cancer cell lines and mouse xenograft; no WWOX allele of interest
**Transferability:** **T-none** toward the reference genotype, and deliberately not more
**clinical relevance:** LOW — unchanged; its value is entirely methodological and upstream
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** corpus alignment · `CC-20260913-ALDAZ-B004-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260913-14526170-01`
**Note:** Title: WWOX, the common chromosomal fragile site, FRA16D, cancer gene
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-14526170-01`; manifest `deepdive_manifests/PMID14526170.json`
**Registry record:** [[paper_registry_current#PAPER 101]]

---

## LIT-0150
**Short title:** corpus paper 131
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33129329 / DOI 10.1186/s12917-020-02638-3
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 131
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Characterization of WWOX expression and function in canine mast cell tumors and malignant mast cell lines

---

## LIT-0151
**Short title:** corpus paper 132
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32368285 / DOI 10.7150/jca.40840
**Date discovered:** 2026-04-12
**Date processed:** 2026-10-04 — read at full text in intake wave 7 and recorded at [[literature_tracking_log_current#LIT-0494]]
**Status note:** superseded — duplicate identity. This row is the phase-2 corpus-alignment **placeholder** twin of [[paper_registry_current#CORPUS-STUB-132]] for PMID 32368285, and the reading landed at [[literature_tracking_log_current#LIT-0494]] with [[paper_registry_current#PAPER 201]] (`BATCH_20261004_001`, 2026-10-04). 🔴 **Count this PMID once, at `LIT-0494`.** `CC-20261004W7-A-REGISTRY-01` stated that the PMID had no LIT record; it had this one, and the integrator's post-propagation identity census found the duplicate. Retired rather than deleted, and pointed at its replacement, exactly as the corpus stub is
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 132
**Status:** superseded
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — superseded by [[literature_tracking_log_current#LIT-0494]]
**Flags:** corpus placeholder / **superseded by `LIT-0494`** — do not count as a separate paper and do not cite as unread
**Note:** Title: Silencing of Wwox Increases Nuclear Import of Dvl proteins in Head and Neck Cancer

---

## LIT-0152
**Short title:** corpus paper 133
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 11572989 / DOI 10.1073/pnas.191175898
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 133
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX: a candidate tumor suppressor gene involved in multiple tumor types

---

## LIT-0153
**Short title:** corpus paper 134
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32314321 / DOI 10.1007/s10792-020-01368-7
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 134
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Analysis of WWOX gene expression and protein levels in pterygium

---

## LIT-0154
**Short title:** corpus paper 135
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 16360296 / DOI 10.1016/j.ejso.2005.11.002
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 135
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX — the FRA16D cancer gene: expression correlation with breast cancer progression and prognosis

---

## LIT-0155
**Short title:** corpus paper 136
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 32931356 / DOI 10.1080/15384047.2020.1806689
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 136
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: LncRNA WWOX-AS1 sponges miR-20b-5p in hepatocellular carcinoma and represses its progression by upregulating WWOX

---

## LIT-0156
**Short title:** corpus paper 137
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 24126431 / DOI 10.3892/ijmm.2013.1526
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 137
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: The WWOX tumor suppressor gene in endometrial adenocarcinoma

---

## LIT-0157
**Short title:** PNAS 2014 ATM/DDR
**Authors:** Schrock et al.
**Year:** 2014
**Source type:** primary mechanistic DDR study
**Journal/source:** *PNAS*
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25331887 / DOI 10.1073/pnas.1409252111
**Date discovered:** 2026-04-12
**Date processed:** 2026-04-17
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 138
**Status:** integrated
**Primary pathway:** genome stability / ATM / DNA damage response
**Genotype/model tag:** cellular DDR systems / WWOX deficiency / non-CNS pediatric direct
**Transferability:** T2 conceptual / indirect
**clinical relevance:** LOW direct / MEDIUM structural
**Claim links:** 029
**Working Model impact:** adds candidate ATM/DDR structural axis; no BLOCCO 1 change
**Report mentions:** corpus alignment; post-181–220 propagation
**Next action:** seek neurodevelopmental convergence (progenitor stress, γH2AX / 53BP1 VZ findings, ATR branch) before promoting to central pathway or full research line
**Flags:** primary full text available; new propagation candidate
**Note:** Title: WWOX, the common fragile site FRA16D gene product, regulates ATM activation and the DNA damage response. Integrated as the first true new-propagation paper after the initial 181–220 commit.

---

## LIT-0158
**Short title:** corpus paper 139
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 24008736 / DOI 10.1038/cddis.2013.308
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 139
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none - screened and read on 2026-10-03 (`partial_fulltext_read`, per its receipt) (integrator amendment, `BATCH_20261003_002`) (intake wave 3, Scientist B); promoted to [[paper_registry_current#PAPER 148]] by `CC-20261003W3-B-REGISTRY-01`
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX suppresses autophagy for inducing apoptosis in methotrexate-treated human squamous cell carcinoma

---

## LIT-0159
**Short title:** corpus paper 140
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 23525648 / DOI 10.3892/or.2013.2361
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 140
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: The role of the WWOX gene in leukemia and its mechanisms of action

---

## LIT-0160
**Short title:** corpus paper 141
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35712340 / DOI 10.7759/cureus.25003
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 141
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none — processed 2026-10-03 (`FTR-20261003-35712340-01`, `complete_fulltext_read`) and promoted to [[paper_registry_current#PAPER 144]] by `CC-20261003W3-A-REGISTRY-01`; Sukkar G et al. 2022, *Cureus* 14(5):e25003; a non-DEE homozygous missense with unproven attribution; the placeholder fields above are kept as history
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Novel Mutation With Literature Review WW Domain-Containing Oxidoreductase (WWOX) Gene

---

## LIT-0161
**Short title:** corpus paper 142
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31966508
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 142
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX suppresses proliferation and induces apoptosis via G2 arrest and caspase 3 pathway in nasopharyngeal carcinoma cells

---

## LIT-0162
**Short title:** Ludes-Meyers 2004 — WWOX WW1 binds the PPxY ligand; five array candidates
**Authors:** Ludes-Meyers JH, Kil H, Bednarek AK, Drake J, Bedford MT, Aldaz CM
**Year:** 2004
**Source type:** primary experimental — WW-domain interaction biochemistry (NIH author manuscript NIHMS222052)
**Journal/source:** *Oncogene* 23(29):5049-5055
**Identifier type:** PMID / DOI
**Identifier value:** PMID 15064722 / DOI 10.1038/sj.onc.1207680
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 143
**Status:** claim_linked
**Status note:** complete_fulltext_read — `FTR-20260913-15064722-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260913-15064722-01`; linked to CLAIM 007 by `BATCH_20260926_ALDAZ_R7`
**Primary pathway:** P3 — interaction logic / WW-domain scaffold
**Genotype/model tag:** in vitro + MCF-7; no WWOX disease variant, no neural cell, tissue or system
**Transferability:** T3 — domain logic only
**clinical relevance:** LOW
**Claim links:** 007 — mechanistic antecedent only; P47T measurement is in `PAPER 007`
**Working Model impact:** `BATCH_20260926_ALDAZ_R7` (WM_v5.6): bounded in-vitro provenance added to CLAIM 007, without altering its P47T result
**Report mentions:** corpus alignment · `CC-20260913-15064722-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260913-15064722-01`
**Note:** Title: WWOX binds the specific proline-rich ligand PPXY: identification of candidate interacting proteins
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-15064722-01`; manifest `deepdive_manifests/PMID15064722.json`
**Registry record:** [[paper_registry_current#PAPER 104]]

---

## LIT-0163
**Short title:** corpus paper 145
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 23675860 / DOI 10.1111/neup.12040
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 145
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Reduced WWOX protein expression in human astrocytoma

---

## LIT-0164
**Short title:** corpus paper 146
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 23525362 / DOI 10.3892/ijmm.2013.1314
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 146
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX induces apoptosis and inhibits proliferation in cervical cancer and cell lines

---

## LIT-0165
**Short title:** corpus paper 147
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41677633 / DOI 10.3390/cells15030270
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 147
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** none - screened and read on 2026-10-03 (`partial_fulltext_read`, per its receipt) (integrator amendment, `BATCH_20261003_002`) (intake wave 3, Scientist B); promoted to [[paper_registry_current#PAPER 147]] by `CC-20261003W3-B-REGISTRY-01`
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Induction Promotes Bcl-XL and Mcl-1 Degradation Through a Lysosomal Pathway upon Stress Response

---

## LIT-0166
**Short title:** Nunez 2005 — WWOX protein across ovarian carcinoma histotypes (reagent paper of record)
**Authors:** Nunez MI, Rosen DG, Ludes-Meyers JH, Abba MC, Kil H, Page R, Klein-Szanto AJP, Godwin AK, Liu J, Mills GB, Aldaz CM
**Year:** 2005
**Source type:** primary descriptive IHC + immunoblot series on pooled tissue microarrays (444 invasive epithelial ovarian carcinomas); not an experiment
**Journal/source:** *BMC Cancer* 5:64
**Identifier type:** PMID / DOI
**Identifier value:** PMID 15982416 / DOI 10.1186/1471-2407-5-64
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 148
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260913-15982416-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260913-ALDAZ-B003-01`
**Primary pathway:** baseline expression / tumour-tissue protein loss — explicitly not P5
**Genotype/model tag:** none — human somatic tumour tissue, no WWOX allele
**Transferability:** T3, `ESPANSIONE`
**clinical relevance:** LOW — unchanged
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** corpus alignment · `CC-20260913-ALDAZ-B003-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260913-15982416-01`
**Note:** Title: WWOX protein expression varies among ovarian carcinoma histotypes and correlates with less favorable outcome (corrected from *"…less favorable prognosis"*, which is not the article's title; `CC-20260913-ALDAZ-B003-01` §1.1)
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-15982416-01`; manifest `deepdive_manifests/PMID15982416.json`
**Registry record:** [[paper_registry_current#PAPER 105]]

---

## LIT-0167
**Short title:** corpus paper 149
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 17704139 / DOI 10.1158/1541-7786.MCR-07-0211
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 149
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Wwox suppresses prostate cancer cell growth through modulation of ErbB2-mediated androgen receptor signaling

---

## LIT-0168
**Short title:** corpus paper 150
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34140629 / DOI 10.1038/s42003-021-02271-2
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 150
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Normal cells repel WWOX-negative or -dysfunctional cancer cells via WWOX cell surface epitope 286-299

---

## LIT-0169
**Short title:** corpus paper 152
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 26256646 / DOI 10.1038/srep12959
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-11
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 152
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 074]] (`BATCH_20260815_001`)
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Tumor Suppressor WWOX inhibits osteosarcoma metastasis by modulating RUNX2 function

---

## LIT-0170
**Short title:** corpus paper 153
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33565365 / DOI 10.1369/0022155421991629
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 153
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Cellular Expression and Subcellular Localization of Wwox Protein During Testicular Development and Spermatogenesis

---

## LIT-0171
**Short title:** corpus paper 154
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 33688485 / DOI 10.22088/IJMCM.BUMS.9.4.273
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 154
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Downregulated Expression of WWOX in Cervical Carcinoma: A Case-Control Study

---

## LIT-0172
**Short title:** corpus paper 155
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35290621 / DOI 10.1007/s13353-022-00690-3
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 155
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: TGFalpha-EGFR pathway in breast carcinogenesis, association with WWOX expression and estrogen activation

---

## LIT-0173
**Short title:** corpus paper 156
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27551439 / DOI 10.1038/cddiscovery.2015.3
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 156
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX dysfunction induces sequential aggregation of TRAPPC6ADelta, TIAF1, tau and amyloid beta, and causes apoptosis

---

## LIT-0174
**Short title:** corpus paper 157
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35559044 / DOI 10.3389/fgene.2022.843661
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 157
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: EHBP1, TUBB, and WWOX SNPs, Gene-Gene and Gene-Environment Interactions on Coronary Artery Disease and Hypertension

---

## LIT-0175
**Short title:** corpus paper 158
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 19458077 / DOI 10.1158/0008-5472.CAN-08-2974
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 158
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX gene expression abolishes ovarian cancer tumorigenicity in vivo and decreases attachment to fibronectin via the ITGA3 integrin

---

## LIT-0176
**Short title:** corpus paper 159
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 29845204 / DOI 10.3892/mmr.2018.9058
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 159
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: LncRNA WWOX-AS1 inhibits the proliferation, migration and invasion of osteosarcoma cells

---

## LIT-0177
**Short title:** corpus paper 160
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 17289881 / DOI 10.1158/1078-0432.CCR-06-2016
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 160
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX expression in different histologic types and subtypes of non-small cell lung cancer

---

## LIT-0178
**Short title:** corpus paper 161
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27840941 / DOI 10.3892/ijmm.2016.2800
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 161
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Deregulated WWOX is involved in a negative feedback loop with microRNA-214-3p in osteosarcoma

---

## LIT-0179
**Short title:** corpus paper 162
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25051421 / DOI 10.3892/or.2014.3335
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 162
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX modulates the gene expression profile in the T98G glioblastoma cell line rendering its phenotype

---

## LIT-0180
**Short title:** corpus paper 164
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30082886 / DOI 10.1038/s41419-018-0896-z
**Date discovered:** 2026-04-12
**Date processed:** 2026-08-10
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 164
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 066]] (`BATCH_20260815_001`)
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Somatic loss of WWOX is associated with TP53 perturbation in basal-like breast cancer

---

## LIT-0181
**Short title:** Bonin 2018 — VOPP1–WWOX via WW1 and PPPY¹⁶⁵
**Authors:** Bonin F, Taouis K, Azorin P, Petitalot A, Tariq Z, Nola S, Bouteille N, Tury S, Vacher S, Bièche I, Ait Rais K, Pierron G, Fuhrmann L, Vincent-Salomon A, Formstecher E, Camonis J, Lidereau R, Lallemand F, Driouch K (as in `PAPER 103`)
**Year:** 2018
**Source type:** primary experimental — interaction biochemistry, cell biology, and a retrospective series of 448 human tumours
**Journal/source:** *BMC Biol* 16:109
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30285739 / DOI 10.1186/s12915-018-0576-6
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 165
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-30285739-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-30285739-01`
**Primary pathway:** P5 — trafficking / endomembrane
**Genotype/model tag:** cell lines, SCID xenograft and human tumour series; no neural material and no WWOX disease variant
**Transferability:** T3
**clinical relevance:** LOW — unchanged: a breast-oncology axis in non-neural systems; its value to this corpus is mechanistic, not clinical
**Claim links:** 026 — VOPP1 interaction limb only
**Working Model impact:** none in this batch — the candidate's `CLAIM 026` sentence is held for the claim batch
**Report mentions:** corpus alignment · `CC-20260914-30285739-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-30285739-01`
**Note:** Title: VOPP1 promotes breast tumorigenesis by interacting with the tumor suppressor WWOX
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-30285739-01`; manifest `deepdive_manifests/PMID30285739.json`
**Registry record:** [[paper_registry_current#PAPER 103]]

---

## LIT-0182
**Short title:** corpus paper 166
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34034642 / DOI 10.1080/01616412.2021.1932173
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 166
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Recently defined epileptic encephalopathy related to WWOX gene mutation: six patients and new mutations

---

## LIT-0183
**Short title:** corpus paper 167
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31532107 / DOI 10.7754/Clin.Lab.2019.190119
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 167
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: High and Low WWOX Gene Expression Levels in Acute Myeloid Leukemia

---

## LIT-0184
**Short title:** Ferguson 2012 — conditional Wwox deletion in mouse mammary gland (BK5-Cre, MMTV-Cre)
**Authors:** Ferguson BW, Gao X, Kil H, Lee J, Benavides F, Abba MC, Aldaz CM
**Year:** 2012
**Source type:** primary research — genetica murina condizionale (sopravvivenza, morfometria, trascrittoma)
**Journal/source:** *PLoS ONE* 7(5):e36618
**Identifier type:** PMID / DOI
**Identifier value:** PMID 22574198 / DOI 10.1371/journal.pone.0036618
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 168
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-22574198-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-22574198-01`
**Primary pathway:** P7 — gene therapy readiness / dose-threshold logic (mammary leg of `CLAIM 032`); secondary: oncology
**Genotype/model tag:** delezione condizionale murina tessuto-ristretta; nessun materiale neurale; nessun allele WWOX umano
**Transferability:** T3 (T2 indiretta per il solo confine di dose)
**clinical relevance:** MODERATE
**Claim links:** none — held for the claim batch
**Working Model impact:** none in this batch — the `CLAIM 032` source addition is held for the claim batch
**Report mentions:** corpus alignment · `CC-20260914-22574198-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-22574198-01`
**Note:** Title: Conditional Wwox deletion in mouse mammary gland by means of two Cre recombinase approaches
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-22574198-01`; manifest `deepdive_manifests/PMID22574198.json`
**Registry record:** [[paper_registry_current#PAPER 107]]

---

## LIT-0185
**Short title:** corpus paper 169
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 16818616 / DOI 10.1158/0008-5472.CAN-06-0956
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 169
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** MED
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: A role for the WWOX gene in prostate cancer

---

## LIT-0186
**Short title:** corpus paper 170
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 15131042 / DOI 10.1158/1078-0432.ccr-03-0594
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 170
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Loss of WWOX expression in gastric carcinoma

---

## LIT-0187
**Short title:** corpus paper 171
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 20480411 / DOI 10.1007/s13277-010-0039-3
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 171
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX gene may contribute to progression of non-small-cell lung cancer (NSCLC)

---

## LIT-0188
**Short title:** corpus paper 172
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 23254778 / DOI 10.1002/jcp.24310
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 172
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Characterization of WWOX inactivation in murine mammary gland development

---

## LIT-0189
**Short title:** corpus paper 173
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27773744 / DOI 10.1016/j.jbior.2016.09.008
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 173
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Fhit and Wwox loss-associated genome instability: A genome caretaker one-two punch

---

## LIT-0190
**Short title:** corpus paper 174
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27352332 / DOI 10.1007/s12013-015-0654-0
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 174
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: Ectopic WWOX Expression Inhibits Growth of 5637 Bladder Cancer Cell In Vitro and In Vivo

---

## LIT-0191
**Short title:** corpus paper 175
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39416860 / DOI 10.3389/fped.2024.1453778
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 175
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** HIGH
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX-related epileptic encephalopathy caused by a novel mutation in the WWOX gene: a case report

---

## LIT-0192
**Short title:** corpus paper 176
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 25400415 / DOI 10.3978/j.issn.1000-9604.2014.09.03
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 176
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX suppresses KLF5 expression and breast cancer cell growth

---

## LIT-0193
**Short title:** corpus paper 177
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31966718
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 177
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: EBV-LMP1 regulating AKT/mTOR signaling pathway and WWOX in nasopharyngeal carcinoma

---

## LIT-0194
**Short title:** Hussain 2025 — B-cell Wwox deletion in the Vk∗MYC myeloma model
**Authors:** Hussain T, Bramble MD, Liu B, Abba MC, Chesi M, Aldaz CM
**Year:** 2025
**Source type:** primary research — cross-model mouse cohort + RNA-seq/WES genomics + public-dataset re-analysis
**Journal/source:** *Blood Neoplasia* 2(4):100153
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41090157 / DOI 10.1016/j.bneo.2025.100153
**Date discovered:** 2026-04-12
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 178
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-41090157-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-41090157-01`
**Primary pathway:** genome stability / DNA damage response (secondary: inflammation)
**Genotype/model tag:** murine B/plasma-cell lineage on a MYC-driven background; no WWOX disease allele; no neural material
**Transferability:** T3
**clinical relevance:** LOW — unchanged
**Claim links:** none — held for the claim batch
**Working Model impact:** none in this batch — the `CLAIM 029` sentence is held for the claim batch
**Report mentions:** corpus alignment · `CC-20260914-41090157-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-41090157-01`
**Note:** Title: B-cell-specific Wwox deletion promotes plasmablastic tumor development and proinflammatory signature
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-41090157-01`; manifest `deepdive_manifests/PMID41090157.json`
**Registry record:** [[paper_registry_current#PAPER 115]]

---

## LIT-0195
**Short title:** corpus paper 179
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 23446842 / DOI 10.3892/ijmm.2013.1289
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 179
**Status:** discovered
**Primary pathway:** unassigned
**Genotype/model tag:** unassigned
**Transferability:** unassigned
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none yet
**Report mentions:** corpus alignment
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: p73 participates in WWOX-mediated apoptosis in leukemia cells

---

## Tracking update — papers 181–220
**Date:** 2026-04-17
**Commit:** 181–220

### Deep-dive / high-confidence
- **182** — full text deep — WWOX interactome / trafficking–metabolism coupling → CLAIM 026 — source normalized 2026-07-05 to [[paper_registry_current#PAPER 032]] (PMID 30619736 / PMCID PMC6300487 / DOI 10.3389/fonc.2018.00591)
- **191** — full text deep — WWOX/HIF1A axis in human non-tumoral GDM → CLAIM 025
- **204** — deep, high-confidence, partial-access structural analysis — WW1–WW2 tandem cooperativity → CLAIM 024
- **206** — deep, high-confidence, partial-access mechanistic analysis — WWOX–p73 routing/scaffold → CLAIM 023
- **210** — deep, high-confidence, partial/full-text-limited but strong analysis — neocortical hyperexcitability / oscillatory pathology → CLAIM 021 — source normalized 2026-07-05 to [[paper_registry_current#PAPER 031]] (PMID 34634460 / PMCID PMC8609180 / DOI 10.1016/j.nbd.2021.105529)
- **214** — deep with supporting experimental paper — HYAL-2 / WWOX / SMAD4 ECM signaling → CLAIM 027
- **216** — deep, high-confidence, partial-access human case analysis — prenatal null-severe onset → CLAIM 022
- **207** — deep, high-confidence, partial-access translational analysis — context-dependence support → CLAIM 028

### Advanced triage only
- remaining papers in 181–220 (181, 183, 185, 188, 189, 190, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 205, 208, 209, 211, 215, 217, 219, 220)

### Notes
- Commit 181–220 is based not only on batch triage but on focused deep-dive escalation of the most model-shifting papers.
- Claims generated: CLAIM 021–028 (added to claim_registry_current.md v1.5)
- Working Model: v1.6 — Mechanistic Architecture section added; BLOCCO 1 unchanged
- Meta files updated: meta_metabolism v1.1, meta_human_spectrum v1.1, meta_prenatal_structure v1.1
- Research lines added: RL-NET-001, RL-MET-002, RL-PREN-002, RL-ARCH-001, RL-ECM-001
- Research candidates added: RC-007–011

---


---

# FASE 1 TRIAGE — PAPERS 221–400

**Date:** 2026-04-18
**Batch source:** 400_paper.txt (papers 221–400)
**Total entries created:** 179 (180 paper range − 1 dedup)
**Dedup:** LIT-0264 skipped — PMID 39101447 already integrated as PAPER 016 / LIT-0116 (You 2024)
**Numbering:** LIT-NNNN aligned to paper number N in 400_paper.txt
**Processing depth:** triage only — screened, tier-assigned, no deep-dive

## Tier distribution

- **Tier A (priority full-text):** 7 papers — P294, P298, P300, P356, P359, P365, P383
- **Tier B (secondary full-text):** 16 papers — P222, P225, P242, P253, P263, P295, P301, P309, P318, P327, P333, P343, P362, P363, P372, P395
- **Tier C (background corpus):** 156 papers — all remaining in 221–400 minus P264

## Rationale for batch processing at triage level

LEGEND v3.2 RULE 3 (zero data loss) and RULE 8 (loss > elegance) prevail: the full 180-paper
range is committed to `literature_tracking_log_current.md` with structured triage-level
metadata, even when individual papers are background-only. Tier-A and tier-B entries are
promoted via `full_text_queue_current.md` in next-session operations.

## Triage-level field policy

At this depth, the following fields remain **unassigned**:
- Genotype/model tag (requires abstract-level or full-text review)
- Transferability (T1/T2/T3 assignment requires depth pass)
- Directness to the reference genotype
- Claim links

Pathway assignment uses **title+abstract keyword heuristics**, flagged as preliminary.
clinical relevance is **tier-aware**: tier A ≥ MODERATE-HIGH baseline, tier B ≈ MODERATE baseline,
tier C ≈ LOW unless clinical-DEE content is explicit.

## Open debts flagged in this commit

1. **Count discrepancy**: operator instruction stated 178 entries; real count from
   400_paper.txt source is 179 (180 paper − 1 P264 dedup). Applied 179; no known
   additional dedup target in 221–400.
2. **Gap in LIT sequence**: LIT-0196..0220 (except LIT-0205) remain without tracking
   entries. These correspond to papers 181–220 deep-dived in the prior session (commit
   181–220) but not backfilled into `literature_tracking_log_current.md` as full LIT
   entries. This debt is **pre-existing** and is **not resolved** in this FASE 1 commit.

---

## LIT-0221
**Short title:** WWOX tumour suppressor gene polymorphisms and ovarian cancer pathology and pr...
**Authors:** Paige et al.
**Year:** 2010
**Source type:** Multicenter Study
**Journal/source:** Eur J Cancer
**Identifier:** PMID 20074932 / DOI 10.1016/j.ejca.2009.12.021
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 221
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WWOX tumour suppressor gene polymorphisms and ovarian cancer pathology and prognosis

## LIT-0222
**Short title:** The WWOX tumor suppressor is essential for postnatal survival and normal bone...
**Authors:** Aqeilan et al.
**Year:** 2008
**Source type:** Article
**Journal/source:** J Biol Chem
**Identifier:** PMID 18487609 / PMC2490770 / DOI 10.1074/jbc.M800855200
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 222
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The WWOX tumor suppressor is essential for postnatal survival and normal bone metabolism

## LIT-0223
**Short title:** Correlation of WWOX, RUNX2 and VEGFA protein expression in human osteosarcoma
**Authors:** Yang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** BMC Med Genomics
**Identifier:** PMID 24330824 / PMC3878685 / DOI 10.1186/1755-8794-6-56
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 223
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P8 — bone / RUNX2 axis
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Correlation of WWOX, RUNX2 and VEGFA protein expression in human osteosarcoma

## LIT-0224
**Short title:** Deletion of the WWOX gene and frequent loss of its protein expression in huma...
**Authors:** Yang et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Cancer Lett
**Identifier:** PMID 19896763 / DOI 10.1016/j.canlet.2009.09.018
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 224
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P8 — bone / RUNX2 axis
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Deletion of the WWOX gene and frequent loss of its protein expression in human osteosarcoma

## LIT-0225
**Short title:** Identification of a novel splice-site WWOX variant with paternal uniparental...
**Authors:** Nishino et al.
**Year:** 2024
**Source type:** Case Reports
**Journal/source:** Am J Med Genet A
**Identifier:** PMID 38407561 / DOI 10.1002/ajmg.a.63575
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 225
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Identification of a novel splice-site WWOX variant with paternal uniparental isodisomy in a patient with infantile epileptic encephalopathy

## LIT-0226
**Short title:** A WWOX-binding molecule, transmembrane protein 207, is related to the invasiv...
**Authors:** Takeuchi et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Carcinogenesis
**Identifier:** PMID 22226915 / DOI 10.1093/carcin/bgs001
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 226
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: A WWOX-binding molecule, transmembrane protein 207, is related to the invasiveness of gastric signet-ring cell carcinoma

## LIT-0227
**Short title:** Hypermethylation-mediated reduction of WWOX expression in intraductal papilla...
**Authors:** Nakayama et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Br J Cancer
**Identifier:** PMID 19352382 / PMC2694421 / DOI 10.1038/sj.bjc.6604986
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 227
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Hypermethylation-mediated reduction of WWOX expression in intraductal papillary mucinous neoplasms of the pancreas

## LIT-0228
**Short title:** Expression of ORAOV1, CD133 and WWOX correlate with metastasis and prognosis...
**Authors:** Lu et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Int J Clin Exp Pathol
**Identifier:** PMID 31966760 / PMC6965444
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 228
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Expression of ORAOV1, CD133 and WWOX correlate with metastasis and prognosis in gastric adenocarcinoma

## LIT-0229
**Short title:** Role of WW Domain-containing Oxidoreductase WWOX in Driving T Cell Acute Lymp...
**Authors:** Huang et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** J Biol Chem
**Identifier:** PMID 27339895 / PMC5016130 / DOI 10.1074/jbc.M116.716167
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 229
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Role of WW Domain-containing Oxidoreductase WWOX in Driving T Cell Acute Lymphoblastic Leukemia Maturation

## LIT-0230
**Short title:** Molecular alterations of the WWOX gene in nasopharyngeal carcinoma
**Authors:** Yang et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Neoplasma
**Identifier:** PMID 24299313 / DOI 10.4149/neo_2014_023
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 230
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Molecular alterations of the WWOX gene in nasopharyngeal carcinoma

## LIT-0231
**Short title:** TMEM207 hinders the tumour suppressor function of WWOX in oral squamous cell...
**Authors:** Bunai et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** J Cell Mol Med
**Identifier:** PMID 29164763 / PMC5783854 / DOI 10.1111/jcmm.13456
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 231
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: TMEM207 hinders the tumour suppressor function of WWOX in oral squamous cell carcinoma

## LIT-0232
**Short title:** Molecular analysis of WWOX expression correlation with proliferation and apop...
**Authors:** Kosla et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** J Neurooncol
**Identifier:** PMID 20535528 / PMC2996532 / DOI 10.1007/s11060-010-0254-1
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 232
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Molecular analysis of WWOX expression correlation with proliferation and apoptosis in glioblastoma multiforme

## LIT-0233
**Short title:** Wwox expression may predict benefit from adjuvant tamoxifen in randomized bre...
**Authors:** Eremo et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Oncol Rep
**Identifier:** PMID 23381945 / DOI 10.3892/or.2013.2261
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 233
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Wwox expression may predict benefit from adjuvant tamoxifen in randomized breast cancer patients

## LIT-0234
**Short title:** Angiomotin Counteracts the Negative Regulatory Effect of Host WWOX on Viral P...
**Authors:** Liang et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** J Virol
**Identifier:** PMID 33536174 / PMC8103691 / DOI 10.1128/JVI.00121-21
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 234
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** animal model — pathway variable
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Angiomotin Counteracts the Negative Regulatory Effect of Host WWOX on Viral PPxY-Mediated Egress

## LIT-0235
**Short title:** Exosomal miR-625-3p secreted by cancer-associated fibroblasts in colorectal c...
**Authors:** Zhang et al.
**Year:** 2022
**Source type:** Article
**Journal/source:** Pharmacol Res
**Identifier:** PMID 36336217 / DOI 10.1016/j.phrs.2022.106534
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 235
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Exosomal miR-625-3p secreted by cancer-associated fibroblasts in colorectal cancer promotes EMT and chemotherapeutic resistance by blocking the CELF2/WWOX pathway

## LIT-0236
**Short title:** WWOX CNV-67048 Functions as a Risk Factor for Epithelial Ovarian Cancer in Ch...
**Authors:** Chen et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Biomed Res Int
**Identifier:** PMID 27190995 / PMC4842385 / DOI 10.1155/2016/6594039
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 236
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WWOX CNV-67048 Functions as a Risk Factor for Epithelial Ovarian Cancer in Chinese Women by Negatively Interacting with Oral Contraceptive Use

## LIT-0237
**Short title:** Ectopic expression of the WWOX gene suppresses stemness of human ovarian canc...
**Authors:** Yan et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Oncol Lett
**Identifier:** PMID 25789010 / PMC4356412 / DOI 10.3892/ol.2015.2971
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 237
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Ectopic expression of the WWOX gene suppresses stemness of human ovarian cancer stem cells

## LIT-0238
**Short title:** Diverse effect of WWOX overexpression in HT29 and SW480 colon cancer cell lines
**Authors:** Nowakowska et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Tumour Biol
**Identifier:** PMID 24938873 / PMC4190457 / DOI 10.1007/s13277-014-2196-2
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 238
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Diverse effect of WWOX overexpression in HT29 and SW480 colon cancer cell lines

## LIT-0239
**Short title:** Strategies by which WWOX-deficient metastatic cancer cells utilize to survive...
**Authors:** # et al.
**Year:** 2019
**Source type:** Article
**Journal/source:** Cell Death Discov
**Identifier:** PMID 31123603 / PMC6529460 / DOI 10.1038/s41420-019-0176-4
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 239
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Strategies by which WWOX-deficient metastatic cancer cells utilize to survive via dodging, compromising, and causing damage to WWOX-positive normal microenvironment

## LIT-0240
**Short title:** An opposing view on WWOX protein function as a tumor suppressor
**Authors:** Watanabe et al.
**Year:** 2003
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 14695174
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 240
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: An opposing view on WWOX protein function as a tumor suppressor

## LIT-0241
**Short title:** The correlation of the expressions of WWOX, LGR5 and vasohibin-1 in epithelia...
**Authors:** Yu et al.
**Year:** 2019
**Source type:** Article
**Journal/source:** Int J Clin Exp Pathol
**Identifier:** PMID 31933749 / PMC6944017
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 241
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The correlation of the expressions of WWOX, LGR5 and vasohibin-1 in epithelial ovarian cancer and their clinical significance

## LIT-0242
**Short title:** Conditional inactivation of the mouse Wwox tumor suppressor gene recapitulate...
**Authors:** Abdeen et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** J Cell Physiol
**Identifier:** PMID 23254685 / PMC3943428 / DOI 10.1002/jcp.24308
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-08-11
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 242
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 075]] (`BATCH_20260815_001`)
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Conditional inactivation of the mouse Wwox tumor suppressor gene recapitulates the null phenotype

## LIT-0243
**Short title:** Gene expression of WWOX, FHIT and p73 in acute lymphoblastic leukemia
**Authors:** Chen et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Oncol Lett
**Identifier:** PMID 24137446 / PMC3796419 / DOI 10.3892/ol.2013.1514
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 243
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Gene expression of WWOX, FHIT and p73 in acute lymphoblastic leukemia

## LIT-0244
**Short title:** Park 2004 — WWOX in 18 HCC lines: mRNA and protein reduced, two aberrant transcripts, four coding variants
**Authors:** Park SW, Ludes-Meyers J, Zimonjic DB, Durkin ME, Popescu NC, Aldaz CM
**Year:** 2004
**Source type:** Article
**Journal/source:** Br J Cancer
**Identifier:** PMID 15266310 / PMC2364795 / DOI 10.1038/sj.bjc.6602023
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Date last touched:** 2026-09-26
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 244
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-15266310-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-15266310-01`
**Primary pathway:** oncology / tumor suppressor biology — corrected from `P6 — DDR / genome stability` (no DDR assay in the paper)
**Genotype/model tag:** linee di HCC umane, nessun materiale neurale, nessun allele WWOX umano germinale
**Species:** cell line
**Transferability:** T3
**Directness to the reference genotype:** none — adult somatic liver-cancer cell lines
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW (unchanged)
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** FASE 1 triage 221–400 · `CC-20260914-15266310-01` · `BATCH_20260926_ALDAZ_R2`
**Current status:** processed — C
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-15266310-01`
**Note:** Title: Frequent downregulation and loss of WWOX gene expression in human hepatocellular carcinoma
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-15266310-01`; manifest `deepdive_manifests/PMID15266310.json`
**Registry record:** [[paper_registry_current#CORPUS P244]]

## LIT-0245
**Short title:** WWOX, a novel WW domain-containing protein mapping to human chromosome 16q23....
**Authors:** Bednarek et al.
**Year:** 2000
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 10786676
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 245
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WWOX, a novel WW domain-containing protein mapping to human chromosome 16q23.3-24.1, a region frequently affected in breast cancer

## LIT-0246
**Short title:** The role of WWOX tumor suppressor gene in the regulation of EMT process via r...
**Authors:** Płuciennik et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 25892250 / DOI 10.3892/ijo.2015.2964
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 246
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The role of WWOX tumor suppressor gene in the regulation of EMT process via regulation of CDH1-ZEB1-VIM expression in endometrial cancer

## LIT-0247
**Short title:** WWOX suppresses cell growth and induces cell apoptosis via inhibition of P38...
**Authors:** Wang et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Cell Physiol Biochem
**Identifier:** PMID 25502636 / DOI 10.1159/000366372
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 247
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WWOX suppresses cell growth and induces cell apoptosis via inhibition of P38 nuclear translocation in cholangiocarcinoma

## LIT-0248
**Short title:** Inhibition of the Wnt/beta-catenin pathway by the WWOX tumor suppressor protein
**Authors:** Bouteille et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Oncogene
**Identifier:** PMID 19465938 / DOI 10.1038/onc.2009.120
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 248
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Inhibition of the Wnt/beta-catenin pathway by the WWOX tumor suppressor protein

## LIT-0249
**Short title:** Impact of WWOX alterations on p73, ΔNp73, p53, cell proliferation and DNA plo...
**Authors:** Gomes et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Oral Dis
**Identifier:** PMID 21332605 / DOI 10.1111/j.1601-0825.2011.01802.x
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 249
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Impact of WWOX alterations on p73, ΔNp73, p53, cell proliferation and DNA ploidy in salivary gland neoplasms

## LIT-0250
**Short title:** [Effects of WWOX on ovarian cancer cell attachment in vitro]
**Authors:** [Article in Chinese]
**Year:** 2009
**Source type:** Article
**Journal/source:** Zhonghua Zhong Liu Za Zhi
**Identifier:** PMID 19950548
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 250
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: [Effects of WWOX on ovarian cancer cell attachment in vitro]

## LIT-0251
**Short title:** Genetic alterations of the WWOX gene in breast cancer
**Authors:** Ekizoglu et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Med Oncol
**Identifier:** PMID 21983861 / DOI 10.1007/s12032-011-0080-0
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 251
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Genetic alterations of the WWOX gene in breast cancer

## LIT-0252
**Short title:** Expression of WW domain-containing oxidoreductase WWOX in pterygium
**Authors:** Huang et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Mol Vis
**Identifier:** PMID 26120275 / PMC4480446
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 252
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Expression of WW domain-containing oxidoreductase WWOX in pterygium

## LIT-0253
**Short title:** Novel Homozygous Mutation in the WWOX Gene Causes Seizures and Global Develop...
**Authors:** Ehaideb et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Transl Neurosci
**Identifier:** PMID 30746283 / PMC6368664 / DOI 10.1515/tnsci-2018-0029
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 253
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** processed
**Status note:** promoted 2026-10-02 to [[paper_registry_current#PAPER 119]] by `CC-20261002-INTAKE-A-REGISTRY-01` — `complete_fulltext_read`, receipt `FTR-20261002-30746283-01`; the triage fields below are kept as history
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Novel Homozygous Mutation in the WWOX Gene Causes Seizures and Global Developmental Delay: Report and Review

## LIT-0254
**Short title:** New syngeneic inflammatory-related lung cancer metastatic model harboring dou...
**Authors:** Bleau et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Int J Cancer
**Identifier:** PMID 24473991 / DOI 10.1002/ijc.28574
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 254
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P8 — bone / RUNX2 axis
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: New syngeneic inflammatory-related lung cancer metastatic model harboring double KRAS/WWOX alterations

## LIT-0255
**Short title:** Exogenous WWOX enhances apoptosis and weakens metastasis in CNE2 nasopharynge...
**Authors:** Chen et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Int J Clin Exp Pathol
**Identifier:** PMID 31966369 / PMC6965803
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 255
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Exogenous WWOX enhances apoptosis and weakens metastasis in CNE2 nasopharyngeal carcinoma cells through the intrinsic apoptotic pathway

## LIT-0256
**Short title:** Circular RNA CircMTO1 Inhibits Proliferation of Glioblastoma Cells via miR-92...
**Authors:** Zhang et al.
**Year:** 2019
**Source type:** Article
**Journal/source:** Med Sci Monit
**Identifier:** PMID 31456594 / PMC6738003 / DOI 10.12659/MSM.918676
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 256
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Circular RNA CircMTO1 Inhibits Proliferation of Glioblastoma Cells via miR-92/WWOX Signaling Pathway

## LIT-0257
**Short title:** Tyrosine phosphorylation of WW proteins
**Authors:** Reuven et al.
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25627656 / PMC4935225 / DOI 10.1177/1535370214565991
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 257
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Tyrosine phosphorylation of WW proteins

## LIT-0258
**Short title:** LncRNA HOTAIRM1 Inhibits the Proliferation and Invasion of Lung Adenocarcinom...
**Authors:** No authors listed
**Year:** 2024
**Source type:** Article
**Journal/source:** Cancer Manag Res
**Identifier:** PMID 38282791 / PMC10812133 / DOI 10.2147/CMAR.S460239
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 258
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: LncRNA HOTAIRM1 Inhibits the Proliferation and Invasion of Lung Adenocarcinoma Cells via the miR-498/WWOX Axis [Retraction]

## LIT-0259
**Short title:** miR-187* Enhances SiHa Cervical Cancer Cell Oncogenicity Via Suppression of WWOX
**Authors:** Hung et al.
**Year:** 2020
**Source type:** Article
**Journal/source:** Anticancer Res
**Identifier:** PMID 32132039 / DOI 10.21873/anticanres.14084
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 259
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: miR-187* Enhances SiHa Cervical Cancer Cell Oncogenicity Via Suppression of WWOX

## LIT-0260
**Short title:** Molecular alterations in the tumor suppressor gene WWOX in oral leukoplakias
**Authors:** Pimenta FJ, Cordeiro GT, Pimenta LG, Viana MB, Lopes J, Gomez MV, Aldaz CM, De Marco L, Gomez RS
**Year:** 2008
**Source type:** Article
**Journal/source:** Oral Oncol
**Identifier:** PMID 18061530 / PMC4143237 / DOI 10.1016/j.oraloncology.2007.08.019
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Date last touched:** 2026-09-26
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 260
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-18061530-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-18061530-01`
**Primary pathway:** oncology / tumor suppressor biology — premalignant lesion; corrected from `P6 — DDR / genome stability`
**Genotype/model tag:** 23 oral leukoplakias, adult human tissue; no WWOX germline allele, no neural material
**Species:** not assessed in triage
**Transferability:** T3
**Directness to the reference genotype:** none — adult oral premalignant lesions
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW (unchanged)
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** FASE 1 triage 221–400 · `CC-20260914-18061530-01` · `BATCH_20260926_ALDAZ_R2`
**Current status:** processed — C
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-18061530-01`
**Note:** Title: Molecular alterations in the tumor suppressor gene WWOX in oral leukoplakias
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-18061530-01`; manifest `deepdive_manifests/PMID18061530.json`
**Registry record:** [[paper_registry_current#CORPUS P260]]

## LIT-0261
**Short title:** Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenes...
**Authors:** Mare et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Am J Cancer Res
**Identifier:** PMID 21731849 / PMC3124638
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 261
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001 — receipt `FTR-20260909-21731849-01`
**Note:** Title: Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenesis of osteosarcoma
**Evidence depth:** complete_fulltext_read — `FTR-20260909-21731849-01` (BATCH_20260909_001)
**Batch note:** REVIEW (corrected from Article); read, deliberately not promoted to PAPER

## LIT-0262
**Short title:** Expression of WWOX and FHIT is downregulated by exposure to arsenite in human...
**Authors:** Huang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Toxicol Lett
**Identifier:** PMID 23618899 / DOI 10.1016/j.toxlet.2013.04.007
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 262
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** rat
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Expression of WWOX and FHIT is downregulated by exposure to arsenite in human uroepithelial cells

## LIT-0263
**Short title:** WW domain-containing oxidoreductase in neuronal injury and neurological diseases
**Authors:** Chang et al.
**Year:** 2014
**Source type:** Review
**Journal/source:** Oncotarget
**Identifier:** PMID 25537520 / PMC4322972 / DOI 10.18632/oncotarget.2961
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-10-02 (partial full text; FTR-20261002-25537520-01)
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 263
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** background_only
**Primary pathway:** review — neuronal injury, tau/GSK-3β, TGF-β/TIAF1, neurodevelopment (corrected 2026-10-02 from "P6 — DDR / genome stability", CC-20261002-B-NONLINEAGE-01)
**Genotype/model tag:** unassigned in triage
**Species:** review — secondary source (corrected 2026-10-02 from "rat", CC-20261002-B-NONLINEAGE-01)
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** background_only — provenance map, read in full except the four schematic figure images; no claim link
**Next action:** none for evidence; figure images owed for a complete read (PMC CDN or Europe PMC bundle)
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WW domain-containing oxidoreductase in neuronal injury and neurological diseases

## LIT-0265
**Short title:** MiR-214 Mediates Cell Proliferation and Apoptosis of Nasopharyngeal Carcinoma...
**Authors:** Han et al.
**Year:** 2020
**Source type:** Article
**Journal/source:** Cancer Biother Radiopharm
**Identifier:** PMID 32101017 / PMC7578184 / DOI 10.1089/cbr.2019.2978
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 265
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: MiR-214 Mediates Cell Proliferation and Apoptosis of Nasopharyngeal Carcinoma Through Targeting Both WWOX and PTEN

## LIT-0266
**Short title:** Decreased expression of WWOX in the development of esophageal squamous cell c...
**Authors:** Guo et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Mol Carcinog
**Identifier:** PMID 22213016 / DOI 10.1002/mc.21853
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 266
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Decreased expression of WWOX in the development of esophageal squamous cell carcinoma

## LIT-0267
**Short title:** Germline mutation and aberrant transcripts of WWOX in a syndrome with multipl...
**Authors:** Xu et al.
**Year:** 2019
**Source type:** Case Reports
**Journal/source:** J Pathol
**Identifier:** PMID 31056747 / DOI 10.1002/path.5288
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 267
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Germline mutation and aberrant transcripts of WWOX in a syndrome with multiple primary tumors

## LIT-0268
**Short title:** Frequent attenuation of the WWOX tumor suppressor in osteosarcoma is associat...
**Authors:** Kurek et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 20530675 / PMC3037996 / DOI 10.1158/0008-5472.CAN-09-4602
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 268
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001 — receipt `FTR-20260909-20530675-01`
**Note:** Title: Frequent attenuation of the WWOX tumor suppressor in osteosarcoma is associated with increased tumorigenicity and aberrant RUNX2 expression
**Evidence depth:** complete_fulltext_read — `FTR-20260909-20530675-01` (BATCH_20260909_001)
**Batch note:** read, deliberately not promoted to PAPER; qualifies CLAIM 036

## LIT-0269
**Short title:** The fragile genes FHIT and WWOX are inactivated coordinately in invasive brea...
**Authors:** Guler et al.
**Year:** 2004
**Source type:** Article
**Journal/source:** Cancer
**Identifier:** PMID 15073846 / DOI 10.1002/cncr.20137
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 269
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The fragile genes FHIT and WWOX are inactivated coordinately in invasive breast carcinoma

## LIT-0270
**Short title:** Tumor Suppressor WWOX Contributes to the Elimination of Tumorigenic Cells in...
**Authors:** O'Keefe et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 26302329 / PMC4547717 / DOI 10.1371/journal.pone.0136356
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 270
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Tumor Suppressor WWOX Contributes to the Elimination of Tumorigenic Cells in Drosophila melanogaster

## LIT-0271
**Short title:** Loss of WWOX expression in human extrahepatic cholangiocarcinoma
**Authors:** Wang et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** J Cancer Res Clin Oncol
**Identifier:** PMID 18629536 / PMC12160241 / DOI 10.1007/s00432-008-0449-4
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 271
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Loss of WWOX expression in human extrahepatic cholangiocarcinoma

## LIT-0272
**Short title:** Characterizing WW domain interactions of tumor suppressor WWOX reveals its as...
**Authors:** Abu-Odeh et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** J Biol Chem
**Identifier:** PMID 24550385 / PMC3979411 / DOI 10.1074/jbc.M113.506790
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 272
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Characterizing WW domain interactions of tumor suppressor WWOX reveals its association with multiprotein networks

## LIT-0273
**Short title:** PARTICLE triplexes cluster in the tumor suppressor WWOX and may extend throug...
**Authors:** O'Leary et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Sci Rep
**Identifier:** PMID 28769061 / PMC5541130 / DOI 10.1038/s41598-017-07295-5
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 273
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: PARTICLE triplexes cluster in the tumor suppressor WWOX and may extend throughout the human genome

## LIT-0274
**Short title:** Strategies of oncogenic microbes to deal with WW domain-containing oxidoreduc...
**Authors:** Chang et al.
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25488911 / PMC4935232 / DOI 10.1177/1535370214561957
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 274
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Strategies of oncogenic microbes to deal with WW domain-containing oxidoreductase

## LIT-0275
**Short title:** Helicobacter pylori infection promotes methylation of WWOX gene in human gast...
**Authors:** Yan et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Biochem Biophys Res Commun
**Identifier:** PMID 21466786 / DOI 10.1016/j.bbrc.2011.03.127
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 275
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Helicobacter pylori infection promotes methylation of WWOX gene in human gastric cancer

## LIT-0276
**Short title:** Association between WWOX and the risk of malignant tumor, especially among As...
**Authors:** # et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Onco Targets Ther
**Identifier:** PMID 29662317 / PMC5892619 / DOI 10.2147/OTT.S152140
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 276
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** animal model — pathway variable
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Association between WWOX and the risk of malignant tumor, especially among Asians: evidence from a meta-analysis

## LIT-0277
**Short title:** Association of Wwox with ErbB4 in breast cancer
**Authors:** Aqeilan et al.
**Year:** 2007
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 17909041 / DOI 10.1158/0008-5472.CAN-07-2147
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 277
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Association of Wwox with ErbB4 in breast cancer

## LIT-0278
**Short title:** Therapeutic Zfra4-10 or WWOX7-21 Peptide Induces Complex Formation of WWOX wi...
**Authors:** Su et al.
**Year:** 2020
**Source type:** Article
**Journal/source:** Cancers (Basel)
**Identifier:** PMID 32764489 / PMC7464583 / DOI 10.3390/cancers12082189
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 278
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Therapeutic Zfra4-10 or WWOX7-21 Peptide Induces Complex Formation of WWOX with Selective Protein Targets in Organs that Leads to Cancer Suppression and Spleen Cytotoxic Memory Z Cell Activation In Vivo

## LIT-0279
**Short title:** [Effects of WWOX gene transfection on cell growth of epithelial ovarian cancer]
**Authors:** [Article in Chinese]
**Year:** 2008
**Source type:** Article
**Journal/source:** Zhonghua Fu Chan Ke Za Zhi
**Identifier:** PMID 18953870
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 279
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: [Effects of WWOX gene transfection on cell growth of epithelial ovarian cancer]

## LIT-0280
**Short title:** Physical and functional interactions between the Wwox tumor suppressor protei...
**Authors:** Aqeilan et al.
**Year:** 2004
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 15548692 / DOI 10.1158/0008-5472.CAN-04-2055
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 280
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Physical and functional interactions between the Wwox tumor suppressor protein and the AP-2gamma transcription factor

## LIT-0281
**Short title:** Inhibition of breast cancer cell growth in vitro and in vivo: effect of resto...
**Authors:** Iliopoulos et al.
**Year:** 2007
**Source type:** Article
**Journal/source:** Clin Cancer Res
**Identifier:** PMID 17200365 / DOI 10.1158/1078-0432.CCR-06-2038
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 281
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Inhibition of breast cancer cell growth in vitro and in vivo: effect of restoration of Wwox expression

## LIT-0282
**Short title:** Inactivation of the Wwox gene accelerates forestomach tumor progression in vivo
**Authors:** Aqeilan et al.
**Year:** 2007
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 17575124 / PMC2621009 / DOI 10.1158/0008-5472.CAN-07-1081
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-08-11
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 282
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 077]] (`BATCH_20260815_001`)
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Inactivation of the Wwox gene accelerates forestomach tumor progression in vivo

## LIT-0283
**Short title:** Epigenetic and genetic alterations affect the WWOX gene in head and neck squa...
**Authors:** Ekizoglu et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 25612104 / PMC4303423 / DOI 10.1371/journal.pone.0115353
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 283
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Epigenetic and genetic alterations affect the WWOX gene in head and neck squamous cell carcinoma

## LIT-0284
**Short title:** Tumor suppressor WWOX binds to ΔNp63α and sensitizes cancer cells to chemothe...
**Authors:** Salah et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Cell Death Dis
**Identifier:** PMID 23370280 / PMC3564006 / DOI 10.1038/cddis.2013.6
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-08-14
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 284
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 079]] (`BATCH_20260815_001`)
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Tumor suppressor WWOX binds to ΔNp63α and sensitizes cancer cells to chemotherapy

## LIT-0285
**Short title:** Association between CpG island methylation of the WWOX gene and its expressio...
**Authors:** Wang et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Tumour Biol
**Identifier:** PMID 19188760 / DOI 10.1159/000197911
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 285
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Association between CpG island methylation of the WWOX gene and its expression in breast cancers

## LIT-0286
**Short title:** Dias 2007 — WWOX IHC in 53 thyroid lesions: absent or weak in papillary carcinoma, kept in follicular lesions
**Authors:** Dias EP, Pimenta FJ, Sarquis MS, Dias Filho MA, Aldaz CM, Fujii JB, Gomez RS, De Marco L
**Year:** 2007
**Source type:** Article
**Journal/source:** Thyroid
**Identifier:** PMID 18047428 / PMC4150466 / DOI 10.1089/thy.2007.0232
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Date last touched:** 2026-09-26
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 286
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-18047428-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-18047428-01`
**Primary pathway:** oncology / tumor suppressor biology — tissue protein expression (IHC); corrected from `P6 — DDR / genome stability`
**Genotype/model tag:** 53 thyroid lesions from 46 adults; no WWOX germline allele, no neural material
**Species:** human
**Transferability:** T3
**Directness to the reference genotype:** none — adult thyroid tissue
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW (unchanged)
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** FASE 1 triage 221–400 · `CC-20260914-18047428-01` · `BATCH_20260926_ALDAZ_R2`
**Current status:** processed — C
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-18047428-01`
**Note:** Title: Association between decreased WWOX protein expression and thyroid cancer development
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-18047428-01`; manifest `deepdive_manifests/PMID18047428.json`
**Registry record:** [[paper_registry_current#CORPUS P286]]

## LIT-0287
**Short title:** The JNK inhibitor SP600129 enhances apoptosis of HCC cells induced by the tum...
**Authors:** Aderca et al.
**Year:** 2008
**Source type:** Article
**Journal/source:** J Hepatol
**Identifier:** PMID 18620777 / PMC2574998 / DOI 10.1016/j.jhep.2008.05.015
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 287
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The JNK inhibitor SP600129 enhances apoptosis of HCC cells induced by the tumor suppressor WWOX

## LIT-0288
**Short title:** WWOX gene is associated with HDL cholesterol and triglyceride levels
**Authors:** Sáez et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** BMC Med Genet
**Identifier:** PMID 20942981 / PMC2967537 / DOI 10.1186/1471-2350-11-148
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 288
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WWOX gene is associated with HDL cholesterol and triglyceride levels

## LIT-0289
**Short title:** Intertwined Relationship of WWOX and RUNX2 Proteins as a Biomarker for Predic...
**Authors:** Sharma et al.
**Year:** 2025
**Source type:** Article
**Journal/source:** Cureus
**Identifier:** PMID 41141138 / PMC12552799 / DOI 10.7759/cureus.93160
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 289
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Intertwined Relationship of WWOX and RUNX2 Proteins as a Biomarker for Predicting Response and Survival in Patients With Childhood Bone Cancer in North India: A Pilot Study

## LIT-0290
**Short title:** Allostery mediates ligand binding to WWOX tumor suppressor via a conformation...
**Authors:** Schuchardt et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** J Mol Recognit
**Identifier:** PMID 25703206 / PMC4376589 / DOI 10.1002/jmr.2419
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 290
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Allostery mediates ligand binding to WWOX tumor suppressor via a conformational switch

## LIT-0291
**Short title:** In vitro and in silico assessment of the effect of WWOX expression on invasiv...
**Authors:** # et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** BMC Urol
**Identifier:** PMID 33691672 / PMC7944886 / DOI 10.1186/s12894-021-00806-7
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 291
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: In vitro and in silico assessment of the effect of WWOX expression on invasiveness pathways associated with AP-2 transcription factors in bladder cancer

## LIT-0292
**Short title:** Expression of FRA16D/WWOX and FRA3B/FHIT genes in hematopoietic malignancies
**Authors:** Ishii et al.
**Year:** 2003
**Source type:** Article
**Journal/source:** Mol Cancer Res
**Identifier:** PMID 14638866
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 292
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Expression of FRA16D/WWOX and FRA3B/FHIT genes in hematopoietic malignancies

## LIT-0293
**Short title:** Genetic and epigenetic alterations of WWOX in the development of gastric card...
**Authors:** Guo et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Environ Mol Mutagen
**Identifier:** PMID 23197378 / DOI 10.1002/em.21748
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 293
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Genetic and epigenetic alterations of WWOX in the development of gastric cardia adenocarcinoma

## LIT-0294
**Short title:** The tumour suppressor gene WWOX is mutated in autosomal recessive cerebellar...
**Authors:** Mallaret et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Brain
**Identifier:** PMID 24369382 / PMC3914474 / DOI 10.1093/brain/awt338
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 294
**Priority:** high
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — priority
**Tier:** A
**Status:** screened
**Primary pathway:** clinical spectrum / SCAR12
**Genotype/model tag:** unassigned in triage
**Species:** human + mouse — nessun esperimento su ratto; il ratto *lde* è solo un comparatore citato (corretto da `BATCH_20260926_MALLARET`; registro [[paper_registry_current#PAPER 042]])
**Transferability:** see [[paper_registry_current#PAPER 042]] (T1/T2 — genotype caution P47T ≠ Q230P)
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — A
**Next action:** full-text retrieval + deep-dive in next session
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The tumour suppressor gene WWOX is mutated in autosomal recessive cerebellar ataxia with epilepsy and mental retardation
**Resolved (`BATCH_20260927_002`, 2026-09-27):** ✅ **letto integralmente il 2026-09-13**, receipt `FTR-20260913-24369382-01` (`complete_fulltext_read`; manifest `deepdive_manifests/PMID24369382.json`, 35 locator), su `files/fulltext/PMID24369382_Mallaret2014_PMCreader.html`. Registrato come [[paper_registry_current#PAPER 042]]; questa voce resta come lineage di triage. **Current status:** processed — full text reviewed. **Claim links:** 007 · 008 · 019 · 030 · 033 · **037** (provocazione audiogena e crisi spontanee nel topo `Wwox`-null costitutivo, comportamentali e non scorate, con comparatore wild-type `n = 8`). Il precedente `FTR-20260726-24369382-01` (`legacy_reconstruction`) è superato per nome. Coda `FT-128` chiusa dalla lettura; il debito dichiarato residuo è Supplementary Video 1.

## LIT-0295
**Short title:** Generation and characterization of mice carrying a conditional allele of the...
**Authors:** Ludes-Meyers et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 19936220 / PMC2777388 / DOI 10.1371/journal.pone.0007775
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 295
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Generation and characterization of mice carrying a conditional allele of the Wwox tumor suppressor gene
**Resolved (BATCH_20260806_002):** ✅ **letto integralmente 2026-08-06**, receipt `FTR-20260806-19936220-01` (corretto append-only da `-02`, solo lista output). Promosso a [[paper_registry_current#PAPER 057]]; questa voce resta come lineage di triage. **Current status:** processed — full text reviewed. **Claim links:** 036 (new) · 038 · 005. Coda `FT-043` chiusa.

## LIT-0296
**Short title:** Upregulation of the putative oncogene COTE1 contributes to human hepatocarcin...
**Authors:** Zhang et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 24899407 / DOI 10.3892/ijo.2014.2482
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 296
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Upregulation of the putative oncogene COTE1 contributes to human hepatocarcinogenesis through modulation of WWOX signaling

## LIT-0297
**Short title:** Functional and clinical characterization of the putative tumor suppressor WWO...
**Authors:** Becker et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** J Thorac Oncol
**Identifier:** PMID 21892104 / DOI 10.1097/JTO.0b013e31822e59dd
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 297
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P9 — immune / glia / inflammation
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Functional and clinical characterization of the putative tumor suppressor WWOX in non-small cell lung cancer

## LIT-0298
**Short title:** Neuroimaging features of WOREE syndrome: a mini-review of the literature
**Authors:** Battaglia et al.
**Year:** 2023
**Source type:** Review
**Journal/source:** Front Pediatr
**Identifier:** PMID 38161429 / PMC10757851 / DOI 10.3389/fped.2023.1301166
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 298
**Priority:** high
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — priority
**Tier:** A
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — A
**Next action:** none — promoted earlier to [[paper_registry_current#PAPER 046]]; full re-read 2026-10-03 (`FTR-20261003-38161429-01`, every section read; partial only for the open multihop queue); see `CC-20261003W3-A-BATTAGLIA-01`
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Neuroimaging features of WOREE syndrome: a mini-review of the literature

## LIT-0299
**Short title:** Molecular origin of the binding of WWOX tumor suppressor to ErbB4 receptor ty...
**Authors:** Schuchardt et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Biochemistry
**Identifier:** PMID 24308844 / PMC3906126 / DOI 10.1021/bi400987k
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 299
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Molecular origin of the binding of WWOX tumor suppressor to ErbB4 receptor tyrosine kinase

## LIT-0300
**Short title:** Early infantile-onset epileptic encephalopathy 28 due to a homozygous microde...
**Authors:** Davids et al.
**Year:** 2019
**Source type:** Article
**Journal/source:** Hum Mutat
**Identifier:** PMID 30362252 / PMC6296882 / DOI 10.1002/humu.23675
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 300
**Priority:** high
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — priority
**Tier:** A
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — A
**Next action:** full-text retrieval + deep-dive in next session
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Early infantile-onset epileptic encephalopathy 28 due to a homozygous microdeletion involving the WWOX gene in a region of uniparental disomy

## LIT-0301
**Short title:** Novel mutations in WWOX, RARS2, and C10orf2 genes in consanguineous Arab fami...
**Authors:** Alkhateeb et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Metab Brain Dis
**Identifier:** PMID 27121845 / DOI 10.1007/s11011-016-9827-9
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 301
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** unassigned — triage only
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Novel mutations in WWOX, RARS2, and C10orf2 genes in consanguineous Arab families with intellectual disability

## LIT-0302
**Short title:** Expression of CD133, E-cadherin and WWOX in colorectal cancer and related ana...
**Authors:** Sun et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Pak J Med Sci
**Identifier:** PMID 28523049 / PMC5432716 / DOI 10.12669/pjms.332.11687
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 302
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Expression of CD133, E-cadherin and WWOX in colorectal cancer and related analysis

## LIT-0303
**Short title:** Mol Cancer
**Authors:** . Jun:14:112. doi:.1186/s12943-015-0389-y.
**Year:** unknown
**Source type:** Article
**Journal/source:** Retracted article
**Identifier:** PMID 26041563 / PMC4453100
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 303
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Mol Cancer

## LIT-0304
**Short title:** ACK1 promotes hepatocellular carcinoma progression via downregulating WWOX an...
**Authors:** Xie et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 25738261 / DOI 10.3892/ijo.2015.2910
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 304
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: ACK1 promotes hepatocellular carcinoma progression via downregulating WWOX and activating AKT signaling

## LIT-0305
**Short title:** The tumor suppressor gene WWOX links the canonical and noncanonical NF-κB pat...
**Authors:** Fu et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Blood
**Identifier:** PMID 21115974 / PMC3318777 / DOI 10.1182/blood-2010-08-303073
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 305
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The tumor suppressor gene WWOX links the canonical and noncanonical NF-κB pathways in HTLV-I Tax-mediated tumorigenesis

## LIT-0306
**Short title:** WWOX oxidoreductase--substrate and enzymatic characterization
**Authors:** Sałuda-Gorgul et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Z Naturforsch C J Biosci
**Identifier:** PMID 21476439 / DOI 10.1515/znc-2011-1-210
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-10-04
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 306
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** deep-dive — full text required
**Tier:** A
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** HIGH
**Claim links:** none — read in full, supports no canonical claim. PAPER link: [[paper_registry_current#PAPER 244]].
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** READ IN FULL 2026-10-04 — version-of-record PDF held, receipt `FTR-20261004-21476439-01`, manifest PASS 0 gaps, blind locator audit over 17 triples; registered as [[paper_registry_current#PAPER 244]]
**Next action:** none for acquisition — acquired and read 2026-10-04. The open reading debt moves to its references: PMID 10786676 (the WWOX discovery paper, carried in the Introduction's SDR interpretation; ⚠️ note that the sentence giving the `GANSGIG` and `YNRSK` motif coordinates carries **no citation of its own** — the discovery-paper citation governs a different, adjacent statement, measured by blind audit 2026-10-04 — so this is a debt on the interpretation, not on a cited coordinate), PMID 11896615 and PMID 12829805. See the manifest's multihop block.
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WWOX oxidoreductase--substrate and enzymatic characterization

## LIT-0307
**Short title:** WW domain-containing proteins, WWOX and YAP, compete for interaction with Erb...
**Authors:** Aqeilan et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 16061658 / DOI 10.1158/0008-5472.CAN-05-1150
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 307
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WW domain-containing proteins, WWOX and YAP, compete for interaction with ErbB-4 and modulate its transcriptional function

## LIT-0308
**Short title:** WW domain-containing oxidoreductase's role in myriad cancers: clinical signif...
**Authors:** Gardenswartz et al.
**Year:** 2014
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 24510053 / DOI 10.1177/1535370213519213
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 308
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001 — receipt `FTR-20260909-24510053-01`
**Note:** Title: WW domain-containing oxidoreductase's role in myriad cancers: clinical significance and future implications
**Evidence depth:** complete_fulltext_read — `FTR-20260909-24510053-01` (BATCH_20260909_001)
**Batch note:** REVIEW; carries the primary provenance for DIS-001 ACK1 cascade

## LIT-0309
**Short title:** Novel compound heterozygous mutations in the WWOX gene cause early infantile...
**Authors:** Yang et al.
**Year:** 2019
**Source type:** Case Reports
**Journal/source:** Int J Dev Neurosci
**Identifier:** PMID 31669195 / DOI 10.1016/j.ijdevneu.2019.10.003
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 309
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Novel compound heterozygous mutations in the WWOX gene cause early infantile epileptic encephalopathy

## LIT-0310
**Short title:** Cancer Manag Res
**Authors:** . Jun:12:4379-4390. doi:.2147/CMAR.S244573. eCollection.
**Year:** unknown
**Source type:** Article
**Journal/source:** Retracted article
**Identifier:** PMID 32606933 / PMC7295110
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 310
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Cancer Manag Res

## LIT-0311
**Short title:** Exploring the mechanism of WWOX growth inhibitory effects on oral squamous ce...
**Authors:** Yang et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Oncol Lett
**Identifier:** PMID 28521426 / PMC5431404 / DOI 10.3892/ol.2017.5850
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 311
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Exploring the mechanism of WWOX growth inhibitory effects on oral squamous cell carcinoma

## LIT-0312
**Short title:** Relevance of Sp Binding Site Polymorphism in WWOX for Treatment Outcome in Pa...
**Authors:** Schirmer et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** J Natl Cancer Inst
**Identifier:** PMID 26857392 / PMC4859408 / DOI 10.1093/jnci/djv387
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 312
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Relevance of Sp Binding Site Polymorphism in WWOX for Treatment Outcome in Pancreatic Cancer

## LIT-0313
**Short title:** The downregulation of WWOX induces epithelial-mesenchymal transition and enha...
**Authors:** Li et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 30335523 / PMC6434457 / DOI 10.1177/1535370218806455
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 313
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The downregulation of WWOX induces epithelial-mesenchymal transition and enhances stemness and chemoresistance in breast cancer

## LIT-0314
**Short title:** The correlation analysis of WWOX expression and cancer related genes in neuro...
**Authors:** Nowakowska et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Acta Biochim Pol
**Identifier:** PMID 24455756
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 314
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The correlation analysis of WWOX expression and cancer related genes in neuroblastoma- a real time RT-PCR study

## LIT-0315
**Short title:** The role of WWOX polymorphisms on COPD susceptibility and pulmonary function...
**Authors:** Xie et al.
**Year:** 2016
**Source type:** Multicenter Study
**Journal/source:** Sci Rep
**Identifier:** PMID 26902998 / PMC4763216 / DOI 10.1038/srep21716
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 315
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** animal model — pathway variable
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The role of WWOX polymorphisms on COPD susceptibility and pulmonary function traits in Chinese: a case-control study and family-based analysis

## LIT-0316
**Short title:** Genetic alterations of WWOX in Wilms' tumor are involved in its carcinogenesis
**Authors:** Płuciennik et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Oncol Rep
**Identifier:** PMID 22842668 / DOI 10.3892/or.2012.1940
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 316
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Genetic alterations of WWOX in Wilms' tumor are involved in its carcinogenesis

## LIT-0317
**Short title:** Genetic alterations of the tumor suppressor gene WWOX in esophageal squamous...
**Authors:** Kuroki et al.
**Year:** 2002
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 11956080
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 317
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Genetic alterations of the tumor suppressor gene WWOX in esophageal squamous cell carcinoma

## LIT-0318
**Short title:** Loss of wwox expression in zebrafish embryos causes edema and alters Ca(2+) d...
**Authors:** Tsuruwaka et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** PeerJ
**Identifier:** PMID 25649963 / PMC4312067 / DOI 10.7717/peerj.727
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 318
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** zebrafish
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Loss of wwox expression in zebrafish embryos causes edema and alters Ca(2+) dynamics

## LIT-0319
**Short title:** The polymorphisms and haplotypes of WWOX gene are associated with the risk of...
**Authors:** Huang et al.
**Year:** 2013
**Source type:** Comparative Study
**Journal/source:** Mol Carcinog
**Identifier:** PMID 22693020 / DOI 10.1002/mc.21934
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 319
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The polymorphisms and haplotypes of WWOX gene are associated with the risk of lung cancer in southern and eastern Chinese populations

## LIT-0320
**Short title:** Upregulation of tumor suppressor WWOX promotes immune response in glioma
**Authors:** Yang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Cell Immunol
**Identifier:** PMID 24044959 / DOI 10.1016/j.cellimm.2013.07.015
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 320
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P9 — immune / glia / inflammation
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Upregulation of tumor suppressor WWOX promotes immune response in glioma

## LIT-0321
**Short title:** Tumor suppressor genes FHIT and WWOX are deleted in primary effusion lymphoma...
**Authors:** Roy et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Blood
**Identifier:** PMID 21685375 / PMC3158728 / DOI 10.1182/blood-2010-12-323659
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 321
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Tumor suppressor genes FHIT and WWOX are deleted in primary effusion lymphoma (PEL) cell lines

## LIT-0322
**Short title:** miR-134 induces oncogenicity and metastasis in head and neck carcinoma throug...
**Authors:** Liu et al.
**Year:** 2014
**Source type:** Comparative Study
**Journal/source:** Int J Cancer
**Identifier:** PMID 23824713 / DOI 10.1002/ijc.28358
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 322
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: miR-134 induces oncogenicity and metastasis in head and neck carcinoma through targeting WWOX gene

## LIT-0323
**Short title:** Synergistic effect of toosendanin and regorafenib against cell proliferation...
**Authors:** Yang et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** Phytother Res
**Identifier:** PMID 34058790 / DOI 10.1002/ptr.7174
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 323
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Synergistic effect of toosendanin and regorafenib against cell proliferation and migration by regulating WWOX signaling pathway in hepatocellular carcinoma

## LIT-0324
**Short title:** Frequent loss of WWOX expression in breast cancer: correlation with estrogen...
**Authors:** Nunez MI, Ludes-Meyers J, Abba MC, Kil H, Abbey NW, Page RE, Sahin A, Klein-Szanto AJP, Aldaz CM
**Year:** 2005
**Source type:** Comparative Study
**Journal/source:** Breast Cancer Res Treat
**Identifier:** PMID 15692750 / PMC4145848 / DOI 10.1007/s10549-004-1474-x
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Date last touched:** 2026-09-26
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 324
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260913-15692750-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260913-ALDAZ-B003-01`
**Primary pathway:** baseline expression / tumour-tissue protein loss — corrected from `P5 — metabolism / mitochondria / redox` (nothing hormonal is measured)
**Genotype/model tag:** human adult breast tissue, somatic; no WWOX allele
**Species:** not assessed in triage
**Transferability:** T3, `ESPANSIONE`
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** evaluated — HIGH on the SDR/sex-steroid framing, LOW on the staining observation
**clinical relevance:** LOW — unchanged
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** FASE 1 triage 221–400 · `CC-20260913-ALDAZ-B003-01` · `BATCH_20260926_ALDAZ_R2`
**Current status:** processed — C
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260913-15692750-01`
**Note:** Title: Frequent loss of WWOX expression in breast cancer: correlation with estrogen receptor status
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-15692750-01`; manifest `deepdive_manifests/PMID15692750.json`
**Registry record:** [[paper_registry_current#CORPUS P324]]

## LIT-0325
**Short title:** Primary WWOX phosphorylation and JNK activation during etoposide induces cyto...
**Authors:** Jamshidiha et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Daru
**Identifier:** PMID 22615609 / PMC3304374
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 325
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Primary WWOX phosphorylation and JNK activation during etoposide induces cytotoxicity in HEK293 cells

## LIT-0326
**Short title:** SENP2 regulated the stability of β-catenin through WWOX in hepatocellular car...
**Authors:** Jiang et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Tumour Biol
**Identifier:** PMID 24969559 / DOI 10.1007/s13277-014-2239-8
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 326
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: SENP2 regulated the stability of β-catenin through WWOX in hepatocellular carcinoma cell

## LIT-0327
**Short title:** Early onset epileptic encephalopathy caused by novel compound heterozygous mu...
**Authors:** Su et al.
**Year:** 2020
**Source type:** Case Reports
**Journal/source:** Int J Dev Neurosci
**Identifier:** PMID 32037574 / DOI 10.1002/jdn.10013
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 327
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Early onset epileptic encephalopathy caused by novel compound heterozygous mutation of WWOX gene

## LIT-0328
**Short title:** The Tumor-Suppressor WWOX and HDAC3 Inhibit the Transcriptional Activity of t...
**Authors:** El-Hage et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Mol Cancer Res
**Identifier:** PMID 25678599 / DOI 10.1158/1541-7786.MCR-14-0180
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 328
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The Tumor-Suppressor WWOX and HDAC3 Inhibit the Transcriptional Activity of the β-Catenin Coactivator BCL9-2 in Breast Cancer Cells

## LIT-0329
**Short title:** The prognostic significance of WWOX expression in patients with breast cancer...
**Authors:** Wang et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** J Cancer Res Clin Oncol
**Identifier:** PMID 20401669 / PMC11828298 / DOI 10.1007/s00432-010-0880-1
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 329
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The prognostic significance of WWOX expression in patients with breast cancer and its association with the basal-like phenotype

## LIT-0330
**Short title:** Complement C1q activates tumor suppressor WWOX to induce apoptosis in prostat...
**Authors:** Hong et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 19484134 / PMC2685983 / DOI 10.1371/journal.pone.0005755
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 330
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Complement C1q activates tumor suppressor WWOX to induce apoptosis in prostate cancer cells

## LIT-0331
**Short title:** Virus-encoded miR-155 ortholog in Marek's disease virus promotes cell prolife...
**Authors:** Zhu et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** Vet Microbiol
**Identifier:** PMID 33191002 / DOI 10.1016/j.vetmic.2020.108919
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 331
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Virus-encoded miR-155 ortholog in Marek's disease virus promotes cell proliferation via suppressing apoptosis by targeting tumor suppressor WWOX

## LIT-0332
**Short title:** Alternative transcripts of the candidate tumor suppressor gene, WWOX, are exp...
**Authors:** Driouch et al.
**Year:** 2002
**Source type:** Comparative Study
**Journal/source:** Oncogene
**Identifier:** PMID 11896615 / DOI 10.1038/sj.onc.1205273
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 332
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Alternative transcripts of the candidate tumor suppressor gene, WWOX, are expressed at high levels in human breast tumors

## LIT-0333
**Short title:** The tumor suppressor WW domain-containing oxidoreductase modulates cell metab...
**Authors:** Abu-Remaileh et al.
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25491415 / PMC4935230 / DOI 10.1177/1535370214561956
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-08-11
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 333
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 073]] (`BATCH_20260815_001`)
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The tumor suppressor WW domain-containing oxidoreductase modulates cell metabolism

## LIT-0334
**Short title:** Tumor Suppressor WWOX and p53 Alterations and Drug Resistance in Glioblastomas
**Authors:** Chiang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Front Oncol
**Identifier:** PMID 23459853 / PMC3586680 / DOI 10.3389/fonc.2013.00043
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 334
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Tumor Suppressor WWOX and p53 Alterations and Drug Resistance in Glioblastomas

## LIT-0335
**Short title:** Comparative mapping and genomic annotation of the bovine oncosuppressor gene...
**Authors:** Manera et al.
**Year:** 2009
**Source type:** Comparative Study
**Journal/source:** Cytogenet Genome Res
**Identifier:** PMID 20016169 / DOI 10.1159/000245919
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 335
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Comparative mapping and genomic annotation of the bovine oncosuppressor gene WWOX

## LIT-0336
**Short title:** WWOX induces apoptosis and inhibits proliferation of human hepatoma cell line...
**Authors:** Hu et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** World J Gastroenterol
**Identifier:** PMID 22736928 / PMC3380332 / DOI 10.3748/wjg.v18.i23.3020
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 336
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WWOX induces apoptosis and inhibits proliferation of human hepatoma cell line SMMC-7721

## LIT-0337
**Short title:** Gourley 2005 — WWOX variant 1 and variant 4 mRNA in 71 ovarian tumours and 13 contralateral ovaries
**Authors:** Gourley C, Paige AJW, Taylor KJ, Scott D, Francis NJ, Rush R, Aldaz CM, Smyth JF, Gabra H — corrected from the literal placeholder `# et al.`
**Year:** 2005
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 15870886 / PMC4166600 / DOI 10.3892/ijo.26.6.1681
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-28 (`BATCH_20260928_007`)
**Date last touched:** 2026-09-28
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 337
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260928-15870886-01` (contemporaneous re-read 2026-09-28, route (b) of `CC-20260914-15870886-01`; the 2026-09-14 reading `FTR-20260914-15870886-01` had not been appended to the ledger when this record was written); identity completed by `BATCH_20260926_ALDAZ_R2`, remaining fields by `BATCH_20260928_007`. Superseded wording kept verbatim: *«identity completed by `BATCH_20260926_ALDAZ_R2` (`CC-20260914-15870886-01`); a reading exists whose manifest is now complete (0 gaps, the PMID 11572989 hop resolved 2026-09-27; corretto 2026-09-28, `CC-20260914-15870886-01` § RESIDUE RE-CHECK, al posto di *«with one declared multihop gap»*) but which has **no persisted receipt**, so no reading depth is declared and the triage status stands»*
**Primary pathway:** oncology / tumor suppressor biology — adult ovarian-cancer mRNA expression
**Genotype/model tag:** 71 adult epithelial ovarian tumours + 13 contralateral ovaries; PEO1hyg1.6 transfectants; no WWOX germline allele, no neural material
**Species:** human
**Transferability:** T3
**Directness to the reference genotype:** none — adult ovarian cancer
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** FASE 1 triage 221–400
**Current status:** processed — C
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260928-15870886-01`
**Note:** Title: WWOX mRNA expression profile in epithelial ovarian cancer supports the role of WWOX variant 1 as a tumour suppressor, although the role of variant 4 remains unclear
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260928-15870886-01`; manifest `deepdive_manifests/PMID15870886.json`

## LIT-0338
**Short title:** Aberrant expression of WWOX protein in epithelial ovarian cancer: a clinicopa...
**Authors:** Lan et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Int J Gynecol Pathol
**Identifier:** PMID 22317867 / DOI 10.1097/PGP.0b013e3182297fd2
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 338
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Aberrant expression of WWOX protein in epithelial ovarian cancer: a clinicopathologic and immunohistochemical study

## LIT-0339
**Short title:** Combinations of single nucleotide polymorphisms WWOX-rs13338697, GALNT14-rs96...
**Authors:** Lin et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Asia Pac J Clin Oncol
**Identifier:** PMID 28695683 / DOI 10.1111/ajco.12745
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 339
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Combinations of single nucleotide polymorphisms WWOX-rs13338697, GALNT14-rs9679162 and rs6025211 effectively stratify outcomes of chemotherapy in advanced hepatocellular carcinoma

## LIT-0340
**Short title:** Study of FHIT and WWOX expression in mucoepidermoid carcinoma and adenoid cys...
**Authors:** Dincer et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Oral Oncol
**Identifier:** PMID 20060354 / DOI 10.1016/j.oraloncology.2009.12.003
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 340
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Study of FHIT and WWOX expression in mucoepidermoid carcinoma and adenoid cystic carcinoma of salivary gland

## LIT-0341
**Short title:** Functional genetic variant in the Kozak sequence of WW domain-containing oxid...
**Authors:** Cheng et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Oncotarget
**Identifier:** PMID 27655721 / PMC5342485 / DOI 10.18632/oncotarget.12082
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 341
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Functional genetic variant in the Kozak sequence of WW domain-containing oxidoreductase (WWOX) gene is associated with oral cancer risk

## LIT-0342
**Short title:** Association of polymorphisms in WWOX gene with risk and outcome of osteosarco...
**Authors:** Zhang et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Onco Targets Ther
**Identifier:** PMID 26929649 / PMC4767064 / DOI 10.2147/OTT.S99106
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 342
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P8 — bone / RUNX2 axis
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Association of polymorphisms in WWOX gene with risk and outcome of osteosarcoma in a sample of the young Chinese population

## LIT-0343
**Short title:** W44X mutation in the WWOX gene causes intractable seizures and developmental...
**Authors:** Elsaadany et al.
**Year:** 2016
**Source type:** Case Reports
**Journal/source:** BMC Med Genet
**Identifier:** PMID 27495153 / PMC4975905 / DOI 10.1186/s12881-016-0317-z
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 343
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** none — promoted earlier to [[paper_registry_current#PAPER 049]]; first receipted full-text read 2026-10-03 (`FTR-20261003-27495153-01`, `complete_fulltext_read`)
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: W44X mutation in the WWOX gene causes intractable seizures and developmental delay: a case report

## LIT-0344
**Short title:** FRA16D common chromosomal fragile site oxido-reductase (FOR/WWOX) protects ag...
**Authors:** O'Keefe et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Oncogene
**Identifier:** PMID 16007179 / DOI 10.1038/sj.onc.1208806
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 344
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** Drosophila
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: FRA16D common chromosomal fragile site oxido-reductase (FOR/WWOX) protects against the effects of ionizing radiation in Drosophila

## LIT-0345
**Short title:** The long non-coding RNA PARTICLE is associated with WWOX and the absence of F...
**Authors:** O'Leary et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Oncotarget
**Identifier:** PMID 29152092 / PMC5675644 / DOI 10.18632/oncotarget.21086
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 345
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The long non-coding RNA PARTICLE is associated with WWOX and the absence of FRA16D breakage in osteosarcoma patients

## LIT-0346
**Short title:** Biophysical basis of the binding of WWOX tumor suppressor to WBP1 and WBP2 ad...
**Authors:** McDonald et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** J Mol Biol
**Identifier:** PMID 22634283 / PMC3412936 / DOI 10.1016/j.jmb.2012.05.015
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 346
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Biophysical basis of the binding of WWOX tumor suppressor to WBP1 and WBP2 adaptors

## LIT-0347
**Short title:** [Expressions of WWOX and CD133 in colorectal cancer and their clinical signif...
**Authors:** [Article in Chinese]
**Year:** 2015
**Source type:** Article
**Journal/source:** Nan Fang Yi Ke Da Xue Xue Bao
**Identifier:** PMID 26607080
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 347
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: [Expressions of WWOX and CD133 in colorectal cancer and their clinical significance]

## LIT-0348
**Short title:** Genetic and Functional Evidence Links Germline Biallelic Inactivating Variant...
**Authors:** Zhang et al.
**Year:** 2025
**Source type:** Article
**Journal/source:** Adv Sci (Weinh)
**Identifier:** PMID 41124647 / PMC12767083 / DOI 10.1002/advs.202507602
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 348
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Genetic and Functional Evidence Links Germline Biallelic Inactivating Variants in WWOX to Histological Mixed-Type Thyroid Cancer

## LIT-0349
**Short title:** A multi-exon deletion within WWOX is associated with a 46,XY disorder of sex...
**Authors:** White et al.
**Year:** 2012
**Source type:** Case Reports
**Journal/source:** Eur J Hum Genet
**Identifier:** PMID 22071891 / PMC3283189 / DOI 10.1038/ejhg.2011.204
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 349
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: A multi-exon deletion within WWOX is associated with a 46,XY disorder of sex development

## LIT-0350
**Short title:** [Effect of WWOX gene on the attachment and adhesion of ovarian cancer cells]
**Authors:** [Article in Chinese]
**Year:** 2009
**Source type:** Article
**Journal/source:** Zhonghua Fu Chan Ke Za Zhi
**Identifier:** PMID 19957554
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 350
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: [Effect of WWOX gene on the attachment and adhesion of ovarian cancer cells]

## LIT-0351
**Short title:** Alternating expression levels of WWOX tumor suppressor and cancer-related gen...
**Authors:** Płuciennik et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Oncol Lett
**Identifier:** PMID 25295115 / PMC4186597 / DOI 10.3892/ol.2014.2476
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 351
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Alternating expression levels of WWOX tumor suppressor and cancer-related genes in patients with bladder cancer

## LIT-0352
**Short title:** Homozygous deletions may be markers of nearby heterozygous mutations: The com...
**Authors:** Alsop et al.
**Year:** 2008
**Source type:** Article
**Journal/source:** Genes Chromosomes Cancer
**Identifier:** PMID 18273838 / DOI 10.1002/gcc.20548
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 352
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Homozygous deletions may be markers of nearby heterozygous mutations: The complex deletion at FRA16D in the HCT116 colon cancer cell line removes exons of WWOX

## LIT-0353
**Short title:** Functional genetic variant of WW domain-containing oxidoreductase (WWOX) gene...
**Authors:** Lee et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 28426730 / PMC5398630 / DOI 10.1371/journal.pone.0176141
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 353
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Functional genetic variant of WW domain-containing oxidoreductase (WWOX) gene is associated with hepatocellular carcinoma risk

## LIT-0354
**Short title:** [The relationship between FHIT and WWOX expression and clinicopathological fe...
**Authors:** [Article in Chinese]
**Year:** 2010
**Source type:** Article
**Journal/source:** Zhonghua Gan Zang Bing Za Zhi
**Identifier:** PMID 20510001 / DOI 10.3760/cma.j.issn.1007-3418.2010.05.011
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 354
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: [The relationship between FHIT and WWOX expression and clinicopathological features in hepatocellular carcinoma]

## LIT-0355
**Short title:** Expression of B Cell-Specific Moloney Murine Leukemia Virus Integration Site...
**Authors:** Yu et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Med Sci Monit
**Identifier:** PMID 30242144 / PMC6166521 / DOI 10.12659/MSM.909675
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 355
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Expression of B Cell-Specific Moloney Murine Leukemia Virus Integration Site 1 (BMI-1) and WW Domain-Containing Oxidoreductase (WWOX) in Liver Cancer Tissue and Normal Liver Tissue

## LIT-0356
**Short title:** West syndrome, developmental and epileptic encephalopathy, and severe CNS dis...
**Authors:** Shaukat et al.
**Year:** 2018
**Source type:** Case Reports
**Journal/source:** Epileptic Disord
**Identifier:** PMID 30361190 / DOI 10.1684/epd.2018.1005
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 356
**Priority:** high
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — priority
**Tier:** A
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — A
**Next action:** none — promoted earlier to [[paper_registry_current#PAPER 045]]; first receipted full-text read 2026-10-03 (`FTR-20261003-30361190-01`, `complete_fulltext_read`; the earlier `FTR-20260726-30361190-01` is a legacy reconstruction); see `CC-20261003W4-A-SHAUKAT-01`
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: West syndrome, developmental and epileptic encephalopathy, and severe CNS disorder associated with WWOX mutations

## LIT-0357
**Short title:** Transforming growth factor beta1 signaling via interaction with cell surface...
**Authors:** Hsu et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** J Biol Chem
**Identifier:** PMID 19366691 / PMC2708898 / DOI 10.1074/jbc.M806688200
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 357
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Transforming growth factor beta1 signaling via interaction with cell surface Hyal-2 and recruitment of WWOX/WOX1

## LIT-0358
**Short title:** Drosophila orthologue of WWOX, the chromosomal fragile site FRA16D tumour sup...
**Authors:** O'Keefe et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Hum Mol Genet
**Identifier:** PMID 21075834 / PMC3016910 / DOI 10.1093/hmg/ddq495
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-08-11
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 358
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 071]] (`BATCH_20260815_001`)
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** Drosophila
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Drosophila orthologue of WWOX, the chromosomal fragile site FRA16D tumour suppressor gene, functions in aerobic metabolism and regulates reactive oxygen species

## LIT-0359
**Short title:** The supposed tumor suppressor gene WWOX is mutated in an early lethal microce...
**Authors:** Abdel-Salam et al.
**Year:** 2014
**Source type:** Case Reports
**Journal/source:** Orphanet J Rare Dis
**Identifier:** PMID 24456803 / PMC3918143 / DOI 10.1186/1750-1172-9-12
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 359
**Priority:** high
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — priority
**Tier:** A
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — A
**Next action:** none — promoted earlier to [[paper_registry_current#PAPER 043]]; first receipted full-text read 2026-10-03 (`FTR-20261003-24456803-01`, `complete_fulltext_read`)
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: The supposed tumor suppressor gene WWOX is mutated in an early lethal microcephaly syndrome with epilepsy, growth retardation and retinal degeneration

## LIT-0360
**Short title:** Identification of IGF1, SLC4A4, WWOX, and SFMBT1 as hypertension susceptibili...
**Authors:** Yang et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 22479346 / PMC3315540 / DOI 10.1371/journal.pone.0032907
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 360
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Identification of IGF1, SLC4A4, WWOX, and SFMBT1 as hypertension susceptibility genes in Han Chinese with a genome-wide gene-based association study

## LIT-0361
**Short title:** Effect of the WWOX gene on the regulation of the cell cycle and apoptosis in...
**Authors:** Yan et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Mol Med Rep
**Identifier:** PMID 25891642 / PMC4464321 / DOI 10.3892/mmr.2015.3640
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 361
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Effect of the WWOX gene on the regulation of the cell cycle and apoptosis in human ovarian cancer stem cells

## LIT-0362
**Short title:** A novel whole exon deletion in WWOX gene causes early epilepsy, intellectual...
**Authors:** Ben-Salem et al.
**Year:** 2015
**Source type:** Case Reports
**Journal/source:** J Mol Neurosci
**Identifier:** PMID 25403906 / DOI 10.1007/s12031-014-0463-8
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 362
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** clinical spectrum / SCAR12
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: A novel whole exon deletion in WWOX gene causes early epilepsy, intellectual disability and optic atrophy

## LIT-0363
**Short title:** A spontaneous mutation of the Wwox gene and audiogenic seizures in rats with...
**Authors:** Suzuki et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Genes Brain Behav
**Identifier:** PMID 19500159 / DOI 10.1111/j.1601-183X.2009.00502.x
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 363
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** rat
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: A spontaneous mutation of the Wwox gene and audiogenic seizures in rats with lethal dwarfism and epilepsy
**Resolved (BATCH_20260806_002):** ✅ **letto integralmente 2026-08-06**, receipt `FTR-20260806-19500159-01`. Promosso a [[paper_registry_current#PAPER 058]]; questa voce resta come lineage di triage. **Current status:** processed — full text reviewed (supplementari `unavailable`, HTTP 403). **Claim links:** 037 (new) · 005 · 038. Coda `FT-042` chiusa. Il triage lo aveva assegnato a `P5 — metabolismo`: l'asse primario è **P2, eccitabilità**.

## LIT-0364
**Short title:** Reversing effect of exogenous WWOX gene expression on malignant phenotype of...
**Authors:** Zhou et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Chin Med J (Engl)
**Identifier:** PMID 20367991
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 364
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Reversing effect of exogenous WWOX gene expression on malignant phenotype of primary cultured lung carcinoma cells

## LIT-0365
**Short title:** Modeling genetic epileptic encephalopathies using brain organoids
**Authors:** Steinberg et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** EMBO Mol Med
**Identifier:** PMID 34268881 / PMC8350905 / DOI 10.15252/emmm.202013610
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 365
**Priority:** high
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — priority
**Tier:** A
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human organoid
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — A
**Next action:** full-text retrieval + deep-dive in next session
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Modeling genetic epileptic encephalopathies using brain organoids

## LIT-0366
**Short title:** Methylation status of WWOX gene promoter CpG islands in epithelial ovarian ca...
**Authors:** Yan et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Biomed Rep
**Identifier:** PMID 24648952 / PMC3917087 / DOI 10.3892/br.2013.86
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 366
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Methylation status of WWOX gene promoter CpG islands in epithelial ovarian cancer and its clinical significance

## LIT-0367
**Short title:** Characterization of the tumor suppressor gene WWOX in primary human oral squa...
**Authors:** Pimenta FJ, Gomes DA, Perdigão PF, Barbosa AA, Romano-Silva MA, Gomez MV, Aldaz CM, De Marco L, Gomez RS
**Year:** 2006
**Source type:** Article
**Journal/source:** Int J Cancer
**Identifier:** PMID 16152610 / PMC4145845 / DOI 10.1002/ijc.21446
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Date last touched:** 2026-09-26
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 367
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-16152610-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-16152610-01`
**Primary pathway:** oncology / tumor suppressor biology — expression and aberrant transcripts; corrected from `P6 — DDR / genome stability`
**Genotype/model tag:** 20 adult OSCC; somatic S329F; no WWOX germline allele, no neural material
**Species:** not assessed in triage
**Transferability:** T3
**Directness to the reference genotype:** none — adult oral squamous cell carcinomas
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW (unchanged)
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** FASE 1 triage 221–400 · `CC-20260914-16152610-01` · `BATCH_20260926_ALDAZ_R2`
**Current status:** processed — C
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-16152610-01`
**Note:** Title: Characterization of the tumor suppressor gene WWOX in primary human oral squamous cell carcinomas
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-16152610-01`; manifest `deepdive_manifests/PMID16152610.json`
**Registry record:** [[paper_registry_current#CORPUS P367]]

## LIT-0368
**Short title:** Aberrant gene promoter methylation of p16, FHIT, CRBP1, WWOX, and DLC-1 in Ep...
**Authors:** He et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Med Oncol
**Identifier:** PMID 25720522 / DOI 10.1007/s12032-015-0525-y
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 368
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Aberrant gene promoter methylation of p16, FHIT, CRBP1, WWOX, and DLC-1 in Epstein-Barr virus-associated gastric carcinomas

## LIT-0369
**Short title:** Versatile communication strategies among tandem WW domain repeats
**Authors:** Dodson et al.
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25710931 / PMC4436281 / DOI 10.1177/1535370214566558
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 369
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** animal model — pathway variable
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Versatile communication strategies among tandem WW domain repeats

## LIT-0370
**Short title:** Activated tyrosine kinase Ack1 promotes prostate tumorigenesis: role of Ack1...
**Authors:** Mahajan et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 16288044 / DOI 10.1158/0008-5472.CAN-05-1127
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 370
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Activated tyrosine kinase Ack1 promotes prostate tumorigenesis: role of Ack1 in polyubiquitination of tumor suppressor Wwox

## LIT-0371
**Short title:** Fragile genes as biomarkers: epigenetic control of WWOX and FHIT in lung, bre...
**Authors:** Iliopoulos et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Oncogene
**Identifier:** PMID 15674328 / DOI 10.1038/sj.onc.1208398
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 371
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Fragile genes as biomarkers: epigenetic control of WWOX and FHIT in lung, breast and bladder cancer

## LIT-0372
**Short title:** Zfra Inhibits the TRAPPC6AΔ-Initiated Pathway of Neurodegeneration
**Authors:** Lin et al.
**Year:** 2022
**Source type:** Article
**Journal/source:** Int J Mol Sci
**Identifier:** PMID 36498839 / PMC9739312 / DOI 10.3390/ijms232314510
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 372
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** P9 — immune / glia / inflammation
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Zfra Inhibits the TRAPPC6AΔ-Initiated Pathway of Neurodegeneration

## LIT-0373
**Short title:** WWOX protein expression varies among RCC histotypes and downregulation of WWO...
**Authors:** Lin et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Ann Surg Oncol
**Identifier:** PMID 22555346 / DOI 10.1245/s10434-012-2371-x
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 373
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WWOX protein expression varies among RCC histotypes and downregulation of WWOX protein correlates with less-favorable prognosis in clear RCC

## LIT-0374
**Short title:** Common chromosomal fragile site FRA16D tumor suppressor WWOX gene expression...
**Authors:** Dayan et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Genes Chromosomes Cancer
**Identifier:** PMID 23765596 / DOI 10.1002/gcc.22078
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 374
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Common chromosomal fragile site FRA16D tumor suppressor WWOX gene expression and metabolic reprograming in cells

## LIT-0375
**Short title:** Genetic association study identifies a functional CNV in the WWOX gene contri...
**Authors:** Fan et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Oncotarget
**Identifier:** PMID 26910372 / PMC4941300 / DOI 10.18632/oncotarget.7546
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 375
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Genetic association study identifies a functional CNV in the WWOX gene contributes to the risk of intracranial aneurysms

## LIT-0376
**Short title:** Structural insights into the functional versatility of WW domain-containing o...
**Authors:** Amjad Farooq
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25662954 / PMC4374002 / DOI 10.1177/1535370214561586
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 376
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Structural insights into the functional versatility of WW domain-containing oxidoreductase tumor suppressor

## LIT-0377
**Short title:** Large common fragile site genes and cancer
**Authors:** Smith et al.
**Year:** 2007
**Source type:** Review
**Journal/source:** Semin Cancer Biol
**Identifier:** PMID 17140807 / DOI 10.1016/j.semcancer.2006.10.003
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 377
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Large common fragile site genes and cancer

## LIT-0378
**Short title:** Stewart 2014 — decitabine and FHIT/WWOX/FUS1/PTEN IHC in paired biopsies: WWOX rises as a non-significant trend (P = 0.0547)
**Authors:** Stewart DJ, Nunez MI, Jelinek J, Hong D, Gupta S, Aldaz M, Issa JP, Kurzrock R, Wistuba II (`Aldaz M` as printed)
**Year:** 2014
**Source type:** Article
**Journal/source:** Clin Epigenetics
**Identifier:** PMID 25024751 / PMC4094901 / DOI 10.1186/1868-7083-6-13
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Date last touched:** 2026-09-26
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 378
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-25024751-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-25024751-01`
**Primary pathway:** epigenetics / pharmacological re-expression — corrected from `P6 — DDR / genome stability`
**Genotype/model tag:** tumori umani refrattari adulti, tessuto bioptico, nessun materiale neurale, nessun allele WWOX germinale
**Species:** human
**Transferability:** T3
**Directness to the reference genotype:** none — adult refractory tumours, no child, no neural material
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW (unchanged)
**Claim links:** none — the reading proposes none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** FASE 1 triage 221–400 · `CC-20260914-25024751-01` · `BATCH_20260926_ALDAZ_R2`
**Current status:** processed — C
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-25024751-01`
**Note:** Title: Impact of decitabine on immunohistochemistry expression of the putative tumor suppressor genes FHIT, WWOX, FUS1 and PTEN in clinical tumor samples
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-25024751-01`; manifest `deepdive_manifests/PMID25024751.json`
**Registry record:** [[paper_registry_current#CORPUS P378]]

## LIT-0379
**Short title:** MicroRNA-153 promotes Wnt/β-catenin activation in hepatocellular carcinoma th...
**Authors:** Hua et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Oncotarget
**Identifier:** PMID 25708809 / PMC4414157 / DOI 10.18632/oncotarget.2927
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 379
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: MicroRNA-153 promotes Wnt/β-catenin activation in hepatocellular carcinoma through suppression of WWOX

## LIT-0380
**Short title:** Gene mapping and expression analysis of 16q loss of heterozygosity identifies...
**Authors:** Jenner et al.
**Year:** 2007
**Source type:** Multicenter Study
**Journal/source:** Blood
**Identifier:** PMID 17609426 / DOI 10.1182/blood-2007-02-075069
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 380
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Gene mapping and expression analysis of 16q loss of heterozygosity identifies WWOX and CYLD as being important in determining clinical outcome in multiple myeloma

## LIT-0381
**Short title:** Association study of a functional copy number variation in the WWOX gene with...
**Authors:** Yu et al.
**Year:** 2014
**Source type:** Randomized Controlled Trial
**Journal/source:** Int J Cancer
**Identifier:** PMID 24585490 / DOI 10.1002/ijc.28815
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 381
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Association study of a functional copy number variation in the WWOX gene with risk of gliomas among Chinese people

## LIT-0382
**Short title:** Frequent PVT1 rearrangement and novel chimeric genes PVT1-NBEA and PVT1-WWOX...
**Authors:** Nagoshi et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 22869583 / DOI 10.1158/0008-5472.CAN-12-0213
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 382
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** unassigned — triage only
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Frequent PVT1 rearrangement and novel chimeric genes PVT1-NBEA and PVT1-WWOX occur in multiple myeloma with 8q24 abnormality

## LIT-0383
**Short title:** A novel missense variant in the SDR domain of the WWOX gene leads to complete...
**Authors:** Johannsen et al.
**Year:** 2018
**Source type:** Case Reports
**Journal/source:** Neurogenetics
**Identifier:** PMID 29808465 / DOI 10.1007/s10048-018-0549-5
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 383
**Priority:** high
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — priority
**Tier:** A
**Status:** screened
**Primary pathway:** clinical spectrum / WWOX-DEE
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — A
**Next action:** full-text retrieval + deep-dive in next session
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: A novel missense variant in the SDR domain of the WWOX gene leads to complete loss of WWOX protein with early-onset epileptic encephalopathy and severe developmental delay

## LIT-0384
**Short title:** A functional copy number variation in the WWOX gene is associated with lung c...
**Authors:** Yang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Hum Mol Genet
**Identifier:** PMID 23339925 / DOI 10.1093/hmg/ddt019
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 384
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: A functional copy number variation in the WWOX gene is associated with lung cancer risk in Chinese

## LIT-0385
**Short title:** Expression of common chromosomal fragile site genes, WWOX/FRA16D and FHIT/FRA...
**Authors:** Thavathiru E, Ludes-Meyers JH, MacLeod MC, Aldaz CM
**Year:** 2005
**Source type:** Article
**Journal/source:** Mol Carcinog
**Identifier:** PMID 16187332 / PMC4166602 / DOI 10.1002/mc.20122
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Date last touched:** 2026-09-26
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 385
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-16187332-01` (read on the VPS laboratory checkout, recovered by `fulltext_receipts.py rechain`); fields completed by `BATCH_20260926_ALDAZ_R2` from `CC-20260914-16187332-01`
**Primary pathway:** P6 — DDR / genome stability (kept): it measures WWOX expression after DNA damage, not WWOX's role in the damage response
**Genotype/model tag:** MCF-7 and Saos-2 only; no WWOX allele, no neural material
**Species:** not assessed in triage
**Transferability:** T3
**Directness to the reference genotype:** none — two transformed adult lines
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW (unchanged)
**Claim links:** none — deliberately; the reading refuses a `CLAIM 029` edit (converse direction)
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** FASE 1 triage 221–400 · `CC-20260914-16187332-01` · `BATCH_20260926_ALDAZ_R2`
**Current status:** processed — C
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-16187332-01`
**Note:** Title: Expression of common chromosomal fragile site genes, WWOX/FRA16D and FHIT/FRA3B is downregulated by exposure to environmental carcinogens, UV, and BPDE but not by IR
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-16187332-01`; manifest `deepdive_manifests/PMID16187332.json`
**Registry record:** [[paper_registry_current#CORPUS P385]]

## LIT-0386
**Short title:** Cigarette smoking extract causes hypermethylation and inactivation of WWOX ge...
**Authors:** Yang et al.
**Year:** 2012
**Source type:** Comparative Study
**Journal/source:** Neoplasma
**Identifier:** PMID 22248280 / DOI 10.4149/neo_2012_028
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 386
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Cigarette smoking extract causes hypermethylation and inactivation of WWOX gene in T-24 human bladder cancer cells

## LIT-0387
**Short title:** Cloning of WWOX gene and its growth-inhibiting effects on ovarian cancer cells
**Authors:** Xiong et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** J Huazhong Univ Sci Technolog Med Sci
**Identifier:** PMID 20556583 / DOI 10.1007/s11596-010-0358-z
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 387
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Cloning of WWOX gene and its growth-inhibiting effects on ovarian cancer cells

## LIT-0388
**Short title:** Components of DNA damage checkpoint pathway regulate UV exposure-dependent al...
**Authors:** Ishii et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Mol Cancer Res
**Identifier:** PMID 15798093 / DOI 10.1158/1541-7786.MCR-04-0209
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 388
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** clinical spectrum / SCAR12
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Components of DNA damage checkpoint pathway regulate UV exposure-dependent alterations of gene expression of FHIT and WWOX at chromosome fragile sites

## LIT-0389
**Short title:** Common fragile genes and digestive tract cancers
**Authors:** Kuroki et al.
**Year:** 2006
**Source type:** Review
**Journal/source:** Surg Today
**Identifier:** PMID 16378185 / DOI 10.1007/s00595-005-3094-4
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 389
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Common fragile genes and digestive tract cancers

## LIT-0390
**Short title:** Common chromosomal fragile sites and cancer: focus on FRA16D
**Authors:** O'Keefe et al.
**Year:** 2006
**Source type:** Review
**Journal/source:** Cancer Lett
**Identifier:** PMID 16242840 / DOI 10.1016/j.canlet.2005.07.041
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 390
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Common chromosomal fragile sites and cancer: focus on FRA16D

## LIT-0391
**Short title:** Expression of fragile histidine triad (FHIT) and WW-domain oxidoreductase gen...
**Authors:** Chen et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Asian Pac J Cancer Prev
**Identifier:** PMID 23534718 / DOI 10.7314/apjcp.2013.14.1.165
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 391
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Expression of fragile histidine triad (FHIT) and WW-domain oxidoreductase gene (WWOX) in nasopharyngeal carcinoma

## LIT-0392
**Short title:** Inhibition of miR-24 suppresses malignancy of human non-small cell lung cance...
**Authors:** Wang et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Thorac Cancer
**Identifier:** PMID 30307120 / PMC6275841 / DOI 10.1111/1759-7714.12824
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 392
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Inhibition of miR-24 suppresses malignancy of human non-small cell lung cancer cells by targeting WWOX in vitro and in vivo

## LIT-0393
**Short title:** WW domain-binding protein 2: an adaptor protein closely linked to the develop...
**Authors:** Chen et al.
**Year:** 2017
**Source type:** Review
**Journal/source:** Mol Cancer
**Identifier:** PMID 28724435 / PMC5518133 / DOI 10.1186/s12943-017-0693-9
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 393
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** cell line
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: WW domain-binding protein 2: an adaptor protein closely linked to the development of breast cancer

## LIT-0394
**Short title:** Bone metastatic process of breast cancer involves methylation state affecting...
**Authors:** Matteucci et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Eur J Cancer
**Identifier:** PMID 22717556 / DOI 10.1016/j.ejca.2012.05.006
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 394
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** mouse
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Bone metastatic process of breast cancer involves methylation state affecting E-cadherin expression through TAZ and WWOX nuclear effectors

## LIT-0395
**Short title:** A cascade of protein aggregation bombards mitochondria for neurodegeneration...
**Authors:** Sze et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Cell Death Dis
**Identifier:** PMID 26355344 / PMC4650446 / DOI 10.1038/cddis.2015.251
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 395
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — B
**Next action:** full-text retrieval; depth pass if model-shifting
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: A cascade of protein aggregation bombards mitochondria for neurodegeneration and apoptosis under WWOX deficiency

## LIT-0396
**Short title:** Hypoxia inducible factor-1 is activated by transcriptional co-activator with...
**Authors:** Bendinelli et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Eur J Cancer
**Identifier:** PMID 23566416 / DOI 10.1016/j.ejca.2013.03.002
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 396
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Hypoxia inducible factor-1 is activated by transcriptional co-activator with PDZ-binding motif (TAZ) versus WWdomain-containing oxidoreductase (WWOX) in hypoxic microenvironment of bone metastasis from breast cancer

## LIT-0397
**Short title:** Editorial: WW Domain Proteins in Signaling, Cancer Growth, Neural Diseases, a...
**Authors:** Chang et al.
**Year:** 2019
**Source type:** Editorial
**Journal/source:** Front Oncol
**Identifier:** PMID 31428585 / PMC6688159 / DOI 10.3389/fonc.2019.00719
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 397
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Editorial: WW Domain Proteins in Signaling, Cancer Growth, Neural Diseases, and Metabolic Disorders

## LIT-0398
**Short title:** Evidences that the polymorphism Pro-282-Ala within the tumor suppressor gene...
**Authors:** Cancemi et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Int J Cancer
**Identifier:** PMID 21520031 / DOI 10.1002/ijc.25937
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 398
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** Drosophila
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Evidences that the polymorphism Pro-282-Ala within the tumor suppressor gene WWOX is a new risk factor for differentiated thyroid carcinoma

## LIT-0399
**Short title:** Deletion and mutation of WWOX exons 6-8 in human non-small cell lung cancer
**Authors:** Zhou et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** J Huazhong Univ Sci Technolog Med Sci
**Identifier:** PMID 16116962 / DOI 10.1007/BF02873566
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 399
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** oncology / tumor suppressor biology
**Genotype/model tag:** unassigned in triage
**Species:** human
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Deletion and mutation of WWOX exons 6-8 in human non-small cell lung cancer

## LIT-0400
**Short title:** Fragile histidine triad protein, WW domain-containing oxidoreductase protein...
**Authors:** Guler et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Cancer
**Identifier:** PMID 19130459 / PMC2640223 / DOI 10.1002/cncr.24103
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 400
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
**Genotype/model tag:** unassigned in triage
**Species:** not assessed in triage
**Transferability:** unassigned in triage
**Directness to the reference genotype:** unassigned in triage
**Over-inference risk:** standard triage — not evaluated
**clinical relevance:** LOW
**Claim links:** none — triage only
**Working Model impact:** none yet
**Report mentions:** FASE 1 triage 221–400
**Current status:** screened — C
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Fragile histidine triad protein, WW domain-containing oxidoreductase protein Wwox, and activator protein 2gamma expression levels correlate with basal phenotype in breast cancer

---

## LIT-0401
**Short title:** Bendinelli 2017 HGF/Met bone metastasis — RETRACTED
**Authors:** Bendinelli P, Maroni P, Matteucci E, Desiderio MA et al.
**Year:** 2017 (retracted 2022)
**Source type:** original research — retracted publication
**Journal/source:** Cell Death & Disease
**Identifier type:** PMID / DOI / Retraction DOI
**Identifier value:** PMID 28151481 / DOI 10.1038/cddis.2016.403 / retraction DOI 10.1038/s41419-022-04992-6
**Date discovered:** 2026-07-09
**Date processed:** 2026-07-10 (URGENT integrity audit)
**Discovery window:** batch-50 2016–2018
**Discovery source:** PubMed retraction gate + full dependency audit
**Discovery query:** PMID 28151481 / author-line retraction audit
**Status:** excluded_integrity
**Status note:** retracted 2022 (retraction DOI 10.1038/s41419-022-04992-6); formerly `archived`, a value outside the vocabulary (`BATCH_20260926_LITVOCAB`)
**Primary pathway:** publication integrity / HGF-Met / bone metastasis
**Genotype/model tag:** oncology; not a WWOX-DEE model
**Transferability:** none
**clinical relevance:** LOW scientific directness / HIGH epistemic-integrity relevance
**Claim links:** none
**Working Model impact:** source excluded; no baseline claim or BLOCCO change
**Report mentions:** URG_2026-07-09_001 / CC-2026-07-09-002
**Next action:** none — never use as evidence; retain permanently for dedup and dependency auditing
**Flags:** RETRACTED / invalid evidence / western-blot integrity / category-5 urgent
**Note:** Official 2022 retraction states that duplicated, reused or manipulated vinculin controls across Figures 3–6 invalidate confidence in the results. The derivative Maroni 2017 review (PMID 28045433; LIT-0085 / CORPUS-STUB-061) reuses data from this source and is therefore `dependency-contaminated / background_only`. No canonical claim depended on either record at the time of repair.

---

## LIT-0402
**Short title:** Saadane 2021 — photoreceptor calpain–WWOX
**Authors:** Saadane A, Du Y, Thoreson WB, Miyagi M, Lessieur EM, Kiser J, Wen X, Berkowitz BA, Kern TS
**Year:** 2021
**Source type:** primary — in vivo mouse + ex vivo retina + 661W cone line
**Journal/source:** *The American Journal of Pathology* 191(10):1805-1821
**Identifier type:** PMID / PMCID / DOI
**Identifier value:** PMID 34214506 / PMC8579242 / DOI 10.1016/j.ajpath.2021.06.006
**Date discovered:** 2026-07-05 (corpus seed `corpus_seed_pubmed_20260705.tsv`)
**Date processed:** 2026-07-26
**Discovery window:** corpus seed 2026-07-05
**Discovery source:** corpus seed + batch inferential sweep (random draw, seed `LEGEND-TEST-20260726`)
**Discovery query:** WWOX corpus seed — never-processed partition
**Status:** claim_linked
**Primary pathway:** P5 — metabolism / mitochondria / redox; secondary P1 — Ca²⁺
**Genotype/model tag:** wild-type WWOX, acute siRNA knockdown; **no WWOX-variant model**
**Transferability:** T3
**clinical relevance:** INDIRECT
**Claim links:** CLAIM 034 (new) · CLAIM 028 (supports) · CLAIM 009 (tensions)
**Working Model impact:** BLOCK 2 only — CLAIM 034 added; CLAIM 009 carries a mandatory counter-directional note. No BLOCK 1 change
**Report mentions:** CC-20260726-001 → BATCH_20260726_001
**Next action:** none for this record; the calpain proteolysis arc stays open in DIS-008 with its `REVIVAL_TRIGGER`
**Flags:** full text read (receipt `FTR-20260726-34214506-01`) / parity-of-sources case / source-correction registered / multi-hop reading debt declared
**Note:** Promosso a [[paper_registry_current#PAPER 054]]. Il titolo promette retinopatia diabetica; il contenuto è un asse Ca²⁺→calpaina→WWOX→ROS in un neurone eccitabile, con un hit proteomico non guidato su WWOX. Filed by disease label sarebbe stato rumore. Debito di lettura dichiarato e **non pagato** in questa sessione: PMID 28123895 (C1q → attivazione di WWOX, coda HIGH) e PMID 21444760 (Wwox come candidato HDL da QTL murino, coda MEDIUM), più i riferimenti 38/39 non risolti a PMID.

---

## LIT-0403
**Short title:** Rotem-Bamberger 2022 — WW2 e cooperatività tandem WW-PPxY
**Authors:** Rotem-Bamberger S et al.
**Year:** 2022
**Source type:** primary — biofisica strutturale in vitro
**Journal/source:** *Journal of Biological Chemistry* 298(8):102145
**Identifier type:** PMID / PMCID / DOI
**Identifier value:** PMID 35716775 / PMC9293652 / DOI 10.1016/j.jbc.2022.102145
**Date discovered:** 2026-07-05 (corpus seed `corpus_seed_pubmed_20260705.tsv`)
**Date processed:** 2026-07-26
**Discovery window:** corpus seed 2026-07-05
**Discovery source:** corpus seed + study-intake triage
**Discovery query:** WWOX corpus seed — never-processed partition
**Status:** claim_linked
**Primary pathway:** architettura di dominio / interpretazione delle varianti
**Genotype/model tag:** WWOX wild-type, frammenti WW; **nessun allele WWOX-DEE testato**
**Transferability:** T2/T3 indiretta
**clinical relevance:** INDIRECT
**Claim links:** CLAIM 024 (primary) · CLAIM 028 (secondary)
**Working Model impact:** BLOCK 2 only — precisazione del linguaggio su «Domain cooperativity»; nessun claim nuovo, nessun cambio BLOCK 1
**Report mentions:** CC-20260726-002 → BATCH_20260726_001
**Next action:** nessuna. La fusione con il placeholder [[paper_registry_current#CORPUS P204]] resta **non eseguita** finché la lineage non è confermata
**Flags:** full text read (receipt `FTR-20260726-35716775-02`) / placeholder lineage unresolved / engineered-construct caveat
**Note:** Promosso a [[paper_registry_current#PAPER 055]]. ⚠️ Il candidato citava `CORPUS P376` come lineage: è un indice della TSV di seed e **non** il record [[paper_registry_current#CORPUS P376]] del registry (Farooq 2015, PMID 25662954). Riferimento scartato in fase di commit per evitare una falsa identità fra due pubblicazioni diverse.

---

## LIT-0404
**Short title:** Wang 2012 — WWOX ⊣ GSK3β via L404
**Authors:** Wang H-Y, Juo L-I, Lin Y-T, Hsiao M, Lin J-T, Tsai C-H, Tzeng Y-H, Chuang Y-C, Chang N-S, Yang C-N, Lu P-J
**Year:** 2012
**Source type:** primary — biochimica + biologia cellulare + co-IP endogena da cervello di topo
**Journal/source:** *Cell Death and Differentiation* 19(6):1049-1059
**Identifier type:** PMID / PMCID / DOI
**Identifier value:** PMID 22193544 / PMC3354054 / DOI 10.1038/cdd.2011.188
**Date discovered:** 2026-07-05 (corpus seed `corpus_seed_pubmed_20260705.tsv`)
**Date processed:** 2026-07-26
**Discovery window:** corpus seed 2026-07-05
**Discovery source:** corpus cross-query — il paper risultava **portante in cinque file del modello senza essere mai stato letto**
**Discovery query:** `L404` / `388-407` cross-query sul modello (9 hit)
**Status:** claim_linked
**Primary pathway:** P1 — neurosviluppo / GSK3β–Tau–microtubuli; funzione SDR
**Genotype/model tag:** WWOX wild-type + mutanti ingegnerizzati L404A/L311A, troncamenti Δ286/Δ389; **nessun allele WWOX-DEE**
**Transferability:** T2
**clinical relevance:** INDIRECT — alto come saggio e vincolo di disegno
**Claim links:** CLAIM 035 (new) · CLAIM 016 (enriched) · CLAIM 030 · CLAIM 028
**Working Model impact:** BLOCK 2 only — CLAIM 035 added, CLAIM 016 arricchito con il meccanismo e con un `PREMISE_TAG`. Nessun cambio BLOCK 1
**Report mentions:** CC-20260726-003 → BATCH_20260726_001
**Next action:** acquisire [[full_text_queue_current#FT-022]]–[[full_text_queue_current#FT-025]]; l'esperimento discriminante proposto (pull-down GSK3β su WWOX-WT vs Q230P vs G372R vs L404A) resta non eseguito
**Flags:** full text read (receipts `FTR-20260726-22193544-01` + `-02`) / **UNREAD_PREMISE risolta** / difetto di figura supplementare documentato / author-dispute flag (Chang N-S)
**Note:** Promosso a [[paper_registry_current#PAPER 056]]. Chiude il missing-info item #7 del red-team Q230P: **L404 è confermato necessario** al legame WWOX–GSK3β da cinque readout indipendenti, quindi la zona di esclusione 388–407/L404 per uno stabilizzatore SDR passa da *citata* a `DATO`. 🔴 Difetto della fonte: la Supplementary Figure A non contiene alcun blot per Tau pur essendo citata come la co-IP che dimostra il negativo — vedi DIS-010 e la riga `D-14` di *DEFAULTS THAT BIT US*. ⚠️ Il riferimento `CORPUS P263` del candidato è un indice della TSV di seed, non il record [[paper_registry_current#CORPUS P263]] del registry (Chang 2014, PMID 25537520).

---

## LIT-0405
**Short title:** Suzuki 2007 — fenotipo originario del ratto `lde`, prima del gene
**Authors:** Suzuki H, Takenaka M, Suzuki K
**Year:** 2007
**Source type:** primary — caratterizzazione fenotipica di un mutante spontaneo
**Journal/source:** *Comparative Medicine* 57(4):360–369
**Identifier type:** PMID
**Identifier value:** PMID 17803050 — **nessun DOI registrato, nessun PMCID**
**Date discovered:** 2026-08-06
**Date processed:** 2026-08-06
**Discovery window:** multi-hop 2026-08-06
**Discovery source:** referenza 27 di PMID 19936220 e riferimento portante di PMID 19500159 — l'unico dei riferimenti WWOX-diretti assente da ogni registro
**Discovery query:** enumerazione delle referenze durante la lettura completa di `FT-043`, poi di `FT-042`
**Status:** claim_linked
**Primary pathway:** P5 — metabolismo / rene
**Genotype/model tag:** ratto, locus `lde` **ipotetico** — il gene non era ancora identificato
**Species:** rat
**Transferability:** T3
**Directness to the reference genotype:** bassa — nessun allele umano, nessun gene identificato all'epoca
**Over-inference risk:** **alto se letto solo per abstract**, vedi sotto
**clinical relevance:** INDIRECT
**Claim links:** CLAIM 038 (new, primary) · CLAIM 039 (new, primary) · CLAIM 037 (co-source)
**Working Model impact:** BLOCK 2 only — CLAIM 038 e 039 aggiunti, CLAIM 037 co-sorgente. Nessun cambio BLOCCO 1.
**Report mentions:** CC-20260806-17803050 → BATCH_20260806_002
**Next action:** nessuna coda aperta da questo paper. L'esperimento discriminante — clearance renale, o creatina-chinasi e massa muscolare in parallelo — è registrato in [[claim_registry_current#CLAIM 038]].
**Flags:** full text read (receipt `FTR-20260806-17803050-01`) / **recuperato solo per via operatore** — nessun DOI rende il record irraggiungibile da Unpaywall, OpenAlex e Semantic Scholar / **UNREAD_PREMISE risolta** per tre affermazioni di [[paper_registry_current#PAPER 058]]
**Note:** Promosso a [[paper_registry_current#PAPER 059]]. 🔴 **Ha refutato una citazione che poggiava su di esso:** PMID 19500159 attribuisce il nanismo `lde` al GH ipofisario basso citando questo paper; qui la differenza **non è significativa** e il paper conclude che il nanismo *"cannot be explained solely by low levels of plasma GH"*. La frase non qualificata esiste **solo nell'abstract** di questo stesso paper — l'abstract sovradichiara il proprio corpo. **Nota di metodo:** il 2026-08-06 l'operatore aveva fornito prima il solo abstract, registrato come `abstract_only` **senza receipt**, lasciando `FT-041` aperta. Se fosse stato accettato come lettura, «GH ridotto» sarebbe entrato nel modello come dato, e non lo è. È il controfattuale più pulito della regola *un abstract non è una lettura*.

---

## BATCH_20260710_B — tracking

Promossi da `CORPUS` placeholder a `PAPER` completi (i placeholder restano come audit trail, marcati `promoted`):

| PAPER | PMID | Studio | Origine |
|---|---|---|---|
| 040 | 33916893 | Banne 2021, *Cells* — overview varianti germinali WWOX | CORPUS-STUB-013 |
| 043 | 24456803 | Abdel-Salam 2014, *Orphanet J Rare Dis* — p.Arg54\*, letale 16 mesi | CORPUS P359 |
| 044 | 30362252 | Davids 2019, *Hum Mutat* — EIEE28 / UPD, isoform-resolved assay | CORPUS P300 |
| 046 | 38161429 | Battaglia 2023, *Front Pediatr* — neuroimaging WOREE (**background**) | CORPUS P298 |
| 049 | 27495153 | Elsaadany 2016, *BMC Med Genet* — W44X | CORPUS P343 |
| 050 | 26857392 | Schirmer 2016, *JNCI* — Sp1 / assay giunzione esone 8-9 | CORPUS P312 |
| 053 | 24932569 | Aldaz 2014, *BBA* — crossroads (**background** + CLAIM 032) | CORPUS-STUB-020 |

**Duplicato evitato:** Tochigi 2019 (PMID 31340538) **era già [[paper_registry_current#PAPER 021]]** → non creato; CLAIM 032 vi è stato ancorato.

**Nuovo CLAIM 033** (genotipo↔mortalità) ancorato a PAPER 018 + 040 + 041, con quattro riserve obbligatorie **dentro** il claim.

**Rinviati a un batch successivo (motivo esplicito):**
- `CC-2026-07-05-005` — source-normalization corpus 181-220 → PAPER 033-038 (+ CLAIM 022/023/024/025/027/028).
- `CC-2026-07-09-003` — Chang JY 2015: **ambiguità irrisolta** fra PMID 27551439 (*Cell Death Discov*) e 26355344 (*Cell Death Dis*), fusi in un unico record dal triage. Da sciogliere prima di creare PAPER 047/048 e il CLAIM "SDR = scaffold anti-aggregazione".
- `CC-2026-07-09-001` — PAPER 051/052 (oncologia/meccanismi indiretti).
- `CC-2026-07-05-008` — upgrade di PAPER 001 (Aqeilan/Davila, *Brain* awag239) + CLAIM WWOX⊣MYC.
- `CC-2026-07-05-006` — residuo: estensione di CLAIM 002 (il PAPER 039 è già creato in Batch A).
- Upgrade full-text di PAPER 024 (Abu-Remaileh 2014).

---

## BATCH_20260726_001 — tracking

Tre candidati propagati, tutti da **lettura integrale con ricevuta persistita** (nessuna promozione da abstract):

| PAPER | LIT | PMID | Studio | Candidato | Claim |
|---|---|---|---|---|---|
| 054 | LIT-0402 | 34214506 | Saadane 2021, *Am J Pathol* — Ca²⁺/calpaina/WWOX nei fotorecettori | CC-20260726-001 | **CLAIM 034** (new); nota controdirezionale su CLAIM 009 |
| 055 | LIT-0403 | 35716775 | Rotem-Bamberger 2022, *JBC* — WW2 e cooperatività tandem | CC-20260726-002 | CLAIM 024 precisato (nessun claim nuovo) |
| 056 | LIT-0404 | 22193544 | Wang 2012, *Cell Death Differ* — WWOX ⊣ GSK3β via L404 | CC-20260726-003 | **CLAIM 035** (new); CLAIM 016 arricchito |

**Conflitti rilevati e risolti in fase 2 (non propagati come proposti):**
- I candidati CC-002 e CC-003 citano rispettivamente `CORPUS P376` e `CORPUS P263` come lineage dei rispettivi studi. **Sono indici della TSV di seed, non ID del registry**: nel registry quei due ID appartengono a pubblicazioni diverse (Farooq 2015, PMID 25662954; Chang 2014, PMID 25537520). I riferimenti sono stati **scartati** e i tre PAPER ancorati ai soli PMID/DOI, che sono non ambigui. Difetto registrato nelle note dei record.
- CC-002 proponeva la fusione condizionale del placeholder [[paper_registry_current#CORPUS P204]] (fonte di CLAIM 024, Identifier PENDING) con PMID 35716775. La condizione — *«se la lineage del batch lo conferma»* — **non è verificata**: fusione non eseguita, placeholder conservato, CLAIM 024 ancorato alla fonte identificata con il pointer storico mantenuto come audit trail.
- CC-001 proponeva voci di ledger con uno schema di ID inesistente in questo repository (`DISC-2026-07-26-A/B/C`, `DISM-2026-07-26-A`). Le voci erano **già atterrate** con lo schema corretto (`DL-MECH-061`, `DIS-008`) prima del commit: i wikilink dei claim puntano agli ID reali, non a quelli proposti.

**Debito dichiarato e non pagato:** PMID 28123895 (C1q → attivazione WWOX, coda HIGH) · PMID 21444760 (Wwox/HDL da QTL murino, coda MEDIUM) · riferimenti 38/39 di PMID 34214506 non risolti a PMID · [[full_text_queue_current#FT-022]]–[[full_text_queue_current#FT-025]] dall'espansione multi-hop di PMID 22193544.

---

## LIT-0406
**Short title:** Drusco 2011 fragile-site mouse-model review
**Identifier:** PMID 21318118 / PMCID PMC3035048 / DOI 10.1155/2011/984505
**Date processed:** 2026-08-10
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 064]] (`BATCH_20260815_001`)
**Evidence depth:** complete_fulltext_read — `FTR-20260810-21318118-01`
**Claim links:** none

## LIT-0407
**Short title:** Bidany-Mizrahi 2026 WWOX/p53 cutaneous SCC
**Identifier:** PMID 41984841 / PMCID PMC13099603 / DOI 10.1073/pnas.2534844123
**Date processed:** 2026-08-10
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 070]] (`BATCH_20260815_001`)
**Evidence depth:** complete_fulltext_read — `FTR-20260810-41984841-01`
**Claim links:** CLAIM 032

## LIT-0408
**Short title:** Aqeilan 2009 impaired steroidogenesis
**Identifier:** PMID 18974271 / PMCID PMC2654736 / DOI 10.1210/en.2008-1087
**Date processed:** 2026-08-11
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 076]] (`BATCH_20260815_001`)
**Evidence depth:** complete_fulltext_read — `FTR-20260811-18974271-01`
**Claim links:** CLAIM 036

## LIT-0409
**Short title:** Aqeilan 2007 targeted Wwox deletion
**Identifier:** PMID 17360458 / PMCID PMC1820689 / DOI 10.1073/pnas.0609783104
**Date processed:** 2026-08-11
**Status:** processed
**Status note:** completed — [[paper_registry_current#PAPER 078]] (`BATCH_20260815_001`)
**Evidence depth:** complete_fulltext_read with declared SI gap — `FTR-20260811-17360458-01`
**Claim links:** CLAIM 032 · CLAIM 036

## LIT-0410
**Short title:** WWOX–p73 functional association (Aqeilan 2004)
**Authors:** Aqeilan RI, Pekarsky Y, Herrero JJ, Palamarchuk A, Letofsky J, Druck T, Trapasso F, Han S-Y, Melino G, Huebner K, Croce CM
**Year:** 2004
**Source type:** primary experimental
**Journal/source:** PNAS 101(13):4401–4406
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 15070730 / DOI 10.1073/pnas.0400805101 / PMC384759
**Date discovered:** 2026-09-08 (Aqeilan free-full-text sweep dispatch)
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** Aqeilan 54-PMID sweep
**Discovery source:** orchestration dispatch 2026-09-08 / task contracts AQEILAN-FT-A/B/C-001
**Discovery query:** Aqeilan RI free full text
**Status:** processed
**Status note:** complete_fulltext_read
**Evidence depth:** complete_fulltext_read — `FTR-20260909-15070730-02` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 081]]
**Primary pathway:** signaling organization / routing / scaffold logic
**Genotype/model tag:** no WWOX-DEE allele
**Transferability:** T2
**clinical relevance:** INDIRECT
**Claim links:** CLAIM 023
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** orchestration_reviews/2026-09-09.md
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001
**Note:** Identified primary source of CLAIM 023. Its title clause coupling phosphorylation to rerouting is NARROWED in this batch: 20 body sentences mention Src, zero also mention localisation. Promoted from CORPUS P206, whose Identifier was the literal string PENDING.

---

## LIT-0411
**Short title:** Pancreatic Ad-WWOX restoration (Nakayama 2008)
**Authors:** Nakayama S, Semba S, Maeda N, Aqeilan RI, Huebner K, Yokozaki H
**Year:** 2008
**Source type:** primary experimental
**Journal/source:** Cancer Sci 99(7):1370–1376
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 18460020 / DOI 10.1111/j.1349-7006.2008.00841.x / PMC11159152
**Date discovered:** 2026-09-08 (Aqeilan free-full-text sweep dispatch)
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** Aqeilan 54-PMID sweep
**Discovery source:** orchestration dispatch 2026-09-08 / task contracts AQEILAN-FT-A/B/C-001
**Discovery query:** Aqeilan RI free full text
**Status:** processed
**Status note:** complete_fulltext_read
**Evidence depth:** complete_fulltext_read — `FTR-20260909-18460020-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 083]]
**Primary pathway:** oncology / TGF-beta / SMAD4
**Genotype/model tag:** no WWOX-DEE allele
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** orchestration_reviews/2026-09-09.md
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001
**Note:** Carries a Reagent provenance field: Ad-WWOX, Ad-GFP and both anti-Wwox antibodies all cite PMID 16223882, which carries a standing expression of concern. Nothing about adenoviral or AAV WWOX delivery in a neuronal context may cite this paper.

---

## LIT-0412
**Short title:** WWOX cis-regulatory variation and low plasma HDL-C (Lee 2008)
**Authors:** Lee JC, Weissglas-Volkov D, Kyttälä M, … Croce CM, Aqeilan RI, … Pajukanta P
**Year:** 2008
**Source type:** primary human genetic association
**Journal/source:** Am J Hum Genet 83(2):180–192
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 18674750 / DOI 10.1016/j.ajhg.2008.07.002 / PMC2495060
**Date discovered:** 2026-09-08 (Aqeilan free-full-text sweep dispatch)
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** Aqeilan 54-PMID sweep
**Discovery source:** orchestration dispatch 2026-09-08 / task contracts AQEILAN-FT-A/B/C-001
**Discovery query:** Aqeilan RI free full text
**Status:** processed
**Status note:** complete_fulltext_read
**Evidence depth:** complete_fulltext_read — `FTR-20260909-18674750-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 084]]
**Primary pathway:** P5 — metabolism / lipids
**Genotype/model tag:** no WWOX-DEE allele
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** orchestration_reviews/2026-09-09.md
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001
**Note:** The corpus only human quantitative WWOX phenotype outside cancer and outside neurodevelopment. No neural endpoint; licenses no transfer to the reference genotype.

---

## LIT-0413
**Short title:** WWOX in HTLV-I Tax tumorigenesis (Fu 2011)
**Authors:** Fu J, Qu Z, Yan P, Ishikawa C, Aqeilan RI, Rabson AB, Xiao G
**Year:** 2011
**Source type:** primary experimental
**Journal/source:** Blood 117(5):1652–1661
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 21115974 / DOI 10.1182/blood-2010-08-303073 / PMC3318777
**Date discovered:** 2026-09-08 (Aqeilan free-full-text sweep dispatch)
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** Aqeilan 54-PMID sweep
**Discovery source:** orchestration dispatch 2026-09-08 / task contracts AQEILAN-FT-A/B/C-001
**Discovery query:** Aqeilan RI free full text
**Status:** processed
**Status note:** complete_fulltext_read
**Evidence depth:** complete_fulltext_read — `FTR-20260909-21115974-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 086]]
**Primary pathway:** viral oncology / NF-kB
**Genotype/model tag:** no WWOX-DEE allele
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** CLAIM 023
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** orchestration_reviews/2026-09-09.md
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001
**Note:** Group Xiao, not the Aqeilan group. R4 audit run and NOT clean: 12 of 32 triples defective, one disqualifying. Corroborates the not-only-by-binding leg of CLAIM 023; its rerouting-exclusion leg did not survive audit and is recorded as an author assertion on unshown data.

---

## LIT-0414
**Short title:** Editor introduction, CMLS 71(23) fragile-site special issue (Aqeilan 2014)
**Authors:** Aqeilan RI
**Year:** 2014
**Source type:** secondary — editor introduction
**Journal/source:** Cell Mol Life Sci 71(23):4487–4488
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 25238781 / DOI 10.1007/s00018-014-1716-y / PMC11113964
**Date discovered:** 2026-09-08 (Aqeilan free-full-text sweep dispatch)
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** Aqeilan 54-PMID sweep
**Discovery source:** orchestration dispatch 2026-09-08 / task contracts AQEILAN-FT-A/B/C-001
**Discovery query:** Aqeilan RI free full text
**Status:** processed
**Status note:** complete_fulltext_read
**Evidence depth:** complete_fulltext_read — `FTR-20260909-25238781-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 087]]
**Primary pathway:** fragile-site taxonomy
**Genotype/model tag:** no WWOX-DEE allele
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** orchestration_reviews/2026-09-09.md
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001
**Note:** Two pages, single-authored, no figure or table, 11 references, received and accepted the same day. PubMed and PMC both over-describe it as a review. Carries the taxonomic finding: twelve neurological terms occur zero times each over the 7,211-character body.

---

## LIT-0415
**Short title:** Hazan & Aqeilan 2015 — editorial, not review
**Authors:** Hazan I, Aqeilan RI
**Year:** 2015
**Source type:** secondary — EDITORIAL
**Journal/source:** Cell Death Discov 1:15040
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 27551470 / DOI 10.1038/cddiscovery.2015.40 / PMC4979517
**Date discovered:** 2026-09-08 (Aqeilan free-full-text sweep dispatch)
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** Aqeilan 54-PMID sweep
**Discovery source:** orchestration dispatch 2026-09-08 / task contracts AQEILAN-FT-A/B/C-001
**Discovery query:** Aqeilan RI free full text
**Status:** processed
**Status note:** complete_fulltext_read
**Evidence depth:** complete_fulltext_read — `FTR-20260909-27551470-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 090]]
**Primary pathway:** fragile-site / WWOX passive-vs-active
**Genotype/model tag:** no WWOX-DEE allele
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** orchestration_reviews/2026-09-09.md
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001
**Note:** PMC deposit carries article-type editorial; PubMed assigns no Review tag. Standing caution: of its 17 references this repository holds four, and on all four checking changed something.

---

## LIT-0416
**Short title:** Published erratum to PMID 38182577 (WWOX/Myc osteosarcoma)
**Authors:** Cell Death & Disease editorial office
**Year:** 2024
**Source type:** published erratum
**Journal/source:** Cell Death Dis 15(2):141
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 38355659 / DOI 10.1038/s41419-024-06518-8 / PMC10867017
**Date discovered:** 2026-09-08 (Aqeilan free-full-text sweep dispatch)
**Date processed:** 2026-09-09 (BATCH_20260909_001)
**Discovery window:** Aqeilan 54-PMID sweep
**Discovery source:** orchestration dispatch 2026-09-08 / task contracts AQEILAN-FT-A/B/C-001
**Discovery query:** Aqeilan RI free full text
**Status:** processed
**Status note:** complete_fulltext_read
**Evidence depth:** complete_fulltext_read — `FTR-20260909-38355659-01` (BATCH_20260909_001)
**Registry record:** [[paper_registry_current#PAPER 092]]
**Primary pathway:** oncology / osteosarcoma
**Genotype/model tag:** no WWOX-DEE allele
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** orchestration_reviews/2026-09-09.md
**Next action:** none — read and integrated
**Flags:** read BATCH_20260909_001
**Note:** Read as its own source; establishes the corrected scope of PMID 38182577 from the deposit itself, closing its SCOPE_UNDECLARED status. Corrects an author name only; the title is unchanged.

---

## LIT-0417
**Identifier value:** PMID 42397075 / DOI 10.1093/brain/awag239
**Short title:** Steinberg 2026 — disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids
**Journal/source:** *Brain* 2026
**Status:** processed
**Status note:** complete — read in full, `FTR-20260810-42397075-04`; registry record [[paper_registry_current#PAPER 094]] (status set to the registry record's value by `BATCH_20260926_LITVOCAB`)
**Discovery window:** post-harvest; this PMID had no literature entry before BATCH_20260920_002
**Flags:** created by `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01` to give an existing complete reading the entry its PAPER record links to

---

## LIT-0418
**Short title:** Ludes-Meyers 2007 — Wwox hypomorphic gene-trap mice: viable, reduced survival, B-cell lymphomas in females, testicular atrophy
**Authors:** Ludes-Meyers JH, Kil H, Nuñez MI, Conti CJ, Parker-Thornburg J, Bedford MT, Aldaz CM
**Year:** 2007
**Source type:** primary research — mouse genetics, long-term ageing/tumorigenesis cohort, histopathology (NIH author manuscript NIHMS222061)
**Journal/source:** *Genes Chromosomes Cancer* 46(12):1129-1136
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 17823927 / DOI 10.1002/gcc.20497 / PMC4143238
**Date discovered:** 2026-09-14 (`SCIENCE-EXEC-20260914`, VPS laboratory checkout)
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** Aldaz series reconciliation, 2026-09-14
**Discovery source:** `CC-20260914-17823927-01`; the paper was restated in `CLAIM 032` with no registry record
**Discovery query:** hypomorph leg of `CLAIM 032`
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-17823927-01`; record created by `BATCH_20260926_ALDAZ_R2`
**Primary pathway:** P7 — gene therapy readiness / dose-threshold logic
**Genotype/model tag:** topo ipomorfo gene-trap, nessun materiale neurale, nessun allele WWOX umano
**Transferability:** T3
**clinical relevance:** INDIRECT-LOW
**Claim links:** none — held for the claim batch
**Working Model impact:** none in this batch — the `CLAIM 032` Summary correction is held for the claim batch
**Report mentions:** `CC-20260914-17823927-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-17823927-01`
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-17823927-01`; manifest `deepdive_manifests/PMID17823927.json`
**Registry record:** [[paper_registry_current#PAPER 098]]
**Note:** Title: Wwox hypomorphic mice display a higher incidence of B-cell lymphomas and develop testicular atrophy

---

## LIT-0419
**Short title:** Ramos 2008 — WWOX IHC in 101 bladder tumours: loss correlates with grade, stage and progression
**Authors:** Ramos D, Abba M, López-Guerrero JA, Rubio J, Solsona E, Almenar S, Llombart-Bosch A, Aldaz CM
**Year:** 2008
**Source type:** primary research — serie clinica retrospettiva monocentrica con immunoistochimica (NIH author manuscript NIHMS222064)
**Journal/source:** *Histopathology* 52(7):831-839
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 18452537 / DOI 10.1111/j.1365-2559.2008.03033.x / PMC4151645
**Date discovered:** 2026-09-14 (`SCIENCE-EXEC-20260914`, VPS laboratory checkout)
**Date processed:** 2026-09-26 (`BATCH_20260926_ALDAZ_R2`)
**Discovery window:** Aldaz series reconciliation, 2026-09-14
**Discovery source:** `CC-20260914-18452537-01`; the PMID had no record in the log (checked by PMID, DOI, PMCID and title)
**Discovery query:** unread and unregistered Aldaz series paper
**Status:** processed
**Status note:** complete_fulltext_read — `FTR-20260914-18452537-01`; record created by `BATCH_20260926_ALDAZ_R2`
**Primary pathway:** oncologia adulta / biomarcatore tissutale, fuori dagli assi del modello
**Genotype/model tag:** tessuto vescicale umano adulto, nessun allele WWOX, nessun materiale neurale
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no working-model block is redefined by this record
**Report mentions:** `CC-20260914-18452537-01` · `BATCH_20260926_ALDAZ_R2`
**Next action:** none — read and registered
**Flags:** read — receipt `FTR-20260914-18452537-01`
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260914-18452537-01`; manifest `deepdive_manifests/PMID18452537.json`
**Registry record:** [[paper_registry_current#PAPER 099]]
**Note:** Title: Low levels of WWOX protein immunoexpression correlate with tumour grade and a less favourable outcome in patients with urinary bladder tumours

---

## LIT-0420
**Short title:** Hammouz 2026 IJMS — WWOX/HIF1A balance across BRCA subtypes and ovarian carcinoma (TCGA, DFS proxy)
**Authors:** Hammouz RY, Maciejek K, Bednarek AK
**Year:** 2026
**Source type:** primary research — retrospective bioinformatic analysis of TCGA RNA-seq and clinical data
**Journal/source:** *Int J Mol Sci* 2026;27(15):6740
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42589397 / DOI 10.3390/ijms27156740 / PMC13467099
**Date discovered:** 2026-09-21 (`FT-144`, singleton imported from `human_genotype_and_claim025_wave1b_20260921.md`)
**Date processed:** 2026-09-27 (first-hand read, `FTR-20260927-42589397-02`)
**Discovery window:** wave-1b sibling-node import, 2026-09-21
**Discovery source:** `FT-144`; the PMID had no record in this log (checked by PMID, DOI, PMCID and title — the same group's PMID 41007296 is `LIT-0019` and is a DIFFERENT paper)
**Discovery query:** `CLAIM 025` sign-invariance bound
**Status:** processed
**Status note:** `partial_fulltext_read` — receipts `FTR-20260921-42589397-01` (a verification receipt of another actor's reading, tables and figures declared unavailable) and `FTR-20260927-42589397-02` (first-hand, PMC JATS XML). 🔴 **Record created 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` (Mirror M3):** the reading bounded `CLAIM 025` on 2026-09-27 while no registry record named this PMID at all, so the bound was invisible to `trace_claim_foundation` and LINT could only emit `UNLINKED_SUPPORT_UNCHECKED`.
**Primary pathway:** P5 — HIF1A / metabolismo (contesto oncologico)
**Genotype/model tag:** dati umani tumorali TCGA (mammella, ovaio); nessun allele WWOX, nessun materiale neurale, nessuna perturbazione
**Transferability:** T3
**clinical relevance:** BACKGROUND — bounds `CLAIM 025` on the direction of the ratio–outcome association; authorises no CNS transfer
**Claim links:** 025 (bounding source, non-corroborating: same group, same dataset family, tumour only, no perturbation)
**Working Model impact:** none — no block is redefined; the record bounds an existing claim's direction
**Report mentions:** `CC-20260922-CLAIM025-SIGN-INVARIANCE-01` · `BATCH_20260927_003` · `CC-20260928-MIRROR003-REPAIRS-01`
**Next action:** none owed on the supplement — Supplementary Tables S4–S8 read 2026-09-28 (`FTR-20260928-42589397-04`); ⚠️ Table S7's HR column contradicts its own «more favourable DFS group» labels for HER2-enriched and Luminal B (detail in [[paper_registry_current#PAPER 118]]); an author query on the HR orientation is optional, not blocking
**Flags:** read — partial (body + Supplementary File S1); supplementary S4–S8 debt discharged 2026-09-28; source-internal Table S7 inconsistency recorded
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20260927-42589397-02`; manifest `deepdive_manifests/PMID42589397.json`, **7** verbatim locators — 5 persisted with `FTR-20260927-42589397-02`, 2 appended 2026-09-28 (entries 6–7, `Results 2.6.2` and `Methods 5.1`) inside that receipt's declared coverage and re-verified verbatim here; its `receipt` field carried `FTR-20260921-42589397-01` and now names **`FTR-20260927-42589397-02`**, the reading that produced it — 🟢 repaired 2026-09-28 by `framework/scripts/manifest_receipt_repoint.py`, which derives the value from the ledger; `manifest_receipt_provenance.py --pmid 42589397` reports **CONFORMS**. The old value named this manifest in no `outputs` and fingerprinted a different document from the artefact the manifest declares, so the repair tightened the artefact binding as well as the pointer (present tense corrected 2026-09-28 by `CC-20260928-MIRROR002B-REPAIRS-01`, discharging `REP-26`, from *«still names `FTR-20260921-42589397-01` and is routed for re-pointing»*). **One** evidence gap was declared (Supplementary Tables S4–S8 unfetched) and is discharged by `FTR-20260928-42589397-04`; the **five** are the manifest's `waived` deep-dive sections, which `deepdive_manifest.py` prints as *"5 gap(s)"* in its own vocabulary (disambiguated 2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDINGS 4 and 5)
**Registry record:** [[paper_registry_current#PAPER 118]]
**Note:** Title: WWOX/HIF1A Balance Delineates Context-Dependent Molecular States in Breast Cancer Subtypes and Ovarian Carcinoma. The authors declare their subtype effects *"descriptive and hypothesis-generating rather than formally validated prognostic groupings"*.

---

## LIT-0421
**Short title:** Bayanova 2023 Mol Neurobiol — WGS in 20 children with early-onset epilepsy; one WWOX compound heterozygote (missense + splice donor)
**Authors:** Bayanova M et al.
**Year:** 2023
**Source type:** primary research — diagnostic WGS case series (n = 20)
**Journal/source:** *Mol Neurobiol* 2023;60(8)
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 37095367 / DOI 10.1007/s12035-023-03346-3 / PMC10293429
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-37095367-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02 (PubMed abstract, Europe PMC body check, dedup against the registries)
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261002-INTAKE-A-REGISTRY-01`
**Primary pathway:** clinical spectrum / WWOX-DEE
**Transferability:** T2 (one case; segregation and function absent)
**clinical relevance:** LOW-MODERATE — one new case, alleles named, no segregation
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_A.md` · `CC-20261002-INTAKE-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID37095367.json`

## LIT-0422
**Short title:** Rim 2018 BMC Med Genomics — 172-gene panel in 74 intractable early-onset epilepsies; one WWOX compound heterozygote (last-exon nonsense + exon 6–8 duplication)
**Authors:** Rim JH et al.
**Year:** 2018
**Source type:** primary research — diagnostic panel series (n = 74)
**Journal/source:** *BMC Med Genomics* 2018;11:6
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 29390993 / DOI 10.1186/s12920-018-0320-7 / PMC5796507
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-29390993-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02 (PubMed abstract, Europe PMC body check, dedup against the registries)
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261002-INTAKE-A-REGISTRY-01`
**Primary pathway:** clinical spectrum / WWOX-DEE · allele classes
**Transferability:** T1 (human; neither allele is the reference genotype's)
**clinical relevance:** MODERATE — the only intragenic WWOX duplication in LEGEND, with carrier parents asymptomatic by inclusion criterion
**Claim links:** 032 (carrier observation; not a supporting source)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_A.md` · `CC-20261002-INTAKE-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID29390993.json`

## LIT-0423
**Short title:** Szymańska 2014 Biomed Res Int — seven neurodevelopmental/neurometabolic cases; a 16q23.1 duplication called 'WWOX and MAF'
**Authors:** Szymańska K et al.
**Year:** 2014
**Source type:** primary research — clinical case series (n = 7)
**Journal/source:** *Biomed Res Int* 2014:424796
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 24949445 / DOI 10.1155/2014/424796 / PMC4052700
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-24949445-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02 (PubMed abstract, Europe PMC body check, dedup against the registries)
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261002-INTAKE-A-REGISTRY-01`
**Primary pathway:** gene dose (rejected reading)
**Transferability:** T3 for WWOX (the CNV holds only WWOX exon 9)
**clinical relevance:** BACKGROUND — recorded so the dose-gain reading is not made again
**Claim links:** none — the rejection is `DIS-022` (`CC-20261002-DOSE-GAIN-DISMISSAL-01`)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_A.md` · `CC-20261002-INTAKE-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID24949445.json`

## LIT-0424
**Short title:** Robertson 2025 NAR Genom Bioinform — FoundHaplo; WWOX p.Glu17Lys is a founder allele carried by 172 UK Biobank participants
**Authors:** Robertson E et al.
**Year:** 2025
**Source type:** primary research — statistical-genetics method with application
**Journal/source:** *NAR Genom Bioinform* 2025;7(2):lqaf033
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40191585 / DOI 10.1093/nargab/lqaf033 / PMC11970371
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-40191585-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02 (PubMed abstract, Europe PMC body check, dedup against the registries)
**Status:** processed
**Status note:** `partial_fulltext_read`; record created by `CC-20261002-INTAKE-A-REGISTRY-01`
**Primary pathway:** population genetics of WWOX alleles
**Transferability:** T2 for allele frequency; none for phenotype (no carrier phenotype reported)
**clinical relevance:** MODERATE — fixes the gene of `p.E17K` and makes its recurrence a founder effect; licenses nothing about carriers
**Claim links:** 032 (missense-carrier observation, under `DO_NOT_INFER`; not a supporting source)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_A.md` · `CC-20261002-INTAKE-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID40191585.json`

## LIT-0425
**Short title:** Bacchelli 2020 Sci Rep — PsychArray CNVs in 128 ASD families; one intronic-for-canonical WWOX deletion in a case, one exon 6–8 deletion in a control
**Authors:** Bacchelli E et al.
**Year:** 2020
**Source type:** primary research — family-based case-control CNV study
**Journal/source:** *Sci Rep* 2020;10:3198
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 32081867 / DOI 10.1038/s41598-020-59922-3 / PMC7035424
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-32081867-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02 (PubMed abstract, Europe PMC body check, dedup against the registries)
**Status:** processed
**Status note:** `partial_fulltext_read`; record created by `CC-20261002-INTAKE-A-REGISTRY-01`
**Primary pathway:** gene dose / heterozygous carriers
**Transferability:** T2 (human array data; no WWOX expression test)
**clinical relevance:** LOW-MODERATE — the one exon-level null-class heterozygote of the wave sits in a control without psychiatric history, neurologically unassessed
**Claim links:** 032 (carrier observation; not a supporting source)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_A.md` · `CC-20261002-INTAKE-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID32081867.json`

## LIT-0426
**Short title:** Yang 2023 Zoological Research — marmoset colony WGS; a 17-SNP intronic WWOX haplotype suggestively associated with handling-evoked seizures
**Authors:** Yang X et al.
**Year:** 2023
**Source type:** primary research — population-genetics WGS with pedigree association
**Journal/source:** *Zoological Research* 2023;44(5):837-847
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 37501399 / DOI 10.24272/j.issn.2095-8137.2022.514 / PMC10559097
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-37501399-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Primary pathway:** non-lineage association signals / intron 8
**Species:** common marmoset (*Callithrix jacchus*)
**Transferability:** T3 (non-coding primate association; no WWOX function measured)
**clinical relevance:** BACKGROUND — an earned near-null
**Claim links:** none — `CLAIM 037` explicitly untouched
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_B.md` · `CC-20261002-B-INTRON8-01` · `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID37501399.json`

## LIT-0427
**Short title:** Chou 2019 Cell Commun Signal — p53/TIAF1/WWOX triad; the brain-aggregation statement rests on one xenograft arm
**Authors:** Chou PY, Lin SR, Lee MH et al.
**Year:** 2019
**Source type:** primary research — cell and xenograft study
**Journal/source:** *Cell Commun Signal* 2019;17:76
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 31315632 / DOI 10.1186/s12964-019-0382-y / PMC6637503
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-31315632-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Primary pathway:** aggregation / TIAF1 lineage
**Species:** mouse xenograft (Wwox-intact) and human cell lines
**Transferability:** T3 (no neural WWOX-loss arm)
**clinical relevance:** BACKGROUND — an earned null for the brain; single-laboratory lineage
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_B.md` · `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID31315632.json`

## LIT-0428
**Short title:** Kałuzińska 2021 Cancers — PLEK2/RRM2/GCSH, a 'WWOX-dependent' glioma triad defined by a correlation, not a perturbation
**Authors:** Kałuzińska Ż et al.
**Year:** 2021
**Source type:** primary research — bioinformatic analysis of public bulk tumour expression data
**Journal/source:** *Cancers* 2021;13(12):2955
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 34204789 / DOI 10.3390/cancers13122955 / PMC8231639
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-34204789-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02
**Status:** processed
**Status note:** `partial_fulltext_read` — figure panels and supplement unread; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Primary pathway:** biomarkers (rejected)
**Species:** human bulk tumour expression data
**Transferability:** T3
**clinical relevance:** BACKGROUND — the title is not transferable to this model
**Claim links:** none — the rejection is `DIS-026`
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_C.md` · `CC-20261002-BIOMARKER-REJECTIONS-01` · `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Next action:** figure panels and supplement owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID34204789.json`

## LIT-0429
**Short title:** Zhang & Freudenreich 2007 Mol Cell — the FRA16D Flex1 AT-repeat stalls replication forks and breaks chromosomes in yeast
**Authors:** Zhang H, Freudenreich CH
**Year:** 2007
**Source type:** primary research — yeast genetics / replication
**Journal/source:** *Mol Cell* 2007;27(3):367-379
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 17679088 / DOI 10.1016/j.molcel.2007.06.012 / PMC2144737
**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-17679088-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02
**Status:** processed
**Status note:** `partial_fulltext_read` — figure panels and supplement unread; **OFF-AXIS for the assigned hypothesis**; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Primary pathway:** locus fragility / FRA16D architecture
**Species:** *Saccharomyces cerevisiae*
**Transferability:** T3 — somatic, mitotic, in yeast; no WWOX function measured
**clinical relevance:** BACKGROUND — a mechanistic precedent plus `LEAD-C1`; **not** a biomarker entry in either direction
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_C.md` § 4 (`LEAD-C1`) · `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Next action:** Finnis 2005 owed before anything is asserted about where Flex1 sits inside WWOX; figure panels and supplement owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID17679088.json`

## LIT-0430
**Short title:** Mondragon-Estrada 2025 Birth Defects Res — spina bifida GWAS; three imputed WWOX intron-8 SNPs, nominal and unreplicated
**Authors:** Mondragon-Estrada E et al.
**Year:** 2025
**Source type:** primary research — case-control GWAS
**Journal/source:** *Birth Defects Research* 2025;117(12):e70007
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41378749 / DOI 10.1002/bdr2.70007 / PMC12697008
**Date discovered:** before 2026-10-02 (queued as `FT-142`)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-41378749-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` § 6
**Primary pathway:** non-lineage association signals / intron 8
**Species:** human infants
**Transferability:** T3 — nominal, imputed, not technically replicated
**clinical relevance:** BACKGROUND — an earned null
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_B.md` · `CC-20261002-B-INTRON8-01` · `CC-20261002-B-NONLINEAGE-01` · `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID41378749.json`

## LIT-0431
**Short title:** Xia 2017 Transl Psychiatry — infant brain-volume GWAS; rs10514437 (WWOX intron) below the study's own threshold, unreplicated
**Authors:** Xia K et al.
**Year:** 2017
**Source type:** primary research — GWAS of neonatal MRI volumes
**Journal/source:** *Transl Psychiatry* 2017;7(8):e1188
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 28763065 / DOI 10.1038/tp.2017.159 / PMC5611727
**Date discovered:** before 2026-10-02 (queued as `FT-142`)
**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-28763065-01`)
**Discovery source:** Orchestrator selection record of intake wave 2026-10-02
**Status:** processed
**Status note:** `partial_fulltext_read` — supplement read by label only, appendix plot books unread; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` § 6
**Primary pathway:** white matter / non-lineage association signals
**Species:** human infants
**Transferability:** T3 — common variation, normal-range volumetry
**clinical relevance:** BACKGROUND — bounded context; the minor allele goes with *more* white matter
**Claim links:** none — `CLAIM 003` explicitly untouched
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261002_B.md` · `CC-20261002-B-INTRON8-01` · `CC-20261002-B-NONLINEAGE-01` · `CC-20261002-INTAKE-WAVE-ORPHANS-01`
**Next action:** supplement appendices owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID28763065.json`

## LIT-0432
**Short title:** Riva 2022 Front Pediatr — WOREE with p.Arg264* and an exon-6-only deletion missed by exome CNV calling
**Authors:** Riva A et al.; Zara F, Iacomino M
**Year:** 2022
**Source type:** primary research — single case report
**Journal/source:** *Front Pediatr* 2022;10:847549
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 35573960 / DOI 10.3389/fped.2022.847549 / PMC9100683
**Date discovered:** before 2026-07-05 (cited in the discovery ledger, DL-MOL-007, with no identity record)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-35573960-01`)
**Discovery source:** Orchestrator selection record of intake wave 2 2026-10-03
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261003-A-REGISTRY-01`
**Primary pathway:** clinical spectrum / WWOX-DEE · allele detection
**Transferability:** T1 for allele detection; T3 for genotypes with residual protein
**clinical relevance:** MODERATE
**Claim links:** 001 (through `CC-20261003-A-VIGABATRIN-01`)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003_A.md` · `CC-20261003-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID35573960.json`

## LIT-0433
**Short title:** Kim 2025 Sci Rep — WWOX intronic SNVs and self-reported sleep duration in two Korean cohorts, with a Drosophila Wwox hypomorph
**Authors:** Kim S, Kang SW, Kim SE, Kim HJ, Kim SA, Lee YW, Kim EY, Shin C, Lee HW
**Year:** 2025
**Source type:** primary research — genome-wide association study (n = 8,840) with an invertebrate functional arm
**Journal/source:** *Sci Rep* 2025;15(1):5552
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 39952983 / DOI 10.1038/s41598-024-81158-8 / PMC11828923
**Date discovered:** earlier (the PMID is addressed by `FT-016` and by `DL-MECH-013`); no record existed in this log or in the paper registry until now
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-39952983-02`, prior `FTR-20260811-39952983-01`)
**Discovery window:** intake wave 2, 2026-10-03, group C
**Discovery source:** `FT-016`
**Discovery query:** models and metabolic/ER-stress axis in WWOX loss — which endpoint could serve as a rescue readout
**Status:** processed
**Status note:** `partial_fulltext_read` — body, Tables 1-3, both figure images and the supplementary DOCX read; Supplementary Figures 1 and 2 (Manhattan and Q-Q plots) not inspected as images; 58-item reference list enumerated and screened mechanically, not read. 🔴 **Record created 2026-10-03 by this candidate:** the PMID was addressed by a queue entry and a discovery lead but by no registry record, which is the `ORPHAN_COMPLETE_READ` shape LINT blocks on.
**Primary pathway:** behavioural / network-state endpoints (non-seizure)
**Genotype/model tag:** human common intronic SNVs `rs16948804` and `rs4887991` at 16q23.1-q23.2 (one LD block, distal gene body); *Drosophila* `Wwox^f04545` insertion hypomorph, mRNA at about 8 per cent of control, homozygous, males only
**Transferability:** T3 — no WWOX-DEE allele, no patient, no measured WWOX expression in any human
**clinical relevance:** LOW — a non-seizure behavioural endpoint exists in the fly; the human arm licenses nothing
**Claim links:** none
**Working Model impact:** none — `DL-MECH-013` is qualified by `CC-20261003-C-SLEEP-SUGGESTIVE-01`, no block is redefined
**Report mentions:** `research/intake_wave_20261003_C.md` · `CC-20261003-C-SLEEP-SUGGESTIVE-01`
**Next action:** none owed; Supplementary Figures 1-2 remain unviewed and are not blocking
**Flags:** read — partial; human arm below conventional genome-wide significance **by the authors' own statement**
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-39952983-02`; manifest `deepdive_manifests/PMID39952983.json` (14 verbatim locators, PASS with artefact verification); dossier `research/fulltext_dossiers/PMID39952983.md`
**Registry record:** [[paper_registry_current#PAPER 135]]
**Note:** 🔴 The paper measures **no human WWOX expression**: the Results sentence *«The associations between WWOX expression and sleep parameters are presented in Table 2»* describes a genotype table, and the same conflation appears in the Abstract. ⚠️ The declared artefacts of this paper's deep-dive manifest were **absent from the corpus** at the start of this reading and the manifest was BLOCK; a Europe PMC re-fetch returned byte-identical files, which were restored under their declared names. Not medical advice.

## LIT-0434
**PMID:** 27551439
**Short title:** Chang 2015 Cell Death Discov — WWOX dysfunction and the sequential TRAPPC6AΔ/TIAF1/tau/Aβ aggregation cascade
**Status:** processed
**Route:** Europe PMC REST `fullTextXML` (HTTP 200 with a body), with figures, article PDF and supplements from the PMC open-access S3 mirror; read 2026-10-03 by ACTOR_ID `scientist` (Scientist B) under `context_policy: SOURCE_FIRST`.
**Outcome:** INGEST — `paper_registry_current#PAPER 136`.
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03). Provisional number; the integrator renumbers in event order.
**PAPER link:** [[paper_registry_current#PAPER 136]]

## LIT-0435
**PMID:** 25650666
**Short title:** Chang 2015 Oncotarget — TRAPPC6AΔ as an extracellular plaque-forming protein; pT181-tau in the 3-week-old Wwox-null brain
**Status:** processed
**Route:** Europe PMC REST `fullTextXML` (HTTP 200 with a body), with figures, article PDF and supplements from the PMC open-access S3 mirror; read 2026-10-03 by ACTOR_ID `scientist` (Scientist B) under `context_policy: SOURCE_FIRST`.
**Outcome:** INGEST — `paper_registry_current#PAPER 137`.
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03). Provisional number; the integrator renumbers in event order.
**PAPER link:** [[paper_registry_current#PAPER 137]]

## LIT-0436
**PMID:** 36498839
**Short title:** Lin 2022 IJMS — MPP+ and TPC6AΔ in a neuroblastoma line; Wwox heterozygote memory and cortical plaques at 10–11 months
**Status:** processed
**Route:** Europe PMC REST `fullTextXML` (HTTP 200 with a body), with figures, article PDF and supplements from the PMC open-access S3 mirror; read 2026-10-03 by ACTOR_ID `scientist` (Scientist B) under `context_policy: SOURCE_FIRST`.
**Outcome:** INGEST — `paper_registry_current#PAPER 138`.
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03). Provisional number; the integrator renumbers in event order.
**PAPER link:** [[paper_registry_current#PAPER 138]]

## LIT-0437
**PMID:** 29067327
**Short title:** Lee 2017 Alzheimers Dement (N Y) — Zfra4–10 peptide in 3×Tg-AD mice; not a WWOX model
**Status:** processed
**Route:** Europe PMC REST `fullTextXML` (HTTP 200 with a body), with figures, article PDF and supplements from the PMC open-access S3 mirror; read 2026-10-03 by ACTOR_ID `scientist` (Scientist B) under `context_policy: SOURCE_FIRST`.
**Outcome:** INGEST — `paper_registry_current#PAPER 139`.
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03). Provisional number; the integrator renumbers in event order.
**PAPER link:** [[paper_registry_current#PAPER 139]]

## LIT-0438
**PMID:** 19918364
**Short title:** Li 2009 PLoS One — WOX1 activation with CREB and NF-κB in rat DRG after sciatic transection; the pro-death direction
**Status:** processed
**Route:** Europe PMC REST `fullTextXML` (HTTP 200 with a body), with figures, article PDF and supplements from the PMC open-access S3 mirror; read 2026-10-03 by ACTOR_ID `scientist` (Scientist B) under `context_policy: SOURCE_FIRST`.
**Outcome:** INGEST — `paper_registry_current#PAPER 140`.
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03). Provisional number; the integrator renumbers in event order.
**PAPER link:** [[paper_registry_current#PAPER 140]]

## LIT-0439
**PMID:** 34359949
**Short title:** Hsu 2021 Cells — review of WWOX binding partners in neurodegeneration; provenance of the SDR–tau mechanism
**Status:** processed
**Route:** Europe PMC REST `fullTextXML` (HTTP 200 with a body), with figures, article PDF and supplements from the PMC open-access S3 mirror; read 2026-10-03 by ACTOR_ID `scientist` (Scientist B) under `context_policy: SOURCE_FIRST`.
**Outcome:** INGEST — `paper_registry_current#PAPER 141`.
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03). Provisional number; the integrator renumbers in event order.
**PAPER link:** [[paper_registry_current#PAPER 141]]

## LIT-0440
**PMID:** 21212468
**Short title:** Dudekula 2010 Aging — Zfra in mitochondrial apoptosis; a perspective that performs no experiment
**Status:** processed
**Route:** Europe PMC REST `fullTextXML` into the root `files/fulltext/`, with the single figure from the PMC open-access mirror; read 2026-10-03 by ACTOR_ID `scientist` (Scientist B) under `context_policy: SOURCE_FIRST`, intake wave 3.
**Outcome:** INGEST — `paper_registry_current#PAPER 142`.
**Record provenance:** 🔴 identity landing written by `BATCH_20261003_001` to clear the `ORPHAN_COMPLETE_READ` block this reading left on `main`; the scientific landing was completed on 2026-10-03 by `BATCH_20261003_002` from `CC-20261003W3-B-REGISTRY-01`, the candidate of the wave-3 reader who authored the reading (secondary throughout: every mitochondrial datum traces to one earlier primary of the same laboratory; `Transferability` T4; no claim link). No second record was created for this PMID.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-21212468-01`; manifest `deepdive_manifests/PMID21212468.json`
**PAPER link:** [[paper_registry_current#PAPER 142]]
**Note:** Not medical advice.

## LIT-0441
**Short title:** Nagarajan 2023 Epilepsia Open — genetic IESS in 124 children; four biallelic WWOX
**Authors:** Nagarajan B et al.; Sahu JK
**Year:** 2023
**Source type:** primary research — multicentre cross-sectional cohort
**Journal/source:** *Epilepsia Open* 2023;8:1383-1404
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 37583270 / DOI 10.1002/epi4.12811 / PMC10690684
**Date discovered:** before 2026-07-22 (cited in the discovery ledger, DL-MECH-060, with no identity record)
**Date processed:** 2026-10-03 (`FTR-20261003-37583270-01`)
**Discovery source:** Orchestrator selection record of intake wave 3 2026-10-03
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261003W3-A-REGISTRY-01`
**Primary pathway:** clinical spectrum / WWOX-DEE · drug response (spasms)
**Transferability:** T1 for predicted-null clinical course
**clinical relevance:** MODERATE
**Claim links:** 001 (through `CC-20261003W3-A-VIGABATRIN-01`)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w3_A.md` · `CC-20261003W3-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID37583270.json`

## LIT-0442
**Short title:** Serce Pehlevan 2026 J Paediatr Child Health — homozygous WWOX p.Leu239Arg, neonatal–infantile hypokinetic–rigid features
**Authors:** Serce Pehlevan O, Gider Yaman G, Gok A, Tekin Orgun L
**Year:** 2026
**Source type:** primary research — single case report
**Journal/source:** *J Paediatr Child Health* 2026;62(7):1273-1277
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42092735 / DOI 10.1111/jpc.70401 / PMC13378201
**Date discovered:** 2026-09-21 (full-text queue `FT-106`)
**Date processed:** 2026-10-03 (`FTR-20261003-42092735-01`)
**Discovery source:** next-node scouting 2026-09-21; selected again by intake wave 3 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (article read in full; cited prior report of the allele queued); record created by `CC-20261003W3-A-REGISTRY-01`
**Primary pathway:** clinical spectrum / movement phenotype
**Transferability:** T3 for any allele-level movement phenotype
**clinical relevance:** MODERATE
**Claim links:** 001 (through `CC-20261003W3-A-VIGABATRIN-01`)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w3_A.md` · `CC-20261003W3-A-REGISTRY-01` · `CC-20261003W3-A-L239R-01`
**Next action:** read Serin 2018 (PMID 30094525), the cited prior report of the allele, in full
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID42092735.json`

## LIT-0443
**Short title:** Lee 2010 TIAF1 aggregation and amyloid
**Authors:** Lee MH, et al.; Chang NS
**Year:** 2010
**Source type:** primary research - cell biology and postmortem human tissue
**Journal/source:** *Cell Death Dis* 2010;1:e110
**Identifier type:** PMID / DOI
**Identifier value:** PMID 21368882 / DOI 10.1038/cddis.2010.83
**Date discovered:** 2026-10-03
**Date processed:** 2026-10-03
**Discovery window:** intake wave 3 2026-10-03 (Scientist B, group B)
**Discovery source:** Orchestrator wave-3 selection record
**Discovery query:** WWOX organelle endpoints - mitochondria, lysosome/autophagy, ROS, aggregation
**Status:** processed
**Primary pathway:** protein aggregation / TIAF1-APP cascade
**Genotype/model tag:** no WWOX genotype
**Transferability:** T4
**clinical relevance:** LOW for WWOX directly
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w3_B.md`
**Next action:** none
**Flags:** created by `CC-20261003W3-B-REGISTRY-01`; provisional number
**Note:** Paired with [[paper_registry_current#PAPER 146]]. Read 2026-10-03 (`partial_fulltext_read`: figure panels from their legends only) (integrator amendment, `BATCH_20261003_002`); WWOX is not manipulated or measured in it - an earned null for the gene.

---

## LIT-0444
**Short title:** Tarta-Arsene 2017 Epileptic Disord — one WOREE patient, normal head circumference (= Piard 2019 P8)
**Authors:** Tarta-Arsene O, Barca D, Craiu D, Iliescu C
**Year:** 2017
**Source type:** primary research — clinical commentary, single case
**Journal/source:** *Epileptic Disord* 2017;19(3):357-361
**Identifier type:** PMID / DOI
**Identifier value:** PMID 28721938 / DOI 10.1684/epd.2017.0924
**Date discovered:** 2026-09-21 (harvest-to-registry gap, `FT-121`)
**Date processed:** 2026-10-03 (`FTR-20261003-28721938-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261003W4-A-REGISTRY-01`
**Primary pathway:** clinical spectrum / WWOX-DEE
**Transferability:** T1 for the null/null clinical course
**clinical relevance:** MODERATE
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_A.md` · `CC-20261003W4-A-REGISTRY-01` · `CC-20261003W4-A-PATIENT-OVERLAP-01`
**Next action:** none owed — count the patient once with Piard 2019 P8
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID28721938.json`

## LIT-0445
**Short title:** Dong 2022 J Lipid Res — exome sequencing in hypoalphalipoproteinemia; the clearest human heterozygote negative available on WWOX
**Authors:** Dong Z, Hoover A, Guo Y, Vitali C, Rao H, Cuchel M, et al.
**Year:** 2022
**Source type:** primary research — human whole-exome discovery study
**Journal/source:** *J Lipid Res* 2022;63(6):100209
**Identifier type:** PMID / PMCID / DOI
**Identifier value:** PMID 35460704 / PMCID PMC9126845 / DOI 10.1016/j.jlr.2022.100209
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (`FTR-20261003-35460704-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group B
**Status:** processed
**Status note:** `partial_fulltext_read`; record created by `CC-20261003W4-B-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P5 — metabolism / lipids
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** 045
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_B.md` · `CC-20261003W4-B-REGISTRY-01`
**Next action:** none owed — figure panels and supplements still owed for a complete read
**Evidence depth:** `partial_fulltext_read` — registry landing [[paper_registry_current#PAPER 156]]
**Note:** 🔴 `DO_NOT_CITE` as *«four WWOX carriers with a biochemical abnormality»*: the four occurrences are three distinct heterozygous missense alleles, one of them common and ClinVar-Benign, with no loss-of-function allele, no lipid value reported for any WWOX carrier, no significance in the burden test and no normal-HDL-C comparison cohort.

## LIT-0446
**Short title:** Abudiab 2025 bioRxiv — WWOX deficiency and myelin repair, Olig2-Cre conditional deletion (**PREPRINT**)
**Authors:** Abudiab et al.
**Year:** 2025
**Source type:** 🔴 **preprint (bioRxiv v1, 2025-11-24), NOT peer reviewed** — primary experimental
**Journal/source:** bioRxiv
**Identifier type:** Preprint DOI / bioRxiv id
**Identifier value:** DOI 10.1101/2025.11.22.689900 / bioRxiv PPR1124524 — **no PMID**; the receipt `FTR-20261003-PPR1124524-01` is keyed by DOI, as the ledger keys every record without a PMID
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (`FTR-20261003-PPR1124524-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group B
**Status:** processed
**Status note:** `partial_fulltext_read`; record created by `CC-20261003W4-B-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P4 — myelination / white matter
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none — a preprint founds no claim
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_B.md` · `CC-20261003W4-B-REGISTRY-01`
**Next action:** none owed — figure panels and supplements still owed for a complete read
**Evidence depth:** `partial_fulltext_read` — registry landing [[paper_registry_current#PAPER 157]]
**Note:** 🔴 A preprint never raises a claim's status. It is the experiment `CLAIM 003` names as its condition, in a source that cannot discharge it, and it comes from the same senior laboratory as [[paper_registry_current#PAPER 004]].

## LIT-0447
**Short title:** Lucas-Clarke 2025 bioRxiv — *Wwox* dose in a *Drosophila* amyloid model, in both directions (**PREPRINT**)
**Authors:** Lucas-Clarke et al.
**Year:** 2025
**Source type:** 🔴 **preprint (bioRxiv v1, 2025-05-07), NOT peer reviewed** — primary experimental
**Journal/source:** bioRxiv
**Identifier type:** Preprint DOI / bioRxiv id
**Identifier value:** DOI 10.1101/2025.05.01.651195 / bioRxiv PPR1015434 — **no PMID**; receipt keyed by DOI
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (`FTR-20261003-PPR1015434-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group B
**Status:** processed
**Status note:** `partial_fulltext_read`; record created by `CC-20261003W4-B-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P5 — metabolism (pyruvate / UPR)
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none — a preprint founds no claim
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_B.md` · `CC-20261003W4-B-REGISTRY-01`
**Next action:** none owed — figure panels and supplements still owed for a complete read
**Evidence depth:** `partial_fulltext_read` — registry landing [[paper_registry_current#PAPER 158]]
**Note:** The only source in the corpus that moves WWOX in **both** directions in the same model, with re-supply as a modest endogenous up-regulation (about 2× mRNA). The HIF1α-homologue reporter does **not** move — a direct negative on the WWOX/HIF1A axis in this system.

## LIT-0448
**Short title:** Fukai 2026 Mol Ther — a compact 410-bp mouse Gad1 promoter (cmGAD67) driving selective AAV expression in inhibitory neurons
**Authors:** Fukai Y, Konno A, Hosoi N, Miyakawa K, Kaneko R, Hirai H
**Year:** 2026
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther* 2026;34(9):5510-5526
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42349402 / DOI 10.1016/j.ymthe.2026.06.007 / PMCID PMC13555566
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-42349402-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group C
**Status:** processed
**Status note:** `partial_fulltext_read` — figure panels not inspected as images and no supplementary file fetched; record created by `CC-20261003w4-C-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P7 gene-therapy design
**Species:** mouse (C57BL/6J, VGAT-tdTomato), AAV-PHP.eB intravenous and intraparenchymal
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_C.md` · `CC-20261003w4-C-REGISTRY-01`
**Next action:** supplement and figure panels owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID42349402.json`; registry landing [[paper_registry_current#PAPER 159]]
**Note:** this source does not mention WWOX; it is carried as a transferable-method record, not as evidence. Not medical advice.

## LIT-0449
**Short title:** Song 2026 Mol Ther — EXG001-307, a dose-optimised intra-CSF AAV9 for SMA; the two-sided dose claim, with its upper limb unmeasured
**Authors:** Song C, Liu J, Wang Q, Zhu P, Xu J, Zhou Y, et al. (Exegenesis Bio)
**Year:** 2026
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther* 2026;34(7):3783-3804
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41992613 / DOI 10.1016/j.ymthe.2026.04.027 / PMCID PMC13330066
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-41992613-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group C
**Status:** processed
**Status note:** `partial_fulltext_read` — figure panels not inspected as images and no supplementary file fetched; record created by `CC-20261003w4-C-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P7 gene-therapy design
**Species:** SMNΔ7 mouse, Wistar Han rat (male only), juvenile cynomolgus macaque
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_C.md` · `CC-20261003w4-C-REGISTRY-01`
**Next action:** supplement and figure panels owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID41992613.json`; registry landing [[paper_registry_current#PAPER 160]]
**Note:** this source does not mention WWOX; it is carried as a transferable-method record, not as evidence. Not medical advice.

## LIT-0450
**Short title:** Boitnott 2026 Mol Ther — unregulated DDX3X overexpression after an intra-CSF injection kills newborn mice from the heart
**Authors:** Boitnott A, Hu Y, Wight-Carter M, Lopez Escobar C, Chen X, Gray SJ
**Year:** 2026
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther* 2026;34(9):5135-5144
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42458834 / DOI 10.1016/j.ymthe.2026.07.032 / PMCID PMC13555558
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-42458834-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group C
**Status:** processed
**Status note:** `partial_fulltext_read` — figure panels not inspected as images and no supplementary file fetched; record created by `CC-20261003w4-C-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P7 gene-therapy design
**Species:** wild-type C57BL/6J mouse, bilateral i.c.v. at P1 and intrathecal at P21
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_C.md` · `CC-20261003w4-C-REGISTRY-01`
**Next action:** supplement and figure panels owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID42458834.json`; registry landing [[paper_registry_current#PAPER 161]]
**Note:** this source does not mention WWOX; it is carried as a transferable-method record, not as evidence. Not medical advice.

## LIT-0451
**Short title:** Grubor 2025 Mol Ther Methods Clin Dev — immune events precede AAV DRG pathology in macaques, and dexamethasone plus tacrolimus reduce it across three cargos
**Authors:** Grubor B, Henry KL, Chan SJ, Sheehan M, Shah A, Pellerin A, et al. (Biogen)
**Year:** 2025
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(4):101643
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41404412 / DOI 10.1016/j.omtm.2025.101643 / PMCID PMC12704302
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-41404412-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group C
**Status:** processed
**Status note:** `partial_fulltext_read` — main figure panels read as images and Document S1 fetched in wave 9 (supplementary figures by caption, receipt `FTR-20261004-41404412-02`); record created by `CC-20261003w4-C-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P7 gene-therapy design / BLOCK-1 safety
**Species:** cynomolgus macaque, intra-cisterna magna and intrathecal lumbar
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_C.md` · `CC-20261003w4-C-REGISTRY-01`
**Next action:** supplement and figure panels owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID41404412.json`; registry landing [[paper_registry_current#PAPER 162]]
**Note:** this source does not mention WWOX; it is carried as a transferable-method record, not as evidence. Not medical advice.

## LIT-0452
**Short title:** Tukov 2022 Hum Gene Ther — intrathecal onasemnogene DRG and trigeminal findings, not mitigated by prednisolone or by rituximab plus everolimus
**Authors:** Tukov FF, Mansfield K, Milton M, Meseck E, Penraat K, Chand D, Hartmann A
**Year:** 2022
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Hum Gene Ther* 2022;33(13-14):740-756
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 35331006 / DOI 10.1089/hum.2021.255 / PMCID PMC9347375
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-35331006-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group C
**Status:** processed
**Status note:** `partial_fulltext_read` — figure panels not inspected as images and no supplementary file fetched; record created by `CC-20261003w4-C-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P7 gene-therapy design / BLOCK-1 safety
**Species:** cynomolgus macaque, intrathecal lumbar with iohexol contrast, plus an intravenous arm
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_C.md` · `CC-20261003w4-C-REGISTRY-01`
**Next action:** supplement and figure panels owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID35331006.json`; registry landing [[paper_registry_current#PAPER 163]]
**Note:** this source does not mention WWOX; it is carried as a transferable-method record, not as evidence. Not medical advice.

## LIT-0453
**Short title:** Johnson 2022 Mol Ther Methods Clin Dev — blood and CSF NfL against AAV9 DRG injury in 260 macaques, with per-animal operating characteristics
**Authors:** Johnson EW, Sutherland JJ, Meseck E, McElroy C, Chand DH, Tukov FF, Hudry E, Penraat K
**Year:** 2022
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther Methods Clin Dev* 2022;28:208-219
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 36700120 / DOI 10.1016/j.omtm.2022.12.012 / PMCID PMC9852542
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 4)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-36700120-01`)
**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03, group C
**Status:** processed
**Status note:** `partial_fulltext_read` — figure panels not inspected as images and no supplementary file fetched; record created by `CC-20261003w4-C-REGISTRY-01`, number assigned by `BATCH_20261003_003`
**Primary pathway:** P7 gene-therapy design / toxicity surveillance
**Species:** cynomolgus macaque, nine pooled studies, intrathecal and intravenous
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w4_C.md` · `CC-20261003w4-C-REGISTRY-01`
**Next action:** supplement and figure panels owed for a complete read
**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID36700120.json`; registry landing [[paper_registry_current#PAPER 164]]
**Note:** this source does not mention WWOX; it is carried as a transferable-method record, not as evidence. Not medical advice.
## LIT-0454
**Short title:** Greenberg 2026 first-in-human high-dose intrathecal AAV9, CLN7
**Authors:** Greenberg BM, et al.; Gray SJ, Kayani SN
**Year:** 2026
**Source type:** primary clinical study - phase 1, n = 4
**Identifier:** PMID 41314141 / DOI 10.1016/j.ebiom.2025.106044
**Status:** processed
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-41314141-01`
**Relevance:** transferable protocol only - CRIM-based immunosuppression and empty-capsid arithmetic; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 165]]
**Note:** not medical advice.
## LIT-0455
**Short title:** Quinlan 2025 oversized full-length SYNGAP1 AAV cassette
**Authors:** Quinlan MA, Guo R, et al.; Levi BP
**Year:** 2025
**Source type:** primary preclinical study
**Identifier:** PMID 40988338 / DOI 10.1016/j.ymthe.2025.09.040
**Status:** processed
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-40988338-01`
**Relevance:** transferable cargo-size arithmetic in a heterozygous, dose-sensitive model; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 166]]
**Note:** not medical advice.
## LIT-0456
**Short title:** Wiseman 2024 AP4B1 gene replacement IND package
**Authors:** Wiseman JP, Scarrott JM, et al.; Azzouz M
**Year:** 2024
**Source type:** primary preclinical study with GLP primate toxicology
**Identifier:** PMID 39358605 / DOI 10.1038/s44321-024-00148-5
**Status:** processed
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-39358605-01`
**Relevance:** nearest architectural analogue for a recessive loss-of-function CNS disease; immunogenicity tested only in wild-type animals; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 167]]
**Note:** not medical advice.
## LIT-0457
**Short title:** Bailey 2026 SLC13A5 gene replacement, metabolic and seizure endpoints
**Authors:** Bailey LE, Adams RM, et al.; Bailey RM
**Year:** 2026
**Source type:** primary preclinical study
**Identifier:** PMID 41712282 / DOI 10.1172/JCI197503
**Status:** processed
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-41712282-01`
**Relevance:** the two phenotypes do not share a dose; age costs an order of magnitude of delivery at matched dose and route; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 168]]
**Note:** not medical advice.
## LIT-0458
**Short title:** Duba-Kiss 2025 early postnatal expression and CNS immunity to a foreign protein
**Authors:** Duba-Kiss R, Hampson DR
**Year:** 2025
**Source type:** primary preclinical immunology study
**Identifier:** PMID 40809677 / DOI 10.1016/j.omtm.2025.101536
**Status:** processed
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-40809677-01`
**Relevance:** the window x immunity interaction, with three limits - humoral response at both ages, no transfer to a redose, antigen specificity; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 169]]
**Note:** not medical advice.
## LIT-0459
**Short title:** Balestrini 2026 Dravet therapy landscape review
**Authors:** Balestrini S, Scheffer IE
**Year:** 2026
**Source type:** narrative review - not peer-reviewed primary evidence for any datum it reports
**Identifier:** PMID 41712149 / DOI 10.1007/s40263-026-01276-x
**Status:** processed
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-41712149-01`
**Relevance:** positioning map; most of its advanced modalities require an intact allele and so cannot transfer to a biallelic null; the review does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 170]]
**Note:** not medical advice.

## LIT-0460
**Short title:** Burgess 2019 Ann Neurol — EIMFS landscape; one WWOX patient (= PAPER 018 patient 6)
**Authors:** Burgess R et al.; Scheffer IE
**Year:** 2019
**Source type:** primary research — consortium cohort
**Journal/source:** *Ann Neurol* 2019;86(6):821-831
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 31618474 / DOI 10.1002/ana.25619 / PMC7423163
**Date discovered:** 2026-09-21 (FT-116 cohort triage; FT-140)
**Date processed:** 2026-10-03 (`FTR-20261003-31618474-01`)
**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)
**Status:** processed
**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`
**Primary pathway:** clinical spectrum / EIMFS
**Transferability:** T1 (one patient, counted under PAPER 018)
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID31618474.json`

## LIT-0461
**Short title:** Yang 2022 Sci Rep — 36 EIMFS children; WWOX carrier with a second (ATP7A) diagnosis
**Authors:** Yang H et al.; Wu L
**Year:** 2022
**Source type:** primary research — two-centre cohort
**Journal/source:** *Sci Rep* 2022;12:10187
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 35715422 / DOI 10.1038/s41598-022-13974-9 / PMC9205988
**Date discovered:** before 2026-07-22 (DL-MECH-058 next-search agenda)
**Date processed:** 2026-10-03 (`FTR-20261003-35715422-01`)
**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)
**Status:** processed
**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`
**Primary pathway:** clinical spectrum / EIMFS
**Transferability:** none for WWOX-specific inference
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID35715422.json`

## LIT-0462
**Short title:** Spagnoli 2021 Int J Mol Sci — neonatal-onset genetic epilepsy with movement disorder; WWOX section re-describes Piard 2019
**Authors:** Spagnoli C et al.; Pisani F
**Year:** 2021
**Source type:** secondary — systematic review
**Journal/source:** *Int J Mol Sci* 2021;22(8):4202
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 33919646 / DOI 10.3390/ijms22084202 / PMC8072943
**Date discovered:** 2026-10-03 (wave-5 selection; no earlier record)
**Date processed:** 2026-10-03 (`FTR-20261003-33919646-01`)
**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)
**Status:** processed
**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`
**Primary pathway:** movement phenotype (secondary)
**Transferability:** none beyond its source
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID33919646.json`

## LIT-0463
**Short title:** Hengel 2020 Eur J Hum Genet — consanguineous-population exome cohort; WWOX row = SCAR12 G372R family of PAPER 042
**Authors:** Hengel H et al.; Schöls L
**Year:** 2020
**Source type:** primary research — family exome cohort
**Journal/source:** *Eur J Hum Genet* 2020;28(8):1034-1043
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 32214227 / DOI 10.1038/s41431-020-0609-9 / PMC7382450
**Date discovered:** 2026-09-21 (FT-116 cohort triage; FT-140)
**Date processed:** 2026-10-03 (`FTR-20261003-32214227-01`)
**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)
**Status:** processed
**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`
**Primary pathway:** clinical spectrum / SCAR12 (pointer)
**Transferability:** none beyond its source
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID32214227.json`

## LIT-0464
**Short title:** Mori 2019 Brain Dev — heterozygous 16q22.2-q23.1 deletion through WWOX, West syndrome, not attributed to WWOX
**Authors:** Mori T et al.; Kagami S
**Year:** 2019
**Source type:** primary research — case report
**Journal/source:** *Brain Dev* 2019;41(10):888-892
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31353122 / DOI 10.1016/j.braindev.2019.07.005
**Date discovered:** 2026-10-03 (wave-5 selection; no earlier record)
**Date processed:** 2026-10-03 (`FTR-20261003-31353122-01`)
**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)
**Status:** processed
**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`
**Primary pathway:** copy-number carriers / negative control
**Transferability:** none for WWOX haploinsufficiency
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (**partial full text**) (figures not inspected) — manifest `deepdive_manifests/PMID31353122.json`
## LIT-0465
**Short title:** Wang 2026 Mol Ther — first-in-human single-patient intra-cisterna-magna AAV9 in severe MPS I, followed beyond five years
**Authors:** Wang RY, et al.
**Year:** 2026
**Source type:** primary research — single-patient open-label clinical report
**Journal/source:** *Molecular Therapy* 2026
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41966056 / DOI 10.1016/j.ymthe.2026.04.016 / PMCID PMC13239742
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 5, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-41966056-01`)
**Discovery source:** Orchestrator wave-5 selection record
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — figure panels not rendered and supplementary documents not fetched; record created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C), number assigned by `BATCH_20261003_004`
**Primary pathway:** P7 — CSF-route AAV9 human safety and tolerability
**Species:** human, single patient, dosed in the second year of life
**Transferability:** T4 — route, immunosuppression and monitoring transfer; cargo, pharmacodynamic readout and disease do not
**clinical relevance:** MODERATE as the only human intracisternal AAV9 datum in the second year of life
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w5_C.md` · `CC-20261003W5-C-REGISTRY-01`
**Next action:** figure panels and the supplementary protocol owed for a complete read
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41966056.json`; registry landing [[paper_registry_current#PAPER 177]]
**Note:** this source does not mention WWOX — an earned null for the gene. ⚠️ the dose literal is printed with an impossible negative exponent in both abstract and body and must never be carried as printed; ⚠️ nerve conduction was not performed, so the dorsal-root-ganglion statement rests on clinical observation only. Not medical advice.
## LIT-0466
**Short title:** Vono 2025 Mol Ther Methods Clin Dev — pre-existing anti-AAV9 antibody does not bound CNS biodistribution after intrathecal dosing in macaques
**Authors:** Vono M, et al.
**Year:** 2025
**Source type:** primary research — NHP toxicology and biodistribution
**Journal/source:** *Mol Ther Methods Clin Dev* 2025
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41210171 / DOI 10.1016/j.omtm.2025.101602
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 5, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-41210171-01`)
**Discovery source:** Orchestrator wave-5 selection record
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — figure captions only, supplement fetched; record created by `CC-20261003W5-C-REGISTRY-01`, number assigned by `BATCH_20261003_004`
**Primary pathway:** P7 — CSF-route AAV9 immunity and biodistribution
**Species:** cynomolgus macaque, intrathecal, single dose level
**Transferability:** T4
**clinical relevance:** MODERATE for CSF-route eligibility criteria
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w5_C.md` · `CC-20261003W5-C-REGISTRY-01`
**Next action:** none
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41210171.json`; registry landing [[paper_registry_current#PAPER 178]]
**Note:** this source does not mention WWOX — an earned null for the gene. ⚠️ one dose level only; ⚠️ dorsal-root-ganglion pathology is reported in prose with no incidence or severity count for that tissue (the tabulated incidence in the article is for brain). Not medical advice.
## LIT-0467
**Short title:** Aihara 2025 Mol Ther Methods Clin Dev — the transcriptional response to intrathecal AAV9 in macaques, and what the toxicity requires
**Authors:** Aihara Y, et al.
**Year:** 2025
**Source type:** primary research — NHP transcriptomics
**Journal/source:** *Mol Ther Methods Clin Dev* 2025
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41257285 / DOI 10.1016/j.omtm.2025.101617
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 5, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-41257285-01`)
**Discovery source:** Orchestrator wave-5 selection record
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — figure captions only, supplement not fetched; record created by `CC-20261003W5-C-REGISTRY-01`, number assigned by `BATCH_20261003_004`
**Primary pathway:** P7 — mechanism of CSF-route AAV9 organ toxicity
**Species:** cynomolgus macaque, intrathecal
**Transferability:** T3
**clinical relevance:** HIGH as the mechanistic layer under any CSF-route restoration programme
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w5_C.md` · `CC-20261003W5-C-REGISTRY-01`
**Next action:** none
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41257285.json`; registry landing [[paper_registry_current#PAPER 179]]
**Note:** this source does not mention WWOX — an earned null for the gene. Liver and dorsal-root-ganglion toxicity were detected only after full vector particles, not after empty capsids or a promoterless genome; ⚠️ the in-life toxicity data are cited to a prior report. Not medical advice.
## LIT-0468
**Short title:** Stavrou 2026 Mol Ther Nucleic Acids — intrathecal AAV9 RNA interference in mice and macaques, with dorsal-root-ganglion histopathology by arm
**Authors:** Stavrou M, et al.
**Year:** 2026
**Source type:** primary research — murine and NHP safety and biodistribution
**Journal/source:** *Mol Ther Nucleic Acids* 2026
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41948127 / DOI 10.1016/j.omtn.2026.102881
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 5, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-41948127-01`)
**Discovery source:** Orchestrator wave-5 selection record
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — Figure 5 read at panel level, supplement not fetched; record created by `CC-20261003W5-C-REGISTRY-01`, number assigned by `BATCH_20261003_004`
**Primary pathway:** P7 — CSF-route AAV9 peripheral-nervous-system biodistribution and dorsal-root-ganglion safety
**Species:** mouse and cynomolgus macaque, intrathecal
**Transferability:** T4 — the cargo is a U6-driven small RNA and does not stand proxy for a promoter-driven protein transgene
**clinical relevance:** HIGH for dorsal-root-ganglion attribution and for monitoring design
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w5_C.md` · `CC-20261003W5-C-REGISTRY-01`
**Next action:** none
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41948127.json`; registry landing [[paper_registry_current#PAPER 180]]
**Note:** this source does not mention WWOX — an earned null for the gene. Dorsal-root-ganglion lesions were present in two of four concurrent saline-dosed controls. ⚠️ three internal quantity contradictions (dose 6E13 in text against 5E13 in the figure row labels; infusion volume 4 mL in Results against 3 mL in Methods; scale bars in millimetres in the caption against micrometres in the panel) — see `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01`. Not medical advice.
## LIT-0469
**Short title:** Engelhard 2026 Front Drug Deliv — cerebrospinal-fluid circulation variability and what it does to a delivered intraventricular dose
**Authors:** Engelhard HH, et al.
**Year:** 2026
**Source type:** narrative review — not primary evidence for any datum it reports
**Journal/source:** *Front Drug Deliv* 2026
**Identifier type:** PMID / DOI
**Identifier value:** PMID 42205472 / DOI 10.3389/fddev.2026.1735474
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 5, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-42205472-01`)
**Discovery source:** Orchestrator wave-5 selection record
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — Tables 4 and 7 read cell-wise from the JATS table structure, figure panels not rendered, supplements not fetched; record created by `CC-20261003W5-C-REGISTRY-01`, number assigned by `BATCH_20261003_004`
**Primary pathway:** P7 — cerebrospinal-fluid physiology and the determinants of delivered dose
**Species:** cross-species compilation (mouse, rat, macaque, adult human)
**Transferability:** T4 — method for dose-setting only
**clinical relevance:** MODERATE for dose-setting method
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w5_C.md` · `CC-20261003W5-C-REGISTRY-01`
**Next action:** Supplementary Material 2 (the paediatric section) owed before any age-specific scaling is attempted
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42205472.json`; registry landing [[paper_registry_current#PAPER 181]]
**Note:** this source does not mention WWOX — an earned null for the gene. ⚠️ its scope is **intraventricular**, not intrathecal; ⚠️ its cross-species table carries a single, undated, adult human row, so it cannot convert an adult or primate dose into an infant one. Not medical advice.
## LIT-0470
**Short title:** Kagiava 2026 eBioMedicine — the human record of intrathecal gene therapy for neurological disorders, and its immunosuppression practice
**Authors:** Kagiava A, et al.
**Year:** 2026
**Source type:** narrative review — not primary evidence for any datum it reports
**Journal/source:** *eBioMedicine* 2026
**Identifier type:** PMID / DOI
**Identifier value:** PMID 42134074 / DOI 10.1016/j.ebiom.2026.106294
**Date discovered:** 2026-10-03 (Orchestrator selection record of intake wave 5, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-42134074-01`)
**Discovery source:** Orchestrator wave-5 selection record
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — Table 1 read cell-wise; record created by `CC-20261003W5-C-REGISTRY-01`, number assigned by `BATCH_20261003_004`
**Primary pathway:** P7 — human CSF-route gene therapy and immunosuppression practice
**Species:** human (review of clinical programmes)
**Transferability:** T3
**clinical relevance:** HIGH as the human layer of the CSF-route evidence base
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w5_C.md` · `CC-20261003W5-C-REGISTRY-01`
**Next action:** none
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42134074.json`; registry landing [[paper_registry_current#PAPER 182]]
**Note:** this source does not mention WWOX — an earned null for the gene. It carries the regulatory history of the dorsal-root-ganglion question, including a hold on enrolment in a paediatric intrathecal programme. ⚠️ one paragraph's four hepatotoxicity percentages are unusable as printed: the comparison names one route twice and gives a sham-control rate above the treated rate. Not medical advice.
## LIT-0471
**Short title:** Aeran 2025 Mol Ther — neuron-targeted STXBP1 gene replacement, mouse and primate
**Authors:** Aeran R, et al.
**Year:** 2025
**Source type:** primary research — preclinical gene replacement
**Journal/source:** *Mol Ther* 2025
**Identifier type:** PMID / DOI
**Identifier value:** PMID 40349107 / DOI 10.1016/j.ymthe.2025.05.011
**Date discovered:** 2026-10-03 (Orchestrator wave-3 selection, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-40349107-01`)
**Discovery source:** Orchestrator wave-3 selection, group C
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — figure panels not rendered, supplement not fetched; record authored by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01`
**Primary pathway:** P7 — delivery and vector engineering
**Species:** mouse and nonhuman primate
**Transferability:** T4
**clinical relevance:** BACKGROUND
**Directness to the reference genotype:** indirect — different gene
**Over-inference risk:** HIGH — the single named risk is importing a dose, a window or a tolerability statement from another gene without its transfer limit
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w3_C.md` · `CC-20261003W3-C-REGISTRY-01` · `RL-C-20261003w3`
**Next action:** figure panels and supplement owed for a complete read
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID40349107.json`; registry landing [[paper_registry_current#CORPUS P401]]
**Note:** this source does not mention WWOX; carried as a transferable-method record, not as evidence. Not medical advice.
## LIT-0472
**Short title:** Chen 2025 J Clin Invest — neonatal versus juvenile gene therapy in an SCN1B Dravet model
**Authors:** Chen C, et al.
**Year:** 2025
**Source type:** primary research — preclinical gene replacement
**Journal/source:** *J Clin Invest* 2025
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39847501 / DOI 10.1172/JCI182584
**Date discovered:** 2026-10-03 (Orchestrator wave-3 selection, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-39847501-01`)
**Discovery source:** Orchestrator wave-3 selection, group C
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — figure panels not rendered, supplement not fetched; record authored by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01`
**Primary pathway:** P7 — delivery and timing
**Species:** mouse
**Transferability:** T4
**clinical relevance:** BACKGROUND
**Directness to the reference genotype:** indirect — different gene
**Over-inference risk:** HIGH — it looks like a window result and resolves to delivery; see `DIS-033`
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w3_C.md` · `CC-20261003W3-C-REGISTRY-01` · `DIS-033`
**Next action:** none
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID39847501.json`; registry landing [[paper_registry_current#CORPUS P402]]
**Note:** this source does not mention WWOX; carried as a transferable-method record, not as evidence. Not medical advice.
## LIT-0473
**Short title:** Wagner 2025 Nat Med — antisense oligonucleotide in a preterm infant with SCN2A developmental and epileptic encephalopathy
**Authors:** Wagner M, et al.
**Year:** 2025
**Source type:** primary research — single-patient clinical report
**Journal/source:** *Nat Med* 2025
**Identifier type:** PMID / DOI
**Identifier value:** PMID 40263630 / DOI 10.1038/s41591-025-03656-0
**Date discovered:** 2026-10-03 (Orchestrator wave-3 selection, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-40263630-01`)
**Discovery source:** Orchestrator wave-3 selection, group C
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — figure panels not rendered, supplement not fetched; record authored by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01`
**Primary pathway:** P7 — route, schedule and n-of-1 architecture
**Species:** human, n = 1
**Transferability:** T4
**clinical relevance:** BACKGROUND
**Directness to the reference genotype:** indirect — different gene, different modality
**Over-inference risk:** HIGH — ⚠️ its cumulative-exposure statements disagree across sections, so no cumulative dose may be carried without naming the statement it came from
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w3_C.md` · `CC-20261003W3-C-REGISTRY-01`
**Next action:** none
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID40263630.json`; registry landing [[paper_registry_current#CORPUS P403]]
**Note:** this source does not mention WWOX; carried as a transferable-architecture record, not as evidence. Not medical advice.
## LIT-0474
**Short title:** Diaz 2026 Mol Ther Nucleic Acids — AAV9 natural-antisense-transcript targeting in Dravet syndrome
**Authors:** Diaz J, et al.
**Year:** 2026
**Source type:** primary research — preclinical transcript upregulation
**Journal/source:** *Mol Ther Nucleic Acids* 2026
**Identifier type:** PMID / DOI
**Identifier value:** PMID 42181696 / DOI 10.1016/j.omtn.2026.102942
**Date discovered:** 2026-10-03 (Orchestrator wave-3 selection, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-42181696-01`)
**Discovery source:** Orchestrator wave-3 selection, group C
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — figure panels not rendered, supplement not fetched; record authored by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01`
**Primary pathway:** P7 — transcript upregulation
**Species:** mouse
**Transferability:** T4
**clinical relevance:** BACKGROUND
**Directness to the reference genotype:** indirect — different gene
**Over-inference risk:** HIGH — the rescue-without-measurable-protein result is a statement about the assay as much as about the biology
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w3_C.md` · `CC-20261003W3-C-REGISTRY-01` · `RL-C-20261003w3` · `DIS-033`
**Next action:** none
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42181696.json`; registry landing [[paper_registry_current#CORPUS P404]]
**Note:** this source does not mention WWOX; carried as a transferable-method record, not as evidence. Not medical advice.
## LIT-0475
**Short title:** Saravanan 2026 Ann Clin Transl Neurol — endogenous HiBiT knock-in for NaV1.1 protein quantity
**Authors:** Saravanan S, et al.
**Year:** 2026
**Source type:** primary research — assay development in human induced pluripotent stem cells
**Journal/source:** *Ann Clin Transl Neurol* 2026
**Identifier type:** PMID / DOI
**Identifier value:** PMID 42521212 / DOI 10.1002/acn3.70500
**Date discovered:** 2026-10-03 (Orchestrator wave-3 selection, group C)
**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-42521212-01`)
**Discovery source:** Orchestrator wave-3 selection, group C
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**) — figure captions only, supplement captions only; record authored by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01`
**Primary pathway:** P-BIO — pharmacodynamic assay
**Species:** human induced pluripotent stem cells
**Transferability:** T4
**clinical relevance:** BACKGROUND
**Directness to the reference genotype:** indirect — different gene; nothing WWOX-specific exists
**Over-inference risk:** HIGH — abundance is not activity, and the clone-specific copy-number caveat must be designed out rather than inherited
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `research/intake_wave_20261003w3_C.md` · `CC-20261003W3-C-REGISTRY-01` · `RC-C-20261003w3`
**Next action:** none
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42521212.json`; registry landing [[paper_registry_current#CORPUS P405]]
**Note:** this source does not mention WWOX; carried as a transferable-method record, not as evidence. Not medical advice.

## LIT-0476
**Short title:** Hudry 2023 Mol Ther — liver injury in cynomolgus monkeys after intravenous and intrathecal scAAV9; the hepatic arm of the CSF-route dose question
**Authors:** Hudry E, Aihara F, Meseck E, Mansfield K, McElroy C, Chand D, Tukov FF, Penraat K
**Year:** 2023
**Source type:** primary research — nonclinical safety/toxicology (NHP, mouse-free)
**Journal/source:** *Mol Ther* 2023;31(10):2999-3014
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 37515322 / PMCID PMC10556189 / DOI 10.1016/j.ymthe.2023.07.020
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group C)
**Date processed:** 2026-10-03 (`FTR-20261003-37515322-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); **off-WWOX by measurement** — the string WWOX occurs zero times in every artefact; held as a transferable AAV-safety source. Record created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`.
**Primary pathway:** gene-therapy safety (P7) · hepatic endpoint · route
**Transferability:** T3 — transferable as a design fact about route, cassette and immunosuppression; no dose transfers to a WWOX cassette
**clinical relevance:** MODERATE strategic / NOT clinically validated
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_C.md` · `CC-20261003W6-C-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID37515322.json`
**Registry twin:** [[paper_registry_current#PAPER 183]]

## LIT-0477
**Short title:** Amaral 2026 Mol Ther Adv — intra-CNS AAV9 delivery: species and route differences in safety and transgene expression
**Authors:** Amaral AC, Grubor B, Gianni D, Koetzner L, Abraham N, Bourque S, Brown D, Chen Y, Chicoine KE, Clarner P, De Giovanni PJ, Hamann S, Kirkland M, Mendes OR, Michael M, Nadella MVP, Nambiar K, Sebalusky J, Zeng W, Xu S, Trapa P, Plowey ED, Tien E, Fikes J, Walsh DM, Hirst WD, Suh J, Glajch KE
**Year:** 2026
**Source type:** primary research — nonclinical biodistribution and safety (mouse + NHP)
**Journal/source:** *Mol Ther Adv* 2026;34(3):201779
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42422766 / PMCID PMC13343144 / DOI 10.1016/j.omta.2026.201779
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group C)
**Date processed:** 2026-10-03 (`FTR-20261003-42422766-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); **off-WWOX by measurement** — the string WWOX occurs zero times in every artefact; held as a transferable AAV-safety source. Record created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`.
**Primary pathway:** gene-therapy safety (P7) · route · CNS biodistribution
**Transferability:** T3 — the route-versus-harm contrast transfers as a design fact; the magnitudes are capsid-, cargo- and species-specific
**clinical relevance:** MODERATE strategic / NOT clinically validated
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_C.md` · `CC-20261003W6-C-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID42422766.json`
**Registry twin:** [[paper_registry_current#PAPER 184]]

## LIT-0478
**Short title:** Okai 2025 Mol Ther Methods Clin Dev — AAV1/AAV5/AAV9/AAVDJ biodistribution after intra-cisterna magna delivery in NHP
**Authors:** Okai T, Sato S, Yasuno H, Nakayama M, Yamamoto S, Sjöqvist S, Otake K, Nakashima M, Deshpande M, Galbreath E, Oak JH, Miyamoto S, Proetzel G
**Year:** 2025
**Source type:** primary research — nonclinical biodistribution and tolerability (NHP)
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(4):101593
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41078870 / PMCID PMC12509745 / DOI 10.1016/j.omtm.2025.101593
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group C)
**Date processed:** 2026-10-03 (`FTR-20261003-41078870-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); **off-WWOX by measurement** — the string WWOX occurs zero times in every artefact; held as a transferable AAV-safety source. Record created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`.
**Primary pathway:** gene-therapy safety (P7) · capsid choice · CNS biodistribution
**Transferability:** T3 — 'capsid is not a lever on this route' transfers as a design fact; the deep-brain ceiling is route-specific
**clinical relevance:** MODERATE strategic / NOT clinically validated
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_C.md` · `CC-20261003W6-C-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID41078870.json`
**Registry twin:** [[paper_registry_current#PAPER 185]]

## LIT-0479
**Short title:** DuBreuil 2025 Mol Ther Adv — a secretable frataxin: lowering vector burden instead of tolerating it
**Authors:** DuBreuil DM, Fleming M, Parikh Y, Woo M, Bu J, Ayloo S, Langohr IM, Bangari DS, Mueller C, Ramachandran S
**Year:** 2025
**Source type:** primary research — vector and cargo engineering with NHP and mouse arms
**Journal/source:** *Mol Ther Adv* 2025;34(1):201661
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42157962 / PMCID PMC13182795 / DOI 10.1016/j.omta.2025.201661
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group C)
**Date processed:** 2026-10-03 (`FTR-20261003-42157962-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); **off-WWOX by measurement** — the string WWOX occurs zero times in every artefact; held as a transferable AAV-safety source. Record created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`.
**Primary pathway:** gene-therapy design (P7) · cargo engineering · dose window
**Transferability:** T2 for the **units** (fold-of-endogenous), T3 for the numbers; WWOX protein is intracellular and the secretion strategy does not transfer to it without evidence
**clinical relevance:** HIGH strategic / NOT clinically validated
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_C.md` · `CC-20261003W6-C-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID42157962.json`
**Registry twin:** [[paper_registry_current#PAPER 186]]

## LIT-0480
**Short title:** Chen 2023 J Clin Invest — intrathecal AAV9/AP4M1 for SPG50: the recessive-null IND-directed architecture closest to a WWOX programme
**Authors:** Chen X, Dong T, Hu Y, De Pace R, Mattera R, Eberhardt K, Ziegler M, Pirovolakis T, Sahin M, Bonifacino JS, Ebrahimi-Fakhari D, Gray SJ
**Year:** 2023
**Source type:** primary research — complete IND-enabling package (patient fibroblasts, KO mouse, rat and NHP toxicology)
**Journal/source:** *J Clin Invest* 2023;133(10):e164575
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 36951961 / PMCID PMC10178841 / DOI 10.1172/JCI164575
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group C)
**Date processed:** 2026-10-03 (`FTR-20261003-36951961-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); **off-WWOX by measurement** — the string WWOX occurs zero times in every artefact; held as a transferable AAV-safety source. Record created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`.
**Primary pathway:** gene-therapy design and safety (P7) · dose · immune interface
**Transferability:** T2 for the **architecture** (recessive null, intrathecal, age-dependent benefit), T3 for every dose figure
**clinical relevance:** HIGH strategic / NOT clinically validated
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_C.md` · `CC-20261003W6-C-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID36951961.json`
**Registry twin:** [[paper_registry_current#PAPER 187]]

## LIT-0481
**Short title:** Ma 2025 Mol Med — AAV9-coSMN1 for spinal muscular atrophy: the group's only DRG-negative primate study, and its weakest reporting
**Authors:** Ma W, Wu Z, Zhao T, Xia Y, Qin J, Tian X, Li X, He J, Zhang Y, Zhang L, Li L, Dong Z, Feng Z, Dong X, Sheng W, Wu X
**Year:** 2025
**Source type:** primary research — nonclinical efficacy and safety (mouse + NHP)
**Journal/source:** *Mol Med* 2025;31(1):158
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40301740 / PMCID PMC12042585 / DOI 10.1186/s10020-025-01207-4
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group C)
**Date processed:** 2026-10-03 (`FTR-20261003-40301740-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); **off-WWOX by measurement** — the string WWOX occurs zero times in every artefact; held as a transferable AAV-safety source. Record created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`.
**Primary pathway:** gene-therapy safety (P7) · dose saturation
**Transferability:** T3 — a counterexample whose reporting depth does not support a strong negative
**clinical relevance:** LOW-MODERATE strategic / NOT clinically validated
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_C.md` · `CC-20261003W6-C-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID40301740.json`
**Registry twin:** [[paper_registry_current#PAPER 188]]

## LIT-0482
**Short title:** Cerulli Irelli 2025 Epilepsia — purified cannabidiol in 266 monogenic epilepsies; one Table 2 row of three WWOX patients (response at last follow-up)
**Authors:** Cerulli Irelli E, Mazzeo A, Caraballo RH, et al.; Orsini A, Coppola A
**Year:** 2025
**Source type:** primary research — retrospective multicentre real-world cohort
**Journal/source:** *Epilepsia* 2025;66:2253-2267
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40126049 / DOI 10.1111/epi.18378 / PMC12291005
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)
**Date processed:** 2026-10-03 (`FTR-20261003-40126049-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); record created by `CC-20261003W6-B-REGISTRY-01`
**Primary pathway:** drug response (cannabidiol) · denominator
**Transferability:** T3 — n = 3, adjunctive, uncontrolled; no allele class
**clinical relevance:** LOW-MODERATE — the only genotype-stratified CBD response row naming WWOX
**Claim links:** none (see `CC-20261003W6-B-CBDRESPONSE-01`, DL-MECH-030)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01` · `CC-20261003W6-B-CBDRESPONSE-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID40126049.json`

## LIT-0483
**Short title:** Innes 2025 Dev Med Child Neurol — IESS aetiopathogenesis and ACTH/corticosteroid mechanisms (scoping review); WWOX in two re-tabulated cohort rows
**Authors:** Innes EA, Han VX, Patel S, Farrar MA, Gill D, Mohammad SS, Dale RC
**Year:** 2025
**Source type:** secondary — scoping review
**Journal/source:** *Dev Med Child Neurol* 2025;67:1004-1025
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40019827 / DOI 10.1111/dmcn.16273 / PMC12237231
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)
**Date processed:** 2026-10-03 (`FTR-20261003-40019827-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); record created by `CC-20261003W6-B-REGISTRY-01`
**Primary pathway:** denominator (IESS genetics) · ACTH mechanism
**Transferability:** none for WWOX — re-tabulation only
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01`
**Next action:** read Ko 2018 (PMID 29455050), the primary of the single-patient WWOX row, before counting that patient
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID40019827.json`

## LIT-0484
**Short title:** Zhu 2025 Front Pediatr — etiology of 361 IESS patients; one WWOX patient, no allele or response
**Authors:** Zhu L, Xia Y, Ding H, Zhang T, Li J, Li B
**Year:** 2025
**Source type:** primary research — retrospective two-hospital series
**Journal/source:** *Front Pediatr* 2025;12:1522079
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 39850204 / DOI 10.3389/fped.2024.1522079 / PMC11754263
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)
**Date processed:** 2026-10-03 (`FTR-20261003-39850204-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); record created by `CC-20261003W6-B-REGISTRY-01`
**Primary pathway:** denominator (IESS)
**Transferability:** denominator only
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID39850204.json`

## LIT-0485
**Short title:** Snyder 2024 Genes — IESS genetics and precision-medicine opportunities (narrative review); WWOX one uncited autosomal-recessive list entry
**Authors:** Snyder HE, Jain P, RamachandranNair R, Jones KC, Whitney R
**Year:** 2024
**Source type:** secondary — narrative review
**Journal/source:** *Genes (Basel)* 2024;15(3):266
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 38540325 / DOI 10.3390/genes15030266 / PMC10970414
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)
**Date processed:** 2026-10-03 (`FTR-20261003-38540325-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); record created by `CC-20261003W6-B-REGISTRY-01`
**Primary pathway:** denominator (IESS genetics) · precision medicine
**Transferability:** none
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID38540325.json`

## LIT-0486
**Short title:** Yuan 2025 Acta Epileptol — genetic DEE with movement disorders; WWOX top-ten gene, pooled 18-patient row (dystonia 15/18)
**Authors:** Yuan M, Wang X, Yang Z, Luo H, Gan J, Luo R
**Year:** 2025
**Source type:** secondary — narrative review with bibliometric step
**Journal/source:** *Acta Epileptol* 2025;7(1):9
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40217411 / DOI 10.1186/s42494-024-00194-z / PMC11960234
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)
**Date processed:** 2026-10-03 (`FTR-20261003-40217411-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); record created by `CC-20261003W6-B-REGISTRY-01`
**Primary pathway:** movement phenotype
**Transferability:** none for counting — primaries not named
**clinical relevance:** LOW
**Claim links:** none (see `CC-20261003W6-B-MOVEMENT-01`)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01` · `CC-20261003W6-B-MOVEMENT-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID40217411.json`

## LIT-0487
**Short title:** Mohammad 2026 Mov Disord Clin Pract — movement disorders in DEE (non-systematic review); four WWOX rows, all citing one cohort
**Authors:** Mohammad S, Ebrahimi-Fakhari D, Morales-Briceno H
**Year:** 2026
**Source type:** secondary — non-systematic structured review
**Journal/source:** *Mov Disord Clin Pract* 2026
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42068099 / DOI 10.1002/mdc3.70641 / PMC13339248
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)
**Date processed:** 2026-10-03 (`FTR-20261003-42068099-01`)
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** `partial_fulltext_read` (partial full text); record created by `CC-20261003W6-B-REGISTRY-01`
**Primary pathway:** movement phenotype · neuroimaging
**Transferability:** none — re-description
**clinical relevance:** LOW
**Claim links:** none (see `CC-20261003W6-B-MOVEMENT-01`)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01` · `CC-20261003W6-B-MOVEMENT-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text) — manifest `deepdive_manifests/PMID42068099.json`

## LIT-0488
**Short title:** Reinehr 2022 Biomolecules — rat autoimmune glaucoma; retinal Wwox mRNA lower (microarray probe fails FDR; qPCR 0.24-fold, n 3-4)
**Authors:** Reinehr S, Safaei A, Grotegut P, et al.; Joachim SC
**Year:** 2022
**Source type:** primary research — experimental animal model (rat)
**Journal/source:** *Biomolecules* 2022;12(10):1538
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 36291747 / PMC9599116 / DOI 10.3390/biom12101538
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)
**Date processed:** 2026-10-03
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`
**Primary pathway:** CNS injury expression (retina) — off-genotype
**Transferability:** T4 — expression change in an acquired injury; no transfer to a loss-of-function genotype class
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read`

## LIT-0489
**Short title:** Kang 2026 npj Parkinsons Dis — multi-locus burden and dementia in PD; WWOX SNP rs8050111 one of five loci
**Authors:** Kang X, Lin Z, et al.; Scherzer CR
**Year:** 2026
**Source type:** primary research — multi-cohort longitudinal survival meta-analysis
**Journal/source:** *NPJ Parkinsons Dis* 2026;12
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42135313 / PMC13424109 / DOI 10.1038/s41531-026-01367-y
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)
**Date processed:** 2026-10-03
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`
**Primary pathway:** adult neurodegeneration genetics — off-genotype
**Transferability:** none to WWOX-DEE
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read`

## LIT-0490
**Short title:** Pascual 2025 Biochem J — review: excess Wnt in neurological disease; one WWOX table row
**Authors:** Pascual DM, Jebreili Rizi D, Kaur H, Marcogliese PC
**Year:** 2025
**Source type:** review
**Journal/source:** *Biochem J* 2025;482(10):601-618
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40377402 / PMC12203940 / DOI 10.1042/BCJ20240265
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)
**Date processed:** 2026-10-03
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`
**Primary pathway:** P3 — Wnt/DVL (background)
**Transferability:** none — citation of a cancer-cell primary
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text)

## LIT-0491
**Short title:** Sengupta 2025 iScience — sterols regulate DVL2 membrane/nuclear localisation; nuclear DVL2 with inhibited TCF/LEF signalling
**Authors:** Sengupta S, Yaeger JDW, Schultz MM, May DG, Roux KJ, Francis KR
**Year:** 2025
**Source type:** primary research — cell, iPSC-derived NSC and mouse
**Journal/source:** *iScience* 2025;28(6):112704
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40524961 / PMC12167792 / DOI 10.1016/j.isci.2025.112704
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)
**Date processed:** 2026-10-03
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`
**Primary pathway:** P3 — Wnt/DVL (background; inference check)
**Transferability:** none for WWOX data; bears on the inference step of DL-MOL-003
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (partial full text)

## LIT-0492
**Short title:** Hsu 2025 IJMS — review: hyaluronan in cancer and neural disease; HYAL-2/WWOX/SMAD4 and C1q-WWOX restated
**Authors:** Hsu CY, Nguyen-Tran HH, Chen YA, et al.; Chang NS
**Year:** 2025
**Source type:** review
**Journal/source:** *Int J Mol Sci* 2025;26(11):5132
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40507943 / PMC12155404 / DOI 10.3390/ijms26115132
**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)
**Date processed:** 2026-10-03
**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03
**Status:** processed
**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`
**Primary pathway:** ECM / HYAL-2 / SMAD4 (background)
**Transferability:** none to WWOX-DEE
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read`

## LIT-0493
**Short title:** Liu 2021 Nat Genet — genome-wide survival study of cognitive progression in Parkinson's disease (discovery source of the WWOX SNP rs8050111)
**Authors:** Liu G, et al.; Scherzer CR
**Year:** 2021
**Source type:** primary research — genome-wide survival study
**Journal/source:** *Nat Genet* 2021;53:787-793
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 33958783 / DOI 10.1038/s41588-021-00847-6 / PMC8459648
**Date discovered:** 2026-10-03 (reference 17 of PMID 42135313)
**Date processed:** 2026-10-04 (intake wave 7, Scientist A)
**Status note:** read at full text in intake wave 7, receipt `FTR-20261004-33958783-01`; paper record [[paper_registry_current#PAPER 204]], which declares this PMID's depth. 🔴 No depth marker is restated on this row, deliberately: a registry depth declaration counts as a reading in `coverage_report.py`, and `PAPER 204` already carries it
**Discovery source:** multihop from `FTR-20261003-42135313-01`
**Status:** processed
**Primary pathway:** adult neurodegeneration genetics — off-genotype
**Transferability:** none expected to WWOX-DEE (common SNP)
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none
**Report mentions:** `CC-20261003W6-A-REGISTRY-01`
**Next action:** none — read at full text in intake wave 7. 🔴 Two qualifications the primary supplies about the signal it is cited for: its own authors call the WWOX locus a *«suggestive association signal»* at the discovery stage (*«suggestive P < 5 × 10⁻⁵ in discovery and P < 0.05 in the replication cohort»*) and report genome-wide significance (*«P < 5 × 10⁻⁸»*) **only in the combined discovery-and-replication analysis** (integrator amendment, blind audit: the one-sided reading *suggestive* alone was corrected against the source); and WWOX is the **nearest-gene label of an imputed common variant**, with no eQTL and no fine-mapping.

## LIT-0494
**Identifier:** PMID 32368285 / DOI 10.7150/jca.40840
**Short title:** Silencing of Wwox Increases Nuclear Import of Dvl proteins in Head and Neck Cancer
**Authors:** Celebi A, Orhan C, Seyhan B, Buyru N
**Year:** 2020
**Source type:** primary research — human cell lines and tumour tissue
**Status:** processed
**Status note:** supersedes [[literature_tracking_log_current#LIT-0151]], the phase-2 corpus-alignment placeholder twin for this PMID, retired by `BATCH_20261004_001`; `partial_fulltext_read` (**partial full text**), receipt `FTR-20261004-32368285-01`; record created by `CC-20261004W7-A-REGISTRY-01`
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID32368285.json`; registry landing [[paper_registry_current#PAPER 201]]
**clinical relevance:** LOW
**Why tracked:** the one open-access primary of the three behind LEGEND's WWOX-Dvl direction; read in intake wave 7.
**PAPER link:** [[paper_registry_current#PAPER 201]]
**Note:** class-level record. Not medical advice.

## LIT-0495
**Identifier:** PMID 42558002 / DOI 10.1002/jnr.70148
**Short title:** Astrocytes in Genetic Epilepsies: Supporting Actor or Key Player?
**Authors:** Lange J, Zhao E, O'Connell E, Gillham O, McTague A
**Year:** 2026
**Source type:** review (narrative)
**Status:** processed
**Status note:** `complete_fulltext_read`, receipt `FTR-20261004-42558002-01`; record created by `CC-20261004W7-A-REGISTRY-01`
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID42558002.json`; registry landing [[paper_registry_current#PAPER 202]]
**clinical relevance:** LOW
**Why tracked:** an independent group's tabulation of the WWOX astrocyte evidence, with its own cell-autonomy verdict.
**PAPER link:** [[paper_registry_current#PAPER 202]]
**Note:** class-level record. Not medical advice.

## LIT-0496
**Identifier:** PMID 40937943 / DOI 10.1002/alz.70593
**Short title:** Ancestral genomic functional differences in oligodendroglia: implications for Alzheimer's disease
**Authors:** Ramirez AM, Nasciben LB, Moura S, et al.; Vance JM
**Year:** 2025
**Source type:** primary research — iPSC multiome
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**), receipt `FTR-20261004-40937943-01`; record created by `CC-20261004W7-A-REGISTRY-01`
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID40937943.json`; registry landing [[paper_registry_current#PAPER 203]]. Partial: figure panels captions only; thirteen supplementary tables not fetched
**clinical relevance:** LOW
**Why tracked:** the only held record quantifying WWOX transcript in human oligodendrocyte-lineage cells.
**PAPER link:** [[paper_registry_current#PAPER 203]]
**Note:** class-level record. Not medical advice.

## LIT-0497
**Short title:** Karaer 2026 Epileptic Disord — exome/clinical exome in 250 Turkish children with unexplained epilepsy; two homozygous WWOX p.Arg264* patients
**Authors:** Karaer D, Yüzbaşı BK, Şahin İ, Güngör O, Karaer K
**Year:** 2026
**Source type:** primary research — retrospective single-centre exome cohort
**Journal/source:** *Epileptic Disord* 2026;28(4):1252-1273
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42394473 / DOI 10.1002/epd2.70277 / PMC13499239
**Date discovered:** 2026-10-04 (Orchestrator selection record, intake wave 7, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-42394473-01`)
**Discovery source:** Orchestrator selection record of intake wave 7 2026-10-04
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261004W7-B-REGISTRY-01`
**Primary pathway:** clinical spectrum / WWOX-DEE · denominator
**Transferability:** T1 for the clinical presentation of a homozygous predicted-null genotype; none for missense classes
**clinical relevance:** LOW-MODERATE — counting source; phenotype is table-level
**Claim links:** none (see `CC-20261004W7-B-PATIENT-OVERLAP-01`)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_B.md` · `CC-20261004W7-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID42394473.json`

## LIT-0498
**Short title:** Alotibi 2023 Front Pediatr — array-CGH and WES in 105 Saudi children with NDD; homozygous WWOX c.606-1G>A and c.33del rows without phenotype
**Authors:** Alotibi RS, Sannan NS, AlEissa M, et al.; Alfares A
**Year:** 2023
**Source type:** primary research — retrospective laboratory-record review
**Journal/source:** *Front Pediatr* 2023;11:1133789
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 36937954 / DOI 10.3389/fped.2023.1133789 / PMC10014736
**Date discovered:** 2026-10-04 (Orchestrator selection record, intake wave 7, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-36937954-01`)
**Discovery source:** Orchestrator selection record of intake wave 7 2026-10-04
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261004W7-B-REGISTRY-01`
**Primary pathway:** clinical spectrum / allele presence · splice-acceptor allele class
**Transferability:** allele presence only; no course, outcome or RNA
**clinical relevance:** LOW — but the acceptor allele bears on the open Tabarki 2015 / Al Baradie family-3 overlap
**Claim links:** none (see `CC-20261004W7-B-PATIENT-OVERLAP-01`, `CC-20261004W7-B-SPLICE-MEASURED-01`)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_B.md` · `CC-20261004W7-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID36937954.json`

## LIT-0499
**Short title:** Sabau 2025 Int J Mol Sci — panels/exomes/genomes in 140 Romanian children with epilepsy; one compound heterozygous WWOX patient (exon-5 copy gain + intron-6 donor delins)
**Authors:** Sabau IM, Bacos-Cosma IS, Streata I, Dragulescu B, Puiu M, Chirita-Emandi A
**Year:** 2025
**Source type:** primary research — retrospective cohort
**Journal/source:** *Int J Mol Sci* 2025;26(10):4843
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40429983 / DOI 10.3390/ijms26104843 / PMC12112176
**Date discovered:** 2026-10-04 (Orchestrator selection record, intake wave 7, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-40429983-01`)
**Discovery source:** Orchestrator selection record of intake wave 7 2026-10-04
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261004W7-B-REGISTRY-01`
**Primary pathway:** clinical spectrum / WWOX-DEE · copy-number allele class
**Transferability:** T2 — both consequences predicted; the gain is unconfirmed by an orthogonal method
**clinical relevance:** LOW-MODERATE — first exon-level WWOX copy gain held; mild course
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_B.md` · `CC-20261004W7-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID40429983.json`

## LIT-0500
**Short title:** Khadija 2026 Front Genet — corpus callosum abnormalities in 107 Tunisian patients; one de novo heterozygous 16q23q24 deletion including WWOX
**Authors:** Khadija B, Abdallah HH, Slimani W, et al.; Depienne C, Mougou-Zerelli S
**Year:** 2026
**Source type:** primary research — cross-sectional referral cohort
**Journal/source:** *Front Genet* 2026;17:1815268
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42807679 / DOI 10.3389/fgene.2026.1815268 / PMC13617407
**Date discovered:** 2026-10-04 (Orchestrator selection record, intake wave 7, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-42807679-01`)
**Discovery source:** Orchestrator selection record of intake wave 7 2026-10-04
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**); record created by `CC-20261004W7-B-REGISTRY-01`
**Primary pathway:** CNV carrier / contiguous-gene deletion
**Transferability:** none for WWOX-DEE allele classes; a contiguous-gene carrier
**clinical relevance:** LOW
**Claim links:** none (see `CC-20261004W7-B-CNV-CARRIER-01` on CLAIM 032)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_B.md` · `CC-20261004W7-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42807679.json`

## LIT-0501
**Short title:** De 2025 Sci Rep — CNV dosage in two epilepsy cohorts and ten brain regions; a common WWOX intronic deletion with a nominal drug-response association
**Authors:** De T, Coin L, Johnson MR
**Year:** 2025
**Source type:** primary research — CNV association and CNV-eQTL from bead-chip intensities
**Journal/source:** *Sci Rep* 2025;15:45726
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41345172 / DOI 10.1038/s41598-025-28338-2 / PMC12753814
**Date discovered:** 2026-10-04 (Orchestrator selection record, intake wave 7, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-41345172-01`)
**Discovery source:** Orchestrator selection record of intake wave 7 2026-10-04
**Status:** processed
**Status note:** `partial_fulltext_read` (**partial full text**); record created by `CC-20261004W7-B-REGISTRY-01`
**Primary pathway:** population CNV / fragile site · drug response
**Transferability:** none for WWOX-DEE; a population polymorphism at FRA16D
**clinical relevance:** LOW
**Claim links:** none (see `CC-20261004W7-B-CNV-CARRIER-01`, DIS proposal)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_B.md` · `CC-20261004W7-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41345172.json`

## LIT-0502
**Short title:** Zhao 2026 NPJ Genom Med — targeted reflex blood RNA-seq after clinical ES/GS; WWOX c.1056+5G>C measured as partial exon deletion (VUS → LP)
**Authors:** Zhao X, Rigobello R, Driver M, et al.; Xia F, Eng CM
**Year:** 2026
**Source type:** primary research — retrospective clinical-laboratory series with a validated RNA assay
**Journal/source:** *NPJ Genom Med* 2026;11:52 [article number added 2026-10-04 by `BATCH_20261004_004` from the JATS front matter's `elocation-id`, Mirror note F7]
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42248868 / DOI 10.1038/s41525-026-00571-2 / PMC13562735
**Date discovered:** 2026-10-04 (Orchestrator selection record, intake wave 7, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-42248868-01`)
**Discovery source:** Orchestrator selection record of intake wave 7 2026-10-04
**Status:** processed
**Status note:** `complete_fulltext_read`; record created by `CC-20261004W7-B-REGISTRY-01`
**Primary pathway:** splice-allele RNA consequence · method
**Transferability:** T1 for feasibility of measuring WWOX splicing in blood RNA; T3 for the reference genotype's acceptor allele (different position)
**clinical relevance:** MODERATE — a measured WWOX splice outcome in the same intron as the reference genotype's splice allele
**Claim links:** none (see `CC-20261004W7-B-SPLICE-MEASURED-01` on CLAIM 033 and DL-BIO-002)
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_B.md` · `CC-20261004W7-B-REGISTRY-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID42248868.json`

## LIT-0503
**Short title:** Hordeaux & Chan 2026 Mol Ther Adv — commentary: how much of AAV dorsal-root-ganglion toxicity is immune-mediated?
**Authors:** Hordeaux J, Chan YK
**Year:** 2026
**Source type:** commentary (PubMed publication type News)
**Journal/source:** *Molecular Therapy Advances* 2026;34(1):201675
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42137271 / DOI 10.1016/j.omta.2026.201675 / PMC13148899
**Date discovered:** 2026-10-04 (intake wave 7 selection record, group C1 (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-42137271-01`)
**Discovery source:** intake wave 7 selection record, group C1 (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w7-C1-REGISTRY-01`; off-WWOX by measurement (zero occurrences)
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_C1.md` · `CC-20261004W7-C1-DRG-ATTRIBUTION-01`
**Next action:** none owed
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID42137271.json`; registry landing [[paper_registry_current#PAPER 211]]
**Note:** class-level record. Not medical advice.

## LIT-0504
**Short title:** Flotte 2026 Mol Ther Adv — commentary: the dose makes the poison; mechanisms of high-dose AAV cytotoxicity
**Authors:** Flotte TR
**Year:** 2026
**Source type:** commentary (PubMed publication type News)
**Journal/source:** *Molecular Therapy Advances* 2026;34(2):201746
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42170349 / DOI 10.1016/j.omta.2026.201746 / PMC13188094
**Date discovered:** 2026-10-04 (intake wave 7 selection record, group C1 (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-42170349-01`)
**Discovery source:** intake wave 7 selection record, group C1 (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w7-C1-REGISTRY-01`; off-WWOX by measurement; a liver, systemic-route commentary
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_C1.md` · `CC-20261004W7-C1-DRG-ATTRIBUTION-01`
**Next action:** none owed. The primary it comments on (a liver expression-profiling study) is **not held**; a queue candidate, not a reading of this wave
**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID42170349.json`; registry landing [[paper_registry_current#PAPER 212]]
**Note:** class-level record. Not medical advice.

## LIT-0505
**Short title:** Rioux 2026 Genes — head-to-head AAV9 biodistribution in mice by route and age
**Authors:** Rioux M, Boitnott A, Paduri S, Hu Y, Gray SJ
**Year:** 2026
**Source type:** primary research article, peer reviewed, open access
**Journal/source:** *Genes* 2026;17(2):213
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41751597 / DOI 10.3390/genes17020213 / PMC12940312
**Date discovered:** 2026-10-04 (intake wave 7 selection record, group C1 (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-41751597-01`)
**Discovery source:** intake wave 7 selection record, group C1 (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w7-C1-REGISTRY-01`; off-WWOX by measurement
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_C1.md` · `CC-20261004W7-C1-DRG-ATTRIBUTION-01` · `CC-20261004W7-C1-AGE-DOSE-CONFOUND-01`
**Next action:** DRG histology of the **survivors** is not reported in the source and would decide the exposure-without-injury reading; no further reading owed here
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41751597.json`; registry landing [[paper_registry_current#PAPER 213]]. Partial: Figures 4 to 6 and several appendix figures captions only; references not read
**Note:** class-level record. Not medical advice.

## LIT-0506
**Short title:** Gao 2026 Biomedicines — four AAV capsids by neonatal intravenous route in the murine nervous system
**Authors:** Gao H, Xu T [corrected 2026-10-04 by `CC-20261004-MIRROR-22`, replacing *«Gao H, Xu T, Lebleu B»*: Lebleu B is the journal's Academic Editor, not an author]
**Year:** 2026
**Source type:** primary research article, peer reviewed, open access
**Journal/source:** *Biomedicines* 2026;14(7):1426
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42511902 / DOI 10.3390/biomedicines14071426 / PMC13405926
**Date discovered:** 2026-10-04 (intake wave 7 selection record, group C2 (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-42511902-01`)
**Discovery source:** intake wave 7 selection record, group C2 (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W7-C2-REGISTRY-01`; off-WWOX by measurement (zero occurrences); held as a transferable neonatal-IV capsid datum
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_C2.md` · `CC-20261004W7-C2-DOSE-ROUTE-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42511902.json`; registry landing [[paper_registry_current#PAPER 214]]
**Note:** class-level record. Not medical advice.

## LIT-0507
**Short title:** Zhao 2025 PLOS One — volumetric MRI of dorsal root ganglia in a Fabry mouse, as progression and AAV-response biomarker
**Authors:** Zhao F, Yuan S, Kaittanis C, Deshpande M, Kugadas A, et al.
**Year:** 2025
**Source type:** primary research article, peer reviewed, open access; sponsor-authored
**Journal/source:** *PLOS One* 2025;20(10):e0334840
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41134821 / DOI 10.1371/journal.pone.0334840 / PMC12551818
**Date discovered:** 2026-10-04 (intake wave 7 selection record, group C2 (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-41134821-01`)
**Discovery source:** intake wave 7 selection record, group C2 (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W7-C2-REGISTRY-01`; off-WWOX by measurement; the only DRG imaging endpoint in this corpus
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety; endpoint and biomarker method
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_C2.md` · `CC-20261004W7-C2-DRG-IMAGING-01`
**Next action:** none owed
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41134821.json`; registry landing [[paper_registry_current#PAPER 215]]
**Note:** class-level record. Not medical advice.

## LIT-0508
**Short title:** Thomsen 2026 Mol Ther Adv — CSF-route AAV9 micro-dystrophin preclinical package (INS1201)
**Authors:** Thomsen G, Kaspar A, Ferraiuolo L, Chu B, Garcia VJ, et al.
**Year:** 2026
**Source type:** primary research article, peer reviewed, open access; sponsor-authored
**Journal/source:** *Molecular Therapy Advances* 2026;34(1):201707
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42137291 / DOI 10.1016/j.omta.2026.201707 / PMC13148950
**Date discovered:** 2026-10-04 (intake wave 7 selection record, group C2 (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-42137291-01`)
**Discovery source:** intake wave 7 selection record, group C2 (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W7-C2-REGISTRY-01`; off-WWOX by measurement; sponsor-authored
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w7_C2.md` · `CC-20261004W7-C2-DRG-GENOME-01` · `CC-20261004W7-C2-DOSE-ROUTE-01`
**Next action:** **reading debt retired 2026-10-04** (`CC-20261004W9-A-THOMSEN-DRG-01`) — Table S5 and Figure S7 were read and carry **no** DRG-specific NHP grading (clinical pathology; vector-genome biodistribution and shedding), verified on the rendered table and figure, so the mononuclear-infiltrate-at-every-dose pattern **cannot be tested in this package**
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42137291.json`; registry landing [[paper_registry_current#PAPER 216]]
**Note:** class-level record. Not medical advice.

## LIT-0509
**Short title:** Colin 2023 Front Cell Dev Biol — multi-omics diagnostics; one WWOX genotype with blood RT-PCR and a fibroblast western
**Authors:** Colin E, Duffourd Y, Chevarin M, et al.; Vitobello A
**Year:** 2023
**Source type:** primary research — diagnostic multi-omics series
**Journal/source:** *Front Cell Dev Biol* 2023;11:1021920
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 36926521 / PMCID PMC10011630 / DOI 10.3389/fcell.2023.1021920
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group A (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-36926521-01`)
**Discovery source:** intake wave 8 selection record, group A (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-A-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P1 — allele consequence / splicing
**Transferability:** T3
**clinical relevance:** MODERATE
**Claim links:** CLAIM 033
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_A.md` · `CC-20261004W8-A-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID36926521.json`; registry landing [[paper_registry_current#PAPER 217]]
**Note:** class-level record. Not medical advice.

## LIT-0510
**Short title:** Pagnamenta 2023 Genome Med — clinical WGS cohort; its WWOX case re-reports Piard 2019 Patient 11
**Authors:** Pagnamenta AT, Camps C, Giacopuzzi E, et al.; Taylor JC
**Year:** 2023
**Source type:** primary research — clinical whole-genome sequencing cohort
**Journal/source:** *Genome Med* 2023;15(1):94
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 37946251 / PMCID PMC10636885 / DOI 10.1186/s13073-023-01240-0
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group A (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-37946251-01`)
**Discovery source:** intake wave 8 selection record, group A (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-A-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P1 — allele consequence / genotype census
**Transferability:** none
**clinical relevance:** LOW
**Claim links:** CLAIM 033
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_A.md` · `CC-20261004W8-A-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID37946251.json`; registry landing [[paper_registry_current#PAPER 218]]
**Note:** class-level record. Not medical advice.

## LIT-0511
**Short title:** Hamanaka 2025 NPJ Genom Med — genome sequencing in ID/DD; one WWOX case, intron-5 acceptor allele + exon-5 deletion, DNA only
**Authors:** Hamanaka K, Fujita A, Miyatake S, et al.; Matsumoto N
**Year:** 2025
**Source type:** primary research — diagnostic genome-sequencing cohort
**Journal/source:** *NPJ Genom Med* 2025;10(1):60
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40858643 / PMCID PMC12381280 / DOI 10.1038/s41525-025-00521-4
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group A (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-40858643-01`)
**Discovery source:** intake wave 8 selection record, group A (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-A-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P1 — allele consequence / splicing
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** CLAIM 033
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_A.md` · `CC-20261004W8-A-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID40858643.json`; registry landing [[paper_registry_current#PAPER 219]]
**Note:** class-level record. Not medical advice.

## LIT-0512
**Short title:** Yigit 2026 Front Neurol — re-analysis in children with a cerebral-palsy diagnosis; one homozygous WWOX p.Leu239Arg child
**Authors:** Yigit A, Akgun-Dogan O, Ozkeserli Z, et al.; Ozbek U
**Year:** 2026
**Source type:** primary research — diagnostic re-analysis cohort
**Journal/source:** *Front Neurol* 2026;17:1742186
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41835067 / PMCID PMC12979860 / DOI 10.3389/fneur.2026.1742186
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group A (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-41835067-01`)
**Discovery source:** intake wave 8 selection record, group A (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-A-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P1 — allele consequence / genotype census
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_A.md` · `CC-20261004W8-A-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41835067.json`; registry landing [[paper_registry_current#PAPER 220]]
**Note:** class-level record. Not medical advice.

## LIT-0513
**Short title:** Stamouli 2026 Sci Adv — human glia-to-interneuron reprogramming; WWOX transcript peaks transiently along the trajectory
**Authors:** Stamouli CA, Degener A, Cepeda-Prado E, et al.; Rylander Ottosson D
**Year:** 2026
**Source type:** primary research — human cell reprogramming, snRNA-seq
**Journal/source:** *Sci Adv* 2026;12(1):eadv0588
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41477840 / PMCID PMC12757047 / DOI 10.1126/sciadv.adv0588
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group A (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-41477840-01`)
**Discovery source:** intake wave 8 selection record, group A (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-A-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P3 — interneuron / network development
**Transferability:** none
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_A.md` · `CC-20261004W8-A-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41477840.json`; registry landing [[paper_registry_current#PAPER 221]]
**Note:** class-level record. Not medical advice.

## LIT-0514
**Short title:** Qin 2025 J Transl Med — drug-target MR in a lymphoma; its drug list inverts its own CTD table
**Authors:** Qin Y, Wei J, He Y, et al.; Huang Y
**Year:** 2025
**Source type:** computational — Mendelian randomisation and docking
**Journal/source:** *J Transl Med* 2025;23(1):1306
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41254692 / PMCID PMC12625014 / DOI 10.1186/s12967-025-07301-9
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group A (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-41254692-01`)
**Discovery source:** intake wave 8 selection record, group A (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-A-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P8 — repurposing / expression modulation
**Transferability:** none to WWOX-DEE
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_A.md` · `CC-20261004W8-A-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41254692.json`; registry landing [[paper_registry_current#PAPER 222]]
**Note:** class-level record. Not medical advice.

## LIT-0515
**Short title:** Makii 2020 BMC Vet Res — a pure WWOX-measurement protocol, and the ceiling of every direct WWOX read-out it uses
**Authors:** Makii R, Cook H, Louke D, Breitbach J, Jennings R, Premanandan C, et al.; Fenger JM
**Year:** 2020
**Source type:** primary research — veterinary oncology; declared a pilot study
**Journal/source:** *BMC Vet Res* 2020;16:415
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 33129329 / PMCID PMC7603737 / DOI 10.1186/s12917-020-02638-3
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group B (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-33129329-01`)
**Discovery source:** intake wave 8 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-B-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P9 — measurement / assay specification
**Transferability:** T4 as biology; **T1 as an assay specification and as a ceiling on it**
**clinical relevance:** MODERATE — the corpus's only end-to-end WWOX measurement protocol
**Claim links:** CLAIM 046
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_B.md` · `CC-20261004W8-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID33129329.json`; registry landing [[paper_registry_current#PAPER 223]]
**Note:** class-level record. Not medical advice.

## LIT-0516
**Short title:** Carpanese 2025 J Cell Physiol — WWOX is one unquantified row of 283 in a murine KCa3.1 proxisome
**Authors:** Carpanese V, Sadeghi S, Todesca LM, Szabo I, Checchetto V
**Year:** 2025
**Source type:** primary research — proximity-labelling proteomics
**Journal/source:** *J Cell Physiol* 2025;240(9):e70092
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40952239 / PMCID PMC12435150 / DOI 10.1002/jcp.70092
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group B (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-40952239-01`)
**Discovery source:** intake wave 8 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-B-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P5 — interactome / proximity annotation
**Transferability:** T5 — murine Wwox, non-excitable epithelium, unvalidated proximity hit
**clinical relevance:** LOW
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_B.md` · `CC-20261004W8-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID40952239.json`; registry landing [[paper_registry_current#PAPER 224]]
**Note:** class-level record. Not medical advice.

## LIT-0517
**Short title:** Chornyy 2025 Mol Ther Methods Clin Dev — ten CNS promoters head to head; the cell-restricted one put the most protein in the liver
**Authors:** Chornyy S, Herstine JA, Holaway C, Biddle A, Vetter TA, et al.; Bradbury AM
**Year:** 2025
**Source type:** primary research — vector-engineering comparison
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(4):101588
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41036104 / PMCID PMC12481918 / DOI 10.1016/j.omtm.2025.101588
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group B (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-41036104-01`)
**Discovery source:** intake wave 8 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-B-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P7 — gene-therapy design / promoter selection
**Transferability:** T3
**clinical relevance:** MODERATE — promoter choice is a restoration-spec parameter
**Claim links:** CLAIM 047
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_B.md` · `CC-20261004W8-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41036104.json`; registry landing [[paper_registry_current#PAPER 225]]
**Note:** class-level record. Not medical advice.

## LIT-0518
**Short title:** Chauhan 2026 Mol Ther — a 126 bp non-viral mini-promoter in AAV-DJ, whose ranking inverts between IT and ICV
**Authors:** Chauhan M, Daugherty AL, Khadir F, Duzenli OF, Hoffman A, et al.; Pacak CA
**Year:** 2026
**Source type:** primary research — vector-engineering comparison
**Journal/source:** *Molecular Therapy Advances* 2026;34(1):201681
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42137269 / PMCID PMC13148911 / DOI 10.1016/j.omta.2026.201681
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group B (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-42137269-01`)
**Discovery source:** intake wave 8 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-B-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P7 — gene-therapy design / cassette headroom
**Transferability:** T3
**clinical relevance:** MODERATE
**Claim links:** CLAIM 047
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_B.md` · `CC-20261004W8-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42137269.json`; registry landing [[paper_registry_current#PAPER 226]]
**Note:** class-level record. Not medical advice.

## LIT-0519
**Short title:** Haque 2026 Front Med — lumbar IT reaches primate brain at 1-4 vg/DG, with no expression measured anywhere
**Authors:** Haque E, Devidze N, Nagendran S, Haque-Ahmed R, McAuliffe S, Lamontagne A, et al.; Porter F
**Year:** 2026
**Source type:** primary research — primate biodistribution, sponsor-authored
**Journal/source:** *Frontiers in Medicine* 2026;13:1819594
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42136830 / PMCID PMC13167494 / DOI 10.3389/fmed.2026.1819594
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group B (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-42136830-01`)
**Discovery source:** intake wave 8 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-B-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P7 — gene-therapy design / route selection
**Transferability:** T2
**clinical relevance:** HIGH for route selection
**Claim links:** CLAIM 047
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_B.md` · `CC-20261004W8-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42136830.json`; registry landing [[paper_registry_current#PAPER 227]]
**Note:** class-level record. Not medical advice.

## LIT-0520
**Short title:** Nabakowski 2026 Cells — liver de-targeting ~127-fold, at eight-fold worse packaging and fewer brain vector genomes
**Authors:** Nabakowski ZC, Jaramillo IC, Tanachaiwiwat P, Keeler GD, Chen S-H
**Year:** 2026
**Source type:** primary research — capsid engineering
**Journal/source:** *Cells* 2026;15(4):334
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41744777 / PMCID PMC12938943 / DOI 10.3390/cells15040334
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group B (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-41744777-01`)
**Discovery source:** intake wave 8 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W8-B-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt
**Primary pathway:** P7 — gene-therapy design / off-target organ risk
**Transferability:** T3
**clinical relevance:** MODERATE
**Claim links:** CLAIM 047
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_B.md` · `CC-20261004W8-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41744777.json`; registry landing [[paper_registry_current#PAPER 228]]
**Note:** class-level record. Not medical advice.

## LIT-0521
**Short title:** Moeini 2026 Mol Ther Adv — primate liver after toxic high-dose IV AAV-SMN1: p53/DNA damage at every dose, UPR only above 5e13 vg/kg
**Authors:** Moeini P, Bilbao-Arribas M, Guruceaga E, Torrens-Baile J, Lanz TA, et al.; González-Aseguinolaza G
**Year:** 2026
**Source type:** primary research — reanalysis of an existing primate and rat liver RNA-seq dataset
**Journal/source:** *Molecular Therapy Advances* 2026;34(1):201682
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42137263 / PMCID PMC13148890 / DOI 10.1016/j.omta.2026.201682
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group C (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-42137263-01`)
**Discovery source:** intake wave 8 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w8-C-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3
**clinical relevance:** MODERATE
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_C.md` · `CC-20261004w8-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42137263.json`; registry landing [[paper_registry_current#PAPER 229]]
**Note:** class-level record. Not medical advice.

## LIT-0522
**Short title:** Hordeaux 2018a Mol Ther Methods Clin Dev — rhesus ICM AAV9-hIDUA toxicology; a three-animal immunosuppression arm, single day-90 necropsy
**Authors:** Hordeaux J, Hinderer C, Goode T, Katz N, Buza EL, et al.; Wilson JM
**Year:** 2018
**Source type:** primary research — GLP-style primate toxicology
**Journal/source:** *Mol Ther Methods Clin Dev* 2018;10:79
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 30073179 / PMCID PMC6070681 / DOI 10.1016/j.omtm.2018.06.003
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group C (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-30073179-01`)
**Discovery source:** intake wave 8 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w8-C-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T2
**clinical relevance:** MODERATE
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_C.md` · `CC-20261004w8-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID30073179.json`; registry landing [[paper_registry_current#PAPER 230]]
**Note:** class-level record. Not medical advice.

## LIT-0523
**Short title:** Hordeaux 2018b Mol Ther Methods Clin Dev — companion rhesus ICM AAV9-hIDS toxicology; five-animal immunosuppression arm, no consistent ganglion reduction
**Authors:** Hordeaux J, Hinderer C, Goode T, Buza EL, Bell P, et al.; Wilson JM
**Year:** 2018
**Source type:** primary research — GLP-style primate toxicology; companion to PMID 30073179
**Journal/source:** *Mol Ther Methods Clin Dev* 2018;10:68
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 30073178 / PMCID PMC6070702 / DOI 10.1016/j.omtm.2018.06.004
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group C (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-30073178-01`)
**Discovery source:** intake wave 8 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w8-C-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T2
**clinical relevance:** MODERATE
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_C.md` · `CC-20261004w8-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID30073178.json`; registry landing [[paper_registry_current#PAPER 231]]
**Note:** class-level record. Not medical advice.

## LIT-0524
**Short title:** Buss 2022 Mol Ther Methods Clin Dev — the expression-null DRG control: AAV9.Null reaches DRG at DNA parity and produces no neuronal degeneration
**Authors:** Buss N, Lanigan L, Zeller J, Cissell D, Metea M, et al.; Fiscella M
**Year:** 2022
**Source type:** primary research — controlled primate experiment; sponsor-authored
**Journal/source:** *Mol Ther Methods Clin Dev* 2022;24:342
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 35229008 / PMCID PMC8851102 / DOI 10.1016/j.omtm.2022.01.013
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group C (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-35229008-01`)
**Discovery source:** intake wave 8 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w8-C-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T2
**clinical relevance:** HIGH strategic
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_C.md` · `CC-20261004w8-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID35229008.json`; registry landing [[paper_registry_current#PAPER 232]]
**Note:** class-level record. Not medical advice.

## LIT-0525
**Short title:** Fortuna 2025 Mol Ther Methods Clin Dev — AAV-PHP.eB beats AAV9 for primate cortical neurons after ICV, with no toxicity endpoint and a heavy liver load
**Authors:** Fortuna MG, Nyberg LH, Taskin N, Hunker A, Weed N, et al.; Ting JT
**Year:** 2025
**Source type:** primary research — capsid comparison in primate
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(4):101636
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 41438872 / PMCID PMC12721033 / DOI 10.1016/j.omtm.2025.101636
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group C (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-41438872-01`)
**Discovery source:** intake wave 8 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w8-C-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement
**Primary pathway:** P7 — gene-therapy design / capsid and route selection
**Transferability:** T2
**clinical relevance:** MODERATE
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_C.md` · `CC-20261004w8-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID41438872.json`; registry landing [[paper_registry_current#PAPER 233]]
**Note:** class-level record. Not medical advice.

## LIT-0526
**Short title:** Boespflug-Tanguy 2026 Mol Ther — a fatal human high-dose systemic AAV9 case under prednisolone plus sirolimus; complement, not adaptive immunity
**Authors:** Boespflug-Tanguy O, Valent A, Rambaud J, Léger P-L, Plu I, et al.; Perret G
**Year:** 2026
**Source type:** primary research — single fatal case report, compassionate use
**Journal/source:** *Molecular Therapy* 2026;34(8):4442
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42198847 / PMCID PMC13464153 / DOI 10.1016/j.ymthe.2026.05.016
**Date discovered:** 2026-10-04 (intake wave 8 selection record, group C (2026-10-04))
**Date processed:** 2026-10-04 (`FTR-20261004-42198847-01`)
**Discovery source:** intake wave 8 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004w8-C-REGISTRY-01`; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3 as a **class-level dose boundary**
**clinical relevance:** HIGH as a safety boundary
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `research/intake_wave_20261004w8_C.md` · `CC-20261004w8-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42198847.json`; registry landing [[paper_registry_current#PAPER 234]]
**Note:** class-level record. Not medical advice.
## LIT-0527
**Short title:** Krug 2013 Arch Toxicol — hESC-derived test systems for developmental neurotoxicity; the platform behind a curated valproate row
**Authors:** Krug AK, Kolde R, Gaspar JA, Rempel E, Balmer NV, et al.; Sachinidis A (38 authors)
**Year:** 2013
**Source type:** primary research
**Journal/source:** *Archives of Toxicology* 2013;87(1):123-143
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 23179753 / PMCID PMC3535399 / DOI 10.1007/s00204-012-0967-3
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-23179753-01`)
**Discovery source:** intake wave 9 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9, group B); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement — WWOX occurs zero times in the running text
**Primary pathway:** none — toxicogenomics background
**Transferability:** T3 — transferable platform lesson only
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID23179753.json`; registry landing [[paper_registry_current#PAPER 235]]
**Note:** class-level record. Not medical advice.

---
## LIT-0528
**Short title:** Balmer 2014 Arch Toxicol — transient transcriptome responses to disturbed neurodevelopment; the one 'down' WWOX row is an untreated developmental change
**Authors:** Balmer NV, Klima S, Rempel E, Ivanova VN, Kolde R, Weng MK, Meganathan K, Henry M, Sachinidis A, Berthold MR, Hengstler JG, Rahnenführer J, Waldmann T, Leist M
**Year:** 2014
**Source type:** primary research
**Journal/source:** *Archives of Toxicology* 2014;88(7):1451-1468
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 24935251 / PMCID PMC4067541 / DOI 10.1007/s00204-014-1279-6
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-24935251-01`)
**Discovery source:** intake wave 9 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9, group B); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement — WWOX occurs zero times in the running text
**Primary pathway:** none — toxicogenomics background
**Transferability:** T3 — transferable platform lesson only
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID24935251.json`; registry landing [[paper_registry_current#PAPER 236]]
**Note:** class-level record. Not medical advice.

---
## LIT-0529
**Short title:** Rempel 2015 Arch Toxicol — a transcriptome-based classifier for developmental toxicants; three of five WWOX probe sets up with valproate, sign fixed by sentinels
**Authors:** Rempel E, Hoelting L, Waldmann T, Balmer NV, Schildknecht S, et al.; Leist M (18 authors)
**Year:** 2015
**Source type:** primary research
**Journal/source:** *Archives of Toxicology* 2015;89(9):1599-1618
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 26272509 / PMCID PMC4551554 / DOI 10.1007/s00204-015-1573-y
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-26272509-01`)
**Discovery source:** intake wave 9 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9, group B); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement — WWOX occurs zero times in the running text
**Primary pathway:** none — toxicogenomics background
**Transferability:** T3 — transferable platform lesson only
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID26272509.json`; registry landing [[paper_registry_current#PAPER 237]]
**Note:** class-level record. Not medical advice.

---
## LIT-0530
**Short title:** Shinde 2017 Arch Toxicol — transcriptome-based developmental indices; signed fold changes put WWOX up with valproate in both systems
**Authors:** Shinde V, Hoelting L, Srinivasan SP, Meisig J, Meganathan K, et al.; Sachinidis A (22 authors)
**Year:** 2017
**Source type:** primary research
**Journal/source:** *Archives of Toxicology* 2017;91(2):839-864
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 27188386 / PMCID PMC5306084 / DOI 10.1007/s00204-016-1741-8
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-27188386-01`)
**Discovery source:** intake wave 9 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9, group B); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement — WWOX occurs zero times in the running text; the print year is 2017 although the e-publication is 2016
**Primary pathway:** none — toxicogenomics background
**Transferability:** T3 — transferable platform lesson only
**clinical relevance:** BACKGROUND
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID27188386.json`; registry landing [[paper_registry_current#PAPER 238]]
**Note:** class-level record. Not medical advice.

---
## LIT-0531
**Short title:** Bey 2020 Mol Ther Methods Clin Dev — intra-CSF AAV9 and AAVrh10 in nonhuman primates under triple immunosuppression; a descriptive DRG baseline
**Authors:** Bey K, Deniaud J, Dubreil L, Joussemet B, Cristini J, Ciron C, Hordeaux J, et al.; Colle M-A (22 authors)
**Year:** 2020
**Source type:** primary research
**Journal/source:** *Molecular Therapy. Methods & Clinical Development* 2020;17:771-784
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 32355866 / PMCID PMC7184633 / DOI 10.1016/j.omtm.2020.04.001
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-32355866-01`)
**Discovery source:** intake wave 9 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9, group B); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement — WWOX occurs zero times in the running text. 🔴 **First author is Bey, not Hordeaux** — the wave-9 selection's label «Hordeaux 2020» is wrong; Hordeaux J is author 7 of 22
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3 as a class-level route-and-regimen baseline; T5 for anything quantitative
**clinical relevance:** BACKGROUND — safety context, not evidence
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID32355866.json`; registry landing [[paper_registry_current#PAPER 239]]
**Note:** class-level record. Not medical advice.

---
## LIT-0532
**Short title:** Hordeaux 2022 Hum Gene Ther — a graded GLP ICM dose-response without immunosuppression; DRG neuronal degeneration at most grade 1, dorsal axonopathy to grade 3
**Authors:** Hordeaux J, Jeffrey BA, Jian J, Choudhury GR, Michalson K, Mitchell TW, Buza EL, Chichester J, Dyer C, Bagel J, Vite CH, Bradbury AM, Wilson JM
**Year:** 2022
**Source type:** primary research
**Journal/source:** *Human Gene Therapy* 2022;33(9-10):499-517
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 35333110 / PMCID PMC9142772 / DOI 10.1089/hum.2021.245
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group B)
**Date processed:** 2026-10-04 (`FTR-20261004-35333110-01`)
**Discovery source:** intake wave 9 selection record, group B (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9, group B); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt; off-WWOX by measurement — WWOX occurs zero times in the running text
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Transferability:** T3 as a class-level graded dose-response without immunosuppression; T5 for dose transfer
**clinical relevance:** BACKGROUND — safety context, not evidence
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-B-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID35333110.json`; registry landing [[paper_registry_current#PAPER 240]]
**Note:** class-level record. Not medical advice.

---
## LIT-0533
**Short title:** Henry 2025 Epilepsia — clinical genome sequencing in 733 children with epilepsy; four WWOX diagnoses and the only measured RNA consequence of a deep intronic WWOX allele
**Authors:** Henry OJ, Ygberg S, Barbaro M, Lesko N, Karlsson L, Peña-Pérez L, Båvner A, Töhönen V, Lindstrand A, Stödberg T, Wedell A
**Year:** 2025
**Source type:** primary research
**Journal/source:** *Epilepsia* 2025;66(8):2966-2979
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 40183601 / PMCID PMC12371643 / DOI 10.1111/epi.18403
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group C)
**Date processed:** 2026-10-04 (`FTR-20261004-40183601-01`)
**Discovery source:** intake wave 9 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-C-REGISTRY-01` (intake wave 9, group C); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt. The consequence is **qualitative only**: no read fraction, frame position, NMD, protein or tissue is printed. No individual-level or parent-of-origin detail is carried
**Primary pathway:** P1 — allele consequence; splice mechanism
**Transferability:** T2 for the allele's qualitative RNA consequence; T5 for anything quantitative
**clinical relevance:** BACKGROUND — class-level allele mechanics
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID40183601.json`; registry landing [[paper_registry_current#PAPER 241]]
**Note:** class-level record. Not medical advice.

---
## LIT-0534
**Short title:** Tang 2026 Cells — WWOX protein measured in L1CAM-captured plasma neuronal-enriched vesicles; relative NPX, singlet, one marked within-sex comparison
**Authors:** Tang N, Xia F, Freasier H, Tien PC, Glesby MJ, et al.; Pulliam L (18 authors)
**Year:** 2026
**Source type:** primary research
**Journal/source:** *Cells* 2026;15(17):1581
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42738875 / PMCID PMC13565498 / DOI 10.3390/cells15171581
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group C)
**Date processed:** 2026-10-04 (`FTR-20261004-42738875-01`)
**Discovery source:** intake wave 9 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-C-REGISTRY-01` (intake wave 9, group C); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt. **§ 13: Tier 1 by kind, NOT validated** — no sensitivity and no specificity are printed for WWOX in any population. The journal's Academic Editor is excluded from the Authors field
**Primary pathway:** biomarker / endpoint interface (LEGEND_CORE § 13)
**Transferability:** T3 as a measurement route; T5 as an endpoint
**clinical relevance:** BACKGROUND — a measurement route, not an endpoint and not validated
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42738875.json`; registry landing [[paper_registry_current#PAPER 242]]
**Note:** class-level record. Not medical advice.

---
## LIT-0535
**Short title:** Lima 2026 eLife — PRMT1-SFPQ intron retention in craniofacial development; Wwox named among the long retained-intron genes, retention marked and abundance not
**Authors:** Lima JR, Ungvijanpunya N, Chen Q, Pham HQH, Rosen T, Park G, Vantankhah M, Yen S, Chai Y, Merrill AE, Liu Z, Chen JF, Yang Y, Peng W, Xu J
**Year:** 2026
**Source type:** primary research
**Journal/source:** *eLife* 2026;13:RP101386
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42770556 / PMCID PMC13597084 / DOI 10.7554/eLife.101386
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group C)
**Date processed:** 2026-10-04 (`FTR-20261004-42770556-01`)
**Discovery source:** intake wave 9 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-C-REGISTRY-01` (intake wave 9, group C); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt. ⚠️ **No dossier was written** — the write was halted by a model safety classifier; the halt is recorded in the receipt and in the wave note. Two JATS editor contribs are excluded from the Authors field
**Primary pathway:** transcript-level WWOX dose regulation
**Transferability:** T3 for the existence of a trans-acting mechanism; T5 for any lever, neuronal relevance or protein effect
**clinical relevance:** BACKGROUND — mechanism candidate only
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42770556.json`; registry landing [[paper_registry_current#PAPER 243]]
**Note:** class-level record. Not medical advice.

---
## LIT-0536
**Short title:** Köhler 2026 J Neurooncol — patient-derived tissue cultures for AAV-mediated gene delivery in glioblastoma; an earned null for WWOX
**Authors:** Köhler F, Hess K, Koloske C, Gaunitz F, Rosahl SK, Gerlach R, Kallendrusch S
**Year:** 2026
**Source type:** primary research
**Journal/source:** *Journal of Neuro-Oncology* 2026;179(3):93
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42771216 / PMCID PMC13597561 / DOI 10.1007/s11060-026-05807-w
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group C)
**Date processed:** 2026-10-04 (`FTR-20261004-42771216-01`)
**Discovery source:** intake wave 9 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-C-REGISTRY-01` (intake wave 9, group C); identity authored from the artefact's JATS front matter; reading is `partial_fulltext_read` (**partial full text**), never upgraded from its receipt. 🔴 **WWOX occurs zero times: an EARNED NULL**, read and measured, landing as a corpus stub rather than a PAPER record because there is no WWOX content to record
**Primary pathway:** none — transferable method question only
**Transferability:** T3 — transferable method lesson only
**clinical relevance:** BACKGROUND — transferable method only, not evidence
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-C-REGISTRY-01`
**Next action:** none — read and registered
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — manifest `deepdive_manifests/PMID42771216.json`; registry landing [[paper_registry_current#CORPUS-STUB-180]]
**Note:** class-level record. Not medical advice.

---
## LIT-0537
**Short title:** van der Sanden 2026 medRxiv (PREPRINT — NOT PEER REVIEWED) — optical genome mapping in 57 patient-parent trios; the same deep intronic WWOX allele, with an RT-PCR asserted and no data shown
**Authors:** van der Sanden B, Vorimo S, Brunet T, Boughalem A, Jacob M, et al.; Hoischen A (29 authors)
**Year:** 2026
**Source type:** preprint — NOT PEER REVIEWED
**Journal/source:** medRxiv (the preprint server for health sciences), posted 21 January 2026
**Identifier type:** DOI / preprint id (no PMID exists)
**Identifier value:** DOI 10.64898/2026.01.16.26344264 / PPR1269651
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group C)
**Date processed:** 2026-10-04 (`FTR-20261004-PPR1269651-01`)
**Discovery source:** intake wave 9 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-C-REGISTRY-01`, keyed by DOI with the PPR id because **no PMID exists**. 🔴 **PREPRINT, NOT PEER REVIEWED**; a preprint never earns a PAPER record and never raises a claim. Reading is `partial_fulltext_read` (**partial full text**), receipt `FTR-20261004-PPR1269651-01`, dossier `research/fulltext_dossiers/PPR1269651.md`; there is no PMID-keyed manifest. ⚠️ Its WWOX content is **three sentences and no figure**: the donor effect is printed as a **prediction**, the RT-PCR confirmation as **one unillustrated sentence with no data, method or tissue**, and the zygosity it prints (in trans with a 51 kb deletion) **differs** from the peer-reviewed cohort's homozygous record — recorded, not reconciled
**Primary pathway:** P1 — allele consequence; splice mechanism
**Transferability:** T5 — a preprint never raises a claim's status and is never promoted
**clinical relevance:** BACKGROUND — class level only
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-C-REGISTRY-01`
**Next action:** none — read and registered. **Never promoted; a preprint raises nothing.**
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — dossier `research/fulltext_dossiers/PPR1269651.md`; no PAPER landing by design (preprint)
**Note:** class-level record. **Preprint, not peer reviewed.** Not medical advice.

---
## LIT-0538
**Short title:** Ruhela 2026 Research Square (PREPRINT — NOT PEER REVIEWED) — a GWAS integrating maternal and child genotypes for fetal alcohol spectrum disorders; the WWOX result is an unreplicated common-variant modifier association
**Authors:** Ruhela V, Lesseur C, Cilleros-Portet A, Jacobson SW, Jacobson JL, Meintjes EM, Dodge NC, Akkaya-Hocagil T, Hoyme HE, Cheng H, Chen J, Hao K, Deyssenroth MA, Tosto G, Carter RC
**Year:** 2026
**Source type:** preprint — NOT PEER REVIEWED
**Journal/source:** Research Square, posted 10 September 2026
**Identifier type:** DOI / preprint id (no PMID exists)
**Identifier value:** DOI 10.21203/rs.3.rs-9950101/v1 / PPR1316475
**Date discovered:** 2026-10-04 (intake wave 9 selection record, group C)
**Date processed:** 2026-10-04 (`FTR-20261004-PPR1316475-01`)
**Discovery source:** intake wave 9 selection record, group C (2026-10-04)
**Status:** processed
**Status note:** record created by `CC-20261004W9-C-REGISTRY-01`, keyed by DOI with the PPR id because **no PMID exists**. 🔴 **PREPRINT, NOT PEER REVIEWED.** Reading is `partial_fulltext_read` (**partial full text**), receipt `FTR-20261004-PPR1316475-01`, dossier `research/fulltext_dossiers/PPR1316475.md`; there is no PMID-keyed manifest. ⚠️ **Author order differs inside the artefact:** the cover page puts Carter RC first, while the manuscript's own title page gives Ruhela V as first author and Carter RC as last, shared-senior and corresponding — the manuscript byline is used here and the cover-page order is recorded as the discrepancy it is. ⚠️ The WWOX result is a **common-variant modifier association** on a parent-side haplotype, **unreplicated**, and the preprint is **internally inconsistent on the direction of effect**. Nothing here bears on any WWOX allele class the model holds, and a heterozygote is neither a negative nor a positive for haploinsufficiency
**Primary pathway:** none — common-variant association, off the disease model's allele classes
**Transferability:** T5 — a preprint never raises a claim's status and is never promoted
**clinical relevance:** BACKGROUND — class level only
**Claim links:** none
**Working Model impact:** none — no block is redefined
**Report mentions:** `CC-20261004W9-C-REGISTRY-01`
**Next action:** none — read and registered. **Never promoted; a preprint raises nothing.**
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — dossier `research/fulltext_dossiers/PPR1316475.md`; no PAPER landing by design (preprint)
**Note:** class-level record. **Preprint, not peer reviewed.** Not medical advice.

---
