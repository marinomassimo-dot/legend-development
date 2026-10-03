# COMMIT CANDIDATE — CC-20261003W5-B-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 5 2026-10-03, branch `task/sci-B-20261003w5`.
**context_policy:** `SOURCE_FIRST` — first pass written from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w5_B.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`paper_registry_current.md`: create `PAPER 156`-`161` after `PAPER 150`; promote `CORPUS-STUB-060` (two field updates). `literature_tracking_log_current.md`: create `LIT-0447`-`0451` after `LIT-0443`; update `LIT-0084`. `discovery_ledger_current.md`: `DL-MECH-059` gains its receipted primary.

## Registry landing per PMID handled (wave-1 correction 8)
| PMID | PAPER record | LIT record | needs creation? |
|---|---|---|---|
| 35792847 | `PAPER 156` (new; promotes `CORPUS-STUB-060`) | `LIT-0084` (exists, placeholder; updated) | PAPER yes |
| 31618474 | `PAPER 157` (new) | `LIT-0447` (new) | **yes — only `FT-140` named it** |
| 35715422 | `PAPER 158` (new) | `LIT-0448` (new) | **yes — only `DL-MECH-058/059` and `FT-140` named it** |
| 33919646 | `PAPER 159` (new) | `LIT-0449` (new) | **yes — no record at all** |
| 32214227 | `PAPER 160` (new) | `LIT-0450` (new) | **yes — only `FT-140` named it** |
| 31353122 | `PAPER 161` (new) | `LIT-0451` (new) | **yes — no record at all** (the selector's statement that it sits in the full-text-queue appendix is not reproduced by `registry_records.py get --pmid 31353122`) |

Without these, LINT's `ORPHAN_COMPLETE_READ` blocks BATCH_COMMIT once the six receipts are recorded.

**Numbers are provisional.** Measured 2026-10-03 with `registry_records.py catalog` on the branch after merging `main` f110c76: highest landed `PAPER 150`, `LIT-0443`. Open candidates on main claim up to `PAPER 155` (`CC-20261003W4-A-REGISTRY-01`) and `LIT-0446` (`CC-20261003w4-C-REGISTRY-01`), measured by `git grep` over `commit_candidates/`. This candidate takes `PAPER 156`-`161` and `LIT-0447`-`0451`; wave-5 peers (A, C) may claim the same numbers — the integrator renumbers in event order and updates the wikilinks used in the sibling candidates `CC-20261003W5-B-PATIENT-OVERLAP-01`, `-ALBARADIE-01`, `-HYPOKINESIA-01` and `-CNV-CARRIER-01`, and the `insert-after` anchors.

## Change class
**MINOR** — paper additions, a placeholder promotion and an evidence pointer on a discovery lead (§ 7). No claim status or working-model block changes.

## Ordering
Apply this candidate before its four siblings (they wikilink `PAPER 156`-`161`). If `CC-20261003W4-A-REGISTRY-01` (PAPER 151-155) lands first, the `insert-after PAPER 150` anchor still exists; renumber only on collision.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` (no `--apply`) on main f110c76 merged into the branch (no registry file changed on the branch): exit 0, 8 op(s), anchors ['PAPER 150', 'PAPER 156', 'PAPER 157', 'PAPER 158', 'PAPER 159', 'PAPER 160', 'CORPUS-STUB-060', 'CORPUS-STUB-060'])

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 150",
  "text": "\n## PAPER 156\n**Short title:** Al Baradie 2022 Epileptic Disord — nine homozygous WWOX patients in six families (P47T, R54*, c.606-1G>A, Q230P) plus a 61-patient literature table\n**Full title:** Epilepsy in patients with WWOX-related epileptic encephalopathy (WOREE) syndrome\n**Authors:** Al Baradie R, Mir A, Alsaif A, Ali M, Al Ghamdi F, Bashir S, Howsawi Y\n**Year:** 2022\n**Source type:** primary research — retrospective single-centre case series with a literature aggregation\n**Journal/source:** *Epileptic Disord* 2022;24(4):697-712\n**Identifier:** PMID 35792847 / DOI 10.1684/epd.2022.1444\n**Status:** processed\n**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Promotes [[paper_registry_current#CORPUS-STUB-060]] (kept as history).\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-35792847-01`; manifest `deepdive_manifests/PMID35792847.json`; dossier `research/fulltext_dossiers/PMID35792847.md`\n**Primary pathway:** clinical spectrum / WOREE epileptology\n**Model/species:** human\n**Genotype/model:** all homozygous: P47T (two families, three patients), R54* (two families, three patients), canonical splice acceptor `c.606-1G>A` (one non-consanguineous family, two brothers), Q230P (one patient); an affected sib of the Q230P homozygote carries Q230P heterozygous only, second allele not found at publication\n**Transferability:** T1 for the clinical course of each homozygous class; the Q230P homozygote is not the reference genotype (compound heterozygous)\n**clinical relevance:** MODERATE — first Q230P-homozygous course with neonatal onset and suppression-burst in LEGEND; P47T homozygotes intermediate between SCAR12 and WOREE\n**Claim links:** none (proposed bearing on 032 through `CC-20261003W5-B-CNV-CARRIER-01`; on DL-MECH-022 through `CC-20261003W5-B-ALBARADIE-01`)\n**Role:** 🔴 Counting: family 2 (homozygous R54* sibship) is probably the R54* sibship of [[paper_registry_current#PAPER 119]] re-described without cross-citation (`CC-20261003W5-B-PATIENT-OVERLAP-01`); net new patients 7, possibly 6 (one family-3 patient may be in Tabarki 2015, unread). The abstract's 'correlations between genotype and phenotype' are not supported by any analysis in the body (Table 3 has no genotype column). The 70-patient literature denominator double-counts Tarta-Arsene 2017 / Piard 2019 patient 8 and the Ehaideb sibship, and counts six SCAR12 patients as WOREE: **do not use its percentages as a WOREE denominator.**\n**LIT link:** [[literature_tracking_log_current#LIT-0084]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 156",
  "text": "\n## PAPER 157\n**Short title:** Burgess 2019 Ann Neurol — EIMFS genetic landscape, 135 patients; one WWOX patient (E17K + two intronic deletions, both VUS here) = patient 6 of the 2023 WWOX-DEE cohort\n**Full title:** The Genetic Landscape of Epilepsy of Infancy with Migrating Focal Seizures\n**Authors:** Burgess R, Wang S, McTague A, et al.; Scheffer IE\n**Year:** 2019\n**Source type:** primary research — international consortium cohort\n**Journal/source:** *Ann Neurol* 2019;86(6):821-831 (erratum PMID 32176372, content not retrieved)\n**Identifier:** PMID 31618474 / PMCID PMC7423163 / DOI 10.1002/ana.25619\n**Status:** processed\n**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-31618474-01` (earlier `FTR-20260921-31618474-01`, a verification of an artefact without gene symbols, tables or supplement); manifest `deepdive_manifests/PMID31618474.json`; dossier `research/fulltext_dossiers/PMID31618474.md`\n**Primary pathway:** clinical spectrum / EIMFS\n**Model/species:** human\n**Genotype/model:** one compound heterozygote: missense `c.49G>A p.(Glu17Lys)` + two intronic deletions on the other allele (introns 3 and 4, microarray); both alleles VUS in the paper's Table 2; splicing effect predicted only\n**Transferability:** T1 for the EIMFS presentation of one missense/null-class genotype\n**clinical relevance:** LOW — one patient, counted in [[paper_registry_current#PAPER 018]]\n**Claim links:** none\n**Role:** 🔴 **Not an independent patient:** [[paper_registry_current#PAPER 018]] states that its patient 6 was briefly reported here and supplies the RNA result this paper lacks (intron-4 deletion → exon 5 skipping; intron-3 deletion benign). Count once, under `PAPER 018`. Not Piard patient 12 (second allele S304F). The cohort's 6.8 Mb deletion is on chromosome 2, unrelated to the 16q case of [[paper_registry_current#PAPER 161]].\n**LIT link:** [[literature_tracking_log_current#LIT-0447]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 157",
  "text": "\n## PAPER 158\n**Short title:** Yang 2022 Sci Rep — 36 EIMFS children; the only WWOX carrier (p.M1? + p.H78Y) also carries a pathogenic ATP7A frameshift with Menkes features\n**Full title:** Analysis of clinical phenotypic and genotypic spectra in 36 children patients with Epilepsy of Infancy with Migrating Focal Seizures\n**Authors:** Yang H, Yang X, Cai F, Gan S, Yang S, Wu L\n**Year:** 2022\n**Source type:** primary research — retrospective two-centre cohort\n**Journal/source:** *Sci Rep* 2022;12:10187\n**Identifier:** PMID 35715422 / PMCID PMC9205988 / DOI 10.1038/s41598-022-13974-9\n**Status:** processed\n**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-35715422-01`; manifest `deepdive_manifests/PMID35715422.json`; dossier `research/fulltext_dossiers/PMID35715422.md`\n**Primary pathway:** clinical spectrum / EIMFS · attribution guardrail\n**Model/species:** human\n**Genotype/model:** WWOX initiator codon `p.M1?` (LP) + `p.H78Y` (VUS) with a hemizygous ATP7A frameshift (P) in one male\n**Transferability:** none for WWOX-specific inference (dual diagnosis)\n**clinical relevance:** LOW — a guardrail record\n**Claim links:** none\n**Role:** The abstract's 'WWOX may be associated with poor prognosis' is one patient who also has a Menkes-compatible ATP7A variant; Table 3 records seizure control 'ineffective' beside oxcarbazepine 'effective'. Not counted as a WWOX-DEE case. Supplies the receipted primary behind [[discovery_ledger_current#DL-MECH-059 — Una doppia diagnosi impedisce attribuzioni WWOX-specifiche|DL-MECH-059]], whose data this reading confirms.\n**LIT link:** [[literature_tracking_log_current#LIT-0448]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 158",
  "text": "\n## PAPER 159\n**Short title:** Spagnoli 2021 Int J Mol Sci — systematic review of neonatal-onset genetic epilepsy with movement disorder; all WWOX content re-describes Piard 2019\n**Full title:** Genetic Neonatal-Onset Epilepsies and Developmental/Epileptic Encephalopathies with Movement Disorders: A Systematic Review\n**Authors:** Spagnoli C, Fusco C, Percesepe A, Leuzzi V, Pisani F\n**Year:** 2021\n**Source type:** secondary — PRISMA systematic review (49 papers)\n**Journal/source:** *Int J Mol Sci* 2021;22(8):4202\n**Identifier:** PMID 33919646 / PMCID PMC8072943 / DOI 10.3390/ijms22084202\n**Status:** processed\n**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-33919646-01`; manifest `deepdive_manifests/PMID33919646.json`; dossier `research/fulltext_dossiers/PMID33919646.md`\n**Primary pathway:** movement phenotype (secondary)\n**Model/species:** human\n**Genotype/model:** six WWOX genotypes, all patients of [[paper_registry_current#PAPER 117]] (Piard 1, 2, 3, 4, 9, 11)\n**Transferability:** none beyond its source\n**clinical relevance:** LOW — secondary\n**Claim links:** none (see `CC-20261003W5-B-HYPOKINESIA-01`)\n**Role:** 🔴 Its claim that a neonatal hypokinetic movement disorder occurs only with WWOX rests on five Piard patients whose primary row reads 'poor spontaneous movements', re-labelled 'hypokinesia'; the primary's own movement-disorder row for those patients lists dystonia, myoclonus, startle, pedalling/boxing or 'no'. Zero new patients; do not cite as an independent observation.\n**LIT link:** [[literature_tracking_log_current#LIT-0449]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 159",
  "text": "\n## PAPER 160\n**Short title:** Hengel 2020 Eur J Hum Genet — first-line exome in 83 consanguineous-population families; WWOX row is the published SCAR12 G372R family\n**Full title:** First-line exome sequencing in Palestinian and Israeli Arabs with neurological disorders is efficient and facilitates disease gene discovery\n**Authors:** Hengel H, Buchert R, Sturm M, et al.; Schöls L\n**Year:** 2020\n**Source type:** primary research — family exome cohort\n**Journal/source:** *Eur J Hum Genet* 2020;28(8):1034-1043 (licence correction PMID 34050322)\n**Identifier:** PMID 32214227 / PMCID PMC7382450 / DOI 10.1038/s41431-020-0609-9\n**Status:** processed\n**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-32214227-01` (earlier `FTR-20260921-32214227-01`, a verification of an artefact without tables); manifest `deepdive_manifests/PMID32214227.json`; dossier `research/fulltext_dossiers/PMID32214227.md`\n**Primary pathway:** clinical spectrum / SCAR12 (pointer)\n**Model/species:** human\n**Genotype/model:** homozygous G372R, two affected sibs — the family of [[paper_registry_current#PAPER 042]] (Supplementary Table 1 names that publication)\n**Transferability:** none beyond its source\n**clinical relevance:** LOW — pointer\n**Claim links:** none\n**Role:** 🔴 The 2026-09-21 statement that this paper has 'zero WWOX variants' is wrong: Table 1 carries the WWOX row (the earlier artefact had lost the tables). The 'homozygous nonsense, intellectual disability, epilepsy, corpus callosum dysgenesis' row is TMCO1, not WWOX. Zero new patients.\n**LIT link:** [[literature_tracking_log_current#LIT-0450]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 160",
  "text": "\n## PAPER 161\n**Short title:** Mori 2019 Brain Dev — heterozygous 6.8 Mb 16q22.2-q23.1 deletion ending inside WWOX in an infant with West syndrome; second allele exon-clean; not attributed to WWOX\n**Full title:** A 16q22.2-q23.1 deletion identified in a male infant with West syndrome\n**Authors:** Mori T, Goji A, Toda Y, Ito H, Mori K, Kohmoto T, Imoto I, Kagami S\n**Year:** 2019\n**Source type:** primary research — single case report\n**Journal/source:** *Brain Dev* 2019;41(10):888-892 (accepted manuscript read)\n**Identifier:** PMID 31353122 / DOI 10.1016/j.braindev.2019.07.005\n**Status:** processed\n**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-31353122-01` (figures not inspected; Figure 1 is a patient photograph); manifest `deepdive_manifests/PMID31353122.json`; dossier `research/fulltext_dossiers/PMID31353122.md`\n**Primary pathway:** copy-number carriers / negative control\n**Model/species:** human\n**Genotype/model:** heterozygous 57-gene deletion whose distal breakpoint lies inside WWOX (exons removed not stated); other allele clean on exon-targeted panel; no intronic, RNA or parental testing\n**Transferability:** none for WWOX haploinsufficiency (56 other genes in the interval)\n**clinical relevance:** LOW — a counting boundary\n**Claim links:** none (proposed qualification of 032 through `CC-20261003W5-B-CNV-CARRIER-01`)\n**Role:** Not a WWOX-DEE case and not a demonstrated haploinsufficiency case; the authors decline the attribution. The drug history (seizure freedom on valproate plus lamotrigine) is one patient with a contiguous deletion and is not a WWOX treatment datum.\n**LIT link:** [[literature_tracking_log_current#LIT-0451]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-060",
  "old": "**Status:** not_processed",
  "new": "**Status:** promoted — see [[paper_registry_current#PAPER 156]]"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-060",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — upgraded to [[paper_registry_current#PAPER 156]] by `CC-20261003W5-B-REGISTRY-01` (receipt `FTR-20261003-35792847-01`); this placeholder is kept as history"
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` (no `--apply`) on main f110c76 merged into the branch (no registry file changed on the branch): exit 0, 7 op(s), anchors ['LIT-0443', 'LIT-0447', 'LIT-0448', 'LIT-0449', 'LIT-0450', 'LIT-0084', 'LIT-0084'])

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0443",
  "text": "\n## LIT-0447\n**Short title:** Burgess 2019 Ann Neurol — EIMFS landscape; one WWOX patient (= PAPER 018 patient 6)\n**Authors:** Burgess R et al.; Scheffer IE\n**Year:** 2019\n**Source type:** primary research — consortium cohort\n**Journal/source:** *Ann Neurol* 2019;86(6):821-831\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 31618474 / DOI 10.1002/ana.25619 / PMC7423163\n**Date discovered:** 2026-09-21 (FT-116 cohort triage; FT-140)\n**Date processed:** 2026-10-03 (`FTR-20261003-31618474-01`)\n**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)\n**Status:** processed\n**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`\n**Primary pathway:** clinical spectrum / EIMFS\n**Transferability:** T1 (one patient, counted under PAPER 018)\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID31618474.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0447",
  "text": "\n## LIT-0448\n**Short title:** Yang 2022 Sci Rep — 36 EIMFS children; WWOX carrier with a second (ATP7A) diagnosis\n**Authors:** Yang H et al.; Wu L\n**Year:** 2022\n**Source type:** primary research — two-centre cohort\n**Journal/source:** *Sci Rep* 2022;12:10187\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 35715422 / DOI 10.1038/s41598-022-13974-9 / PMC9205988\n**Date discovered:** before 2026-07-22 (DL-MECH-058 next-search agenda)\n**Date processed:** 2026-10-03 (`FTR-20261003-35715422-01`)\n**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)\n**Status:** processed\n**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`\n**Primary pathway:** clinical spectrum / EIMFS\n**Transferability:** none for WWOX-specific inference\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID35715422.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0448",
  "text": "\n## LIT-0449\n**Short title:** Spagnoli 2021 Int J Mol Sci — neonatal-onset genetic epilepsy with movement disorder; WWOX section re-describes Piard 2019\n**Authors:** Spagnoli C et al.; Pisani F\n**Year:** 2021\n**Source type:** secondary — systematic review\n**Journal/source:** *Int J Mol Sci* 2021;22(8):4202\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 33919646 / DOI 10.3390/ijms22084202 / PMC8072943\n**Date discovered:** 2026-10-03 (wave-5 selection; no earlier record)\n**Date processed:** 2026-10-03 (`FTR-20261003-33919646-01`)\n**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)\n**Status:** processed\n**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`\n**Primary pathway:** movement phenotype (secondary)\n**Transferability:** none beyond its source\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID33919646.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0449",
  "text": "\n## LIT-0450\n**Short title:** Hengel 2020 Eur J Hum Genet — consanguineous-population exome cohort; WWOX row = SCAR12 G372R family of PAPER 042\n**Authors:** Hengel H et al.; Schöls L\n**Year:** 2020\n**Source type:** primary research — family exome cohort\n**Journal/source:** *Eur J Hum Genet* 2020;28(8):1034-1043\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 32214227 / DOI 10.1038/s41431-020-0609-9 / PMC7382450\n**Date discovered:** 2026-09-21 (FT-116 cohort triage; FT-140)\n**Date processed:** 2026-10-03 (`FTR-20261003-32214227-01`)\n**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)\n**Status:** processed\n**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`\n**Primary pathway:** clinical spectrum / SCAR12 (pointer)\n**Transferability:** none beyond its source\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID32214227.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0450",
  "text": "\n## LIT-0451\n**Short title:** Mori 2019 Brain Dev — heterozygous 16q22.2-q23.1 deletion through WWOX, West syndrome, not attributed to WWOX\n**Authors:** Mori T et al.; Kagami S\n**Year:** 2019\n**Source type:** primary research — case report\n**Journal/source:** *Brain Dev* 2019;41(10):888-892\n**Identifier type:** PMID / DOI\n**Identifier value:** PMID 31353122 / DOI 10.1016/j.braindev.2019.07.005\n**Date discovered:** 2026-10-03 (wave-5 selection; no earlier record)\n**Date processed:** 2026-10-03 (`FTR-20261003-31353122-01`)\n**Discovery source:** Orchestrator selection record of intake wave 5 2026-10-03 (group B)\n**Status:** processed\n**Status note:** record created by `CC-20261003W5-B-REGISTRY-01`\n**Primary pathway:** copy-number carriers / negative control\n**Transferability:** none for WWOX haploinsufficiency\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w5_B.md` · `CC-20261003W5-B-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `partial_fulltext_read` (figures not inspected) — manifest `deepdive_manifests/PMID31353122.json`\n"
 },
 {
  "op": "replace-within",
  "id": "LIT-0084",
  "old": "**Status:** discovered",
  "new": "**Status:** processed"
 },
 {
  "op": "replace-within",
  "id": "LIT-0084",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none — processed 2026-10-03 (`FTR-20261003-35792847-01`, `complete_fulltext_read`) and promoted to [[paper_registry_current#PAPER 156]] by `CC-20261003W5-B-REGISTRY-01`; Al Baradie R et al. 2022, *Epileptic Disord* 24(4):697-712; nine homozygous WOREE patients, family 2 probably already counted under PAPER 119; the placeholder fields above are kept as history"
 }
]
```

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` (no `--apply`) on main f110c76 merged into the branch (no registry file changed on the branch): exit 0, 1 op(s), anchors ['DL-MECH-059'])

```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-059",
  "old": "Dossier: `staging/deepdive_PMID35715422_Yang2022.md`.",
  "new": "Dossier: `staging/deepdive_PMID35715422_Yang2022.md`. 🟢 **Receipted primary (2026-10-03, intake wave 5, Scientist B):** `FTR-20261003-35715422-01`, manifest `deepdive_manifests/PMID35715422.json`, dossier `research/fulltext_dossiers/PMID35715422.md`; every DATO line below re-verified at source (three variants and their classes, Menkes features, Table 3 inconsistency, Table 4/5 percentages); registry landing [[paper_registry_current#PAPER 158]] (provisional)."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the Yang WWOX carrier also carries a pathogenic ATP7A frameshift | Chr16:78133677T > C Chr16:78148874C > T ChrX:77271345DelG p.M1? p.H78Y p.G865Dfs*5 | PMID 35715422, Table 2, patient 10; files/fulltext/PMID35715422_Yang2022_PMC.xml)
(the authors cannot separate the two genes' contributions | We could not confirm whether it was a copathogenic gene. | PMID 35715422, Discussion; files/fulltext/PMID35715422_Yang2022_PMC.xml)
(the Burgess WWOX alleles are both VUS in the paper's own table | Intronic Deletions: Chr16:78,180,536-78,185,186 x1 and Chr16:78,200,089-78,218,016 x1 NA NA 0 NA NA NA CMA VUS | PMID 31618474, Table 2; files/fulltext/PMID31618474_Burgess2019_PMC_efetch.xml)
(the Burgess 6.8 Mb deletion is a chromosome 2 SCN1A/SCN2A deletion | Patient 54 had a heterozygous de novo 6.8 Mb deletion that included two known EIMFS genes, SCN1A and SCN2A. | PMID 31618474, Results; files/fulltext/PMID31618474_Burgess2019_PMC_efetch.xml)
(Al Baradie's literature denominator is 61 patients from 19 studies | Sixty-one patients with WWOX gene mutation and WOREE syndrome, reported in 19 studies, were identified from the literature search. | PMID 35792847, Results; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(Al Baradie counts the SCAR12 linkage family among its literature patients | Gribaa et al. (2007) [5] 3 M Seizure 9 months GTC No PHB | PMID 35792847, Table 3 (continued); files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(Hengel's homozygous nonsense row with ID, epilepsy and callosal dysgenesis is TMCO1 | TMCO1 213980 2/4 TR24* Intellectual disability, epilepsy, corpus callosum dysgenesis NM_019026.4:c.616C>T: p.(Arg206*) | PMID 32214227, Table 1; files/fulltext/PMID32214227_Hengel2020_PMC.xml)
