# Verification IT21 P8 (ACTOR verifier-it21)

Blind-first: for each item the first view in `verdicts_it21_p8.tsv` (column `my_first_view`) was written from primary artefacts (catalogue records, ChEMBL jsonl, saved XML, expression row tables, PubMed abstracts) before the producer README or conclusion column was read for that item. Verdicts: `verdicts_it21_p8.tsv`.

## Limits of the independence obtained

* Same repository, same tools and same catalogue as the producers; the catalogue, the action tables and the expression row tables are the producers' own derived artefacts. Raw GEO counts were not recomputed.
* For items A and B the producer tables (qualification TSVs) were the only place some of the rows could be read at all; the first view was formed on the ChEMBL record, the PubMed abstracts and the saved paper, then compared. I did see the producer conclusion column for a few rows before forming a view (G02, G03 rows), so those two are not blind.
* The saved IOX1 XML is gitignored; it was read from a sibling worktree and its sha256 matched the stated one.
* Abstracts of the Triac and P140 papers only; no full texts re-read.
* Item E ran in a temp copy of `framework/scripts` with the file at 7fe0f097 substituted.

Read-only toward every scientific file; nothing outside this directory was written.
