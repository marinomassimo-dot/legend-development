# IT23 gene-symbol lookup, offline trial (PRESIDIO-004 part A, HE, 2026-11-15)

Non-canonical research material. Public edition (WWOX-DEE reference genotype class). **Not medical advice.** Offline, zero spend, no install, no download, no external request, **no live LINCS query**. This folder is the whole trial: deleting it undoes it. No committed file and nothing in `signature_it23_20261103/` was changed, run or regenerated.

Origin: operator instruction of 2026-11-15 recorded in `roadmap_current.md` and in `advisor_pilot_20261113/assignments/PRESIDIO-004.md`. Part B (SCI's independent manual mapping of the 15 rows) and the disposition (IT) are not part of this folder.

## What was done

`symbol_lookup_trial.py` takes each of the 834 query symbols of `composition_class.tsv` and looks for its row in the authors' list (`gse156243/derived/list_padj_le_0.05.tsv`) by two routes that must agree: (A) the symbol itself, else the previous symbols and aliases of the approved HGNC record, the logic of `gse156243/validate_symbols.py`; (B) the Ensembl gene identifier (ENSG) of the approved HGNC record (`files/geo/GSE156243/hgnc_complete_set_20261022.json`, not in git). A conversion is accepted only when both routes name the same single row. Anything else is kept with its reason (`unresolved`, `ambiguous`, `routes_disagree`), never dropped or guessed. The original symbol and the ENSG are kept on every row.

The flags are then recomputed with the reproduction script's own definitions (copied, not imported): log2FC from the authors' row, rho against log10 day from the maturation series (GSE150123, 62 samples) by ENSG, declared markers, composition class (|rho| >= 0.6 in the maturation direction), broad class (|rho| >= 0.4), L1000 space and landmark membership.

## Controls

| Check | Result |
|---|---|
| "Before" (the lookup keyed by the query symbol, as the package ran it) reproduces the committed `composition_class.tsv` | 834 of 834 rows identical in every column: the "before" side is the package's before |
| Status of the 834 rows | 819 `same_symbol`, 15 `converted_two_routes_agree`, 0 unresolved, 0 ambiguous, 0 routes disagreeing |
| Five rows whose symbol is already the authors' key, and whose HGNC aliases are other rows of the list (MAGEA2B, GPNMB, CELSR1, CACNA1A, TGFBRAP1) | kept as `same_symbol`; the alias hits are listed in `note`. A symbol-only conversion would have met 5 competing candidates there; the ENSG route resolves them |
| CCN2 | rho -0.009 reproduced from the counts; the flags are unchanged, as in the team's recalculation |

## The 15 rows, before and after (`output/before_after_converted_rows.tsv`)

| Query symbol | Authors' symbol | KO direction (query set / authors' list) | log2FC | rho vs log10 day | Composition class | Broad class |
|---|---|---|---|---|---|---|
| IRAG1 | MRVI1 | up / up | 2.21 | 0.543 | 0 -> 0 | 0 -> **1** |
| CCN2 | CTGF | up / up | 1.32 | -0.009 | 0 -> 0 | 0 -> 0 |
| DRC4 | GAS8 | up / up | 1.03 | 0.044 | 0 -> 0 | 0 -> 0 |
| MNMIP1 | SH3D21 | up / up | 1.00 | -0.248 | 0 -> 0 | 0 -> 0 |
| POFUT4 | FUT11 | up / up | 0.62 | -0.549 | 0 -> 0 | 0 -> **1** |
| MTCL2 | SOGA1 | up / up | 0.60 | 0.099 | 0 -> 0 | 0 -> 0 |
| ATOSB | FAM214B | up / up | 0.49 | 0.128 | 0 -> 0 | 0 -> 0 |
| HDIP1 | C16orf87 | down / down | -0.76 | -0.576 | 0 -> 0 | 0 -> **1** |
| BBLN | C9orf16 | down / down | -0.47 | 0.278 | 0 -> 0 | 0 -> 0 |
| ADPRS | ADPRHL2 | down / down | -0.53 | 0.058 | 0 -> 0 | 0 -> 0 |
| CIRSR | CIR1 | down / down | -0.66 | -0.317 | 0 -> 0 | 0 -> 0 |
| H1-2 | HIST1H1C | down / down | -0.56 | -0.454 | 0 -> 0 | 0 -> **1** |
| H1-10 | H1FX | down / down | -0.55 | -0.514 | 0 -> 0 | 0 -> **1** |
| H4C15 | HIST2H4B | down / down | -0.93 | -0.261 | 0 -> 0 | 0 -> 0 |
| ZNRD2 | SSSCA1 | down / down | -0.55 | -0.177 | 0 -> 0 | 0 -> 0 |

The L1000-space flag also moves 0 -> 1 for ten of the 15 rows (the old symbol is in the Broad gene table; the current one is not), and stays 0 for IRAG1, POFUT4, HDIP1, ADPRS and H4C15, whose authors' symbols are absent from it; no landmark flag changes. Full columns are in the TSV.

## Query membership (`output/query_membership_changes.tsv`)

| Query | Genes before (up/down) | After | Changed |
|---|---|---|---|
| QA_all, QC_minus_declared, QD_minus_composition, QE_composition_flipped | unchanged | unchanged | no |
| QF_minus_broad_maturation | 365 / 260 | 363 / 257 | yes: IRAG1, POFUT4 (up) and H1-10, H1-2, HDIP1 (down) leave the query |

The stored LINCS responses (`run_facts.json` `responses`) are untouched and none was run. If a regeneration were ever adopted, only `QF_minus_broad_maturation` would have to be repeated (scenarios S8 and S9); the other four queries have the same membership.

## Kept apart

| Statement | Status |
|---|---|
| The 15 default-zero rows convert to one authors' row each, by two agreeing routes, with direction agreeing with the authors' list | **observed** in this folder |
| log2FC and rho of the 15 rows were absent from the table and are now computed | **observed**; the broad-class flag moves for 5 of them |
| The composition class (primary) and the directions do not change | **observed** |
| Any effect on a compound ranking | **none claimed, none measured** (no query was run; correcting the lookup does not guarantee a change) |
| Predictive capacity | none |

## Limits

- The broad class is the sensitivity class that the package defined after seeing that the primary class held 26 genes; its membership moves by 5 genes of 834 (about 0.6%). Whether that matters for S8 and S9 is untested.
- Whether the LINCS service resolved the current symbols in the stored responses was not tested (no live query). The L1000-space flag is from the Broad gene table, not from the service.
- The rho comes from one maturation series (62 samples) and the thresholds are the package's; a rho of -0.549 or 0.543 is below the primary threshold and above the broad one by construction, not by biology.
- HGNC was read from one local release (2026-10-22); a later release may change previous symbols.
- The disposition (KEEP, DISCARD, INCONCLUSIVE) belongs to IT and is not stated here. Regenerating any committed file is IT's decision and was not done.

## Reproduce and undo

```
python3 -I symbol_lookup_trial.py <repo_root> <repo_root>/files/geo output
```

Takes about 15 s offline. Undo: delete this folder.
