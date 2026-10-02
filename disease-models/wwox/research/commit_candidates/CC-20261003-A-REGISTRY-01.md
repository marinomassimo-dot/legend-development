# COMMIT CANDIDATE — CC-20261003-A-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 2 2026-10-03, branch `task/sci-A-20261003`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003_A.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
- `paper_registry_current.md`: **create** `PAPER 133` (Riva 2022, PMID 35573960 — no identity record existed) and `PAPER 134` (Dong 2023, PMID 37974179 — promotes `CORPUS-STUB-096`), inserted after `PAPER 132`; update the `Evidence depth` line of `PAPER 117`, `PAPER 016`, `PAPER 012`, `PAPER 043`; one sentence on `CORPUS-STUB-096`.
- `literature_tracking_log_current.md`: **create** `LIT-0432` (Riva) after `LIT-0431`; `LIT-0118` (Dong placeholder) gets its processed note; `LIT-0016` and `LIT-0359` get the receipt.

## Registry landing per PMID handled (wave-1 correction 8)
| PMID | PAPER record | LIT record | needs creation? |
|---|---|---|---|
| 35573960 | `PAPER 133` (new) | `LIT-0432` (new) | **yes — no identity record existed** |
| 37974179 | `PAPER 134` (new, promotes `CORPUS-STUB-096`) | `LIT-0118` (existing placeholder) | PAPER yes; LIT exists |
| 30356099 | `PAPER 117` (exists) | `LIT-0083` (exists, already promoted) | no |
| 39101447 | `PAPER 016` (exists) | `LIT-0016` (exists) | no |
| 42193054 | `PAPER 012` (exists) | `LIT-0012` (exists; untouched) | no |
| 24456803 | `PAPER 043` (exists; `CORPUS P359` placeholder kept) | `LIT-0359` (exists) | no |

**Numbers are provisional.** Measured 2026-10-03 with `registry_records.py catalog` on `main` ba5682f: highest `PAPER 132`, highest `LIT-0431` (batch 20261002 has propagated wave 1); no open candidate claims a higher number, so this candidate takes `PAPER 133`–`126` and `LIT-0432`. Wave-2 peers (B, C) may claim the same numbers; the integrator renumbers in event order and updates the wikilinks `PAPER 133`/`PAPER 134` used inside `CC-20261003-A-VIGABATRIN-01`, `CC-20261003-A-DONG-01` and `CC-20261003-A-SAPUPPO-01`, and the `insert-after` anchors.

## Change class
**MINOR** — paper additions and evidence-depth updates (§ 7). No claim status or working-model block changes.

