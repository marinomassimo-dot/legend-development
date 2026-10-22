# WWOX rows inside the supplements of genotype-stratified treatment-response cohorts - group R4c

> **Actor** `scientist-d` - **Task** `REPURP-10H-WWOXROWS-D-20261022` - 2026-10-22. Non-canonical research record. It touches none of the four scientific current files, `disease_model.md`, `drug_repurposing/` or `repurposing_bridge.py`. It extends [`repurposing_10h_scientist-d_20261022b.md`](repurposing_10h_scientist-d_20261022b.md) (the Table S7 finding) and **corrects one reading in it** (section 4).
>
> **NOT WWOX EVIDENCE, at class level, for every paper below as a paper.** The WWOX rows themselves are WWOX-DIRECT but class level and anonymous; nothing that could identify a patient is reproduced (no ages, no sites, no variant paired with a parent). Treatments appear only as the exposure a published registry recorded, never as guidance: no dose, no administration recommendation, no paediatric suitability presumed. Nothing here is medical advice; it supports discussion with a treating clinical team and never substitutes for one.
>
> **This is a SEARCH, not a set of readings.** What was done to each paper: its supplement was retrieved from the open Europe PMC `supplementaryFiles` route, searched by `framework/scripts/supplement_symbol_search.py` for the aliases listed in section 1, and, where a hit or a table structure mattered, the hit's table and the main-text passage that defines it were read. No paper was read to completion, so **no manifest and no new receipt is claimed** (declared as a default taken, section 8). The one paper already receipted (R4b) keeps its staged receipt.

## 1. What was searched, and how

- **Tool.** `supplement_symbol_search.py` (scientist-b): whole-token, case-insensitive; opens `.xlsx`, `.docx`, `.csv/.tsv/.txt`; **cannot see PDFs, images or tables-as-pictures**. PDF supplements were converted with `pdftotext -layout` first; the converted text is what was searched. The tool walks `files/supplement/` only, so a scratch workspace with symlinks to the 24 searched files was built (their SHA-256 digests, in full, are in [`repurposing_10h_scientist-d_20261022c_searchlog.json`](repurposing_10h_scientist-d_20261022c_searchlog.json)). The `xlsx` files were also checked outside the tool for inline-string cells (none) so the tool's `<v>`-only cell parser missed nothing.
- **Aliases tried.** Gene symbol `WWOX`; aliases `FRA16D`, `WOX1`, `SDR41C1`; HGNC id `HGNC:12799`; Ensembl id `ENSG00000186153`; OMIM `605131`; full name fragment `WW domain` / `WW-domain`; syndrome labels `WOREE`, `SCAR12`, `DEE28`, `EIEE28`; older aliases `HHCMA56`, `D16S432E`; cytogenetic bands `16q23`, `16q23.1`, `16q23.2`, `16q23.3`; transcript accessions `NM_016373`, `NM_130791`, `NM_001291997`, `NG_011976`.
- **Not tried.** Variant notation (any `c.` / `p.` string - a row that gives a variant and no symbol would not be found); the alias `FOR` (it collides with the English word and was dropped after it produced false hits); the symbol written in a figure, image or scanned table; patients described only as "recessive epilepsy" with the gene omitted; any language other than English.
- **Disk sweep.** The same aliases over the whole existing `files/supplement/` tree returned only the mouse, Drosophila, GWAS, expression-sheet and slide hits that tree was built for; none is a patient treatment row.
- **Candidate selection.** Europe PMC and PubMed queries on developmental and epileptic encephalopathy, genetic epilepsy, infantile spasms, cannabidiol, fenfluramine, ketogenic diet, perampanel, cenobamate, ACTH/steroid and vigabatrin cohorts, restricted to open access with supplementary files. Dedup: `registry_records.py get --pmid` and `fulltext_receipts.py status --pmid` before use (results in the table). An empty registry result is a statement about that query only.

## 2. The twelve counted papers

"Gene col" = the column or row-header that carries the gene; "Tx" = treatment; "Resp" = response. Every "no" below means **no WWOX row in the files named**, nothing wider.

