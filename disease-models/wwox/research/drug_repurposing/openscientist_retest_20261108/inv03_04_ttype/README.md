# INV-03/04 T-type: full-input repeat (label os-03, 2026-11-08)

Non-canonical research material, public edition, WWOX-DEE reference genotype class. Not medical advice: no dose, schedule or route is given. Source cap: 5 sources newly read (stated in advance); 5 used, none over; one search-hit abstract (PMID 41510857) is a labelled lead beyond the cap with no receipt. Staged receipts only (suffix 32), not recorded.

## Answer first

1. DATO: the report contains no WWOX measurement of any Cav3 channel and no WWOX-specific drug datum of its own; it audits one knowledge-base file and literature (`phase1_note.md`). Its central negative (no WWOX-Cav3 link in PubMed) holds at title-abstract level in two routes today; one unrelated cohort abstract lists WWOX and CACNA1H among many genes.
2. INFERENZA: the report's "annotation artifact" and "general anticonvulsant default" are priors drawn from an absence, not results; the previous brief rightly refused to assume either. They do not replace the three separate questions (benefit, Cav3 mediation, genotype dependence) already answered in `ttype_20261107/output/README.md`.
3. DATO/INFERENZA: the report treats ulixacaltamide as a fourth "unrelated" antagonist beside Z944; it is the same molecule (prior identity check), and Z944 and TTA-P2 are both piperidinylmethyl benzamides (ML218 shares the benzamide head with a different amine; the structural paper studies TTA-P2 and ML218, not Z944). The "orthogonal chemotype concordance" design therefore has fewer independent arms than it claims (D06, D08).
4. DATO (abstract): the CaV3.2/CaV3.3 knockout sentence is stronger than its source; the enhanced-seizure result is for CaV3.3 knockouts and a CaV3.3 plus CaV3.2 double knockout; the paper has no single CaV3.2 knockout and does not show effects "opposite in sign" (D07).
5. DATO (partial full text): the CACNA1H "DEE" citation is one child, inherited variant from an asymptomatic parent, loss-of-function direction, authors say CACNA1H has never been associated with DEE (D10). It does not support the report's prime-candidate ranking of CACNA1H.
6. IPOTESI (kept, weak): metabolic stress to HIF1alpha to Cav3.2 is a chain of transfers; link 1 is a WWOX datum not read here, link 2 has no source, link 3 is hypoxia in non-WWOX neurons (abstract only). It should not rank CACNA1H above G or I (D01-D03, D09).
7. Priority question (unchanged from the previous package): does a Cav3-class blocker at measured exposure reproduce the late-phase reduction seen with ethosuximide in the Wwox-null pup, and does it differ from wild type by an interaction term (`ttype_20261107/output/experiment.tsv` X1)? The report adds one design element worth keeping as a later step: allele-class comparison (E24).

## (a) Coverage

Items: 84 (extraction.tsv; E84 added after the audit). Per kind: observation 20, inference 14, compound 9, alternative_explanation 6, experiment 6, target 5, limit 5, mechanism_step 4, other 4, hypothesis_favourable 3, recommendation 3, open_question 2, link_proposed 2, counter_evidence 1. Sources cited: 19 rows (17 PMIDs). Chains: 10. Per legend_class (reconcile.tsv, items): already_present_and_used 36, unverified 18, verified_or_corrected 11, new_to_legend 10, present_not_used 7, superseded_or_contradicted 2. Per prior_brief_fate (items): omitted 42, kept 25, narrowed 10, modified 7. Decisive propositions: 14 (decisive.tsv).

## (b) What the previous brief did

`ttype_20261107/BRIEF.md` said the report was not in the repository and not needed. Kept: the ethosuximide Fig 7b datum and the lithium comparison (Part 1), the three questions (Part 2), the HIF to CaV3.2 residue (Part 3), probe identity Z944 = ulixacaltamide = PRAX-944 and "do not transfer the ethosuximide result" (Part 4), the worm control. Narrowed: probes to Z944; genetics after one pharmacological comparison. Modified: refusal to assume mechanism or artefact; refusal to prefer CACNA1H for coherence. Omitted: semiology argument, CACNA1H variant literature, knockout-phenotype precedents, mibefradil/Orai, inactive-enantiomer control, allele-class design, cross-model controls, the two flagged citations, the dismech-file claims.

## (c) Sustainable favourable reasons

DATO: Cav3.2 loss prevents epileptogenesis in a mouse status-epilepticus model (abstract); HIF1alpha overexpression raises Cacna1h and network firing in mouse neurons (abstract); gain-of-function CACNA1H variants raise excitability in cultured rat neurons (abstract; TTA-P2 blocked the firing, ethosuximide was tested only on dendritic growth, per the audit). All are transfers from other systems. No favourable WWOX-side link is established beyond the module's own ethosuximide datum, which is class-level and floor-limited.

## (d) Errors and counter-evidence found

