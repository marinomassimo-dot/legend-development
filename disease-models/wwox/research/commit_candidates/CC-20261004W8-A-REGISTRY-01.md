# COMMIT CANDIDATE — CC-20261004W8-A-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 8 2026-10-04, branch `task/sci-A-20261004w8`.
**context_policy:** `SOURCE_FIRST` — each first pass was written before any registry record about the paper was opened (`research/intake_wave_20261004w8_A.md`).
**Not medical advice.** Class-level records only.

## Target
- `paper_registry_current.md`: **create** `PAPER 207`–`PAPER 212`; **promote** `CORPUS-STUB-101` (PMID 41254692) to `PAPER 212`.
- `literature_tracking_log_current.md`: **create** `LIT-0500`–`LIT-0505`.

## Registry landing per PMID (correction 8)
| PMID | PAPER | LIT | needs creation? | receipt (prepared, not appended) |
|---|---|---|---|---|
| 36926521 | `PAPER 207` | `LIT-0500` | yes | `FTR-20261004-36926521-01` partial |
| 37946251 | `PAPER 208` | `LIT-0501` | yes | `FTR-20261004-37946251-01` partial |
| 40858643 | `PAPER 209` | `LIT-0502` | yes | `FTR-20261004-40858643-01` partial |
| 41835067 | `PAPER 210` | `LIT-0503` | yes | `FTR-20261004-41835067-01` partial |
| 41477840 | `PAPER 211` | `LIT-0504` | yes | `FTR-20261004-41477840-01` partial |
| 41254692 | `PAPER 212` (promotes `CORPUS-STUB-101`) | `LIT-0505` | yes | `FTR-20261004-41254692-01` partial |

**Numbers are provisional.** `registry_records.py catalog` at commit `69db97f` (this branch = `main` 520c726 + wave-8 A work): highest landed `PAPER 200`, `LIT-0493`, `CORPUS-STUB-179`. Open wave-7 candidates already claim `PAPER 201`–`206` and `LIT-0494`–`0499` (measured by grep over `commit_candidates/`), so this candidate starts at `PAPER 207` / `LIT-0500`. Wave-8 peers B and C may collide; the integrator renumbers in event order and updates the `LIT link` / `Paper link` wikilinks, the cross-candidate links and the `insert-after` anchors (written here against `PAPER 200` / `LIT-0493`, the highest records on `main`).

## Ordering
The six receipts must be appended first. Each was dry-recorded against throwaway copies of the ledger and state manifest from `main` (`RECORDED`, exit 0, `verify` OK at 392 chained receipts on the copy; real ledger untouched). Propagate with `CC-20261004W8-A-PATIENT-OVERLAP-01`, `CC-20261004W8-A-MEASURED-01` and `CC-20261004W8-A-VPA-DIRECTION-01`, which link to these records.

## Registry statements compared with the source (correction 12)
- `CORPUS-STUB-101` carries the title and identifiers of PMID 41254692 correctly and makes no claim; promoted, not corrected.
- No other registry record cites any of the six PMIDs.

## Reading-debt discharge (correction 15)
None of the six was a cited-and-unread primary behind an existing statement. Two held statements were checked against primaries in passing: PMID 37946251's WWOX case is `PAPER 117` (Piard 2019) Patient 11, and PMID 41477840's citation of PMID 33255508 does not match that review's wording (dossier § 4).

## Change class
**MINOR** — record creation and one placeholder promotion; no claim, block or baseline touched.

