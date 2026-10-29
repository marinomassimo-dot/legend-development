# IT8 P2 independent verification: licence corrections

Verifier (not the producer). Date of work: 2026-10-29 to 2026-10-30. Object: branch `task/it8-p2`, commits `5ce051b4` and
`22d4791e`, file `disease-models/wwox/research/drug_repurposing/licence_corrections_it8_20261029.md` and the edits
listed in the mandate. Read-only toward the producer's work: nothing was rewritten, deleted, registered, e-mailed or paid;
no access control was bypassed. Not legal advice. "Read" below means this verifier fetched the page from its host and read
the sentence; "unreadable" means the page returned a script shell, a browser check, an error or no connection.

Verdict: the producer's primary-source claims, counts and row tallies reproduce. No defect changes a licence conclusion.
One verification step the producer could not do (the dynamic shareable audit) was flaky under host load and is reported
separately. Defects are ranked at the end (section 8).

## 1. Primary terms (task 1)

| Source | Page | Result by this verifier | Producer's claim |
|---|---|---|---|
| ChEMBL | `chembl.github.io/chembl-licensing` | READ. Dated 03 Oct 2010: "licensed under ... CC Attribution-ShareAlike 3.0 Unported license"; "The required attribution should contain the url of the ChEMBL resource, and also the release version"; example credit; "visible on the entry portal ... or contained with the documentation for any further distribution". Gitbook `about` page also read (200). | Reproduced. |
| GtoPdb | `guidetopharmacology.org/about.jsp` | READ. "licensed under the Open Data Commons Open Database License (ODbL). Its contents are licensed under a Creative Commons Attribution-ShareAlike 4.0 International License". The download page carries only the CC BY-SA 4.0 footer. ODbL text page reachable (200). | Reproduced. |
| TRRUST | `grnpedia.org/trrust/` | READ. "freely available for both academic and commercial use under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license ... appropriate attribution ... adapted material is distributed under the same license". | Reproduced. |
| openFDA | `open.fda.gov/terms/` | READ. "public domain and made available with a Creative Commons CC0 1.0 Universal dedication"; works where CC0 does not apply are "clearly marked". Attribution "not required". | Reproduced. |
| NCI reuse | `cancer.gov/policies/copyright-reuse` | READ. "all text within National Cancer Institute (NCI) products is free of copyright and may be reused without our permission. Credit the National Cancer Institute"; graphics mixed. No occurrence of "Gene Index", "dataset" or "data set" in the page text. | Reproduced. |
| COSMIC | `cancer.sanger.ac.uk/cosmic/license` | READ. Academic use free for the academic community; commercial organisations licence COSMIC. DGIdb's own string is "Free for non-commercial use". | Reproduced. |
| DGIdb | GraphQL `sources { nodes { sourceDbName license licenseLink } }` | READ. 200 OK, 48 sources, 48 with a licence string and 48 with a link, no node for DGIdb itself. | Reproduced (48, none for DGIdb). Table: ChEMBL "CC BY-SA 3.0", GuideToPharmacology "CC BY-SA 4.0", ClinPGx "CC BY-SA 4.0", DTC "CC BY-NC-SA 3.0", CKB-CORE "CC BY-NC-SA 4.0", CGI "CC BY-NC 4.0", OncoKB "Restrictive, non-commercial", COSMIC "Free for non-commercial use", NCI "Public domain", TTD "Unclear...", DoCM "CC BY 4.0", CIViC "CC0 1.0": all as the producer reports. |
| NCBI policies | the NCBI "Policies and Disclaimers" page | READ. "created by or for the US government on this site is within the public domain"; NLM acknowledgement requested; "NCBI itself places no restrictions on the use or distribution of the data"; submitters may claim rights, "no transfer of rights from submitters to NCBI". | Reproduced. |
| NLM terms | `nlm.nih.gov/databases/download/terms_and_conditions.html` | READ. "Courtesy of the U.S. National Library of Medicine". | Reproduced. |
| CKB | `ckb.jax.org` (front page footer) | READ, NEW. "This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License". The producer's host name `ckb.genomenon.org` did not resolve here either. | Producer: UNVERIFIED. It can now be marked verified at the JAX site. |
| ClinPGx | `clinpgx.org/page/dataUsagePolicy` | UNREADABLE (script shell). DGIdb reports CC BY-SA 4.0 with that link. | Consistent. |
| CGI | `cancergenomeinterpreter.org/faq` | UNREADABLE (shell, 27 characters). | Consistent. |
| OncoKB | `oncokb.org/terms` | UNREADABLE (outdated-browser shell). | Consistent. |
| TTD | `ttd.idrblab.cn` | UNREADABLE (34 characters). | Consistent. |
| DTC | `drugtargetcommons.fimm.fi` | UNREADABLE (no connection). | Consistent. |
| MyCancerGenome | `mycancergenome.org` | UNREADABLE (no connection). | Consistent. |
| UniProt licence page | `uniprot.org/help/license` | UNREADABLE (JavaScript shell). | Consistent. |
| ClinVar data use | `ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/`, `/clinvar/intro/` | UNREADABLE (reCAPTCHA check). The FTP README has no licence sentence. | Consistent. |
| GEO disclaimer | `ncbi.nlm.nih.gov/geo/info/disclaimer.html` | UNREADABLE (reCAPTCHA check). | Consistent. |
| ClinicalTrials.gov terms | `clinicaltrials.gov/about-site/terms-conditions` | UNREADABLE (script shell, 177 characters). | Consistent. |
| LINCS policy | `lincsproject.org/LINCS/data/data-policy` | UNREADABLE (19 characters). | Consistent. |
| SIGNOR | `signor.uniroma2.it` | UNREADABLE (no connection, timeout). | Consistent. |

