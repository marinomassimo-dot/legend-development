# COMMIT CANDIDATE — CC-20261003W3-A-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 3 2026-10-03, branch `task/sci-A-20261003w3`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w3_A.md`, which also declares two exposures before reading).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
- `paper_registry_current.md`: **create** `PAPER 142` (Nagarajan 2023, PMID 37583270 — no identity record existed), `PAPER 143` (Sukkar 2022, PMID 35712340 — promotes `CORPUS-STUB-141`) and `PAPER 144` (Serce Pehlevan 2026, PMID 42092735 — no identity record existed; resolves `FT-106`), inserted after `PAPER 141`; two field updates on `CORPUS-STUB-141`.
- `literature_tracking_log_current.md`: **create** `LIT-0440` (Nagarajan) and `LIT-0441` (Serce Pehlevan) after `LIT-0439`; update `LIT-0160` (Sukkar placeholder), `LIT-0013`, `LIT-0343`, `LIT-0298`.

## Registry landing per PMID handled (wave-1 correction 8)
| PMID | PAPER record | LIT record | needs creation? | evidence-depth update carried by |
|---|---|---|---|---|
| 41153369 | `PAPER 013` (exists) | `LIT-0013` (exists) | no | `CC-20261003W3-A-L239R-01` (PAPER) · this candidate (LIT) |
| 37583270 | `PAPER 142` (new) | `LIT-0440` (new) | **yes — no identity record existed** (only `DL-MECH-060`, `FT-144`) | this candidate |
| 27495153 | `PAPER 049` (exists; `CORPUS P343` placeholder kept) | `LIT-0343` (exists) | no | `CC-20261003W3-A-W44X-01` (PAPER) · this candidate (LIT) |
| 35712340 | `PAPER 143` (new, promotes `CORPUS-STUB-141`) | `LIT-0160` (exists, placeholder) | PAPER yes; LIT exists | this candidate |
| 42092735 | `PAPER 144` (new) | `LIT-0441` (new) | **yes — only `FT-106` existed** | this candidate |
| 38161429 | `PAPER 046` (exists; `CORPUS P298` placeholder kept) | `LIT-0298` (exists) | no | `CC-20261003W3-A-BATTAGLIA-01` (PAPER) · this candidate (LIT) |

**Numbers are provisional.** Measured 2026-10-03 with `registry_records.py catalog` on `main` c740c6e (after merging): highest landed `PAPER 132`, highest landed `LIT-0431`. The open, unpropagated wave-2 registry candidates claim beyond that: `CC-20261003-A-REGISTRY-01` (`PAPER 133`-`134`, `LIT-0432`), `CC-20261003-B-REGISTRY-01` and `CC-20261003-C-REGISTRY-01` (together up to `PAPER 141` and `LIT-0439`, measured by `git grep` over `commit_candidates/`). This candidate therefore takes `PAPER 142`-`144` and `LIT-0440`-`0441`. Wave-3 peers (B, C) may claim the same numbers; the integrator renumbers in event order and updates the wikilinks `PAPER 142`/`143`/`144` used in `CC-20261003W3-A-L239R-01` and `CC-20261003W3-A-VIGABATRIN-01`, and the `insert-after` anchors.

## Change class
**MINOR** — paper additions, placeholder promotion and evidence-depth / next-action updates (§ 7). No claim status or working-model block changes.

