# Literature Tracking Log

> **Public edition — de-identified.** Disease-level registry from public literature. All individual-linking data removed (names, geography, report/sample IDs, dates, parent-of-origin, cell-line ownership). Specific variants appear only as decoupled disease-model worked examples drawn from public literature, never as one persistent individual's inherited alleles. Some entries remain in their original language. Not medical advice.
## WWOX — Literature Tracking Log
**Version:** v1.5
**Date baseline:** 2026-03-28
**Last update:** 2026-07-10 — URG_2026-07-09_001 category 5: LIT-0085 Maroni 2017 declassato `background_only / dependency-contaminated`; creato LIT-0401 per il primario ritirato PMID 28151481. Nessun claim baseline contaminato.

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
**Journal/source:** Molecular Therapy - Methods & Clinical Development (OMTA) 2026;34 (Cell Press)
**Identifier type:** Journal (published) — era Preprint DOI
**Identifier value:** OMTA vol 34 (2026); PMID/DOI da confermare quando indicizzato su PubMed (aggiornato preprint→published 2026-07-04, CC-2026-07-03-001)
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
**Current status:** integrated
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
**Current status:** integrated
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
**Current status:** processed
**Next action:** no further action
**Flags:** low-yield flag

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
**Current status:** integrated
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
**Current status:** integrated
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
**Evidence depth:** full text reviewed (PMC open access)
**Full text status:** found — PMC11298992
**Current status:** integrated
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
**Current status:** integrated
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
**Current status:** filtered_in — queued per full text
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
**Current status:** background_only
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
**Current status:** filtered_in — queued per lettura media priorità
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
**Current status:** processed
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
**Status:** filtered_out
**Filter reason:** WWOX in Bcl-XL/Mcl-1 degradation via lysosome in cancer cells — non-CNS, non-pediatric, mechanistically distant
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
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX and metabolic regulation in normal and pathological conditions

---

## LIT-0030
**Short title:** corpus paper 3
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34831305 / DOI 10.3390/cells10113082
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 3
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
**Next action:** screening and tier assignment
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
**Next action:** screening and tier assignment
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
**Next action:** screening and tier assignment
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 11
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 29
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
**Note:** Title: WWOX gene and gene product: tumor suppression through specific protein interactions

---

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
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34852950 / DOI 10.1016/j.neurobiolaging.2021.10.011
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 33
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
**Next action:** screening and tier assignment
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 44
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
**Note:** Title: Pleiotropic Functions of Tumor Suppressor WWOX in Normal and Cancer Cells

---

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
**Short title:** corpus paper 46
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 27869163 / DOI 10.1038/onc.2016.389
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 46
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
**Note:** Title: Wwox-Brca1 interaction: role in DNA repair pathway choice

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
**Short title:** corpus paper 48
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 34747138 / DOI 10.15252/emmm.202114599
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 48
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 50
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
**Short title:** corpus paper 53
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 36828035 / DOI 10.1016/j.pneurobio.2023.102425
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 53
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
**Note:** Title: WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice

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
**Short title:** corpus paper 55
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 24330518 / DOI 10.1186/1471-2407-13-593
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 55
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
**Note:** Title: The cancer gene WWOX behaves as an inhibitor of SMAD3 transcriptional activity via direct binding

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
**Next action:** screening and tier assignment
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
**Short title:** corpus paper 59
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30356099 / DOI 10.1038/s41436-018-0339-3
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 59
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
**Short title:** corpus paper 70
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35984507 / DOI 10.1007/s00018-022-04508-7
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 70
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
**Note:** Title: WWOX inhibition by Zfra1-31 restores mitochondrial homeostasis and viability of neuronal cells exposed to high glucose

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
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 29724996 / DOI 10.1038/s41419-018-0510-4
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 73
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
**Note:** Title: WWOX controls hepatic HIF1alpha to suppress hepatocyte proliferation and neoplasia

---

## LIT-0097
**Short title:** corpus paper 74
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 35409089 / DOI 10.3390/ijms23073729
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 74
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
**Note:** Title: Wwox Binding to the Murine Brca1-BRCT Domain Regulates Timing of Brip1 and CtIP Phospho-Protein Interactions

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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 76
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 77
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 78
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 81
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 83
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
**Note:** Title: Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects

---

