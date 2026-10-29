# Independent leak scan of the shareable package (P13), 2026-10-29

Producer: scientist-a (audit-shareable and the package). Verifier: independent subagent with its own forbidden-value set built from the full catalogue; the producer checker was read last. Verdict: no third-party identifier leak and no embedded class-B or class-C table; counts reproduce; three findings that the checker passes by design (class-B/C-only compound-target pairs in visible lead prose and card text; status classes in pair objects; names that entered only through catalogue rows) sent back for repair together with the closing of the checker blind spots.

# P13 independent verification (scientist-d) - shareable view

Scope: `view/index_shareable.html` (byte-identical to `view/shareable_package/index.html`, cmp verified) and `view/shareable_package/`. Own scripts and scratch are in `<scratchpad>`. The producer's checker was read only at the end. I did not render the page in Chromium: the one attempt used `--no-sandbox`, the auto-mode classifier refused it, and I did not retry.

## Verdict
No third-party identifier leak and no embedded class-B/C table. Three findings that the producer's counts and checker do not reflect:

- **F1 (medium).** Visible prose names compound-target pairs asserted only by class-B/C sources, with the source named.
- **F2 (low-medium).** The "0 rows with per-row status" claim holds for `rows[].st/mod` only. A status class is still embedded for 549 rows through the pair objects.
- **F3 (low).** Six compound names, and 16 names in all, enter the repository's own text only through class-B/C rows. They appear in card and lead prose.

## Method
- I built the forbidden set from `catalog/catalog.jsonl.gz` with `gzip`: 44,211 records and 134,958 distinct names or synonyms, each with its claim sources and origin.
- Identifier sets: DrugBank 13,001, ChEBI 13,263, UNII 15,002, InChIKey 15,242, skeleton key 14,813, ATC 4,579.
- (record, gene) pairs: 86,936, each with its claim sources.
- Mechanism and target wording: 1,977 ChEMBL `mechanism_of_action` strings, 1,410 `target_name`, 1,785 GtoPdb target names.
- Surfaces scanned:
  - every JSON string and key of the data object, parsed;
  - visible text, tags and attributes, and script literals (the exported-card builder and the standalone-download template are in the script, built from the same data object);
  - the raw JSON text;
  - the other package files.

## Scans and hits

| Scan | Result |
|---|---|
| DrugBank, ChEBI, UNII, InChIKey, ATC (set lookup plus regex over the whole file) | 0 hits |
| E-mail-like string, `/home/`, `/tmp/`, `scratchpad`, worktree, `.claude`, session UUID, `file://`, `javascript:`, `fetch`/`XMLHttpRequest` | 0 hits. The word "session" occurs 6 times, only as "session clock" in search-log text. |
| NCT ids | 0 (matches the NOTICE census) |
| Name scan, 1-6 word n-grams against the 134,958 names | 144 hits, classified below |
| ChEMBL and GtoPdb target wording (full-string match) | Longest 4 words ("Histone deacetylase 6 inhibitor", "Voltage-gated T-type calcium channel"). The 5-word quote in card H01 ("...channel blocker") is the card's own quotation. Nothing is over 8 words. |
| Pair scan: compound name and gene symbol in the same string, pair asserted only by non-A sources | 75 (name, gene, record) combinations, see F1 |
| Hrefs | 66 in-page anchors and 6 public hosts (civicdb.org, docm.info, open.fda.gov, genenames.org, nlm.nih.gov, ebi.ac.uk). The 2 empty-attribute matches are JS string templates (`cardLinks`, `ext`), not links. No repository-relative href. |
| Provenance by 8-word shingle (see Task 4) | Longest unquoted run 11 words |
| Mutation test | Both injected items caught (see Task 6) |

### Name hits (144 distinct)
- **(c) Short generic or common-word hits: about 70.** Examples: null, same, paper, search, legend, oxygen, calcium, glucose, glutamate, GABA, NMDA, hydrogen, citrate, lactate, antioxidant, anticonvulsant, "proteasome inhibitor", "calcium channel blocker", "antisense oligonucleotide". Some have only NCI or TTD claim rows, but they are class names or generic terms. Not violations.
- **(b) Card compounds also attested by cited literature in our own text: about 56.**
  - 73 of the 89 non-generic names whose claim sources include no class-A source occur in the local full-text corpus (954 files, 13.0M words), e.g. ethosuximide, vigabatrin, memantine, perampanel, bumetanide, stiripentol, cannabidiol, amlexanox, dichloroacetate.
  - Pairs scanned in `cur` (card text) are literature statements, e.g. memantine-GRIN2A, butyrate-HDAC6. I classify these as benign.
