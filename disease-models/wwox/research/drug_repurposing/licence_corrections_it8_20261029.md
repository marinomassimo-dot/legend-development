# Licence corrections: from the census to practicable actions (IT8 P2)

Status: 2026-10-29, ACTOR scientist-d, branch `task/it8-p2`. Not legal advice. This file builds on
`licence_inventory_it7_20261029.md` (the census) and `../locator_audits/2026-10-29_it7_p8_licence_verifier.md`
(its verifier). It reads primary terms where they could be read, applies the reversible corrections, and prepares
the decisions that are the operator's. It does not change visibility, rewrite history, delete unique material,
contact a rights holder, register anywhere or spend. Privacy findings are out of scope (package P1).

Conventions. "Read" means the sentence was read on the source's own page on 2026-10-29 by this actor (WebFetch or
`curl`). "Reported by DGIdb" means only the DGIdb public GraphQL service says so (queried 2026-10-29,
`https://dgidb.org/api/graphql`, `sources { nodes { sourceDbName license licenseLink } }`; it returns a licence string and a
link for 48 sources and none for DGIdb as a whole). "UNREADABLE" means the page exists but is script-rendered,
returns 403, a browser check or does not resolve from this host; it is NOT a finding about the terms.
Status: OK (nothing to change), FIXED (changed in this commit), OPEN (needs the operator or a source we cannot read).

## 1. Per-component table (primary terms)

### 1a. Catalogue, aggregated sources and the container

