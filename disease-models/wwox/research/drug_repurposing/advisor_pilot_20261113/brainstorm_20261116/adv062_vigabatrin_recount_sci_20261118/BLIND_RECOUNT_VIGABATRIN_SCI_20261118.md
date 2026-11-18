# ADV-062: blind recount of the vigabatrin exposure aggregates from the held per-child tables (SCI, 2026-11-18; non-canonical; aggregates only; no per-child table in this file; cells under 3 are written "fewer than 3"; hypothesis level; no dose, no schedule, no recommendation; reference genotype class only; not medical advice)

Written for: ADV (assigner) and IT (to correct its ADV-056 section 1 by dated line if this differs). **Part 1 below was written before IT's ADV-056 result or its A_ and B_ tables were opened** (the digest of this file's first version is recorded in the comparison section). **Disclosure:** earlier in the same session I had read, for another purpose, the first lines of IT's older `GROUP_RECOUNT_IT_20261116.md` (Al-Baradie Table 3: "vigabatrin is listed in 4 rows"); I did not use that figure: Table 3 was re-parsed from the held bytes below, and the two disagree.

## Tables used and the rules (fixed before comparing)
* **Table A** = `batch_sci_20261105/a1_wwox_reports/cases_a1.tsv`, my own earlier extraction (57 rows; one row per child and intervention class as printed by the source; a `same_patient_as` column). Vigabatrin rows: the rows whose intervention class is vigabatrin.
* **Table B** = Al-Baradie 2022 Table 3 (PMID 35792847; held HTML, `files/fulltext/`): previously published patients and the paper's own cohort, one row per patient, an ASMs column, no outcome column. Parsed from the bytes with the reference cell carried down over blank continuation cells; "vigabatrin exposure" = the ASMs cell names VGB or vigabatrin.
* **Rule R1 (rows and reports):** a row is one child-by-class record; a report is one source paper that contributes at least one such row.
* **Rule R2 (distinct children, Table A):** upper bound = rows linked only by definite `same_patient_as` links (a link to another table row, not "possible"); lower bound = definite plus "possible" links between table rows (union of linked rows). Links to records outside the table (another module's record, an earlier sibship report) cannot be resolved inside the table and do not reduce the counts.
* **Rule R3 (alone):** (a) alone within the four tracked classes (vigabatrin, hormonal, ketogenic diet, cannabidiol, other context): no linked row of another class; (b) strictly alone: (a) and the row states no other drug.
* **Rule R4 (response):** a response is "stated" when the table's symptomatic outcome is resolved, partial or none (not "not reported"); a response is a resolved or partial coding; a non-response is none. "Resolved" is this table's coding of controlled, not seizure freedom.
* **Rule R5 (qualified):** lower bound = rows coded partial; upper bound = every response with a printed qualifier or a clinical-only criterion (no instrument-defined sustained response).
* **Rule R6 (co-therapy):** hormonal = a linked hormonal row or the row text names prednisolone, ACTH, hormonal therapy or a steroid; phenobarbital = the row text (or a linked row's text) names phenobarbital. Rows that say "other drugs listed in the same cell, no dates" state nothing and count for neither.

## Counts
**Table A (vigabatrin)**
| Quantity | Count |
|---|---|
| vigabatrin rows | 22 |
| reports contributing rows | 10 |
| distinct children after de-duplication inside the table | **20 to 22** (lower with possible links merged) |
| alone within the four classes | 10 to 12 |
| strictly alone (no other drug stated) | fewer than 3 |
| response stated | 11 children (rows): 8 responses and 3 non-responses; 9 to 11 children have no response stated |
| responses qualified | **4 to 8 of the 8** (4 coded partial; the 4 coded resolved are all clinical-report codings; three carry an explicit qualifier: an overall response coded partial across three drugs, "controlled, not seizure freedom", breakthrough with a febrile illness later; one is a clinical cessation for at least 4 weeks with no instrument criterion; one of the partial rows was clinically controlled while video-EEG still recorded electrical attacks) |
| steroid or hormonal agent in the same children | 7 to 8 |
| phenobarbital in the same children (stated) | 4 |
| both a steroid or hormonal agent and phenobarbital | fewer than 3 |
No child in Table A has an instrument-defined, sustained response.
**Table B (Al-Baradie Table 3, parsed from the held HTML)**
| Quantity | Count |
|---|---|
| table rows parsed (patients) | 66 data rows, 46 distinct (reference, patient number) pairs (merged cells make the parse ambiguous) |
| rows whose ASMs cell names vigabatrin | 8 |
| distinct reference cells among those rows | 6 (including the paper's own cohort) |
| outcome stated | none: the table has no outcome column |
| rows with a steroid or hormonal agent in the same cell | 3 |
| rows with phenobarbital in the same cell | none stated (fewer than 3) |
**Union of A and B:** Table A already carries the paper's own vigabatrin rows and the rows from two of Table 3's cited reports (Shaukat 2018 and Tarta-Arsene 2017, as source papers); Table 3 cites two further reports (Mignot 2015, Serin 2018) that Table A does not. **Distinct children with vigabatrin exposure across both tables: 22 to 26** (lower: Table A's 20 plus the two Table 3 rows from reports not read in Table A; upper: Table A's 22 plus up to 4 Table 3 rows not coded in Table A, since blank reference cells in the parse leave 2 rows unattributed); **reports 10 read plus 2 cited-only**. Table B adds no response data.

## Reading of the counts (INFERENZA)
Of the 8 responses in Table A none is instrument-defined and sustained; the response rate cannot be computed (a response is stated for 11 of 20 to 22 children; selection of reported children is unknown). The conclusion "case-level data bear only reported, no more" (the sentence under test) is supported by these counts.

## Comparison with IT's ADV-056 section 1 (written AFTER Part 1; Part 1 above is unchanged; its sha256 was `c8949fff422f48bb1ad51e10509124b9f1796c7c028b2bc95534198392af6c07` when IT's file was opened; IT's text was then read only for the Answer-first item 1 and section 1)
| Cell | IT | SCI (Part 1) | Verdict and cause |
|---|---|---|---|
| vigabatrin rows and reports | 22 children in 10 reports | 22 rows, 10 reports | **agree** |
| distinct children, lower bound | 21 | 20 (Table A) | **IT right, my rule wrong**: "possible: A1-09 or A1-10" means one of the two, and my union merged the child with both; the correct lower bound is 21 |
| distinct children, upper bound | 24 | 22 (Table A); 26 (union with Table 3) | **partly different**: IT adds 2 compilation-table children to the upper bound, I allowed up to 4: two Table 3 vigabatrin rows have a blank reference cell in the held HTML and cannot be attributed from the bytes. The held sources support "24 to 26", and a lower bound of 21 (my union lower bound of 22 assumed the two named additional reports' children are new; their primary reports are unread, so identity with a Table A child cannot be excluded, IT's treatment is the better supported) |
| received vigabatrin alone | 0 | fewer than 3 (strictly alone, the one table row that lists vigabatrin as the only agent, with no statement about earlier agents); 10 to 12 alone only in the sense of no linked row of another tracked class | **different reading of "alone"**: IT 0 is right if "alone" means a documented full regimen without other agents; the held Table 3 cell lists VGB only for fewer than 3 children and says nothing about earlier or later agents; the sentence "no child received vigabatrin alone" should read "no child is documented as receiving vigabatrin alone with a known full regimen" |
| response stated | 11 of 22 (8 responses, 3 non-responses) | 11 rows (8 and 3) | **agree** |
| responses qualified | every response (8 of 8) | 4 to 8 of 8 | **agree on IT's definition** (partial, transient, or clinical-only while EEG recorded attacks; my lower bound counted only the partial codings) |
| row A response cell | "8 of 10 (partial or transient 6); non-response fewer than 3; not stated fewer than 3" | row A reports: 5 responses, **3 non-responses**, 2 not stated | **IT's cell is internally inconsistent**: 8 of 10 has the 3 non-responses inside it, and 3 is not "fewer than 3"; the 3 non-response codings all sit in row A's reports; the total (8 responses, 3 non-responses of 11 stated) is right |
| row B (Al-Baradie case series) | 4 children, controlled in 3, not stated fewer than 3 | 4 rows: 1 partial, 2 resolved (controlled), 1 not stated | **agree** |
| row C (Oliver 2023) | 8 children, phenobarbital 4, vigabatrin current at follow-up fewer than 3, stopped 6 | Table 2 cells (held XML): 8 vigabatrin-exposed patients, phenobarbital named in 4, steroid or hormonal (prednisolone or ACTH) in 2, 6 stopped and 2 continued | **agree on phenobarbital and on stopped 6 / continued 2**; IT's row C omits the 2 steroid or hormonal cells (fewer than 3; a gap, not an error) |
| steroid or hormonal agent in the same children | row A 4 (row B fewer than 3, row C not given) | rows A reports 5 to 6 (the two rows of one report may be one child, and a hormonal row linked to a vigabatrin row), Oliver 2, Al-Baradie rows 3 of 8 parsed (the paper's own cohort and cited rows, not attributable per child); union 7 to 8 | **different rule**: IT counts the hormonal agent only when the vigabatrin row's own text states it (4); I also count a hormonal row linked by `same_patient_as`. The same-row reading is the stricter one; the linked-row reading is what the held links support if the link is definite. Both are defensible: the aggregate should say "4 stated in the same row, up to 8 counting linked rows" |
| phenobarbital in the same children | row A 4, row C 4, row B fewer than 3 | non-Oliver rows 4, Oliver 4 (Table 2 "PHB"), none stated in the Al-Baradie rows: 8 | **agree** (my Part 1 R6 wrongly counted the Oliver Table 2 cells as stating nothing: they list the agents; corrected here: Oliver contributes 4 phenobarbital, 2 steroid or hormonal, 1 both) |
| both a steroid or hormonal agent and phenobarbital | not given | fewer than 3 (1 in the Oliver cells, 1 in the other rows) | not comparable |
## Which reading the held sources support, and what changes
IT's headline holds: **"case-level data can bear only reported"** (22 children, 10 reports, 8 responses of 11 stated, all qualified, no instrument-defined sustained response, co-therapy in all but fewer than 3). Three wording changes for IT's section 1: (1) the lower bound stays 21 (not 20); the upper bound is 24, and up to 26 if two unattributed Table 3 rows are new children; (2) "no child received vigabatrin alone" to "no child is documented as receiving vigabatrin alone with a known full regimen (fewer than 3 children have vigabatrin as the only agent listed)"; (3) row A's response cell has 3 non-responses, not "fewer than 3", and the "8 of 10" counts them. IT's row C steroid or hormonal count (2) can be added. Nothing changes the harm-heavy comparison.
**Limits:** Table A is my own earlier extraction (read at partial full text, not re-read); Table B was parsed from held HTML with merged cells; Oliver Table 2 cells were counted from the held XML; the recount is by aggregates and does not re-open any original paper; no per-child row is written here.
