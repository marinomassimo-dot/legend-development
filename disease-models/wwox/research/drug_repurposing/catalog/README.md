# Compound catalogue

Non-canonical research material, built 2026-10-27 (iteration 3, `scientist-a`). A wide,
updatable, provenance-carrying list of **substances** that the drug-repurposing module can
look up. It says what exists, under which source and scope. It does **not** say that a
compound is suitable, safe, effective, or obtainable by anyone: accessibility, approval,
appropriateness and safety are separate fields, and the last two are always `NOT_ASSESSED`.
Nothing here is medical advice and nothing changes the four scientific current files.

## What is in the directory

| File | What it is | In git (once the task branch is landed) |
|---|---|---|
| `catalog_build.py` | fetch (cached, incremental) + build + query + verify; standard library only | yes |
| `test_catalog_build.py` | offline regressions on a synthetic cache, including the refusal and partial-build guarantees below | yes |
| `catalog.jsonl.gz` | the catalogue, one entry per line, deterministic (sorted, `mtime=0`) | yes (about 6 MB) |
| `catalog_stats.json` | every count the later view reads, with the reconciliation | yes |
| `card_links.json` | link of the curated cards to catalogue ids, with rule and an unmatched list | yes |
| `card_identity_declarations.tsv` | ten curator declarations (card -> ChEMBL id) used by the link rule `curator_declared_identifier` | yes |
| `ligand_reconciliation.tsv` | every GtoPdb-ligand relation of a DGIdb-only record (3 030 rows): candidate, ligand id, ChEMBL id, decision, reason code and the evidence fields; the sampling table for a verifier. Written by `build` | yes |
| `ligand_reconciliation_not_merged.tsv` | the same rows without `merged`: related-not-merged, rejected-conflict, out-of-selection, unresolved, each with its reason (2 545 rows) | yes |
| `non_molecule_modalities.tsv` | diets, gene replacement and other non-molecule modalities named by the cards, kept **out** of the molecule counts | yes |
| `dsld_probe_annotations.tsv` | hand-written (IT5 P10): per probed string, family, catalogue target and the ambiguity note (homonym, salt, form, mixture) | yes |
| `dsld_probe_results.tsv` | written by `catalog_build.py dsld-report`: per probed string, match type, text hits, sampled labels, equal-name and equal-group counts, DSLD group match and ids, date, ambiguity note | yes |
| `eu_context_probe.py`, `eu_context_probe.tsv` | European context probe (below): the two EU registers as published on the EU Open Data Portal, name counts only | yes |
| `cache_manifest.json` | per source: URL, retrieval date, version, sha256, bytes, licence, terms, last attempt status | yes |
| `cache/` | raw downloads (about 100 MB: ChEMBL pages, NDC zip, DGIdb TSVs) | **no** (gitignored); override with `LEGEND_CATALOG_CACHE` |

## Sources, what each really gave, licences

| Source | Used for | Measured 2026-10-27 | Licence / terms |
|---|---|---|---|
| ChEMBL (REST, `ChEMBL_37`, 2026-05-01) | backbone: molecule records with `max_phase`, `first_approval`, `molecule_type`, parent/child hierarchy, InChIKey, synonyms; all curated mechanisms (`action_type`, reference ids); targets | molecules with `max_phase>=0.5`, `max_phase=-1` (unknown phase), or `chemical_probe=1`, plus parents of selected salts; 7 561 mechanisms | CC BY-SA 3.0, re-verified 2026-10-28 (chembl.gitbook.io About). **Share-alike effect:** the ChEMBL-derived part of `catalog.jsonl.gz` (names, hierarchy, mechanisms, status records) is an adaptation and must be redistributed under CC BY-SA 3.0 with EMBL-EBI attribution; the file is a composite whose ChEMBL part keeps that licence |
| UniChem whole-source mappings (FTP, 3 small files) | identifier cross-references ChEMBL to DrugBank, ChEBI and FDA UNII | 3 files, under 1 MB | EMBL-EBI Terms of Use (the UniChem documentation points to them; **no CC0 statement was found, so none is claimed**); attribution expected |
| DGIdb `drugs.tsv` / `interactions.tsv` | approval flag per claim, gene-drug interaction type, claim source | **export of 2024-06-10** (the newest `/data/latest` serves; its ChEMBL claims are from ChEMBL 33); 81 572 claims, 98 239 interactions | **NOT CLEARED FOR PUBLIC RELEASE as a whole.** DGIdb states no data licence of its own: its software is MIT, and each claim keeps the terms of its source database (dgidb-data README, read 2026-10-28; DGIdb 5.0 paper: "We aggregate content from 44 sources with varying content licenses"). The repository is **public** (GitHub, `visibility: public`, checked 2026-10-28), so the earlier wording "the DGIdb-derived rows stay in this development repository" was wrong and has been withdrawn: the rows are published and the question is the operator's. Per-source terms for the 21 sources present in our rows: section below |
| GtoPdb `interactions.csv` + `targets_and_families.csv` + `ligands.csv` (guidetopharmacology.org/DATA, release 2026.3.1) | verification and correction of the gene named by DGIdb Guide-to-Pharmacology rows (target id, species, type, selectivity statement); not a target source of its own. `ligands.csv` (ChEMBL ID, InChIKey, Type, Withdrawn, Labelled, Radioactive) is used only to reconcile DGIdb-only records that carry an IUPHAR ligand id with ChEMBL records (section "Ligand reconciliation"). The ChEMBL `chembl_id_lookup` status of the ChEMBL ids that GtoPdb names and the selection does not hold is cached as `chembl/gtopdb_ref_lookup.json` and pinned in the manifest | 3 files, 24,968 interactions, 14,029 ligands (7,227 with a ChEMBL id); 3,708 ChEMBL ids looked up | database ODbL, contents CC BY-SA 4.0 (about.jsp, download.jsp, read 2026-10-28); public download, no registration. Share-alike applies to the GtoPdb-derived fields of `catalog.jsonl.gz`. The web-services API needs a key and is not used |
| Every Cure MATRIX drug list (Hugging Face, via datasets-server rows) | `approved_usa`, `gras_usa`, ATC, DrugBank and ChEBI ids for 1 927 live rows | HF commit `dc75f85…`, 1 935 rows declared = 1 935 received | CC BY 4.0, from the drug-list dataset-card metadata. The MATRIX knowledge graph and the **scores** table are separate artefacts: nothing is transferred to them from this licence; the scores have no declared licence and are not used | **Independent verification 2026-10-29:** class A applies only to the fields the MATRIX authors own (approval flags, names); the ATC, DrugBank and ChEBI identifiers inside are third-party and are identifiers-only (class C), because a dataset-card licence cannot grant rights in third-party content.
| openFDA `drug/ndc` bulk zip | the only open source of a US access category: `product_type` (prescription vs OTC), `marketing_category`, UNII | 138 143 products, export 2026-10-27 | CC0 / public domain (verified 2026-10-28 at open.fda.gov/license; the third-party GMDN notice on that site concerns device content, not the NDC fields used); openFDA disclaimer applies |
| NIH ODS DSLD API v9 (per-query) | dietary-supplement label evidence | 1 046 label probes OK, 0 errors (971 bulk-list names, interrupted, and 75 targeted: IT5 P10 added 51 compound-family strings and 68 ingredient-group lookups) | the API root page (`api.ods.od.nih.gov/dsld/v9/`, HTTP 200 on 2026-10-28) carries a licence block "CC0 1.0 Universal" and a version 9.4.0; the website `dsld.od.nih.gov` terms page returned 403 on 2026-10-28, so the terms are **not verified** for anything beyond counts, probes and DSLD's own ingredient-group ids and names; no label text is stored |

