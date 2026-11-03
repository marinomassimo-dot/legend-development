# IT22 P3-D sweep: WWOX-system observations after the seed freeze that no seed, process id, origin override or question role carries

Public edition, WWOX-DEE genotype class, no individual-level record. Not medical advice. Non-canonical research material. Nothing existing was edited; no e-mail, account or spend was used; no address was sent to any service.

## Method (reproducible)

Worktree: `.claude/worktrees/it22`, directory `disease-models/wwox/research/drug_repurposing/` (DR below).

1. Frozen set: `DR/generation_it9_p1_20261030/seeds.tsv` (131 rows, 2026-10-30), `process_ids.tsv`, `CORRECTION_NOTE_IT10/11/12`, and `DR/generation_it10_p1_20261031/origin_overrides.tsv` (1 row) and `question_roles.tsv` (7 questions).
2. Post-freeze window: `git log --since=2026-10-30 --format='%h %ad %s' --date=short` (346 commits), and the same filtered to `needs/needs.json`, `disease-models/wwox/registries`, `disease-models/wwox/analysis` (only receipt/derived-surface regenerations; no new observation was found there). Most IT17-IT21 commits are tooling, evaluation and view work, not WWOX-system measurements.
3. Packages read (README decision section, then tables): `p47t_it12_*`, `hif_it10_p21_*`, `product_it12_p1a_*`, `modifiers_it12_p1b_*`, `recoverable_it13_p3b_*`, `function_pharm_it14_p3_*` and `function_pharm_verify_it14_p3v_*`, `ack1_it12_mahajan_*`, `ack1_it11_p24_*`, `ack1_probes_it13_p15_*`, `recovery_it10_p23_*`, `question_it11_p22_*`, `bench_followup_it13b_*`, `hnpc_gse126075_it5_*` (RESULTS.md), `gse158684_identity_it14_p1a_*` and `gse158684_verify_it14_p1b_*` (snRNA, covered elsewhere, not ranked), `target_first_it15_qa/qb_*` and their verifiers (pharmacology, no WWOX measurement), `wwox_contribution_it15_p6_*`, `figure_audit_it12_p22_*` (non-WWOX systems), `complementary_it10_p24`/`it11_p3` (computational, no new WWOX observation). Excluded as assigned: NRF2/redox, snRNA/PV, glia/myelination, the three correction notes.
4. In-seed test for each candidate: `grep -ci '<key>' generation_it9_p1_20261030/seeds.tsv` with keys such as luciferase, HAP1, GSE298081, shHIF1, digoxin, Y287, ACK1, CTIP2, SATB2, Epas1, Ndrg1, P4ha1, Pgk1, KCl, Kv7, `gate 1`; the same keys over `generation_it10_p1_20261031/question_roles.tsv` (0 hits) and `origin_overrides.tsv`. Result is written per row in `in_seed_evidence`.
5. Numbers verified against sources: Breton 2021 Table 1 and Methods 5.3 (grep of `files/fulltext/PMID34634460_Breton2021_PMC.xml`: Vm, Rin, sag, rebound, N cells/animals, KCl internal); P47T values from `p47t_it12_20261031/results/compare_it12.tsv` and `genes_it12.tsv`; hNPC TPM from `hnpc_gse126075_it5_20261029/RESULTS.md`; HRE-luciferase from `hif_it10_p21_20261031/premises_it10_p21.tsv`; maturity slopes from `maturity_stress_check_it10_p21.tsv`; HAP1 scores from `modifiers_it12_p1b_20261031/evidence/selected_genes_qgi_fdr.tsv`; P17 gene values from `mouse_p17_hif_genes_it10_p21.tsv`.

## Not verified (stated in the rows where it applies)

Burst counts 36/42, 4/23, 0/11 and the Fisher p values (taken from seed S119 and the P3 package; the Breton text grep did not return them); RC1 bar values (read by eye by the package); PMID 25012504 and 35328751 primary text (relayed through package tables, not re-read); Mahajan figures (read through the orchestrator's verdict table only); Steinberg 2026 supplement (not available); GEO/PMC pages not re-fetched.

## Caveats on use

D08, D13 (and D06's A51 arm) are intervention responses; the seed policy holds those out (`RESERVED_INTERVENTION_RESPONSE`), so they should enter only as evaluation lines. The ranking is by expected effect on generation, not by strength of evidence. D01 and D02 act as corrections to existing usable rows (S017-S025, S128) and are written as proposed rows with temporary ids `N22-D..`.