| Component | Primary source, date | Clause in my words | What the repository does | Obligation actually triggered | Status / action |
|---|---|---|---|---|---|
| DGIdb (container) | `dgidb.org/api/graphql`, 2026-10-29 | The service lists a licence string and link per source; there is none for DGIdb itself. The web pages are script-rendered. | `catalog.jsonl.gz` (106,315 target rows), `coverage/associations.jsonl.gz`, raw `dgidb_*.json`, `kg_lookup/` | A container's label never grants rights in its sources' content (the DGIdb manifest even lists DoCM as "no licence identified" while DoCM says CC BY 4.0). Each row follows its own source (below). | FIXED wording: `DATA_SOURCES.md`, `THIRD_PARTY_NOTICES.md` now say "absence of a licence string, not a grant"; "software MIT" removed (unread). |
| ChEMBL (CC BY-SA 3.0) | `chembl.gitbook.io/chembl-interface-documentation/about` and `chembl.github.io/chembl-licensing`, 2026-10-29 | "The ChEMBL data is made available on a Creative Commons Attribution-Share Alike 3.0 Unported License." Attribution "should contain the url of the ChEMBL resource, and also the release version", example "ChEMBL data is from http://www.ebi.ac.uk/chembl - the version of ChEMBL is ChEMBL_07", shown on the entry portal or in the documentation of further distribution. | 16,947 + 8,068 ChEMBL-sourced target rows inside the merged catalogue; 46 unmodified ChEMBL web responses (`chembl_raw/`); class-B 12-record file in the package; ChEMBL ids in the page | Verbatim copies (the raw responses): licence copy or URI with every copy, credit, no further restriction (legal code 4(a), 4(c)). Adaptations (merged catalogue records): only under the same licence or a listed compatible one (4(b)). Verified wording of the policy file ("URL and release version") is now sourced to `chembl.github.io/chembl-licensing` (the verifier D8 had only read the gitbook page). | Raw responses: FIXED (notice with licence URI and credit line in `THIRD_PARTY_NOTICES.md`). Merged catalogue: OPEN, see 2 and 3.1. |
| GtoPdb (ODbL + CC BY-SA 4.0) | `guidetopharmacology.org/about.jsp`, 2026-10-29; ODbL text `opendatacommons.org/licenses/odbl/1-0/`, 2026-10-29 | "The Guide to PHARMACOLOGY database is licensed under the ... (ODbL)"; "Its contents are licensed under a CC BY-SA 4.0". ODbL: a Derivative Database that is Publicly Used must stay under the ODbL or a compatible licence (4.4), re-extraction of a substantial part into a new database is a Derivative Database, a Collective Database need not be (4.5), a Produced Work made from the database needs only a notice (4.3), notices and licence copy travel with a publicly conveyed database (4.2). DGIdb labels the same source CC BY-SA 4.0 only. | 16,070 GtoPdb rows in the merged catalogue; GtoPdb ligand ids in `ligand_reconciliation.tsv` (3,030 rows) | Both licences attach to the same rows; a merged file cannot also be MIT. Counts or ids alone are not an extraction of a substantial part, and the page (a Produced Work) embeds none. | Package: OK (counts only). Catalogue and `ligand_reconciliation.tsv`: OPEN (R2). |
| ClinPGx / PharmGKB (CC BY-SA 4.0) | `clinpgx.org/page/dataUsagePolicy` (301 from pharmgkb.org), 2026-10-29 | UNREADABLE: the page returns only its title. DGIdb reports CC BY-SA 4.0 with that page as the link. | 5,976 rows in the merged catalogue; counts only in the package | If CC BY-SA 4.0 is right: same as ChEMBL for adaptations. | OPEN (UNVERIFIED at source); counts-only stays. |
| DTC (CC BY-NC-SA 3.0) | DGIdb service 2026-10-29; DTC 2018 paper (verifier), DTC site unreachable | Reported by DGIdb as BY-NC-SA 3.0, with the DTC database paper as the link; the paper link itself was 403 here. | 23,879 rows in the catalogue | Non-commercial and share-alike; incompatible with the MIT label and with BY-SA files. | OPEN (UNVERIFIED at the DTC site). Class C stays. |
| JAX-CKB / CKB-CORE (CC BY-NC-SA 4.0) | DGIdb 2026-10-29; `ckb.genomenon.org/about/index` did not resolve | Reported only. | 2,148 rows | Non-commercial, share-alike. | OPEN (UNVERIFIED). Class C. |
| CGI (CC BY-NC 4.0) | DGIdb 2026-10-29 (link `cancergenomeinterpreter.org/faq#q19`: 403 / shell only) | Reported only. | 368 rows | Non-commercial. | OPEN (UNVERIFIED). Class C. |
| OncoKB | DGIdb 2026-10-29: "Restrictive, non-commercial"; `oncokb.org/terms` returned an error page | Reported only. | 148 rows | Non-commercial. | OPEN (UNVERIFIED). Class C. |
| TTD | `ttd.idrblab.cn` homepage, 2026-10-29: no licence or terms statement on the page returned; DGIdb: "Unclear. Website states All Rights Reserved but ... 2002 publication indicate open-access" | No grant found; absence of a licence is not a grant. | 15,246 rows | Without a licence, redistribution is not permitted by default. | OPEN. Class C. Counted, never embedded: unchanged. |
| COSMIC | `cancer.sanger.ac.uk/cosmic/license`, 2026-10-29 | Free for academic, not-for-profit use; commercial R&D, a commercial product or service and patient services need a commercial licence. | 37 rows | Non-commercial; the repository's MIT label allows commercial reuse of its content. | OK that the rows are class C; verified at source (was "custom terms, declared by DGIdb"). The 37 rows remain at the tip: part of R1. |
| MyCancerGenome (+ trials), CancerCommons, Clearity, TdgClinicalTrial, TEND, TALC | DGIdb 2026-10-29 (restrictive custom non-commercial; custom non-commercial; unknown, data no longer available; supplementary tables of copyrighted publications) | Reported only. | 829 + 317, 109, 240 + 163, 5,072, 2,242, 602 rows | Publisher or custom rights; no grant. | OPEN (UNVERIFIED). Class C. |
| NCI Cancer Gene Index | `cancer.gov/policies/copyright-reuse`, 2026-10-29 | "all text within National Cancer Institute (NCI) products is free of copyright" unless otherwise indicated and "may be reused without our permission"; credit NCI; graphics are a mix of copyrighted and copyright-free material; the page does not mention data or datasets and does not name the Cancer Gene Index. | 6,231 rows | If the text policy covers NCI-curated data, credit NCI; not established. | FIXED wording (verifier D4): "source page gone" replaced in `DATA_SOURCES.md`, `catalog/README.md`, `view/shareable_sources.json` and the package notice. Class C kept; moving to A is arguable and left to the operator (R1). |
| CIViC, DoCM, FDA PGx, openFDA, Open Targets, HGNC, MATRIX | read at their sources by IT5 P1 / IT7 (CIViC CC0, FDA public domain, DoCM CC BY 4.0 archived page, HGNC CC0, Open Targets public domain, MATRIX CC BY 4.0 for fields its authors own); openFDA re-read 2026-10-29 | openFDA: "public domain and made available with a Creative Commons CC0 1.0 Universal dedication"; "we ask that proper credit be given"; some data may not be public domain, such works are marked, GMDN content needs a licence. | CIViC 19, DoCM 3 and openFDA 8 attributes embedded in the page; rest in the catalogue | CC BY 4.0 for DoCM: credit, licence link, changes, no endorsement; others: courtesy credit. | OK; the package notice already meets these. |
| UniChem, DrugBank (ids) | `ebi.ac.uk/about/terms-of-use`, 2026-10-29 | "EMBL-EBI imposes no additional restriction ... than those provided by the data owner ... expects attribution." DrugBank is reported as custom non-commercial. | identifiers only | Attribution; no DrugBank content. | OK. |

