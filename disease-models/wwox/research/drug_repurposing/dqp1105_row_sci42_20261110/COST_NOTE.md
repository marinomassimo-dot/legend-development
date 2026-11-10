# Cost note — SCI42 S5 (DQP-1105 row), 2026-11-10

Perimeter: two delegates read from their transcripts by `session_model_census.py`, each including its resumes. The Orchestrator's turns are not separable here. No spend, no service, no external contact.

| Delegate | Asked, read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|
| Producer (abstract-level pass, one extra open source, rewrite on the primary source) | sonnet/medium, medium on every turn | 36 | 31,380 | 1,905,295 | 96,863 |
| Verifier (blind audit, recheck of 25 changed rows) | sonnet/high, high on every turn | 48 | 60,885 | 3,987,982 | 152,185 |
| Total | | 84 | 92,265 | 5,893,277 | max 152,185 |

The package cost about a third of the main SCI42 package in cache read. What the verification bought: the producer's draft concluded "unresolved" because its own route to the primary paper was blocked; the verifier's plain request reached the paper and decided the row set (a 1000-fold unit error on two of three registry rows). The cost of that lesson was one rewrite and one recheck.
