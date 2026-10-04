# Intake wave 12 (re-read) — Scientist A, 2026-10-04

context_policy: SOURCE_FIRST · ACTOR_ID `scientist` (Scientist A) · branch `task/sci-A-20261004w12` · Group A of the wave-12 selection.
**Question:** what do the owed sections add to or limit in the claim that one WWOX allele conserves some endpoints but defines no CNS threshold, and in the genotype–mortality class?
Class-level only. Nothing here is medical advice. Genotype caution: P47T ≠ Q230P ≠ G372R ≠ A141T ≠ P252A; a heterozygote is neither a negative nor a positive for haploinsufficiency.

## 1 · PMID 29808465 — Johannsen 2018 (owed: figures) — verdict INGEST (re-read)

- Read: Figs. 1-3 as images (native extractions + page render). Receipt `sciA_29808465_1.json` (`FTR-20261004-29808465-03`, complete over cumulative coverage). Manifest new, PASS 0 gaps. Dossier `fulltext_dossiers/PMID29808465.md`.
- **CLAIM 019 severity does not rest on an unrendered figure** — it rests on clinical text; nothing changes there.
- **Selection premise wrong:** "Q230P sisters" — text and pedigree say **cousins** in two related consanguineous families. CLAIM 019, PAPER 041 and DL-MECH-029 carry "sisters".
- **Narrowing (MAJOR):** "normal transcript" is "comparable to three non-fibroblast lines (two cancer, HEK293), no control fibroblast, no dispersion". Protein absence holds; the patient lane is the most heavily loaded.
- Carrier parents: "(data not shown)", no phenotype — nothing for CLAIM 032.
- Candidate: `CC-20261004W12-A-Q230P-01` (MAJOR; 3 ops CLAIM 019, 4 ops PAPER 041; 7 triples).

## 2 · PMID 31353122 — Mori 2019 (owed: figures) — verdict INGEST (re-read)

- Read: Figures 2 (EEG) and 3 (clinical course) as page renders; Figure 1 is a facial photograph, not opened (so still partial). Receipt `sciA_31353122_1.json` (`FTR-20261004-31353122-02`).
- **Answer:** the carrier phenotype is not a WWOX datum. Figure 3 adds extra-neural events (airway malformation with tracheostomy, ductus closure, a gastrostomy shown only in the figure); spasms ceased and the last EEG was normal. Features no WWOX series attributes to WWOX → contiguous-gene reading (INFERENZA). CLAIM 032 (a) **holds**.

## 3 · PMID 32081867 — Bacchelli 2020 (owed: supplement) — verdict INGEST (re-read)

- Read: Supplementary Methods in full, all 30 Figure S1 panels (contact sheets), Table S3 cell-wise (897 rows), Table S6. Receipt `sciA_32081867_1.json` (`FTR-20261004-32081867-02`, complete over cumulative coverage).
- **Answer:** "without psychiatric history" was **assumed by recruitment, not examined** — controls came from a headache centre for a nicotine-dependence genetics study, with no assessment described. Neither WWOX-interval CNV was qPCR-validated; exactly two Table S3 rows overlap WWOX (the held case and control). CLAIM 032 (c) **holds by measurement**. Source defect: sheet titles are off by one (S3 titled "Table S2", S6 titled "Table S5").

## 4 · PMID 40191585 — Robertson 2025 (owed: supplement) — verdict INGEST (re-read)

- Read: all supplement legends; Notes 1-2 and Tables S2-S5 by term search; Figures S1-S11 at overview resolution (so still partial). Receipt `sciA_40191585_1.json` (`FTR-20261004-40191585-02`).
- **Answer:** the 172-carrier endpoint set **does not exist** — no phenotype, diagnosis, zygosity or age anywhere. Figure S11's "171 UKBB" are SCN1B carriers (a count that is easy to transpose). CLAIM 032 (d) **holds**; nothing changes.

## 5 · PMID 36926521 — Colin 2023 (owed: figures, supplement) — verdict INGEST (re-read)

- Read: Figure 5 (decision tree) as image; all legends. Figures 2-4 and S2 show patient photographs and were not opened; Figure 1 and S1, S3, S4 concern named non-WWOX genes by legend (earned null). Receipt `sciA_36926521_1.json` (`FTR-20261004-36926521-02`, partial).
- **Answer:** the blood RNA assay reads the structural allele only (exon 5 skipping); the exon-1 missense has no allele-specific RNA or protein assay; Figure 5 is a proposed strategy, not a result. CLAIM 033 (a) and DL-BIO-002 **hold — nothing changes**.

## 6 · PMID 33129329 — Makii 2020 (owed: figures) — verdict INGEST (re-read)

- Read: Figure 1 c-e, 2, 3, 4, 5 as pixels → every panel now read. Receipt `sciA_33129329_1.json` (`FTR-20261004-33129329-02`, complete over cumulative coverage).
- **Answer:** no LoD, linear range, standard curve or calibrator in any panel. Protein quantities are single-lane ratios from one representative blot (0.11 → 0.25; 0.58 → 0.21 / 0.30) against an about 11-fold transcript rise. Intensity exemplars differ in pattern. CLAIM 046 **holds**; a MINOR qualification is proposed (`CC-20261004W12-A-ASSAY-01`). Earned null for the disease question.

## Answer to the Group A question

The owed sections **add no WWOX dosage datum and fire no revival trigger**. For CLAIM 032 they strengthen the existing reading by measurement rather than by absence: the contiguous-gene carrier has a multi-system phenotype; the "control without psychiatric history" is a recruitment label from a headache-centre cohort and its CNV was never validated; the biobank missense carriers have no endpoint at all. For CLAIM 019, severity does not rest on an unread figure, but the functional DATO narrows: "normal transcript" means comparable to three non-fibroblast lines with no control fibroblast (MAJOR, blind audit owed). For the genotype–mortality class nothing in these six sources changes: no death is recorded in any of them. Measured vs predicted: Q230P transcript and protein MEASURED in one fibroblast line; exon-5 structural allele RNA MEASURED in blood; exon-1 missense, `p.Glu17Lys` and every CNV carrier PREDICTED or unmeasured. No transfer across alleles.

**What would change the model:** a control-fibroblast arm for Q230P, or a phenotype readout in any exon-level WWOX deletion carrier. **What would falsify the narrowed DATO:** a published healthy-fibroblast comparison showing the Q230P transcript at a different level.

## Brief statements found wrong

- Selection row 29808465: "Q230P **sisters**" — they are **cousins** (text and pedigree); the same error sits in CLAIM 019, PAPER 041 and DL-MECH-029.
- PAPER 041 still reads "Evidence depth: abstract only" and CLAIM 019 "held here as abstract only" — stale since 2026-09-23.

## Candidates

| id | class | targets | triples |
|---|---|---|---|
| `CC-20261004W12-A-Q230P-01` | **MAJOR** | CLAIM 019 (3 ops), PAPER 041 (4 ops) | 7 |
| `CC-20261004W12-A-CARRIERS-01` | MINOR | CLAIM 032 (3 ops) | 6 |
| `CC-20261004W12-A-ASSAY-01` | MINOR | CLAIM 046 (1 op) | 4 |

No registry candidate: every PMID is already registered (re-read wave, brief item 35). DL-MECH-029's "sisters" is flagged for its append-only owner, not edited.