## Ordering
1. The wave-2 registry candidates (`CC-20261003-A-REGISTRY-01`, `-B-REGISTRY-01`, `-C-REGISTRY-01`) first: together they create the anchors `PAPER 141` and `LIT-0439`. If they are not propagated in the same batch, re-anchor the first insert of each op list on the highest `PAPER` / `LIT` record then present.
2. The receipts named below must be appended to the ledger before this candidate is propagated, so that no record cites a receipt the ledger does not hold. Receipts: `FTR-20261003-37583270-01`, `FTR-20261003-35712340-01`, `FTR-20261003-42092735-01`, `FTR-20261003-41153369-01`, `FTR-20261003-27495153-01`, `FTR-20261003-38161429-01`.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` c740c6e after applying the three wave-2 registry candidates' paper ops in A, C, B order: exit 0, 5 op(s), keys ['PAPER 141', 'PAPER 142', 'PAPER 143', 'CORPUS-STUB-141', 'CORPUS-STUB-141'])

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 141",
  "text": "\n## PAPER 142\n**Short title:** Nagarajan 2023 Epilepsia Open — genetic IESS in 124 children; four biallelic WWOX with per-patient treatment and outcome\n**Full title:** Landscape of genetic infantile epileptic spasms syndrome — A multicenter cohort of 124 children from India\n**Authors:** Nagarajan B, Gowda VK, Yoganathan S, et al.; Sahu JK\n**Year:** 2023\n**Source type:** primary research — multicentre cross-sectional cohort of genetically confirmed IESS\n**Journal/source:** *Epilepsia Open* 2023;8:1383-1404\n**Identifier:** PMID 37583270 / PMCID PMC10690684 / DOI 10.1002/epi4.12811\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-A-REGISTRY-01` (intake wave 3 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-37583270-01` (earlier: `FTR-20260921-37583270-01`, partial); manifest `deepdive_manifests/PMID37583270.json`; dossier `research/fulltext_dossiers/PMID37583270.md`\n**Primary pathway:** clinical spectrum / WWOX-DEE · drug response (spasms)\n**Model/species:** human\n**Genotype/model:** four children (Table 1 rows 37-40): frameshift + nonsense (x2, compound heterozygous as stated); in-frame exons 6-8 deletion + `c.517-3C>A` (compound heterozygous as stated; neither consequence measured); homozygous `c.790C>T p.Arg264Ter`. Phase not shown for the compound genotypes.\n**Transferability:** T1 for the clinical course of predicted-null genotypes; none for missense classes\n**clinical relevance:** MODERATE — the only multi-patient WWOX series in LEGEND with per-patient spasm treatment and outcome\n**Claim links:** 001 (vigabatrin observation, through `CC-20261003W3-A-VIGABATRIN-01`)\n**Role:** Spasm onset 2-4 months; microcephaly and central hypotonia in all four. Clinical spasm control (≥ 4 weeks, no electrographic criterion) with vigabatrin, nitrazepam or zonisamide in three at 6-12 months; the homozygous p.Arg264Ter child drug-refractory with a failed ketogenic diet at 30 months. 🔴 No denominator of all IESS; p.Trp398Ter is labelled 'missense' in the source; the deletion column says 'exons 5 to 8' for a c.517-c.1056 span; row 39's outcome reads 'persistent spasms' and 'seizure-free' together; none of the four rows is marked as previously published, but the children were tested from January 2018 and overlap with earlier reports is not excluded by the source.\n**LIT link:** [[literature_tracking_log_current#LIT-0440]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 142",
  "text": "\n## PAPER 143\n**Short title:** Sukkar 2022 Cureus — homozygous WWOX c.406A>G (p.Ile136Val) in a child WITHOUT seizures; attribution unproven\n**Full title:** Novel Mutation With Literature Review: WW Domain-Containing Oxidoreductase (WWOX) Gene\n**Authors:** Sukkar G, Alzahrani RM, Altirkistani BA, Al Lohaibi RS\n**Year:** 2022\n**Source type:** primary research — single case report with a literature table\n**Journal/source:** *Cureus* 2022;14(5):e25003\n**Identifier:** PMID 35712340 / PMCID PMC9193507 / DOI 10.7759/cureus.25003\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-A-REGISTRY-01`; promotes [[paper_registry_current#CORPUS-STUB-141]] (kept as history). Provisional number.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-35712340-01` (earlier: `FTR-20260921-35712340-01`, partial); manifest `deepdive_manifests/PMID35712340.json`; dossier `research/fulltext_dossiers/PMID35712340.md`\n**Primary pathway:** clinical spectrum — boundary case\n**Model/species:** human\n**Genotype/model:** homozygous missense `c.406A>G` (`p.Ile136Val` in the source's Table 3), four nucleotides upstream of the exon 4 donor; splice alteration predicted in silico only; DNA only\n**Transferability:** none — the genotype-phenotype attribution is not established\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** 🔴 **Do not count as a WOREE or SCAR12 case.** No seizures, normal MRI, walking and ten words at 21 months; raised CK, cholestasis and low lipids asserted, not shown, to be WWOX-related; an affected sibling with seizures was not genotyped. The literature table (Table 3) attributes `c.160G>T` to two unrelated reports and is not a count source.\n**LIT link:** [[literature_tracking_log_current#LIT-0160]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 143",
  "text": "\n## PAPER 144\n**Short title:** Serce Pehlevan 2026 J Paediatr Child Health — homozygous WWOX p.Leu239Arg with neonatal–infantile hypokinetic–rigid features; neurotransmitters not measured\n**Full title:** WWOX Mutation as a Rare Cause of Neonatal-Infantile Parkinsonism Mimicking a Neurotransmitter Disorder: A Case Report\n**Authors:** Serce Pehlevan O, Gider Yaman G, Gok A, Tekin Orgun L\n**Year:** 2026\n**Source type:** primary research — single case report\n**Journal/source:** *J Paediatr Child Health* 2026;62(7):1273-1277\n**Identifier:** PMID 42092735 / PMCID PMC13378201 / DOI 10.1111/jpc.70401\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-A-REGISTRY-01` (resolves `FT-106`). Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-42092735-01` (every section read; partial only because the cited prior report of the allele, PMID 30094525, is queued in the manifest); earlier `FTR-20260921-42092735-01`; manifest `deepdive_manifests/PMID42092735.json`; dossier `research/fulltext_dossiers/PMID42092735.md`\n**Primary pathway:** clinical spectrum / movement phenotype\n**Model/species:** human\n**Genotype/model:** homozygous missense `c.716T>G p.(Leu239Arg)`; carrier parents; DNA only\n**Transferability:** T3 for any allele-level movement phenotype (n = 1, confounded)\n**clinical relevance:** MODERATE — a presentation a clinician may take for a monoamine disorder\n**Claim links:** 001 (vigabatrin observation, through `CC-20261003W3-A-VIGABATRIN-01`)\n**Role:** Hypokinetic-rigid features with hypomimia from the neonatal period, persisting at 4 months. 🔴 CSF neurotransmitters were never measured and no dopaminergic drug was tried, so 'mimicking a neurotransmitter disorder' is a clinical working diagnosis, not a tested one; perinatal confounders (resuscitation, a thalamic diffusion focus) are present. Spasms continued on vigabatrin + phenobarbital and stopped on valproate + clobazam (one month seizure-free at 4 months). Its cited prior report of the allele is Serin 2018 (PMID 30094525), not [[paper_registry_current#PAPER 013]] from the same university, which it does not cite; identity with that cohort's case 49 is not excluded — do not sum carriers (see `CC-20261003W3-A-L239R-01`).\n**LIT link:** [[literature_tracking_log_current#LIT-0441]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-141",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — upgraded to [[paper_registry_current#PAPER 143]] by `CC-20261003W3-A-REGISTRY-01` (receipt `FTR-20261003-35712340-01`); this placeholder is kept as history"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-141",
  "old": "**Status:** not_processed",
  "new": "**Status:** promoted — see [[paper_registry_current#PAPER 143]]"
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` c740c6e after applying the three wave-2 registry candidates' LIT ops in A, C, B order: exit 0, 6 op(s), keys ['LIT-0439', 'LIT-0440', 'LIT-0160', 'LIT-0013', 'LIT-0343', 'LIT-0298'])

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0439",
  "text": "\n## LIT-0440\n**Short title:** Nagarajan 2023 Epilepsia Open — genetic IESS in 124 children; four biallelic WWOX\n**Authors:** Nagarajan B et al.; Sahu JK\n**Year:** 2023\n**Source type:** primary research — multicentre cross-sectional cohort\n**Journal/source:** *Epilepsia Open* 2023;8:1383-1404\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 37583270 / DOI 10.1002/epi4.12811 / PMC10690684\n**Date discovered:** before 2026-07-22 (cited in the discovery ledger, DL-MECH-060, with no identity record)\n**Date processed:** 2026-10-03 (`FTR-20261003-37583270-01`)\n**Discovery source:** Orchestrator selection record of intake wave 3 2026-10-03\n**Status:** processed\n**Status note:** `complete_fulltext_read`; record created by `CC-20261003W3-A-REGISTRY-01`\n**Primary pathway:** clinical spectrum / WWOX-DEE · drug response (spasms)\n**Transferability:** T1 for predicted-null clinical course\n**clinical relevance:** MODERATE\n**Claim links:** 001 (through `CC-20261003W3-A-VIGABATRIN-01`)\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w3_A.md` · `CC-20261003W3-A-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID37583270.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0440",
  "text": "\n## LIT-0441\n**Short title:** Serce Pehlevan 2026 J Paediatr Child Health — homozygous WWOX p.Leu239Arg, neonatal–infantile hypokinetic–rigid features\n**Authors:** Serce Pehlevan O, Gider Yaman G, Gok A, Tekin Orgun L\n**Year:** 2026\n**Source type:** primary research — single case report\n**Journal/source:** *J Paediatr Child Health* 2026;62(7):1273-1277\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 42092735 / DOI 10.1111/jpc.70401 / PMC13378201\n**Date discovered:** 2026-09-21 (full-text queue `FT-106`)\n**Date processed:** 2026-10-03 (`FTR-20261003-42092735-01`)\n**Discovery source:** next-node scouting 2026-09-21; selected again by intake wave 3 2026-10-03\n**Status:** processed\n**Status note:** `partial_fulltext_read` (article read in full; cited prior report of the allele queued); record created by `CC-20261003W3-A-REGISTRY-01`\n**Primary pathway:** clinical spectrum / movement phenotype\n**Transferability:** T3 for any allele-level movement phenotype\n**clinical relevance:** MODERATE\n**Claim links:** 001 (through `CC-20261003W3-A-VIGABATRIN-01`)\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w3_A.md` · `CC-20261003W3-A-REGISTRY-01` · `CC-20261003W3-A-L239R-01`\n**Next action:** read Serin 2018 (PMID 30094525), the cited prior report of the allele, in full\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID42092735.json`\n"
 },
 {
  "op": "replace-within",
  "id": "LIT-0160",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none — processed 2026-10-03 (`FTR-20261003-35712340-01`, `complete_fulltext_read`) and promoted to [[paper_registry_current#PAPER 143]] by `CC-20261003W3-A-REGISTRY-01`; Sukkar G et al. 2022, *Cureus* 14(5):e25003; a non-DEE homozygous missense with unproven attribution; the placeholder fields above are kept as history"
 },
 {
  "op": "replace-within",
  "id": "LIT-0013",
  "old": "**Flags:** low-yield flag",
  "new": "**Flags:** low-yield flag\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-41153369-01` (tables read for the first time; earlier `FTR-20260921-41153369-01`, partial); manifest `deepdive_manifests/PMID41153369.json`; see `CC-20261003W3-A-L239R-01`"
 },
 {
  "op": "replace-within",
  "id": "LIT-0343",
  "old": "**Next action:** full-text retrieval; depth pass if model-shifting",
  "new": "**Next action:** none — promoted earlier to [[paper_registry_current#PAPER 049]]; first receipted full-text read 2026-10-03 (`FTR-20261003-27495153-01`, `complete_fulltext_read`)"
 },
 {
  "op": "replace-within",
  "id": "LIT-0298",
  "old": "**Next action:** full-text retrieval + deep-dive in next session",
  "new": "**Next action:** none — promoted earlier to [[paper_registry_current#PAPER 046]]; full re-read 2026-10-03 (`FTR-20261003-38161429-01`, every section read; partial only for the open multihop queue); see `CC-20261003W3-A-BATTAGLIA-01`"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the four WWOX children's response is clinical only | the treatment response in this study was defined only clinically and it did not include electrographic resolution in the definition | PMID 37583270, Discussion para 3; files/fulltext/PMID37583270_Nagarajan2023_PMC.xml)
(a stop codon allele is labelled missense in the variation-type column | 37 WWOX (ENST00000566780.6) Exons 6 and 9 Chromosome 16 Deletion and missense | PMID 37583270, Table 1 row 37; files/fulltext/PMID37583270_Nagarajan2023_PMC.xml)
(the child had no seizure disorder | our patient presented with a global developmental delay and no early seizure disorder despite a family history of seizures and cerebral palsy in his brother and cousin, respectively | PMID 35712340, Discussion para 1; files/fulltext/PMID35712340_Sukkar2022_PMC.xml)
(the splice effect of c.406A>G is predicted only | The in silico predicted that the position of the identified variant might lead to significant alterations in mRNA splicing owing to an altered splice site. | PMID 35712340, Case presentation, WES paragraph; files/fulltext/PMID35712340_Sukkar2022_PMC.xml)
(CSF neurotransmitters were not measured | Cerebrospinal fluid (CSF) neurotransmitter analysis was not performed. | PMID 42092735, Case Presentation para 4; files/fulltext/PMID42092735_SercePehlevan2026_PMC.xml)