## Licence reconciliation (IT5 P1, read 2026-10-28)

Not legal advice. "Verified" means the sentence was read on the source's own page or code on that date;
"declared by DGIdb" means only DGIdb's own metadata says so. The DGIdb software state of 2024-06-07
(importer code, commit `a35759a` of `dgidb/dgidb-v5`, the last before our 2024-06-10 export) declares
the same licence strings as the live service for every source below, so the 2026 reading holds for the
version we hold. A container's licence does not clarify the content's: DGIdb's own manifest
(`dgidb/dgidb-data`, `dgidb_source_licensing.xlsx`, 2026-10-14) even lists DoCM as "no public dataset
license identified" while DoCM's own page says CC BY 4.0; the source's own page decides.

| claim_source (rows in `catalog.jsonl.gz`) | Terms | Reference | Verified at the content's own source? | Class |
|---|---|---|---|---|
| DTC (23,879) | CC BY-NC-SA 3.0 | declared by DGIdb (importer, API) | no (site unreachable today) | C |
| ChEMBL (16,947) | CC BY-SA 3.0 Unported; attribution must give the ChEMBL URL and the release version | chembl.github.io/chembl-licensing: "The required attribution should contain the url of the ChEMBL resource, and also the release version"; gitbook "about" | yes | B |
| GuideToPharmacology (16,070) | database ODbL, contents CC BY-SA 4.0 | guidetopharmacology.org/about.jsp: "licensed under the Open Data Commons Open Database License (ODbL) ... Its contents are licensed under a Creative Commons Attribution-ShareAlike 4.0 International License" | yes | B |
| TTD (15,246) | unclear ("All Rights Reserved" vs open access) | declared by DGIdb | no | C |
| NCI Cancer Gene Index (6,231) | declared public domain; the CGI wiki page named in DGIdb's importer is gone ("Page Not Found") and cancer.gov's reuse policy covers cancer.gov text only | cancer.gov/policies/copyright-reuse | **no** | C until verified |
| PharmGKB / ClinPGx (5,976) | CC BY-SA 4.0 | pharmgkb.org / clinpgx.org pages show it; the data-usage-policy page is script-rendered and its text was not read | partly | B |
| TdgClinicalTrial (5,072), TEND (2,242), TALC (602) | rights in a publisher's supplementary table | declared by DGIdb | no | C |
| JAX-CKB / CKB-CORE (2,148) | CC BY-NC-SA 4.0 (2024 importer and live) | declared by DGIdb | no | C |
| CIViC (1,120) | CC0 1.0 | docs.civicdb.org FAQ: "released under the Creative Commons Public Domain Dedication (CC0 1.0 Universal)" | yes | A |
| MyCancerGenome (829) + ClinicalTrial (317), OncoKB (148), CancerCommons (109), COSMIC (37) | restrictive / non-commercial custom terms | declared by DGIdb | no | C |
| FDA PGx biomarkers (427) | public domain | fda.gov website policies: "not copyrighted ... in the public domain and may be republished, reprinted and otherwise used freely"; credit appreciated | yes (FDA site policy, "unless otherwise noted") | A |
| CGI (368) | CC BY-NC 4.0 | declared by DGIdb | no (403) | C |
| Clearity (240 + 163) | unknown, data no longer available | declared by DGIdb | no | C |
| DoCM (76) | CC BY 4.0 | DoCM about page as archived in the project's GitHub history (docm.info now redirects to GitHub, so this is not a live page): "licensed under a Creative Commons Attribution 4.0 International License" | yes (CC BY 4.0: link to the licence, indicate changes, no endorsement) | A |

Other components. "Class" proposals are for the view allowlist (another worker owns the builder): **A** redistribute
with attribution; **B** share-alike, separate file with its own licence and credit; **C** identifiers and counts only;
**D** local only.