### 1b. Other data, figures and services

| Component | Primary source, date | Clause | What the repository does | Obligation | Status / action |
|---|---|---|---|---|---|
| TRRUST (OmniPath-derived rows) | `grnpedia.org/trrust/`, 2026-10-29 | "freely available for both academic and commercial use under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license ... appropriate attribution ... adapted material is distributed under the same license"; cite the TRRUST paper. | rows in the CollecTRI edge table (and TRRUST_DoRothEA etc.) | Adaptations under BY-SA 4.0; credit | The BY-SA label is confirmed at the source. FIXED notice (see 3.5). The whole-table statement is narrowed because other rows carry other labels: OPEN (R6). |
| Other OmniPath resources | `omnipathdb.org/info` (first 100,000 of 247,859 characters read), 2026-10-29: OmniPath assigns each resource a label from its own search and states that where it found none it assumed none; users need a licence that grants use, modification and redistribution | Labels are OmniPath's, not the resources'. SIGNOR's own site was not reachable (P3 notice). | `resource_licences.tsv` (per resource), rows list their resources | Per row | FIXED: licence rows summarised in `THIRD_PARTY_NOTICES.md`; counts by compatibility computed (3.5). Resources' own sites UNVERIFIED. |
| GEO series (GSE156243, GSE126075, GSE215425, GSE92742) | `ncbi.nlm.nih.gov/home/about/policies/`, 2026-10-29; GEO disclaimer page returned a browser check | NCBI itself places no restriction on data it holds; submitters may claim rights; "there is no transfer of rights from submitters to NCBI". | derived per-gene or per-signature values and test results only (about 1.7 MB of tables); no matrices | Cite the deposit and paper; derived statistics are the repository's own computation. | FIXED (notice entry). GEO-specific disclaimer UNVERIFIED. |
| iLINCS / LINCS | `ilincs.org/ilincs/about` and ACKNOWLEDGEMENTS (read 2026-10-23): iLINCS "under Creative Commons (CC BY)"; LINCS data policy page UNREADABLE | Attribution by citing the iLINCS paper. | signature metadata, census counts, tool responses (`gse156243/tool_responses/`, 3.3 MB) | CC BY credit | FIXED (notice entry citing Pilarczyk 2022). The raw tool responses: kept as evidence; they quote service output (SigCom, L1000FWD), whose terms are UNVERIFIED. |
| ClinicalTrials.gov raw pages | NLM `databases/download/terms_and_conditions.html` and `web_policies.html`, 2026-10-29; ClinicalTrials.gov terms page UNREADABLE (script-rendered) | Acknowledge NLM with "Courtesy of the U.S. National Library of Medicine"; non-government content may be protected and the reuser must satisfy copyright. | 7 raw JSON pages in `clinical_census_20261020_raw/` (5.2 MB decompressed) | The acknowledgement; free-text fields come from registrants. | FIXED (acknowledgement added). Registrant free-text rights UNVERIFIED. |
| RefSeq NM_016373.4 `.gb` | NCBI policies page, 2026-10-29 | "Information that is created by or for the US government on this site is within the public domain"; asks for NLM acknowledgement. | one 18,784-byte record | Acknowledgement | FIXED (notice entry). |
| PRISM, Drug Repurposing Hub tags | DGIdb 2026-10-29: Hub "CC-BY 4.0"; PRISM "Supplementary data from Nature Publishing Group copyright publication". Hub site: certificate error (not bypassed) | Tags are provenance labels in prose, no rows. | 19 + 11 tags in `join/cards.json` | None beyond naming the source | FIXED (notice entry); site terms UNVERIFIED. |
| CC BY 4.0 / CC BY-SA 3.0 legal code | `creativecommons.org`, 2026-10-29 | BY 4.0: credit, link to licence, indicate changes (the page does not address sui generis database rights). BY-SA 3.0 Adaptation definition excludes a work that constitutes a Collection; 4(b): adaptation only under this licence, a later version with the same elements, a jurisdiction port or a listed compatible licence (local copy `LICENSES/CC-BY-SA-3.0.txt`, lines 188-214). | used for 3.1 | | OK |
| OpenFDA / DSLD | openFDA terms (above); DSLD documentation 403 on 2026-10-27, not retried successfully | openFDA CC0; DSLD unread | 1,005 name probes, counts (`dsld_probe_*.tsv`) | None for counts | OK for openFDA; DSLD UNVERIFIED, counts only. |
| Foundation letter PDF | repository README lines 31-32 and 85-93; `SPONSORSHIP.md`; `git log` | The README says the copy is "published here", reproduces the signed text without the signature, the signed original is "retained privately", and "all associated rights remain with the WWOX Foundation". The letter is addressed to the Anthropic AI for Science review committee, dated 30 July 2026, and names the project lead as the Foundation's Rare Disease AI Research Lead. `SPONSORSHIP.md` records that sponsorship was "formally confirmed to the project lead" (2026-07-25). | tracked since 8ab8e4b8 (2026-08-01) | A third party's text and letterhead; MIT excludes it | OPEN. No record of permission to publish the letter exists in the repository (searched `README.md`, `SPONSORSHIP.md`, `docs/`, `governance/`, git log): sponsorship is documented, permission to publish is not. See R5. |
| Page crops of PMID 17803050 | PubMed record read 2026-10-29: Comparative Medicine 2007;57(4):360-9, no licence line; Europe PMC: not in PMC, no licence, no full text; commit message de089055: the PDF states "Copyright 2007 by the American Association for Laboratory Animal Science", no Creative Commons mark, no DOI, no PMCID; publisher permissions page UNREADABLE (script shell 10.6 kB) | No open licence exists for the paper; a full-page crop with three complete tables is a reproduction, not a quotation. | 7 PNG (2,031,445 bytes) in history of ef20b9ef / 902f943e, removed in de089055 on 2026-08-09; reachable from `origin/main`, `development/main`, `backup/vps-main-2026-09-25`. At the tip: none (checked 2026-10-29: `git ls-tree` of this branch holds no `page_adjudications/**/*.png`). Recipe (digest, page, rectangle, dpi) kept. | The clearest unlicensed reproduction, in history only. | OPEN, R4. |
| Paper figures, supplements, XML, PDFs at the tip | `git ls-tree -r HEAD` extension census, 2026-10-29 | The only PNG/PDF/GB paths at the tip are own plots, own analysis PNG, the view's own screenshots and previews, the RefSeq record and the Foundation letter. No `.xml`, `.zip`, `.docx`, `.xlsx`, `.jpg`. `files/` is git-ignored. | | | OK. |
| Screenshots and PDF previews of the view (23 at the tip) | follow the catalogue rows they render | If the full view is rendered, class B/C names are visible. | `view/preview/` | follows R1 | OPEN, follows R1. |

