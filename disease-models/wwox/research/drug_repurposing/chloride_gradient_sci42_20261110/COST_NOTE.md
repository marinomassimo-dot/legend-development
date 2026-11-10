# Cost note — SCI42 S6 (chloride gradient), 2026-11-10

Perimeter: two delegates read from their transcripts by `session_model_census.py`, each including its resumes. The Orchestrator's turns are not separable here. No spend, no service, no external contact.

| Delegate | Asked, read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|
| Producer (re-read of the source paper, five newly read sources, one more after the audit, corrections) | sonnet/medium, medium on every turn | 69 (53 first pass, 16 resume) | 92,705 | 9,222,215 | 248,224 |
| Verifier (blind audit, recheck of the changed rows) | sonnet/high, high on every turn | 47 | 85,255 | 6,431,730 | 256,473 |
| Total | | 116 | 177,960 | 15,653,945 | max 256,473 |

What the verification bought: the "native chloride" label on a pipette-set whole-cell record, a weakening outcome that contradicted a source, two inverted conditional rows and a missed mouse layer 2/3 mIPSC age series (read afterwards). The recheck found five further small errors, fixed by the Orchestrator. The package is the cheapest of the three principal SCI42 packages in output tokens; it answers with a bounded "undetermined" and an ordered measurement programme, which is what a reading package without a laboratory result can honestly give.