| # | PMID (DOI) | Treatment / design | Supplement on disk (shared `files/`) | Gene col | Resp col | WWOX in supplement | WWOX elsewhere in the paper |
|---|---|---|---|---|---|---|---|
| 1 | 42334048 (10.1002/epi.70342) | fenfluramine, 166 patients, 18 hospitals, retrospective | `files/supplement/PMID42334048/` docx (S1-S8) + text rendering | S7 column headers (gene) | S7 rows: seizure freedom, responder (>=50%), worsening, adverse events | **YES, 1 column, Table S7** | Table 1 footnote lists the gene once |
| 2 | 40126049 (10.1111/epi.18378) | cannabidiol, 266 monogenic, 27 centres | `files/fulltext/PMID40126049_CerulliIrelli2025_supplement/` Appendix S1 pdf (+ text) | none: S1/S2 are missing-data and adjusted-mean tables | - | no | **YES, main-text Table 2 row, 3 patients** (PAPER 189) |
| 3 | 37583270 (10.1002/epi4.12811) | infantile spasms, genetic, 124 children, India | `files/fulltext/PMID37583270_wwoxrows_supplement/x/` docx = two supplementary figures | none | - | no (figures-only supplement) | **YES, main-text Table 1, 4 children** (PAPER 143) |
| 4 | 42394473 (10.1002/epd2.70277) | exome yield, Turkish centre | `files/fulltext/PMID42394473_Karaer2026_supplement/` docx = a self-test quiz, no data | none | none | no | YES, main-text variant table, 2 patients, **genotype only** (PAPER 205) |
| 5 | 42798297 (10.1111/ene.70760) | cannabidiol in adults with LGS | `PMID42798297_wwoxrows_supplement/x/` docx: S1 reasons for stopping by patient number; S2 confirmed genetic diagnoses by gene with n | S2 "Gene/Chromosomal abnormality" | none per gene | no | no |
| 6 | 38678505 (10.1007/s40120-024-00618-5) | perampanel, aetiology subgroups | `PMID38678505_wwoxrows_supplement/x/` pdf (text rendering searched) | none (aetiology categories only) | - | no | no |
| 7 | 42397117 (10.1002/epi4.70301) | cenobamate, paediatric, European | `PMID42397117_wwoxrows_supplement/x/` three **TIFF** files = Kaplan-Meier retention figures | none (etiology categories only) | - | **not searchable**: images; legends read in main text; no gene table is described | no |
| 8 | 42449462 (10.1186/s42466-026-00513-4) | ACTH, infantile spasms, responder vs non-responder | docx Table 1S baseline by responder | "Genetic finding" normal / abnormal / unknown only | responder status | no (no gene column exists) | no |
| 9 | 41713210 (10.3345/cep.2025.02089) | vigabatrin / hormonal therapy, infantile spasms, Korea | four pdf tables (text rendering searched) | S1 lists genetic and chromosomal aetiologies | S2-S4 outcomes by etiology group, not by gene | **band-level hit only**: S1 chromosomal list names a `16q23 microdeletion` (1 child); see section 5 | no |
| 10 | 42828465 (10.1002/epi4.70357) | **no treatment**; genotype table of 80 children, Hamburg | `PMID42828465_wwoxrows_supplement/x/` xlsx S1 (all patients) + S2 (GO terms) | S1 "Gene symbol" | **none** | **YES, 1 row, Suppl Tab1** | **no** (main text never names the gene) |
| 11 | 42528014 (10.1002/cns.71061) | 50 chromatin-remodeller cases, genotype/phenotype | xlsx Table S1 | "Gene" | none | no | no |
| 12 | 36734057 (10.1111/epi.17530) | perampanel in rare genetic epilepsies, 137 patients, 79 aetiologies - the best-fitting cohort | **PARKED** (section 6) | - | - | not searched | not read |

Searched but **not counted** among the twelve (genotype-only supplements downloaded before the set was fixed; no reading, no response column): 42220229 (monogenic epilepsies, four docx), 38279250 (genetic and DEE early-onset cohort, xlsx), 42541364 (adult DEE cohort; panel gene lists), 35330882 (infantile spasms aetiology, docx gene-variant list), 41137852 (absence-seizure genetic cohort, docx figures). The only symbol hit among them: 42541364 lists the gene as a member of its sequencing panel (a list of genes tested, **not a patient row**).

## 3. WWOX-row inventory (the product)

"Meaning" is what the row can carry; **"cannot mean"** is what it cannot. All rows are n = small, uncontrolled, anonymous.

