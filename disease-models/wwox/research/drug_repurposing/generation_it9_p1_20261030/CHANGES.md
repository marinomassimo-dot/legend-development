# CHANGES: IT9 P1 seed table, v1 -> v2 (response to the verifier report 2026-10-30_it9_p1_verifier.md)

Schema: the 18 columns of seeds.tsv keep their names and order; two columns are appended (`guard_tag`, `change_ref`). Row ids S001..S111 are unchanged; 20 new rows are S112..S131 (`change_ref` ends in `+new`). `level` vocabulary unchanged (cell counts and area fractions are typed `pathology`, observation_class `cell_count` or `histology_area_or_count`). `hgnc_check.tsv` gains one column at the end (`rgd_id_ortholog_link`). New file `guards.tsv`.

## Needs-table statements that must be corrected by the batch path (needs.json was NOT edited here)

1. NEED-NEUROINFLAMMATION-GLIA, observation O1 (PMID 30290271): "Il6, not Tnf-a, is significant by qPCR. (qPCR at n 4 per group in the registry's reading.)" Paper Results 3.3 (full text re-read): ">1.5 fold upregulation of both cytokines (significant at p<.05) in KO (n=4) compared with WT (n=4)". Correct to: Il6 and Tnf-a both up. Consequence: the need's direction statement and the J01 card/need counter-evidence that relied on "Il6, not Tnf" should be re-read.
2. NEED-PDH-PYRUVATE-AXIS, observation O2 (PMID 35328751): "no PDK activity or protein is measured". The paper reports PDK activity unchanged and PDK transcript significantly higher in the knockout line (normoxia normoglycaemia, p<0.05); the line is CRISPR sgRNA 'downregulation' (the paper calls it knockout). Correct the statement; the HIF1A-PDK-PDH axis then has a third human system with PDK transcript up (non-neural).
3. NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR, observation O3 (PMID 34634460): "excitatory amplitude: slight separation only". The paper reports an increased mEPSC amplitude distribution (KS test) and more large-amplitude sEPSCs with unchanged frequency, while mean amplitudes are 23.3 v 24.7 pA; the statement should carry both the means and the distribution shift.

## Repairs (verifier item -> action)

| Item | Action |
|---|---|
| H1 | S085 TNF -> up, S086 IL6 reason corrected (both up in null hippocampus, P47T up); locators now cite paper section 3.3 |
| H2 | S081 intervention sentence and its O3 locator removed (moved to reserved S124); S067 guard sentence removed (S126 reserved add-back row); checker bans intervention terms and response-statement locators in usable rows |
| H3 | D1 split: Wnt bulk stays dropped (D1); MYC/radial-glia moved to new question Q6 (S100 and S101 usable by direction only, S102 and magnitude row reserved, cell-cycle row unusable) |
| H4 | one rule (README 3): usable = presence and direction; endpoint magnitudes and baselines reserved. Stripped from S058, S059, S077, S080, S083, S101; reserved baseline rows S119 to S123, S125, S118; S006 presence only; S075 (seizure presence) now usable, SWD magnitudes reserved |
| M1 | S030 corrected; new usable rows PDK activity unchanged and PDK transcript up (SET:PDK_FAMILY_4); knockout/knockdown wording in context |
| M2 | README 3a: single-system composition-confounded organoid rows demoted (S067, S068, S069, new GAD67 area); NPY organoid transcript admitted because the mouse agrees |
| M3 | S104 GSK3B pSer9 restored usable under new secondary question Q7 |
| M4 | S004 and S005 -> unusable (premise unread; S005 is an inference) |
| M5 | levels split: GAD1 transcript (S067) vs GAD67 area (new), NPY counts (S066) vs NPY transcript (new) |
| M6 | PVALB, NPY, GFAP, AIF1 counts/areas typed `pathology` |
| M7 | baseline vs treated split (S075/S014, S092 baseline in S123); S009 state carried by S007/S008; S110 split by species |
| M8 | S061 -> means unchanged; new row for the amplitude distribution (up) |
| M9 | S056 rewritten to the paper (drug-induced; p-IRE-1 less in WWOX-null; PERK no change by WWOX status) |
| M10 | D6 reason reworded; points at S033 |
| M11 | `guard_tag` column + `guards.tsv`; S027 phrase removed; IT7 readout rows (including S029) tagged; checker enforces |
| L1-L9 | adult-derived removed, comparator added (S001); S003 direction uncertain; S062 table note; S071 ratio typed as state; D3/D4/D6 wording scoped to 'sources read'; S110 split; RGD links added (AIF1, GFAP closed); hallmark glycolysis row added (P47T); wording of Q1/Q4 already-explored fixed |
| extra | GRIN2C, KCNA2, GRM3 transcript down in null hippocampus added as usable Q4 rows (paper section 3.5/Discussion) |

## Seed counts, usable / reserved / unusable (+ gaps), v1 -> v2

| Q | v1 | v2 |
|---|---|---|
| Q1 | 6/5/5 | 4/5/7 |
| Q2 | 17/2/4 | 20/2/4 |
| Q3 | 13/0/2 (+3 gaps) | 13/0/2 (+3 gaps) |
| Q4 | 12/5/1 | 15/8/5 |
| Q5 | 10/2/5 | 10/6/5 |
| Q6 | - | 2/2/1 |
| Q7 | - | 1/0/0 |
| D1 | 0/2/8 | 0/1/6 |
| D2 | 0/0/5 | 0/0/4 |
| D3 | 2 gaps | 2 gaps |
| D5 | 0/1/0 | 0/2/0 |
| D6 | 0/0/1 | 0/0/1 |
| total | 58/17/31 (+5 gaps) = 111 | 65/26/35 (+5 gaps) = 131 |

Rows whose class, direction, level, question or entity changed: S003, S004, S005, S061, S063, S066, S067, S068, S069, S071, S075, S080, S081, S082, S083, S085, S100, S101, S102, S104 (plus text-only edits to many others; `change_ref` marks every touched row).

## Follow-up (branch task/it9-p1n): the three needs statements were corrected

NEED-NEUROINFLAMMATION-GLIA O1, NEED-PDH-PYRUVATE-AXIS O2 and NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR O3 in `needs/needs.json` now carry the corrected readings (document locators point at this file and at the I01 card). The J01 packet/card wording ("Il6 but not Tnf-a") and the F04 packet/card wording ("separates by a sliver") were corrected and rebuilt with the bridge; the I01, E03 and F01 cards already carried the correct reading. Seeds S030, S085, S086, S112, S113, S061 and S114 already say what the corrected statements say, so no seed row changed. Historical cycle folders (IT6 P10, IT6 P9, IT8 P4 classified inputs, the 2026-10-28 needs verification) keep their original wording as a record of what was read then.
