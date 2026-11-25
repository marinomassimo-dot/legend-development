# Read-back of the batch 2 delegates (IT successor, 2026-11-25)

Source: `python3 framework/scripts/session_model_census.py --json --dir <session>/subagents` (one response counted once). All four were dispatched as `legend-delegate`, **asked: sonnet, effort high stated in the dispatch** (the Agent tool has no effort parameter). A delegate's own statement about its setting is not the record; the transcript is.

| Call | Statements | Report | Model read back | Effort read back | Turns | Output tokens | Cache read |
|---|---|---|---|---|---|---|---|
| B (U1-U8) | 8 | VERIFIER_REPORT_AS_DELIVERED_BATCH2B | claude-sonnet-5-5 | high on 25 of 25 | 25 | 27,936 | 1,751,004 |
| C (U9-U16) | 8 | ..._BATCH2C | claude-sonnet-5-5 | high on 42 of 42 | 42 | 28,217 | 3,083,317 |
| D (B1-B8) | 8 | ..._BATCH2D | claude-sonnet-5-5 | high on 44 of 44 | 44 | 47,064 | 3,375,252 |
| E (I1-I3, P1, P2, R3, R2) | 7 | ..._BATCH2E | claude-sonnet-5-5 | high on 70 of 70 | 70 | 49,095 | 7,154,313 |

Call A (the second blind check of the three held-back sentences and the ADV255/ADV253 review statements) was run by the predecessor: `VERIFIER_REPORT_AS_DELIVERED_BATCH2A_IT_20261125.md`. One delegate was active at a time. The four statement files are `statements_batch2b.tsv` to `statements_batch2e.tsv` (the file letters follow the report letters; `statements_batch2a.tsv` is the predecessor's).
