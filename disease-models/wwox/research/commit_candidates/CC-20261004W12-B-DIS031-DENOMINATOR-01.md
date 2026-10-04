# CC-20261004W12-B-DIS031-DENOMINATOR-01 - the DRG denominator of one DIS-031 premise is wrong, and the wave-6 arm's "every dose" gains its measured form

`context_policy: QUESTION_DRIVEN` (re-read of PMID 41078870 and PMID 42422766 against DIS-031, intake wave 12, 2026-10-04, Scientist B)
**Date:** 2026-10-04 · **Change class: MINOR.** One dismissal-ledger premise is corrected and one is sharpened; the dismissal itself (neither pole is established) does not move. No `consolidated baseline` claim is touched.
**Target records:** `disease-models/wwox/research/dismissal_ledger_current.md`, record `DIS-031` (two `replace-within` ops).
Receipts: `FTR-20261004-41078870-02`, `FTR-20261004-42422766-02` (prepared, not recorded) · Manifests PASS · Dossiers `PMID41078870.md` and `PMID42422766.md`, part 2.
**Nothing here is medical advice. WWOX occurs zero times in either source; earned nulls for the gene.**

## 1 - What was measured

- **PMID 41078870 (study design, Table 1 read cell-wise from the JATS table markup).** Study 1: 1 vehicle, 2 AAVDJ, 2 AAV9 (5 animals). Study 2: 2 vehicle, 3 AAV1, 3 AAV5, 3 AAV9 (11 animals). Dosed animals: 4 + 9 = 13. The Results state that DRG at four levels "were examined in detail in the three-month study" only, and that the one finding (sacral DRG, one AAV5 animal) is the only one. The denominator is therefore **1 of the 9 dosed animals of study 2**; the four dosed animals of study 1 are outside the "examined in detail" statement. "1 of 11" matches neither 13 nor 9: 11 is the total number of animals of study 2, vehicle included.
- **PMID 42422766 (supplement, read cell-wise and as a rendered figure).** ICM study, 3 animals per group: DRG neuronal degeneration absent in all 3 vehicle animals and present in all 3 animals at each of the three dose levels (Figure S6 per-animal plot; Table S2 sacral DRG row reproduces the low-dose count). The existing wording ("found adverse findings at every dose") holds; the added numbers state it.
- **Not changed:** the premise's conclusion that neither paper contains an unmedicated arm of its own (the vehicle arm of 41078870 is itself under the steroid), and the "suggestive, not a controlled comparison" caution.

## 2 - Ops (record-scoped; `old` measured unique in `DIS-031` with the registry reader)

### Op 1 - `DIS-031`, wave-6 arm, premise (4), the denominator

- `old` (unique in `DIS-031`): `found DRG degeneration in 1 of 11 dosed animals`
- `new`: `found DRG degeneration in 1 of the 9 dosed animals whose DRG were examined in detail (the three-month study only; the one-month study's 4 dosed animals are outside that statement, and 11 is the total animal count of the three-month study, vehicle included)`

### Op 2 - `DIS-031`, wave-6 arm, premise (4), the unmedicated study's finding

- `old` (unique in `DIS-031`): `which used none and screened no antibodies, found adverse findings at every dose`
- `new`: `which used none and screened no antibodies, found adverse findings at every dose (DRG neuronal degeneration in 3 of 3 animals at each of three dose levels and in 0 of 3 vehicle animals, per its supplement Table S2 and Figure S6; 3 animals per group)`

## 3 - Defaults taken

- The two ops carry only corrected counts and their provenance; no new premise, no new revival trigger.
- 11 versus 9: the registry statement could also have meant "11 animals examined"; the source says DRG were examined in detail in the three-month study, whose dosed animals number 9, so 9 is the figure the source supports.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (DRG at four levels were examined in detail in the three-month study only | sections were examined in detail in the three-month study | Results, Toxicity endpoints, `files/fulltext/PMID41078870_Okai2025_PMC.xml`)
- (The single DRG finding was in one animal of the AAV5 group | detected only in a sacral DRG of one animal of the AAV5-treated group | Results, Toxicity endpoints, `files/fulltext/PMID41078870_Okai2025_PMC.xml`)
- (The remaining animals showed no DRG neuronal abnormality | There were no DRG neuronal abnormalities present in the remaining two AAV5 animals or in any of the animals in the AAV1- or AAV9-dose groups | Results, Toxicity endpoints, `files/fulltext/PMID41078870_Okai2025_PMC.xml`)
- (The unmedicated study states findings at all dose levels | histopathology findings were present at all dose levels and affected the DRG, TG, spinal cord, cauda equina, dorsal nerve roots, and peripheral nerves | Results, ICM and IPa safety findings, `files/fulltext/PMID42422766_Amaral2026_PMC.xml`)
- (ICM groups are 3 animals per dose level with 3 vehicle animals | `[table attestation]` Supplement Data S1, sheet Table S2, row No. Animals Examined: 2, 1, 2, 1, 1, 2, 1, 2 across male and female control, low, medium, high columns | `files/fulltext/PMID42422766_Amaral2026_supplement/mmc2_cellwise.txt`)
- (Sacral DRG neuronal degeneration: 0 vehicle, 1 and 2 at the low dose | `[table attestation]` Supplement Data S1, sheet Table S2, Dorsal root ganglion sacral, Degeneration neuronal: (0), (1), (2), (1), (0), (2), (1), (0) | `files/fulltext/PMID42422766_Amaral2026_supplement/mmc2_cellwise.txt`)