## 2. What the share-alike conditions actually require here

Question: does the CC BY-SA ChEMBL file require the package index to be share-alike? What is "derived" for counts and identifiers?

1. The shareable package index (`index.html`, 1,485 `CAT:` ids, 260 `CHEMBL` ids, no ChEMBL mechanism, status or name text, counts only for B/C rows): the page embeds identifiers, own text and counts. Under the BY-SA 3.0 definition, a work is an Adaptation only if it is "based upon the Work"; the verbatim 12-record class-B file is the only place ChEMBL content sits and it carries its own licence copy, credit line and adaptation statement. The index is not placed under BY-SA by the licence text; the package also meets 4(a) for the class-B file as a "Collection" arrangement. This reading stands unless the operator or a lawyer concludes that a ChEMBL accession number or a count is protected expression. Neither the licence text nor the ChEMBL pages say so, and identifiers and counts carry little or no copyright; whether a database right (EU) covers a substantial extraction is a different question that the CC 3.0 unported text does not answer and that I did not verify. STATUS OK for the package.
2. What is "derived" for counts and identifiers: a count of rows by source and an identifier are facts about a database, not its expression; I treat them as not triggering share-alike, and I did not find a source that says otherwise. The line is crossed when field values of records are reproduced together (name, status, mechanism, target) or when records are merged and rearranged into a new database. That is what `catalog.jsonl.gz` does: each of its 44,211 records merges DGIdb, ChEMBL, MATRIX and openFDA fields, 106,315 target rows of 22 claim sources, with GtoPdb ligand data. It is an adaptation of ChEMBL (4(b): same licence), of GtoPdb (ODbL 4.4 and BY-SA 4.0 3(b) at once), and of DTC and CKB (NC-SA). Those obligations cannot be met together in one file, and the repository's MIT label contradicts every one of them. The notices already say "the MIT licence does not cover those parts"; this commit adds the missing per-source licence rows (1a) but does not make the merged file compliant. That is the single largest legal issue (R1, R2).
3. The 46 raw ChEMBL responses are Works, not Adaptations; their only condition (licence copy or URI, credit, no extra restriction) is met by the notice added here.
4. `ligand_reconciliation.tsv` (3,030 rows of GtoPdb and ChEMBL identifiers, InChIKeys and flags): identifiers and a derived flag; borderline; follows R2.

