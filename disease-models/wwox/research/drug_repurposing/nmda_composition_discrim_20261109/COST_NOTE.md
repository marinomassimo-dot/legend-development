# Cost note — INV-05 narrow comparison (2026-11-09)

Perimeter: two delegates read from their transcripts by `session_model_census.py` (response counted once, largest output); the Orchestrator's own turns are not measured here. No spend, no service. Numbers are tokens and turns; they are not translated into any subscription share.

| Delegate | Asked, read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|
| Producer (read, tables, 11 corrections) | sonnet/medium, medium on every turn | 57 | 59,447 | 7,320,762 | 222,723 |
| Verifier (blind audit, recheck of corrections) | sonnet/high, high on every turn | 44 | 42,362 | 3,903,644 | 166,816 |
| Total | | 101 | 101,809 | 11,224,406 | max 222,723 |

For comparison, the IT39 membrane and AMPA/NMDA packages (four delegates, same models) used 371 turns, 523,793 output tokens and 73,757,265 cache-read tokens, with peaks of 333,925 to 443,582 (`it39_science_delivery_20261108/COST_NOTE.md`). This package used about one fifth of the output and about one seventh of the cache read, with a peak context roughly half of the largest.

What the cost bought: the verifier read the originals and changed five things the producer had written (a number read from a bar graph that a table gave exactly; a species mix in the radiprodil contrast; a glycine level stated as unknown; an absence perimeter that was too narrow; a "strengthens" outcome that was unresolved). The saving came from one question, five sources, four figures viewed, no supplements, no second phase and a recheck limited to the corrections.

Closing pass (2026-11-09, after landing 38a5f73b): the same verifier, resumed, checked the five final residual edits (one number, four wordings) against the sources: sonnet/high, high on every turn, 6 further turns, output 8,281, cache read 918,155; transcript totals 50 turns, output 50,643, cache read 4,821,799, peak 194,648. The pass changed one reason (the fragility of the three-share solution is near-collinearity, not subtracted terms) and one table cell (H_total_gain "strengthened by"); no battery was repeated.
