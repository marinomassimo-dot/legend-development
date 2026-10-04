# COMMIT CANDIDATE — CC-20261004W13-C-VPA-SURFACE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 13 2026-10-04, branch `task/sci-C-20261004w13`.
**context_policy:** `QUESTION_DRIVEN` (DL-REPO-003's surface debt was the assignment).
**Not medical advice.** Nothing here is a statement about valproate in any person.

## Target

`disease-models/wwox/research/discovery_ledger_current.md` · `DL-REPO-003`: the surface-debt sentence
added by `CC-20261004-MIRROR-34` is discharged for PMID 27188386 and the direction is replaced by a
measurement on the bytes.

## What is wrong or missing now

The record states that the ratios behind the valproate direction live in supplementary tables **absent
from this checkout**, that a digest search returned `recoverable: 0`, and that the range is therefore
"declared, not re-attestable here".

Two things have changed, both verifiable:

1. **The artefacts are no longer absent.** `evidence_presence.py --search` over the sibling worktrees
   found all three missing files as **exact SHA-256 matches** in a peer worktree
   (`agent-ad7fd468d55287609`), and `--restore` copied them to their declared paths. The tool now
   reports **5/5 present and matching** for this PMID. No acquisition route is owed; the earlier
   `recoverable: 0` was a search that did not cover the worktrees.
2. **The direction is now measured, not declared.** Supplementary Table 3 is 24 compound blocks of
   three columns (probe set, fold change, p-value) under two test-system headers. Every cell equal to
   one of the five WWOX probe set ids was mapped to its block. Seven hits, **all positive**:

   | System | Compound | Probe set | Fold | p |
   |---|---|---|---|---|
   | UKK | VPA | 219077_s_at | +2.13 | 5.4e-16 |
   | UKN1 | VPA | 223868_s_at | +1.68 | 8.5e-5 |
   | UKK | Entinostat | 223868_s_at | +1.74 | 6.0e-5 |
   | UKK | Entinostat | 219077_s_at | +1.56 | 1.6e-6 |
   | UKK | SAHA | 223868_s_at | +1.53 | 7.2e-4 |
   | UKN1 | Entinostat | 219077_s_at | +1.51 | 1.7e-9 |
   | UKN1 | Entinostat | 223868_s_at | +1.51 | 3.2e-4 |

   No WWOX probe set carries a negative fold change in any compound block, and none appears in a
   mercurial block. Supplementary Table 7 prints no fold change and no p-value, so it carries no sign;
   WWOX sits in its 800 and 1000 µM columns.

**Scope of the discharge:** PMID 27188386 only. PMID 23179753 is still artefact-short, and PMID
28001369 is still unread and paywalled.

**Transfer limit, exact:** human embryonic-stem-cell-derived test systems (UKK embryoid body to day 14,
UKN1 neural induction to day 6), valproate 0.35–1 mM, transcript only, by probe set. No protein, no
mature neuron, no WWOX allele, no patient. The two VPA rows are two probe sets in two systems — two
observations, not a replication.

## Change class

**MINOR.** A research-layer ledger entry. The lead stays `open`; its verdict, its falsifier and its
"next action" are unchanged.

## Ordering

Receipt `FTR-20261004-27188386-02` (`scratchpad/receipts_pending_w13/sciC_27188386_1.json`) first.

## Op list — `discovery_ledger_current.md` (record-scoped; dry run EXECUTED, nothing written)

```json
[
 {
  "op": "replace-within",
  "id": "DL-REPO-003",
  "old": "The manifests fingerprint the absent files, so the range is re-measurable once they are re-acquired; until then it is **declared, not re-attestable here**",
  "new": "The manifests fingerprint the absent files, so the range is re-measurable once they are re-acquired; until then it is **declared, not re-attestable here** [🔴 **DISCHARGED for PMID 27188386 on 2026-10-04 by `CC-20261004W13-C-VPA-SURFACE-01`:** the three absent files were found as exact SHA-256 matches in a peer worktree and restored to their declared paths; `evidence_presence.py` now reports 5/5 present and matching for this PMID, and no acquisition route is owed. Supplementary Table 3 was then re-measured cell-wise, mapping every cell equal to one of the five WWOX probe set ids to its compound block: seven hits, all positive — VPA 219077_s_at +2.13 (p = 5.4e-16) in UKK and VPA 223868_s_at +1.68 (p = 8.5e-5) in UKN1, plus Entinostat (four rows, +1.51 to +1.74) and SAHA (+1.53); no WWOX probe set carries a negative fold change in any compound block, and none appears in a mercurial block. Supplementary Table 7 prints no fold change and no p-value, so it carries no sign. PMID 23179753 remains artefact-short.]"
 }
]
```

Dry run: `scope 'DL-REPO-003': span 706029→711744`, `DRY RUN — nothing written; 1 op(s)`, at commit
`b07016a0`. The `old` string occurs once in the file.

## Registry records for this PMID

None owed; this is a re-read of a PMID already landed.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. Valproate raises a WWOX probe set in the embryoid-body system, by 2.13-fold at an FDR-adjusted p of 5.4e-16 | UKK    VPA (3316)         probe=219077_s_at  fold=2.1265200000000002 p=5.3745300000000004E-16  [S553] | Supplementary Table 3, UKK VPA block, row 553, `files/fulltext/PMID27188386_Shinde2016_supplement/wwox_probe_blockmap.txt`
2. Valproate raises a WWOX probe set in the neural-induction system as well | UKN1   VPA (5880)         probe=223868_s_at  fold=1.6833199999999999 p=8.5455099999999994E-5  [BC2346] | Supplementary Table 3, UKN1 VPA block, row 2346, same artefact
3. The concentration-series sheet carries probe ids and symbols but no fold change and no p-value | SHEET=Suppl. Table 7 | ROW=3 | A=350 (µM) | B=450 (µM) | C=550 (µM) | D=800 (µM) | E=1000 (µM) | F=Symbol | Supplementary Table 7, header row, `files/fulltext/PMID27188386_Shinde2016_supplement/204_2016_1741_MOESM2_ESM_xlsxdump.txt`
4. The sheet's threshold and system are declared in its own title | Supplementary Table 7 :  The significantly deregulated probe setsts by  various concentrations of VPA in UKN1 test system (Fold change ≥ ±2, FDR adjusted p Value <0.05) | Supplementary Table 7, title cell, same artefact

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261004_007` · 2026-10-04 · ACTOR_ID `scientist` (Scientist Q, batch integrator)
**Working model:** WM_v7.19 -> WM_v7.20 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit (BEFORE propagation, auditor had not seen this candidate):** 4 triples — 4 SUPPORTED, re-measured cell-wise with independent parsers
**What landed, and what the audit changed:** Five qualifications landed. The two systems raise DIFFERENT probe sets, neither appearing in the other's valproate block; a third probe up in one block carries no symbol at all in the workbook; the FDR label comes from the sheet title, not the column header; the concentration-series sheet carries symbols only for the top dose, which the paper itself calls cytotoxic; and NO surface of either paper reports valproate lowering a probe set of this gene. The four artefacts this candidate recorded as absent were recovered by SHA-256 from a peer worktree and restored digest-equal.
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record, no geography and no parent-of-origin detail is carried.
