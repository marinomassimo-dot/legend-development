# SCI45 queue Q1 — consumer delta (proposals only)

| # | Consumer | Change proposed | Source rows |
|---|---|---|---|
| 1 | `compound_view.tsv` / IT44 pointers (`pointers_it44.tsv`) | ONO-TR-772: role probe-pointer (conditional); potency to carry 0.15-0.26 uM (not 15 nM); TREK-1/TREK-2 dual inhibitor; species label Rat unsupported (human); no pH series, no neuronal data | `output/pointers.tsv` T1; D02-D06, D12 |
| 2 | IT44 activity path / catalogue labels | Species labels of the GtoPdb rows for ONO-TR-772 (Rat), KU124 (Human) are not supported by the primary papers; keep the label out of typed roles or mark it unverified | D12 |
| 3 | `tools_roles.tsv` (SCI45 P1) and the INV-18 ladder step 3 | AVE1231 and KU124 are TASK-1 pointers of low quality (single channel, no selectivity, no pH); ML365 stays the TASK-1 probe; ONO-2920632 cannot be a restorability probe until its assay pH and an acid-pHo test exist | T3-T5; D08-D10 |
| 4 | `open_questions_map.tsv` | Add: TREK-1 Hill slope at 30-37 C (no source); ONO-TR-772 true human patch-clamp potency (15 nM vs 0.15 uM); pH dependence of any K2P tool. Closed: the pointers of S11/P1 now have a primary read (Cpd8l abstract only) | D02, D11 |
| 5 | SCI45 P1 `size_check_imin` and hypotheses KP1/KP4 | TREK-1 Imin 0.25 (Bagriantsev 2011 Supp Table S1): the pH route is a partial contributor at best | `trek1_ph_slope.tsv` V6-1 |
| 6 | Receipts | 5 producer (`-86`) and 7 verifier (`-85`) staged receipts; `prior_receipt` set by the verifier to the producer's ids; none recorded | `output/receipts/`, `verify/receipts/` |
