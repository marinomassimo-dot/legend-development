# Brief WO-12: the stated conditions behind the GluN2B-over-GluN2A ratios of ifenprodil and Ro 25-6981

Read `../batch_sci_20261105/BRIEF_COMMON.md` first; it binds (open routes only, no e-mail address to any service, no administered-dose numbers, depth honesty, write only in your folder, stage receipts, never record them, the wording rules). `framework/protocols/delegation_budget.md` sections 2 and 7 bind you: you start no agents.

**Question (map row WO-12, reopen row NP5A2).** The module's class window of roughly 10^2 to 10^3 GluN2B-over-GluN2A selectivity rests on ifenprodil (110 versus 39,500 nM, about 359-fold; Hess 1996, PMID 8768735) and Ro 25-6981 (9 versus 52,000 nM, about 5,778-fold; Fischer 1997, PMID 9400004), compiled in a review (PMID 29446949). Do the two primary papers state one set of conditions (expression system and species, subunit combination, glycine, glutamate or NMDA, Mg2+, holding voltage, pH, polyamine or other additions, how the IC50 was defined and fitted)? Where they differ, which differences are known to move a GluN2B-NAM IC50 and in which direction, according to a primary source you read? Do the two papers measure the same quantities as the review's table (IC50 of which response, on which subunit pair)?

**Decision at stake.** Whether the 10^2 to 10^3 window is a property of the slice-relevant condition or of oocyte compilations (grade of the carried claim N17).

**Already done, cite and do not repeat.** `target_first_it15_qa_nmdar_20261101/README.md` (corrections 2 and 3) and `reopen_searches_it15_qa.tsv` row NP5A2: the numbers and the review provenance are verified; the conditions of the primary papers were not opened. Use `depth.py`-style check against the receipt ledger before reading any PMID again.

**Work, bounded.** Obtain the full text of PMID 8768735 and PMID 9400004 (open routes; if one is not reachable, say so and stop for that paper, do not substitute the review). At most three further full-text sources, only for a stated reason (a condition-dependence claim you need a primary source for). Stop when answered or exhausted.

**Deliverables, in `wo12_glun2b_conditions_20261106/output/`:** `README.md` (answer first, at most one page), `evidence.tsv` (one row per condition per paper: `row_id, paper_pmid, quantity, stated_value, locator_quote, source_depth, comparable_between_papers, note`; quotes verbatim, at most 25 words), `queries.tsv`, `receipts/` with staged receipts (suffix `30`) and `INDEX.tsv`. Label every statement DATO, INFERENZA or IPOTESI.

**Consequences fixed before you read.**
| Return | Consumer action |
|---|---|
| the two papers state the same conditions for the quantities used | the window loses its provenance caveat; N17 grade unchanged, wording note proposed |
| they differ in a named condition | the difference is listed with its known direction and source; the window is described as a compilation across conditions; N17 caveat proposed |
| a paper is unreachable or the condition is not stated | stated as such; NP5A2 stays NEEDS-DATUM |

Final message: what you completed, what you did not, what you could not reach, and the setting you ran under as you can see it.
