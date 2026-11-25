# src_10 (card F03_bumetanide_chloride_gradient, /p4_card/novelty_for_woree)

## Verbatim sentence (marked word: "the one" in "the one human knockout deposit")
New: (1) the transcript-level ratio in the one human knockout deposit does not point to a depolarising gradient (descriptive, confounded);

## Source pointers
- Card packet: disease-models/wwox/research/drug_repurposing/cards/F03_bumetanide_chloride_gradient.packet.json, p4_card.novelty_for_woree; the ratio is DA-W2-020 (source "GSE156243 (PMID 34268881 deposit); descriptive panel by scientist-c, w2_therapeutic_it2_20261027/README.md"; locator w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv).
- Tables and censuses held in the repository: w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv; wwox_data_census_it6_20261029.md (IT6 P3, accession checks of 2026-10-29); ebi_access_request_E-MTAB-14792_draft.md (checks of 2026-10-25); wwox_systems_comparison_it5_20261029.md; chloride_gradient_sci42_20261110/README.md.
- The set named by "the one human knockout deposit": public or announced transcript deposits (GEO, ArrayExpress/BioStudies) whose WWOX perturbation is a human knockout, as listed in the IT6 census (GEO query of 2026-10-29: `WWOX[All Fields] AND gse[Entry Type]` = 39 series, titles screened; ArrayExpress/BioStudies `biostudies-arrayexpress` WWOX = 27 entries).

## Packet assertions DA-W2-020 and DA-W2-021 (verbatim JSON)
```json
[
 {
  "id": "DA-W2-020",
  "target_id": "SLC12A2 (NKCC1) over SLC12A5 (KCC2) transcript ratio",
  "endpoint": "ratio per library",
  "direction": "UNKNOWN",
  "source": "GSE156243 (PMID 34268881 deposit); descriptive panel by scientist-c, disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/README.md",
  "locator": "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv",
  "epistemic_status": "INFERENZA",
  "reading_depth": "queried_not_full_read",
  "context": {
   "disease_id": "WWOX-deficient human cerebral organoid model (engineered knockout; NOT a patient allele; no amyloid)",
   "genotype": "WWOX knockout versus wild type (4 versus 2 libraries, one laboratory)",
   "species": "human",
   "cell_type": "cerebral organoid, bulk RNA",
   "developmental_stage": "organoid, culture week 15"
  },
  "measured_result_note": "Ratio 0.24, 0.29, 0.13, 0.14 in the four knockouts and 0.29, 0.30 in the two wild types: not higher in knockouts, so no transcript-level hint of a more depolarising chloride gradient; SLC12A2 is flat and SLC12A5 is higher in two knockouts. Composition-confounded (GAD1 about ten-fold different), transcript not function, direction left UNKNOWN.",
  "evidence_scope": "COMPUTATIONAL_RESULT"
 },
 {
  "id": "DA-W2-021",
  "target_id": "GABRB2 and GABRB3 transcripts",
  "endpoint": "CPM, knockout minus wild type",
  "direction": "DECREASE",
  "source": "GSE156243 descriptive panel by scientist-c (the marker pattern behind DL-MECH-035)",
  "locator": "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv",
  "epistemic_status": "INFERENZA",
  "reading_depth": "queried_not_full_read",
  "context": {
   "disease_id": "WWOX-deficient human cerebral organoid model (engineered knockout; NOT a patient allele; no amyloid)",
   "genotype": "WWOX knockout versus wild type (4 versus 2 libraries, one laboratory)",
   "species": "human",
   "cell_type": "cerebral organoid, bulk RNA",
   "developmental_stage": "organoid, culture week 15"
  },
  "measured_result_note": "GABRB2 about a quarter and GABRB3 about half of wild type; the same libraries carry more GABAergic-lineage transcripts. Reduced receptor transcript is not a chloride gradient.",
  "evidence_scope": "COMPUTATIONAL_RESULT"
 }
]
```

## Card not_known entry on this deposit (verbatim)
[
 "Whether any organoid transcript difference or null on this card (deposit GSE156243) is independent of the CRISPR clone and of the batch: the sequenced knockout organoids are four of ONE clone (1B, from edit-spanning reads, ADV-244, SCI, 2026-11-25), the other clone (A2) was not sequenced, the comparator is two organoids of the parental line (the authors removed two of four wild-type libraries, one for failed quality control and one for not clustering), and the organoids appear to come from one batch (the authors' Methods: organoids from the same batch were used for all analyses unless stated otherwise; their reply to reviewers speaks of the batch of the RNA-seq; not stated as a measured fact for these six libraries), so a difference here is not shown to be a property of the knockout rather than of the clone or the batch. [IT 2026-11-25, ADV-244]"
]