- **(a) Violations or borderline: the 16 names that occur in no local full text.** Their only provenance in the repository is catalogue rows.
  - In `leads` (visible static HTML): hesperadin, ziprasidone, quetiapine (and "quetiapine fumarate"), "haloperidol decanoate", flufenamic acid, regadenoson.
  - In card text (`cur`): AZD7545, VER-246608, AZD3965, TTA-A2, devimistat, suvecaltamide.
  - Card-compound synonyms or code names: apinocaltamide, ACT-709478, NBI-827104, ELX-02.
  - The last group is excluded from F3 because the card compounds are named in our own text. Names alone are facts and are weak evidence of a licence breach. The stronger issue is F1.

## F1 (medium): class-B/C compound-target pairs in prose

The `leads` section (LD-001 to LD-006) is pre-rendered into the visible HTML (hesperadin at byte 135847, carbenoxolone at 137933). It states pairs that exist only as GtoPdb, PharmGKB or DTC claim rows. The catalogue source sets below come from my own lookup.

| Lead | Statement on the page | Catalogue source (own lookup) |
|---|---|---|
| LD-002 | glycine and aspartic acid are agonists of GRIN1, GRIN2A, GRIN2B ("GtoPdb rows") | GuideToPharmacology only (glycine-GRIN2A also TTD) |
| LD-003 | adenosine and regadenoson flagged "opposed" through ABAT via a "Guide-to-Pharmacology ligand row 'ABAT agonist'" | GtoPdb (class B) |
| LD-004 | hesperadin-EIF2AK4 "claim source DTC, 'inhibitor'", "81 target rows in the record"; five antipsychotics-EIF2AK4 "PharmGKB, interaction type unknown" | DTC (class C); PharmGKB (class B) |
| LD-005 | carbenoxolone and flufenamic acid carry "Guide-to-Pharmacology 'inhibitor' rows on PANX2 and PANX3" | GuideToPharmacology only |

Card prose adds ChEMBL curated-mechanism statements about card compounds:
- sodium dichloroacetate "ChEMBL mechanism rows INHIBITOR at PDK1 to PDK4" (I01);
- vigabatrin "ChEMBL curated mechanism INHIBITOR" (H02);
- E03 assertion DR-E03-002 "PDK2 inhibition by AZD7545 or VER-246608" (GtoPdb-only pairs, scope EXTERNAL_DATABASE_RECORD);
- "DGIdb gives [devimistat] no action type on PDK2-4".

These are the producer's own paraphrases with a source named, and they are short. They still name the compound, gene, action and database, which is the information the class-B/C rule says to withhold (identifier and counts only). Whether paraphrase counts as embedding is a legal reading I cannot settle. The mismatch with the stated policy is clear. Remedy: describe the lead outcome without naming pair, action and source, or move it into `class_b/`.

## F2 (low-medium): per-row status class is not absent

The producer states 0 rows with per-row status or modality. I confirm `rows[].st` and `rows[].mod` are empty for all 1,463 rows. But `pairs[].p.cr.pha[1]` (in 697 of the 1,664 pairs) lists a status class for the row the pair points to (`r`). The values are approved_any_source, clinical_candidate, phase_unknown and others. Joining on `r` gives 549 distinct rows with a status class, 14 of them among the 37 named rows.

I traced the source of the status class for those rows in the catalogue:
- 444 rows have status records from DGIdb only (the DGIdb "approved" flag, mixed provenance);
- about 56 have ChEMBL only;
- the rest mix ChEMBL, openFDA and MATRIX.

The catalogue README states that `status_class` derives from "ChEMBL max_phase 4, DGIdb approved TRUE or MIXED, MATRIX APPROVED...". The producer's own path rules call st/mod "derive from ChEMBL/MATRIX/DGIdb statements: not embedded", so this is a bypass of the stated rule. I did not check whether a status bucket is itself copyrightable or share-alike content; it is a coarse derived tag.

## Task 2: counts per provenance class (embedded JSON)

