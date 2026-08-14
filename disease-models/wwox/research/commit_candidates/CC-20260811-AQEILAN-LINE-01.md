# COMMIT CANDIDATE — Aqeilan line, three complete reads

**Candidate ID:** CC-20260811-AQEILAN-LINE-01

**Status:** committed — `BATCH_20260815_001`

**Receipts:** FTR-20260811-27308416-01 · FTR-20260811-25491415-01 · FTR-20260811-26256646-01

## Proposed canonical effect at the next lawful BATCH_COMMIT

- Upgrade `CORPUS-STUB-078`/`LIT-0101` (PMID 27308416), but classify it as commentary. Its metabolic
  observations are transmitted from primary PMID 25012504 and must not be counted as replication.
- Preserve `CORPUS P333`/`LIT-0333` (PMID 25491415) as Tier-B review, now with a complete-read receipt.
  Record the internally reversed HIF1alpha/glucose wording and the questionable Drosophila ROS
  transmission; neither creates a new DATO.
- Upgrade `CORPUS-STUB-152`/`LIT-0169` (PMID 26256646) as primary rescue-model evidence that WWOX
  re-expression suppresses osteosarcoma migration/invasion and lung metastasis. Keep the RUNX2
  mechanism tagged `INFERENZA`: no direct RUNX2 perturbation, occupancy, reporter or interaction assay
  occurs in this paper.
- Correct any metabolism synthesis that calls PMID 27308416 a second “core paper”: it is commentary
  on PMID 25012504. Preserve its value as author interpretation and pathway diagram.
- Close only the PMID 27308416 and PMID 26256646 components of `FT-047`; do not imply that the remaining
  Aqeilan structured-fulltext debt is closed.
- Carry forward the Del Mare constraints: n=5 per mouse arm, unequal intratibial endpoints, LM7
  intratibial non-result, `p=0.05` against a declared `P<0.05` threshold, absent qPCR replicate count,
  and the non-load-bearing expression-of-concern reference PMID 16223882.

**Target WM:** current at `BATCH_COMMIT` time; rebase required.

**Batch gate:** intentionally untouched.
