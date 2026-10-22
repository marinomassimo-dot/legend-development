# Self-evaluation - scientist-d, group R4c (WWOX rows in supplements), 2026-10-22

Verdict: a supplement symbol search over 12 counted papers (17 supplements opened in all) found two supplement-only WWOX rows (one with a treatment context, one genotype-only); no paper was read to completion, so no manifest and no receipt is claimed. One reading of my own earlier note was wrong and is withdrawn.

1. **The most valuable result is a correction, and it is mine.** R4b had written that the all-zero column of Table S7 "means not a responder". Re-deriving it from the docx cells and from the denominators (Table 3 prints 21/40 for the other-DEE group, Table S6 sums to 21 over the full 40, Table S4 drops to 38) showed the reading cannot be made: a recorded sub-50% course and an absent datum scored as zero look identical. The note now says UNDETERMINED. No blind audit has been run (declared OWED).
2. **The new row is genotype-only.** The one WWOX row found by this search that no text index would reach (a single-centre genotype table) carries no treatment and no response, so it adds nothing to the treatment question; it is recorded because the task asked for the inventory, not because it matters to efficacy.
3. **Overlap is the weak point.** Rows are anonymous; independence is shown for none. The count is stated as 7 to 8, not 8.
4. **Search limits stated, not hidden.** The tool cannot see PDFs or images; the best-fitting cohort (a 79-aetiology perampanel registry) is parked behind a publisher bot challenge, not bypassed; one supplement is TIFF figures.
5. **Mistakes caught.** The alias `FOR` matched the English word and produced false hits (caught on reading the output); my first search log was written to the wrong directory (caught when the load failed); a symlink name with a space was mangled (caught by the file count). A text flattening of a docx table had put a header out of cell order, so the column mapping was re-checked cell by cell before any claim was written.

Micro-upgrade (one, proportional): `supplement_symbol_search.py` should accept `--root DIR` pointing at any directory of supplements (so `files/fulltext/PMID*_supplement/` is reachable without a symlink workspace) and should convert PDFs with `pdftotext` itself, reporting the count of PDFs and images it could not read. Candidate for Harness Engineering; not done here (the tool belongs to scientist-b).

ATTRIBUTION_CENSUS
incidents: 5
machine: 1   blind_auditor: 0   peer: 0   self: 4
severity_high: 1   of which self: 1
undetected_known: 0
