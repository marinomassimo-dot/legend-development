# Licence and redistribution inventory of the whole repository, tip and history (IT7 P8, R11)

Status: working inventory for the operator, 2026-10-29. Not legal advice. Nothing here changes
visibility, deletes material, rewrites history or contacts a rights holder. It declares no clearance:
"unverified" means no source page or licence text was read for it. A different verifier can recompute every
count with the script and commands below.

Reproduce (repository root, any worktree; about 80 s, reads every historical blob once, no network):

```
python3 disease-models/wwox/research/drug_repurposing/licence_inventory_it7.py --rev 619418f1 > inventory.txt
python3 disease-models/wwox/research/drug_repurposing/licence_inventory_it7.py --rev 619418f1 --skip-blob-scan   # sections 1-6, about 25 s
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
| ChEMBL (via DGIdb) | 16 947 | B | CC BY-SA 3.0; attribution with URL and release |
| GuideToPharmacology | 16 070 | B | ODbL database, CC BY-SA 4.0 contents |
| TTD | 15 246 | C | unclear ("all rights reserved" vs open access) |
| ChEMBL curated mechanism | 8 068 | B | CC BY-SA 3.0 |
| NCI Cancer Gene Index | 6 231 | C | public domain declared by DGIdb; source page gone |
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
| Page crops of one all-rights-reserved paper (7 PNG, 2.1 MB; about 46 % of a printed page plus three complete tables) | `research/page_adjudications/PMID17803050/p02,p03,p04 (2),p05,p08 (2)*.png` | added ef20b9ef (3), 902f943e (4), 2026-08-09; removed de089055, same day | no | `origin/main`, `development/main`, `backup/vps-main-2026-09-25` |
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

## 5. History: personal identifiers

None of these is a patient record; the full-privacy scan of history (variant, person and linkage patterns of `public_release_gate.py`) was NOT run over history by this
inventory and is listed as an open item in section 8. What was measured:

| finding | measure | where | at tip? |
|---|---|---|---|
| operator's personal mailbox in commit metadata | 22 commits, 44 author or committer fields (digest d0f5527b) | `git log --format=%ae%x09%ce` | history only; 22 of 22 commits reachable from `origin/main` and `development/main` |
| operator machine hostname in commit addresses | 5 579 fields (two digests: a5774f28, 20e8c823); 0 blobs contain the hostname | commit metadata only | history only |
| placeholder / noreply / vendor addresses | 18 / 1 455 / 448 fields | commit metadata | not a finding |
| third-party author e-mail addresses in the PubMed corpus seed | 336 occurrences in blob 43eb2dcedd of `registries/corpus_seed_pubmed_20260806.jsonl` | introduced ca506034 (2026-08-06), cleaned at the tip by dcbcc922 (2026-09-08) | history only; reachable from both remotes |
| other historical blobs with non-placeholder e-mail strings | 14 history-only blobs (7 paths): 3 analysis notes of 2026-09-20/21, 1 skill test, 1 safe-push test, 8 versions of `scripts/test_public_release_gate.py` (fixtures) | script section 7 | the paths exist at the tip; the listed blobs do not |
| absolute machine path `/home/<user>/` | 162 blobs: 40 at the tip, 122 history-only; `git grep` at the tip finds 890 occurrences of the operator account directory in 41 paths | script section 7 | yes (low sensitivity; the gate passes) |
| secrets (private keys, API token shapes) | 0 blobs in history | script section 7 | none |

## 6. Residual problems, ranked by exposure

Exposure = what is available to a third party today (tip or history, both public if the repository is public) times how clear the problem is. Rank is a judgement, not a measure.

| # | Problem | Facts | Why this rank |
|---|---|---|---|
| 1 | Catalogue holds 57 631 class C target rows (54.2 %) and 47 061 class B rows in a repository labelled MIT; raw DGIdb/Monarch responses add more | section 2; first commit 2bd6cde1, 5 versions, on the remotes | largest volume; several terms are non-commercial or unknown (DTC, JAX-CKB, CGI, TTD, OncoKB, COSMIC, TEND/TALC/Tdg); NCI class C only until read at NCI. Class B terms (share-alike, ODbL notice) may not be met by a single MIT-labelled file; they are mentioned in the notices, which say the MIT licence does not cover those parts |
| 2 | Verbatim paper text in 592 manifests (9 433 snippets, 229 749 words, up to 224 words each) and in dossiers (53 runs of 25+ words, longest 94) | section 3 | deliberate, large, and per-paper licences are unknown; quotation rules differ by jurisdiction and purpose; no per-paper licence field |
| 3 | Seven page crops of an all-rights-reserved paper remain in history; reachable from both remotes | section 4; added ef20b9ef / 902f943e, removed de089055 | clearest legal case (a known copyrighted page, substantial reproduction), small and removed from the tip, live only in history |
| 4 | Personal identifiers in history: the operator's personal mailbox on 22 commits; machine hostname on 5 579 fields; third-party author e-mails in a 2026-08-06 corpus-seed blob | section 5 | personal and persistent; removal from history is the only fix |
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
| B. Remove from the tip only (git-ignore or delete the class C rows from `catalog.jsonl.gz`, the raw folders and cards; keep ids and counts; page crops already done) | 1, 2 (manifest snippets), 7 | stops new distribution of the tip; history keeps 5 catalogue versions, all earlier files | medium: the catalogue is rebuilt by `catalog_build.py` from DGIdb and ChEMBL downloads and feeds `join/`, `coverage/`, the view and tests, so an offline-reproducible replacement (builder fed from re-downloaded sources) must exist first; deleting uncertain unique evidence is excluded by R11 | reversible from history | OPERATOR (deletes evidence artefacts and breaks the build until replaced) |
| C. Replace with counts and identifiers (class C sources reduced to claim-source counts, ChEMBL ids, gene symbols, our own annotations; snippets shortened to a short anchor plus digest and page, as already done for page crops) | 1, 2, 4 | tip carries only what the policy classes allow; the derivation stays checkable by anyone who holds the source | medium to high for snippets: 592 manifests, 3 356 snippets of 25+ words, quote audit and locator audit tooling depend on them; high for the catalogue (the shareable build already does it for the page) | reversible from history, but information is lost at the tip | OPERATOR for snippets and catalogue (changes verified evidence and gates) |
| D. Move class C and B data and the long quotation material to a private repository, keep a manifest with digests in the public one | 1, 2 | public tip clean; unique evidence preserved | medium: a private repository must exist (an account action, perhaps spend), and tests that read these files need a fixture or skip path | reversible | OPERATOR (new repository, access control, possible cost) |
| E. Rewrite history with `git filter-repo` (not run, not dry-run here) | 1 (earlier versions), 3, 4 | removes named paths and replaces identities in all commits | see below | NOT reversible for anyone who already cloned or forked; the old objects survive in other clones and may stay reachable on GitHub | OPERATOR, and force-push to a public remote |
| F. Make the repository private | all | stops new public access; does not retract copies, forks, caches | low cost; may cost the project its public aim | reversible (but a reversal re-exposes) | OPERATOR (visibility), never done here |
| G. Obtain permission or verify terms at the source (NCI, TTD, DTC and others unread; the Foundation for the letter; publishers) | 1, 5 | converts unknown to known | requires a human, possibly a contact or a fee: no contact or spend is made here | n/a | OPERATOR |

Scope and risks of E, for a decision and not a recommendation. The operation would have to name: (a) the seven page-crop paths; (b) the 8 removed preview paths and, if class C
rows are to leave history, the 5 versions of `catalog.jsonl.gz`, 11 of `coverage/associations.jsonl.gz`, the raw folders in section 4; (c) one blob of the corpus seed (43eb2dcedd) or
a text replacement of address strings; (d) a mailmap or `--mailmap` rewrite for the 22 commits with the personal mailbox (and for the 5 579 hostname-bound fields if wanted).
Because every later commit's hash depends on its ancestors, the earliest affected commit sets the cost: ca506034 (2026-08-06) is 3 706 commits before the tip; the 2026-10-28
catalogue commit alone would be 410. Specific risks recorded here: (1) 819 distinct 40-hex strings occur in 307 tracked files at the tip and 202 of them resolve to commits that would
change (ledger anchors, seals such as `git_head_at_freeze`, receipts); (2) the read-receipt ledger is a hash chain and the state manifest anchors its tail (CLAUDE.md, "Hand-editing the
ledger breaks its hash chain"), so SHA-bearing records would have to be re-anchored by their own tools; (3) `origin/main` and `development/main` and the worktrees (`task/it7-*`) diverge
and every collaborator would need to re-clone; (4) pull-request refs, forks and GitHub caches are outside any rewrite (section 9); (5) a rewrite would also have to cover the commits that exist only on local refs and other worktrees. Rewriting history was excluded by the mandate and is not proposed as the default.

A conservative sequence that needs the operator only at the two marked points: first A and the notice gaps (reversible, no authority); then the operator decides per class whether the rows
stay (accept with attribution), are reduced (C), or move (D); only afterwards, and only if copies already published must be retracted, E or F.

## 8. Reserved decisions (the operator's) and open items

1. Keep the class C catalogue rows and raw responses in the public tip (accept), reduce them (B or C), or move them (D). This is the largest decision (problem 1).
2. Whether the class B material may stay in a single MIT-labelled file or must be split into share-alike files with licence text, as the shareable package already does for ChEMBL.
3. Whether verbatim snippets up to 224 words stay, shorten, or move; whether papers should carry a per-paper licence field before that is decided.
4. Whether the seven page crops, the corpus-seed e-mail blob and the personal-mailbox commits justify a history rewrite (E) or are accepted as history; this includes any force-push.
5. Whether the repository is or should remain public (F), and who may confirm the current visibility.
6. Confirm that the Foundation gave permission for the letter PDF (G) and for the use of its name and letterhead; the repository records only that the rights remain with it.
7. Any contact with a rights holder (NCI, TTD, DTC, publishers) or spend for verification (G).
8. Open item for an actor: run the privacy scanners over history (`public_release_gate.py` patterns, `independent_privacy_scan.py`, `commit_metadata_scan.py` with `--base` set to the commit before the first
   published one) and report counts only; this inventory covered e-mail, machine path and secret shapes only.
9. Open item: add the missing notices (section 6, problem 6) and the licence-class column to `THIRD_PARTY_NOTICES.md`; classify the MATRIX, UniChem and iLINCS content already recorded in the README into that table.

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
| paths ever touched | `git log --all --name-only --format= \| sort -u` (4 475 paths ever, 293 not at the tip, none under `files/`, `staging/`, `_qa/`, `backup/`, `tmp/`, `overlay/`; the only excluded-pattern path ever tracked is `.codex/config.toml`, an own harness file, retired 2026-09-07) |
| binary and document history | `git log 619418f1 --diff-filter=AD --name-status` (script section 4) |
| versions of files embedding rows | `git log 619418f1 --format=%H -- <path>` (script section 5) |
| commit identities | `git log 619418f1 --format=%ae%x09%ce` (script section 6) |
| blob scan | `cat-file --batch` over 12 319 blobs (script section 7) |
| catalogue claim sources | parse `catalog.jsonl.gz` (script section 2) |
| SHA references in tracked text | `git grep -I -h -o -E '\b[0-9a-f]{40}\b' 619418f1 \| sort -u` then `git cat-file --batch-check` (819 distinct, 202 commits, 307 files) |