Ulixacaltamide listed as separate from Z944 (D08). CaV3.2 single knockout implied; source shows double knockout (D07). CACNA1H "directly implicated in DEE" overshoots its case report (D10). "These effects were reversed" in the C456S abstract attaches to the dendritic-growth result: per the audit TTA-P2 was tested on firing, ethosuximide only on dendritic growth, so no two-drug excitability reversal exists (D12, moderate confidence; full-text read open). The three "independent" convergences for CACNA1H are not independent (shared authorship; a case report that disclaims DEE association). The report says each bridge link is supported (L103) yet cites nothing for metabolic stress to HIF1alpha (D02). It calls antagonists selective and decisive (L12, L28) then not isoform-discriminating (L109). It says the "reported" effect could not be traced; the module traces the one ethosuximide datum to a specific paper (reconcile E57, E60). The Phase-1 note lists the remaining internal tensions.

## (e) Hypotheses still explorable, and what weakens them

Allele-class gradient of a drug response (D14): weakened if severity alone explains it or no hypomorphic model exists. Direct Cav3 current by genotype with and without HIF inhibition (E25): weakened by an absent difference in P17 transcripts (held, within control background) and by culture-condition HIF effects. Cav3.2-directed attribution: weakened by D07 (isoform signs diverge), D09, D10, D11.

## (f) Priority question and experiment

As (7): one concurrent acute comparison in Wwox littermates at measured exposure with a Cav3-class blocker, ethosuximide and vehicle, interaction term fixed in advance (`ttype_20261107/output/experiment.tsv` X1). Allele-class arms only after a null-genotype result.

## (g) Consequence for drug repurposing

Nothing here promotes a compound. The report's only new design elements: allele-class stratification (new_to_legend), an inactive matched control (new_to_legend, no pair named), and a probe panel that must be restated as non-independent. Z944 as a Cav3-class tool: already_in_legend. Ulixacaltamide as separate probe: corrected (same molecule). Mibefradil/Orai: new_to_legend, literature-novel not assessed. CACNA1H over G/I: not supported.

## (h) Consumers to update (proposal only, no edit made)

`ranking_it8_p9_20261029/investigations_it20.tsv` INV-03: add the non-independence of the "unrelated antagonist" panel. `needs/needs.json` NEED-T-TYPE-CALCIUM: add the CaV3.3/CaV3.2 double-knockout precedent and the CACNA1H case-report caveat. `ttype_20261107/output/probes.tsv`: no change. `deepdive_manifests/PMID35243344.json` MH-35243344-01: still open; the primary abstract was read, full text not. No ranking change implied.

## (i) Not reachable

Full text of 25071191, 24277868, 19052226 (Europe PMC HTTP 500 twice; PMC tool returned an empty body for 24277868); full text of 42276303 (prior package); sources 34747138, 30356099, 42538876, 42954437, 42309484, 37391087, 29588962, 31271653 read only to identity; the dismech WOREE file itself; Tringham per-isoform table; 89 Europe PMC full-text hits unscreened. Read order error: 31419467 claimed after the abstract was seen.

## (j) Queries

`queries.tsv` (Q01-Q11).

## Audit appendix (blind verifier vf-03, 2026-11-08)
Verdicts on the 14 decisive propositions: 12 SUPPORTED, 2 PARTLY (D06: identity holds, scaffold sentence mis-sourced and wrong for ML218; D13: the INFERENZA part holds, the 85/77/69 percentages were not found in the paper's main text), 0 NOT SUPPORTED, 0 UNVERIFIABLE (one sub-claim of D13 cannot be verified). Coverage check of the first extraction: 12 report points sampled, 10 PRESENT, 1 PRESENT_NARROWED (the word "independent" in the three convergences, now restored in E46), 1 MISSING (the header identifier MONDO:0014533, now E84); the warrant adjectives of the key absence claim are now noted in E07 and the "entirely T-type-independent" overreach in E13. Reconciliation sample: 8 rows, all pointers hold. Evidence sample: all 17 quotes verbatim; EV18 to EV20 were added for D01, D11 and D03 (EV18 is a verifier read, no producer quote). Narrowings applied: no single CaV3.2 knockout in the CaV3.3/CaV3.2 paper (D07); the C456S reversal covers dendritic growth, not firing, for ethosuximide (D12); promoter activity was in a cell line (D03); the held mouse P17 transcripts show no HIF-target rise (D02); the secondary review on Cacna1i probably shares its origin with the primary (D09). E31 now verified for the hypoglycaemia part (verifier read 34747138), E33 stays unverified. I checked the PubChem structure names for Z944, TTA-P2 and ML218 myself on 2026-11-08 (database, not a counted source). Not reached: full text of 42276303; Results of 24277868 and 25071191 beyond a summary route (verifier, moderate confidence); tables of 30356099; Z941 chemistry; the 89 Europe PMC full-text hits.
