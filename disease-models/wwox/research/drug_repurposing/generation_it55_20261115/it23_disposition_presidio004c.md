# PRESIDIO-004 part C: disposition of the IT23 symbol lookup (IT, 2026-11-15)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Operator's rule (roadmap_current.md, 2026-11-15, item 1): KEEP a conversion whose classification and provenance can be verified; DISCARD ambiguous ones; INCONCLUSIVE on the benefit of the reversal until the comparison exists. No ranking, need, candidate state or committed file was changed by this disposition.

## Evidence read
* HE's trial `it23_symbol_lookup_trial_he_20261115/` (e16c42b70): 15 of 15 converted by two agreeing routes, 0 unresolved, 0 ambiguous.
* SCI's reference `symbol_reference_presidio004b_20261115/comparison_with_he_trial.md` (branch a7ec78e2f, read from the object store): 15 of 15 agree on authors' symbol, ENSG, direction, log2FC; independence weaker than it looks (same HGNC release and authors' data); two checks outside HGNC (authors' EntrezID, authors' description column), 15 of 15.
* My re-derivation `rederive_qf.py` (this folder; standard library, offline; run `python3 -I rederive_qf.py <repo_root>`): authors' raw GEO lists by the 15 old symbols of SCI's hand-read table (not HE's output), rho from GSE150123 with the package's own definitions (copied: log2 CPM+1, mean count at least 5, Spearman against log10 day, broad class = declared markers or |rho| at least 0.4). Results: rho of all 15 rows equals HE's to three decimals; on every row of the committed table that carries a rho, my code reproduces it (0 mismatches); the broad flag changes for exactly IRAG1, POFUT4, HDIP1, H1-2, H1-10; QF_minus_broad_maturation goes from 365/260 (committed, reproduced) to 363/257. Limit: same definitions, same data; this checks arithmetic and the lookup, not whether |rho| 0.4 is a good class boundary. The primary composition class (|rho| at least 0.6) does not change: no rho of the 15 reaches 0.6 (largest 0.576).

## Disposition
| Item | Disposition | Reason |
|---|---|---|
| The 15 conversions (authors' symbol, ENSG, direction, log2FC) | **KEEP**, per row, all 15 | two agreeing routes (HE), a separate hand reading (SCI), authors' EntrezID and description (not HGNC), none ambiguous |
| The 15 rho values and the broad-class flags (5 flips, 10 unchanged) | **KEEP**, per row | HE, my re-derivation and (CCN2) the ADV-007 analysis agree |
| Ambiguous conversions | **DISCARD**: none arose | the only alias-only ambiguities (CIRSR~CIR, ZNRD2~p27 in SCI's table; five alias-hit rows outside the 15 in HE's) were not used for any conversion |
| Benefit of reversing the committed table (any effect on a compound result) | **INCONCLUSIVE** | no LINCS query was run (S8 and S9 would be the only ones to repeat; the other four queries keep their membership); an effect on a compound ranking is neither measured nor claimed; 5 of 625 genes (0.8 percent) in the one affected query |

## What this decides
* No regeneration of `composition_class.tsv`, `scenarios.tsv`, `run_facts.json` or the stored LINCS responses: the verified conversion lives in the trial folder and the dated note in the IT23 README says what the committed rows are. Regenerating would not be reversible without the service and the benefit is unmeasured.
* No query repeat is proposed now: S8 and S9 are sensitivity scenarios (ignore the broad class), the primary class and the four other queries do not move, and nothing in the repository rests a decision on S8 or S9 alone (checked in the IT23 README and scenarios table only; not an exhaustive search of every consumer).
* Revival: if a decision ever rests on S8 or S9, or the operator authorises the two live queries; then repeat only those two and read whether any compound's position changes. The trial folder remains the source of the corrected rows.