Observation on scope. The DGIdb service also lists sources whose strings are share-alike or ODbL and that are not in the
producer's table or notices: HumanProteinAtlas (CC BY-SA 3.0), IDG and Pharos (CC BY-SA 4.0), MOAlmanac (ODbL). The
tip catalogue holds claim rows for 21 claim sources and none of these four (recomputed from `catalog.jsonl.gz`), so no
catalogue consequence follows; the DGIdb raw responses in `dgidb_raw/` were not re-inspected for them.

What BY-SA triggers (task 1, second half). The producer's reading is sound on the licence text: the 46 raw ChEMBL responses
are verbatim Works (credit, licence copy, no extra restriction); the merged `catalog.jsonl.gz` re-arranges ChEMBL fields
with DGIdb, GtoPdb and MATRIX fields and is an adaptation, which the MIT label cannot cover. Per-source row counts
recomputed from the catalogue match the producer: ChEMBL 16,947 (DGIdb claim) plus 8,068 (curated mechanism), GtoPdb
16,070, ClinPGx 5,976, DTC 23,879, TTD 15,246, NCI 6,231, CKB 2,148, CGI 368, OncoKB 148, COSMIC 37; class B total
47,061 and class C total 57,631 both recompute exactly.

## 2. The package page and the class-B file (task 2)

- `view/shareable_package/index.html`: 1,485 distinct `CAT:` ids by the manifest (259 by a plain regex on the page), 260
  distinct `CHEMBL` ids, no occurrence of `max_phase`, `mechanism_of_action`, `action_type`, `molecule_type`, `pref_name`
  or `chembl_release`. None of the mechanism strings or target names of the class-B file occurs in the page. The
  producer's claim that the page embeds ChEMBL identifiers, counts and own text and no mechanism or status data holds.
- Residual precision gap (low): the page embeds 1,506 record names (`ROWNAME`, per `manifest.json`). The names of at least
  three of the twelve class-B compounds (amlexanox, lithium, cannabidiol) appear in the page. Generic drug names are facts,
  but the notice states "no ChEMBL content" and "(only ChEMBL identifiers)" without saying where the 1,506 names come from.
  The notice should name the origin of record names or soften the sentence.
