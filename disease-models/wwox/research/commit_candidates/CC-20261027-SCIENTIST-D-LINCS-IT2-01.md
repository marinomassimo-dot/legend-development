# CC-20261027-SCIENTIST-D-LINCS-IT2-01

- **Class:** ORDINARY (research layer; no consolidated baseline claim; no working-model change). **target_wm_version:** none.
- **Source:** package W3, task `SD-IT2-LINCS-20261027`, branch `task/sd-it2-lincs`: `research/drug_repurposing/gse156243/lincs_iteration2_interpretation_20261027.md` and the `lincs_it2_*` scripts and derived files beside it.
- **NOT WWOX EVIDENCE.** LINCS signatures of cancer and other cell lines; a knockout signature is not a rescue or variant-specific signature; no q-value, z-sum or rank is efficacy. Class level, not medical advice.

## What changes in the record
1. **The shuffled-direction control of iteration 1 was a client-side defect, not an unexplained service outcome.** Hyphen-stripped entity ids were sent; with the ids restored the control returns full rankings. The README row "LINCS / SigCom / iLINCS" of `drug_repurposing/README.md` should read, in substance: *one signature family fills both tails of the S1 ranking (61 and 59 of 100); with the direction pattern destroyed or the gene content matched, the family disappears (0 to 3.5 percent), so its concentration depends on the S1 up/down pattern; it is not a reversal list (both tails), most top reversers are frequent hitters, and a within-KO split of the same libraries reaches the same top score (-16.3 against -16.65); inconclusive, limit named*. Requested edit: the Orchestrator's (README measured-state table), not made here.
2. **The "7 signatures with q < 0.05" and the "100 requested, 50 returned" statements are re-qualified**: the cap belongs to the L1000FWD `topn` endpoint (direct call: 50 and 50, identical ranking), the `similar` tail has 40 q < 0.05 hits that iteration 1 never read, and a KO-library split (K1) returns 47 and 50, so the count is a property of the gene set.
3. **No change to any HYP, card, mechanism-map row or queue.** Section 5 of the note compares Chain D (Wnt), HYP-20261026-10, HYP-20261026-11 and N-07 with the interpretable results and finds *no usable information* for each (neither a hypothesis nor counter-evidence). TWS-119 (GSK3 beta inhibitor, ChEMBL activities) is S1's rank-3 SigCom reverser, the opposite side from what Chain D predicts for a Wnt activator, inside a family that fills both tails: a note, not a counter-claim.
4. **Harness changes landed on the task branch (T0, section 21e):** `framework/adapters/chembl.py` makes a second mechanism request by `parent_molecule_chembl_id` when the first returns no row (sildenafil had been reported as `molecule_without_mechanism`; adapter selftest, `test_repurposing_adapter.py` 19 tests and `test_repurposing_join.py` 42 tests green); `gse156243/sigcom_permuted_direction_query.py` restores the hyphens before sending. New scripts have a safe `--help`.

## Owed to an independent verifier (scientist-a); the producer cannot verify itself
H-ENC (hyphenless S1 empty, hyphenated S1P/S1P2 full) from the stored IT2 files and byte counts; Table 1.3 recomputed by `lincs_it2_summarise.py`; the K1 direct result; the 129 of 134 resolution and five failures (including BRD-K09398529) against the two GEO `pert_info` tables; the TWS-119 and IWP-2 target rows in the stored ChEMBL activity files; and the judgement "adds no hypothesis" (try to find a counter-example in `derived/lincs_it2_informative_signatures.tsv`).

## Not verified / next bounded step
Identity of five BRD codes (the 2021 library's compound table needs a key); what the `MCLF*` lines are; a local permutation-null analysis of S1 against the GSE92742 level 5 signatures (several GB, not downloaded) is the route that no service limit touches. Reopening condition for any LINCS-derived lead: a second independent genotype contrast, absent from matched controls and KO splits, not a frequent hitter.

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED (research layer; `WM_v7.27` preserved)
**Batch:** `BATCH_20261019_023` (2026-10-27, MINOR, MANUAL, ACTOR_ID `integrator`, task `INT-IT2-BATCH-20261027`)

- **Verification:** `locator_audits/2026-10-27_lincs_it2_independent_verification.md` (SUPPORTED; no error changes a conclusion). Wording corrections applied: "most top reversers are frequent hitters" now reads 33 of 76 distinct reversers (43 percent; "most" holds for mimickers, 39 of 68); "129 resolved" means 97 with a compound name and 32 structure-only; the join suite has 44 tests, not 42.
- **README:** the LINCS row (and the P6 row) of `drug_repurposing/README.md` rewritten to the verified finding: the iteration-1 empty shuffled control was our request defect (hyphen-stripped ids); the 50-signature cap belongs to the L1000FWD endpoint; the content-match reading is not supported by the matched controls; no WWOX hypothesis or counter-evidence added; next step offline GSE92742. The interpretation note (`gse156243/lincs_iteration2_interpretation_20261027.md`) carries the two wording corrections.
- **Not applied:** no test yet exercises the new ChEMBL parent-id fallback branch, and a salt-form id would still miss (verifier gap, unverified); left to the author.
