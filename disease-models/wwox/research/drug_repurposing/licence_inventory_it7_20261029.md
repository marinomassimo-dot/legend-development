# Licence and redistribution inventory of the whole repository, tip and history (IT7 P8, R11)

Status: working inventory for the operator, 2026-10-29. Not legal advice. Nothing here changes
visibility, deletes material, rewrites history or contacts a rights holder. It declares no clearance:
"unverified" means no source page or licence text was read for it. A different verifier can recompute every
count with the script and commands below.

Reproduce (repository root, any worktree; about 80 s, reads every historical blob once, no network):

```
python3 disease-models/wwox/research/drug_repurposing/licence_inventory_it7.py --rev 619418f1 > inventory.txt
python3 disease-models/wwox/research/drug_repurposing/licence_inventory_it7.py --rev 619418f1 --skip-blob-scan   # sections 0-6, about 25 s
python3 disease-models/wwox/research/drug_repurposing/licence_inventory_it7.py history-privacy --rev 619418f1   # gate privacy scan over history, about 12 min
```

`619418f1` is the `main` commit this inventory was taken from (3 772 commits reachable; the inventory commit itself
adds two files and is not counted). Sections quoted below are the script's own sections 1 to 8; the output is deterministic
for a given `--rev` (two runs compared byte for byte).

## 0. Scope, population and what the script does not see

| item | value | command |
|---|---|---|
| tracked files at the tip | 4 182, 150 954 917 bytes | `git ls-tree -r -l -z --full-tree 619418f1` |
| commits reachable from the tip | 3 772 | `git rev-list --count 619418f1` |
| distinct blobs in that history | 12 319, 2 108 312 758 bytes uncompressed (pack about 108 MiB) | `git rev-list --objects 619418f1` then `git cat-file --batch-check` |
| refs other than task branches | local `main`; remote-tracking `origin/main` (70d6b323) and `development/main` (3202b372), both URLs the same GitHub repository; `backup/vps-main-2026-09-25`; one `refs/codex/turn-diffs/...` ref | `git for-each-ref` |
| paths ever touched by commits of the tip | 4 331, of which 149 are not at the tip (script section 0b; `--all` gives larger, ref-dependent numbers) | `git log 619418f1 --name-only --format=` |
| commits of the tip not in `origin/main` | 152 (1 not in `development/main`) | `git rev-list --count origin/main..619418f1` |
| repository licence | `LICENSE` is the MIT licence, "Copyright (c) 2026 The LEGEND project" | `git show 619418f1:LICENSE` |

What the repository's own notices say the MIT licence covers: `THIRD_PARTY_NOTICES.md` line 3 states it applies only to material for which
the authors hold the rights, and that third-party datasets and derived assets keep their terms; the catalogue README ("Licence reconciliation",
IT5 P1, with its independent verification of 2026-10-29) and `view/shareable_sources.json` classify sources A (attribution), B (share-alike),
C (identifiers and counts only), D (local only). `DATA_SOURCES.md` says the repository "is public, so those terms apply to what is already tracked".

Not decidable from inside the repository: see section 9.

## 1. The tip, by content family

Rule: the first matching rule of the `FAMILIES` table in the script (a path regex), applied to every tracked path. Terms and classes are the
repository's recorded readings, not new ones. `tabular rows` = lines of `.jsonl`, `.tsv`, `.csv` (header excluded), `.gz` decompressed.

| family | files | bytes | rows | origin | terms recorded | proposed class |
|---|---|---|---|---|---|---|
| licence and notice files | 4 | 39 669 | 0 | own | MIT / notices | A |
| shareable package licence texts and class-B ChEMBL file | 8 | 90 444 | 12 | licence texts; ChEMBL records of 12 compounds | CC BY-SA 3.0 | B |
| catalogue and per-source tables | 10 | 9 937 532 | 50 010 | DGIdb, ChEMBL, GtoPdb, MATRIX, openFDA rows reorganised | mixed by claim source (section 2) | B + C |
| join, coverage, view and package (embed catalogue-derived rows) | 94 | 23 662 329 | 4 489 | own computation over third-party rows | mixed | A / B / C |
| raw third-party responses and tool output | 132 | 23 607 803 | 0 | verbatim Monarch, DGIdb, ChEMBL, ClinicalTrials.gov, LINCS-type responses | per source, not individually verified | C |
| page-adjudication derivation records (json, md) | 38 | 599 389 | 0 | own recipes; the page crops are git-ignored | rights of the adjudicated papers | D for images |
| full-text dossiers | 342 | 2 949 675 | 0 | own notes quoting papers | each paper's copyright / licence | quotation (section 3) |
| deep-dive manifests (verbatim snippets) | 592 | 13 456 915 | 0 | own manifests carrying verbatim snippets | each paper's copyright / licence | quotation (section 3) |
| registries and read receipts | 15 | 11 347 470 | 3 490 | own; PMIDs, titles, author names from NLM | NLM terms; rights stay with holders | A for facts |
| AlphaFold / ClinVar / GTEx / ESM-2 / ThermoMPNN derived data | 60 | 7 627 560 | 13 267 | public data and own derivatives | CC BY 4.0, NCBI, GTEx open, MIT (DATA_SOURCES.md) | A |
| third-party document (Foundation letter, PDF) | 1 | 148 275 | 0 | authored by a third party | no licence recorded; README says rights stay with it | unknown |
| screenshots and previews of the view | 24 | 4 536 199 | 0 | own screenshots rendering catalogue-derived rows | follows the rows shown | follows view |
| other own figures | 3 | 151 617 | 0 | own plots | MIT + source terms | A |
| code (py, sh, js, css) | 409 | 7 087 938 | 0 | own | MIT | A |
| patch and diff files | 8 | 176 848 | 0 | own proposed edits | MIT | A |
| skills and agent definitions | 49 | 297 750 | 0 | own | MIT | A |
| governance, ledger, learning, reviews, roles, release, framework text | 650 | 14 593 789 | 330 | own | MIT | A |
| other disease-model research and analysis | 1 727 | 30 501 853 | 36 230 | own; may quote papers | MIT for own text | A + quotation |
| other root files | 16 | 141 862 | 0 | own | MIT | A |
| total | 4 182 | 150 954 917 | | | | |

