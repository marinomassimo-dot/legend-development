# IT30: where the functional path was interrupted, and what the adapter changes (retrospective)

Non-canonical. Not medical advice. Retrospective on inputs frozen at IT29 (the 174 evidence rows of `../phenotype_first_it29_20261105/p3_*`); no predictive claim.

## Map: capability, where it runs, result, consumer, and what was missing
| Capability | Runs in | Result | Consumer | Diagnosis |
|---|---|---|---|---|
| Target-to-need coupling from signed perturbations | `phenotype_roles_it29.py` then `repurposing_search.py --roles` | 216 signed rows over 191 families (case 1; 97 over 80 in the first IT29 count, before two NCC rows were withdrawn) | comparison, stage tables | executed and consumed; its input was a hand-curated table (knowledge present, converter signs few raw rows because actions are free text) |
| Counter-premise on HDAC class | generator `carried_limits` | carried on 30 proposals | stage S10 | executed; the text was cut at 1,600 characters (fixed, S11) |
| Compound-level effect with context | none before IT30 | none | none | **representation present (raw rows), never executed, so never consumed** |
| Lesion-class sign flips (case 2) | descriptive table | none | none | representation present, not executable (agent classes, not compounds); now three class-level questions (IT30) |
| Neonatal acquired-seizure record on bumetanide | read in IT29 package E | none | card F03 carried none of it | **executed but not consumed** (fixed: packet, card, view) |

## What the adapter changes (`compound_context_it30.py`)
| Quantity on the frozen rows | Current path | Adapter |
|---|---|---|
| Compound-only rows the target converter can use | 0 of 100 (it signs a target only when target-controlled or genetic: 54 rows) | not applicable: it does not sign targets |
| Compound rows read with their context | 0 | 53 of 119 (34 compound-theme entries); 66 rows are panels or classes and stay unattributed |
| Conditional questions for the queue | 0 | 9: 6 compound-level (2 sign flips: rapamycin, vigabatrin; 1 benefit not reproduced: bumetanide; 3 benefit with a stated limit: benztropine, clemastine, clonazepam) and 3 class-level from the case-2 lesion table (sodium-channel blockers, GABA-transaminase inhibitors, Kv7 openers) |
| Class transfers made | 0 | 0 (by rule and by test) |
| Compounds that were already stage proposals | - | 1 of 34 (phenobarbital): the stage is built from transcript chains, the evidence from pharmacology |

**What it does not show.** No new molecule, no changed ranking, no prediction that anything works. The two layers barely meet (1 of 22), which is a finding about the layers: transcript-derived proposals and literature pharmacology describe mostly different compounds. A variant "only the added data, without the new link" is the current path with the rows in the folder, which reaches 0 compound-only rows; so the gain is attributable to the link, not to new data (no row was added). Cost: one script, 7 tests, under a second to run; maintenance is the rule list for panels and classes (a regex), which will need extension when new wording appears.

**Independent set.** None exists for compound-level context effects, so no part was reserved. Rows of one study share an origin (`n_sources` is printed beside `n_rows`).
