# Items for the blind verifier (statement, report anchor, source, locator hint, class) — the producer's reasoning and prior-check notes are withheld

## D01
- statement: DATO (as reported, unchecked): Wwox-null mice carry metabolic stress or hypoglycaemia that neuronal WWOX rescues; link 1 of the chain, measured in the mouse if the report reads its source correctly.
- report anchor: L41, L63, L103 (E31)
- source cited or found: PMID:34747138 (identity MATCH)
- locator hint: Repudi 2021 results on blood glucose and rescue by neuronal gene therapy
- class: WWOX datum

## D02
- statement: IPOTESI: metabolic stress activates HIF1alpha in WWOX-deficient neurons; link 2, inferred, no source cited by the report, and the module's HIF record holds the neuronal WWOX-to-HIF direction as unresolved and two-sided.
- report anchor: L65, L103 (E32)
- source cited or found: none cited; hif_it10_p21_20261031/README.md found
- locator hint: hif_it10 README section on neural premise and direction
- class: absence

## D03
- statement: DATO (abstract): HIF1alpha overexpression raises Cacna1h expression, promoter activity and network firing in cultured mouse neurons; INFERENZA: necessity of CaV3.2 for the firing rise is not shown at abstract level, and the context is hypoxia or OD/R, not hypoglycaemia; link 3, transfer from another system.
- report anchor: L41, L66, L93 (E29)
- source cited or found: PMID:42276303 (identity MATCH; abstract seen again today in PubMed tool output, not counted as newly read)
- locator hint: Results: any CACNA1H knockdown, blocker or current recording; Methods: culture protocol
- class: transfer from other system

## D04
- statement: DATO (abstract): Cav3.2 knockout mice lack the post-status-epilepticus T-current and burst changes and have far fewer spontaneous seizures; INFERENZA: this is an acquired-epilepsy precedent for Cav3.2 necessity, with no link to WWOX loss or to a DEE.
- report anchor: L22, L41, L86 (E30)
- source cited or found: PMID:19052226 (identity MATCH)
- locator hint: Results on Cav3.2-/- after pilocarpine status epilepticus; Methods for species
- class: transfer from other system

## D05
- statement: DATO (search): no PubMed title-abstract hit joins WWOX or WOREE with CACNA1G, H, I, T-type or Cav3 except one cohort abstract listing both genes among many; INFERENZA: that is not a negative result for a link in full text (Europe PMC full text: 89 hits, unread) nor in unpublished work. Perimeter: PubMed tool and Europe PMC REST, 2026-11-08, strings in queries.tsv.
- report anchor: L8, L41, L103 (E01, E05)
- source cited or found: PMID:41510857 (abstract only, lead beyond cap); queries Q05-Q09
- locator hint: Full-text hits of Q08 (89) would need screening for a WWOX-near-T-type statement
- class: absence

## D06
- statement: INFERENZA: the report's 'structurally unrelated selective antagonists' (Z944, Z941, TTA-P2, ulixacaltamide) are not a set of independent chemotypes: ulixacaltamide is Z944, and Z944, ML218 and TTA-P2 share a piperidine-amide scaffold per the structural paper; the abstracts describe Z944 as selective for the T-type class, and the report itself concedes imperfect isoform discrimination (L109). Class selectivity is not isoform discrimination, and concordance across them does not establish independence.
- report anchor: L12, L28, L34, L109, L116 (E21, E62, E66-E69)
- source cited or found: PMID:38605177 and PMID:41489546 (prior full text, partial); PMID:31419467 abstract (today); PubChem CID 44540045
- locator hint: 38605177 Results on binding pocket; 41489546 Table 2 potencies; Z941 chemistry not read
- class: compound/class

## D07
- statement: DATO (abstract): CaV3.3 knockout, TRN-silenced CaV3.3, and a CaV3.3 plus CaV3.2 double knockout all show increased drug-induced SWD susceptibility; the report's 'CaV3.2 knockout' phrase (L22) is not supported as a single-isoform statement at abstract level. Model: drug-induced absence-type seizures in mice, not WWOX.
- report anchor: L22, L87 (E36)
- source cited or found: PMID:25071191 (identity MATCH)
- locator hint: Results on single CaV3.2 knockout, if any; ethosuximide sensitivity of the double knockout (secondary account only, deepdive manifest PMID35243344 MH-35243344-01)
- class: transcript/protein/activity/phenotype

