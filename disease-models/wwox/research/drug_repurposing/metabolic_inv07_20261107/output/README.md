# INV-07: metabolic bottleneck in WWOX deficiency (package I7, label i7-p, 2026-11-07)

Non-canonical research material. Not medical advice; no dose, route or schedule; reference genotype class only. E01 to E42 are rows of `evidence.tsv`.

## Answer

NON RISOLTO. No WWOX-deficient neural system has a PDH amount, phosphorylation, activity or flux measurement, or a lactate/pyruvate pair, so a pyruvate-oxidation defect, a lactate-side change and a secondary response are not separated. The lever premises (PDK, LDH, substrate bypass) stay open. No new measurement was made; this package corrects readings and orders the next comparison.

## Errors corrected, and what is new

* DATO: INV-07 says the one human PDH activity measurement shows no difference. It is a non-neural fibroblast line, partial depletion, n not stated, with lactate up in all four conditions and PDK transcript up (E36). It says nothing about neurons.
* DATO: earlier files say the fly paper "measures no pyruvate". It reports none; omics tested only the 200 highest-variance features and the supplement lists significant metabolites, so detection is unestablished (E02). The deposit re-integration has no pyruvate either (E22).
* DATO (fly, PMID 42909904, complete read, cited by receipt): lactate and Atf4 rise only with Wwox RNAi on an Abeta42 background (E03, E11); RNAi alone gives a negative lactate sign, never tested alone, and no Atf4 rise (E04, E12). Ldh transcript is up with Abeta42 alone while lactate does not visibly rise there (E06): INFERENZA, RNA and metabolite abundance dissociate, and neither is activity or flux.
* DATO: Atf4 was never perturbed, so Atf4 to Ldh is co-occurrence in the authors' conditional wording (E13); Abeta42 load rises with Wwox RNAi (E16), a possible mediator. The Ldh rescue is partial, one locomotor endpoint, no Ldh-alone arm, no lactate in the double-RNAi flies (E08); INFERENZA: it neither shows nor excludes a PDH role. The pool is mixed head tissue, so no cell type can be assigned (E01).
* DATO (new, abstract only): the PDK-inhibitor trial in MELAS (PMID 16476929) randomised 30; 15 of 15 on drug against 4 of 15 on placebo stopped medication; 17 of 19 discontinuations were for neuropathy; stopped early, efficacy not judgeable (E29 to E32). 17 of 19 is a share of discontinuations, not of participants. INFERENZA: documents risk in a mitochondrial lactic-acidosis disease at one exposure; neither benefit nor risk transfers to WWOX, and a cell probe is a different use. Full text blocked (HTTP 403).
* DATO: the SH-SY5Y study (PMID 35984507, reused) is WWOX activation under high glucose with a peptide called the inhibitor: no scrambled or genetic arm, text and panel disagree, no pyruvate, lactate or PDH readout (E24 to E28). INFERENZA: not a loss model; no metabolic premise.
* DATO (new, abstract only): PDK isoenzymes phosphorylate different E1 sites and activity depends on kinase and phosphatase amounts (E33, E34). INFERENZA: one phospho-site, Ser293 included, gives neither activity state nor the kinase; numbering against site 1 not read. PDK1 of PDH is not PDPK1.
* DATO (new, abstract only): respiratory CO2 supplies 3 to 100 percent of extracellular acidification (E35); acidification is not a lactate readout without an oxygen correction.

## Explanations still compatible (`explanations.tsv`)

Phosphorylation-limited PDH; lactate production, utilisation or redox change; stress-dependent response; downstream respiratory limit; pyruvate transport; activity-driven demand; composition and maturation. They can coexist.

## Priority question, first comparison

In matched-stage WWOX-deficient human neural cells against an isogenic control, is PDH limited by amount, by phosphorylation, or not at all? First comparison (`experiment.tsv`, step 2): total E1-alpha, phosphorylation at all three sites, activity before and after dephosphorylation, one sample series. Flux, labelled tracing, lactate/pyruvate with redox state and intervention arms follow only where they separate named hypotheses, each with a functional outcome beside it.

## Conditional hypothesis (IPOTESI; nothing promoted or discarded)

If matched neural cells show phosphorylation-limited PDH reversible by dephosphorylation under a defined workload or stress, a PDK-directed probe would act on that limit in that context, and the benefit to test is activity-linked energy handling. LDH reduction only if lactate-driven harm is shown in the same cells (it is detrimental in other fly models, E10); a PDH-bypassing substrate tests supply, not a PDH defect. Cell endpoints cannot separate symptomatic from disease-modifying effect; no such claim is made.

## In silico versus laboratory

Now, in silico: descriptive re-read of PDK, PDP, transporter and LDH transcripts in held tables (step 1; only picks isoforms). Laboratory: steps 2 to 8. Reopen on: an isogenic WWOX-deficient neural line or a deposit with PDH state, flux or lactate/pyruvate; the authors' metabolite table; licensed full text of 16476929 if the operator decides; open full text of PMID 11485553.

## Proposed updates

INV-07 premise text (first bullet). Cards E03 and I01: non-neural qualifier on the human activity datum. ISR/LDH prediction file: "reports no pyruvate". Card E04: fly lactate sign without Abeta42 is nominal. INV-07 priority unchanged.

## Depth

Reused: 42909904 and 35984507 (complete receipts), 35328751 by repository record. New, abstract only: 16476929, 11485553 (full text server error twice, empty PMC text), 25449966. Hit 33629572 not opened. PubMed tool honours OR and parentheses (Q01).

## Added after the independent audit (`../verify/audit_i7.md`: 42 rows, 35 supported, 3 overshoot, 1 not in source, 3 unverifiable)

E02 (pyruvate is not shown to have been tested or undetectable), E18 (the Fig 5D schematic does draw pyruvate and a TCA node, without arrows or values; no PDH or PDK node), E36 (fibroblast details; PDK transcript up in one condition only; a naming slip 'PDK activity' for PDH activity in the source text, repeated in the repository record) and E26 (exact p values; high glucose alone lowers basal respiration and ATP production; the quote was a paraphrase and is flagged for replacement) corrected; limits added to E03, E08, E12, E15, E21, E40, E41. Explanations: the PDK/PDP support list was circular; the downstream-respiratory row cited rows without citrate; "lysate PDH normal" does not point to transport. Experiment steps: XM2, XM3, XM4 carry the audit's cautions (isoform-selective knockdown, transport versus PDH needs a carrier bypass, phosphatase-inhibitor lysis). Absence claim H4 corrected: WWOX with PDH/PDK terms gives 1 hit (the fly paper) in the PubMed tool, which splits "pyruvate dehydrogenase" into pyruvic AND dehydrogenase and so matches lactate dehydrogenase; Europe PMC title/abstract gives 0 for PDH/PDK terms and 2 for lactate plus neural (the fly paper and its preprint); about 69 full-text hits for WWOX with pyruvate dehydrogenase were not read; PMID 33629572 is a mitochondrial-disease exome paper without WWOX or PDK in its abstract (PDK1 identity unverified). MELAS trial arithmetic: 19 of 30 discontinued, at least 13 of the 15 on the drug for neuropathy; the 17 by arm and crossover handling are not stated. Unverifiable blind (barred files): E22, E38, E39, E40/E41 quoted strings. The corrections were rechecked by comparison with the audit text, not by a second blind pass.
