# Cost note — SCI42 onfasprodil and NP10679 package (2026-11-10)

Perimeter: two delegates read from their transcripts by `session_model_census.py` (response counted once, largest output), each including its resume for the corrections or the recheck. The Orchestrator's own turns are not separable here: the coordinating session also carried other work before this task, so its share is not given rather than estimated. No spend, no service, no external contact. Numbers are tokens and turns; they are not translated into any subscription share.

| Delegate | Asked, read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|
| Producer (read, tables, 14 decisive rows corrected after the audit, one extra abstract opened) | sonnet/medium, medium on every turn | 84 (71 first pass, 13 resume) | 99,488 | 13,786,423 | 297,957 |
| Verifier (blind audit, recheck of the changed rows) | sonnet/high, high on every turn | 73 (61 first pass, 12 resume) | 116,691 | 14,082,655 | 336,920 |
| Total | | 157 | 216,179 | 27,869,078 | max 336,920 |

First-pass figures alone (before the resumes): producer 71 turns, 79,875 output, 10,398,840 cache read; verifier 61 turns, 95,031 output, 10,356,493 cache read.

For comparison, the IT41 packages used 138 (AMPA), 157 (HIF1A→BNIP3) and 165 (fly) turns with 165,886, 160,679 and 151,857 output tokens. This package has the same number of turns as the BNIP3 package and about a third more output, mostly on the verifier's side (a larger source set per proposition, ten sources opened, a patent, three clinical papers and a registry API check). The resume cost was low (13 and 12 turns) because the corrections were precise.

What the cost bought: the verifier found a perimeter error that changed a role statement (a second pH value for NP10679 existed in a conference abstract the producer had screened out by title), an overstatement of the proton-sensor mutants ("abolish" against ratios 2.6, 1.0 and 1.5), a provenance error (H1 and hERG values cited a paper, not "unpublished"), and showed that the Orchestrator's own design claim (a "specificity signature") rested on four unsupported presuppositions. No digit error was found in any number re-read; all substantive errors were scope, wording, provenance or perimeter. The Orchestrator wrote the minimum design itself without an agent; no agent was used for counts, conversions or table assembly.

What it did not buy: the NP10679 discovery paper (the primary source of its pH dependence) remained unreachable by open routes, so the main uncertainty is unchanged.
