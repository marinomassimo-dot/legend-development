# CC-20261004w8-B-BIOMARKER-01 — the three direct WWOX read-outs, their §13 class, and their measured ceilings

```yaml
context_policy: SOURCE_FIRST
actor: scientist (Group B, intake wave 8 2026-10-04)
branch: task/sci-B-20261004w8
change_class: MINOR
targets:
  - disease-models/wwox/registries/claim_registry_current.md
depends_on: CC-20261004w8-B-REGISTRY-01   # for the PAPER id this claim cites
```

> **Not medical advice.** Public edition: class level only.

## What this candidate adds, and why it is MINOR and not MAJOR

PMID 33129329 is, as far as this corpus goes, the only end-to-end **protocol for measuring WWOX**:
transcript, protein by immunoblot and protein in tissue, with controls, a scoring scheme and a
measured inter-rater statistic. Read as a pharmacodynamic specification rather than as oncology, it
settles what the existing direct read-outs can and cannot do.

**It narrows nothing.** `claim_registry_current` was searched for `biomarker` and for `biomarcatore`
across all 44 records: **zero matches**. There is no consolidated baseline claim about a WWOX
biomarker to narrow or reverse, so by §7 of the batch protocol this is an **addition**, class MINOR.
The candidate is written so that a future positive biomarker claim has to clear a stated bar rather
than a vague one.

## Op — claim_registry_current.md

**Op:** append one new record in the section where the registry's other method/measurement claims
sit. **No `old` text is replaced**, so no `old`/`new` pair is given; this is a pure append.

**Proposed record (provisional id — the integrator assigns the next free `CLAIM` number):**

> **Statement.** The three direct read-outs of WWOX that a published protocol actually demonstrates —
> transcript by relative comparative-Ct, protein by immunoblot densitometry, and protein in fixed
> tissue by immunohistochemistry — are **Tier 1 modalities** under `LEGEND_CORE` §13, and **none of
> them is a validated biomarker for any disease population**. In the one source that specifies all
> three end to end, no limit of detection, linear range, calibrator, sensitivity, specificity or
> cut-off is stated for any of them; the tissue read-out, the most clinically deployable, achieved
> **fair** inter-rater agreement only (weighted κ 0.264 for staining intensity and 0.273 for percent
> positivity, two blinded board-certified pathologists); and **WWOX enzymatic activity was not
> measured at all**.
>
> **Classification.** `DATO` for the measurement properties; the §13 tier assignment is a
> classification, not a finding.
>
> **Status.** `open` — this is a floor, not a ceiling: it states what the published protocol
> demonstrates, and a calibrated assay would supersede it.
>
> **Scope and transfer limit.** The source matrix is canine cutaneous mast cell tumour tissue and
> canine/murine mast cell lines. Nothing in it is a measurement of human CNS tissue, of any WWOX
> variant, of any zygosity, or of any body fluid. The immunohistochemistry antiserum was raised
> against human/murine residues 12–94 and applied across a species barrier on a stated homology
> argument (94.4% protein-level similarity overall, 96% across the epitope) — an argument about the
> epitope, not a validation. **The transfer that IS warranted is the negative one**: a protocol that
> could not exceed fair agreement with unlimited tissue and expert readers does not become more
> precise in a harder matrix.
>
> **What would change this claim.** A WWOX assay reporting a concentration against a recombinant
> calibrator, with a stated limit of detection and linear range, in any matrix obtainable from a
> living patient; or any published inter-rater agreement above κ 0.6 for WWOX immunohistochemistry.
>
> **What would falsify it.** A source showing sensitivity and specificity for a WWOX read-out in a
> disease population — which would move the modality from Tier 1 *class* to Tier 1 *validated*.
>
> **Paper link.** `[[paper_registry_current#PAPER 151]]` (provisional; see
> `CC-20261004w8-B-REGISTRY-01`).
>
> **Note.** Class-level record; no individual-level detail. Not medical advice.

## Consequential edit to the paper record

If this lands, `PAPER 151`'s `Claim links:` field changes from `none` to the id this record receives.
That is the only existing text this candidate touches, and it cannot be written as an `old`/`new`
pair until both numbers are assigned — the integrator makes the substitution when it renumbers.

## Why this matters for the restoration spec

A gene-restoration programme needs a pharmacodynamic read-out: something that changes when the
therapy works. This candidate records that **the measurement side of a WWOX restoration spec is the
unsolved half.** Group B's five delivery papers each supply numbers; the one measurement paper
supplies ceilings. Stating the ceiling is what stops a future reading from treating "WWOX
immunohistochemistry" as an available endpoint.