| Row | Where | Treatment recorded | n | Response entry | Where the gene appears | What it can mean | What it cannot mean | Registry status |
|---|---|---|---|---|---|---|---|---|
| A | 42334048, **supplement S7**, third column of a three-gene block | fenfluramine (add-on, retrospective registry) | 1 | seizure freedom 0, responder 0, worsening 0, adverse events 0 at 3, 6, 12 months, discontinuation 0 | main text Table 1 footnote (gene only) | one WWOX-direct patient exposed to the drug and retained with no adverse event recorded | efficacy or non-efficacy; "non-responder" **and** "not evaluable" are both **undetermined** (section 4) | new (R4b) |
| B | 40126049, **main-text Table 2** (not a supplement) | cannabidiol | 3 | mean seizure reduction 41.7 (SD 38.2); 2/3 reached the 50% band; 2/3 improved on the global impression | main text | three WWOX-direct patients with a quantified, heterogeneous response in a 266-patient registry | a response rate: the paper itself prints percentages only for groups of more than five | PAPER 189 |
| C | 37583270, **main-text Table 1** | spasm treatments (per patient) | 4 | per the registry record (not re-read here): spasm control at 6-12 months in three; not a drug-specific comparison | main text | the repository's own largest WWOX spasm series (PAPER 143); re-tabulated, not re-observed, in PAPER 190 | independent of A, B (unknown); a drug effect | PAPER 143 / 190 |
| D | 42394473, main text | none recorded | 2 | none | main text | genotype-only WWOX patients | any treatment inference | PAPER 205 |
| E | 42828465, **supplement S1** | none recorded | 1 | none | **supplement only** | one more WWOX-direct genotype row that no index of the paper's text would find | any treatment inference; independence from C or D (unknown) | **new** (not in the registry) |
| - | 42541364, supplement panel list | - | 0 patients | - | gene list | the gene is on that panel | a patient | not a row |
| - | 41713210, supplement S1 | vigabatrin/hormonal context | 1 child with a band-level deletion | none per gene | **cytogenetic band only** | nothing about WWOX: a 16q23 band deletion may or may not include the gene | a WWOX row; **excluded from the count** | not a row |

**Counts, recomputed from the printed tables.** Rows with an entry in a treatment-response structure: A (1) + B (3) + C (4) = **8 WWOX-direct patient-rows on a treatment**. Genotype-only WWOX rows: D (2) + E (1) = 3. Rows found *in a supplement* by this search: A and E = **2 rows, 1 with a treatment context**. Of the 12 papers searched, 2 hold a WWOX symbol in a supplement table; 10 do not (band-level hit, panel list and images excluded as stated).

## 4. The Table S7 column: what the all-zero entries mean

**Verdict: UNDETERMINED between two readings; the earlier R4b wording ("not a responder") was a reading and is withdrawn.** Evidence, in the paper's own words:

- The table: "Supplementary Table S7. Responder (≥50% reduction in seizure frequency) and adverse event rates according to genetic etiology in other DEEs at 12 months"; the block's headers read "SCN1B (n=1) | SCN8A(n=1) | WWOX(n=1)" (read from the docx table cell by cell, not from a text flattening) and the rows "Seizure freedom | 1 (100) | 0 (0) | 0 (0)", "Responder rate (≥50%) | 1 (100) | 0 (0) | 0 (0)", "Worsening | 0 (0) | 0 (0) | 0 (0)".
- The denominator is the **whole group**: main Table 3 prints "All ages, n / N (%) 48/83 (57.8) 32/42 (76.2) 21/40 (52.5) 101/165 (61.2)" - the other-DEE denominator is 40, the group's size - and Table S6 prints "Responder rate (≥50%) | 7 (43.8) | 3 (37.5) | 4 (57.1) | 0 (0) | 1 (100) | 6 (85.7)", whose responders sum to 21. So in S6 (whose six columns sum to the full 40) nobody in the group was removed as non-evaluable, and S7's 24 patients (19 by gene plus 5 with chromosomal findings, counted from its headers) match S6's genetic, genetic-and-structural and genetic-and-metabolic columns (16 + 7 + 1 = 24), which is consistent with the same rule; a patient without a 12-month datum, if present, would sit in the denominator as a zero. That is the only evidence in the paper bearing on the question and it points **away from "excluded as not evaluable"**.
- But the same paper shows missing data exist: Table S4 is headed "LGS / (n=78) | DS / (n=40) | Other DEEs / (n=38) | All DEEs / (n=156)", i.e. two other-DEE patients are absent from the seizure-severity table, and the Limitations say outcomes "were derived from routine clinical records and caregiver reports, which may be affected by recall bias, documentation variability between centers, and missing information". No sentence states how an absent 12-month datum is scored in the responder and worsening cells.
- Two readings therefore survive: (i) the patient had a recorded 12-month course with a reduction below 50% and no worsening; (ii) the cells are zero because no datum was available and absence was scored as zero. Reading (i) cannot be told from (ii) in the supplement. **Not resolved; a request to the corresponding author is the only route, and none is made here.** Whichever holds, n = 1 supports no statement about the drug in this genotype.
- The R4b note is corrected in place (two phrases) and its owed blind audit now reads: the S7 WWOX column is "undetermined", not "not a responder".