- Class-B file: 12 JSON Lines records, `CREDIT.txt` contains the ChEMBL URL and release ("ChEMBL data is from
  https://www.ebi.ac.uk/chembl/ - the version of ChEMBL is ChEMBL_37 2026-05-01"), licence URL, adaptation notice
  (selection of 12 records and listed fields, values unaltered, same licence, no endorsement) and a scope clause. The
  legal code is shipped next to it (22,240 bytes). Against the ChEMBL wording read in section 1 and CC BY-SA 3.0 4(a)-4(c)
  this is complete. Each record carries `licence` and `chembl_release` fields.
- BY-SA reach: the scope clause says the Collection (the other package files) is not required to be share-alike. This
  rests on the Adaptation definition of CC BY-SA 3.0 (a Collection is excluded) and is a defensible reading, not a settled
  one; the producer says so. The one condition the package adds beyond the licence is "do not merge this file into another
  dataset" which is advice, not a licence term, and is worded as such.
- Garbled redaction phrase in the shipped English notice (low): `NOTICE.md` of the package contains "un registro del
  repository (non incluso in questo pacchetto)" in three places, one of which sits inside the UniChem version string
  ("version Last-Modified un registro del repository (...)=Sat, 24 Oct 2026 ..."), so the version information of that
  source is unreadable. The producer listed the phrase as cosmetic; the UniChem version string is a credit-line content
  loss, not only cosmetic.

## 3. Quotation indicator, recomputed (task 3)

Code: own script over `deepdive_manifests/*.json` (592 files), entries of `verbatim_locators.entries[].snippet`; Europe PMC
REST `search?resultType=core`, field `license`, one query per 40 PMIDs, 2026-10-29.

| Quantity | Producer | Verifier |
|---|---|---|
| snippets | 9,433 | 9,433 |
| snippets of 25 or more words | 3,356 | 3,356 |
| own descriptions / attestations among them | 1,355 | 1,292 (strict prefix rule) to 1,366 (keyword rule) |
| third-party candidates | 2,001 | 1,990 (keyword rule), 456 papers |
| CC BY | 1,167 | 1,161 |
| NC family | 491 (298 NC-ND, 166 NC, 27 NC-SA) | 488 (295, 166, 27) |
| no licence tag | 343 | 333 plus 8 not returned by Europe PMC = 341 |
| runs of 50 or more words | 97 CC BY, 34 NC, 12 none | 96, 32, 12 (the CC BY and NC cells differ by the same rule noise) |
| runs of 50 or more words with no tag | 12 runs in 9 papers (50-71 words) | 12 runs, 9 papers, 50-71 words (identical list of papers) |
| runs of 100 or more words | 6 CC BY, 3 NC, 0 none | 6, 3, 0 |

The differences (at most 11 snippets, under 1 per cent) come from the unstated rule that separates own descriptions from
quotations; the producer's numbers sit inside my two-rule range for the own-description class. The headline holds.

Sample of the 15 longest candidate runs read by this verifier (first 230 characters and anchor of each). Ranks 1, 2, 4, 10,
11 and 12 are results paragraphs of CC BY papers (224, 185, 136, 98, 93 and 90 words); ranks 3 and 8 are CC BY figure
legends; ranks 7 and 15 are CC BY limitation paragraphs; ranks 6 and 13 are numeric table rows from CC BY-NC-ND papers
(facts, little expression); rank 9 (101 words, 36779245) is the reader's own description of a figure, missed by my first
rule and correctly treated as own text by the producer; rank 14 is an 85-word CC BY-NC-ND discussion paragraph; rank 5 is
the 134-word adverse-events paragraph of 40665325 (CC BY-NC-ND). Judgment: agrees with the producer on all 15; the only long
third-party prose under a non-open tag is rank 5 (and rank 14), correctly marked WATCH or low. The twelve runs of 50 or more
words with no licence tag (24369382 at 71 and 50 words; 17679088, 67; 21115974, 59; 33547201, 57 and 55; 33405376, 56;
40875931, 52; 25595186, 51; 33914858, 51 twice; 36537114, 50) are each one paragraph or one table row, as the producer
says. Caveats the producer already states hold: a
missing Europe PMC tag means "no CC licence recorded", not "copyright reserved"; dossiers and commit candidates were not
sampled.

## 4. OmniPath table tallies (task 4)

Computed from `inputs/signor_omnipath_edges.tsv.gz`, `inputs/collectri_omnipath_edges.tsv.gz` and
`inputs/resource_licences.tsv` (92 resources; every resource named in `sources` has a label):

| table | rows | only CC BY / CC0 / MIT / BSD (incl. CC BY 2.5) | adds BY-SA, nothing else | lists GPLv3 / LGPLv3 / ND / DSL / NAR / Informal / Artistic |
|---|---|---|---|---|
| SIGNOR | 55,760 | 55,465 | 156 | 139 |
| CollecTRI | 51,621 | 36,959 | 7,117 | 7,545 |

Exact match. A sensitivity check found no CollecTRI row whose resources are only the composite labels (Composite), so the
permissive class does not hide unlabelled rows. The resource labels named in `THIRD_PARTY_NOTICES.md` (BY-SA 4.0: TRRUST,
KEGG-MEDICUS, PhosphoPoint; BY-SA 3.0: SignaLink3, Guide2Pharma, TFe, ARN; GPL, LGPL, ND, DSL, NAR, Artistic, Informal)
match `resource_licences.tsv`. The labels are OmniPath's, as the notice says. The statement that BY-SA 3.0 rows may be
adapted under 4.0 rests on clause 4(b) of the 3.0 legal code (later version with the same elements) and on Creative
Commons' compatibility list; it was not re-read here.

## 5. History claims (task 5)

- Seven page crops of PMID 17803050: added in `ef20b9ef` (3 files) and `902f943e` (4 files), both 2026-08-09, removed in
  `de089055` (7 files, 2026-08-09). Reachable from `origin/main`, `development/main`, `origin/HEAD`, the local `main`, the
  local `backup/vps-main-2026-09-25` and every local task branch. Tip: no `page_adjudications/**/*.png` (0). Confirmed.
- Not in the producer's account (medium): a third commit, `d5da584b` (2026-08-09, "An adjudication artifact must contain the
  entire span it adjudicates"), replaced two of the crops with larger images (`p04_table1_organ_weights.png` 46,708 to
  205,304 bytes; `p04_table2_BUN_CRE_GLU.png` 50,822 to 97,428 bytes). The history therefore holds nine distinct image
  blobs, 2,260,814 bytes, across four commits. The seven final images removed by `de089055` total 2,163,284 bytes; the
  figure 2,031,445 bytes in the file matches neither number. A rewrite for R4 that names only `ef20b9ef` and `902f943e`
  would leave two superseded blobs reachable from `d5da584b`.
