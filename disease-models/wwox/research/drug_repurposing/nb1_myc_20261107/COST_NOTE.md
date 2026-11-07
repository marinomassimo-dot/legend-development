# Cost note: NB-4 delta and NB-1 against the NB-4 pilot (observable values only)

Non-canonical. Read from the transcripts with `session_model_census.py`'s deduplication (one response counted once), checked by a separate count. Tokens as logged; no conversion to a plan share, money or remaining capacity is possible from these data and none is made. Task `ORCH-NB1SCI-20261107`.

## Configuration, requested and observed

The prompt asked for a coordinator at Sonnet, effort medium, "if configurable". It is not configurable from a prompt. Observed in the coordinator transcript for the window of this session: `claude-sonnet-5-5`, effort **high** on all 29 responses. Delegates: `legend-delegate`, producers asked sonnet/medium, verifiers sonnet/high; read back in the transcripts as claude-sonnet-5-5 with effort medium x28 and x49 (producers) and high x34 and x66 (verifiers). No delegate ran another model; no escalation; no resume; one delegate active at a time (the task record's `CURRENT_PACKAGE` named the live package at each step). The transcripts show no API error, no compaction marker and no quota notice in any of the five logs; absence of a notice says nothing about the main session's remaining capacity.

## Per actor

| Actor | Birth ctx | Peak ctx | Turns | Wall | Output | Cache written | Cache read | Completed |
|---|---|---|---|---|---|---|---|---|
| Coordinator (window of this session) | n/a (long session) | 381,189 | 29 | ~36 min | 41,423 | 80,752 | 9,730,870 | briefs, mechanical checks, corrections, notes |
| A producer | 17,292 | 109,710 | 28 | ~5 min | 34,413 | 109,708 | 1,880,971 | README, 21 rows, 12 queries, 2 receipts |
| A verifier | 17,989 | 105,088 | 34 | ~5 min | 35,823 | 96,603 | 2,191,267 | 21 rows + H1-H4, audit file |
| B producer | 17,357 | 186,856 | 49 | ~10 min | 70,063 | 178,371 | 4,757,545 | README, 41 rows, chain 10, levers 2, 26 relations, 25 queries, 8 receipts |
| B verifier | ~18,000 | 234,972 | 66 | ~11 min | 83,377 | 226,487 | 8,182,903 | 29 items + chain + levers + H1-H3, audit file |
| Delegates total | | | 177 | | 223,676 | 611,169 | 17,012,686 | |

## Against the NB-4 pilot (same settings, same agent type)

| | Pilot producer | Pilot verifier | Pilot coordinator window | A producer | A verifier | B producer | B verifier |
|---|---|---|---|---|---|---|---|
| Turns | 31 | 53 | 35 | 28 | 34 | 49 | 66 |
| Output | 32,487 | 66,561 | 27,688 | 34,413 | 35,823 | 70,063 | 83,377 |
| Cache read | 2,248,353 | 5,166,594 | 7,883,241 | 1,880,971 | 2,191,267 | 4,757,545 | 8,182,903 |

Differences that bound the comparison: the pilot covered a reconciliation and two abstract-level sources (21 audited rows); package A is a delta of the same size (2 sources read as text, one page of figures viewed as an image, 21 rows) with no reproduction and no rebuild of the pilot's tables; package B is a larger literature package (8 sources, 41 rows, a chain, two levers, 29 audited items). So only A is comparable with the pilot, and a single package does not show that this scales.

## Where the cost arises

* Package A's verifier cost 34 turns and 2.19 million cache read for 21 decisive items, against 53 turns and 5.17 million for the pilot's 21 rows plus five computations: blind items with a declared decisive set, targeted section retrieval and no large metadata export were the differences. The pilot's recommended verifier restriction held in this run.
* Package B's verifier is the single largest item (8.18 million cache read, 66 turns, context to 235,000): 78 tool calls over 29 items, a chain, two levers and three H items, with two searches routes. It found 8 overshoots and one false absence wording, so the check was not redundant, and the producer-side saving available is upstream: stage-1 rows written with `role` tags and locators the verifier could check in fewer retrievals.
* The coordinator's cache read (9.73 million over 29 responses, about 335,000 per response) comes from the accumulated context of this long session, not from the work done in the window: each coordinator response costs about three times a delegate response (about 96,000). Coordination was a little over a third of the cache read logged in this session (9.73 of 26.7 million).

## One concrete correction before the next batch

Run the coordinator of a secondary batch in a fresh session (or after a handover note) instead of at the end of a long one: that alone removes the largest per-response cost without touching a scientific step. Not changed in this session because the runtime setting is not reachable from the prompt.

## Not measured

Wall-clock of the main session, the IT33 session's own consumption, and capacity left on the account. No claim is made about interference beyond: no concurrent write to the other session's worktree, no shared consumer touched, no battery started while one was running, and the battery of this package is run at low priority after the delegates have finished.
