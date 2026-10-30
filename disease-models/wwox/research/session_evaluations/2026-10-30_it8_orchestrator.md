# Session self-evaluation: iteration 8 (ORCH-ROADMAP-IT8-20261029), 2026-10-30

Part 1 (executable): `session_self_eval.py` PASS (925 chained receipts after the five P5 receipts); `fulltext_receipts.py verify` OK; LINT 0 BLOCK (existing UNLINKED_SUPPORT warnings); `growth_anchors.py check` PASS; `public_release_gate.py` 0 blocks. The final release battery result is recorded in the mandate record, not here.

Part 2 (judgement; process graded apart from outcome):

1. **Independent verification again found material defects in every package that carried a scientific premise.** P3: the type filter hid four contrary cell-level rows and "selective LDHA tool" was unsupported (LDHB never queried). P5: the claim that Sephin-1 is absent from ChEMBL was false at structure level. P9: the first group rule rewarded not having tested (ethosuximide above lithium) and apinocaltamide rested on an unmeasured T-type chain. Scout: lithium is in B3DB under its CAS number. Caught by verifiers other than the producers; all repaired before integration.
2. **A producer's own correction needed a second correction.** The IT7 "WWOX-enriched" arm was first narrowed to "four added relations"; the IT8 P4 diagnosis showed they were duplicates of edges already present. I had landed the first wording before P4 finished. Lesson: do not land a perimeter correction while the diagnosis it depends on is still running.
3. **Process errors of mine.** (a) A branch (P0c) was cut from a main that then moved, so it needed a merge instead of a fast-forward; harmless but avoidable. (b) The ranking tool picked the latest snapshot by file name; two same-day snapshots made `check` report a false difference. Repaired (append order of `changes.tsv`) with a regression test. (c) Host load from many parallel agents flaked browser tests earlier; the final runs were done alone.
4. **Scope discipline.** No claim promoted; working model unchanged; no history rewrite, visibility change, deletion, publication or spend; the view is prepared, not published.
5. **Weak answers owed.** The privacy remedies (history, visibility), licence alternatives R1-R7, the Pages enablement and the Foundation permission remain reserved to the operator; the scientific loops remain proposals, none run.

Micro-upgrade delivered (the answer, not a promise): the snapshot-order fix and its test; the gate's UUID rule and its tests; polling waits in the view tooling replacing fixed sleeps.