## Ordering
The receipts `FTR-20261003-<pmid>-01` named below must be appended to the ledger before this candidate is propagated, so that no record cites a receipt the ledger does not hold.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 against `main` ba5682f with `record_scoped_edit.py apply`: exit 0, 7 op(s), keys ['PAPER 132', 'PAPER 133', 'CORPUS-STUB-096', 'PAPER 117', 'PAPER 016', 'PAPER 012', 'PAPER 043'])

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 132",
  "text": "\n## PAPER 133\n**Short title:** Riva 2022 Front Pediatr — WOREE with p.Arg264* and an exon-6-only deletion missed by exome CNV calling; fibroblast RT-PCR\n**Full title:** A Phenotypic-Driven Approach for the Diagnosis of WOREE Syndrome\n**Authors:** Riva A, Nobile G, Giacomini T, et al.; Zara F, Iacomino M\n**Year:** 2022\n**Source type:** primary research — single case report\n**Journal/source:** *Front Pediatr* 2022;10:847549\n**Identifier:** PMID 35573960 / PMCID PMC9100683 / DOI 10.3389/fped.2022.847549\n**Status:** processed\n**Record provenance:** created by `CC-20261003-A-REGISTRY-01` (intake wave 2 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-35573960-01`; manifest `deepdive_manifests/PMID35573960.json`; dossier `research/fulltext_dossiers/PMID35573960.md`\n**Primary pathway:** clinical spectrum / WWOX-DEE · allele detection\n**Model/species:** human\n**Genotype/model:** stop `c.790C>T p.(Arg264*)` (exon 7) + 84.8 kb deletion removing exon 6 only (out-of-frame skip), each from an unaffected parent; predicted null/null\n**Transferability:** T1 for allele detection; T3 for any genotype with residual protein\n**clinical relevance:** MODERATE — a measured transcript consequence of an exon deletion (exon 5–7 junction in patient fibroblast RNA) and an exome CNV false negative\n**Claim links:** 001 (drug-response observation, through `CC-20261003-A-VIGABATRIN-01`)\n**Role:** Day-1 onset; vigabatrin, ACTH, ketogenic diet and five other drugs ineffective; phenobarbital and nitrazepam stopped for adverse events (not reported ineffective). 🔴 The exome CNV analysis was *«unremarkable»*: allele-class censuses built on NGS-diagnosed patients are lower bounds for single-exon deletions. No protein; the stop allele's NMD not tested.\n**LIT link:** [[literature_tracking_log_current#LIT-0432]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 133",
  "text": "\n## PAPER 134\n**Short title:** Dong 2023 BMC Med Genomics — compound WWOX deletions (exons 6–8 / intron-5 + exon-6) resolved by WGS and gap PCR after exome called a homozygous exon 6 deletion\n**Full title:** Identification of compound heterozygous deletion of the WWOX gene in WOREE syndrome\n**Authors:** Dong XS, Wen XJ, Zhang S, Wang DG, Xiong Y, Li ZM\n**Year:** 2023\n**Source type:** primary research — single case report with structural-variant resolution\n**Journal/source:** *BMC Med Genomics* 2023;16:291\n**Identifier:** PMID 37974179 / PMCID PMC10652538 / DOI 10.1186/s12920-023-01731-4\n**Status:** processed\n**Record provenance:** created by `CC-20261003-A-REGISTRY-01`; promotes [[paper_registry_current#CORPUS-STUB-096]] (kept as history). Provisional number.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-37974179-01`; manifest `deepdive_manifests/PMID37974179.json`; dossier `research/fulltext_dossiers/PMID37974179.md`\n**Primary pathway:** clinical spectrum / allele architecture\n**Model/species:** human\n**Genotype/model:** one allele: 177 kb deletion of exons 6–8 (in-frame, predicted); other allele: two separate deletions — 13.26 kb inside intron 5 and 53.9 kb removing exon 6 only (out-of-frame, predicted); breakpoints by gap PCR and Sanger, phase by segregation\n**Transferability:** T1 for allele detection; none for missense or splice-acceptor classes\n**clinical relevance:** MODERATE — the exome call was right on exon-6 dosage and blind to the heterozygous loss of exons 7–8 and to phase\n**Claim links:** none\n**Role:** No RNA or protein from either allele. 🔴 Source-internal defects: the inheritance sentence swaps the two deletion sizes of the two-deletion allele; the pedigree draws the proband with the female symbol while the text and supplement say male; the *«earliest onset»* claim (day 15) is contradicted by published day-1 onsets, and the drug-resistance clause is verbatim from PMID 35573960 although only two drugs are named. Tabulated again by PMID 42193054 under a wrong reference number — count once.\n**LIT link:** [[literature_tracking_log_current#LIT-0118]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-096",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — upgraded to [[paper_registry_current#PAPER 134]] by `CC-20261003-A-REGISTRY-01` (receipt `FTR-20261003-37974179-01`); this placeholder is kept as history"
 },
 {
  "op": "replace-within",
  "id": "PAPER 117",
  "old": "**Evidence depth:** `partial_fulltext_read` — receipts `FTR-20260811-30356099-01` and `FTR-20260921-30356099-02` (a third, `FTR-20260927-30356099-03`, reads the presentation-age and diagnosis-age questions); manifest `deepdive_manifests/PMID30356099.json`",
  "new": "**Evidence depth:** `partial_fulltext_read` — receipts `FTR-20260811-30356099-01` and `FTR-20260921-30356099-02` (a third, `FTR-20260927-30356099-03`, reads the presentation-age and diagnosis-age questions); a fourth, `FTR-20261003-30356099-01`, reads every section, all three figures and Supplemental Tables 1–4, and stays partial only because the manifest's multihop queue (nine WWOX-direct references) is open; manifest `deepdive_manifests/PMID30356099.json`; dossier `research/fulltext_dossiers/PMID30356099.md`"
 },
 {
  "op": "replace-within",
  "id": "PAPER 016",
  "old": "**Evidence depth:** full text reviewed (PMC open access)",
  "new": "**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-39101447-01` (earlier: `FTR-20260921-39101447-01`, partial); manifest `deepdive_manifests/PMID39101447.json`; dossier `research/fulltext_dossiers/PMID39101447.md`"
 },
 {
  "op": "replace-within",
  "id": "PAPER 012",
  "old": "**Evidence depth:** full text reviewed",
  "new": "**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-42193054-01` (the earlier `FTR-20260726-42193054-01` is a legacy reconstruction); manifest `deepdive_manifests/PMID42193054.json`; dossier `research/fulltext_dossiers/PMID42193054.md`"
 },
 {
  "op": "replace-within",
  "id": "PAPER 043",
  "old": "**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read)",
  "new": "**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-24456803-01` (the earlier `FTR-20260726-24456803-01` is a legacy reconstruction without a coverage map, so the previous `complete` wording had no receipt behind it until now); manifest `deepdive_manifests/PMID24456803.json`; dossier `research/fulltext_dossiers/PMID24456803.md`"
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; dry run 2026-10-03 against `main` ba5682f with `record_scoped_edit.py apply`: exit 0, 4 op(s), keys ['LIT-0431', 'LIT-0118', 'LIT-0016', 'LIT-0359'])

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0431",
  "text": "\n## LIT-0432\n**Short title:** Riva 2022 Front Pediatr — WOREE with p.Arg264* and an exon-6-only deletion missed by exome CNV calling\n**Authors:** Riva A et al.; Zara F, Iacomino M\n**Year:** 2022\n**Source type:** primary research — single case report\n**Journal/source:** *Front Pediatr* 2022;10:847549\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 35573960 / DOI 10.3389/fped.2022.847549 / PMC9100683\n**Date discovered:** before 2026-07-05 (cited in the discovery ledger, DL-MOL-007, with no identity record)\n**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-35573960-01`)\n**Discovery source:** Orchestrator selection record of intake wave 2 2026-10-03\n**Status:** processed\n**Status note:** `complete_fulltext_read`; record created by `CC-20261003-A-REGISTRY-01`\n**Primary pathway:** clinical spectrum / WWOX-DEE · allele detection\n**Transferability:** T1 for allele detection; T3 for genotypes with residual protein\n**clinical relevance:** MODERATE\n**Claim links:** 001 (through `CC-20261003-A-VIGABATRIN-01`)\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003_A.md` · `CC-20261003-A-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID35573960.json`\n"
 },
 {
  "op": "replace-within",
  "id": "LIT-0118",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none — processed 2026-10-03 (`FTR-20261003-37974179-01`, `complete_fulltext_read`) and promoted to [[paper_registry_current#PAPER 134]] by `CC-20261003-A-REGISTRY-01`; Dong XS et al. 2023, *BMC Med Genomics* 16:291; the placeholder fields above are kept as history"
 },
 {
  "op": "replace-within",
  "id": "LIT-0016",
  "old": "**Evidence depth:** full text reviewed (PMC open access)",
  "new": "**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-39101447-01`; manifest `deepdive_manifests/PMID39101447.json`"
 },
 {
  "op": "replace-within",
  "id": "LIT-0359",
  "old": "**Next action:** full-text retrieval + deep-dive in next session",
  "new": "**Next action:** none — promoted earlier to [[paper_registry_current#PAPER 043]]; first receipted full-text read 2026-10-03 (`FTR-20261003-24456803-01`, `complete_fulltext_read`)"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the exome CNV analysis did not detect the exon-6 deletion | No other potentially pathogenic variants were identified in the exome. CNVs analysis was also unremarkable. | PMID 35573960, Results, Mutation Identification and Confirmation; files/fulltext/PMID35573960_Riva2022_PMC.xml)
(the deletion's transcript was examined in patient fibroblast RNA | The RT-PCR derived from fibroblast extracts of patient and unaffected parents and age-matched neurotypical control | PMID 35573960, Methods, Agarose Gel Electrophoresis; files/fulltext/PMID35573960_Riva2022_PMC.xml)
(the exome reported a homozygous exon 6 deletion | The WES analysis revealed a homozygous deletion involving exon 6 of the WWOX gene in the proband. | PMID 37974179, Results, Molecular findings; files/fulltext/PMID37974179_Dong2023_PMC.xml)
(the in-frame exons 6-8 deletion's consequence is not measured | theoretically produces a protein with normal WW domains, but due to the disruption of the SDR domain, it may retain poor residual function | PMID 37974179, Discussion para 2; files/fulltext/PMID37974179_Dong2023_PMC.xml)