## 3. What was fixed in this commit (all reversible)

3.1 `THIRD_PARTY_NOTICES.md`: new section "Added components of the drug-repurposing and analysis work": GEO series, iLINCS/LINCS, ClinicalTrials.gov raw pages with the NLM acknowledgement, RefSeq record, PRISM and Drug Repurposing Hub tags, ChEMBL raw responses with licence URI and credit line, raw DGIdb and Monarch responses (not covered by MIT), DGIdb claim-source licence table as reported on 2026-10-29, OmniPath-derived tables with per-resource licence labels and row counts; one table row added.
3.2 NCI wording corrected in `DATA_SOURCES.md`, `catalog/README.md` (Licence reconciliation row), `view/shareable_sources.json` (counts-only entry and `claim_source_policy`), hence in the package `NOTICE.md`, `manifest.json` and the page footer.
3.3 DGIdb "no licence of its own (software MIT)" replaced by what was observed; ChEMBL attribution wording linked to its source page; ClinPGx row says why the policy page is unread.
3.4 `view/shareable_sources.json`: two identifier-source entries (GEO series and UniProt accessions, ClinVar-derived counts and the RefSeq accession) so the page credits what its own text cites; package regenerated.
3.5 `network_comparison_it7_p3_20261029/NOTICE.md`: TRRUST confirmed at its site; the claim that the whole table is CC BY-SA 4.0 is narrowed. Row counts (recomputed from `sources` x `resource_licences.tsv`):

| table | rows | only CC BY / CC0 / MIT / BSD | adds a CC BY-SA resource, nothing incompatible | lists a GPLv3 / LGPLv3 / CC BY-ND / DSL / NAR / Informal / Artistic resource |
|---|---|---|---|---|
| SIGNOR (`signor_omnipath_edges.tsv.gz`) | 55,760 | 55,465 | 156 | 139 |
| CollecTRI (`collectri_omnipath_edges.tsv.gz`) | 51,621 | 36,959 | 7,117 | 7,545 |

Known cosmetic defect left alone: the package `NOTICE.md` prints "un registro del repository (non incluso in questo pacchetto)" inside two English sentences (a redaction phrase that replaced a file name); the generator should use an English phrase in the English notice (a small builder change, not made here).

## 4. Verbatim quotation: sample judgments