Binary and document files at the tip (`.png`, `.pdf`, `.pdb`, `.gb`, `.gz` only; no `.xml`, `.zip`, `.docx`, `.xlsx`, `.jpg`): 15 PNG and 2 PDB under
`analysis/data` (own plots and AlphaFold-derived structures, 3 070 474 bytes); 21 PNG + 2 PDF previews of the view (4 531 043 bytes); 3 PNG figures of
own analyses of GEO series; 1 GenBank record (`input_NM_016373.4.gb`, 18 784 bytes; NCBI RefSeq, not covered by `THIRD_PARTY_NOTICES.md`); the catalogue,
the associations table and one ClinicalTrials.gov page as `.gz`; `docs/WWOX-Foundation-letter-of-support-public.pdf`. Page-adjudication images at the tip: 0
(`.gitignore` excludes them; de089055 explains why).

Code, skills and vendored files: no third-party code is vendored. `_external_repos/` holds a single `MANIFEST.md`. The script's licence-marker scan
(SPDX, "Licensed under the Apache", GPL text, "Copyright (c) <year>") matches 9 blobs in 8 tracked paths, all prose or licence-quoting text (for example
the shareable package's `LEGEND-MIT.txt`, `framework/adapters/opentargets.py` quoting the Open Targets terms it reads); no incompatible licence header was
found in any code. Optional dependencies (OpenMM, MDTraj LGPL, PyMuPDF AGPL) are declared, not redistributed (`THIRD_PARTY_NOTICES.md`).

## 2. Third-party rows embedded in the catalogue

`catalog.jsonl.gz` (8 765 091 bytes, 44 211 records, 106 315 `targets[]` rows) is the single largest holding of third-party rows. Command: parse the file at the
rev; count `targets[].claim_source` (DGIdb rows) or `.source` (ChEMBL curated mechanism rows); class from `view/shareable_sources.json` `claim_source_policy`.

| claim source | target rows | class | terms as recorded (not re-verified here) |
|---|---|---|---|
| DTC | 23 879 | C | CC BY-NC-SA 3.0 declared by DGIdb; not verified at source |
| ChEMBL (via DGIdb) | 16 947 | B | CC BY-SA 3.0; attribution with URL and release (that wording is the policy file's; not found on the pages read) |
| GuideToPharmacology | 16 070 | B | ODbL database, CC BY-SA 4.0 contents |
| TTD | 15 246 | C | unclear ("all rights reserved" vs open access) |
| ChEMBL curated mechanism | 8 068 | B | CC BY-SA 3.0 |
| NCI Cancer Gene Index | 6 231 | C | public domain declared by DGIdb; the cancer.gov reuse page DGIdb links to is live and says NCI text is "free of copyright" with third-party exceptions, without the words "public domain" and without naming the Cancer Gene Index (verifier, 2026-10-29); whether it covers these rows is unread, so class C stays defensible |
| PharmGKB / ClinPGx | 5 976 | B | CC BY-SA 4.0; policy page not read |
| TdgClinicalTrial | 5 072 | C | rights in a publisher's supplementary table |
| TEND | 2 242 | C | same |
| JAX-CKB | 2 148 | C | CC BY-NC-SA 4.0 declared by DGIdb |
| CIViC | 1 120 | A | CC0 1.0, verified at the source |
| MyCancerGenome | 829 | C | restrictive custom terms |
| TALC | 602 | C | rights in a publisher's supplementary table |
| FDA | 427 | A | public domain, verified at fda.gov policy |
| CGI | 368 | C | CC BY-NC 4.0 declared by DGIdb |
| MyCancerGenomeClinicalTrial | 317 | C | restrictive custom terms |
| ClearityFoundationClinicalTrial / Biomarkers | 240 / 163 | C | unknown; data no longer available |
| OncoKB | 148 | C | non-commercial custom terms |
| CancerCommons | 109 | C | custom terms |
| DoCM | 76 | A | CC BY 4.0, verified in the archived about page |
| COSMIC | 37 | C | custom terms |

By class: A 1 623 rows (1.5 %), B 47 061 (44.3 %), C 57 631 (54.2 %) of 106 315. Records by origin: 22 557 `dgidb_only`, 19 926 `chembl_selected`,
1 219 `openfda_unii_only`, 502 `matrix_only`, 7 `chembl_parent_added`. Records with a MATRIX source record: 1 927 (the ATC, DrugBank and ChEBI identifiers inside it are identifiers-only per the 2026-10-29 verification). The `claim_source_policy` covers every source found (no "NOT IN POLICY" row).

Third-party rows outside the catalogue at the tip (script section 2b): JSON entries tagged `"sources": "<label>"` in `join/cards.json` only (GuideToPharmacology 21,
PRISM 19, Drug Repurposing Hub 11, NCI 11, DTC 7, TdgClinicalTrial 5, ChEMBL 4: a handful of compound-level DGIdb tag lists inside prose); `coverage/associations.jsonl.gz`
(4 343 association rows: 3 743 DGIdb-derived by relation kind, 600 ChEMBL curated mechanism; the per-claim-source split is not recoverable from that file); `ligand_reconciliation.tsv`
(3 030 data rows with GtoPdb and ChEMBL identifiers, InChIKeys and flags; a `_not_merged` companion also exists); the raw responses below. The full view `view/index.html` and
`view/index_shareable.html` mention class B/C names only in prose and in a source-version list (6 and 36 mentions); I did not find embedded class C row text there,
but a field-by-field proof was not done.

Raw third-party responses (class C, family of 132 files, 23 607 803 bytes):

| folder (under `drug_repurposing/`) | files | bytes decompressed | mentions of class B/C names |
|---|---|---|---|
| `gse156243/kg_lookup` (WWOX.txt, GRIN2A.txt, HTR2C.txt) | 3 | 10 780 381 | 4 983 |
| `gse156243/kg_lookup/raw_WWOX`, `raw_GRIN2A`, `raw_HTR2C` | 11 + 7 + 8 | 3 693 163 + 2 497 867 + 1 991 027 | 2 271 + 1 717 + 995 |
| `gse156243/tool_responses` | 49 | 3 288 131 | 122 |
| `clinical_census_20261020_raw` | 7 | 5 238 362 | 13 |
| `lucas_clarke_followup_20261026/chembl_raw` | 46 | 500 972 | 44 |
| `lucas_clarke_followup_20261026/dgidb_raw` | 1 | 49 534 | 48 |

(Mentions are word-bounded occurrences, not rows; `raw_*` folders are children of `kg_lookup` and are listed separately by the script.)

## 3. Full-text-derived material and quotation length

Method: tracked `.md` files in each scope; count double-quoted runs of at least 10 words and blockquote lines. This is an upper bound on verbatim third-party text
(it also counts the repository quoting its own registries and tools) and a lower bound on paraphrase and unquoted copying; it cannot say which paper a run comes from or
what that paper's licence is. I found no per-paper licence field in the registries, so the share of open-access (CC BY) papers is unknown.

| scope | files | runs >=10 words | >=25 | >=50 | longest (words) | words in runs | blockquote lines |
|---|---|---|---|---|---|---|---|
| `fulltext_dossiers/*.md` | 342 | 448 | 53 | 4 | 94 | 7 293 | 785 |
| `page_adjudications/*.md` | 30 | 120 | 29 | 13 | 143 | 2 823 | 50 |
| `disease-models/wwox/analysis/*.md` | 220 | 2 604 | 631 | 93 | 168 | 54 169 | 7 512 |
| `disease-models/wwox/research/*.md` (not drug_repurposing, dossiers, adjudications) | 743 | 2 888 | 893 | 388 | 639 | 103 483 | 3 285 |
| `drug_repurposing/**/*.md` | 105 | 346 | 89 | 25 | 130 | 7 586 | 149 |
| `learning/`, `reviews/` `*.md` | 296 | 746 | 42 | 9 | 106 | 10 726 | 3 183 |

Deep-dive manifests (`verbatim_locators.entries[].snippet`, verbatim by design; the repository has quote-audit tooling for them): 592 files, 9 433 snippets, 229 749 words,
longest 224 words, 3 356 snippets of 25 or more words, 667 of 50 or more. This is the largest body of deliberate verbatim text from papers in the tip.
The longest runs of the `research/*.md` scope (up to 639 words) sit in `commit_candidates/CC-*.md`, which on a sample quote the repository's own registry text; that was not
verified paper by paper.

Page adjudication: 8 paper folders hold JSON/MD recipes (source-PDF digest, page, crop rectangle, dpi, image SHA-256); the 0 images are not tracked. For the one paper whose
images were once tracked, the all-rights-reserved notice was read in the PDF (AALAS 2007; no DOI, PMCID or open deposit) per de089055.

Full texts, XML copies, supplements, figure renders and PDFs of papers are not tracked at the tip, and none was ever committed (section 4): `files/` is git-ignored and no path
under `files/`, `staging/`, `_qa/`, `backup/`, `tmp/` or `overlay/` appears anywhere in history (`git log --all --name-only`).

## 4. History: files that are not redistributable, and where they were committed

Command: `git log 619418f1 --diff-filter=AD --name-status`, extension in the binary/document set; tip status from `git ls-tree`; reachability by `git merge-base --is-ancestor`
against the local remote-tracking refs (which may be stale, section 9). Commits are listed by short SHA; no content is reproduced.

| item | paths | commits | at tip | reachable from |
|---|---|---|---|---|
| Page crops of one all-rights-reserved paper (7 PNG, 2.03 MB; about 46 % of a printed page plus three complete tables) | `research/page_adjudications/PMID17803050/p02,p03,p04 (2),p05,p08 (2)*.png` | added ef20b9ef (3), 902f943e (4), 2026-08-09; removed de089055, same day | no | `origin/main`, `development/main`, `backup/vps-main-2026-09-25` |
| Foundation letter of support (third-party authored PDF, 148 275 bytes) | `docs/WWOX-Foundation-letter-of-support-public.pdf` | 8ab8e4b8, 2026-08-01 | yes | both |
| 8 earlier previews of the view (7 PNG + 1 PDF; rendered catalogue-derived rows) | `view/preview/01_overview_desktop.png` ... `08_export_card_ethosuximide.pdf` | added 7aeef97c (2026-10-28), removed 8d693e58 (2026-10-29) | no | both |
| 31 preview paths in all (23 at tip, 8 removed) | `view/preview/` | 7aeef97c, 0c2b9b4f, 83301218 | 23 yes | `development/main` and `origin/main` (the 7 files of 83301218 only `development/main`) |
| Catalogue with class B/C rows | `catalog/catalog.jsonl.gz` | 5 versions since 2bd6cde1 (2026-10-28) | yes | both |
| Coverage associations (DGIdb-derived) | `coverage/associations.jsonl.gz` | 11 versions since 2910c108 | yes | both |
| Raw responses `kg_lookup/WWOX.txt` etc. | `gse156243/kg_lookup/` | d84ed69a (2026-10-22), 1 version | yes | both |
| ClinicalTrials.gov raw page | `clinical_census_20261020_raw/WWOX_page1.json.gz` | 91f8e60c (2026-10-20) | yes | both |
| Shareable page containing NCI-tagged association labels | `view/index_shareable.html` | 54 versions since 7aeef97c; up to 299 mentions of class-C names (286 are the label `DGIdb:NCI`) between 2026-10-28 and the commit deb04a54 of 2026-10-29; 36 at the tip | tip version yes | both |

Class C and unclear rows have therefore been in every version of the catalogue since its first commit; removing them from the tip would not remove them from those 5 versions.
No full text, supplement, XML, figure render of a paper and no vendored code under an incompatible licence has ever been committed (extension census: the only binary or
document paths ever committed are the ones listed here plus `analysis/data` and `redteam` PNG/PDB files of the first commit a2e0dd0f, own plots and AlphaFold structures,
all still tracked).

Quotation in history (script section 8, same heuristic, `fulltext_dossiers` and `page_adjudications` `.md` blobs): 515 blobs ever (372 at the tip, 143 earlier versions); 986 runs of at least 10 words
(568 at the tip); runs of at least 25 words: 175 ever, 82 at the tip, 93 only in earlier versions; of at least 50 words: 29 ever, 17 at the tip, 12 only in earlier versions; longest 143 in both
sets. So earlier versions held somewhat more quotation than the tip, not longer runs. Earlier versions of the 592 manifests were not measured.

## 5. History: personal identifiers and the release gate's privacy scan over history

The tip passes the gate, but the gate has only ever been run on the tip. Run read-only on history it does not pass. Reproduce:
`python3 disease-models/wwox/research/drug_repurposing/licence_inventory_it7.py history-privacy --rev 619418f1` (about 12 minutes; the subcommand writes every history-only text blob to a temporary directory
outside the repository, calls `scan_privacy_and_secrets` of `scripts/public_release_gate.py` on it, and prints only counts, codes and introducing-commit SHAs; no matched text).
None of what follows has been adjudicated, and no finding states that a patient or a person is identified: the detector is digest- and pattern-based and can match common words or older, looser wording.

History privacy scan (the independent verifier obtained the same totals by a separate run; both are reproducible):

| measure | value |
|---|---|
| history-only (blob, path) text pairs scanned | 8 081 (binaries, PDFs and files over 30 MB not scanned) |
| findings, all history-only blobs | 2 778 in 763 blobs: BLOCK 1 202 in 198 blobs, REVIEW 1 576 |
| the same function over the tip | 30 findings (1 BLOCK, 29 REVIEW) |
| non-self-referential BLOCK blobs (gate source, its tests, the independent scanner and `launch/KERNEL_SPEC.md` excluded as detector vocabulary) | 166 |
| of those, mapped to an introducing commit | 156 (10 not mappable by `git log --find-object`); 124 distinct introducing commits: 2026-08: 69, 2026-09: 20, 2026-10: 35 |
| of those, still a path of the tip (so an earlier version of a file that was later reworded) | 146 |
| largest introducing commits (BLOCK blobs each) | 43668dd0 (6), 7abe9ba2 (4), 93b9ab55 (4), d84ed69a (4), 0b433b72 (3) |

BLOCK by code, non-self-referential paths (findings / blobs): DIRECT_IDENTIFIER 163 / 113; EMAIL_ADDRESS 446 / 16; PARENT_OF_ORIGIN_PAIRING 17 / 15; PARENT_OF_ORIGIN_REFERENCE_GENOTYPE 29 / 11;
PARENT_OF_ORIGIN_VARIANT_LINKAGE 12 / 12; CLINICAL_CASE_LINKAGE 6 / 5; GEOGRAPHIC_CASE_LINKAGE 1 / 1; REIDENTIFYING_VARIANT_COMBINATION 1 / 1. REVIEW (non-self-referential): PARENT_OF_ORIGIN_ATTRIBUTED 1 563 / 600,
PUBLIC_BIBLIOGRAPHIC_AUTHOR 1 / 1. The verifier, which excluded a slightly wider self-referential set, counts 91 direct-identifier blobs from 74 introducing commits dated 2026-08-10 to 2026-10-28
(largest d84ed69a, cb50e177, 43668dd0); the other codes agree exactly (16, 15, 11, 12, 5, 1, 1). The script prints all introducing commit SHAs.

Consequence: a public history that contains these blobs exposes whatever they hold to anyone who clones, forks or reads old revisions, even though the tip is clean; only a history rewrite, a replacement of the public history
or removal on the hosting side changes that, and each of those is the operator's (section 7, E, H, I). Whether a given hit is a real identifier is the open question; adjudicating the 166 blobs is the first step
and is reserved (section 8, item 10).

Other identifiers measured earlier (all counts, no values):

| finding | measure | where | at tip? |
|---|---|---|---|
| operator's personal mailbox in commit metadata | 22 commits, 44 author or committer fields (digest d0f5527b) | `git log --format=%ae%x09%ce` | history only; 22 of 22 commits reachable from `origin/main` and `development/main` |
| operator machine hostname in commit addresses | 5 579 fields in 2 790 of 3 772 commits (two digests: a5774f28, 20e8c823); 0 blobs contain the hostname | commit metadata only | history only |
| placeholder / noreply / vendor addresses | 18 / 1 455 / 448 fields | commit metadata | not a finding |
| third-party author e-mail addresses in the PubMed corpus seed | 430 occurrences, 261 distinct (case-folded; 262 case-sensitive), in 245 of 706 records of blob 43eb2dcedd of `registries/corpus_seed_pubmed_20260806.jsonl`; the tip blob has 0 (script section 7b) | introduced ca506034 (2026-08-06), cleaned at the tip by dcbcc922 (2026-09-08) | history only; reachable from both remotes |
| other historical blobs with non-placeholder e-mail strings | 14 history-only blobs (7 paths): 3 analysis notes of 2026-09-20/21, 1 skill test, 1 safe-push test, 8 versions of `scripts/test_public_release_gate.py` (fixtures) | script section 7 | the paths exist at the tip; the listed blobs do not |
| absolute machine path `/home/<user>/` | 162 blobs: 40 at the tip, 122 history-only; `git grep` at the tip finds 890 occurrences of the operator account directory in 41 paths | script section 7 | yes (low sensitivity; the gate passes) |
| secrets (private keys, API token shapes) | 0 blobs in history | script section 7 | none |

## 6. Residual problems, ranked by exposure

Exposure = what is available to a third party today (tip or history, both public if the repository is public) times how clear the problem is. Rank is a judgement, not a measure.

| # | Problem | Facts | Why this rank |
|---|---|---|---|
| P0 (top) | History contains blobs the release gate blocks: 198 history-only blobs with BLOCK findings (166 outside detector vocabulary), 124 introducing commits, Aug to Oct 2026; the tip has 1 | section 5; reproducible with the `history-privacy` subcommand | unadjudicated but the most serious open finding: a public history that contains it, on both remotes, while the tip passes; the remedy is only on the history level and so is the operator's |
| 1 | Catalogue holds 57 631 class C target rows (54.2 %) and 47 061 class B rows in a repository labelled MIT; raw DGIdb/Monarch responses add more | section 2; first commit 2bd6cde1, 5 versions, on the remotes | largest volume; several terms are non-commercial or unknown (DTC, JAX-CKB, CGI, TTD, OncoKB, COSMIC, TEND/TALC/Tdg); NCI class C because the reuse page read does not name the Cancer Gene Index. Class B terms (share-alike, ODbL notice) may not be met by a single MIT-labelled file; they are mentioned in the notices, which say the MIT licence does not cover those parts |
| 2 | Verbatim paper text in 592 manifests (9 433 snippets, 229 749 words, up to 224 words each) and in dossiers (53 runs of 25+ words, longest 94) | section 3 | deliberate, large, and per-paper licences are unknown; quotation rules differ by jurisdiction and purpose; no per-paper licence field |
| 3 | Seven page crops of an all-rights-reserved paper remain in history; reachable from both remotes | section 4; added ef20b9ef / 902f943e, removed de089055 | clearest legal case (a known copyrighted page, substantial reproduction), small and removed from the tip, live only in history |
| 4 | Personal identifiers in history outside the gate scan: the operator's personal mailbox on 22 commits; machine hostname on 5 579 fields in 2 790 commits; third-party author e-mails in a 2026-08-06 corpus-seed blob | section 5 | personal and persistent; removal from history is the only fix |
| 5 | Third-party document at the tip: Foundation letter of support (PDF) | README says it is "published here" and that rights remain with the Foundation; no permission record found | one file, but permission is a fact only the operator can state |
| 6 | Notice gaps: no entry in `THIRD_PARTY_NOTICES.md` or `DATA_SOURCES.md` for GEO series GSE156243 and GSE126075 derivatives, iLINCS/LINCS, ClinicalTrials.gov raw pages, PRISM and Drug Repurposing Hub tags, the GenBank/RefSeq record NM_016373.4 | `ACKNOWLEDGEMENTS.md` (drug_repurposing) covers some services; the repository-level notices do not | cheap to fix, low legal weight |
| 7 | Screenshots of the view (21 PNG + 2 PDF at the tip, 8 in history) render catalogue-derived rows | section 4 | follows problem 1 |
| 8 | Earlier shareable pages carried up to 286 `DGIdb:NCI` labels (fact-level tags beside gene symbols) | section 4 | superseded; the labels are identifiers not row text |

## 7. Alternatives for each residual problem

Cost is effort and side effects; reversibility is whether the action can be undone. "OPERATOR" marks what needs the operator's authority under the rules of this repository
(history rewrite, visibility, deletion of unique evidence, any contact with a rights holder, any spend, anything outside the worktree). Anything not marked can be done by an actor
on a task branch and landed under §21d.

| alternative | applies to | effect | cost / risk | reversibility | authority |
|---|---|---|---|---|---|
| A. Accept with attribution (publish the existing readings; add the missing notice entries; add ChEMBL and GtoPdb credit lines and licence text; label which tracked files are not MIT) | 1, 5, 6, 7 | removes the notice gap; does not make NC or unclear terms compatible | low; one commit | fully reversible | none for notice files; the decision to keep class C rows is the OPERATOR's |
| B. Remove from the tip only (git-ignore or delete the class C rows from `catalog.jsonl.gz`, the raw folders and cards; keep ids and counts; page crops already done) | 1, 2 (manifest snippets), 7 | stops new distribution of the tip; history keeps 5 catalogue versions, all earlier files | medium: the catalogue is rebuilt by `catalog_build.py` from DGIdb and ChEMBL downloads and feeds `join/`, `coverage/`, the view and tests, so an offline-reproducible replacement (builder fed from re-downloaded sources) must exist first; deleting uncertain unique evidence is excluded by R11 | reversible from history only as long as E (a history rewrite) is never chosen; after E the old versions are gone from this repository | OPERATOR (deletes evidence artefacts and breaks the build until replaced) |
| C. Replace with counts and identifiers (class C sources reduced to claim-source counts, ChEMBL ids, gene symbols, our own annotations; snippets shortened to a short anchor plus digest and page, as already done for page crops) | 1, 2, 4 | tip carries only what the policy classes allow; the derivation stays checkable by anyone who holds the source | medium to high for snippets: 592 manifests, 3 356 snippets of 25+ words, quote audit and locator audit tooling depend on them; high for the catalogue (the shareable build already does it for the page) | reversible from history, but information is lost at the tip | OPERATOR for snippets and catalogue (changes verified evidence and gates) |
| D. Move class C and B data and the long quotation material to a private repository, keep a manifest with digests in the public one | 1, 2 | public tip clean; unique evidence preserved | medium: a private repository must exist (an account action, perhaps spend), and tests that read these files need a fixture or skip path | reversible | OPERATOR (new repository, access control, possible cost) |
| E. Rewrite history with `git filter-repo` (not run, not dry-run here) | P0, 1 (earlier versions), 3, 4 | removes named paths and replaces identities in all commits | see below | NOT reversible for anyone who already cloned or forked; the old objects survive in other clones and may stay reachable on GitHub | OPERATOR, and force-push to a public remote |
| F. Make the repository private | all incl. P0 | stops new public access; does not retract copies, forks, caches | low cost; may cost the project its public aim | a visibility switch is reversible in itself (a reversal re-exposes); how GitHub forks, caches and already-made clones behave on the switch is UNREAD here | OPERATOR (visibility), never done here |
| G. Obtain permission or verify terms at the source (NCI, TTD, DTC and others unread; the Foundation for the letter; publishers) | 1, 5 | converts unknown to known | requires a human, possibly a contact or a fee: no contact or spend is made here | n/a | OPERATOR |
| H. Orphan or squashed public history, with the full history kept in a private archive | P0, 1, 2, 3, 4, 5 | public history starts from a clean tip (or a squashed series); old SHA citations point into the archive | medium to high: a private archive must exist and be backed up; no `filter-repo` reconciliation of seals, but every SHA citation in tracked text must be mapped or marked | reversible while the archive exists; the old public history stays in clones and forks | OPERATOR (new public history, force-push or new repository, archive hosting) |
| I. Hosting-provider removal request (cached views, dangling objects, fork network) | P0, 3, 4 and anything copied | the only route that addresses what section 9 lists as unverifiable | needs contact with the provider; effect unknown | n/a | OPERATOR (contact) |
| J. Do nothing but record: a dated register of the known exposures and a prepared response to a notice | all incl. P0 | no change to history; the baseline against which A to I are priced | trivial | fully reversible | none to write the register; the decision to leave the exposure is the OPERATOR's |

Scope and risks of E, for a decision and not a recommendation. Precondition: a bundle of the complete pre-rewrite repository (all refs) is made and stored first. The other copies carrying the same material are not
touched by a rewrite of `main` and must be put in or out of scope explicitly: `backup/vps-main-2026-09-25`, the VPS recovery bundle, `refs/codex/turn-diffs/...`, the `development` remote, all `task/it7-*` branches and worktrees, and every clone.
The operation would have to name: (a) the seven page-crop paths; (b) the 8 removed preview paths and, if class C
rows are to leave history, the 5 versions of `catalog.jsonl.gz`, 11 of `coverage/associations.jsonl.gz`, the raw folders in section 4; (c) one blob of the corpus seed (43eb2dcedd) or
a text replacement of address strings; (d) identity rewriting (`--mailmap`) for the 22 commits with the personal mailbox and, if the machine hostname is to go, for 2 790 commits, which
rewrites about three quarters of all 3 772 commits and is therefore not a small add-on to (a) to (c); (e) whatever the history privacy scan (section 5) leads the operator to adopt, which touches blobs introduced by 100+ commits.
Because every later commit's hash depends on its ancestors, the earliest affected commit sets the cost: ca506034 (2026-08-06) is 3 706 commits before the tip; the 2026-10-28
catalogue commit alone would be 410. Specific risks recorded here (corrected by the independent verifier):
(1) The read-receipt ledger chain (`ledger_prev_hash`) and the state-manifest tail anchor are content hashes (SHA-256 of record content, an event count and a head digest), not Git hashes: of the ledger's
913 lines exactly 1 holds a 40-hex string, so a rewrite that does not edit `fulltext_read_receipts.jsonl` leaves chain and anchor valid. (2) The real coupling is records that quote commit SHAs. At the tip, 819 distinct 40-hex strings occur in 307 files;
202 resolve to commits (5 of them not reachable from the tip), 124 already resolve to nothing in this clone, 493 are other objects. The 202 is an upper bound: from ca506034 194 reachable commits would change, from ef20b9ef 190, from 2bd6cde1 4, from 7aeef97c 3 (script section 5b).
Seals and records: 39 `git_head_at_freeze` occurrences in 15 files; 17 distinct 40-hex strings in `framework/state/state_history.md` and 1 in `framework/state/sync_epochs.jsonl`; 91 distinct 12-hex tokens that resolve to commits (script section 5b; the J2 deriver anchors on 12-character SHAs).
Someone must decide who re-anchors these after a rewrite (reserved item). (3) `origin/main`, `development/main` and the worktrees diverge and every collaborator would re-clone. (4) Pull-request refs, forks and GitHub caches are outside any rewrite (section 9). (5) A rewrite must also cover commits that exist only on local refs and other worktrees.
Rewriting history was excluded by the mandate and is not proposed as the default.

A conservative sequence (J first, as the baseline; the operator is needed at every row marked OPERATOR): first A and the notice gaps (reversible, no authority); then the operator decides per class whether the rows
stay (accept with attribution), are reduced (C), or move (D); only afterwards, and only if copies already published must be retracted, H, E, F or I, and only after the history privacy findings of section 5 have been adjudicated.

## 8. Reserved decisions (the operator's) and open items

1. (After item 10.) Keep the class C catalogue rows and raw responses in the public tip (accept), reduce them (B or C), or move them (D). This is the largest decision (problem 1).
2. Whether the class B material may stay in a single MIT-labelled file or must be split into share-alike files with licence text, as the shareable package already does for ChEMBL.
3. Whether verbatim snippets up to 224 words stay, shorten, or move; whether papers should carry a per-paper licence field before that is decided.
4. Whether the seven page crops, the corpus-seed e-mail blob and the personal-mailbox commits justify a history rewrite (E) or are accepted as history; this includes any force-push.
5. Whether the repository is or should remain public (F), and who may confirm the current visibility.
6. Confirm that the Foundation gave permission for the letter PDF (G) and for the use of its name and letterhead; the repository records only that the rights remain with it.
7. Any contact with a rights holder (NCI, TTD, DTC, publishers) or spend for verification (G).
8. (Partly done: the gate's own privacy scan was run over history, section 5; its findings are not adjudicated.) Open item for an actor: run the remaining scanners over history (`public_release_gate.py` patterns, `independent_privacy_scan.py`, `commit_metadata_scan.py` with `--base` set to the commit before the first
   published one) and report counts only; this inventory covered e-mail, machine path and secret shapes only.
9. Open item: add the missing notices (section 6, problem 6) and the licence-class column to `THIRD_PARTY_NOTICES.md`; classify the MATRIX, UniChem and iLINCS content already recorded in the README into that table.
10. FIRST: disposition of the history privacy findings of section 5 (adjudicate the 166 blobs, adopt a remedy, or accept and record). Nothing else in this list should precede it.
11. Scope of the other copies (backup branch, VPS recovery bundle, codex ref, `development` remote, clones) in any rewrite or publication decision.
12. Who re-anchors seals (`git_head_at_freeze`, `state_history.md`, `sync_epochs.jsonl`, short SHAs in prose) after a rewrite.
13. A no-destruction hold: no deletion of the pre-rewrite bundle or of the other copies while a rights-holder or privacy notice is possible.
14. A removal request to the hosting provider (alternative I).

## 9. Not verifiable from inside the repository

- Whether the GitHub repository is public today, since when, and whether a particular branch or the `development` remote is public: UNVERIFIABLE here. The remote-tracking refs are local copies; `origin/main` was last
  fetched at 70d6b323 and may not equal the server.
- Forks, clones, the fork network and any copy a third party made between 2026-08-09 (page crops) and now: UNVERIFIABLE.
- GitHub's cached views, search index, raw-content caches, code-search and the web archive: UNVERIFIABLE.
- Pull-request refs (`refs/pull/*`), deleted-branch objects retained by GitHub and dangling commits reachable by SHA: UNVERIFIABLE (the local clone has none of them; a rewrite would not remove them).
- Whether any third party has issued a notice: UNVERIFIABLE.
- Current terms of every source marked "declared by DGIdb" or "unread": not re-read here; the readings are those of the catalogue README as of 2026-10-28/29.
- The licence of each cited paper (open access or not): not recorded in the registries read; not determined here.
- Whether the Foundation granted permission for the PDF: UNVERIFIABLE (operator knowledge).

## 10. Commands used, in one place

| purpose | command |
|---|---|
| tip files and bytes | `git ls-tree -r -l -z --full-tree 619418f1` |
| history population | `git rev-list --count 619418f1`; `git rev-list --objects 619418f1`; `git cat-file --batch-check` |
| paths ever touched | `git log 619418f1 --name-only --format= \| sort -u` (script section 0b: 4 331 paths ever, 149 not at the tip; with `--all` the counts are larger and depend on local refs; none under `files/`, `staging/`, `_qa/`, `backup/`, `tmp/`, `overlay/`; the only excluded-pattern path ever tracked is `.codex/config.toml`, an own harness file, retired 2026-09-07) |
| binary and document history | `git log 619418f1 --diff-filter=AD --name-status` (script section 4) |
| versions of files embedding rows | `git log 619418f1 --format=%H -- <path>` (script section 5) |
| commit identities | `git log 619418f1 --format=%ae%x09%ce` (script section 6) |
| gate privacy scan over history-only text blobs | `licence_inventory_it7.py history-privacy --rev 619418f1` (section 5) |
| blob scan | `cat-file --batch` over 12 319 blobs (script section 7) |
| catalogue claim sources | parse `catalog.jsonl.gz` (script section 2) |
| SHA references in tracked text | `git grep -I -h -o -E '\b[0-9a-f]{40}\b' 619418f1 \| sort -u` then `git cat-file --batch-check` (819 distinct, 202 commits, 307 files; script section 5b adds the descendants, seal and short-SHA counts) |