| Source | Content reused | Terms and reference | Conditions | Class and alternative |
|---|---|---|---|---|
| ChEMBL release `ChEMBL_37` (2026-05-01; DGIdb claims carry ChEMBL 33) | names, hierarchy, status, mechanisms, reference ids | CC BY-SA 3.0 (above) | attribution with URL and release; adaptations redistributed under the same licence (CC legal code 4(b)) | B; or ChEMBL ids plus our own annotations only |
| GtoPdb 2026.3.1 (public download) | target id, species, selectivity used to verify and correct DGIdb GtoPdb rows; GtoPdb-derived claim rows | ODbL database, CC BY-SA 4.0 contents (about.jsp, download.jsp) | ODbL 4.4: a Derivative Database that is publicly used stays under ODbL or a compatible licence, with notice; BY-SA 4.0 3(b): adapted material under BY-SA or a listed compatible licence | B (two licences: do not merge into one file); or target ids and gene symbols |
| GtoPdb 2026.3.1 `ligands.csv` + ChEMBL `chembl_id_lookup` (status of ids outside the selection) | ligand ChEMBL id, InChIKey, type and withdrawn/labelled flags, used to decide and to record `relations.gtopdb_reconciliation` (tag `gtopdb_ligand_chembl_ref`) on DGIdb-only records; ChEMBL id status | ODbL database, CC BY-SA 4.0 contents (GtoPdb); CC BY-SA 3.0 (ChEMBL); each relation carries both terms in its `terms` field and the asserting source and release in `asserted_by` | the relation is an adaptation of both: share-alike with attribution; the identifier chain is a fact about the sources and is kept with its provenance, not an untraceable merge | B; or counts and decision codes only |
| PharmGKB / ClinPGx | claim rows via DGIdb | CC BY-SA 4.0 | as above | B; or ids and "see ClinPGx" |
| openFDA NDC (export 2026-10-27) | product type, marketing category, UNII | open.fda.gov/terms: "public domain and made available with a Creative Commons CC0 1.0 Universal dedication"; credit asked, not required: "Data provided by the U.S. Food and Drug Administration (https://open.fda.gov)"; works to which CC0 does not apply are marked | do not imply endorsement; openFDA disclaimer | A |
| Every Cure MATRIX drug list (HF commit `dc75f85`) | approval flags, ATC, ids, names | HF dataset-card licence field `cc-by-4.0` (card prose not rendered; read 2026-10-28). The scores table is a separate artefact with no declared licence and is not used | CC BY 4.0 attribution, indicate changes | A | **Independent verification 2026-10-29:** class A applies only to the fields the MATRIX authors own (approval flags, names); the ATC, DrugBank and ChEBI identifiers inside are third-party and are identifiers-only (class C), because a dataset-card licence cannot grant rights in third-party content.
| UniChem mappings | ChEMBL to DrugBank / ChEBI / UNII identifier pairs | UniChem docs point to EMBL-EBI Terms of Use (ebi.ac.uk/about/terms-of-use; the unichem termsOfUse page is 404): "EMBL-EBI itself places no additional restrictions on the use or redistribution of the data ... other than those provided by the original data owners"; "expects attribution". No CC0 statement exists and none is claimed | attribution | A for identifiers; DrugBank content beyond the id is not carried |
| DrugBank | identifiers only | DGIdb: custom non-commercial | no DrugBank text or tables | ids only |
| NIH DSLD | 1,005 name probes, counts only | documentation page returned 403 today; "CC0" is the repo's earlier reading (2026-10-27), not re-verified | none shipped beyond counts | C |
| Open Targets | one cached API response | platform-docs.opentargets.org/licence: "dedicates the data to the public domain"; upstream sources keep their terms | none beyond citation | A (counts, ids) |
| HGNC | symbols and ids | genenames.org/about/license: "all data is released under the Creative Commons Public Domain (CC0) License"; attribution not mandatory | none | A |
| DailyMed | `DailyMed:id` strings inside ChEMBL references; no label text | NLM policy: government works not copyrighted; manufacturer content may be; DailyMed page states no reuse terms | do not ship label text | ids only |
| ClinicalTrials.gov | NCT ids and counts in the census | terms page is script-rendered; no sentence read | ids only | ids only |
| PubMed / PMC | PMIDs, titles in `join/pubmed_cache`, locator pointers; no abstracts or passages found in `cards/`, `join/` or the views | NLM policy: article and abstract rights stay with rights holders | keep it so; quote only briefly with citation | A for bibliographic facts; D for any passage |
| PubTator3 | 43 empty or tiny cached responses | NCBI policies page | none | A |

Proposed `shareable_sources.json` changes (not applied here): move **NCI** from `dgidb_claim_sources` to
counts-only until the Cancer Gene Index terms are read at NCI; keep FDA, CIViC, DoCM (all three verified at
their own source today); keep ChEMBL, GtoPdb, PharmGKB/ClinPGx counts-only in the single shareable file, and
if they are wanted, add class B files `catalog_chembl_cc-by-sa-3.0.jsonl.gz`, `gtopdb_odbl.jsonl.gz`,
`clinpgx_cc-by-sa-4.0.jsonl.gz`, each with its licence text and credit line; add UniChem, HGNC and Open Targets
as identifier-only sources with credit; keep DSLD counts-only. Until a component is verified, new results use
a projection with compatible terms and the uncertain rows are not widened.

Not obtained, stated plainly: **no open bulk list of dietary supplements** exists that carries
identifiers (the NDC directory has no supplement product type; DSLD labels carry no UNII, so
supplement evidence is name-only and US-only); **no Italian or EU access source was ingested**.
A quick look (2026-10-28) found two candidates and stopped there: AIFA publishes open data under
CC BY 4.0 as CSV/XML (`aifa.gov.it/en/open-data`, "liste dei farmaci", transparency lists) and EMA
publishes website data as JSON (`ema.europa.eu/en/about-us/about-website/download-website-data-json-data-format`,
centrally authorised medicines only). Neither download URL was verified or fetched, neither
carries a dietary-supplement list, and **a US classification (OTC, prescription, supplement) is
not an Italian one**. 9 223 US Rx/OTC NDC products have no UNII and cannot be linked by
identifier. DrugCentral was not used (no light open bulk file was verified).