- Foundation letter: added in `8ab8e4b8` (2026-08-01, with a README change of 75 lines). The README (lines 31-32, 85-93)
  says the letter is "published here", that "the published copy ... reproduces the signed text in full, with the handwritten
  signature omitted", and that the Foundation's name, logo, letterhead and letter "are not covered by this repository's MIT
  License. All associated rights remain with the WWOX Foundation". `SPONSORSHIP.md` records only the sponsorship
  confirmation (2026-07-25). A search of tracked text (excluding the PDF and the research folder) found no record of
  permission to publish. The producer's statement stands. One addition: the file name carries "public" and the README
  speaks of a "published copy" distinct from a signed original, which suggests a public version was prepared; that is an
  inference, not a record.

## 6. Reserved decisions R1 to R7 (task 6)

| R | Alternative | Impact | Evidence preservation | Restore | Verdict |
|---|---|---|---|---|---|
| R1 | B-narrow in two steps, with a tip baseline | Correct; names that class-C-dependent positions drop to unknown | SHA-256 manifest, tag, `git bundle --all` | `git checkout <tag> -- <paths>` | Sound. Missing alternative: apply the repository's own precedent of `de089055` (publish the derivation, not the derived): untrack the merged catalogue, keep the builder, the cache manifest and the class-A subset (1,623 rows) tracked. It is stronger than "reduce" for the GtoPdb/ChEMBL rows and keeps research reproducibility. |
| R2 | Split by source licence; label the folder | Correct: GtoPdb cannot share a file with ChEMBL | As R1 | As R1 | Gap (low-medium): the text says the folder README would carry "third-party rows, not MIT" and calls it "done in the root notices only". `catalog/README.md` has no such label (`grep` finds none); the label is cheap, reversible and was not applied. Also not decided: whether `ligand_reconciliation.tsv` (3,030 rows) stays; it is stated as borderline. |
| R3 | Leave, tag per PMID, 50-word cap for new non-open snippets | Correct; audits compare snippets to sources, so only matching cuts are possible | Longer text in history and bundle | `git revert` | Sound. The 12 long runs are verifiably single paragraphs or rows (section 3). |
| R4 | No rewrite for the crops alone; fold into a privacy rewrite if one happens | Hash changes, seals and J2 anchors listed | Pre-rewrite bundle; hold on other copies | Bundle only | Two defects: (i) incomplete path/commit set (`d5da584b`, section 5); (ii) "ef20b9ef is far cheaper than ca506034" is not true in practice: `ca506034` (2026-08-06) precedes `ef20b9ef` and the numbers of descendants of each in the 3,896 commits of this branch are 3,830 and 3,798, a difference of 32 commits (under 1 per cent). Either point alone rewrites about 97 per cent of history. |
| R5 | Operator records one-line permission, else replace with a link and keep the PDF private | None on research; README lines named | PDF in history and private archive | `git checkout <sha> -- <pdf>` | Sound. Missing alternative: ask the Foundation, which the operator can do without a third party since the letter names the project lead in the Foundation's own role; and the record could simply be made in `SPONSORSHIP.md` with the date of the public version. |
| R6 | Regenerate both tables restricted to permissive and BY-SA labels, drop the 139 and 7,545 rows | Correct; 0.25 and 14.6 per cent of rows | Keep current tables and digests | `git revert` | Sound, and the percentages recompute (139/55,760 = 0.25; 7,545/51,621 = 14.6). Missing alternative: keep the tables and ship only the permissive-only subset publicly (a filter at release time instead of a re-run of P3). |
| R7 | Not prepared | n/a | n/a | n/a | Acceptable: each item needs contact, spend or an account action. |