## Record content
Each record's `Role` is one short sentence and points to the dossier; the substance is in the dossiers and in the three topical candidates. Exact op JSON: `## Op list` below.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on this branch at 0941054: exit 0, 8 op(s), keys PAPER 200, PAPER 207-211, CORPUS-STUB-101 ×2)

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 200",
  "text": "\n## PAPER 207\n**Short title:** Colin 2023 Front Cell Dev Biol — multi-omics diagnostics; one WWOX genotype with blood RT-PCR and a fibroblast western\n**Full title:** Stepwise use of genomics and transcriptomics technologies increases diagnostic yield in Mendelian disorders\n**Authors:** Colin E, Duffourd Y, Chevarin M, et al.; Vitobello A\n**Year:** 2023\n**Source type:** primary research — diagnostic multi-omics series\n**Journal/source:** *Front Cell Dev Biol* 2023;11:1021920\n**Identifier:** PMID 36926521 / PMCID PMC10011630 / DOI 10.3389/fcell.2023.1021920\n**Status:** processed\n**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A). Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-36926521-01`; manifest `deepdive_manifests/PMID36926521.json`; dossier `research/fulltext_dossiers/PMID36926521.md`\n**Genotype/model:** exon-1 missense `p.(Thr12Arg)` + structural variant inverting exon 5; compound heterozygous\n**Transferability:** T3 — neither allele is the reference genotype's class\n**clinical relevance:** MODERATE\n**Claim links:** none\n**Role:** RNA consequence measured for the structural allele only (exon 5 skipping, blood); fibroblast western measures the genotype qualitatively. See the dossier and `CC-20261004W8-A-MEASURED-01`.\n**LIT link:** [[literature_tracking_log_current#LIT-0500]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 207",
  "text": "\n## PAPER 208\n**Short title:** Pagnamenta 2023 Genome Med — clinical WGS cohort; its WWOX case re-reports Piard 2019 Patient 11\n**Full title:** Structural and non-coding variants increase the diagnostic yield of clinical whole genome sequencing for rare diseases\n**Authors:** Pagnamenta AT, Camps C, Giacopuzzi E, et al.; Taylor JC\n**Year:** 2023\n**Source type:** primary research — clinical whole-genome sequencing cohort\n**Journal/source:** *Genome Med* 2023;15(1):94\n**Identifier:** PMID 37946251 / PMCID PMC10636885 / DOI 10.1186/s13073-023-01240-0\n**Status:** processed\n**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A). Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-37946251-01`; manifest `deepdive_manifests/PMID37946251.json`; dossier `research/fulltext_dossiers/PMID37946251.md`\n**Genotype/model:** in-frame deletion of exons 6-8 + `c.705dup p.(His236fs)`; DNA only\n**Transferability:** none — re-report of a held patient\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Not an independent patient: the paper names it Patient 11 of [[paper_registry_current#PAPER 117]]. See `CC-20261004W8-A-PATIENT-OVERLAP-01`.\n**LIT link:** [[literature_tracking_log_current#LIT-0501]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 208",
  "text": "\n## PAPER 209\n**Short title:** Hamanaka 2025 NPJ Genom Med — genome sequencing in ID/DD; one WWOX case, intron-5 acceptor allele + exon-5 deletion, DNA only\n**Full title:** Genome sequencing provides high diagnostic yield and new etiological insights for intellectual disability and developmental delay\n**Authors:** Hamanaka K, Fujita A, Miyatake S, et al.; Matsumoto N\n**Year:** 2025\n**Source type:** primary research — diagnostic genome-sequencing cohort\n**Journal/source:** *NPJ Genom Med* 2025;10(1):60\n**Identifier:** PMID 40858643 / PMCID PMC12381280 / DOI 10.1038/s41525-025-00521-4\n**Status:** processed\n**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A). Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-40858643-01`; manifest `deepdive_manifests/PMID40858643.json`; dossier `research/fulltext_dossiers/PMID40858643.md`\n**Genotype/model:** `c.517-1G>A` + single-exon deletion spanning exon 5; trio-phased\n**Transferability:** T3 — not the reference genotype's class\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Both consequences predicted by rule; no RNA or protein. See the dossier and `CC-20261004W8-A-MEASURED-01`.\n**LIT link:** [[literature_tracking_log_current#LIT-0502]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 209",
  "text": "\n## PAPER 210\n**Short title:** Yigit 2026 Front Neurol — re-analysis in children with a cerebral-palsy diagnosis; one homozygous WWOX p.Leu239Arg child\n**Full title:** Unmasking genetic etiologies in neurodevelopmental disorders characterized by Cerebral Palsy: insights from integrative genomic approaches\n**Authors:** Yigit A, Akgun-Dogan O, Ozkeserli Z, et al.; Ozbek U\n**Year:** 2026\n**Source type:** primary research — diagnostic re-analysis cohort\n**Journal/source:** *Front Neurol* 2026;17:1742186\n**Identifier:** PMID 41835067 / PMCID PMC12979860 / DOI 10.3389/fneur.2026.1742186\n**Status:** processed\n**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A). Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-41835067-01`; manifest `deepdive_manifests/PMID41835067.json`; dossier `research/fulltext_dossiers/PMID41835067.md`\n**Genotype/model:** homozygous `c.716T>G p.(Leu239Arg)`; DNA and segregation only\n**Transferability:** T3 — not Q230P; nothing measured\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Count once: identity with [[paper_registry_current#PAPER 013]] case 50 not excluded (INFERENZA). See `CC-20261004W8-A-PATIENT-OVERLAP-01`.\n**LIT link:** [[literature_tracking_log_current#LIT-0503]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 210",
  "text": "\n## PAPER 211\n**Short title:** Stamouli 2026 Sci Adv — human glia-to-interneuron reprogramming; WWOX transcript peaks transiently along the trajectory\n**Full title:** A distinct lineage pathway drives parvalbumin chandelier cell fate in human interneuron reprogramming\n**Authors:** Stamouli CA, Degener A, Cepeda-Prado E, et al.; Rylander Ottosson D\n**Year:** 2026\n**Source type:** primary research — human cell reprogramming, snRNA-seq\n**Journal/source:** *Sci Adv* 2026;12(1):eadv0588\n**Identifier:** PMID 41477840 / PMCID PMC12757047 / DOI 10.1126/sciadv.adv0588\n**Status:** processed\n**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A). Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-41477840-01`; manifest `deepdive_manifests/PMID41477840.json`; dossier `research/fulltext_dossiers/PMID41477840.md`\n**Genotype/model:** wild-type; no WWOX manipulation\n**Transferability:** none — expression only, no requirement test\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Transcript-level background datum with a citation error; see the dossier.\n**LIT link:** [[literature_tracking_log_current#LIT-0504]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 211",
  "text": "\n## PAPER 212\n**Short title:** Qin 2025 J Transl Med — drug-target MR in a lymphoma; its drug list inverts its own CTD table\n**Full title:** Integrative multi-omics and Mendelian randomization identify WWOX and THBS2 as potential therapeutic targets in mature T/NK-cell lymphoma\n**Authors:** Qin Y, Wei J, He Y, et al.; Huang Y\n**Year:** 2025\n**Source type:** computational — Mendelian randomisation and docking\n**Journal/source:** *J Transl Med* 2025;23(1):1306\n**Identifier:** PMID 41254692 / PMCID PMC12625014 / DOI 10.1186/s12967-025-07301-9\n**Status:** processed\n**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A); promotes [[paper_registry_current#CORPUS-STUB-101]]. Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-41254692-01`; manifest `deepdive_manifests/PMID41254692.json`; dossier `research/fulltext_dossiers/PMID41254692.md`\n**Genotype/model:** none — common-variant expression instruments\n**Transferability:** none to WWOX-DEE\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Computational only. See the dossier and `CC-20261004W8-A-VPA-DIRECTION-01`.\n**LIT link:** [[literature_tracking_log_current#LIT-0505]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-101",
  "old": "**Status:** not_processed",
  "new": "**Status:** promoted — see [[paper_registry_current#PAPER 212]]"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-101",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — read at full text in intake wave 8 (2026-10-04), receipt `FTR-20261004-41254692-01`"
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; same dry run: exit 0, 6 op(s), keys LIT-0493, LIT-0500-0504)

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0493",
  "text": "\n## LIT-0500\n**Identifier:** PMID 36926521 / DOI 10.3389/fcell.2023.1021920\n**Title:** Stepwise use of genomics and transcriptomics technologies increases diagnostic yield in Mendelian disorders\n**Authors:** Colin E, Duffourd Y, Chevarin M, et al.; Vitobello A\n**Year:** 2023\n**Source type:** primary research — diagnostic multi-omics series\n**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-36926521-01`\n**clinical relevance:** MODERATE\n**Why tracked:** selected for intake wave 8 (Group A, measured vs predicted allele consequence).\n**Paper link:** [[paper_registry_current#PAPER 207]]\n**Note:** class-level record. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0500",
  "text": "\n## LIT-0501\n**Identifier:** PMID 37946251 / DOI 10.1186/s13073-023-01240-0\n**Title:** Structural and non-coding variants increase the diagnostic yield of clinical whole genome sequencing for rare diseases\n**Authors:** Pagnamenta AT, Camps C, Giacopuzzi E, et al.; Taylor JC\n**Year:** 2023\n**Source type:** primary research — clinical whole-genome sequencing cohort\n**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-37946251-01`\n**clinical relevance:** LOW\n**Why tracked:** selected for intake wave 8 (Group A, measured vs predicted allele consequence).\n**Paper link:** [[paper_registry_current#PAPER 208]]\n**Note:** class-level record. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0501",
  "text": "\n## LIT-0502\n**Identifier:** PMID 40858643 / DOI 10.1038/s41525-025-00521-4\n**Title:** Genome sequencing provides high diagnostic yield and new etiological insights for intellectual disability and developmental delay\n**Authors:** Hamanaka K, Fujita A, Miyatake S, et al.; Matsumoto N\n**Year:** 2025\n**Source type:** primary research — diagnostic genome-sequencing cohort\n**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-40858643-01`\n**clinical relevance:** LOW\n**Why tracked:** selected for intake wave 8 (Group A, measured vs predicted allele consequence).\n**Paper link:** [[paper_registry_current#PAPER 209]]\n**Note:** class-level record. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0502",
  "text": "\n## LIT-0503\n**Identifier:** PMID 41835067 / DOI 10.3389/fneur.2026.1742186\n**Title:** Unmasking genetic etiologies in neurodevelopmental disorders characterized by Cerebral Palsy: insights from integrative genomic approaches\n**Authors:** Yigit A, Akgun-Dogan O, Ozkeserli Z, et al.; Ozbek U\n**Year:** 2026\n**Source type:** primary research — diagnostic re-analysis cohort\n**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-41835067-01`\n**clinical relevance:** LOW\n**Why tracked:** selected for intake wave 8 (Group A, measured vs predicted allele consequence).\n**Paper link:** [[paper_registry_current#PAPER 210]]\n**Note:** class-level record. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0503",
  "text": "\n## LIT-0504\n**Identifier:** PMID 41477840 / DOI 10.1126/sciadv.adv0588\n**Title:** A distinct lineage pathway drives parvalbumin chandelier cell fate in human interneuron reprogramming\n**Authors:** Stamouli CA, Degener A, Cepeda-Prado E, et al.; Rylander Ottosson D\n**Year:** 2026\n**Source type:** primary research — human cell reprogramming, snRNA-seq\n**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-41477840-01`\n**clinical relevance:** LOW\n**Why tracked:** selected for intake wave 8 (Group A, measured vs predicted allele consequence).\n**Paper link:** [[paper_registry_current#PAPER 211]]\n**Note:** class-level record. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0504",
  "text": "\n## LIT-0505\n**Identifier:** PMID 41254692 / DOI 10.1186/s12967-025-07301-9\n**Title:** Integrative multi-omics and Mendelian randomization identify WWOX and THBS2 as potential therapeutic targets in mature T/NK-cell lymphoma\n**Authors:** Qin Y, Wei J, He Y, et al.; Huang Y\n**Year:** 2025\n**Source type:** computational — Mendelian randomisation and docking\n**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-41254692-01`\n**clinical relevance:** LOW\n**Why tracked:** selected for intake wave 8 (Group A, measured vs predicted allele consequence).\n**Paper link:** [[paper_registry_current#PAPER 212]]\n**Note:** class-level record. Not medical advice.\n"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the WWOX case of PMID 37946251 is a previously reported patient | Reported as Patient 11 (Table S1) in case series in Piard et al [97]. | PMID 37946251, Table 1 row 009Sev001 (image); files/supplements/PMID37946251/13073_2023_1240_Tab1_HTML.jpg)
(the PMID 41835067 WWOX genotype is homozygous with both parents carriers | Hom (maternal paternal) P (PP3, PM3, PM2, PP5) | PMID 41835067, Table 2 row CP_P14.1; files/fulltext/PMID41835067_Yigit2026_PMC.xml)
