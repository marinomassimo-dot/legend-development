# Intake wave 8 2026-10-04 — Scientist A reading note

context_policy: SOURCE_FIRST

- **Actor:** scientist-a (ACTOR_ID `scientist`), dispatched by the Orchestrator; branch `task/sci-A-20261004w8`.
- **Group A question:** what does each source add to, or limit in, the claim that a named WWOX allele's
  consequence has been *measured* (RNA, protein, dose model) rather than predicted, and which allele class
  does each measurement cover? No transfer across alleles (P47T ≠ Q230P ≠ G372R ≠ A141T ≠ P252A; an
  acceptor allele is not a donor allele; a structural allele is not a splice allele).
- **Public edition:** patients are described at class level only (allele class × zygosity × phenotype band).
  Parent-of-origin, geography and case identifiers are not carried, even where the source prints them.
- Nothing here is medical advice.

## Identity and dedup (measured 2026-10-04, before any reading)

| PMID | First author, year | PMCID | `fulltext_receipts.py status` | `registry_records.py get --pmid` | PubMed article types |
|---|---|---|---|---|---|
| 36926521 | Colin 2023 | PMC10011630 | `[]` (exit 1) | no record | Journal Article |
| 37946251 | Pagnamenta 2023 | PMC10636885 | `[]` (exit 1) | no record | Journal Article; Research Support, Non-U.S. Gov't |
| 40858643 | Hamanaka 2025 | PMC12381280 | `[]` (exit 1) | no record | Journal Article |
| 41835067 | Yigit 2026 | PMC12979860 | `[]` (exit 1) | no record | Journal Article |
| 41477840 | Stamouli 2026 | PMC12757047 | `[]` (exit 1) | no record | Journal Article |
| 41254692 | Qin 2025 | PMC12625014 | `[]` (exit 1) | `CORPUS-STUB-101`, status `not_processed` | Journal Article; Research Support, Non-U.S. Gov't |

No retraction, expression of concern or correction is listed for any of the six (PubMed metadata,
2026-10-04). `dependency_integrity.py screen --manifest-block`: SCREENED_CLEAN for all six.

Acquisition: the Europe PMC REST `fullTextXML` endpoint was re-fetched for each PMCID on 2026-10-04; each
response is byte-identical (SHA-256) to the copy the Orchestrator had staged, and each was persisted as
`files/fulltext/PMID<pmid>_<Author><Year>_PMC.xml`.

## A1 · PMID 36926521 (Colin 2023) — first pass (written before any registry comparison)

- 15-individual multi-omics diagnostic series; one individual carries WWOX (DEE28, autosomal recessive).
- Genotype class: **missense in exon 1 (`p.(Thr12Arg)`) *in trans* with a complex structural variant** (two
  intronic deletions in introns 4 and 5 flanking an **inversion of exon 5**), phase from parental segregation.
- Phenotype band: female child, seizure onset in early infancy progressing to epileptic encephalopathy with
  hypsarrhythmia, limb spasticity, ataxia, dysmetria, movement disorder, progressive cerebral atrophy
  (supplementary clinical note).
- **Measured, RNA (blood):** RT-PCR across exons 4–6 shows a 186 bp product beside the expected 293 bp in the
  proband and in the heterozygous SV carrier, not in the missense carrier; amplicon sequencing of the 186 bp
  product = exon 5 skipping. This measures the **SV allele's** consequence, not the missense allele's.
- **Panel E read (Supplementary Figure S5E, Image5.TIFF):** in the proband lane the 293 bp band is the strong
  band and the 186 bp band is faint; nothing is quantified. So in blood, normally spliced exon 4–5–6 transcript
  is abundant in the proband (it can come from the missense allele, and the panel cannot tell how much comes
  from the SV allele).
