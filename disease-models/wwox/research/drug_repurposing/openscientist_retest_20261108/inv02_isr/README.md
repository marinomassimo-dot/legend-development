# INV-02 ISR, full-input repeat (producer os-02, 2026-11-08)

Non-canonical research material. Not medical advice; no dose, schedule or route. The report is external AI-generated material to assess. Nothing was recorded, committed or promoted; four receipts are staged (suffix 31). Source cap: at most 5 newly read; 4 used (no overrun).

## Answer first

* DATO: the report's central admission holds at the protein level in human cells. No source read or found measures p-eIF2a, ATF4 protein or translation rate in WWOX-deficient human neural cells. INFERENZA: its broader sentence that no study measured ISR endpoints in "a WWOX model" is too wide: one PubMed string returns exactly one paper (PMID 42909904, fly neurons, Atf4 protein up only with amyloid), and LEGEND holds an organoid transcript set with the ISR targets lower, and one shRNA library higher (needs.json NEED-ISR-ATTENUATION O1 O2).
* INFERENZA: the "attenuation" conclusion is the report's own inference by analogy and by a shared node. The GSK3 to eIF2B link was tested link by link on 2026-11-07 and not established; the title of PMID 12133000 says dephosphorylation of the site is insufficient to activate eIF2B.
* DATO: the VWM precedent is real and now read in more detail: ISRIB raised MBP and lowered g-ratio in two patient lines (PMID 40296303), but the line the report quotes is an Introduction sentence, and the authors read the drug as a UPR inhibitor.
* DATO: all 19 cited PMIDs resolve to the right paper, including 42097410 (a 2026 review). No identifier error.
* IPOTESI (priority): measure p-eIF2a, ATF4 protein, phospho-eIF2Be at the GSK3 serine and per-cell translation in isogenic WWOX-deficient human neurons at matched stage before any compound; unchanged from the INV-02 line. The report adds no new reason to move a compound.

## (a) Coverage
Items 57 (Phase 1): observation 20, inference 8, experiment 5, limit 4, other 4, mechanism_step 3, compound 3, alternative_explanation 2, hypothesis_favourable 2, recommendation 2, target 2, link_proposed 1, open_question 1. `reconcile.tsv` covers all 57. Per `legend_class`: verified_or_corrected 16, already_present_and_used 15, present_not_used 14, new_to_legend 5, unverified 5, superseded_or_contradicted 2. Per `prior_brief_fate`: modified 22, narrowed 12, kept 11, omitted 11 (E54 not applicable counted with unverified).

## (b) What the earlier briefs did
The briefs of 2026-11-07 stated that the report was not needed and treated it as a question generator. Kept: the INV-02 question and the idea of reading the sign first. Narrowed: lithium (a comparator only), S535A (numbering, DYRK2). Modified: the GSK3-eIF2B chain (tested link by link), "chronic means harmful" and "hypomyelination means low translation" (both forbidden in the gsk3_eif2b brief), salubrinal "contraindicated" (forbidden as a clinical class). Omitted: the mTOR and autophagy arm (E29 to E32), the knowledge-base claim, elvitegravir, the six other-tissue PMIDs, the 2026 review, the TBI paper as a decision input.

## (c) Sustainable favourable reasons
VWM organoid myelin rescue by ISRIB in a human system (PMID 40296303, small n); GSK-3b phosphorylation of the eIF2Be site outside WWOX (PMID 12133000, 15001529, abstract level); WWOX-null mice show lower GSK-3b Ser9 and lithium lowers a seizure score. All are transfers or single-lane or single-model facts; none is a WWOX measurement of translation.

## (d) Errors and counter-evidence
Overbroad absence claim (above). "Confirmed" in the conclusion for a step the report calls inferred. "Three independent lines" share one node. The quoted VWM sentence says ISRIB inhibits eIF2 phosphorylation, against the held mechanism. Autophagy and mTOR inference from ovarian carcinoma lines without densitometry. "ISRIB rescues regardless of upstream cause" untested. 12133000 title contradicts use as support. The organoid phenotype is based on very small numbers and read by its authors as delay. The ISR in elvitegravir work is drug-induced.

## (e) Hypotheses still explorable
Reduced eIF2B activity without raised p-eIF2a in WWOX deficiency (weakened by: phospho-epsilon not raised, translation not lowered at matched stage). ISR attenuation helping hypomyelination (weakened by: ISR target sets low in knockout organoid transcripts, no benefit of ISRIB in the engagement-controlled arm with p-eIF2a not raised).

## (f) Priority question and experiment
Same as INV-02: protein-level sign by cell type and stage, with an engagement control for any ISRIB arm and phospho-epsilon beside p-eIF2a.

## (g) Consequence for repurposing (novelty class per proposal)
ISRIB-class: probe, already_in_legend. Lithium/GSK3: comparator, already_in_legend. Salubrinal-type: negative-control arm only, already_in_legend (as contested potentiators). Elvitegravir and the 2026 review: new_to_legend as sources, no compound change. The knockout organoid/ISR-transcript datum and the fly datum argue for keeping both directions open. Literature novelty: not assessed.

## (h) Consumers to update
None changed here. Proposal: the INV-02 evidence line may cite PMID 32894619 and 42097410 as transfer context only, and the VWM line may state that the myelin readouts were read in `inv02_isr/evidence.tsv` EV01.

## (i) Not reachable
dismech knowledge base (not opened); full texts of 12133000 and 15001529 (earlier failures, not retried); figures of 40296303 (captions only); full text of 42097410, 32894619, 28696288 (abstract only); 42909904 was found by search, not re-read.

## (j) Queries
`queries.tsv` (Q01 to Q08). Perimeter of the absence check: one PubMed string, one translation string, 2026-11-08, no Europe PMC second route.

## Audit appendix (blind verifier vf-02, 2026-11-08)
Verdicts on the 14 decisive propositions: 13 SUPPORTED (P04, P09, P10, P14 at abstract depth only), 1 PARTLY (P11: "untested" holds, "expected small" rests on one Discussion sentence and a secondary citation, and held EI11 points the other way). None NOT SUPPORTED. Coverage check of the first extraction: 12 points sampled across L2-L150, 10 PRESENT, 2 PRESENT_NARROWED (the L38 joint prediction, now row E58, and the AD/TBI table cells, now in E35), 0 MISSING. Reconciliation sample: 8 rows, all pointers exist and say what the rows claim; the E37/E56 class label overstates (LEGEND holds an INFERENZA, not a measurement). Evidence sample: all 9 quotes verbatim; two proposition id slips repaired (EV02, EV07). Narrowings applied: the fly Atf4 rise is conditional on neuronal Abeta42; PMID 28749468 is a WWOX and PERK datum in ovarian carcinoma cells (non-neural); lithium in Wwox-null mice lowers the PTZ score in all three genotypes and the null still peaks near stage 1 ("abolishes" is too strong); salubrinal arm is wild-type mice; the report cites PMID 12133000 as the bridge but its own result runs the other way; PMID 18583310 does not corroborate the axis. Counts in section (a) are items, not rows. Not reached: full texts of 12133000, 15001529, 32894619, 42097410, 28696288; figure images of 40296303; the dismech knowledge base; absence checks use two PubMed strings, no second route.
