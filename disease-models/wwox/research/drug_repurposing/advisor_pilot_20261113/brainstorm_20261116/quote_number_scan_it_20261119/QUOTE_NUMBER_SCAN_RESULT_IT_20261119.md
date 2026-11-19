# ADV-089: scripted quote-and-number scan of the 26 consumed claims (IT, 2026-11-19)

Hypothesis-level working note. Reading and counting only: no registry, card, need, arm table or receipt was edited; nothing is applied. Not medical advice. Reference genotype class only.

## 1. Answer first
1. **No genuine string or number defect was found where every anchor is held.** Of 44 miss occurrences (43 distinct items) with all anchors held, all 43 were read and classified; none is a quote or number that the anchor lacks while the record presents it as the paper's: 16 are the record's own words (labels, earlier wordings, rejected wordings, a Title), 14 are values the record itself labels as read from a figure, 4 are quotes from a repository audit or manifest, 3 are search terms the record says are absent from the paper, 2 are derived counts, 4 are locator numbers (`scan_adjudication_it_20261119.tsv`, one reason per row).
2. **What the scan cannot size is the CLAIM 025 kind of defect.** That was an overshoot of wording (a Title word naming a vector, a causal verb, a quantifier without its unit), not a string or number that is absent: every word of such a sentence can be present in the paper. Presence of strings and numbers is the narrow defect; this scan finds it at close to zero here. **The decision "more audits" is therefore not settled by this scan**: the four wording audits (CLAIM 025, 021, 002, 005) each found overshoots a presence check could not have found.
3. **A found number is weak evidence; a miss is the signal.** A random two-decimal number that is not in any claim hits the claims' anchor text by chance in **12.2 percent** of tests (650 tests, 25 fixed-seed probes per claim, `scan_summary_it_20261119.json`). A number is therefore reported "found" when it occurs anywhere in an anchor text, with no check of the locus. Single-digit integers (318 occurrences) are found everywhere and are excluded from the headline.
4. **Artefact-absent, not genuine:** 46 headline and 24 boundary informative items could not be decided because at least one anchor or cited paper has no held text (section 4). They are not defects; they wait on the bytes.
5. **Ranking digest:** `ff38fcaa61295a5a` is unchanged (read from `ranking.json` summary.order_digest on the tree this note was written on, after BATCH_20261119_004 and 005; `ranking_it8.py check` reports the files current). The check was not re-run on `main` heads after this tree.

## 2. Counts (scanned text: Title, Summary, Clinical meaning and every note-like field; the Evidence-boundary fields are scanned and counted apart as "boundary")
| | Items |
|---|---|
| Claims scanned | 26 (every claim with consumers in SCI's ranked scan); anchors all held for 16, some unheld for 10 |
| Strings and numbers checked, all fields | 978 (quoted strings 208, numbers 770) |
| Headline, informative (strings and numbers with 2+ digits or a decimal) | 491 |
| of which found in the anchors (exact 374, after formatting 17, alphanumeric-only 2) | 393 |
| found only in another paper the record cites | 7 |
| non-English quoted text (a registry gloss, not testable against an English source) | 19 |
| miss, every anchor held (all classified, section 3) | 26 |
| miss, an anchor or cited paper not held | 46 |
| Boundary, informative | 169 (found 116, found elsewhere 2, non-English 9, miss all held 18, miss with an unheld anchor 24) |
Matching rules, from the strictest: whitespace-collapsed substring only (the rule of the earlier quote-check scripts); then Unicode, dash, quote and case normalisation; then letters and digits only (hyphenated line breaks). A quotation with an ellipsis is checked segment by segment. A claim number written with a decimal comma or a thousands dot is also tried in point form. Spreadsheet cells and Word files of the supplements are read, numbers in their rounded renderings.

## 3. The 43 distinct held-anchor misses, classified
Categories and reasons: `scan_adjudication_it_20261119.tsv` (written by `adjudicate_it_20261119.py`, which refuses to run if a miss has no category). In brief: CLAIM 002 (GABA label, row count, earlier wording 'untested', audit quote, own Title); CLAIM 003 (two manifest locator strings); CLAIM 004 (annotation string, seven by-eye values, a section number); CLAIM 006, 014, 015 (wordings quoted to reject); CLAIM 025 (five: an Italian formula, the earlier wording and its fragments, a queue pointer); CLAIM 040 (three Italian words under discussion, a binomial coefficient, two section numbers); CLAIM 046 (a rejected wording, three absent-term searches, seven values the record says it read as pixels). **Not independently re-checked by a second reader**: the classification is mine; the table gives the sentence so a second reader can contest any row.

## 4. Artefact-absent (decide only when the bytes arrive)
| Claim | Items | Anchor or cited paper with no held text (PMID, as the record gives it) |
|---|---|---|
| 036 | 23 numbers | 19936220, 23254685 |
| 042 | 7 numbers, 3 strings | 40831798, 41830506 |
| 033 | 5 numbers, 4 strings | cited paper 40875931 |
| 021 | 8 numbers | 8609180 (these eight are the by-eye and derived values; the record labels them so) |
| 001 | 5 numbers, 1 string | 41442931 (abstract only, SCI's finding) |
| 034 | 5 numbers | 34214506 |
| 005 | 7 strings | 19500159, 19936220 |
| 009, 028 | 1 string each | 27308416, 34214506; 32185845, 34214506, 35716775, 39420317 |
Held bytes are read from the operator's root checkout `files/` (read-only). **For 23 PMIDs the root checkout holds text files that their manifest does not declare present** (a PMC XML copy beside declared-absent HTML and PDF, for example for the paper CLAIM 005 rests on); the scan uses them (list in the summary JSON under `undeclared_files_used_by_pmid`). That is a registry-hygiene finding for HE and SCI: the manifest says ABSENT where the file is present.

## 5. Limits
Strings and numbers only; no check that a number is attributed to the right quantity; PDF text extraction can interleave two-column layouts (the first run lost three CLAIM 031 quotations to it; reading order fixed it); figure-only values are invisible to a text scan; a quote in the record that was pasted from a different paper's held text than its anchor is reported "found only in another paper". The classification of section 3 is one reader's.

## 6. Reproduce
`python3 -I quote_number_scan_it_20261119.py --repo <repo> --bytes-root <root with files/>` (about 7 minutes; `--selftest` checks the matcher), then `python3 adjudicate_it_20261119.py`. Files: `scan_items_it_20261119.tsv` (every item with its sentence), `scan_claims_it_20261119.tsv` (anchors, held, unheld, cited), `scan_summary_it_20261119.json`, `scan_adjudication_it_20261119.tsv`.
