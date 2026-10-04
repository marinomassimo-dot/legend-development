# COMMIT CANDIDATE — CC-20261003W4-A-PATIENT-OVERLAP-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 4 2026-10-03, branch `task/sci-A-20261003w4`.
**context_policy:** `SOURCE_FIRST` — first pass written from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w4_A.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`paper_registry_current.md` · `PAPER 117` (Piard 2019): one field added before `LIT link`. `full_text_queue_current.md` · `FT-121`: one paragraph. (`PAPER 151` itself is created by `CC-20261003W4-A-REGISTRY-01`.)

## Finding
The single patient of Tarta-Arsene 2017 (PMID 28721938) and Patient 8 of Piard 2019 (PMID 30356099, Supplemental Table 1) agree on: both alleles (`c.173-1G>T` + `c.918del`, two variants private to these reports), the frameshift's protein designation, sex, non-consanguinity, decreased fetal movements, seizure onset at about one month, West syndrome, EEG course (initially normal background, then hypsarrhythmia persisting in sleep), MRI course (thin corpus callosum, later atrophy with midbrain/brainstem flattening), normal head circumference, and death at "almost 3" years. Tarta-Arsene is a Piard co-author. **Neither paper states the identity**; Piard does not cite the 2017 report, omits it from its literature table, and counts P8 among 20 "additional" patients. `PREMISE: INFERENZA` (reader's, strong).
This confirms the wave-2 hypothesis in the open `CC-20261003-A-PIARD-01` item (6) from the two primaries themselves, and sharpens `FT-121` from shared authorship to a source-level match. One citing source in this wave already double-cites him (PMID 36271927, myelination sentence, refs 13 and 66). Not checked here: whether pooled cohorts (`PAPER 018`, PMID 40875931) list both.

## Change class
**MINOR** — identity annotation; no claim or block changes. If the Piard wave-2 candidate is propagated first, this op's anchor (`LIT link` line) is unaffected.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` 663970a (merged into the branch, after `BATCH_20261003_002` landed): exit 0, 1 op(s), keys ['PAPER 117'])

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 117",
  "old": "**LIT link:** [[literature_tracking_log_current#LIT-0083]]",
  "new": "**Patient overlap (2026-10-03, `CC-20261003W4-A-PATIENT-OVERLAP-01`):** 🔴 Patient 8 (Supplemental Table 1: `c.[173-1G>T];[c.918del]`, non-consanguineous, West syndrome, initially thin corpus callosum then atrophy with midbrain flattening, death at almost 3 y) matches the single patient of [[paper_registry_current#PAPER 151]] (Tarta-Arsene 2017) on genotype and on every compared attribute; Tarta-Arsene is a co-author here. This paper neither cites that report nor lists it in its literature table, and counts P8 among its '20 additional' patients. `PREMISE: INFERENZA` — one patient, reported twice: the new-patient count is at most 19, and any aggregate that adds Tarta-Arsene 2017 to this cohort counts him twice.\n**LIT link:** [[literature_tracking_log_current#LIT-0083]]"
 }
]
```

## Op list — `full_text_queue_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` 663970a (merged into the branch, after `BATCH_20261003_002` landed): exit 0, 1 op(s), keys ['FT-121'])

```json
[
 {
  "op": "replace-within",
  "id": "FT-121",
  "old": "**Next action for both: a `CORPUS` placeholder, not a read.**",
  "new": "**Resolved for `PMID 28721938` (2026-10-03, intake wave 4, Scientist A):** read in full (`FTR-20261003-28721938-01`); the non-independence above is now a source-level match, not only a shared author — the patient is Patient 8 of the Piard cohort (`CC-20261003W4-A-PATIENT-OVERLAP-01`). Registry landing: `PAPER 151` / `LIT-0444` (provisional numbers, `CC-20261003W4-A-REGISTRY-01`).\n\n**Next action for both: a `CORPUS` placeholder, not a read.**"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(allele 1 is the intron-2 canonical acceptor variant | intron 2 of the WWOX gene, c.173-1G>T, was detected. | PMID 28721938, Case study; files/fulltext/PMID28721938_TartaArsene2017_JLE.txt)
(allele 2 is the exon-8 frameshift | c.918del (p.Glu306Aspfs*21), was also identified. | PMID 28721938, Case study; files/fulltext/PMID28721938_TartaArsene2017_JLE.txt)
(the family is not consanguineous | Our patient was from a non-consanguineous family. | PMID 28721938, Discussion; files/fulltext/PMID28721938_TartaArsene2017_JLE.txt)
(the patient died aged almost three | Our patient had aspiration pneumonia and died at the | PMID 28721938, Case study; files/fulltext/PMID28721938_TartaArsene2017_JLE.txt)
(Piard Patient 8 carries the same two alleles | c.[173-1G>T];[c.918del] | PMID 30356099, Supplemental Table 1, column 'Patient 8', row 'Mutation at the cDNA level'; files/fulltext/PMID30356099_Piard2019_supplement/41436_2018_339_MOESM1_ESM.xlsx)
(Piard Patient 8 died at almost three years | almost 3 y | PMID 30356099, Supplemental Table 1, column 'Patient 8', row 'Age of death'; files/fulltext/PMID30356099_Piard2019_supplement/41436_2018_339_MOESM1_ESM.xlsx)
(Piard Patient 8's EEG course | initially normal background with bilateral spikes, then hypsarrhythmia, which persisted in sleep up to the end of life | PMID 30356099, Supplemental Table 1, column 'Patient 8', row 'EEG'; files/fulltext/PMID30356099_Piard2019_supplement/41436_2018_339_MOESM1_ESM.xlsx)


## BATCH DISPOSITION — `BATCH_20261003_003` (2026-10-03, ACTOR_ID `scientist`, Scientist H), append-only

**Verdict:** PROPAGATED

**PROPAGATED.** One op on `PAPER 117`, one on `FT-121`. Blind audit 3 independently reproduced both alleles of the 2017 report, the age at death, and Piard Supplemental Table 1 cell I40/I50 for Patient 8 (`c.[173-1G>T];[c.918del]`, *almost 3 y*) from the supplement's own XLSX: 7/7 SUPPORTED. The identity stays labelled `PREMISE: INFERENZA` — neither paper states it — and the op's consequence (count the patient once; the new-patient count is at most 19) is unchanged.
