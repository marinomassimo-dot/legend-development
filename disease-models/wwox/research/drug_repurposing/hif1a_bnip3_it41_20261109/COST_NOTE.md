# Cost note — IT41 package B (2026-11-09)

Perimeter: two delegates read from their transcripts by `session_model_census.py` (response counted once, largest output); the Orchestrator's own turns are not measured here. No spend, no service. Numbers are tokens and turns; they are not translated into any subscription share.

| Delegate | Asked, read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|
| Producer (read, tables, 9 audit corrections) | sonnet/medium, medium on every turn | 78 | 77,931 | 12,661,989 | 273,899 |
| Verifier (blind audit with a GEO re-derivation, recheck) | sonnet/high, high on every turn | 79 | 82,748 | 11,260,712 | 266,992 |
| Total | | 157 | 160,679 | 23,922,701 | max 273,899 |

For comparison, package A used 138 turns, 165,886 output and 17,413,997 cache read; INV-05 101 turns, 101,809 output and 11,224,406 cache read; the IT39 packages 371 turns and 523,793 output. Package B cost about the same output as A and 1.4 times its cache read; the cache read grew because the verifier re-derived the BNIP3 contrast from the public deposits (a decisive number) and both delegates held long contexts (peaks of 267,000 to 274,000).

What the cost bought: the verifier read the originals and the deposits and corrected four substantive things (the fold basis of the HT22 argument; XMU-MP-1 and EGR1 misattributed; omissions on KC7F2; an incomplete padj statement), turned the "sign depends on centring" caveat into a measured scale artefact, and added one public datum (EGR1) that the producer missed. The verification of the decisive premises was not reduced.