- **Measured, protein (fibroblast):** one western blot lane pair, proband vs one healthy control, WWOX 46 kDa
  band strongly reduced in the proband — a faint band remains visible in panel G; no quantification, no
  replicate, no second control, no parental lines. The authors call it "WWOX loss" (text) and "lack of
  expression" (legend). The blot measures the **genotype** (missense + SV together); it cannot attribute the
  loss to either allele.
- **Predicted only:** the missense allele — absent from gnomAD, "in silico prediction scores in favor of its
  pathogenicity". No RNA, protein, stability, localisation or binding assay of `p.(Thr12Arg)` alone.
- **Not measured:** frame of the exon-5-skipped transcript (stated nowhere; exon 5 = 293 − 186 = 107 nt, so a
  frameshift is an INFERENZA from the printed sizes, not a reported result); NMD (no translation-inhibitor
  arm); the fraction of SV-allele transcript that is skipped; allele-specific expression of the missense
  allele; protein in a neural matrix.
- **Methods inconsistencies (supplementary methods):** the cell-culture paragraph names fibroblasts from a
  healthy donor and individual 13, not individual 11; the western paragraph says vinculin was the loading
  control while panel G shows actin. Neither changes the qualitative reading, both weaken the blot as a
  quantified dose.
- Class transfer: neither allele is in the class of any reference-genotype allele named in the brief
  (Q230P missense; splice-site alleles). `p.(Thr12Arg)` is an exon-1 missense near the N-terminus; the SV is
  an exon-5 inversion with flanking intronic deletions. **No transfer.**
- References: 74; **zero** WWOX gene-direct references (earned null for multihop).

## A2 · PMID 37946251 (Pagnamenta 2023) — first pass (written before any registry comparison)

- 122-family clinical WGS cohort (300 genomes). WWOX is one of seven structural-variant cases (Table 1, a JPEG
  table; read as an image and cell-wise from Additional file 3 Table S7).
- Genotype class: **in-frame 219 kb deletion of exons 6–8** (`chr16:g.78291861_78511176del`, GRCh38) *in trans*
  with **`c.705dup p.(His236fs)`** (exon 7). The frameshift lies inside the deleted interval, and Table S7 calls it
  `hom` — a hemizygous call over the deletion, which is what places the two on different chromosomes; Table S7
  lists one sequenced sample for the case.
- Phenotype band: "Severe Epileptic Encephalopathy" only; no narrative.
- **Measured:** DNA only — the deletion was validated by "PCR and Sanger sequencing" (Table 1).
- **Predicted / annotated only:** "in-frame", "loss of 180 amino acids including the mitochondrial targeting
  sequence" — derived from coordinates; ACMG codes `PVS1, PM2, PM3` applied to both alleles, including PVS1 to an
  in-frame deletion. **No RNA, no protein, no patient cells.**
- **Patient counted once — the paper says so itself:** Table 1 "Reference to Case": "Reported as Patient 11
  (Table S1) in case series in Piard et al [97]" (ref 97 = Piard 2019, PMID 30356099). The held Piard 2019
  Supplementary Table 1 (`41436_2018_339_MOESM1_ESM.xlsx`, read cell-wise) gives Patient 11 as
  `c.[517_1056del];[705dupG]`, `p.[His173_Met352del];[His236Alafs*34]`, under a row header that reads "Mutation at
  the protein level (not based on experimental evidence)". **Same patient, same genotype: this is not an
  independent observation.**
- The selection note's premise "a structural allele class the registry does not hold" is therefore not a new
  allele class for LEGEND's corpus: the exon 6–8 in-frame deletion appears in at least four Piard 2019 patients
  (three deletions, one duplication of `c.517_1056`). Whether the *registry* names it is a separate question
  (theme queries `517_1056`, `His173_Met352`, `705dup`: no record).
- "Missed by prior array standard of care" is not what the WWOX row says: its reason is "Gene not incorporated
  into validated panel test at the time of referral. Deletion should be detectable by array."
- Class transfer: an in-frame multi-exon deletion and a frameshift; neither is the reference genotype's class.
  **No transfer.**

