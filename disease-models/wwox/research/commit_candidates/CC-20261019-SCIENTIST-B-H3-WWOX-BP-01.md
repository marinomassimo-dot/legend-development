# COMMIT CANDIDATE — CC-20261019-SCIENTIST-B-H3-WWOX-BP-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-b`, interventions batch 2026-10-19 group H3, branch `task/INTERV-H3-B-20261019`.
**context_policy:** `SOURCE_FIRST` for every reading cited (first reads); registry comparison admitted after each first pass.
**target_wm_version:** `WM_v7.20_2026-10-04`. **Change class:** **MINOR** — new paper-registry records and evidence-boundary notes; no claim status, no baseline claim reversed, no working-model block change. The legend-locator-audit trigger is not met; the triples below are supplied for a later blind audit.
**Not medical advice. Class level only. BLOCK-1 caution: nothing here is a dosing or treatment statement.**
**WWOX evidence on adrenaline or adrenergic signalling: none. This candidate concerns the one WWOX-direct item found by the extra search: a gene-level blood-pressure association, which is not adrenergic evidence.**

## Target

`disease-models/wwox/registries/paper_registry_current.md` · promote `CORPUS P360` (PMID 22479346, Tier C triage placeholder, no deep-dive) to a numbered paper record with the corrections below. No claim is edited.

## What is missing now

The record says "triage only, background, low relevance". The deep-dive adds what the paper actually reports and where it fails.

| Item | Content | Receipt |
|---|---|---|
| Yang 2012 (22479346) | WWOX is one of 17 genes with differential allelic and expression distributions in a young-onset hypertension scan (400 matched pairs, Han Chinese, Taiwan); gene-based p 7.5e-14 and 1.2e-8 in continuous-coding models, 0.017 and 0.022 nominally; no SNP at the stated threshold; replicated in a Hong Kong Han Chinese family study, not in a British case-control study; expression lower in cases (Table S3 beta minus 0.248); 24 cis-eQTL; mouse knockout phenotypes (hypoglycaemia, abnormal adrenal and pituitary morphology, postnatal lethality) are a database lookup, not measurements | `FTR-20261019-22479346-01` |

## Proposed paper-registry record

Role: "WWOX-direct gene-level blood-pressure association, exploratory, ancestry-restricted; no autonomic content; defects: expression test on genotype-extreme pairs, reference 23 versus 34 mismatch, knockout phenotypes described as variant associations; relevance LOW-MODERATE to the autonomic and vascular-tone question". ESPANSIONE; transferability T3.

## Proposed discovery leads

1. **Blood pressure or autonomic data in WWOX-DEE cohorts are an open question**; this gene-level hint (one ancestry group, no SNP-level significance) is a reason to ask, not an answer (IPOTESI).

## Ordering

Receipt for 22479346 must be in the ledger first.

### LOCATOR TRIPLES FOR BLIND AUDIT

| PMID | entry | proposition | verbatim snippet | anchor |
|---|---|---|---|---|
| 22479346 | entry 1 | NO SNP-LEVEL SIGNAL: the single-SNP scan found no SNP at the stated thresholds; the gene-level hits are built from marginal SNPs. | No significant SNPs (pFDR<10−3 or p<10−7) were found. | Results, Genome-wide SBAS |
| 22479346 | entry 2 | WWOX NUMBERS: the gene-based p-values are 7.47 x 10 to the minus 14 (quoted FDR 5.77 x 10 to the minus 3) in the continuous-coding model and 1.18 x 10 to the minus 8 with BMI adjustment; the nominal-coding raw p-values are 0.017 a | WWOX, which encodes the WW domain-containing protein on 16q23.3-q24.1, is the third gene that was simultaneously identified by our genome-wide GBAS | Results, Replication analysis, WWOX paragraph |
| 22479346 | entry 3 | REPLICATION IS WITHIN ANCESTRY: no gene was significantly confirmed in the British case-control data; WWOX is replicated only in the Hong Kong Han Chinese family study. | Although no genes identified by us were significantly confirmed by the WTCCCHS data (Caucasian) | Discussion, paragraph 1 |
| 22479346 | entry 5 | MOUSE ANNOTATION AS MECHANISM: the article says WWOX variants are associated with hypoglycaemia, hyperphosphatemia, lower cholesterol and triglycerides and higher uric acid in mice; supplementary Table S2 shows these are Mouse Gen | WWOX variants are associated with hypoglycemia, hyperphosphatemia, decreased circulating cholesterol levels and triglyceride levels, but with increased blood uric acid le | Results, Replication analysis, WWOX paragraph |
| 22479346 | entry 6 | CITATION MISMATCH: the text says WWOX variants were associated with blood pressure in a previous Japanese GWAS (reference 23), but Table 1 of the same article lists reference 23 as a European-ancestry study and the Japanese study  | WWOX variants were also found to be associated with blood pressure in a previous Japanese GWAS [23]. | Results, Replication analysis, WWOX paragraph |


---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_003` · 2026-10-20 · ACTOR_ID `orchestrator` (stated assumption, batch integrator)
**Working model:** WM_v7.21 -> WM_v7.22 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit:** not run — no baseline claim is narrowed and no MAJOR contingency is declared; the candidate's locator triples are carried for a later audit.
**What landed:** `PAPER 324` (promotion of `CORPUS P360`, kept as history; `LIT-0360` promoted to processed); lead `DL-MECH-142`. Receipt identifier: PMID 22479346 (`FTR-20261019-22479346-01`).
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record is carried.
