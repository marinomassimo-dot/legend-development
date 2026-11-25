# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV275-DEPOSITS-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-275) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_adv275_20261125/RESULT_ADV275_IT_20261125.md` (one reader; four contrasts read a second time blind). **Status:** PROPOSED, for the next `BATCH_COMMIT`; to be written after the DL-REPO-003 line of `CC-20261125-ORCHESTRATOR-ADV273-INDEPENDENCE-01`, whose independence statement counts papers, not deposited tables. No registry file is edited by this act.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** One dated addition to DL-REPO-003; no status or flag change.

## 2 · Proposed line (English; the original text stays)
`discovery_ledger_current.md` DL-REPO-003, dated 2026-11-25 (ADV-275): *Deposited neural expression tables (GEO, not papers; transcript only). WWOX mRNA is higher with valproate in human neural cultures in four independent deposits (GSE129241 induced neurons added day 1, 4 against 4, 1.28-fold; GSE232218 brain organoids at 400 uM, 4 against 4, 1.41; GSE241903 spinal-cord organoids, 3 against 3, 1.91; GSE187006 forebrain organoids of two lines, 3 against 3 each, 1.50 and 1.63); a fifth deposit agrees but is one experiment with technical replicates (GSE166297). No neural contrast read, 57 in 32 deposits, calls WWOX lower. Some neural contrasts do not distinguish it from control (among them GSE305320 spinal-cord organoids, 0.88, and an HDAC inhibitor in adult mouse hippocampus and striatum, GSE185453, 0.95 and 0.88), but each has a weak exposure check, a very short exposure or an interval that includes the rise. So a system-specific transcript positive control exists; generality is neither established nor refuted. WWOX protein was not measured and proteomic repositories were not searched. The valproate "Decreases expression" annotation finds no support in a neural deposit read.*

## 3 · Statements for the blind check
1. Per-contrast ratios, arm sizes, sentinels and replicate units: `adv275_contrasts.tsv` in the origin folder; source files and SHA-256: `data_digests.tsv`.
2. Already read blind (`verify275_report_AS_DELIVERED.md`): GSE241903, GSE166297, GSE129241 day 1, GSE305320. Not read a second time: GSE232218, GSE187006, GSE185453, which the proposed line also quotes.
3. "No neural contrast calls it lower": column `series_call` of the table has no "down" and no "mixed".
4. Replicate unit of GSE232218 ("each sample is replicated 4 times") and of GSE187006 (design text silent) comes from the deposit only.
