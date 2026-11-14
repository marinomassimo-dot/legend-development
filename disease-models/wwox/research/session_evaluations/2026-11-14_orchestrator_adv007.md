# Session self-evaluation: ADV-007 (orchestrator, 2026-11-14)

Non-canonical. Process diagnosis. Not medical advice.

## Executable verdict
`session_self_eval.py --workspace . --disease wwox`: PASS (declared gaps listed are older reads, none from this package). Task record `ledger/tasks/orchestrator/ORCH-ADV007-20261114.json` carries LINT, quick suites and the battery on the landing SHA. No receipt staged: no paper was read, only held tables.

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Premise test | the draft's premise on the all-zero flags was wrong in kind: blanks are defaults from a symbol rename (15 of 15 blank rows), not a clean bill; computed properly the rule still gives 0, for the wrong reason (non-monotone time course) | strong | the 14 other renamed genes keep default flags in the landed IT23 table |
| First-draft reading | my first coupling summary said the median single-marker prediction (0.26) was the headline; the verifier showed a composite score projects the whole rise (+1.21 v +1.15) | corrected | none after the fix |
| Proxy | I called the mouse transcript proxy unique; the verifier showed it is unique only inside the window I chose (three rows at 70-105 percent) and it overstates H_N, so committed gene-level values are quoted where they exist | corrected | cDNA map not held |
| Verification | one blind verifier, Stage A before Stage B; 26 of 32 confirmed, 3 narrowed, 3 unverifiable, 0 contradicted; effort read back high x44 (it self-reported low; the transcript governs) | adequate | clone independence, committed P17 numbers |
| Consumption | consumer_delta.md for the integrator; SCI50 README carries a dated Update line; nothing edited elsewhere | pending | benefit unproven until IT/HE consume it |

## Process diagnosis
* Caught by the verifier, not by me: the composite projection, the window dependence of the proxy, the missing CAGE row, the permutation floor, the "360; 199" misreading.
* My mistakes: a blind spot of mine, choosing a matching window after seeing a match; an unexecuted `--help`-style cleanup left dead lines in the script (removed).
* Environment: the subagent Write of its report was refused by the harness; I placed its returned text under `verify/report.md` with a header saying so.

## Micro-upgrades (the answers)
The symbol-rename cause of blank flags is now in `output/symbol_trace.tsv`; a future composition-class run should key on ENSG, not symbol (stated in `consumer_delta.md` row 3; the generator belongs to another package and is not edited).

## Residual debt
Integrator's choice on INV-06 row 7 wording; the 14 other renamed genes' flags; replicated organoid contrast and the Ensembl cDNA map.