**DGIdb is an old export.** The TSV is dated 2024-06-10 and carries ChEMBL 33 claims, next to
ChEMBL_37 (2026-05-01). The live DGIdb service reports newer source versions (for example
Wikidata 20240411 in the export vs 20260901, RxNorm 20240401 vs 20260803, CIViC 10-Apr-24 vs
01-September-2026); `catalog_stats.json` key `dgidb_age` lists them. Only the export's rows are in
the catalogue: the current service coverage was **not** ingested.

**Supplement probe, what was run.** `probe-dsld` queried the US DSLD for 1 005 names (981 of the
bulk list, interrupted, so 3 716 bulk names have no supplement evidence either way, which is
*unknown*, not negative) plus a targeted set of LEGEND-relevant names: lithium (+ carbonate,
orotate), memantine, pyridoxine / vitamin B6 / pyridoxal 5'-phosphate, dichloroacetate, taurine,
creatine, beta-hydroxybutyrate, medium-chain triglycerides, cannabidiol, carnitine, melatonin,
ursodeoxycholic and tauroursodeoxycholic acid, phenylbutyrate, thiamine, riboflavin, magnesium,
vigabatrin, bumetanide, bortezomib, and one nonsense control. Results (full-text hits / label
ingredient names equal to the query in the first 50): lithium 439/50, lithium carbonate 12/3,
taurine 6 978/50, creatine 3 957/49, melatonin 3 144/50, cannabidiol 661/49,
tauroursodeoxycholic 46/46, pyridoxal 5'-phosphate 3 466/27; **memantine, dichloroacetate,
phenylbutyrate, vigabatrin, ursodeoxycholic acid: 0 hits** (consistent with drug-only
substances); **pyridoxine 30 429 hits but 0 equal names** (labels list it under the group
"Vitamin B6"; this is the limit of name matching, and it shows that a 0 is not a negative);
**"Vitamin B" 34 740 hits, 0 equal names** (ambiguous term); the nonsense control returned 0.
Where a name matched, the entry carries `supplement` with `strength: name_only`, `matched_on`,
example label ids and the retrieval date. It never asserts chemical identity (salt, form, dose
and product are unknown) and never an Italian status.

## Entry fields (one line of `catalog.jsonl.gz`)

`id` (`CAT:CHEMBL…`, `CAT:DGIDB:<sha1-12 of DGIdb drug_name>`, `CAT:UNII:…`, `CAT:EC:…`, stable
because it is the source id) · `name`, `name_source`, `synonyms` (capped at 40; `n_synonyms_total`
is real) · `ids` (ChEMBL, InChIKey and its first block `skeleton_key`, UNII, DrugBank, ChEBI,
DGIdb name, MATRIX id) · `relations` (`parent`, `is_parent`, `children`) · `molecule_type`,
`modality`, `chemistry` · `status_records` (a **list**, one per source, each with its own `scope`
sentence) and `status_class` (a derived one-word summary, rule below) · `access` (a **list** of
`{category, scope, strength}`) and `access_categories` · `targets` (ChEMBL curated mechanism with
`action_type`, genes, UniProt, reference ids as `PubMed:id`/`DailyMed:id`; DGIdb interaction with
type and claim source; **no potency or score is copied**) · `source_records`, `provenance` ·
`appropriateness` and `safety_assessment` = `NOT_ASSESSED`.

### Access category (multi-valued, scoped, never inferred from approval)

* `prescription` / `OTC`: openFDA NDC finished human products carrying the entry's UNII (UNII
  reaches ChEMBL entries through UniChem). Homeopathic listings do not count as OTC access.
  A UNII shared by several salt entries is attached to each and flagged, not collapsed. Scope
  sentence names the directory date and says "US".
* `supplement`: a DSLD label whose ingredient name equals the entry name after normalisation.
  `strength: name_only`, because DSLD offers no identifier. Only probed names can get it.
* `experimental`: ChEMBL clinical-candidate (`max_phase` 0.5 to 3) or chemical-probe statement
  and no approval statement in any source used. It says nothing about obtainability.
* `unknown/unverified`: everything else, including approved compounds with no NDC match. It is
  **not** a negative: country, product and date dependent.

### `status_class` (derived, one per entry; the records stay in `status_records`)

`approved_any_source` (ChEMBL max_phase 4, DGIdb approved TRUE or MIXED, MATRIX APPROVED, or an
NDA/ANDA/BLA NDC product) > `marketed_otc_monograph` > `marketed_unapproved_us` >
`clinical_candidate` > `phase_unknown` > `tool_probe` > `no_status_statement`. The scope of each
statement is in the record: ChEMBL `max_phase` is "highest phase curated for any indication",
**not** an agency statement.

## Identity, deduplication, and what was merged

Entries are **never** merged on name. Evidence from another source is attached to an entry
only through a declared identifier key: ChEMBL id; UniChem ChEMBL to DrugBank, ChEBI or UNII;
DGIdb `chembl:` concept ids (DGIdb groups its claims by `drug_name`, its own rule); MATRIX
`drugbank_id` or ChEBI id through UniChem. Salts, stereoisomers and formulations stay separate
ChEMBL entries with `parent` / `children` kept and a shared `skeleton_key` (InChIKey first
block) so a reader can see the family. The merge report in `catalog_stats.json` says
`entries_merged_away: 0` and lists how many source rows were attached by which key. A source row
that no identifier connects to a ChEMBL entry becomes its own entry, so **the entry count is an
upper bound on distinct substances**: a DGIdb or openFDA entry can describe a substance that a
ChEMBL entry also describes. One-to-many links are flagged `multiplicity`.

### Ligand reconciliation (IT5 P4): the one exception to "never merged on anything but a ChEMBL id", and why it is not a merge

DGIdb-only records that carry an IUPHAR/GtoPdb ligand id (`iuphar.ligand:N`; 6 567 records, 6 597
record-ligand pairs) can be reached from a ChEMBL record through GtoPdb's own ChEMBL id. The rule,
in `catalog_build.py` (`reconcile_gtopdb_ligands`), decides every pair on **identifiers and structure
only**; a name coincidence is stored as evidence (`name_agrees_not_a_basis`) and decides nothing:

```
DGIdb concept iuphar.ligand:L  ->  GtoPdb ligands.csv row L  ->  its "ChEMBL ID" R  ->  ChEMBL record R of the catalogue
```

| decision | when | effect |
|---|---|---|
| `merged` | R is a record of the catalogue (ACTIVE: the molecule record is present), the GtoPdb and ChEMBL standard InChIKeys are **equal in all three blocks**, the ligand is not labelled/radioactive, no contradicting identifier (a DrugBank id of the record disjoint from the UniChem DrugBank ids of R; a DGIdb `chembl:` concept id other than R), and the record does not join two different chemical families | `relations.reconciled_via = "gtopdb_ligand_chembl_ref"`, `relations.family_join = [CAT:R]`; the record joins R's family (`repurposing_search.families`). **No record is created, deleted or fused**: it keeps its own targets, status, access and provenance; R gains `relations.reconciled_source_records` |
| `related_not_merged` | same connectivity block but a different stereo/isotope block (enantiomer vs the other, single enantiomer vs racemate or a flat drawing, isotopologue) or protonation/charge block; or a labelled/radioactive ligand (`[3H]...`); or the ligand's structure equals the **parent** of a salt/derived form that GtoPdb names (parent vs salt not settled) | relation kept with the code; **family not joined**, because a pharmacological distinction may be lost |
| `rejected_conflict` | the connectivity blocks of the two InChIKeys differ: the identifiers do not describe the same structure (a shared or similar name does not help) | relation kept with the code; nothing joined |
| `out_of_selection` | R is ACTIVE and a compound in ChEMBL but not a record of the catalogue's selection | relation kept with R as a reference (`chembl_ref_in_catalogue: false`); nothing joined, nothing dropped; becomes a candidate if a later selection enumerates R |
| `unresolved` | structure unavailable on one or both sides (antibodies, oligonucleotides, inorganic); R INACTIVE/obsolete, not a compound, or unknown to the ChEMBL lookup; the ligand id absent from the GtoPdb release; a contradicting DrugBank or DGIdb ChEMBL id; one record that would join two chemical families | relation kept with the reason code; nothing joined |

Measured on GtoPdb 2026.3.1, the DGIdb export of 2024-06-10 and ChEMBL_37 (all 6 597 pairs; `catalog_stats.json`, key
`gtopdb_ligand_reconciliation`):

| | pairs | of which ChEMBL id in the catalogue (the 510 candidates of IT4) |
|---|---|---|
| ligand id absent from the release | 2 | - |
| ligand without a ChEMBL id in GtoPdb (no relation) | 3 567 | - |
| `merged` | 485 | 485 |
| `related_not_merged` | 14 (7 labelled/radioactive, 3 stereo defined in ChEMBL only, 3 stereoisomers differ, 1 parent form named through a salt id) | 14 |
| `rejected_conflict` (connectivity differs) | 4 | 4 |
| `out_of_selection` (ACTIVE compound, not in the selection) | 2 472 | 0 |
| `unresolved` | 55 (44 ChEMBL id INACTIVE, 1 unknown to the lookup [PBF-509: its GtoPdb id is not a compound record], 6 structure unavailable, 1 disjoint DrugBank ids [ADL5859: identical full InChIKey, held back only by the disjoint ids], 2 ligand ids absent, 1 other) | 7 |

Not a basis for a decision, recorded as evidence: the name, the GtoPdb `Withdrawn` flag and ChEMBL
`withdrawn_flag` (a market withdrawal is a status, not an identity statement; both are in the evidence
and the status records are untouched), the ChEMBL chirality code. A ligand with no ChEMBL id in
GtoPdb makes no relation (3 567 pairs, counted). One-to-many: several GtoPdb ligands naming one ChEMBL
id are each decided on their own structure (the count is in the evidence); one record with several
ligand ids joins at most one chemical family, and is left `unresolved` if two would be needed.
Provenance: every relation names the asserting sources (`asserted_by`: DGIdb concept id and export, GtoPdb
release and column, ChEMBL release) and carries the licence terms (`terms`): the relation is an adaptation of
GtoPdb (ODbL / CC BY-SA 4.0) and ChEMBL (CC BY-SA 3.0) content, share-alike with attribution.
`ligand_reconciliation.tsv` (every relation, sampling-ready) and `ligand_reconciliation_not_merged.tsv`
(everything but `merged`) are written by `build`. The family effect is the only count effect: the number
of **records** does not change; the number of **families** of the coverage tool falls by the number of
joined records (a joined record no longer counts as a family of its own).

## Units: what each number counts (`catalog_stats.json`, key `units`)

| Unit | Count | Reading |
|---|---|---|
| Records enumerated | 44 211 | source-level substance records. **Not distinct drugs, not distinct chemical entities**: a salt, a stereoisomer and a source-only row each count once |
| ... by origin | ChEMBL selected 19 926, ChEMBL parents added 7, DGIdb-only 22 557, MATRIX-only 502, openFDA-UNII-only 1 219 | the entry that created the record |
| External declared total | ChEMBL: 2 921 148 distinct compounds | the database's own figure; **not** records acquired, never added to them |
| Chemical families reconciled (ChEMBL records only) | 16 475 families; 2 965 with more than one record (6 423 records); largest 13 | parent/child hierarchy or identical InChIKey first block; shown, nothing merged |
| Source-only records joined to a ChEMBL family by ligand reconciliation | 485 DGIdb-only records | `relations.reconciled_via = gtopdb_ligand_chembl_ref`: GtoPdb ligand to ChEMBL id with an equal standard InChIKey; the records stay (the record count does not change), only the family grouping of the coverage tool does (section "Ligand reconciliation") |
| Possible duplicates / unresolved identities | 23 793 source-only records have no identifier link to a ChEMBL record (24 278 before the 485 joins); 8 751 of them have a normalised name equal to a ChEMBL name or synonym | **not merged**; the coincidence is a review flag, identity is unresolved |
| Modalities | small molecule 15 053, antibody 1 032, protein/peptide 986, oligonucleotide 209, other biologic classes, **unknown 26 235** (source-only rows) | unknown is not small molecule |
| With pharmacological data | 6 328 with a ChEMBL curated mechanism; 18 855 with a DGIdb interaction; 24 423 with any target link; 1 518 distinct ChEMBL target ids, 5 302 gene symbols | a source statement with action type and reference ids; not potency, not relevance to WWOX |
| **Evaluated against WWOX needs** | **0** | no needs matrix exists yet; nothing in the catalogue is scored or ranked for the disease |