Population (recomputed from `deepdive_manifests/*.json`, `verbatim_locators.entries[].snippet`): 9,433 snippets, 3,356 of 25 or more words. By my reading of the first words of each, 1,355 of those 3,356 are the reader's OWN description of a figure or a spreadsheet ("[figure attestation - pixels cannot be quote-matched]", "FIGURE ATTESTATION, not a quotation", "Visual attestation of ...", "[spreadsheet attestation ...]"); they are not third-party text. The other 2,001 (67,353 words, 457 papers) are candidate verbatim text. Europe PMC (`license` field, REST `search?resultType=core`, 2026-10-29) classifies those papers: CC BY 1,167 snippets (39,743 words); CC BY-NC-ND 298 (10,338); CC BY-NC 166 (5,258); CC BY-NC-SA 27 (966); no licence recorded (publisher copyright, or an author manuscript in PMC) 343 snippets (11,048 words), of which 12 snippets of 50 or more words in 9 papers. Runs of 50 or more words among candidate text: 97 CC BY, 34 NC variants, 12 no licence; of 100 or more: 6, 3, 0. So the headline "3,356 snippets of 25+ words" overstates third-party text by about 40 per cent, and 58 per cent of what remains is under a licence that permits reuse with attribution. The Europe PMC field is a machine tag, not a reading of each licence page.

The 24 longest candidate-text runs (up to two per paper; all 24 read in their first words and anchor):

| # | words | PMID | licence (Europe PMC) | what it is | judgment |
|---|---|---|---|---|---|
| 1 | 224 | 42909904 | CC BY | Results paragraph | Block of results text; permitted with attribution (CC BY). Attribution is present as PMID, anchor and artefact; add the licence name. OK |
| 2 | 185 | 42909904 | CC BY | Results paragraph | same. OK |
| 3 | 159 | 41980417 | CC BY | figure legend | CC BY. OK |
| 4 | 134 | 40665325 | CC BY-NC-ND | Results, adverse events | One paragraph quoted to anchor a safety statement; scholarly use; NC-ND allows verbatim non-commercial reuse with credit, but MIT downstream is not NC. Borderline length, low risk. WATCH |
| 5 | 109 | 40665325 | CC BY-NC-ND | numeric table rows (supplement) | Pharmacokinetic numbers; facts, little expression. Low. OK |
| 6 | 105 | 42310739 | CC BY | Limitations paragraph | CC BY. OK |
| 7 | 104 | 41980417 | CC BY | figure legend | CC BY. OK |
| 8 | 101 | 36779245 | CC BY-NC-ND | description of a figure | The reader's own description, not a quotation. OK |
| 9 | 98 | 42310739 | CC BY | Results paragraph | CC BY. OK |
| 10 | 98 | 24369382 | none (PMC author manuscript) | "FIGURE ATTESTATION, not a quotation" | Own description. OK |
| 11 | 94 | 24369382 | none | same | Own description. OK |
| 12 | 93 | 41257285 | CC BY-NC-ND | spreadsheet attestation (gene, logFC, P) | Own tabulation of numbers read from a supplement; facts. OK |
| 13 | 93 | 41090157 | CC BY-NC-ND | visual attestation of a figure | Own description. OK |
| 14 | 86 | 36779245 | CC BY-NC-ND | one row of a clinical table | Cohort data row; facts. Low. OK |
| 15 | 82 | 40156289 | CC BY | Discussion, limitations | CC BY. OK |
| 16 | 82 | 41124647 | CC BY | spreadsheet attestation | Own tabulation. OK |
| 17 | 82 | 34483921 | CC BY | Results paragraph | CC BY. OK |
| 18 | 82 | 41090157 | CC BY-NC-ND | visual attestation of an oncoplot | Own description. OK |
| 19 | 79 | 36235546 | CC BY | description of a flow diagram | Own description. OK |
| 20 | 78 | 38147624 | CC BY-NC-ND | supplemental methods, MTT assay | Routine methods text, 78 words; scholarly quotation purpose (to prove the control wording); NC-ND. Low. WATCH |
| 21 | 78 | 32000863 | CC BY | description of supplementary figures | Own description. OK |
| 22 | 77 | 34268881 | CC BY | spreadsheet attestation | Own tabulation. OK |
| 23 | 76 | 30175250 | CC BY | Discussion paragraph | CC BY. OK |
| 24 | 76 | 35945201 | CC BY | figure legend | CC BY. OK |