## Change class

**MINOR.** One appended record; one field substitution in a record that this wave is itself creating.

### LOCATOR TRIPLES FOR BLIND AUDIT

(The immunohistochemistry reagent is an antiserum raised against a human and murine epitope and applied to a different species on a stated homology argument rather than a validation | This antiserum detects endogenous and recombinant human and murine WWOX amino acid residues 12–94 containing both of the WW domains. Human and canine WWOX exhibit 94.4% similarity at the protein level and the region corresponding to WWOX amino acids 12–94 shares 96% sequence homology | files/fulltext/PMID33129329_Makii2020_PMC.xml, Methods, 'Tumor microarray construction and immunohistochemistry')

(The only negative control for the tissue read-out is a reagent control, not a genetic negative | Normal canine testes tissue served as a positive control. Negative controls consisted of irrelevant isotype matched antibody at matched dilutions. | files/fulltext/PMID33129329_Makii2020_PMC.xml, Methods, 'Tumor microarray construction and immunohistochemistry')

(The tissue read-out is an ordinal score assigned by eye rather than a measurement | Overall WWOX signal intensity of normal and malignant mast cells was subjectively scored from 0 to 3 (0 = none to weak, 1 = mild, 2 = moderate, 3 = strong) by two boarded veterinary pathologists | files/fulltext/PMID33129329_Makii2020_PMC.xml, Methods, 'Tumor microarray construction and immunohistochemistry')

(The authors measured the reliability of their own tissue read-out and report it as fair | There was fair interrater agreement for both staining intensity and percent of cells stained (K = 0.264 and 0.273, respectively). | files/fulltext/PMID33129329_Makii2020_PMC.xml, Results, 'Immunohistochemical expression of WWOX in primary canine MCT samples')

(The protein read-out is relative densitometry against a loading control, with no standard curve and no calibrator | Band intensities were calculated using ImageJ software (NIH, Bethesda, MD, USA) and relative intensity of WWOX was determined by dividing by β-actin. | files/fulltext/PMID33129329_Makii2020_PMC.xml, Methods, 'Immunoblotting')

(The transcript read-out is a relative comparative-Ct assay normalised to a ribosomal housekeeper, so it reports a fold change within a run and never a concentration | Canine WWOX and 18S were detected using Fast SYBR Green PCR master mix according to the manufacturer's instructions. Data normalization was performed relative to 18S internal control. | files/fulltext/PMID33129329_Makii2020_PMC.xml, Methods, 'RNA isolation, cDNA synthesis, and qRT- PCR')

(The study declares itself unpowered | This was a pilot study with the intent to characterize the expression of WWOX in primary canine MCTs and malignant cell lines, so no power calculation was made. | files/fulltext/PMID33129329_Makii2020_PMC.xml, Methods, 'Tumor microarray construction and immunohistochemistry')

(The transcript read-out does not separate cases from controls at the level of a single sample | [figure attestation — pixels cannot be quote-matched] Panel 1a, y-axis 'Relative Expression (2^-ΔΔCT)' 0.000–0.004 linear. Two cBMCMC bars at approximately 0.0018 (error bar reaching about 0.0031) and 0.0007. Roughly twenty Primary Canine MCT bars: two reach approximately 0.0026 and approximately 0.0028, one approximately 0.0011; the remainder sit at or below approximately 0.0006, most near 0.0002. No significance asterisk is drawn on the panel. | files/figures/PMID33129329/12917_2020_2638_Fig1_HTML.jpg, Figure 1 panel a, read at 300 percent upscale from the publisher raster)

(The uncropped blots show more than one immunoreactive species in tumour lysate, with the reported band selected by an arrow | [figure attestation — pixels cannot be quote-matched] Supplementary Figure S1, 'Figure 1D' membrane: lane 3 carries two distinct bands, one at the arrow and one clearly below it; lane 5 carries two bands, both below the arrow; lane 4 carries a band above the 50 kDa marker that the arrow does not indicate. | files/supplement/PMID33129329/12917_2020_2638_MOESM1_ESM.pdf, Supplementary Figure S1 panel labelled 'Figure 1D', rendered at 300 dpi)

(The target band and the loading control are four kilodaltons apart on the same stripped and reprobed membrane | Western blotting for WWOX (~ 47 kDa, upper panel) and β-actin (43 kDa, lower panel) was performed. | files/fulltext/PMID33129329_Makii2020_PMC.xml, Supplementary Information, Additional file 1 caption)
