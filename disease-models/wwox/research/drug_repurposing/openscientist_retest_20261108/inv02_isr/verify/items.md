# Items for the blind verifier (statement, report anchor, source, locator hint, class) — the producer's reasoning and prior-check notes are withheld

## P01
- statement: INFERENZA/DATO: no protein-level measurement of p-eIF2a, ATF4 or translation exists in WWOX-deficient human neural cells, but the report's wider statement of no ISR endpoint in any WWOX model is contradicted by one fly Atf4 protein datum and by transcript-level sets held in LEGEND.
- report anchor: L9; L17; L19; L155
- source cited or found: PMID 42909904 (found by query Q05); needs.json NEED-ISR-ATTENUATION O1 O2
- locator hint: Results, Atf4 immunofluorescence; organoid ATF4 target-set analysis document
- class: absence

## P02
- statement: DATO: Ser9 phosphorylation of GSK-3b is lower in Wwox-null mouse brain at postnatal day 20 (single lane per genotype); this is a regulatory-site proxy, not an activity measure on eIF2Be.
- report anchor: L34; L108
- source cited or found: PMID 32000863
- locator hint: Results, GSK-3b Western blot figure
- class: WWOX datum

## P03
- statement: DATO/INFERENZA: lithium lowers a PTZ seizure score in Wwox-null mice, but the effect is also present in controls, so it does not show that GSK-3b causes the seizures or that eIF2B is involved.
- report anchor: L34; L38; L153
- source cited or found: PMID 32000863
- locator hint: Results, lithium and PTZ experiments
- class: binding/action/benefit

## P04
- statement: DATO: GSK3 phosphorylates eIF2Be at the Ser535 site (rat numbering) in non-neural systems, but one source (PMID 12133000, title and abstract) reports dephosphorylation of that site is insufficient to activate eIF2B; the step has no WWOX or neuronal measurement.
- report anchor: L36; L109-110; L118
- source cited or found: PMID 12133000; PMID 15001529
- locator hint: 12133000 Results (full text unreachable earlier); 15001529 cardiac myocyte, LiCl or isoproterenol
- class: transfer from other system

## P05
- statement: INFERENZA: salubrinal-type potentiation is called contraindicated by the report on a single adult AD-mouse study; this is a preclinical prediction, not a contraindication, and the held ISR literature says potentiator effects are contested.
- report anchor: L13; L27; L88
- source cited or found: PMID 33531382
- locator hint: Results, salubrinal arm
- class: compound/class

## P06
- statement: DATO: in two patient-derived and two control human iPSC organoid lines carrying EIF2B mutations, ISRIB raised MBP and lowered the g-ratio at week 10; the authors read the drug as a UPR inhibitor and state a small sample.
- report anchor: L43; L111
- source cited or found: PMID 40296303
- locator hint: Results 3.4 and 3.7; Figures 3 and 6; Discussion
- class: transfer from other system

## P07
- statement: INFERENZA: the report's quotation on VWM (ISRIB inhibits eIF2 phosphorylation) is a background sentence of the paper, not a result, and it conflicts with the held mechanism that ISRIB acts downstream of phospho-eIF2.
- report anchor: L43
- source cited or found: PMID 40296303; held rows EI04 EI27 of the nb2_isrib package
- locator hint: Introduction, last paragraph; module PMID 33531382 salubrinal result
- class: binding/action/benefit

## P08
- statement: DATO: WWOX-deletion human cerebral organoids show hyperexcitability and reduced myelin, from small organoid numbers, which the authors read as delay; it does not show a translation-limited state.
- report anchor: L22; L102
- source cited or found: PMID 33914858
- locator hint: Results, organoid section; Fig 7I legend
- class: WWOX datum

## P09
- statement: DATO: elvitegravir blocked rat oligodendrocyte precursor differentiation through an ISR that trans-ISRIB prevented; the ISR here is induced by a drug in cultured rat cells, not by a genetic defect.
- report anchor: L24; L103
- source cited or found: PMID 32894619
- locator hint: Abstract (full text not opened)
- class: transfer from other system

## P10
- statement: DATO: a review states that acute ISR activation can be protective and chronic activation may confine neurons to hypo-plastic states in aging-related cognitive disorders (PMID 42097410, a 2026 review, identity confirmed); the step from chronic to maladaptive in a developmental disorder is the report's inference.
- report anchor: L24; L94; L104
- source cited or found: PMID 42097410
- locator hint: Abstract
- class: independent confirmation or same-origin reuse

## P11
- statement: INFERENZA: ISRIB rescuing the eIF2B step regardless of upstream cause is untested for a GSK3-site lesion; its effect is expected to be small with phospho-eIF2a not raised.
- report anchor: L120
- source cited or found: held: nb2_isrib README_isrib; isrib_discrim README (grid)
- locator hint: ISRIB mechanism rows EI10 EI11 EI15 EI24
- class: binding/action/benefit

## P12
- statement: DATO/INFERENZA: autophagy suppression by WWOX and mTORC1 inference come from ovarian carcinoma lines with no densitometry; the TSC2 statement has no source, so no translation-up counter-mechanism is excluded.
- report anchor: L46; L112
- source cited or found: PMID 33300063
- locator hint: Results and Discussion, Beclin-1 LC3 p-mTOR blots
- class: absence

## P13
- statement: DATO: all 19 PMIDs cited resolve to a matching title, first author and DOI in PubMed and Crossref, including 42097410 (published 2026); none is a wrong identifier.
- report anchor: L102-113
- source cited or found: PMID list (Q01)
- locator hint: identity tool output
- class: independent confirmation or same-origin reuse

## P14
- statement: DATO: ISRIB reversed hippocampal-dependent deficits after TBI in adult mice, with persistent ISR activation reported there; the premise of an elevated ISR is measured in TBI and not in WWOX.
- report anchor: L27; L106
- source cited or found: PMID 28696288
- locator hint: Abstract
- class: transfer from other system