Second sample, the longest runs where no open licence is recorded (the cases that matter): 24369382 Brain 2014 (71 words, Discussion paragraph), 17679088 (67 words, Introduction final paragraph), 21115974 Blood 2011 (59 words, Discussion), 33547201 (57 words, a numeric table row; 55 words, Results paragraph), 33405376 (56 words, Results/Toxicities), 40875931 (52 words, Results), 25595186 (51 words, Introduction). Judgment for the 12 runs of 50 or more words (9 papers): each is one paragraph or one table row, quoted to let a reader verify a locator, with citation by PMID, anchor and artefact. For a scholarly-verification purpose, a single paragraph of a long article is commonly treated as quotation, but the rule differs by jurisdiction and I did not verify any; at 12 runs of 50-71 words the exposure is small, and the 343 runs of 25 to 49 words are at the ordinary scale of quotation. Conclusion: no snippet in the sample is substantial reproduction in the sense of the 7 page crops; the indicator is dominated by CC BY text and by the reader's own descriptions. Recommended low-cost control (not applied: it edits verified evidence): record the Europe PMC licence tag beside each manifest `pmid` and cap new snippets from papers without an open licence at 50 words (R3).

Dossiers and analysis notes (`fulltext_dossiers`, runs of 10+ words in double quotes, 53 of 25+ words, longest 94) and `commit_candidates` (up to 639 words, which on a sample quote the repository's own registry text): not sampled for licence in this commit. UNVERIFIED.

## 5. Reserved decisions (the operator's), each prepared

For every item: recommended alternative; research impact; evidence preservation; restore path.

R1. Class C (and uncertain) rows in the tip catalogue, coverage associations, raw DGIdb and Monarch responses (57,631 of 106,315 rows are class C; plus 132 raw files, 23.6 MB).
- Recommended: B-narrow, in two steps. (i) Keep the tip as is while the operator reads this file; a dated register is the baseline (alternative J of the census). (ii) If a change is wanted, replace in one task branch the C-labelled `targets[]` rows by claim-source counts and identifiers (reduce, alternative C), keeping the rebuild path `catalog_build.py` from re-downloaded DGIdb and ChEMBL releases; do not touch coverage until the replacement reproduces the join.
- Impact: the catalogue feeds `join/`, `coverage/`, the view and tests; positions that depend on class C rows (for example DTC-derived listings) would be recomputed from class A/B rows only and some would drop to "unknown". An offline-reproducible builder is the precondition.
- Evidence: before any removal, record SHA-256 of `catalog.jsonl.gz`, `associations.jsonl.gz` and each raw file in a manifest, tag the pre-change commit, and keep a bundle of the repository (`git bundle create --all`). Nothing is deleted from history.
- Restore: `git checkout <tag> -- <paths>`; or rebuild from the sources with the cached download manifest. After any history rewrite (R4) this path disappears, which is why R1 and R4 are decided together.

R2. Share-alike material inside one MIT-labelled merged file (ChEMBL BY-SA 3.0, GtoPdb ODbL + BY-SA 4.0, ClinPGx BY-SA 4.0).
- Recommended: split by source licence: a B file per source with its legal text and credit (the package already does it for 12 ChEMBL records), the merged catalogue holding ids, counts and own annotations only. Until then label `catalog/catalog.jsonl.gz` and `coverage/associations.jsonl.gz` as "third-party rows, not MIT" in the folder README (done in the root notices only).
- Impact: same as R1 for the B rows (47,061); GtoPdb cannot be put under one licence with ChEMBL, so the split is not optional if the rows are to stay public.
- Evidence and restore: as R1.

R3. Verbatim snippets (9,433; 2,001 of 25+ words are third-party text; 12 of 50+ words from papers with no open licence).
- Recommended: leave as is; add the licence tag per `pmid` and apply the 50-word cap to new snippets from non-open papers; shorten the 12 long runs to anchor + 49 words only if the operator prefers a conservative tip.
- Impact: the quote audit and locator audit tools compare snippets to sources; shortened snippets need the same match, so only snippets that still match their source can be cut (cut at sentence boundary, rerun the audits).
- Evidence: manifests are verified evidence, so keep the longer text in git history and in a bundle; record before/after digests.
- Restore: `git revert` of the shortening commit.

R4. Seven page crops of PMID 17803050 in history, and any history rewrite.
- Recommended: no rewrite for this alone (7 images, 2.03 MB, removed from the tip, the recipe regenerates them for a holder of the PDF). Record it in the register (alternative J); answer promptly to any notice by hosting-side removal. If the operator decides on a rewrite for the privacy findings of P1, include these paths in the same operation (alternative E/K), because the cost is set by the earliest commit and ef20b9ef is far cheaper than ca506034.
- Impact of a rewrite: every later commit hash changes; the census (sections 7 and 8) lists seals, SHA citations and the J2 deriver anchors that must be re-anchored.
- Evidence: pre-rewrite `git bundle --all` stored outside the repository; hold on the other copies (backup branch, VPS bundle, codex ref).
- Restore: the bundle; after clones and forks exist there is no full restore.

R5. Foundation letter PDF.
- Recommended: the operator records a one-line permission statement if it was given (for example in `SPONSORSHIP.md`: date and who agreed to publication of the letter and use of the name and letterhead); otherwise replace the PDF with a link and a summary and keep the PDF in a private location.
- Impact: none on research; README lines 31-32 and 85-93 would be edited.
- Evidence: the PDF stays in history and in the private archive. Restore: `git checkout <sha> -- docs/WWOX-Foundation-letter-of-support-public.pdf`.
- Nothing is removed here because only the operator knows whether permission exists.

R6. OmniPath-derived edge tables with mixed labels.
- Recommended: regenerate the two tables restricted to resources labelled CC BY / CC0 / MIT / BSD / CC BY-SA, drop the GPL/LGPL/ND/DSL/NAR/Informal-labelled rows (139 and 7,545), and re-run P3 on them; state the share-alike subset separately. Cost: one re-run of `fetch_network_inputs.py` and `p3_run.py` (network access to OmniPath).
- Impact: P3 numbers move slightly (the SIGNOR table loses 0.25 per cent of rows; the CollecTRI table loses 14.6 per cent). P3 pre-registration says no verdict depends on a single row, but the change must be reported as a deviation.
- Evidence: keep the current tables and digests in `inputs/` history. Restore: `git revert`.

R7. Visibility, hosting-provider request, contact with rights holders (NCI, TTD, DTC, CKB, CGI, OncoKB, ClinPGx, publishers). Not prepared beyond the census (alternatives F, G, I); each needs contact, spend or an account action.

## 6. Open and unverifiable

- At sources not readable from this host on 2026-10-29: ClinPGx data-usage page, CKB, CGI FAQ, OncoKB terms, DTC site, TTD terms, MyCancerGenome policy, UniProt licence page, ClinVar data-use page, GEO disclaimer, ClinicalTrials.gov terms, LINCS data policy, Drug Repurposing Hub site, AALAS permissions page, SIGNOR site, OmniPath info page beyond its first 100,000 characters, Monarch terms. The licence strings for these are DGIdb's or OmniPath's, not the sources'.
- Whether GitHub is public today, forks, caches, notices received: UNVERIFIABLE (census section 9).
- Whether the Foundation gave permission for the letter: UNVERIFIABLE (operator knowledge).
- Whether a Creative Commons 3.0 or 4.0 licence reaches database rights in a given jurisdiction, and the fair-use or quotation law for the 12 long runs: legal questions I did not research.
- Licence of the individual papers behind dossiers and `commit_candidates`: not sampled.
- Europe PMC licence tags are machine data; a tag absent for a paper in PMC means "no CC licence recorded", not "copyright reserved".

## 7. Reproduction

```
python3 -I - <<'E'   # quotation population: manifests -> snippets >= 25 words, attestation filter, Europe PMC license by PMID
E
curl -s -H 'Content-Type: application/json' -d '{"query":"{ sources { nodes { sourceDbName license licenseLink } } }"}' https://dgidb.org/api/graphql
git ls-tree -r HEAD | grep -E '\.(png|pdf|xml|jpg|zip|docx|xlsx|gb)$'
python3 framework/scripts/repurposing_view.py package && python3 framework/scripts/repurposing_view.py check && python3 framework/scripts/repurposing_view.py audit-shareable --dynamic
```
(`LEGEND_CATALOG_CACHE=.../drug_repurposing/catalog/cache` for the package and audit.) Europe PMC call: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid> AND SRC:MED&resultType=core&format=json`, field `license`.