## 5. Overlap and the counting-once rule

- **Documented duplication.** PAPER 190 re-tabulates the four children of C in a review; the review adds no patient. A row in a review is not an observation.
- **Same drug-class, different drug, same child possible.** A (Spanish fenfluramine registry) and B (a 27-centre cannabidiol registry) both draw on Spanish epilepsy centres, and authors of one appear in the other. A single child could carry both an A row and one of the three B rows. The papers do not say and the rows are anonymous: **independence of A from B is UNDETERMINED.** Treated as possibly overlapping, the independent count of treatment-response patients is **between 7 and 8**, not 8 stated as fact.
- **C against A, B, D, E.** Different countries and enrolment windows; no shared centre is named; independence is *not shown* but also not contradicted. D (a single Turkish centre) and E (a single German centre) are genotype-only and add to no response count.
- **The repository's own WWOX case series** (the WOREE series behind CLAIM 042: a five-patient series with a ketogenic-diet entry) was not re-opened here; its patients are previously published individuals and **any of A-E could coincide with one of them** (the papers are anonymous and the series carries no identifier that could be matched). They are not added to the count, and none of A-E may be cited as confirming or contradicting that series.
- **Count rule applied.** Distinct WWOX-direct treatment-response patients: **at most 8, possibly 7**; distinct reports contributing: **3 (A, B, C)**. No rate, no pooling.

## 6. Parked, with the cascade run

- **36734057** (perampanel, 79 aetiologies): no PMC copy and Europe PMC flags no supplement; Unpaywall lists the publisher's PDF as the open location; the publisher page, direct PDF and the supplement endpoint all returned a bot challenge (HTTP 403) for an ordinary client, as did the DOI resolver. **Not bypassed.** Parked for a manual download by the operator or a session with a browser route. Until then nothing is known of its supplement.
- **42397117**: supplements are TIFF figures; no OCR tool on this host and the legends describe retention curves, not a gene table. Recorded as "not searchable (images)", not as a negative.
- **Images inside other supplements** (figure files that accompany several zips) were not read.

## 7. Safeguards, applied

1. Each WWOX patient counted once - section 5.
2. A zero is "no WWOX row in the files searched": the files are listed by digest in the search log; a zero in 10 of 12 papers says nothing about their main text (rows B, C, D live there), nothing about unsearched files, and nothing about the literature.
3. No inference of efficacy or non-efficacy from n = 1; no pooling; B's fractions are the paper's own and are not a rate.
4. Search aliases and the not-tried list: section 1.
5. Unopenable supplements parked, never bypassed: section 6.

## 8. Defaults taken, stops, and what is owed

- **DEFAULTS_TAKEN.** (a) Set counted as twelve with five incidental genotype-only extras reported but not counted (the tool run was cheap and the files were already downloaded). (b) No manifest and no receipt for search-only papers; a receipt would claim a reading that was not done. (c) Candidate selection from Europe PMC/PubMed queries rather than the repository's DEE-cohort notes alone. (d) The R4b wording corrected in place rather than left to the audit.
- **STOP_LOG.** None.
- **OWED.** A blind audit by another actor of: the S7 column assignment (docx cell order against the printed header), the S6 sum to 21, and the reading in section 4. Nothing in this note is audited. The 36734057 supplement and the 42397117 images remain unsearched.
- **A practical finding for the harness.** `supplement_symbol_search.py` walks one directory and cannot see PDFs; the working pattern here (symlink workspace, `pdftotext` first, `.docx` table cells read by row for column alignment) found both supplement-only rows. A flattened text rendering of a docx table puts a header in a different order from its cells; the column mapping had to be checked from the cells.
