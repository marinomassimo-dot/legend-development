# IT18 P1 - reopen conditions reach the radar; object-named queries compared (2026-11-01)

Non-canonical research material; not medical advice. Code: `framework/scripts/scout_daily.py` (tests `test_scout_daily.py`, 69 now; 7 new).

## P1.1 Why the WATCH/reopen conditions produced no question (verified cause)
On remote main `82e795d4` the plan read 6 surfaces and 0 reopen items. Cause: the module README's CURRENT section links one package README (`evaluation_it17_p3_20261101`), which has no WATCH row; the open conditions are kept as **tables** - 8 `reopen_searches*.tsv` (column `trigger_to_reopen`, verdict NEEDS-DATUM/PARTIAL) and `decisions.tsv` of IT15 (verdict WATCH, `reopen_condition`) - and nothing read tables. Not a format change or a stale state. Fix: `parse_reopen_table` reads those tables as columns (no new regex per sentence); a row is open only while its verdict is NEEDS-DATUM, PARTIAL(LY) or WATCH and a condition is present; one `ls-tree` call finds the tables, newest 12 packages, each blob-cached. Real repository after the fix: 59 questions, 25 of them from reopen tables (before: 0 reopen, 34 others). "Condition checked, still unmet" is a valid result; the daily search does not claim any is met. Limit: a NEEDS-DATUM row whose datum was later supplied elsewhere without updating its table would still ask (e.g. NP1B4 "retry lookups after the ChEMBL service returned" was later served by the IT15-IT17 adapter work); the remedy is to update the row's verdict, which stops the question (tested), not a second ledger.

## P1.2 Queries
Old: commonest words of the prose plus a category anchor (`epilepsy neural available corrected`). New: objects the text names (gene/protein symbols, drug names by INN stem, a short method list), local labels and ions excluded, anchor kept only for a lone short acronym; falls back to the old terms when no object is found. No model, no service. Dedicated tests in `QueryObjects`.

## Comparison (declared before any hit was seen)
Questions: 10 = every third of the sorted reopen/work-order questions (`declared_questions.json`, rule inside). Same live channels (GitHub, Hugging Face, Nature via Crossref, Europe PMC), same day, 6 calls per arm per question, no errors listed. 117 distinct hits (71 old, 66 new, 20 shared). Rated blind to arm by a different actor (a Sonnet subagent that was not shown `arm_key.json`), criteria: pertinent / usable / duplicate of known / noise / insufficient (`ratings.tsv`).

| Arm | Hits | Pertinent yes | Partly | Usable | Noise | Insufficient |
|---|---|---|---|---|---|---|
| old | 71 | 0 | 0 | 0 | 27 | 2 |
| new | 66 | 0 | 12 | 0 | 29 | 4 |

Per question the new arm had at least one partly-pertinent hit on 5 of 10 (old: 0 of 10); 3 questions changed no query materially. Limits, plainly: **one rater, titles only** (descriptions were empty and the rater fetched no page), strictness so high that no hit in either arm was "yes" or "usable"; 10 questions do not show general quality; 12 partial hits come from 5 questions and the query changes there were largest (named objects: DTA-GNN, GABA-A subtype selectivity, GSK3 readouts). What it supports: naming the object removes the zero-pertinent outcome on half the questions at no cost; it does not show that the radar finds usable capabilities (0 in both arms). Noise remained about 40 percent in both arms (the anchorless short acronyms retrieve unrelated repositories); not fixed, a filter that strict would also remove unexpected finds.
