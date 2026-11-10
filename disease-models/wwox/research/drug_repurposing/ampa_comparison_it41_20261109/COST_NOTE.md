# Cost note — IT41 package A (2026-11-09)

Perimeter: two delegates read from their transcripts by `session_model_census.py` (response counted once, largest output); the Orchestrator's own turns are not measured here. No spend, no service. Numbers are tokens and turns; they are not translated into any subscription share.

| Delegate | Asked, read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|
| Producer (read, tables, one targeted NBQX step, 15 corrections) | sonnet/medium, medium on every turn | 76 | 95,239 | 9,332,864 | 253,785 |
| Verifier (blind audit, recheck of substantive corrections) | sonnet/high, high on every turn | 62 | 70,647 | 8,081,133 | 239,104 |
| Total | | 138 | 165,886 | 17,413,997 | max 253,785 |

For comparison, the INV-05 package (same models) used 101 turns, 101,809 output tokens and 11,224,406 cache-read tokens; the IT39 packages 371 turns, 523,793 output and 73,757,265 cache read. This package cost about 1.6 times the INV-05 output and 1.55 times its cache read, for six newly read sources (INV-05: five) and a harder access problem (four publisher texts unreachable, so two extra search steps were spent on open routes); it stayed at about a third of the IT39 output.

What the cost bought: the verifier read the originals and caught five substantive things the producer had written (a false "different laboratories"; the unused abstracts for items called unverified; an incomplete perimeter for perampanel in slices; surmountability resting on a test of other properties; a stale "a higher concentration was not tested"), and showed the producer's premise for "A3 not triggered" was partly wrong while the conclusion stood. The producer's targeted NBQX step found the only open measurement of the NBQX kainate window. The verification of the decisive premises was not reduced.
