# Session self-evaluation: IT48 pilot container and IT49 (orchestrator, 2026-11-12)

Non-canonical. Process diagnosis. Not medical advice.

## Executable verdict
Lint 0 BLOCK; growth anchors PASS; receipts 1,855 chained; self-eval tool PASS (declared gaps are historical). Batteries by SHA: 6991d539 PASS WITH SKIPS; 90cc8a91 FAIL (i18n inventory, fixed in 3870f545, that verdict stays with its SHA); the IT48 and IT49 candidates have no full release battery of their own: targeted suites, the full view suite (223 tests OK with the older Snap revision selected automatically) and the CI gate (IT47 b67d209a #672 success; 4ff3ced5 #667 success; d280c7c3 #666 FAIL for a stale generated ranking.json that I caused).

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Advisor use | A1 changed increment 1 (the sealed action differed); B1 kept it; A2 and B2 did not change increment 2 (B2 agreed only after reading my plan; A2 could not read SCI48 and was exposed to my shortlist) | partial | benefit unproven; one assessment's claim ("never executed") was partly wrong and I checked it |
| Verification | the eight SCI43 rows reread by a distinct verifier from originals (5 supported, 3 partly) | strong | my own count error (4 for 5) propagated to five places before the operator caught it |
| Consumption | SCI48 consumed with a disposition per row, engine rerun, an engine gap exposed (comparator vs probe) | partial | the engine still labels two comparators "probe" (disclosed, handed to Harness) |
| Generalisation | INV-02 case: design-only packages are not consumed | informative negative | one case, builder-scored |

## Process diagnosis
* Caught by the machine: CI regression (stale ranking.json), shareable audit (catalogue names in public text, three times), the i18n inventory suite, receipt-lineage checks (three prior_receipt declarations), the shebang/verbosity lessons did not recur.
* Caught by peers/operator: Harness (Chromium snap refresh cause), the operator (verdict count 4 vs 5, A2's missing SCI48).
* My mistakes: a `git add -A` committed a `files` symlink once (removed in the next commit); stale generated files before landing; copying a verifier's count line without checking the table.
* Environment: Snap Chromium launcher fails in turbovnc-desktop shells; fixed by auto-selection of an installed older revision.

## Micro-upgrades (the answers)
find_chromium skips a candidate that cannot start (+ regressions); generator mapping with per-row context and a reopen cell (+ tests); the five-language reader rows built from the generator mapping.

## Residual debt
CI verdict on 6882ef56 and on the IT49 landing; SCI47-B inferences unverified yet public; the engine comparator role; design-only package reader; translations unreviewed by a native speaker.
