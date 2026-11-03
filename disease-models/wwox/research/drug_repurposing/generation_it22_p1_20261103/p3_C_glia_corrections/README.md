# IT22 P3-C: glia/myelin knowledge and the correction notes against the generator

Not medical advice. Subject: the WWOX-DEE reference genotype class (public edition), no individual. All files here are new; no existing file was edited, no git state changed, no spend, no e-mail.

Files: `trace.tsv` (16 items: G01-G08 glia, C01-C08 corrections), `proposed_seed_rows.tsv` (8 rows, exact 20-column `seeds.tsv` schema, ids `N22-C01`..`N22-C08`), `relations_it22_c.tsv` (11 cell-relation rows: relation, from_cell, to_cell, evidence, context, source_locator, interpretation_limit).

## 1. Glia / myelin (IT14 P4, E01-E34): not consumed

- The Q5 engine seed set is `generation_it9_p2_20261030/seeds_p1/Q5_expression_tiersAB.tsv`: three genes, IL1B, IL6, TNF. The 21 Q5 seed rows reduce to those 3 (adapter_counts.json Q5: 10 usable = 1 process without members S077 + 1 unchanged S078 + 1 dropped for no ortholog link S079 + 4 pathology S080-S083 + 3 placed S084-S086; 11 not usable or reserved).
- S079 (myelin/oligodendrocyte transcript set, usable=yes) is dropped silently because `hgnc_check.tsv` holds a row for MBP only, and the adapter requires an ortholog link for every member of a non-human set. This is a composition readout (OPC up, CC1+ down, OL nuclei share down), so it must not be "repaired" by adding hgnc rows until it is re-tiered `UNUSABLE_MATURITY_OR_COMPOSITION` (G05); otherwise a composition signal would start seeding Q5 as intracellular regulation.
- Nothing from IT14 P4 reaches a generated column except the Q5 falsifier text (`run_generation_it21.py` L736). `generation_it21_p2_20261103/README.md` D1 already says "IT14 glia/myelin ... in no seed row".
- Smallest representation proposed: (a) relation TSV for cell/state/process facts (R01-R11), attached to Q5 handoff text as limits, never as a seed; (b) 8 seed rows, of which only 4 are usable and none can add a composition seed: C01-C02 MBP/CNP protein (unusable, composition), C03 SOX10 stability (unusable, preprint), C04-C05 SOX10 and MYRF transcript unchanged in human spheroids (usable null observations, kept as counter-evidence), plus the S085/S084 splits for part 2; (c) a Q5b sub-question with role `composition`, which the existing `dispose_it10.disposition` already holds (`HELD_UNTIL_COMPOSITION_RESOLVED`). Maturation block versus loss is recorded as favoured, not demonstrated.
- Kept counter-evidence: seizure/illness confound (R01, R11), DRG co-culture ratio within MBP+ cells (R03), preprint-only challenge phenotype with an unresolved text/bar mismatch (R04), human transcripts unchanged (C04, C05, R10), ambiguous snRNA composition (R09).

## 2. Correction audit

| Correction | Consumed by the path that generates proposals today? |
|---|---|
| S085 TNF null hippocampus not significant | Origin counting yes (`origin_overrides.tsv` via `dispose_it10.canonical_origins_checked`, imported by IT21); seed adapter no; displayed seed text in handoff no |
| S086 wording | datum yes (IL6 seed and origin unchanged); wording in seed text only |
| S084 n / overlap | no, and nothing numeric depends on it |
| S004 / IT12 allele wording | not needed (S004 usable=no; Q1 has no proposals) |
| Q6 data-quality note | no script reads it; 560 Q6 rows rest on one MYC pair, unaffected |
| origin_overrides.tsv | one row only; cannot remove a seed or change a z |

Seed adapter versus disposition step: `p1_adapter.py` never reads `origin_overrides.tsv`. `adapter_counts.json` records `p1_seeds_sha256 = 769523339e02...`, equal to the sha256 of the current `seeds.tsv` (checked), so the engine ran on the uncorrected seed table. The corrections exist only in the later disposition/origin step. The engine's z-scores are nevertheless numerically the same as on a corrected input, because the adapter gives every gene level 1.0 and direction `up`, and the P47T cerebellum observation (PMID 36828035) still makes TNF an up seed. They would differ only if TNF were demoted, which no note asks for.

TNF-dependent proposals (my recount from `generation_it21_p2_20261103/results/engine/contributions_p1_Q5_expression_tiersAB.tsv.gz` at the >=10 percent share rule and `proposals_it21.tsv`; the `contributing_seed_1/2` columns alone give 251 because they hold only two seeds):
- 268 of 282 Q5 rows (268 families, 251 base names) carry TNF: 99 TNF only, 45 TNF+IL1B, 94 TNF+IL6, 30 all three. 14 Q5 rows have no TNF.
- Without the override, 144 rows (73 H_HARM, 71 H_PROTECT; those with TNF and no IL6; 133 base names) would show `n_origins` 2; they show 1 today. 124 rows keep 2 through IL6 (PMID 30290271) plus P47T (PMID 36828035).
- No IT21 handoff row loses an origin (6 Q5 handoff rows: IT21P2-0195, 0221, 0236, 0296, 0374, 0388, all keep IL6 + P47T). Their `seed_generated_by` text still prints "S085 TNF ... PMID 30290271 section 3.3".
- With the same H5 sort key, 4 of 55 Q5 clusters would have a different representative uncorrected (TEK H_HARM, FGFR3, MAP3K7 and PAK2 H_PROTECT); only MAP3K7 (CEP-11981) is handed over. This is an approximation that ignores the work-done and attribution keys.
- IL1B: 87 rows (20 H_HARM, 67 H_PROTECT), no number changes. IL1B and TNF P47T cite the same PMID and level, so they count as one origin.

Fix: split S085 in the seed table (N22-C06 / N22-C07), supersede S084 context (N22-C08), print the origin per seed in `seed_generated_by`, retire the override once the split is consumed, and log override keys that match nothing.

## 3. Not verified

- Source papers were read only where the full text is in `/home/desktop/legend-development/files/fulltext/` (Repudi 2021 Brain text, Abudiab 2025 preprint text lines). Verified: E06 counts, E02 two-fold CC1 text and arithmetic, E04 no cell death, E09 n=4 v 4, E10 text, preprint 117.6 and subtle-defect lines. Figure-read values (E01, E02, E09 bars) are the evidence table's hand readings. Hussain 2019 Fig 4E, Hussain 2023, PMID 34747138 and PMID 42397075 were taken from the notes and table, not re-read.
- Whether the Q6 text/figure mismatch touches S100's MYC logFC (about 1.8, 1.65, 1.6) is undecided.
- HGNC ids for CNP, SOX10 and MYRF are left blank (not checked); context_tier for the Oli-neu row is a judgement.
- P4CD-01/02/04 (TNF-arm qualification records) were not re-opened.
- The counterfactual counts are my recomputation, not a stored table, and assume the 0.1 share rule used by IT21.
