# Licence table for the IT9 generation path (P7, 2026-10-30)

Not legal advice. "Read" = the sentence was returned by the resource's own page on 2026-10-30 (WebFetch). UNVERIFIED = the page was
unreadable or unreachable from this host (the page content is a title, a browser check or a refused connection); it says nothing about the
terms. Counts of rows are the IT8 figures (`../licence_corrections_it8_20261029.md`), not recomputed here. Raw evidence kept next to this
file: `evidence/dgidb_source_licences_20261030.tsv` (DGIdb GraphQL, 48 sources, sha-256 in the README), reproduce with the curl line in section 3.

## 1. Resource, licence, what the repository redistributes, obligation

| Resource | Licence verified at the primary page | What the repository redistributes | Obligation met? |
|---|---|---|---|
| ChEMBL | Read 2026-10-30, `chembl.gitbook.io/.../about`: "made available on a Creative Commons Attribution-Share Alike 3.0 Unported License"; the page asks only for a citation (IT8 read the URL-plus-release wording on `chembl.github.io/chembl-licensing`) | merged catalogue rows (IT8: 16,947 + 8,068), 46 raw responses, 12 adapter-cache extracts, 12-record class-B file, ids in the page | raw responses, class-B file, adapter cache: yes (notice with licence and credit; adapter-cache coverage added in this commit). Merged catalogue: NO, MIT label contradicts BY-SA (R1/R2, reserved) |
| GtoPdb | Read 2026-10-30, `guidetopharmacology.org/about.jsp`: database "licensed under the ... (ODbL)"; "Its contents are licensed under a Creative Commons Attribution-ShareAlike 4.0"; citing is by a separate page (not read) | IT8: 16,070 rows in the merged catalogue; 3,030-row `ligand_reconciliation.tsv` (ids) | package (counts only): yes. Catalogue and reconciliation table: NO, open (R2) |
| Open Targets | Read 2026-10-30, `platform-docs.opentargets.org/licence`: "Open Targets Platform is marked with CC0 1.0"; citation of the latest publication requested | 1 adapter-cache file, `lucas_clarke_followup_20261026/opentargets_*` lists and counts | yes: no obligation; courtesy citation ADDED in `THIRD_PARTY_NOTICES.md` this commit (it was absent) |
| STRING | Read 2026-10-30, `string-db.org/cgi/access`: "freely available under the Creative Commons Attribution 4.0 (CC BY 4.0) license"; "credit STRING and indicate any changes or additions"; name STRING and its version in the metadata | nothing: `git grep` finds the string only in one deep-dive manifest quoting a paper | n/a today. If the IT9 network path stores STRING edges or scores in a tracked file: add a notice with the STRING version and "changes indicated" (CC BY 4.0), no share-alike |
| OmniPath (service) | Read 2026-10-30 (first 100,000 of 247,859 characters, as in IT8): licences are OmniPath's own search per resource; "Where we could not find anything about licensing, we assumed no license." OmniPath's own licence statement is not in the part read | two edge tables (SIGNOR-derived 55,760 rows, CollecTRI-derived 51,621) and `resource_licences.tsv` | attribution: yes. Mixed labels: open, IT8 counts (139 and 7,545 rows list a GPL/LGPL/ND/DSL/NAR/informal resource) -> R6 |
| TRRUST (rows inside CollecTRI) | Read 2026-10-29 (IT8), `grnpedia.org/trrust/`: CC BY-SA 4.0; not re-read today | rows inside the CollecTRI table | credit yes; share-alike scope: R6 |
| SIGNOR | NOT readable: `signor.uniroma2.it/about/` refused the connection on 2026-10-30 (as on 2026-10-29). OmniPath label CC BY 4.0 | the SIGNOR-derived table | credit yes; licence UNVERIFIED at source |
| LINCS / iLINCS | NOT readable: `lincsproject.org/.../data-policy` returned only a title on 2026-10-30. IT8 read the iLINCS "CC BY" statement on 2026-10-23 | signature metadata, census counts, 3.3 MB of tool responses (SigCom, L1000FWD service output) | credit yes (notice cites the iLINCS paper); service-output terms UNVERIFIED |
| GEO (GSE156243, GSE126075, GSE215425, GSE92742) | NOT readable: the GEO disclaimer returned a browser check on 2026-10-30. IT8 read the NCBI policy page 2026-10-29: no NCBI restriction, submitters may claim rights | derived per-gene or per-signature statistics, no matrices | yes for derived statistics with the deposit cited; GEO-specific disclaimer UNVERIFIED |
| DGIdb (container) | GraphQL queried 2026-10-30: 48 sources with a licence string and link, none for DGIdb itself; web pages are script-rendered (FAQ page returned only its title) | `catalog.jsonl.gz` (106,315 target rows of 22 claim sources), `coverage/associations.jsonl.gz`, raw responses | per source; class C (non-commercial / restrictive / unclear) is open (R1). Today's label for NCI is "Public domain" (IT8 treated the policy page as not naming the Cancer Gene Index): moving that source to class A is arguable, left to the operator |
| ClinPGx, DTC, CKB-CORE, CGI, OncoKB, COSMIC, TTD, MyCancerGenome, others | labels unchanged in the 2026-10-30 DGIdb answer (BY-SA 4.0; BY-NC-SA 3.0; BY-NC-SA 4.0; BY-NC 4.0; restrictive; free for non-commercial; unclear). Their own pages: unchanged status from IT8 (CKB and COSMIC read, the rest unreadable) | rows in the catalogue (IT8 counts) | open as in IT8, R1 |
| PubTator3 | NOT readable: the about page returned only its title on 2026-10-30; the cache files say "NCBI public domain"; NCBI general policy read 2026-10-29 by IT8 | 43 adapter-cache files | acknowledgement yes (notice, added); PubTator3-specific statement UNVERIFIED |
| openFDA | Read in IT8 on 2026-10-29: CC0 and a request for credit | 12 adapter-cache files, 8 attributes in the page | yes |