## A3 · PMID 40858643 (Hamanaka 2025) — first pass (written before any registry comparison)

- 260 exome-negative ID/DD families, short-read genome sequencing; WWOX is one row of Table 2 and one row in each
  of Supplementary Data 1 (small variants) and 2 (SVs). The main text never discusses it.
- Genotype class: **`c.517-1G>A`** (canonical acceptor of intron 5, i.e. the exon-6 acceptor; genome
  `chr16:78386859G>A`) **in trans with a single-exon CNV, `Chr16:g.78140467_78313935delinsCA`, "WWOX exon 5"**
  (~173 kb). Phase from trio inheritance (one allele from each parent; this edition does not carry which).
- Both alleles classified Pathogenic: `PVS1, PM2, PM3, PP3` (splice) and `PVS1, PM2, PM3` (CNV).
- **Measured:** DNA only (GS; the exon-5 deletion is supported by five SV callers). **No RNA** for WWOX — the
  paper's RNA-seq was run only on lymphoblastoid lines of selected non-WWOX cases. **No protein.**
- **Predicted:** the splice consequence of `c.517-1G>A` (CADD 25.1; PVS1 by rule). Neither exon 6 skipping nor
  cryptic-acceptor use is shown; the exon-5 deletion's frame consequence is not stated.
- Phenotype band (HPO, Supplementary Data 1/2): epilepsy with tonic seizures, exaggerated startle, rigidity,
  hypokinesia, joint contractures, feeding difficulties and recurrent aspiration pneumonia, intellectual
  disability, cerebral white-matter hyperintensity and atrophy, abnormal thalamic signal and size, cerebellar
  dysplasia. Clinical category "Unclassified DD/ID syndrome – Epilepsy".
- Selection-note premises tested: the "reverse-phenotyping flag ('Unclassified (Epilepsy)' → solved)" is **not
  in the paper** — "Unclassified (Epilepsy)" is only the referral category column; no reverse phenotyping is
  described. The splice allele is ES-detectable ("Yes"), the CNV is not.
- Same-site note: `c.517-1G>A` alters the same intron-5 acceptor dinucleotide as `c.517-2A>G` (the allele of the
  patient-derived organoid line of PMID 34268881). A same-site allele is still a different allele: nothing
  measured for one is transferred to the other here.
- Class transfer: an intron-5 acceptor allele and a single-exon deletion. Not the reference genotype's class (the
  reference splice allele named in LEGEND's ASO skill is an intron-8 acceptor). **No transfer.**
- References: 36; no WWOX gene-direct reference.

## A4 · PMID 41835067 (Yigit 2026) — first pass (written before any registry or candidate comparison)

- 66 exome/genome-unsolved children with a preliminary clinical diagnosis of cerebral palsy (CP), re-analysed
  with deep phenotyping; 24 of 66 received a P/LP diagnosis. WWOX is one row of Table 2 (case CP_P14.1) and is
  named once in the Discussion as an example of the epileptic-encephalopathy subgroup.