| Item | Producer | Mine |
|---|---|---|
| Rows | 1,463 | 1,463 (1,426 with `w`, 37 without) |
| Rows carrying a compound name | 37 | 37 |
| Named-row source | card names | all 37 are card identity or attachment names |
| Rows with `st` or `mod` | 0 | 0 |
| Rows with access category | 11 | 11 (6 prescription, 3 unknown/unverified, 2 prescription + unknown) |
| Withheld rows | identifier + counts | only keys acc, cards, dup, id, kind, mod, name (an opaque id), rec, st, tr, w; all empty or numeric |
| Pairs with a target list | 12 of 1,664 | 12 (MTOR x8, JAK2 x4) |
| Target symbols listed | 12 | 12 |
| Class-A backing for those 12 | n/a | I re-derived each from the catalogue: every (record, gene) has a CIViC claim row (3 also DoCM). The listed tags (`DGIdb:CIViC`, `DGIdb:DoCM`) are correct. |
| Pairs with `l1[6]` (pathway members) | n/a | 7 more pairs list MYC or CTNNB1 as need pathway members, with CIViC tag and count 0. These are own need genes. |
| Card actions listed | 0 | 0 (full version: 29) |
| Excluded rows with compound name and gene | 0 | 0 (the 3 entries are opaque DGIDB ids with empty gene lists; full version names Osu-03012, Celecoxib, "Null" with 27 HGNC ids) |
| Identifier census | CAT 1445, CHEMBL 253, DOI 5, HGNC 6, NCT 0, PMID 12 | same (CAT 1,445, CHEMBL 253, DOI 5, HGNC 6, NCT 0; PMID 12 distinct) |
| Rows with a name in the full version | 1,451 | I could not reproduce this. By my method all 1,463 rows have a name. The 12-row difference is unexplained. |
| Third-party id values in catalogue | DrugBank 13,539, ATC 4,875 | DrugBank 13,001 and ATC 4,579 distinct. The producer probably counts occurrences. Not material. |

## Task 3: ChEMBL class-B file
- `class_b/chembl_cc-by-sa-3.0/` has 12 records, matching the cards' ChEMBL ids (CHEMBL1096, 1201333, 146927, 1746, 190461, 1983350, 256997, 306823, 413, 4217292, 696, 89598).
- `LICENSE_CC-BY-SA-3.0.txt` is the CC BY-SA 3.0 Unported legal code, byte-identical to `LICENSES/CC-BY-SA-3.0.txt`.
- `CREDIT.txt` reads "ChEMBL data is from https://www.ebi.ac.uk/chembl/ - the version of ChEMBL is ChEMBL_37 2026-05-01", plus licensor, title, licence URL and a clause 4(c) reference.
- An adaptation notice states: selection of 12 records and listed fields, re-serialised as JSON Lines, no value altered, distributed under the same licence.
- A scope paragraph limits the licence to the file and to adaptations of it, and says `index.html` carries only ChEMBL identifiers.
- Each record carries `chembl_release` "ChEMBL_37 2026-05-01" and the licence name.
- I compared each record with the catalogue: pref_name, max_phase and mechanism rows match (0 differences).
- The legal code includes the Adaptation share-alike clause. The share-alike structure is consistent as shipped.
- The page embeds no ChEMBL mechanism string over 4 words, as in the scan table. The card prose paraphrases ChEMBL statements as in F1; these are not copies of the wording.

