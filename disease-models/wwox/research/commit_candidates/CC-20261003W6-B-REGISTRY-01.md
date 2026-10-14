# COMMIT CANDIDATE — CC-20261003W6-B-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 6 2026-10-03, branch `task/sci-B-20261003w6`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w6_B.md`).
**Not medical advice.** Class-level statements about published patients only.

## Target
- `paper_registry_current.md`: **create** `PAPER 157`–`PAPER 162`, inserted after `PAPER 156`.
- `literature_tracking_log_current.md`: **create** `LIT-0450`–`LIT-0455`, inserted after `LIT-0449`.

## Registry landing per PMID handled (wave-1 correction 8)
| PMID | PAPER record | LIT record | needs creation? | prior presence |
|---|---|---|---|---|
| 40126049 | `PAPER 157` (new) | `LIT-0450` (new) | **yes** | none (`paper_packet.py`: identity none, receipts 0) |
| 40019827 | `PAPER 158` (new) | `LIT-0451` (new) | **yes** | none |
| 39850204 | `PAPER 159` (new) | `LIT-0452` (new) | **yes** | none |
| 38540325 | `PAPER 160` (new) | `LIT-0453` (new) | **yes** | none |
| 40217411 | `PAPER 161` (new) | `LIT-0454` (new) | **yes** | none |
| 42068099 | `PAPER 162` (new) | `LIT-0455` (new) | **yes** | none |

No `CORPUS-STUB` is promoted (none exists for these PMIDs). No existing registry statement about these six papers existed to compare against (correction 12: nothing to correct).

**Numbers are provisional.** Measured 2026-10-03 with `registry_records.py catalog` (highest landed `PAPER 150`, `LIT-0443`), then re-measured after merging `main` 4b1374d: the landed, unpropagated `CC-20261003W6-C-REGISTRY-01` claims `PAPER 151`-`156` and `LIT-0444`-`0449`, so this candidate takes `PAPER 157`-`162` and `LIT-0450`-`0455` and anchors its first inserts on `PAPER 156` / `LIT-0449`. **Ordering:** propagate after `CC-20261003W6-C-REGISTRY-01`; if that candidate is renumbered or not propagated, re-anchor on the highest `PAPER` / `LIT` then present. The integrator renumbers in event order and rewrites the `LIT link` wikilinks.

## Change class
**MINOR** — paper additions only (§ 7).

## Ordering
The six receipts `FTR-20261003-<pmid>-01` must be appended before propagation.

