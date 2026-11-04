# IT24 result (2026-11-04)

Non-canonical. Not medical advice. Baseline `main` `cceaf854`. What LEGEND now does that it did not, what it does not show, and where each piece lives.

| Package | What changed | Kind of gain | Folder |
|---|---|---|---|
| P1 | Eight signed pairs (panobinostat SIRT1-7, idronoxil CASP3) withheld after a source check: one review-table or trial-listing claim each, no primary source, no opposite sign. Named-pair table in the action refresh; the wider listing-tier rule measured only (554 pairs, 28 proposals, one hand-over) | correctness | `source_check_it24_p1_20261104`, `generation_it21_p2_20261103` |
| P2 | 93 of 115 rows IT23 called incomparable carry a structure through routes already held (89 firm), 22 unresolved; the LINCS top-20 overlap stays 0 on 136 rows | coverage | `identity_it24_p2_20261104` |
| P4 | Accession truth, 14-row opportunity table, first per-gene lists (P47T knock-in regions, mouse conditional deletions), MTBLS12344 now public (citrate and 2-hydroxyglutarate only) | data availability, not consumed by the generator | `wwox_data_it24_p4_20261104` |
| P6 | The engine already sums over every target; decomposition shows 32 target-level conflicts (9 above a 1 percent floor) and 4 handed-over compounds with several favourable targets | presentation and a stated limit; no selection change | `multitarget_it24_p6_20261104` |
| P10 | Reverse test on four cases; the own concept-id ligand was never read by the attribution screen (fixed in code, regression; stage tables not regenerated) | consumption | `reverse_it24_p10_20261104` |
| P11 | Independent verification: counts reproduced; findings applied (89 firm plus 4 weaker, salt-key defect, exclusion-key regression, conflict magnitudes) | verification | `verification_it24_20261104` |
| P12 | Provenance of the sign, not of the pair, in the EC-KG discordance reading (3 of 15 pairs looked observed only through other edges) | traceability | `relations_it23_p2_20261103` |
| P13 | Targeted scouting: G-SRS name-to-UNII route for the 22 unresolved identities (TRIAL), three data TRIALs, one WATCH, one REJECT | next step | `scout_it24_p13_20261104` |
| P15 | Dashboard readability: glance summary per investigation (question, why, evidence depth, uncertainty, next test), details on demand, origin legend and filter, English first, an untranslated source-status label fixed | presentation | `framework/scripts/repurposing_view.py`, `view/assets/` |

## What is not shown

- No new hypothesis, no selection change, no position change in the ranking. The gains are correctness, coverage, consumption and traceability; none is predictive accuracy.
- P1 effect on the engine is bounded (no chain depends on the pairs) and was not re-run; the committed stage tables pre-date it. The own-concept-ligand fix (F1) is in code and its effect is measured read-only (20 rows become weak attribution); the stage tables were not regenerated.
- P4 results come from one producer and were not independently verified; two of four metabolites failed the QC gate.
- No wet-lab measurement was made; protein or activity in a WWOX-deficient neural system still has no deposit.

## Reopening

Regenerate the stage tables with F1 and F2 (max_phase from the sibling family) and compare the HDAC5 cluster; read primary sources for the listing-tier rows that drive a proposal (first sorafenib/regorafenib ZHX2, Q6 AKT1/PIK3C3); run the G-SRS identity route on the 22 unresolved rows after reading its terms.

## P15 before and after (English page, main investigations block; counted from the generated HTML, before = `cceaf854`)

| Measure | Before | After |
|---|---|---|
| Visible words per investigation row (mean of 10) | 396 | 202 |
| Visible words in the first row | 470 | 166 |
| Visible words between the block title and the first row | 273 | 164 |
| Fields visible at once per row | 10 | 5 (question, why, depth of reading, decisive uncertainty, next test); the rest under "Scientific details of this row" |
| Origin of each row | a badge only | badge plus a three-line legend of what each origin means, and a filter (shown only when JavaScript runs; the full list is present without it) |
| Explanation of how positions are decided | a long banner before the list | collapsed under its heading; the comparison with IT20 stays visible |
| Source-status label on the English page | "esportazione non aggiornata" (Italian) | "export not up to date" (translated in five languages) |

Checked: the five pages pass the static audit; interface text complete in all five languages (1,398 keys, one new passage, no placeholder changed); the origin classes shown are the generator's (`known_in_wwox`, `generated_by_legend`, `external_transferred`), and no pathway-coverage figure is shown as benefit. Screenshots at 390 px and 1280 px were read before and after.