## LIT-0111
**Short title:** corpus paper 88
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 31275852 / DOI 10.3389/fonc.2019.00517
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 88
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
**Note:** Title: Wwox Deletion in Mouse B Cells Leads to Genomic Instability, Neoplastic Transformation, and Monoclonal Gammopathies

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
**Short title:** corpus paper 91
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 28283473 / DOI 10.1152/ajplung.00034.2017
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 91
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
**Note:** Title: Loss of lung WWOX expression causes neutrophilic inflammation

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
**Next action:** screening and tier assignment
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
**Short title:** corpus paper 101
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41254692 / DOI 10.1186/s12967-025-07301-9
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 101
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 102
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 104
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
**Note:** Title: The common fragile site FRA16D gene product WWOX: roles in tumor suppression and genomic stability

---

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
**Short title:** corpus paper 107
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 16941225 / DOI 10.1007/s10735-006-9046-5
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 107
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
**Note:** Title: WWOX protein expression in normal human tissues

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
**Short title:** corpus paper 110
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 39868255 / DOI 10.1101/2025.01.17.633677
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 110
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
**Note:** Title: Partial Wwox Loss of Function Increases Severity of Murine Sepsis and Neuroinflammation [PREPRINT bioRxiv]

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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 119
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
**Note:** Title: WWOX gene restoration prevents lung cancer growth in vitro and in vivo

---

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
**Short title:** corpus paper 130
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 14526170 / DOI 10.1159/000072844
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 130
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
**Note:** Title: WWOX, the common chromosomal fragile site, FRA16D, cancer gene

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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 132
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
**Next action:** screening and tier assignment
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
**Next action:** screening and tier assignment
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
**Short title:** corpus paper 143
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 15064722 / DOI 10.1038/sj.onc.1207680
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 143
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
**Note:** Title: WWOX binds the specific proline-rich ligand PPXY: identification of candidate interacting proteins

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
**Next action:** screening and tier assignment
**Flags:** corpus placeholder / not yet screened
**Note:** Title: WWOX Induction Promotes Bcl-XL and Mcl-1 Degradation Through a Lysosomal Pathway upon Stress Response

---

## LIT-0166
**Short title:** corpus paper 148
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 15982416 / DOI 10.1186/1471-2407-5-64
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 148
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
**Note:** Title: WWOX protein expression varies among ovarian carcinoma histotypes and correlates with less favorable prognosis

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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 152
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
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 164
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
**Note:** Title: Somatic loss of WWOX is associated with TP53 perturbation in basal-like breast cancer

---

## LIT-0181
**Short title:** corpus paper 165
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 30285739 / DOI 10.1186/s12915-018-0576-6
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 165
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
**Note:** Title: VOPP1 promotes breast tumorigenesis by interacting with the tumor suppressor WWOX

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
**Short title:** corpus paper 168
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 22574198 / DOI 10.1371/journal.pone.0036618
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 168
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
**Note:** Title: Conditional Wwox deletion in mouse mammary gland by means of two Cre recombinase approaches

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
**Short title:** corpus paper 178
**Authors:** not yet extracted
**Year:** unknown
**Source type:** not yet screened
**Journal/source:** not yet extracted
**Identifier type:** PMID / DOI
**Identifier value:** PMID 41090157 / DOI 10.1016/j.bneo.2025.100153
**Date discovered:** 2026-04-12
**Date processed:** not yet processed
**Discovery window:** phase-2 corpus alignment
**Discovery source:** paper_corpus_reference_current.md
**Discovery query:** corpus paper 178
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
**Note:** Title: B-cell-specific Wwox deletion promotes plasmablastic tumor development and proinflammatory signature

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
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 242
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
**Short title:** Frequent downregulation and loss of WWOX gene expression in human hepatocellu...
**Authors:** Park et al.
**Year:** 2004
**Source type:** Article
**Journal/source:** Br J Cancer
**Identifier:** PMID 15266310 / PMC2364795 / DOI 10.1038/sj.bjc.6602023
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 244
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
**Note:** Title: Frequent downregulation and loss of WWOX gene expression in human hepatocellular carcinoma

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
**Authors:** Pimenta et al.
**Year:** 2008
**Source type:** Article
**Journal/source:** Oral Oncol
**Identifier:** PMID 18061530 / PMC4143237 / DOI 10.1016/j.oraloncology.2007.08.019
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 260
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
**Note:** Title: Molecular alterations in the tumor suppressor gene WWOX in oral leukoplakias

