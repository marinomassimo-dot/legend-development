# Cost note — SCI43 K+ conductance package (2026-11-10)

Perimeter: two delegates read from their transcripts by `session_model_census.py` (response counted once, largest output). The Orchestrator's own turns are not separable here (the coordinating session carried other work and was compacted): its share is not given rather than estimated. No spend, no service, no external contact; one plain retry of a rate-limited URL (HTTP 429) on the same route, then stop. Numbers are tokens and turns, not a subscription share.

| Delegate | Asked, read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|
| Producer (9 sources read, 5 tables, 28 queries) | sonnet/medium, medium on every turn | 106 | 112,017 | 18,058,810 | 318,931 |
| Verifier (blind audit, 14 corrections, 16 staged receipts) | sonnet/high, high on every turn | 86 | 124,986 | 14,620,022 | 314,816 |
| Total | | 192 | 237,003 | 32,678,832 | max 318,931 |

No resume turns: the corrections were applied by the Orchestrator and the one addition (K2P) was rechecked on the source text. For comparison, SCI42 used 157 (main), 84 (S5) and 116 (S6) turns.

What the cost bought: the verifier showed that the Orchestrator's own central inference (an implied reversal "in the K+ range") was degenerate against a smaller cell with a shunt and that the producer's absence statement about K2P tools was false because of narrow search strings; it also corrected the tau prediction of the dynamic-clamp step. No digit error in the Wwox Table 1 numbers or in the burst counts.

What it did not buy: eight of the sixteen decisive rows (the Ba2+ share, the Kv7 voltage dependence in neurons, the deep-layer Ih numbers, the Fmr1 calibration) could not be re-read by the verifier because the sources were behind rate limits or bot checks; they stay producer-read only. The Orchestrator wrote the hypotheses, the ladder, the preregistration and the Monte Carlo without an agent; no agent was used for counts or table assembly.
