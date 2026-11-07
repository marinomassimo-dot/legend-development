# NB-4 pilot: separate assessment (A to D)

Non-canonical, not medical advice. Task `ORCH-NB4PILOT-20261107`, 2026-11-07. One package, one producer, one independent verifier. A single pilot does not show that LEGEND scales; it shows what this package cost and where.

## A. What we learned scientifically

* DATO: the existing glial-Wwox tables reproduce byte for byte from the deposited matrices (4.6 s); the sample table matches GEO; the eight raw-read experiments are still not public; GEO names no animal count, pooling, library index, Cre driver or control genotype.
* DATO: the fall is real as a count in this pool (156 to 9 astrocyte-called, 193 to 1 oligodendrocyte-called, 520 to 68 excitatory); the "20- to 44-fold" rests on 9 and 1 UMI (exact interval about 10- to 43-fold and at least 7-fold; neurons 7- to 12-fold).
* INFERENZA: "glia fall deeper than neurons" is suggested (p about 0.03 for astrocytes with nuclei treated as independent, which they are not) and depends on how the classes are drawn; it is not a finding beyond this pool.
* INFERENZA: the six readings are not exclusive and none is isolated; ambient RNA is a minor share of the control signal on p1b's assumed soup fractions.
* The independent audit changed two statements that mattered: the producer's "no characterisation of the Cre line's glial recombination found" was wrong in part (a later report characterises the same line and leaves a glial subset open; it also implies the neuronal deletion may be mosaic); and the wording around the fold was stronger than the arithmetic. Result for INV-15: `CONSUMPTION_NOTE_INV15.md`.

## B. What it cost, as logged (deduplicated, one response counted once)

| Actor | Asked | Read back | Birth ctx | Turns | Wall | Output | Cache written | Cache read | Peak ctx |
|---|---|---|---|---|---|---|---|---|---|
| Coordinator (this session, window of the pilot) | not set by dispatch | sonnet-5-5, effort high x35 | n/a | 35 | ~21 min | 27,688 | 232,699 | 7,883,241 | n/a |
| Producer `legend-delegate` | sonnet / medium | sonnet-5-5 x31, medium x31 | 17,331 | 31 | 5.3 min | 32,487 | 118,670 | 2,248,353 | 118,672 |
| Verifier `legend-delegate` | sonnet / high | sonnet-5-5 x53, high x53 | 18,070 | 53 | 11.4 min | 66,561 | 171,917 | 5,166,594 | 180,402 |

Errors 0, resumes 0, compaction markers 0, escalations 0, API errors 0 in all three logs for the window. No usage-limit notice appeared. That proves nothing about the main session's remaining budget. No turn or output ceiling exists as an Agent parameter, so the brief's scope was an operational constraint, not a technical cap. The delegates are not summed with the coordinator in any plan share: no such conversion is possible from these data.

Comparison, with the differences stated: the batch of 2026-11-05/06 (21 delegates, deduplicated: 1,593 turns, 2.82 million output, 403 million cache read; the 19 over 20 turns average 82 turns, 142,760 output, 21.1 million cache read, all at effort max, general-purpose start about 40,000 tokens) covered five literature packages with 109 receipts; this pilot covered one reconciliation, two new abstract-level sources and 21 audited rows, so it is about an order of magnitude narrower and its difficulty is lower (no full text was readable). Per delegate: 42 turns, 49,500 output, 3.7 million cache read. The earlier WO-12 pair, re-measured with the deduplicating census: producer 24 turns, 22,060 output; verifier 9 turns, 11,187 output (the figures recorded in `ORCH-DELEGBUDGET-20261106` before the fix, 47 and 28 turns, were double counts and should be read as these).

The typed agent did what it was built for: birth context 17,300 to 18,100 tokens against about 40,000 for a general-purpose delegate.

## C. Interference with the main session: documented signals only

None is documented by the logs: no API error, no usage-limit notice, no compaction, no concurrent-session conflict in a worktree, and `git fetch` before landing is recorded in the task record. Signals not measurable here: the account's remaining capacity, the main session's latency. Two items to watch rather than signals: the matrix recomputation (4.6 s, negligible) and the release battery (about 55 minutes of CPU, run at low priority); a leftover reading-claim marker for PMID 25834045 was created by the producer and removed at close.

## D. What is needed before widening the next batch

* The cost concentrates in the verifier: 2.3 times the producer's cache read and a context that grew to 180,000 tokens through 53 turns and 68 tool calls (a 30,000-character metadata fetch and repeated page reads). One concrete correction: give the verifier only the decisive propositions (numbers, absence claims, inferences, any row carrying a gloss) plus a bounded sample of the plain quote checks, and tell it to fetch metadata for named PMIDs only. This run's three overshoots and both material findings came from such items, not from the plain quote checks. Measure it at the next package.
* The brief should state that an absence claim lists the search strings and a second route (here the PubMed tool's AND-only behaviour let a direct characterisation slip through).
* A runtime ceiling on turns or output is not available to the dispatcher; until it is, the scope in the brief is the only limit. Do not read the absence of a usage notice as headroom.