## Task 4: provenance of the cards' own text
- 15 random card paragraphs (seed 13, at least 25 words) against 961 extracted local files (pdf via pdftotext, xml/html stripped, txt) and the fetched vigabatrin label (set id 082d818a..., 25,641 words): longest shared run 0 words in all 15.
- Control: shingling all 579 paragraphs of at least 25 words found these runs.
  - 28 words: bibliographic titles in `pmids[].title`, which are facts.
  - 22 words: the marked, attributed p53 quotation in B01.
  - 11 words: D01 identity "a multi kinase inhibitor a51 established to suppress wnt and myc" (matches the producer's record).
  - 10 words: H02 `pharm`, from the vigabatrin label ("no dose or exposure known to be free of risk and vision assessment recommended at baseline...").
  - 8 words each: E02 note and F01 note.
- No unquoted run is over 11 words. This agrees with `TEXT_PROVENANCE.json` (17 unquoted runs within limit, 3 short marked, 1 attributed).
- The corpus has 189 PDFs, 163 txt and 556 xml. Image-only PDFs, docx, xlsx and similar were not read, and I did not fetch other labels.

## Task 5: links
- Anchors and public hosts only. No e-mail-like string, no local path, no session id.
- Repository-relative paths do appear as visible text, not as links:
  - `framework/scripts/repurposing_coverage.py` and `repurposing_view.py` (regeneration line, twice);
  - `catalog/README.md`;
  - `.tsv` and `.py` names (`assertion_pertinence.tsv`, `repurposing_join.py handoff`);
  - lead fields "Card `cards/H01_apinocaltamide_ttype.packet.json`" and "Record `closed_loop_it3_20261028/README.md#case-a`" (6 leads, visible as code);
  - `class_b/chembl_cc-by-sa-3.0/chembl_cc-by-sa-3.0.jsonl` (package-relative, fine).
- They dangle in a shared package (informational).

## Task 6: mutation
- Temp copy: injected SOTULETINIB (a record whose only claim source is JAX-CKB; the name also appears under GtoPdb) with TP53 as visible text, as a data-object field and as a script literal.
  - The name scan reports it as NEW hit (sotuletinib, sources GuideToPharmacology + JAX-CKB), in the data field and in the html.
  - The pair scan reports `sotuletinib TP53 ['JAX-CKB']` (78 combinations versus 75 in the real page).
- Identifier mutation: injected one real DrugBank id, ChEBI id, UNII and InChIKey (DB00007, 135627, 0022LFJ74Y, AADCDMQTJNYOSS-LBPRGKRZSA-N). The scan reports all four (`ID:drugbank`, `ID:chebi`, `ID:unii`, `ID:inchikey`).
- Not mutated: a status class in a pair, and a pair-list injection into `pairs[].l1`.

## Task 7: producer's NOTICE.md and COMPARISON.md versus my counts
- COMPARISON.md rows (37 / 0 / 11 / 12 / 12 / 0 / 0) all reproduce (Task 2), apart from the "per-row status" nuance in F2 and the unexplained 1,451.
- Per-source "In this page" counts: CIViC 19, DoCM 3, all other sources 0. I reproduce CIViC 12 + 7 pathway pairs = 19 and DoCM 3. Class-B/C sources are indeed absent from the structured data.
- NOTICE says "no abstract and no passage of an article embedded" with a few marked short quotations. Supported by my shingle scan (longest unquoted 11 words).
- NOTICE lists generic short labels ("80s ribosome modulator", "gaba a receptor", "pyruvate dehydrogenase kinase", "reactive oxygen species", "voltage gated t type calcium channel"). My full-string scan agrees (max 4-5 words).
- NOTICE and the leads wording about GtoPdb, PharmGKB and DTC rows are in tension (F1).

### Producer's checker (`framework/scripts/repurposing_shareable_audit.py`, read last)
What it checks that I did not:
- a provenance rule for every path in the data object, so an unclassified field fails;
- per-pair target lists re-derived from the catalogue claim sources, and unclassified claim sources;
- a bibliographic-title cache;
- dynamic surfaces (rendered DOM, each card's export view and standalone download, PDF text) when Chromium is available;
- ChEMBL wording, co-attested and over 8 words;
- footer embedded-source labels;
- text-overlap with a 25-word limit.

What I checked that it does not:
- (record, gene) pair co-occurrence in prose. Its `.leads[]` and `.cur.cands[]` paths are class OWN, and co-attested names are counted but never fail. So F1 passes by design.
- the `.pairs[].p.` subtree is class OWN, so `cr.pha` status classes (F2) are never examined. The tool even documents "st/mod ... not embedded" for rows only.
- whether a name exists in any local cited full text (my test for F3);
- numbers that must agree in both directions (my independent counts above).

It also exempts `.tech.` and `.access.` names. Neither of us rendered the page in my pass (producer's `--dynamic` path not run by me).

## Remaining uncertainty
- Whether prose paraphrase of a class-B/C database fact (F1, F3) breaches share-alike or non-commercial terms is a legal reading I cannot make. My finding is a mismatch with the stated policy and with the checker's claim.
- The "in corpus" test (F3) depends on the local corpus. A name absent from it may still be in a cited article the cards read.
- The rendered page, the export view and the standalone download were analysed from the script and the data object, not from a rendered DOM.
- A status class derived from DGIdb "approved" (F2) may be considered a non-copyrightable fact. I report it because it contradicts the stated "no per-row status".
- The 1,451 versus 1,463 count in the full version is unexplained.
