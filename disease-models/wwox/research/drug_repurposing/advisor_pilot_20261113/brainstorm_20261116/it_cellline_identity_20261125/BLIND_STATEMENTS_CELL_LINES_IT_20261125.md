# Blind check: cell-line identity against the Cellosaurus register

Register: /home/desktop/.claude/jobs/9945c156/tmp/cellosaurus_dl/cellosaurus.txt (public file, version 57.0; entries end with //; relevant tags ID, AC, SY, CC "Problematic cell line").
Line list: LINES.tsv in this folder (78 names, one per row; some are families or stem-cell lines; names may be ambiguous).
Repository (read-only): /home/desktop/legend-development/.claude/worktrees/it_22_20261125/disease-models/wwox

Task 1. With your own parser, list EVERY name in LINES.tsv whose register entry carries a "Problematic cell line" comment: record id (CVCL_), the exact comment, and say when a name is ambiguous or not found. Do not stop at the ones named below.

Task 2. Judge each statement: SUPPORTED / NOT SUPPORTED / PARTLY, saying what the source says more or less.
K1. BGC-823, SGC-7901, SMMC-7721 and HO-8910 are registered as contaminated, HeLa derivatives; the record changes their stated tissue (gastric, hepatocellular, ovarian) from fact to label.
K2. CNE2 (CNE-2) is registered as contaminated, apparently a HeLa hybrid with a line of unknown origin.
K3. U87MG: the register says the line distributed as U-87MG ATCC is misidentified (not the original Uppsala line) but probably still a glioblastoma; so only the label changes.
K4. HepG2 is registered as misclassified (hepatoblastoma, not hepatocellular carcinoma): label only.
K5. SH-SY5Y carries a partial-contamination note (some redistributors supply a mouse-contaminated stock): it changes no statement unless a paper's own stock is shown to be affected.
K6. In analysis/wwox_expression_boost_census_20260922.md, row A7 reads "human gastric carcinoma lines"; of its four lines two are HeLa derivatives, so the gastric attribution can rest only on SNU-719 and AGS, and the abstract does not separate the WWOX result per line (check the abstract of PMID 25720522 with the PubMed tool).
K7. Rows A2 and B1 of the same census share the line HO-8910, so neither is ovarian evidence and they are not two independent platforms.
K8. Search the repository registries/*_current.md and research/*_ledger_current.md for any record where the stated tissue of one of the flagged lines carries an inference (for example "ovarian", "hepatocellular", "gastric" support for a direction). List each with file and line; say whether any statement about a neural or WWOX-deficient neural system depends on a flagged line.
