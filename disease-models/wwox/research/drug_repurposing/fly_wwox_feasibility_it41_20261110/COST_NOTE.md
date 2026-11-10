# Cost note — IT41 light queue, Wwox-loss Drosophila feasibility (2026-11-10)

Perimeter: two delegates read from their transcripts by `session_model_census.py` (response counted once, largest output); the Orchestrator's own turns are not measured here. No spend, no service. Numbers are tokens and turns; they are not translated into any subscription share.

| Delegate | Asked, read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|
| Producer (read, tables, audit corrections) | sonnet/medium, medium on every turn | 79 | 79,368 | 9,715,943 | 247,176 |
| Verifier (blind audit with an independent alignment, recheck) | sonnet/high, high on every turn | 86 | 72,489 | 11,472,000 | 256,613 |
| Total | | 165 | 151,857 | 21,187,943 | max 256,613 |

For comparison, IT41 package A used 138 turns, 165,886 output and 17,413,997 cache read; package B 157 turns, 160,679 output and 23,922,701 cache read. The light queue cost about the same as the two packages although it was asked to stay light; the extra cost came from the access problems (three stock-centre routes blocked) and from the verifier's independent alignment and its absence re-runs, which found the superseded 2005 phenotype.

What the cost bought: the verifier removed a published-looking rescue (the 2005 radiation phenotype, later attributed to background mutations), corrected a false absence ("no protein detection"), and stated the opposite light-phase sign of the two sleep datasets, which changes the first step from reproducing to reconciling. The verification of the decisive premises was not reduced.
