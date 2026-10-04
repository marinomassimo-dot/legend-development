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
  (Q230P missense in the WW2/linker region; splice-site alleles). `p.(Thr12Arg)` is an N-terminal exon-1
  missense, upstream of WW1; the SV is an exon-5 inversion. **No transfer.**
- References: 74; **zero** WWOX gene-direct references (earned null for multihop).
