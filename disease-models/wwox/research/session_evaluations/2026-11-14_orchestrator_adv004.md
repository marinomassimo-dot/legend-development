# Session self-evaluation: ADV-004 GABA-A subtype dispute (orchestrator, 2026-11-14)

Non-canonical. Process diagnosis. Not medical advice.

## Executable verdict
LINT WARN (0 block; the warns are historical UNLINKED_SUPPORT lines); `fulltext_receipts.py verify` OK (1,949 chained, tail anchored); growth anchors PASS; `session_self_eval.py` PASS (declared gaps are other PMIDs and historical); eight staged receipts (producer 3 ending -62, verifier 5 ending -60) validated with `--check-doi`. Full release battery on the landing SHA: pending at the time of writing (it starts only after the IT session's own battery has finished; the verdict will be recorded in the task record and stays with its SHA).

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Reading | three originals read as text, Methods and every table through the Europe PMC XML; figures largely unopened (partial_fulltext_read), stated in the README Limits | partial | the figure surfaces (Hammer Figs 1-6, Ralvenius Fig 1, Jensen Figs 1-2) were never opened by anyone |
| Verification | numbers 117 of 122 correct, 5 unverifiable; IT14 table 38 of 38 rows hold (37 value rows plus the omissions row); G6 prior failed; one added partial cross-check (Fisher 2011) | strong | the five Hammer bar readings stay unresolved |
| Overstatement control | V16's first audit and then a second narrow recheck of my README: 24 rows, 8 supported, 14 overstated, 0 unsupported | informative | I wrote 14 overstated rows into a README from an already-verified audit; the recheck, not my own pass, caught "no independent replication", "potency shows no alpha-selectivity", the "38 numbers" count and the Fig 4A lumping |
| Consumption | consumer delta proposes six rows; none applied outside my own SCI47 README; the NP3P3 re-scope and the L2 wording wait for the IT Orchestrator and the presidio | partial | benefit unproven until a consumer reads it |

## Process diagnosis
* Caught by the verifier: the diazepam bar readings conflicting with Hammer's text (my producer's table had them as clean numbers); the Fisher efficacy discrepancy; two overstatements inside the verifier's own audit (clobazam "at or below 1"; potency selectivity), which the recheck then caught.
* Caught by the machine: nothing new; receipts, LINT and growth passed on the first run.
* My mistakes: wrote the README answers from the verified audit but kept three strong phrases from the producer ("laboratory-dependent", "no independent replication", "not reproduced by Hammer") that the audit did not carry; counted "38 numbers" for 37 value rows plus an omissions row; I had also assumed the staged-receipt checker took a path-only argument and needed `--artifact-root`.
* Environment: two PMC pages and one Europe PMC page returned reCAPTCHA or HTTP 500; the Europe PMC XML route worked for the papers needed.

## Micro-upgrades (the answers)
`output/apply_v16_corrections.py` and `output/apply_v16_recheck.py` (idempotent, with `--help`); the README carries the recheck result and the audit carries a dated correction line. No framework change: the lesson (a README written after a verified audit still needs its own narrow recheck, because the producer's phrases survive into it) is the same as sci51-pitfalls and ADV-001 and is recorded in memory rather than in a new gate.

## Residual debt
Battery on the landing SHA; the unlogged six exploratory search strings in `verify/queries_verifier.tsv`; the presidio and IT dispositions of the six delta rows; figure surfaces.