## Op list — `paper_registry_current.md` (dry run 2026-10-03, `record_scoped_edit.py apply`, numbered 151-156 and anchored on `PAPER 150` before the renumbering: exit 0, 6 ops; the renumbered list differs only in numbers and first anchor, which does not exist until C's candidate is propagated)
```json
[
 {
  "op": "insert-after",
  "id": "PAPER 156",
  "text": "\n## PAPER 157\n**Short title:** Cerulli Irelli 2025 Epilepsia — purified cannabidiol in 266 monogenic epilepsies; one Table 2 row of three WWOX patients (response at last follow-up)\n**Full title:** Expanding the therapeutic role of highly purified cannabidiol in monogenic epilepsies: A multicenter real-world study\n**Authors:** Cerulli Irelli E, Mazzeo A, Caraballo RH, et al.; Orsini A, Coppola A\n**Year:** 2025\n**Source type:** primary research — retrospective multicentre real-world cohort\n**Journal/source:** *Epilepsia* 2025;66:2253-2267\n**Identifier:** PMID 40126049 / PMCID PMC12291005 / DOI 10.1111/epi.18378\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-40126049-01`; manifest `deepdive_manifests/PMID40126049.json`; dossier `research/fulltext_dossiers/PMID40126049.md`\n**Primary pathway:** drug response (cannabidiol) · denominator\n**Model/species:** human\n**Genotype/model:** three WWOX patients, alleles not printed\n**Transferability:** T3 — n = 3, adjunctive, uncontrolled; no allele class\n**clinical relevance:** LOW-MODERATE — the only genotype-stratified CBD response row naming WWOX\n**Claim links:** none (see `CC-20261003W6-B-CBDRESPONSE-01`, DL-MECH-030)\n**Role:** Table 2 row WWOX (3 pts): mean seizure reduction 41.7 % (SD 38.2), ≥50 % responders 2/3, CGI-I improved 2/3, at last follow-up (minimum 3 months) on >99 % purified CBD added to a median of three ASMs. 🔴 No allele, age, syndrome, dose or follow-up length for these three; the authors warn that rows of two or three may reflect chance; overlap with held WWOX cases undetermined (INFERENZA); count once as an unlinked aggregate. Not medical advice.\n**LIT link:** [[literature_tracking_log_current#LIT-0450]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 157",
  "text": "\n## PAPER 158\n**Short title:** Innes 2025 Dev Med Child Neurol — IESS aetiopathogenesis and ACTH/corticosteroid mechanisms (scoping review); WWOX in two re-tabulated cohort rows\n**Full title:** Aetiopathogenesis of infantile epileptic spasms syndrome and mechanisms of action of adrenocorticotrophin hormone/corticosteroids in children: A scoping review\n**Authors:** Innes EA, Han VX, Patel S, Farrar MA, Gill D, Mohammad SS, Dale RC\n**Year:** 2025\n**Source type:** secondary — scoping review\n**Journal/source:** *Dev Med Child Neurol* 2025;67:1004-1025\n**Identifier:** PMID 40019827 / PMCID PMC12237231 / DOI 10.1111/dmcn.16273\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-40019827-01`; manifest `deepdive_manifests/PMID40019827.json`; dossier `research/fulltext_dossiers/PMID40019827.md`\n**Primary pathway:** denominator (IESS genetics) · ACTH mechanism\n**Model/species:** human\n**Genotype/model:** none of its own; re-tabulates WWOX (4) from PMID 37583270 and WWOX (1) from PMID 29455050\n**Transferability:** none for WWOX — re-tabulation only\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Two WWOX counts from two independent cohorts (4 + 1); no WWOX response; ACTH effect placed at a regulatory, not gene-specific, level. 🔴 The four are already held via PMID 37583270; the single patient's primary (PMID 29455050) is unread. Adds no new patient.\n**LIT link:** [[literature_tracking_log_current#LIT-0451]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 158",
  "text": "\n## PAPER 159\n**Short title:** Zhu 2025 Front Pediatr — etiology of 361 IESS patients; one WWOX patient, no allele or response\n**Full title:** Infantile epileptic spasms syndrome: an etiologic study of 361 patients with infantile epileptic spasms syndrome\n**Authors:** Zhu L, Xia Y, Ding H, Zhang T, Li J, Li B\n**Year:** 2025\n**Source type:** primary research — retrospective two-hospital series\n**Journal/source:** *Front Pediatr* 2025;12:1522079\n**Identifier:** PMID 39850204 / PMCID PMC11754263 / DOI 10.3389/fped.2024.1522079\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-39850204-01`; manifest `deepdive_manifests/PMID39850204.json`; dossier `research/fulltext_dossiers/PMID39850204.md`\n**Primary pathway:** denominator (IESS)\n**Model/species:** human\n**Genotype/model:** one WWOX patient in the Genetic (37) group; alleles not printed\n**Transferability:** denominator only\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** 1 WWOX patient among 361 IESS (58 of the 165 'unknown' never genetically tested); authors' 'enzyme synthesis-related' grouping of WWOX is an unassayed construct. 🔴 Etiology only — no WWOX treatment or response.\n**LIT link:** [[literature_tracking_log_current#LIT-0452]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 159",
  "text": "\n## PAPER 160\n**Short title:** Snyder 2024 Genes — IESS genetics and precision-medicine opportunities (narrative review); WWOX one uncited autosomal-recessive list entry\n**Full title:** Genetic Advancements in Infantile Epileptic Spasms Syndrome and Opportunities for Precision Medicine\n**Authors:** Snyder HE, Jain P, RamachandranNair R, Jones KC, Whitney R\n**Year:** 2024\n**Source type:** secondary — narrative review\n**Journal/source:** *Genes (Basel)* 2024;15(3):266\n**Identifier:** PMID 38540325 / PMCID PMC10970414 / DOI 10.3390/genes15030266\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-38540325-01`; manifest `deepdive_manifests/PMID38540325.json`; dossier `research/fulltext_dossiers/PMID38540325.md`\n**Primary pathway:** denominator (IESS genetics) · precision medicine\n**Model/species:** human\n**Genotype/model:** none\n**Transferability:** none\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** WWOX listed (no citation) among autosomal-recessive IESS genes; the precision-medicine section names no WWOX or recessive-LoF strategy. 🔴 Gene-list membership only.\n**LIT link:** [[literature_tracking_log_current#LIT-0453]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 160",
  "text": "\n## PAPER 161\n**Short title:** Yuan 2025 Acta Epileptol — genetic DEE with movement disorders; WWOX top-ten gene, pooled 18-patient row (dystonia 15/18)\n**Full title:** Advances in genetic developmental and epileptic encephalopathies with movement disorders\n**Authors:** Yuan M, Wang X, Yang Z, Luo H, Gan J, Luo R\n**Year:** 2025\n**Source type:** secondary — narrative review with bibliometric step\n**Journal/source:** *Acta Epileptol* 2025;7(1):9\n**Identifier:** PMID 40217411 / PMCID PMC11960234 / DOI 10.1186/s42494-024-00194-z\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-40217411-01`; manifest `deepdive_manifests/PMID40217411.json`; dossier `research/fulltext_dossiers/PMID40217411.md`\n**Primary pathway:** movement phenotype\n**Model/species:** human\n**Genotype/model:** 18 pooled WWOX patients from unnamed primaries\n**Transferability:** none for counting — primaries not named\n**clinical relevance:** LOW\n**Claim links:** none (see `CC-20261003W6-B-MOVEMENT-01`)\n**Role:** Table 2 WWOX: dystonia 15/18, hypokinesia 5/18, ataxia 2/18, myoclonus 1/18, tremor 1/18, chorea 0, stereotypies 0. Table 1 (OMIM) lists WWOX under dystonia, myoclonus, ataxia, tremor, hypokinesia — not chorea. The 2021 'neonatal hypokinesia only with WWOX' framing is not repeated. 🔴 The 18 cannot be de-duplicated against held cases; text-table mismatches for other genes (CACNA1A).\n**LIT link:** [[literature_tracking_log_current#LIT-0454]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 161",
  "text": "\n## PAPER 162\n**Short title:** Mohammad 2026 Mov Disord Clin Pract — movement disorders in DEE (non-systematic review); four WWOX rows, all citing one cohort\n**Full title:** Movement Disorders in Developmental and Epileptic Encephalopathies\n**Authors:** Mohammad S, Ebrahimi-Fakhari D, Morales-Briceno H\n**Year:** 2026\n**Source type:** secondary — non-systematic structured review\n**Journal/source:** *Mov Disord Clin Pract* 2026\n**Identifier:** PMID 42068099 / PMCID PMC13339248 / DOI 10.1002/mdc3.70641\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-42068099-01`; manifest `deepdive_manifests/PMID42068099.json`; dossier `research/fulltext_dossiers/PMID42068099.md`\n**Primary pathway:** movement phenotype · neuroimaging\n**Model/species:** human\n**Genotype/model:** none of its own\n**Transferability:** none — re-description\n**clinical relevance:** LOW\n**Claim links:** none (see `CC-20261003W6-B-MOVEMENT-01`)\n**Role:** WWOX in four Table 2 rows (IESS, excessive startle/hyperekplexia, corpus callosum abnormalities, white matter changes), every one citing PMID 36779245. 🔴 One cohort re-described four times; not corroboration; inherits the PUBLICATION_INTEGRITY_HOLD of PMID 36779245.\n**LIT link:** [[literature_tracking_log_current#LIT-0455]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 }
]
```

## Op list — `literature_tracking_log_current.md` (dry run 2026-10-03 before renumbering, anchored on `LIT-0443`: exit 0, 6 ops; same caveat)
```json
[
 {
  "op": "insert-after",
  "id": "LIT-0449",
  "text": "\n## LIT-0450\n**Short title:** Cerulli Irelli 2025 Epilepsia — purified cannabidiol in 266 monogenic epilepsies; one Table 2 row of three WWOX patients (response at last follow-up)\n**Authors:** Cerulli Irelli E, Mazzeo A, Caraballo RH, et al.; Orsini A, Coppola A\n**Year:** 2025\n**Source type:** primary research — retrospective multicentre real-world cohort\n**Journal/source:** *Epilepsia* 2025;66:2253-2267\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 40126049 / DOI 10.1111/epi.18378 / PMC12291005\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)\n**Date processed:** 2026-10-03 (`FTR-20261003-40126049-01`)\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** `partial_fulltext_read`; record created by `CC-20261003W6-B-REGISTRY-01`\n**Primary pathway:** drug response (cannabidiol) · denominator\n**Transferability:** T3 — n = 3, adjunctive, uncontrolled; no allele class\n**clinical relevance:** LOW-MODERATE — the only genotype-stratified CBD response row naming WWOX\n**Claim links:** none (see `CC-20261003W6-B-CBDRESPONSE-01`, DL-MECH-030)\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01` · `CC-20261003W6-B-CBDRESPONSE-01`\n**Next action:** none owed\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID40126049.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0450",
  "text": "\n## LIT-0451\n**Short title:** Innes 2025 Dev Med Child Neurol — IESS aetiopathogenesis and ACTH/corticosteroid mechanisms (scoping review); WWOX in two re-tabulated cohort rows\n**Authors:** Innes EA, Han VX, Patel S, Farrar MA, Gill D, Mohammad SS, Dale RC\n**Year:** 2025\n**Source type:** secondary — scoping review\n**Journal/source:** *Dev Med Child Neurol* 2025;67:1004-1025\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 40019827 / DOI 10.1111/dmcn.16273 / PMC12237231\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)\n**Date processed:** 2026-10-03 (`FTR-20261003-40019827-01`)\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** `partial_fulltext_read`; record created by `CC-20261003W6-B-REGISTRY-01`\n**Primary pathway:** denominator (IESS genetics) · ACTH mechanism\n**Transferability:** none for WWOX — re-tabulation only\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01`\n**Next action:** read Ko 2018 (PMID 29455050), the primary of the single-patient WWOX row, before counting that patient\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID40019827.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0451",
  "text": "\n## LIT-0452\n**Short title:** Zhu 2025 Front Pediatr — etiology of 361 IESS patients; one WWOX patient, no allele or response\n**Authors:** Zhu L, Xia Y, Ding H, Zhang T, Li J, Li B\n**Year:** 2025\n**Source type:** primary research — retrospective two-hospital series\n**Journal/source:** *Front Pediatr* 2025;12:1522079\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 39850204 / DOI 10.3389/fped.2024.1522079 / PMC11754263\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)\n**Date processed:** 2026-10-03 (`FTR-20261003-39850204-01`)\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** `partial_fulltext_read`; record created by `CC-20261003W6-B-REGISTRY-01`\n**Primary pathway:** denominator (IESS)\n**Transferability:** denominator only\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID39850204.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0452",
  "text": "\n## LIT-0453\n**Short title:** Snyder 2024 Genes — IESS genetics and precision-medicine opportunities (narrative review); WWOX one uncited autosomal-recessive list entry\n**Authors:** Snyder HE, Jain P, RamachandranNair R, Jones KC, Whitney R\n**Year:** 2024\n**Source type:** secondary — narrative review\n**Journal/source:** *Genes (Basel)* 2024;15(3):266\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 38540325 / DOI 10.3390/genes15030266 / PMC10970414\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)\n**Date processed:** 2026-10-03 (`FTR-20261003-38540325-01`)\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** `partial_fulltext_read`; record created by `CC-20261003W6-B-REGISTRY-01`\n**Primary pathway:** denominator (IESS genetics) · precision medicine\n**Transferability:** none\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID38540325.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0453",
  "text": "\n## LIT-0454\n**Short title:** Yuan 2025 Acta Epileptol — genetic DEE with movement disorders; WWOX top-ten gene, pooled 18-patient row (dystonia 15/18)\n**Authors:** Yuan M, Wang X, Yang Z, Luo H, Gan J, Luo R\n**Year:** 2025\n**Source type:** secondary — narrative review with bibliometric step\n**Journal/source:** *Acta Epileptol* 2025;7(1):9\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 40217411 / DOI 10.1186/s42494-024-00194-z / PMC11960234\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)\n**Date processed:** 2026-10-03 (`FTR-20261003-40217411-01`)\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** `partial_fulltext_read`; record created by `CC-20261003W6-B-REGISTRY-01`\n**Primary pathway:** movement phenotype\n**Transferability:** none for counting — primaries not named\n**clinical relevance:** LOW\n**Claim links:** none (see `CC-20261003W6-B-MOVEMENT-01`)\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01` · `CC-20261003W6-B-MOVEMENT-01`\n**Next action:** none owed\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID40217411.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0454",
  "text": "\n## LIT-0455\n**Short title:** Mohammad 2026 Mov Disord Clin Pract — movement disorders in DEE (non-systematic review); four WWOX rows, all citing one cohort\n**Authors:** Mohammad S, Ebrahimi-Fakhari D, Morales-Briceno H\n**Year:** 2026\n**Source type:** secondary — non-systematic structured review\n**Journal/source:** *Mov Disord Clin Pract* 2026\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 42068099 / DOI 10.1002/mdc3.70641 / PMC13339248\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6, group B)\n**Date processed:** 2026-10-03 (`FTR-20261003-42068099-01`)\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** `partial_fulltext_read`; record created by `CC-20261003W6-B-REGISTRY-01`\n**Primary pathway:** movement phenotype · neuroimaging\n**Transferability:** none — re-description\n**clinical relevance:** LOW\n**Claim links:** none (see `CC-20261003W6-B-MOVEMENT-01`)\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_B.md` · `CC-20261003W6-B-REGISTRY-01` · `CC-20261003W6-B-MOVEMENT-01`\n**Next action:** none owed\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID42068099.json`\n"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the 124-case confirmed-genetic cohort lists four WWOX | STXBP1 (4), WWOX (4), SCN1A (4) | PMID 40019827, Table 3; files/fulltext/PMID40019827_Innes2025_PMC.xml)
(the 128-case panel cohort lists one WWOX | KCNB1 (2), DNM1 (2), SCN2A (2), ARX (1), WWOX (1), BRAT (1) | PMID 40019827, Table 2 row Ko et al.; files/fulltext/PMID40019827_Innes2025_PMC.xml)
(58 of the unknown-etiology cases were never genetically tested | 165 cases (45.7%, including 58 that were not genetically tested) were classified as unknown | PMID 39850204, Results para 1; files/fulltext/PMID39850204_Zhu2025_PMC.xml)
(WWOX is placed in an enzyme-synthesis grouping | enzyme synthesis-related: NARS1, MECP2, UBA5, CLU4B, WWOX, RAB3GAP1, and IARS2 | PMID 39850204, Discussion; files/fulltext/PMID39850204_Zhu2025_PMC.xml)
(WWOX is in the autosomal-recessive gene list | TBC1D24; TBCD; TNK2; UGP2; VRK2; WWOX | PMID 38540325, Table 2; files/fulltext/PMID38540325_Snyder2024_PMC.xml)

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261003_005` · 2026-10-03 · ACTOR_ID `scientist` (Scientist J, batch integrator), under the operator's standing authorisation *«procedi sempre»*
**Operations applied:** 12
**Change class as judged by the batch:** MINOR (§7) — every target's live `Status` was read from the registry before judging.

`PAPER 189`–`194` and `LIT-0482`–`0487` created. **Renumbered** from the provisional `PAPER 157`–`162` / `LIT-0450`–`0455`; the candidate's declared ordering was honoured (group C first, then B, then A), so its first anchors became `PAPER 188` and `LIT-0481`, group C's last records. `partial full text` added beside every `partial_fulltext_read`.

**Nothing above this line was rewritten.**
