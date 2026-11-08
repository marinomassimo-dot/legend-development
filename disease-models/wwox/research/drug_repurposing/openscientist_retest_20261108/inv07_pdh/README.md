# INV-07 full-input repeat (PDH, pyruvate, lactate), producer os-07, 2026-11-08

Non-canonical research material. Not medical advice; no dose, route, schedule or clinical preference. Reference genotype class only. Source cap: at most 5 sources newly read; 5 were read (42559713 and 40290041 at partial full text, 42012479, 16517405 and 36537114 at abstract level), so there is no overrun.

## Answer first

* DATO (audit correction, matters for the INV-07 PDK-inhibition hypothesis): the report's node table treats PDK1 expression as inferred from HIF1 biology only. PMID 25012504 reports higher Pdk1 transcript in Wwox-KO MEFs and higher serum lactate in KO mice (Suppl Fig S2A): a WWOX PDK1 datum exists, non-neural, with no PDH activity or phosphorylation measured. The need NEED-PDH-PYRUVATE-AXIS O1 already carries it. So the PDK1 node has WWOX-side transcript support outside neurons; the PDH node has none in any WWOX system.
* DATO: the report is a literature synthesis; it measures nothing. Its central claim, that no PDH activity or flux has been measured in WWOX-deficient human neural cells, was not contradicted. Perimeter (title/abstract only, so full-text-only mentions such as Pdk1 in 25012504 are invisible): Europe PMC and the PubMed tool on 2026-11-08, WWOX/Wwox with pyruvate dehydrogenase, PDK1, PDHA1 or dichloroacetate gave 1 hit (a mitochondrial-disease exome paper, not opened; the auditor's query also returned the fly paper); WWOX with lactate gave 4. Unknown, not negative; the one human PDH activity datum in the module is a non-neural fibroblast pool (no difference).
* INFERENZA: the report's "Model B newly favoured" overreaches. The fly paper reports Ldh, lactate and an Atf4 rise but no PDH measure and no pyruvate value; Atf4 was never perturbed; the Ldh rescue is partial. Models A and B are not exclusive and neither is tested in WWOX-null neurons.
* DATO: the previous INV-07 package (`metabolic_inv07_20261107/`) already holds most of this and in places is more precise than the report. The report adds almost nothing new to the module except a few checkable literature items (KD in PDCD) that the prior brief omitted.
* Errors found in the report: "17 of 19 patients" (30 randomised; 19 stopped, 15 on DCA and 4 on placebo; 17 of those 19 for neuropathy, so 19 is not the trial population); the uncited lithium "abolishes" (module card reads a non-specific suppression); "Drosophila neurons" (mixed head tissue); "25 papers reviewed" versus 12 tabled; 34747138 cited for a statement it does not make (the human-course wording is the DisMech curators'); internal DCA verdict "not justified" versus "conditionally justified at best".
* IPOTESI (unchanged): the priority question stays the prior one, PDH limited by amount, by phosphorylation or not at all, in matched isogenic WWOX-deficient neural cells.

## (a) Coverage

Items per kind (70 after the audit; E68 to E70 added): observation 16, inference 13, recommendation 8, experiment 8, limit 5, compound 4, target 4, other 4, counter_evidence 3, open_question 2, alternative_explanation 1, hypothesis_favourable 1, mechanism_step 1. Sources cited: 15; chains: 7.

Per `legend_class` (items): already_present_and_used 28, unverified 20, verified_or_corrected 13, present_not_used 4, superseded_or_contradicted 5, new_to_legend 0. This package has no new_to_legend row (E35, the WOREE ketogenic diet case series, is held as PAPER 017). Per `prior_brief_fate`: kept 26, omitted 20, modified 17, narrowed 7. Details in `reconcile.tsv`; 14 decisive propositions in `decisive.tsv`; 9 evidence rows in `evidence.tsv`.

## (b) What the previous brief did to the report

The prior brief (`metabolic_inv07_20261107/BRIEF.md`) declared the report a question generator that "prematurely favours LDH/ISR and the ketogenic bypass" and not needed.
* Kept: absence claim, Model A chain, SH-SY5Y qualification, DCA trial denominators, fly-paper contrast, experiments on PDH/phospho/flux.
* Narrowed: BHB or KD as a PDH test, lactate compartmentalisation, ATF4 role.
* Modified: the Model B favour (audit: modified, not narrowed), the scenario verdict table, the "single decisive measurement", the clinical stance, Ser293 as the readout.
* Omitted: 20 items, including 23611579, the PDK1 cytoprotection sentence (cells are HIF-1alpha null, hypoxic), the lithium/Wnt argument, the KD-in-PDCD sources, hypoglycaemia, gene replacement, the footer.

## (c) Sustainable favourable reasons

* DATO: Wwox loss raises HIF1alpha, glycolysis, Pdk1 transcript and lactate in MEFs, cancer cells and KO mice (serum); HIF-1 transactivates PDK1 in HIF-1alpha null cells. Both non-neural; the join is an inference.
* DATO: in the fly, lactate and Atf4 rise with Wwox RNAi on Abeta42; Ldh lowering partly rescues locomotion. Co-occurrence plus partial rescue.
* DATO: KD is effective for seizures in PDCD (8 of 9, retrospective); 3 WOREE individuals responded to KD in one case series (abstract level). Neither shows a PDH defect in WWOX.

## (d) Errors and counter-evidence

See "Errors found" above and `decisive.tsv` P04 to P08, P11, P12, P14. Counter-evidence kept as rows: DCA neuropathy (E25, E26), PDK1 cytoprotection (E27, from `EV07`, hypoxic HIF-1alpha null cells), SH-SY5Y activation under high glucose (E13), absence of human lactic acidosis (E10, a DisMech absence, not a measurement), non-metabolic seizure drivers (E29).

## (e) Hypotheses still explorable and what would weaken them

* Phosphorylation-limited PDH in neurons; weakened by a normal total and phosphorylated E1-alpha with intact activity in isogenic WWOX-null neurons.
* LDH/ISR shift; weakened if lactate rise needs the Abeta42 context or does not follow Atf4 perturbation.
* Subtle, compartment-restricted defect (report's own allowance); weakened by matched flux in separated neuronal and astrocytic populations.

## (f) Priority question and experiment

Unchanged from the prior package: in isogenic WWOX-deficient human neural cells, is PDH limited by amount, by phosphorylation, or not at all? First comparison is total E1-alpha, all three phosphorylation sites, and activity before and after dephosphorylation in one sample series; flux and intervention arms follow only where they separate named hypotheses, each with a functional outcome beside it.

## (g) Consequence for drug repurposing

* DCA/PDK inhibition: already_in_legend (cards E03, I01; INV-07; need O1 holds the WWOX Pdk1 transcript datum); the report adds no WWOX datum; the PDK node has non-neural WWOX transcript support, the PDH node none; PDK1 cytoprotection abstract verified (`EV07`).
* LDH reduction/ISR: already_in_legend as a lever premise; fly rescue is partial, so the premise stays open.
* Ketogenic diet / BHB: already_in_legend (card E04); newly verified PDCD sources (`EV01` to `EV06`) and a WOREE case series (`EV09`, abstract level; already held as PAPER 017). Literature novelty: not assessed for any proposal.
* Priority of INV-07: unchanged.

## (h) Consumers to update

None required by this repeat. Optional: note the existing PAPER 017 (36537114: KD response in 3 of 5; lactate 2.4-3.3 mmol/L in one individual) in the KD card E04 and INV-07 context; note the lithium wording in the report is stronger than card G01.

## (i) Not reachable or not done

Europe PMC fullTextXML returned HTTP 500 for the two PMC records; the PubMed Central full-text tool was used instead (figures not viewed). Not read: 41710159, 42955568 (identity checked only), 23611579 (receipt exists, not reopened), 25012504, 35984507, 42909904 (earlier receipts reused), the dismech YAML, 33629572. Other actors hold reading claims on 36537114. Query times are approximate to the minute.

## (j) Queries run

See `queries.tsv` (12 rows). Identity check of all 13 cited PMIDs: 13 of 13 MATCH, including the six high-range ones.

## Audit appendix (blind verifier vf-07, 2026-11-08)

Verdicts on the 14 decisive propositions: 12 SUPPORTED, P11 supported with two refinements (the null still peaks near 1.3 with lithium, so suppressed; 'also present' in wild type and heterozygote at a floor, no genotype-by-drug test, pSer9 only) and 1 PARTLY (P10: the card's silence is not patient data, and PAPER 017 holds a mild lactate elevation in one of five that was not used). P07's report phrasing was NOT SUPPORTED (denominator). Coverage check of the first extraction: 12 points sampled across the report, 10 PRESENT, 1 PRESENT_NARROWED (the L21 universal claim, now E70) and 1 MISSING (the L98 uniqueness claims, now E68 and E69); i.e. 10 of 12 fully present. Reconciliation sample of 8 rows: E35 not confirmed (already PAPER 017), E21-E23 fate too soft (now modified), E11 pointer unit wrong (lines, not entries); the other five confirmed. Evidence sample: all 9 quotes verbatim; the audit found no row for P02, P04, P05, P06, P07, P11, P14 and P10, now added as EV10 to EV17, several marked as read by the auditor and not by the producer. Narrowings applied: E25 denominator, E16 overexpression rescue without Ldh falling, P03 wording ('HIF-1alpha null cells'), P04 named transcripts, P11 wording, P14 curator wording, P01 perimeter. The audit's tally of the producer's classes (23/12/6/4/2) differs from mine; the figures above are recounted over 70 items. Not reached by the auditor: full text of 16476929 and 16517405, figures of 42909904, Appendix S1C/D of 34747138, the repository copy of the DisMech YAML. Open need for a new read: none within the cap.