Bioactive-molecule universe vs usable-drug universe: the former is the ChEMBL total above; the
catalogue enumerates 19 933 of its records plus source-only rows. The latter is the subset with
US prescription, OTC or supplement evidence on a date (2 901 records with prescription, OTC
evidence from NDC, or a name-only supplement match; overlapping categories are in
`access_category_overlapping_counts`, and the non-overlapping signature counts sum to the total).
Neither is an appropriateness or safety statement. Modality: only entries with a molecule record
count as molecules; diets, gene-replacement vectors and editing systems named by the cards are in
`non_molecule_modalities.tsv`; NDC allergenics, vaccines, plasma derivatives and cell therapies are
excluded from the openFDA-created entries.

## Completeness checks (`catalog_stats.json`, key `source_verification`)

Each build recomputes the sha256 of every cached file against `cache_manifest.json` and compares
declared and received counts: ChEMBL molecule queries 16 809, 2 499, 807 and 7 parents (all equal
to the paging `total_count`), 7 561 mechanisms, 1 518 targets; NDC parsed records equal the
declared total (138 143); MATRIX rows equal the declared 1 935. All coherent on 2026-10-28. A
failed or short download is recorded `FAILED` / `INCOMPLETE` with expected and received counts, the
previous complete retrieval is kept and shown as `STALE_AFTER_FAILED_REFRESH`, and a source never
fetched shows `NOT_FETCHED` (absent, never zero). `build` refuses to run without a complete ChEMBL
backbone.

## Acquisition (network) vs build (offline)

```bash
python3 -B catalog_build.py fetch                 # NETWORK. Skips sources newer than 30 days; --refresh / --only chembl,dgidb to force
python3 -B catalog_build.py probe-dsld [--names a,b] [--retry-errors] [--limit N]   # NETWORK, optional, resumable, 3 parallel requests
python3 -B catalog_build.py probe-dsld --names "a,b" --refresh   # NETWORK, targeted: one request per second, appends detail fields (name/group/partial counts)
python3 -B catalog_build.py probe-dsld-groups --names "a,b"      # NETWORK, DSLD ingredient-group index (group id, DSLD's own synonyms), one request per second
python3 -B catalog_build.py dsld-report                          # OFFLINE. writes dsld_probe_results.tsv from the cache and dsld_probe_annotations.tsv
python3 -B catalog_build.py inputs                # OFFLINE. what the declared version needs: present / missing / mismatching, and how to get each
python3 -B catalog_build.py build                 # OFFLINE. cache -> catalog.jsonl.gz, stats, card links (about 25 s); REFUSES on an incomplete cache
python3 -B catalog_build.py verify                # OFFLINE. counts reconcile
python3 -B test_catalog_build.py                  # OFFLINE. regressions on a synthetic cache
python3 -B catalog_build.py all                   # fetch then build
```

`build` never touches the network (a regression test forbids it); the ChEMBL entity-type lookup
for ids mentioned in cards is part of `fetch`.

## Reproducing the declared version (and what a build refuses to do)

The **declared version** is what `cache_manifest.json` records as the last complete retrieval of
each source: version string, URL, and the sha256 of every file. The cache is the gitignored
`cache/` of the **root checkout**; a git worktree does not have it. A build therefore starts by
checking every file the declared version needs: it must exist, and its sha256 must equal the
manifest. Two files the manifest does not hash are checked for presence only:
`chembl/id_lookup.json` (written by `fetch`; without it every card id stays `UNRESOLVED` and
`card_links.json` changes) and `dgidb/live_sources.json` (the `dgidb_age` comparison).
`dsld/probes.jsonl` and `dsld/groups.jsonl` are append-only; since IT5 P10 the manifest pins their sha256 (the pin moves with each probe run, by design: `probe-dsld` and `probe-dsld-groups` rewrite it), so a build against a probes file that differs from the declared one is refused like any other mismatch.

Reproduce, in a worktree or anywhere else, with separate commands:

```bash
LEGEND_CATALOG_CACHE=/path/to/root/disease-models/wwox/research/drug_repurposing/catalog/cache python3 -B catalog_build.py inputs
LEGEND_CATALOG_CACHE=/path/to/root/disease-models/wwox/research/drug_repurposing/catalog/cache python3 -B catalog_build.py build --check
LEGEND_CATALOG_CACHE=/path/to/root/disease-models/wwox/research/drug_repurposing/catalog/cache python3 -B catalog_build.py build
```

* `inputs` lists each required file with its status (`OK`, `PRESENT_UNHASHED`, `MISSING`,
  `HASH_MISMATCH`), source, pinned hash and the acquisition command; exit 1 if anything is
  missing. In a worktree it also prints the root checkout's cache path.
* `build --check` rebuilds in memory, writes nothing and compares the result with the committed
  `catalog.jsonl.gz`; exit 0 and `MATCH: byte-identical` if the cache reproduces it, exit 4 otherwise.
* `build` replaces the outputs only from a complete, matching cache. The files are staged as
  `*.stage` and moved over the targets only after the build and the count reconciliation passed, so a
  failed build leaves the last valid `catalog.jsonl.gz`, `catalog_stats.json` and `card_links.json`
  as they were.
