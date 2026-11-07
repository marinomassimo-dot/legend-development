# IT33 P4: one premise, one investigation, for three cases (stage S13)

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class. Reference stage = the one actually current in the repository (S12, `../generation_it32_p3_20261107/results_s12/`, itself S11 plus one column), frozen before the change: 994 proposals, 220 eligible, 15 hand-overs.

## Criteria, written before the run
Measure only consumption: (1) every proposal whose mechanism chain rests on a mapped premise names the one investigation that measures it; (2) nothing else in the stage changes (ids, eligibility, hand-overs, every other column); (3) removing the added map rows removes exactly their links. No claim of WWOX specificity, superiority or predictive skill is made, so no popularity or decoy-gene control was run; if one is claimed later it needs them.

## Change (smallest link)
`../generation_it21_p2_20261103/investigation_premises_it32.tsv` now maps a regular expression on the chain to an investigation (it was a literal prefix). Three rows: INV-16 (HDAC5 to SLC2A1, from IT32), INV-14 (EZH2 to IL6 or NFE2L2 in glia), INV-17 (any chain that ends in a change of MYC; new investigation, `../ranking_it8_p9_20261029/investigations_it20.tsv`). The generator adds nothing else; it creates no investigation.

## Before and after (`test_stage_it33.py`)
| | S11 | S12 | S13 |
|---|---|---|---|
| proposals linked to an investigation | 0 | 20 | 605 of 994 |
| INV-16 / INV-14 / INV-17 | - | 20 / - / - | 20 / 30 / 555 |
| eligible among them | - | 12 | 12 / 8 / 123 |
| hand-overs carrying a link | 0 | 1 of 15 | 5 of 15 |
| ids, eligibility, hand-over list, other columns | | identical | identical |
Ablation: with the INV-14 and INV-17 rows removed the column equals S12 for every proposal (test). Not a new row, not a new combination, not a reopening and not a new hypothesis in the perimeter searched: the same 994 proposals; the one new object is a question (INV-17). Proposals are not independent: 555 proposals ending in MYC are one premise, not 555 supports.

## The three cases (the generality test)
| | HDAC5 to SLC2A1 (INV-16) | EZH2 to glial cytokines and NRF2 tone (INV-14) | change of MYC (INV-17) |
|---|---|---|---|
| starting observation | one muscle knockdown; transcript seeds in WWOX systems | cytokine and NRF2-tone seeds, mouse transcripts | MYC top raised gene in knockout radial glia, S and G2M shift (PMID 42397075) |
| role of the change | unresolved (SLC2A1 direction differs across systems) | unresolved (harm or protection of the inflammatory change) | unresolved (driver, marker or consequence) |
| biological action required | catalytic activity versus protein amount, per NB-3 and NB-3b | catalytic inhibition versus knockdown of EZH2 (one reference reports the opposite sign with another agent and siRNA) | depends on the role: a genetic lowering first; none if a marker |
| relation needed and not executed (before) | proposal to the measurement that decides it | same | same |
| counter-evidence | HDAC4 sign context-dependent; neural catalytic arm exists for other outputs | opposite sign in a related reference; Ezh1 compensates in oligodendrocytes (hazard) | SCAR12 shows MYC elevation without the composition phenotype; MYC dose two-sided in cortex |
| datum that changes the decision | SLC2A1 in a human neural cell after knockdown and catalytic-dead rescue | glial cytokines in Wwox-null versus wild-type cultures with a second chemotype and knockdown | MYC within cell-cycle strata, then genetic lowering |
The link generalises: three unrelated premises, one mechanism, no new code after the first case except the pattern type. It covers 605 of 994 proposals, which is a statement about bookkeeping coverage, not about the share that could work.

## What it does not show
No change in what is proposed, no direction chosen for MYC, no compound promoted, no statement about WWOX specificity. A scientific package on the role of MYC (NB-1) is running in another session and was not used; when it lands it updates INV-17 evidence and, if it supports a role, the proposals' arm assumptions.

Recipe: as `../generation_it30_p5_20261105/README.md`, with `--out-dir generation_it33_p4_20261107/results_s13` (propose only; the engine step is unchanged from S11); needs the local catalogue cache. The public checkout runs `test_stage_it33.py`.
