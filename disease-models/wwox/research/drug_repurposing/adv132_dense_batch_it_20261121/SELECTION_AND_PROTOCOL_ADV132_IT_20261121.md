# ADV-132 selection rule and protocol (IT, 2026-11-21): the densest number-bearing English-authored passages, written BEFORE the selection is run

Reference-genotype class only; page text; nothing here is medical advice. Committed before the selection script is run on the pages and before any translation.

## Selection (fixed now)
* Population: the distinct English-authored text nodes of the OWN text of the sections `overview`, `ranking`, `hypotheses`, `priorities-cur`, `priorities` and `leads` of the shareable fr page as built on `main` after ADV-131 (the detector of `repurposing_view.english_authored_node` for fr; `priorities` is read as both section ids that start with it). Passages already in the catalogue scope (the 50 of ADV-131) are excluded; so are passages shorter than 40 characters.
* Score of a passage: the number of numeric tokens plus the number of symbol tokens, both as the parity rule counts them (`parity_check.numeric_tokens` and `symbol_tokens`, summed counts). Ties are broken by painted (document) order, then by length descending.
* The 25 highest scores are the batch, in score order, numbered 51 to 75 in that order (the numbering continues the ADV-131 file). The list and the scores are written to `selected_batch3.json` before the first translation.

## Protocol (as ADV-131; changes in bold)
* Translation fr, de, es by the producer into the content catalogue; every number, name, hedge, limit and negation kept. `EN_SCOPE_SECTIONS` gains the new section ids; `en_scope.json` gains the 25 hashes.
* **Mechanical parity check (`PARITY_RULE_ADV132_IT_20261121.md`) on every row of the batch before the blind check and again after the repairs**; a flag is classified by hand as FALSE POSITIVE or REAL DRIFT; a REAL DRIFT is repaired before the blind check.
* Blind check by a different delegate (sonnet, effort high, stated in the dispatch, read back from the transcript), one at a time, pairs file only; reports persisted as delivered. A repair that changes more than a word gets a third look.
* STOP RULE (unchanged from ADV-131): CHANGED above 5 percent of the 75 rows (more than 3), or any CHANGED row that alters a number, a limit, a hedge or a negation, stops the work; repair that batch, report, no further batch. A REAL DRIFT of the parity check in a number, a limit, a hedge or a negation that the blind check passed is reported as a finding against the blind check.
* Recorded: parity flags and their classification; rates; delegate cost and minutes; whether the rejecting observation named for this trial occurred (a CHANGED row on a long number-bearing evidence sentence); painted before and after for the touched sections; one updated projection paragraph.
* Nothing beyond the 25. The ranking notice stays HE's.