* On a missing or mismatching input, `build` **refuses** (exit 3), names each file, and says how to
  proceed: point `LEGEND_CATALOG_CACHE` at a cache that holds it, or `fetch --only <source>`.
  `fetch` downloads what is served now (keyless public downloads only: EBI/ChEMBL, UniChem FTP,
  DGIdb, guidetopharmacology.org, Hugging Face, api.fda.gov). The DGIdb and GtoPdb URLs serve
  "latest", so a re-download can differ from the declared files; the build then reports
  `HASH_MISMATCH` until the manifest is updated by that fetch, at which point it is a **new
  catalogue version**, not a reproduction. Exact reproduction needs the original cache files.
* Missing the ChEMBL backbone is always refused. Otherwise an explicit, separate
  `python3 -B catalog_build.py build --partial` builds without the sources whose input is missing
  and writes **only** `catalog.PARTIAL.jsonl.gz`, `catalog_stats.PARTIAL.json` and
  `card_links.PARTIAL.json`; the stats carry `PARTIAL_BUILD` (the missing inputs, the excluded
  sources, "NOT equivalent to catalog.jsonl.gz") and each excluded source shows state
  `EXCLUDED_MISSING_OR_MISMATCHING_INPUT`. The complete files are never touched by it.

The build is deterministic: sorted output, `mtime=0`, no dependence on hash randomisation
(verified by two builds with different `PYTHONHASHSEED`, byte-identical to the committed file).
Rebuilding from the complete cache was verified offline on 2026-10-28 and produced the same counts.
To remove: `git rm -r` this directory and `framework/scripts/compound_catalog.py` (plus its row in
the scripts README); nothing else imports them.

## Hook for the rest of the module

Generic, read-only, offline code lives in
[`framework/scripts/compound_catalog.py`](../../../../../framework/scripts/compound_catalog.py);
the data stays here. From `repurposing_join.py`, `repurposing_bridge.py` or a later coverage builder:

```python
import compound_catalog as cc                 # framework/scripts on sys.path
entries = cc.load()                           # catalog.jsonl.gz
cc.find(entries, name="amlexanox")            # also id=, target=, access=, status=
cc.for_card("B01_amlexanox")                  # linked entries + the matching rule, or UNMATCHED + reason
```
```bash
python3 framework/scripts/compound_catalog.py lookup --target PTGS1 --access OTC --limit 5
python3 framework/scripts/compound_catalog.py card B01_amlexanox
```

An empty result means "no entry matched in this catalogue", never "not a drug". The join and the
bridge do **not** call it yet; this is the hook, not an integration.

## Card link

`card_links.json` maps the identities in `cards/`, `cards_early/` and `join/cards.json`
(58 cards considered; **18 with at least one link, 40 unmatched**, each with its reason) by two
identifier rules. (1) A `CHEMBL` id found in the card text is accepted only if ChEMBL's own
`chembl_id_lookup` says it is a COMPOUND (the text also holds target and document ids that share
the prefix; `CHEMBL2534` is a target); it is a **mention**, not an identity declaration; an id
with no cached lookup stays `UNRESOLVED` and unused. (2) Ten curated declarations in
`card_identity_declarations.tsv`, each naming role (`identity` or `named_member`) and basis. Name
similarity is never used. Most unmatched cards are class-level or modality-level and have no
single compound by design.

## Supplements and access categories, IT5 P10 (2026-10-28)

**"Supplement" is a category of access, not an indication of efficacy or safety.** It records that a US
dietary-supplement label in DSLD names an ingredient whose name (or a name DSLD itself lists as a synonym of an
ingredient group) equals the catalogue entry's name. It does not say that the compound is available in Italy
or the EU, in what form, dose or quality, that it is appropriate for anyone, or that it does anything in a
WWOX-deficient system. A DSLD hit is a **product label listing an ingredient**, not the compound's
availability or safety.