## D08
- statement: INFERENZA: adding ulixacaltamide as a fourth, separate probe duplicates Z944; the useful extra arm must be a molecule of a different scaffold (selectivity measured per isoform) and not a different name.
- report anchor: L12, L116 (E69)
- source cited or found: PubChem CID 44540045; ChEMBL CHEMBL3934636 (prior package, 2026-11-07, reused)
- locator hint: identifiers in probes.tsv P1
- class: compound/class

## D09
- statement: IPOTESI: CACNA1I (Cav3.3) is excluded by the report without any CACNA1I row; the only held Cav3.3 information is secondary or in absence-type models (TRN burst loss with enhanced SWD; Cacna1i KO increased GHB sensitivity per a secondary review), so isoform attribution among G, H and I stays undetermined, not weighted toward H.
- report anchor: L34, L79, L114 (E47, E74)
- source cited or found: PMID:25071191 abstract (today); PMID 40564020 (secondary, held in compare_it28 receipt)
- locator hint: 25071191 Results on CaV3.3; 40564020 on Cacna1i KO
- class: transfer from other system

## D10
- statement: DATO: the CACNA1H DEE citation concerns one child with de novo SCN8A plus an inherited CACNA1H variant from an asymptomatic parent; the authors state CACNA1H has never been associated with DEE, that the variant shifts activation by a few millivolts (loss-of-function direction), and that pathogenic involvement needs confirmation. The other flagged citation (Z944) reports a rat kainate epileptogenesis study with a class-level 'selective' wording.
- report anchor: L44, L95, L98 (E42, E40, E63)
- source cited or found: PMID:34399820 (partial full text); PMID:31419467 (abstract)
- locator hint: 34399820 Discussion paragraph on CACNA1H; 31419467 Methods for the exposure design
- class: independent confirmation or same-origin reuse

## D11
- statement: DATO: ethosuximide protection from PTZ convulsions in the worm persisted with a null in the T-type ortholog tested (cca-1); INFERENZA: it justifies an alternative-mechanism control and does not show the mechanism in the Wwox pup; unfavourable to a Cav3 attribution only by analogy.
- report anchor: L19, L22, L36 (E13)
- source cited or found: PMID:30189284
- locator hint: Results on the cca-1 double mutant; one saturating concentration, n 13 to 15
- class: transfer from other system

## D12
- statement: DATO (abstract): in cultured rat neurons the C456S Cav3.2 variant raised firing and burst propensity, and 'these effects' were reversed by ethosuximide or TTA-P2; INFERENZA: the sentence follows the dendritic-growth result, so the reversal of firing excitability is not settled at abstract level; a recombinant gain-of-function variant is not WWOX.
- report anchor: L44, L94 (E44, E82)
- source cited or found: PMID:24277868 (identity MATCH)
- locator hint: Results: drug application on firing and burst threshold; Methods: concentrations
- class: transfer from other system

## D13
- statement: INFERENZA: the semiology argument (focal 85, spasms 77, tonic 69 percent) lowers the prior only if the Wwox pup PTZ endpoint is absence-type, which the module holds as unknown (Racine stage, no EEG); the percentages come from a cohort paper cited second-hand through the knowledge base.
- report anchor: L10, L25, L107 (E15-E17)
- source cited or found: PMID:30356099 and PMID:42954437 (identity MATCH, not read)
- locator hint: 30356099 phenotype table; compare_it28 README section 4 item 8
- class: WWOX datum

## D14
- statement: IPOTESI: a genotype-dependent T-type effect would show a gradient across WWOX allele class; no WWOX measurement of a drug response by allele class exists in the report or in the module (the one ethosuximide datum is in the null with floor-limited wild type and heterozygote and no interaction test); an allele gradient would also arise from severity alone.
- report anchor: L12, L38, L77, L120 (E24, E34, E79)
- source cited or found: PMID:32000863 (prior package); no source for the gradient
- locator hint: Fig 7b and the Methods on age and n (fig7.tsv)
- class: WWOX datum