- Genotype class: **homozygous missense `NM_016373.4:c.716T>G p.(Leu239Arg)`** — not compound heterozygous; the
  selection note's "zygosity and the second allele are not visible in the retrieved body" is wrong: Table 2 prints
  "Hom" with segregation from both parents (parents' origin columns are not carried here).
- ACMG: Pathogenic, `PP3, PM3, PM2, PP5` — **PP5 means it is classified partly on a prior reputable report**,
  i.e. the allele is not new to the literature. gnomAD v4 frequency cell: "–".
- Disorder column lists both DEE28 (MIM 616211) and SCAR12 (MIM 614322); no adjudication between them.
- Phenotype band (Table 1): female young child (last examination in the second year of life), consanguineous
  parents, global developmental delay, hypotonia, seizures, spasticity, scoliosis, short neck, hypertelorism.
  CP risk factor recorded: intrauterine growth retardation.
- **Measured:** DNA and segregation only. **Predicted:** consequence of `p.(Leu239Arg)` (PP3). No RNA, protein,
  enzymatic, localisation or patient-cell assay.
- Referral path: a CP-labelled stream. The Discussion endorses keeping the CP diagnosis when the phenotype fulfils
  the consensus definition, rather than reclassifying as a mimic.
- Class transfer: a homozygous SDR-region missense (residue 239) is not Q230P and is not a splice allele. **No
  transfer**, not even "missense ≈ missense".
- References: 49; no WWOX gene-direct reference.
- **After first pass — L239R counting (compared against `CC-20261003W3-A-L239R-01`, `CC-20261003W5-B-PATIENT-OVERLAP-01`
  and the registry records `PAPER 013`, `PAPER 145`):** this child (female, consanguineous, neonatal-onset
  seizures; onset only in Supplementary file 1) is not excluded from being `PAPER 013` case 50 (female, 11 months,
  EIDEE). INFERENZA, counted once. Read sources now hold 2–4 homozygous L239R children in 1–3 families, never
  summed as independent. The supplement's narrative adds neonatal onset and inability to sit, which the main
  tables do not carry.

## A5 · PMID 41477840 (Stamouli 2026) — first pass (written before any registry comparison)

- Off-axis for alleles: a human glial-progenitor (hGPC, stem-cell-derived) to parvalbumin (PV) interneuron
  reprogramming study in 3D spheroids (lentiviral transcription-factor cocktail), read out by snRNA-seq over days
  0–21, RNA velocity/latent time and diffusion pseudotime. **No WWOX perturbation, no WWOX protein, no allele.**
- **Measured:** WWOX transcript in snRNA-seq. (i) Table S5: WWOX is a top-25 DEG of neuronal cluster 16 (log fold
  change 1.84, adjusted p 5.71E-48). (ii) Fig. 6F heatmap (PV trajectory, latent time): WWOX expression is present
  in the early glial segment and higher in the later neuronal and PV segments. (iii) **Fig. 6H panel, read:**
  average WWOX expression ≈1.3 (day 1) → ≈1.6 (day 3) → ≈2.15 (day 7) → ≈2.5 (day 13) → ≈1.2 (day 21): roughly a
  two-fold rise to a day-13 peak, **then back to the day-1 level by day 21** (approximate values read from the
  plot; units as plotted; the cells averaged are not stated in the legend).
- The paper describes the same gene three ways: "gradually up-regulated" (Results, 6F), "robust up-regulation …
  as early as day 7" (Results, 6H) and "transient up-regulation of neuronal migration genes such as PLEKHG1 and
  WWOX" (Discussion). The panel supports "transient" with a day-13 peak; "robust … as early as day 7" is a ≈1.7×
  change on the plot.
- The "neuronal migration" label is the heatmap's grouping, and the Discussion's reason is speculative
  ("possibly reflecting a more accessible chromatin around these genes and the migratory nature of hGPCs").
- WWOX is **expressed in the starting human glial progenitors** (day-1 average ≈1.3, and the glial segment of 6F
  is not blank). That is a transcript observation in an artificial in-vitro glial progenitor population, not a
  statement about oligodendrocyte-lineage function.
- Discussion citations about WWOX: "highly expressed in basket PV cells (71)", ablation reduces hippocampal PV
  interneurons (72), impairs differentiation and migration (73). Checked after the first pass against the held
  artefacts (see below).
- Selection-note premises tested: "a human, cell-type-resolved, time-resolved **dose curve**" overstates — it is
  an average-expression time course in a reprogramming culture, with no dose and no requirement test; "names
  migration, not metabolism" is a heatmap label plus a speculative sentence.
- Class transfer: no allele, no genotype. **Nothing transfers to any WWOX genotype**; reprogramming is not
  development (the authors' own limitations: no glutamatergic input, limited mature cells, RNA velocity applied
  to nuclei).
