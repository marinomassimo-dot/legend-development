# Cost note: package G (WWOX, GSK3 beta, eIF2B)

Observable values from the transcripts (deduplicated), tokens as logged, no conversion to plan share or money. Task `ORCH-GSK3EIF2B-20261107`. Configuration: producer and verifier `legend-delegate`, asked sonnet/medium and sonnet/high, read back claude-sonnet-5-5 with effort medium x58 and high x47; coordinator observed claude-sonnet-5-5, effort high on all 60 responses of the session. No error, compaction marker or quota notice in any log of the session.

| Actor | Birth ctx | Peak ctx | Turns | Wall | Output | Cache written | Cache read |
|---|---|---|---|---|---|---|---|
| G producer | 17,344 | 191,882 | 58 | ~18 min | 79,513 | 191,880 | 5,942,042 |
| G verifier | 18,112 | 183,538 | 47 | ~9 min | 56,043 | 175,053 | 5,030,877 |
| Coordinator, window of this package | n/a | 437,785 | 13 | ~27 min | 14,056 | 27,932 | 5,454,701 |

Against package B of the same session (producer 49 turns, 4.76 million cache read; verifier 66 turns, 8.18 million): G's producer was heavier on turns (58) because it ran an alignment and 68 tool calls over six sources, its verifier lighter (47 turns, 5.03 million), as the decisive-items-only rule was kept and nothing needed a second route beyond the two absence claims. Breadth differs (six sources of which two abstract-level, five tables, a residue alignment), so the comparison is indicative only.

Session total in the coordinator transcript since the first package: 60 responses, 74,128 output, 22.3 million cache read, peak context 437,785: the coordinator's per-response cost (about 420,000 cache read in this window) is about four times a delegate's, and it grows with the session. The correction proposed in `nb1_myc_20261107/COST_NOTE.md` (run the secondary coordinator in a fresh session or after a handover note) stands and is the one change with measured effect. Not measured: the other session's consumption and the account's remaining capacity.