## organoid_panel_cpm.tsv (complete file; columns: gene, four knockout libraries cko1-4, two wild-type libraries cwt1-2, minimum raw count across libraries; the ratio row is as stored; human, bulk RNA, cerebral organoid, culture week 15 per the packet)
| gene | cko1 | cko2 | cko3 | cko4 | cwt1 | cwt2 | raw_min_across_libraries |
|---|---|---|---|---|---|---|---|
| WWOX | 14.12 | 11.86 | 16.54 | 12.28 | 9.64 | 10.07 | 302 |
| SLC12A2 | 5.02 | 5.55 | 5.49 | 5.53 | 5.82 | 4.65 | 139.296 |
| SLC12A5 | 20.97 | 19.22 | 41.33 | 39.03 | 19.97 | 15.64 | 469 |
| GRIN1 | 33.16 | 37.88 | 43.71 | 46.45 | 40.58 | 48.83 | 1284 |
| GRIN2A | 2.56 | 2.07 | 5.08 | 2.40 | 1.07 | 0.67 | 20 |
| GRIN2B | 27.53 | 45.46 | 27.43 | 20.84 | 26.63 | 20.25 | 607 |
| GRIN2C | 2.14 | 1.41 | 6.33 | 2.34 | 2.25 | 1.07 | 32 |
| GRIN2D | 72.54 | 71.90 | 114.43 | 104.51 | 98.78 | 88.63 | 2657 |
| GRIA1 | 149.75 | 162.00 | 103.28 | 98.02 | 90.40 | 104.81 | 3142 |
| GRIA2 | 12.55 | 19.73 | 13.01 | 12.45 | 11.46 | 16.18 | 426 |
| GRIA3 | 18.98 | 26.44 | 13.43 | 17.28 | 26.84 | 20.95 | 513.001 |
| GRIA4 | 0.85 | 0.75 | 3.53 | 1.87 | 0.78 | 0.43 | 13 |
| GABRB2 | 2.43 | 4.01 | 1.13 | 3.25 | 11.33 | 9.01 | 43 |
| GABRB3 | 16.83 | 21.95 | 16.85 | 18.41 | 47.99 | 27.37 | 629.703 |
| GAD1 | 8.93 | 10.91 | 37.93 | 26.98 | 3.46 | 0.20 | 6 |
| OLIG1 | 0.10 | 0.10 | 0.86 | 0.73 | 0.03 | 0.07 | 1 |
| OLIG2 | 0.65 | 0.63 | 1.83 | 1.64 | 0.81 | 1.10 | 25 |
| SOX10 | 0.18 | 0.05 | 0.10 | 0.06 | 0.11 | 0.07 | 2 |
| PDGFRA | 4.70 | 1.34 | 2.25 | 2.16 | 0.35 | 0.25 | 7.35 |
| MBP | 3.05 | 1.12 | 3.80 | 2.25 | 1.45 | 1.40 | 42 |
| PLP1 | 68.79 | 74.50 | 198.16 | 87.47 | 65.47 | 48.73 | 1461 |
| CHRM1 | 16.86 | 20.14 | 8.69 | 14.30 | 22.04 | 24.88 | 332 |
| CHRM3 | 1.41 | 0.74 | 2.60 | 1.49 | 0.91 | 0.38 | 11.505 |
| HSPA1A | 43.88 | 40.64 | 62.66 | 51.35 | 43.26 | 64.98 | 1611.84 |
| HSPA8 | 1455.24 | 1338.48 | 1446.28 | 1353.50 | 1286.12 | 1393.56 | 41777.8 |
| SLC12A2_over_SLC12A5 | 0.24 | 0.29 | 0.13 | 0.14 | 0.29 | 0.30 |