## LIT-0261
**Short title:** Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenes...
**Authors:** Mare et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Am J Cancer Res
**Identifier:** PMID 21731849 / PMC3124638
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 261
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
**Note:** Title: Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenesis of osteosarcoma

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
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 263
**Priority:** medium
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** in — standard
**Tier:** B
**Status:** screened
**Primary pathway:** P6 — DDR / genome stability
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
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 268
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
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
**Next action:** background-only; escalate only on convergence signal
**Flags:** FASE 1 batch entry / no deep-dive yet
**Note:** Title: Frequent attenuation of the WWOX tumor suppressor in osteosarcoma is associated with increased tumorigenicity and aberrant RUNX2 expression

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
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 282
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
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 284
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
**Short title:** Association between decreased WWOX protein expression and thyroid cancer deve...
**Authors:** Dias et al.
**Year:** 2007
**Source type:** Article
**Journal/source:** Thyroid
**Identifier:** PMID 18047428 / PMC4150466 / DOI 10.1089/thy.2007.0232
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 286
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
**Note:** Title: Association between decreased WWOX protein expression and thyroid cancer development

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
**Species:** rat
**Transferability:** unassigned in triage
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
**Next action:** full-text retrieval + deep-dive in next session
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
**Identifier:** PMID 21476439
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 306
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
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 308
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
**Note:** Title: WW domain-containing oxidoreductase's role in myriad cancers: clinical significance and future implications

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
**Authors:** Nunez et al.
**Year:** 2005
**Source type:** Comparative Study
**Journal/source:** Breast Cancer Res Treat
**Identifier:** PMID 15692750 / PMC4145848 / DOI 10.1007/s10549-004-1474-x
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 324
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
**Note:** Title: Frequent loss of WWOX expression in breast cancer: correlation with estrogen receptor status

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
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 333
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
**Short title:** WWOX mRNA expression profile in epithelial ovarian cancer supports the role o...
**Authors:** # et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 15870886 / PMC4166600 / DOI 10.3892/ijo.26.6.1681
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 337
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
**Note:** Title: WWOX mRNA expression profile in epithelial ovarian cancer supports the role of WWOX variant 1 as a tumour suppressor, although the role of variant 4 remains unclear

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
**Next action:** full-text retrieval; depth pass if model-shifting
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
**Year:** 2026
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
**Next action:** full-text retrieval + deep-dive in next session
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
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 358
**Priority:** low / background
**Quality status:** peer-reviewed (PubMed listing)
**Filter decision:** background only
**Tier:** C
**Status:** screened
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
**Next action:** full-text retrieval + deep-dive in next session
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
**Authors:** Pimenta et al.
**Year:** 2006
**Source type:** Article
**Journal/source:** Int J Cancer
**Identifier:** PMID 16152610 / PMC4145845 / DOI 10.1002/ijc.21446
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 367
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
**Note:** Title: Characterization of the tumor suppressor gene WWOX in primary human oral squamous cell carcinomas

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
**Short title:** Impact of decitabine on immunohistochemistry expression of the putative tumor...
**Authors:** Stewart et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Clin Epigenetics
**Identifier:** PMID 25024751 / PMC4094901 / DOI 10.1186/1868-7083-6-13
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 378
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
**Note:** Title: Impact of decitabine on immunohistochemistry expression of the putative tumor suppressor genes FHIT, WWOX, FUS1 and PTEN in clinical tumor samples

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
**Authors:** Thavathiru et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Mol Carcinog
**Identifier:** PMID 16187332 / PMC4166602 / DOI 10.1002/mc.20122
**Date discovered:** 2026-04-18
**Date screened:** 2026-04-18
**Date processed:** triage only
**Date last touched:** 2026-04-18
**Discovery window:** FASE 1 triage 221–400
**Discovery source:** 400_paper.txt batch corpus
**Discovery query:** corpus paper 385
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
**Note:** Title: Expression of common chromosomal fragile site genes, WWOX/FRA16D and FHIT/FRA3B is downregulated by exposure to environmental carcinogens, UV, and BPDE but not by IR

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
**Status:** archived
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