## 7. Tests run by the verifier (task 7)

All commands were run in the producer's worktree with `LEGEND_CATALOG_CACHE` set to the root checkout's catalogue cache.

| Command | Result |
|---|---|
| `scripts/public_release_gate.py` | VERDICT: PASS, BLOCKS: 0, 30 REVIEW lines (parent-of-origin attribution notes on published-study records, same class as before) |
| `scripts/test_release_surface.py` | 11 tests, OK |
| `scripts/test_structured_data_integrity.py` | 4 tests, OK |
| `framework/scripts/repurposing_view.py package --check` | "package is current" |
| `framework/scripts/test_repurposing_view.py` (end to end, the producer did not run it) | Ran 146 tests in 1,097 s, OK (exit 0) |
| `repurposing_view.py audit-shareable --dynamic` (as specified) | static check PASS (0 violations) on `view/index_shareable.html`; the dynamic part then crashed twice with "Cannot read properties of null (reading 'innerText')" at the `#section=...` render |
| same, with the page-settle wait raised from 350 ms to 3,000 ms (driver in the verifier's scratch, no repository code changed) | PASS (0 violations) on `view/index_shareable.html` and PASS (0 violations) on `view/shareable_package/index.html`, including the rendered sections and briefs; exit 0 |

Diagnosis of the dynamic crash. The audit waits 350 ms after the load event before reading `#export-area`. Measured on this
host (load average about 12 from other actors), `#export-area` appears 0.4 to 1.2 s after load, for the producer's tree and
for the pre-P2 baseline (`fccf0a3f`, extracted into scratch) alike. The crash is a timing flake of a fixed wait under host
load, not a content regression of P2: the code under `framework/scripts` is identical between `fccf0a3f` and `HEAD`. Note
that the baseline run completed but reported its own violation (a compound/target pair in rendered first-screen text) in the
scratch extraction; its result is not used as a P2 finding (the extraction may lack untracked state). The audit script
should poll for `#export-area` instead of waiting a fixed 350 ms.

## 8. Severity-ranked defect list

None is critical or high: no licence conclusion of the producer is contradicted by a primary source.

Medium
1. M1, history under-count (section 5). The producer's account of the crops omits commit `d5da584b` and two superseded blobs; the
   stated size 2,031,445 bytes matches neither the final seven (2,163,284) nor all nine (2,260,814). Any rewrite or hosting
   takedown scoped from the file would miss them.
2. M2, R4 cost statement. "ef20b9ef is far cheaper than ca506034" is false in practice (32 commits apart out of 3,896; about
   97 per cent of history either way). The decision rests partly on that sentence.
3. M3, the dynamic audit cannot be run to a verdict as specified under load (flaky fixed 350 ms wait); the producer's
   "audit-shareable --dynamic" evidence is therefore not reproducible by a second actor on this host. With a 3,000 ms wait both pages pass the dynamic audit (section 7).

Low
4. L1, `catalog/README.md` has no "third-party rows, not MIT" label although R2 promises one as a stopgap; cheap and reversible.
5. L2, shipped package `NOTICE.md` keeps the untranslated redaction phrase in three places and it destroys the UniChem version
   string in the credit line.
6. L3, "no ChEMBL content" in the package notice leaves unexplained the origin of 1,506 embedded record names, among them the
   names of class-B compounds.
7. L4, CKB terms are readable at `ckb.jax.org` (CC BY-NC-SA 4.0); the producer left them UNVERIFIED and the notice cites an
   unresolvable host.
8. L5, missing alternatives: R1 untrack-and-ship-recipe precedent; R5 ask the Foundation and the "public version" inference;
   R6 release-time filter instead of a re-run.
9. L6, the own-description count 1,355 depends on an unstated rule (my two rules give 1,292 and 1,366); state the rule.
10. L7, DGIdb lists four further BY-SA or ODbL sources (HumanProteinAtlas, IDG, Pharos, MOAlmanac) not mentioned in the
    notices; no catalogue rows, raw responses not inspected.

Unverifiable from this host, as in the producer's file: ClinPGx, CGI, OncoKB, TTD, DTC, MyCancerGenome, UniProt, ClinVar
data use, GEO disclaimer, ClinicalTrials.gov terms, LINCS policy and SIGNOR pages.
