# Blind locator audit, R4d lot (2026-10-22)

Two separate agents received only (proposition, quote, anchor) triples and the source files (images opened for figure items) and no dossier, note or conclusion: one for the 67 text triples, one for the 20 figure readings. 87 triples in all: 15 from PMID 35499850, 9 from 39093319, 8 from 41250984, 10 from 39439575, 16 from 39625912, 16 from 39762914 and 13 from 41999155. The auditors were told to judge each proposition against its quote alone, at word level (strength, negation, quantifier, scope words), so a proposition that borrows a subject or a predicate from the sentence next to the quote counts as NARROW.

**Result: 87 audited; presence: all 67 text quotes PRESENT in their source files, every printed label, number and p value of the 20 figure quotes visible; no UNSUPPORTED and no UNVERIFIABLE.** Text: 21 SUPPORTED, 46 NARROW, all 46 with the surrounding text not changing the meaning. Figures: 9 SUPPORTED, 11 NARROW (one of them, 41250984 entry 21, a value read differently: two activation shifts in Figure S3 panel B are about +12 and +14 mV, not near zero). Every NARROW entry was narrowed to what its quote carries before landing; all the audited entries are new in this commit, so no `contradicts_locator` object was needed (no entry already in a landed manifest was narrowed).

Kinds of narrowing, from the audit:

| Kind | Entries (examples) | Change |
|---|---|---|
| Quote cut mid-clause, claim finished by the neighbouring sentence | 39625912 entries 31, 32, 33, 35, 36; 39762914 entries 15, 20, 21, 27 | the proposition now says only what the quote says and names the continuation as sitting in the next or preceding words |
| Content not in the quote (a number, a source, a mechanism, a salt-base inference) | 35499850 entries 20, 21, 26, 28, 29, 30; 41999155 entry 34 | removed, or moved to the note as inference |
| Reader's counts and inferences the quote cannot carry | 39093319 entries 16 and 19 (82 diet rows, 21 of about 75 quinidine rows); 41250984 entry 14 (37 variant rows); 35499850 entry 25 (file list) | the locators now state only the quoted row or title; the counts live in the note as my own counts, unaudited |
| Figure wording stronger than the image | 39439575 entries 15, 16, 17, 20; 41250984 entries 19, 20, 21; 35499850 entry 31; 39093319 entry 23; 39625912 entry 37 | reworded to what the panel shows (for example: the youngest participants' standardised points are at 4 to 10, not 1; the axis ends at 6 but the highest point is about 5; "an institute" not "a hospital") |
| Half-right replacement description | 39762914 entry 23 | the two imputation rules (random control values, regression on control patients) are now named |

Judgement calls recorded by the auditor: protocol version prefixes and table or section identity were treated as anchor information; about a dozen NARROW verdicts (exclusion-list items, dose-table cells) would be SUPPORTED under a looser reading, and I narrowed them anyway because the standing rule puts scope words in the quote.