## 2. What changed in the repository in this commit

`THIRD_PARTY_NOTICES.md`: one entry for the adapter cache of the join step (ChEMBL extracts stay under CC BY-SA 3.0, openFDA, Open Targets
with its CC0 reading and courtesy citation, PubTator3 with its UNVERIFIED flag). Nothing else changed in licences; R1 to R7 are carried
below.

## 3. R1 to R7 after IT8

| item | state after IT9 P7 | needs |
|---|---|---|
| R1 class C rows in catalogue, coverage, raw responses | open, reserved (a content choice with research impact) | operator; proposal in README section 5 |
| R2 share-alike rows inside one MIT-labelled merged file | open, reserved; the interim label "third-party rows, not MIT" exists in the root notices and `catalog/README.md` | operator |
| R3 verbatim snippets and the 50-word cap | open; not a licence-compatibility declaration; no cap is introduced here (no verified need: IT8 found 12 runs of 50 or more words in 9 papers with no recorded open licence) | optional, operator |
| R4 page crops in history | open, reserved (rewrite or not) | operator |
| R5 Foundation letter | open, only the operator knows whether permission exists | operator, one question or one sentence in `SPONSORSHIP.md` |
| R6 mixed OmniPath edge tables | open; the release-time filter needs no code until the tables are shared outside the repository | operator, optional |
| R7 visibility, hosting request, rights-holder contact | reserved | operator |
| attribution gaps found in IT9 | adapter cache and Open Targets: FIXED here. STRING: no gap (nothing redistributed) | none |

Reproduce the DGIdb snapshot:
`curl -s -H 'Content-Type: application/json' -d '{"query":"{ sources { nodes { sourceDbName license licenseLink } } }"}' https://dgidb.org/api/graphql`.