## IT6 census (wwox_data_census_it6_20261029.md), candidate-table header and the rows that concern WWOX perturbation records (verbatim; the other rows of the table are fly, non-neural or non-transcript records and were not copied)
| # | Record | Cat | Sys | Perturbation | Meas | Controls | Unit (n) | Avail | Size |
| 1 | MTBLS12344 (MetaboLights), Brain Commun 2026 (DOI 10.1093/braincomms/fcag385) | c | fly head, pan-neuronal | Wwox RNAi x Abeta42 (2x2) | D for pools of pyruvate/TCA/lactate if tested (untested in public text) | RNAi control line, LacZ | pool of 10 heads (N=5) | **NOT public** (folder 404; absent from public listing; API 401) | n/a |
| 2 | E-MTAB-14948 and E-MTAB-14949 (ArrayExpress), same paper | b,c,d | fly head, pan-neuronal | RNAi knockdown (14948); CRISPRa overexpression (14949); each with and without Abeta42 | P (mRNA) | RNAi control; control gRNA | pool of 10 heads; 4 per cell (16 samples; 15 in 14949, one missing) | public: per-sample featureCounts + SDRF | about 4.5 MB x 31 = about 135 MB |
| 3 | GSE158681 (hippocampus; GEO status "Public on Oct 01 2026"), GSE158682 (cortex), GSE158684 (hippocampal nuclei, snRNA), parent GSE158685 | e,d | mouse brain, P17 | null; neuron-targeted deletion ("S"); neural stem/progenitor deletion ("N") | P (mRNA) | Cre-negative littermate controls | mouse; hippocampus null 2 v WT 3, S 3 v 2, N 2 v 2; cortex S 3 v 4 | public: TPM tables (transcript-level, Salmon); raw in SRA | 4.6 MB + 2.5 MB |
| 4 | GSE215425, P47T knock-in (paper PMID 36828035) | f,e | mouse brain regions | partial-loss missense knock-in, WW1 domain | P (mRNA) | WT littermates | mouse; 5 v 5 per region; 37 samples | public; raw in SRA | not measured (37 samples) |
| 5 | E-MTAB-14792 (scRNA, Brain 2026 organoids, DOI 10.1093/brain/awag239) | e,d | human organoid | WWOX loss; **[IT7] the same paper's AAV9-WWOX add-back at week 10 (its Fig 6C-E); preprint v2 methods list five libraries, one per condition: WT, WWOX-KO, SCAR12, WOREE, WOREE-WWOX** | P (mRNA) | control organoids | one library per condition; cells are not independent units; **the add-back contrast is against non-treated WOREE, none of the 5 libraries is AAV9-EGFP-treated (no vector control)** | **403 not accessible (re-run 2026-10-29)**; whether the add-back library is inside is UNVERIFIED; release request drafted, not sent | n/a |
| 6 | GSE229210 (CAGE; paper PMID 37781246) | c,d | four human glioma lines | WWOX overexpression into low-WWOX lines | P (mRNA) | empty-vector virus | 3 cultures x 4 lines x 2 arms (24) | public | not measured |

## IT6 census search record (verbatim)
NCBI GEO DataSets (`db=gds`): `WWOX[All Fields] AND gse[Entry Type]`: 39 series (Wwox and WWOX give the same list); with knockout/knockdown/mutant/siRNA/shRNA: 16.
All 39 titles screened; WWOX-perturbation series in a neural system: GSE126075, GSE156243, GSE158681/2/4/5, GSE215425 (rows reused or 3 and 4); others are cancer, SNP arrays or unrelated.

## IT6 census paragraph on E-MTAB-14792 (verbatim)
**5. E-MTAB-14792.** The sole single-cell human neural record found; not accessible. [IT7] It is the record of the paper that also holds the AAV9-WWOX add-back (one library of 5,151 cells against 7,687 for WOREE, preprint v2 methods). The release question is in

## ebi_access_request_E-MTAB-14792_draft.md, section "What is established" (verbatim; draft, nothing was sent)
## What is established (each point measured on 2026-10-25, none inferred)
- The accession is **E-MTAB-14792**, named identically in the published article's Data availability statement and in the bioRxiv
  v2 preprint: "The single-cell RNA sequencing data have been uploaded to ArrayExpress with accession number: E-MTAB-14792."
- The article is Steinberg DJ, Zonca A, Abdellatif D, et al., "Disrupted WWOX-MYC interplay impairs neurogenesis in human brain
  organoids", *Brain*, published online 2026-07-03, DOI 10.1093/brain/awag239 (PMID 42397075).
- The BioStudies API distinguishes the cases: a nonexistent accession returns **404 "Study not found"**; **E-MTAB-14792 returns
  403 "Study not accessible"**. So the record **exists** and is **not publicly accessible**. Neighbouring accessions E-MTAB-14791, -14793,
  -14794 and -14795 resolve (200); E-MTAB-14800 returns the same 403.
- The article has been public for nearly four months, so a release held only until publication would already have lapsed.
- **Not established:** whether the study is awaiting a release step, was released only to the submitter, or was suspended. The API uses
  one message for all of them.

## wwox_systems_comparison_it5_20261029.md, section 0 (verbatim lines on GSE126075 and GSE156243)
- P6 has ONE library per arm (library totals recovered from the TSS table: control hNPC 51.0M tags, silenced 14.3M): every statement about the CAGE systems is descriptive. The organoid has 4 knockout vs 2 wild-type libraries (minimum single-gene
- What differs and stays different: knockout (exon deletion; WWOX mRNA not lower, +0.42, so the transcript is not a knockout check there) versus knockdown of unquantified depth   (hNPC: WWOX not lower in the CAGE tags; neurons about 3 to 4 fold lower on 21 versus 83 tags); 3D mixed-cell organoid, week 15, versus 2D clonal H9-derived progenitors   and day-14 neurons; RNA-seq counts versus CAGE promoter sums with 9 to 61 percent of tags in the gene table; control possibly native in GSE126075; different laboratories and lines.

## chloride_gradient_sci42_20261110/README.md, row "Public data" (verbatim)
| Public data | no Wwox electrophysiology deposit found: GEO (transcript series only: GSE158681, GSE158682, GSE158684, GSE158685 neuronal deletion; GSE215425 P47T mutant), DANDI 0 hits, BioStudies no electrophysiology (first page), Zenodo/Figshare/Dryad/OSF nothing relevant (verifier); absence in a bounded set of repositories, not shown absent |
