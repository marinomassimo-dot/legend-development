# Independent verification of P3B-2 (LINCS context stratification, ToolUniverse L1000FWD test)

Verifier: scientist-b (did not produce the work; producer scientist-c). Package merged as db44ad48 (content commit 6b425634). Recomputed from the stored responses with an independent script; no new query sent. Exploratory; not WWOX evidence; not medical advice. A knockout signature is not a rescue signature.

## Verdicts
| # | Claim | Verdict | Basis |
|---|---|---|---|
| 1a | P1 0/25 (S0 vs S1), P4 20/25 (S3 vs S1; S2 15/25), P5 unmapped 2.16 vs 1.08 percent | SUPPORTED | recomputed: 0, 20, 15 |
| 1b | S1 top-100 reversers 74 MCLF, 61 at 4 uM / 6 h; mimickers 59 (S2 54/60, S3 60/59); S0 1/1 | SUPPORTED | recomputed exactly; 74 of 100 reverser signatures have no tissue field |
| 1c | "74 percent one signature family (MCLF lines, 4 uM, 6 h)" in tool_survey | OVERSHOOT (wording) | 74 percent is MCLF; only 61 percent are 4 uM / 6 h (65 at 4 uM, 76 at 6 h, all one library). The result file words it correctly; the survey row merges the two figures |
| 1d | Failed predictions reported as failed | SUPPORTED | P2 (second half), P3 (4 of 76 compounds, 5 percent), P6 (8 of 26, 31 percent) are marked "not held"; the P2 failure is in the half that matters |
| 1e | Predictions committed before results | SUPPORTED | 7736e2eb (22:17:34) and addendum 3303de09 (22:20:14) precede 6b425634 (22:25:30); S1P request 22:20:27, S1P2 22:21:07. Limit: the addendum is written after the stored-data readout (disclosed), and the top-40 S1 reversers were read before the predictions (disclosed) |
| 2 | S1P/S1P2 stored empty (`reversers 0, mimickers 0, results []`, maxRank 693215); "not evaluable" | SUPPORTED | both stored; arms have 0 shared entities (503/313, 509/307) and no duplicates, so shared-entity overlap does not explain the empty answer; S0 (8 shared entities) returned a ranking. Cause unexplained: uncertainty, not error. P7-P9 are correctly left unscored |
| 3 | L1000FWD: 50 returned of 100 requested, no total; q<0.05: S1 7, S0 0, S1P 0, S1P2 0; BRD codes only; no tissue; no MCLF | SUPPORTED | recomputed; 48 distinct perturbagen ids in S1; overlaps S1-S0 0, S1-S1P 1, S1-S1P2 5; cell lines 17/12/11/14 |
| 3b | "all 7 in oncology-derived lines (HCC515, MCF7, SKB, HA1E, PC3)" | OVERSHOOT (minor) | HA1E (2 of the 7) is an immortalised non-cancer epithelial line; "cancer-derived or immortalised lines" is what the data supports |
| 4 | P6 classification of the 26 non-MCLF reversers | SUPPORTED | recomputed list: 8 named antiproliferative or targeted-oncology, 7 BRD codes, 3 NPC (CNS), 8 others; a different reader could move troglitazone or UNC-669 into the first group (9-10 of 26, 35-38 percent), which still fails "mainly". Context note: 22 of 26 sit in oncology or immortalised lines at 24 h, so line context, not drug class, is the larger confound |
| 5 | "LINCS INCONCLUSIVE" and "ToolUniverse: useful use, narrow" in the capability test, tool_survey and README P6 row | SUPPORTED | follow from 1-4: S1 differs from S0 and survives marker removal, but tails are balanced, the null is not content-matched, the shuffle control is empty, no cross-tissue replicated compound. PDK2 verdict stays WATCH (tooluniverse_trial.md untouched by this package; tool_survey states "WATCH (unchanged)"). KO-not-rescue and not-Q230P stated; confounds stated: library (one 2021 library, 100 percent), dose, time, cell line, antiproliferative context; proliferation/toxicity is stated for the non-MCLF stratum, not measured |

## Error versus uncertainty
- Errors (wording only, no number wrong): 1c and 3b. Neither changes an outcome.
- Uncertainty, correctly flagged by the producer: why SigCom returns an empty ranking for shuffled sets; whether the MCLF family reflects gene-content coverage (post hoc, balanced tails are consistent with it, not proof); L1000FWD is the same data lineage, so its S1-vs-shuffle separation is a statement about the query, not an independent vote on biology; it rests on one sample per set and a truncated 50-row list with q = 1 for every S0/shuffle row shown.
- Not checked: that the tool scan found 8 names and no CLUE tool in tooluniverse 1.5.7 (needs the isolated environment); the SigCom metadata call is taken from the stored file.

## Suggested fixes (not applied; I did not edit other files)
Tool_survey row: "74 percent MCLF signatures, 61 percent of them at 4 uM / 6 h". Capability test: replace "all in oncology-derived lines" with "in cancer-derived or immortalised lines (HA1E is non-cancer)".
