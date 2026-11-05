# IT29 P9: proof that two persisted IT28 challenge results are read by the generator

`framework/scripts/challenge_batch.py` checks that a returned file **names the challenge id** (traceability). That is not scientific consumption. This package shows consumption for the two IT28 results that were persisted as `class_limit` rows in `generation_it22_p1_20261103/decision_scope_it22.tsv` (HDAC4/5 needed for myelination; EZH2 inhibition and later seizure burden).

* **Persisted result:** the two scope rows whose basis begins "IT28" (from `batch_it28_p3_hdac5_20261105`, `batch_it28_p4_isr_role_20261105` and the inverse reconstruction).
* **Consumer that reads it:** `run_generation_it21.py propose` through `load_decision_scopes`, which writes the column `carried_limits` of each proposal.
* **Regeneration command:** `LEGEND_CATALOG_CACHE=<cache> python3 consumption_proof_it29.py run --engine-dir <engine dir> --p1-inputs generation_it22_p1_20261103/inputs_it22 --out <scratch>` (about 3 minutes, 4 GB cap; the engine directory is the uncommitted scratch one used for S8/S9).
* **What changes (measured 2026-11-05):** the run as committed reproduces `results_s9/proposals_it21.tsv` cell for cell (`True`); removing the two rows changes **50 proposals, in one column only (`carried_limits`)**; eligible rows 220 and 220; hand-overs unchanged (checked by the committed stage test). `consumption_diff.tsv` lists the 50.
* **Reading:** a real, bounded consumption: the result is carried as a visible limit on 50 proposals and by design does not reorder or veto them. It is not evidence that the limit is correct; that remains the abstract-level reading of the source batches.
* **What this does not show:** consumption of results that live only in prose (no table row); semantic correctness of the limit text.