What was added: 68 probe strings (51 of them new to the targeted set) for the compounds that came out of the research cycles and are in cards
(dichloroacetate and its spellings, thiamine and its salts, alpha-lipoic acid, pyruvate and its salts, beta-hydroxybutyrate
and its salts, carnitine forms, coenzyme Q10 forms, decanoic and neighbouring fatty acids, triheptanoin, phenylbutyrate,
UDCA/TUDCA, ethosuximide, vigabatrin, lithium forms, apinocaltamide, stiripentol, bumetanide, amlexanox, metformin,
valproic acid, riboflavin, biotin, cannabidiol, and the nonsense control), each re-queried with `--refresh` so the
record carries the new detail fields, plus 68 lookups in the DSLD **ingredient-group index** (`/v9/ingredient-groups`,
`method=factsheet`, which matches a term against group names and DSLD's own group synonyms). Results per string:
[`dsld_probe_results.tsv`](dsld_probe_results.tsv); the ambiguity notes are in
[`dsld_probe_annotations.tsv`](dsld_probe_annotations.tsv).

How the evidence is read (all of it `strength: name_only`):

* **Label probe.** First 50 results of a phrase search; `total_fulltext_hits` is a text match count (it counts labels that
  merely contain the words anywhere, so it overstates ingredient presence: "decanoic acid" 7 241 hits, 0 ingredient equal
  names). The ingredient counts are limited to the 50-label sample and are lower bounds, not product counts. Equal
  ingredient **name** and equal ingredient **group** are counted separately, and labels that contain the string only inside
  a longer name ("partial") are kept apart.
* **Ingredient group.** DSLD curates "ingredient groups" with an internal numeric id and a synonym list (the group "Alpha-Lipoic
  Acid" id 6878 lists thioctic acid, lipoic acid and many spelling variants). The id is DSLD's own name curation: it is **not** a chemical
  identifier (no UNII, no InChIKey, no CAS in the response), so a group match is a name match that carries an id and the entry
  stays `name_only`. Where several groups match, up to six ids are kept with `dsld_groups_total`.
* **Rule added to `build`.** An entry gets `supplement` if a label probe of its name (or a targeted synonym) found an equal
  ingredient, or if its name or one of its synonyms (normalised, at least four characters) equals a DSLD group name or
  group synonym that a lookup returned. Three-letter keys (ALA, DCA, PCP) are never matched: "ala" is also alanine. A no
  match is "no match in DSLD on 2026-10-28 under these query strings".

Measured effect on the catalogue (before the probes -> after): entries with the `supplement` category 126 -> 238; entries
with `unknown/unverified` 28 296 -> 28 234; label probes OK 1 005 -> 1 046; targeted probes 24 -> 75; ingredient-group
lookups 0 -> 107 (some of the first 39 were repeated). Not everything new is a card compound: lookups of "thiamine"
and "riboflavin" also returned the vitamin B family groups (and the pyridoxine lookup the B6 groups), which attached `supplement` to pyridoxine, cobalamin and
niacin entries by their own names; the count rise is coverage of the probed families, not a statement about the cards.

Per compound (card context in `closed_loop_it5_p9_20261029`): dichloroacetate, sodium dichloroacetate, dichloroacetic
acid and "DCA": 0 text hits and no group, still `experimental` or `unknown/unverified`. Thiamine, alpha-lipoic acid,
pyruvate, beta-hydroxybutyrate, carnitine, coenzyme Q10 and decanoic acid carry `supplement` by name with group ids;
decanoic acid only through DSLD's synonym (group "Capric Acid" 2486), not through a label ingredient name; triheptanoin
0 hits (prescription by NDC identifier, a separate category); phenylbutyrate, ursodeoxycholic acid, ethosuximide,
vigabatrin, apinocaltamide, stiripentol, bumetanide, amlexanox: 0 hits; tauroursodeoxycholic acid 46 labels (name only).

**Bulk-list note.** Re-labelling ten bulk-list names as targeted lowered `bulk_list_probed` from 981 to 971; the union did not change.

## European context probe, IT5 P10 (2026-10-28)

What was tried, in order. (1) Italian Ministry of Health, the register of notified supplements
("Registro nazionale degli integratori", `salute.gov.it`): the page URLs answered HTTP 200 with a 12.8 kB page
titled "Gcore" (an anti-bot challenge), not the register; it was not worked around. The open-data portal
`dati.salute.gov.it` answered 301/HTTP 000 for the root and served an application shell for `www.dati.salute.gov.it`; a search
of the EU Open Data Portal for Italian supplement registers returned no Ministry dataset. **Not usable: no download,
no API reached.** (2) The EU register of nutrition and health claims and (3) the EU Novel Food status catalogue: the
Commission pages are search applications without a download link, but the EU Open Data Portal lists both as datasets
(DG Health and Food Safety, last modified 2024-08-13) with documented download URLs on
`api.datalake.sante.service.ec.europa.eu`; both answered HTTP 200 without a key, a registration or a contact string
(Novel Food 6 570 records, 11.0 MB; health claims 3 342 records, 4.4 MB). Reuse terms: the Commission legal notice
(`commission.europa.eu/legal-notice_en`, read 2026-10-28) says content owned by the EU is licensed under CC BY 4.0 under the
Commission Decision of 12 December 2011, "unless otherwise indicated"; the dataset records carry no licence field of their own, so
CC BY 4.0 is the Commission legal-notice default for EU-owned content "on this website" AND, per the independent verification, the licence that the data.europa.eu catalogue records declare on both distributions (CC_BY_4_0); the downloaded records themselves carry no licence field, and whether that licence covers every record (the health-claims file has a proprietary_data field) was not checked, so it is **not a statement about each record**; attribution is given here. `eu_context_probe.py`
downloads both files (gitignored `cache/eu/`) and writes name-match counts to `eu_context_probe.tsv` (whole-word
normalised match; EU level, not Italian national). Examples: coenzyme Q10 8 health-claim entries, all "Non-authorised"; alpha-lipoic
acid 9, all "Non-authorised"; carnitine 17, all "Non-authorised"; thiamine 7 "Authorised" (nutrient-function claims); tauroursodeoxycholic acid and
cannabidiol and benfotiamine each 1 Novel Food catalogue entry with status "Novel food"; "pyruvate" matches only creatine pyruvate (a different substance); dichloroacetate,
triheptanoin, phenylbutyrate, lithium: 0 in both. A claim status is a statement about wording of a health claim, not
about the substance; a Novel Food catalogue status is a non-binding orientation (the catalogue says so). Neither says anything about a WWOX use.

Independent verification (2026-10-29, `locator_audits/2026-10-29_it5_p4_independent_verification.md`): 485 of 485 merged pairs agree with an independent InChIKey comparison and no false merge was found; two `rejected_conflict` pairs (LX2931, GNE-7883) are tautomer depictions of the same molecule rather than structural conflicts, and two `unresolved` pairs are recoverable by InChIKey (5-hydroxymethyl-2-furfural, whose GtoPdb id is mis-cased, and PBF-509, whose GtoPdb id is not a compound record but whose structure equals CHEMBL3694769). These are recorded as known low-severity limits; the recoverable ones are not merged by the rule today.

Independent verification of the supplement and EU probes (2026-10-29, `locator_audits/2026-10-29_it5_p10_independent_verification.md`): the DSLD and EU counts reproduce (DCA 0 hits and 0 groups; ALA, pyruvate, beta-hydroxybutyrate, carnitine, coenzyme Q10, lithium and tauroursodeoxycholic acid groups as listed; EU recounts exact). Limits recorded: (1) the thiamine "6 groups" is a display cap (`[:6]`) in the builder: live DSLD has 12 groups with thiamine in a name or synonym and the catalogue stores `dsld_groups_total` = 13; (2) sample-based per-label counts (the first 50 labels) are unstable between runs; (3) some additions match a salt to an element group through DSLD synonyms (for example a disodium phosphate to the group "Sodium"): weak, name-only evidence; (4) the +112 entries with the `supplement` category touch no compound linked from a card (the two card-linked supplement compounds, cannabidiol and lithium, were already among the 126), so the increase is catalogue-wide name-only coverage plus new probe results for the nine compounds handed over by the P9 cycle, not a change in what the cards say.
