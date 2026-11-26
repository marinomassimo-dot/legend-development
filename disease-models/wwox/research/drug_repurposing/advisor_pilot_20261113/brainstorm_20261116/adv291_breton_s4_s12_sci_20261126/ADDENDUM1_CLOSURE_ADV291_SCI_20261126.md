# ADV-291 addendum 1: closure asked by ADV (SCI window 9bb60ab5, 2026-11-26 UTC; hypothesis level; not medical advice)

## 1. ADV's decision on the firing sentence

CLAIM 021's firing sentence goes to IT in the form of section 3, item 1 of `RESULT_ADV291_SCI_20261126.md`: both facts are stated (the caption's null as printed; the plotted knockout points about 4 Hz above wild type at 60 and 80 pA; what a2 plots is not stated; a1 at 100 pA about 14.0 against 6.0 Hz) and neither is chosen. No MUST CHANGE or ADD verdict is written into the repository. It reaches IT after IT's apply report.

## 2. Consumers of the "S1 animal-level significance in 8 of 9" statement

| consumer | line | what it does | for IT |
|---|---|---|---|
| `disease-models/wwox/research/fulltext_dossiers/PMID34634460.md` | 9 (item 3, line read in its file) | states "low-frequency power versus coupling index uncorrelated, animal-level significance in 8 of 9 for delta" | section 3, item 5 of the result (replace the second half); dated |

No other tracked file carries it. Search, 2026-11-26: `git grep -niE` over all tracked files (this folder excluded) for "animal-level significance", "significant or significance in 8 or eight", "8 or eight (of or out of) (the) 9 or nine" next to delta, coupling, animal, subject, mice or PAC, and "8/9" next to "for delta" or "of the subjects". One other hit is unrelated (an ethosuximide count in `repurposing_10h_scientist-b_20261021.md` line 83). No card, claim-registry line or brief carries it. Files that link the dossier (arm-table `cells*.tsv` through `build_cells.py`, `memantine_burst_kinetics_20261123/README.md`, receipt `FTR-20261019-34634460-01`) link it for other content: none of them matched the strings above. Limit: a paraphrase without a number would not be found.

## 3. S1F, a source problem (not repaired by us)

Breton 2021 Supplementary Fig. S1F contradicts itself: the caption gives rho = -0.1201 while the drawn fit line rises, and p = 0.5674 does not follow from that rho with n = 41 (two-sided p = 0.4545, recomputed 2026-11-26; S1D's 0.1283 with n = 102 gives 0.1988 as printed).

## 4. Rotation

ADV-289, ADV-290 and ADV-291 were three increments on Breton 2021. ADV accepted leaving the strand.
