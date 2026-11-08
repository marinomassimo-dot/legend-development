# Blind audit, INV-03/04 (T-type), verifier vf-03, 2026-11-08

Task record ORCH-IT38OS-20261108. Non-canonical working material, not medical advice. Public edition, WWOX-DEE reference genotype class.
Order kept: parts A and B were decided before opening `README.md`, `phase1_note.md` or `chains.tsv`; none of the three was opened at any point. Files read: `verify/items.md`, `extraction.tsv`, `reconcile.tsv`, `evidence.tsv`, the original report (all 126 lines). PMIDs claimed under vf-03 before reading (34747138, 42276303, 19052226, 41510857, 38605177, 31419467, 25071191, 30189284, 34399820, 24277868, 30356099, 42954437). No gate, lint or test run, no delegation.

Depth key: ABS = PubMed abstract (tool output today); MAIN = PMC main text through the PubMed MCP full-text tool or NCBI efetch (figures, tables and legends mostly stripped); WF = PMC page summarised by the WebFetch tool (a secondary model summary, not a verbatim read; confidence moderate); DB = database record read today.

## A. Decisive propositions

### D01 (34747138, mouse) SUPPORTED
Read: ABS, and MAIN via efetch (Results, Methods). Abstract: neuronal restoration "rescued ... hypoglycemia"; Results: Wwox-null and control-vector mice "hypoglycemic from the second week", AAV-treated mice had normal blood glucose (glucometer on tail blood, Methods). DATO. Caveat: "metabolic stress" is the report's gloss; what is measured is blood glucose. Whether hypoglycaemia is a stress acting on neurons is not tested there (INFERENZA).

### D02 (no source; hif_it10 README) SUPPORTED as a claim of absence
Read `hif_it10_p21_20261031/README.md` lines 13-15, 47, 63, 69. It holds the neural WWOX-to-HIF premise as unresolved, direction "genuinely two-sided", and adds that the mouse P17 brain with Wwox deletion shows no HIF-target elevation (Epas1, Slc2a1, Ldha, Pgk1, Ndrg1, P4ha1 flat or lower in four contrasts; bulk transcript). Point for the producer: this record is unfavourable to link 2 in the very species of link 1 (mouse), so the item can say "no source, and the held mouse transcript data do not show HIF-target elevation". Perimeter: that README only; the report cites nothing for the step although L103 says each link is "individually supported".

### D03 (42276303) SUPPORTED, one wording correction
Read: ABS only (full text not in PMC/EPMC: pmcid absent, isOpenAccess N). Abstract confirms: OD/R raised firing; HIF1alpha overexpression increased Cacna1h expression "consistently" in cell lines and primary cortical neurons; promoter activity rose in NS20Y cells (a cell line, not primary neurons); HIF1alpha overexpression elevated MEA network activity in primary cortical neurons; CaV3.2 called a "putative transcriptional target". No CACNA1H knockdown, blocker or current recording is stated, so necessity of CaV3.2 for the firing rise is not shown at abstract level (INFERENZA, correct). Context is hypoxia/OD/R, not hypoglycaemia (transfer, correct). Correction: item says "promoter activity ... in cultured mouse neurons"; the abstract places promoter activity in NS20Y cells, and does not state the species of the primary neurons (mouse is probable from MeSH and from the murine slices). Methods not reachable.

### D04 (19052226) SUPPORTED
Read: ABS. Abstract: Cav3.2 upregulation after status epilepticus raises T-currents and burst firing; "These functional changes are absent in mice lacking Ca(v)3.2 subunits"; neuropathology "virtually completely absent"; spontaneous seizures "dramatically reduced". Pilocarpine acquired-epilepsy model, mouse knockout (Wistar rat also in MeSH, used for the electrophysiology side). DATO. No WWOX or DEE link: INFERENZA correct. Provenance note not in the item: 19052226 and 42276303 share two authors (Becker AJ, Schoch S; Bonn), so the report's "three independent convergences" (L79) include two that come from one research group and one builds on the other.

### D05 (absence, Q05-Q09) SUPPORTED, reproduced
Re-ran today. PubMed MCP, `(WWOX OR WOREE) AND (CACNA1G OR CACNA1H OR CACNA1I OR "T-type" OR Cav3 OR "T-type calcium")`: 1 hit, PMID 41510857. Europe PMC REST, same terms all fields: hitCount 89; restricted to title/abstract: 1 hit (same PMID). The abstract of 41510857 (Europe PMC record) lists WWOX and CACNA1H among about 50 genes in a drug-resistant epilepsy cohort and claims no link. Hence "0 PubMed hits" in the report (L41, L103) is off by one gene-list hit, with no change in meaning. The 89 full-text hits are not screened by me either. Absence of evidence, not a negative result: correct. Perimeter: two routes, 2026-11-08, one query string; the producer's Q05-Q09 strings were not re-run one by one.

### D06 (compound/class) PARTLY
Identity SUPPORTED: PubChem CID 44540045 returns title Z944 with synonyms Ulixacaltamide, PRAX-944, PRAX944, CHEMBL3934636 (DB, today). So the report's list of four "structurally unrelated" antagonists (L12, L116) names one molecule twice. Z944 is also described as "a potent and selective antagonist" in 31419467 (ABS), which is class wording; the report's own L109 concedes imperfect isoform discrimination. Scaffold claim needs correction: PubChem today gives Z944 = N-[[1-[2-(tert-butylamino)-2-oxoethyl]piperidin-4-yl]methyl]-3-chloro-5-fluorobenzamide; TTA-P2 = 3,5-dichloro-N-[[1-[(2,2-dimethyloxan-4-yl)methyl]-4-fluoropiperidin-4-yl]methyl]benzamide (piperidinylmethyl benzamide, shared with Z944); ML218 = 3,5-dichloro-N-[[3-(3,3-dimethylbutyl)-3-azabicyclo[3.1.0]hexan-6-yl]methyl]benzamide (benzamide with a bicyclic amine, not a piperidine). The structural paper 38605177 (ABS) contains ACT-709478, TTA-A2, TTA-P2 and ML218; Z944 is not among its four compounds, so "Z944, ML218 and TTA-P2 share a piperidine-amide scaffold per the structural paper" is mis-sourced for Z944 and over-narrow for ML218. Safer wording: "Z944 and TTA-P2 are both piperidinylmethyl benzamides; ML218 shares the benzamide head with a different amine" (DB-based). Z941 chemistry not found by name in PubChem (not resolved). Not read: 41489546 Table 2 (reused prior full text).

### D07 (25071191) SUPPORTED
Read: ABS and WF. Abstract: CaV3.3(-/-) mice and TRN-silenced CaV3.3 mice show increased drug-induced SWD susceptibility; the CaV3.3 plus CaV3.2 double knockout also shows enhanced SWD. WF: the paper tests no single CaV3.2 knockout; ethosuximide reported only in CaV3.3(-/-) (suppressed GBL-induced SWD). So the report's "CaV3.3 and CaV3.2 knockouts increased susceptibility" (F003, L22; evidence table L87) is not supported for a single-isoform CaV3.2 knockout. Second point: the report's "isoform effects can be opposite in sign" (F003 item 3) is not shown by this paper at abstract level: the evidence is that deleting the isoform raised SWD against expectation, not a comparison of two isoforms with opposite signs. Model: pharmacological absence-type SWD in mice, not WWOX.

### D08 SUPPORTED (identity), inference sound
PubChem synonyms today: Z944 = Ulixacaltamide = PRAX-944 = CHEMBL3934636. A fourth probe named ulixacaltamide adds no chemistry; a molecule of another scaffold with per-isoform potency is the needed arm. The ChEMBL record itself was not re-opened (PubChem carries the ChEMBL id).

### D09 (CACNA1I) SUPPORTED
ABS 25071191: the only CaV3.3 information is knockout in drug-induced SWD models (increased susceptibility). Secondary review 40564020 (PMC12189920 via efetch, MAIN, Introduction and mouse-model section): "In Cacna1i (Cav3.3) knockout mice ... susceptibility to GHB-induced seizures is increased"; the same review's table lists Cacna1g deletion as "No spontaneous SWDs. Resistant to GHB, Baclofen" and Cacna1i deletion as "Increased sensitivity to GHB", and states no CAV3.3 mutations reported in CAE patients. The review's Cacna1i sentence cites a reference that matches the PNAS paper's finding, so it is probably the same origin, not a second confirmation (INFERENZA; the reference list was not checked). The report holds no CACNA1I row, so "less favoured" has no stated basis; note the same table makes Cacna1g the isoform with a resistance phenotype in the absence-type model.

### D10 (34399820, 31419467) SUPPORTED
Read 34399820: ABS and MAIN (case description, Results, summary paragraph; figures not seen). One girl, early severe DEE, de novo SCN8A duplication plus an inherited CACNA1H c.952G>A (G318S) from an asymptomatic father; "has never been associated with DEEs" (gene name stripped in the extraction); recordings in HEK/tsA-201 cells show no change in T-conductance and a half-activation shift of +4.3 mV; the authors call the variant loss-of-function direction, "not predicted to be deleterious", and say pathogenic involvement needs confirmation. The report's "directly implicated in DEE" (L44) overshoots; the producer's wording is right. 31419467 (ABS): rat kainate status epilepticus, Z944 60 mg/kg/day continuous infusion for four weeks versus levetiracetam and vehicle; "potent and selective antagonist" is class wording; Methods not read.

### D11 (30189284, C. elegans) SUPPORTED
Read: ABS and MAIN (Results 3.3, Discussion). unc-49 GABA-A receptor mutant worms, PTZ 7 mg/ml for 15 min, ethosuximide 4 mg/ml pre-treatment 2 h (abolition of convulsions at 4 mg/ml); cca-1 null double mutant: anticonvulsant activity "unaffected"; succinimide inactive. The authors conclude ethosuximide "does not prevent PTZ-induced convulsions in unc-49 mutants by inhibiting T-type calcium channels". Not checked: "n 13 to 15" (counts are in figure legends, stripped in the extraction), and "one saturating concentration" is consistent with 4 mg/ml but not read as such. Overreach in the report, not in the item: L10 says ethosuximide's activity "has been shown to be entirely T-type-independent"; the datum is one worm model, one PTZ assay, the single ortholog tested.

### D12 (24277868) SUPPORTED, strengthened
Read: ABS; WF for Results. Abstract order confirmed: firing and burst threshold, surface expression, then dendritic growth; "These effects were reversed to normal by either ... ethosuximide or ... TTA-P2" follows the dendritic growth sentence. WF of the Results: TTA-P2 (1 uM) blocked spontaneous firing of C456S cells by about 66%; ethosuximide (0.3 mM) was used only in the dendritic growth/arborization experiments, not on firing; neither drug was tested on the burst/low-threshold-spike threshold; the word "reversed" appears in the Abstract and Discussion, Results say "blocked". Consequence: the report's "excitability phenotype was reversed by two structurally distinct blockers" (L44, E82, E44) is not supported for excitability; the two-drug concordance exists only for dendritic growth. Confidence moderate (summariser, first 100000 characters; the Figure 5 legend and text disagree on the TTA-P2 concentration, 0.1 versus 0.3 uM). Recombinant variant in cultured rat neurons, not WWOX.

### D13 (30356099, 42954437) PARTLY
INFERENZA part SUPPORTED: `compare_it28_p9_20261105/README.md` item 8 (line 88) holds the Wwox pup phenotype as absence-type versus clonic UNKNOWN (Racine stage, no EEG). Percentages: UNVERIFIABLE by me. 30356099 (Piard, 20 new plus aggregated cases): ABS and MAIN via efetch (tables not in the XML) give no 85, 77 or 69 percent; the text says seizures "either focal or generalized", West syndrome 26 percent, "Tonic, clonic, tonic-clonic, myoclonic seizures as well as infantile spasms and absences were described". So the percentages are the report's knowledge-base figures, not seen in the paper text. 42954437 is a review of serotonergic modulation in absence epilepsy; "T-type ... well established" is an opening sentence of its abstract (secondary, unsourced there), not a test of T-type necessity.

### D14 SUPPORTED (module record)
Read `ttype_20261107/output/fig7.tsv` (panel 7b rows: floor in +/+ and +/-, null n=6 per arm, no interaction test, graphical reading) and `needs/needs.json` NEED-T-TYPE-CALCIUM O1 (null only, interaction not tested). Grep of `ttype_20261107` and `compare_it28_p9_20261105` for allele-class wording: none; "hypomorph" appears in older records of other topics. The severity-alone alternative for an allele gradient is a logical point, not a datum. I did not re-view the Fig 7 image.

### Verdict table

| Item | Verdict | Note |
|---|---|---|
| D01 | SUPPORTED | hypoglycaemia measured; "metabolic stress" is a gloss |
| D02 | SUPPORTED | module record also shows no HIF-target rise in mouse P17 null brain |
| D03 | SUPPORTED | promoter activity was in NS20Y cells, not primary neurons |
| D04 | SUPPORTED | add shared Bonn authorship with D03 source |
| D05 | SUPPORTED | reproduced: PubMed 1 hit, Europe PMC 89 full-text, 1 title/abstract |
| D06 | PARTLY | identity confirmed; scaffold sentence mis-sourced and imprecise for ML218 |
| D07 | SUPPORTED | no single CaV3.2 KO in the paper; "opposite in sign" not shown |
| D08 | SUPPORTED | PubChem synonyms |
| D09 | SUPPORTED | secondary review likely same origin as the PNAS paper |
| D10 | SUPPORTED | |
| D11 | SUPPORTED | n 13-15 not checked |
| D12 | SUPPORTED | stronger: ethosuximide not tested on firing |
| D13 | PARTLY | inference supported; percentages not found in the paper text |
| D14 | SUPPORTED | module record; image not re-viewed |

Counts: SUPPORTED 12, PARTLY 2, NOT SUPPORTED 0, UNVERIFIABLE 0 (one sub-claim of D13 is unverifiable).

## B. Coverage audit (12 points, report read in full)

| # | Report point (anchor) | Extraction row | Result |
|---|---|---|---|
| 1 | grep of about 1,800 lines for CACNA, T-type, Cav, calcium channel, ethosuximide (L8, L16) | E02 | PRESENT |
| 2 | end of list of curated treatments: ASM, AAV9-SynI-WWOX, nutrition, genetic counselling (L16) | E06 | PRESENT |
| 3 | valproate named in passing, mechanism distinct from Z941/Z944 (L28) | E70 | PRESENT |
| 4 | CACNA1H "prime candidate" through "three independent convergences" (L79) | E46 | PRESENT_NARROWED: the word "independent" is dropped; two convergences share a group and one builds on the other |
| 5 | CACNA1G/CACNA1I "less favoured", CACNA1G channelopathy without seizures (L79) | E47, E74 | PRESENT (E47 notes CACNA1I has no row) |
| 6 | R1584P as seizure modulator (L96) | E45 | PRESENT |
| 7 | 29588962 GGE variants, last in the evidence table (L97) | E43 | PRESENT |
| 8 | "mismatch"-flagged citations 31419467 and 34399820 (L98) | E63 | PRESENT |
| 9 | semiology data cohort-level, lowers the prior only (L107) | E61 | PRESENT |
| 10 | inactive control to exclude non-specific CNS-depressant effect (L118) | E23, E53 | PRESENT |
| 11 | non-WWOX models PTZ/kainate, last follow-up (L124) | E26 | PRESENT |
| 12 | disorder identifier MONDO:0014533 in the report header (L5) | none | MISSING |

Result: 10 of 12 PRESENT, 1 PRESENT_NARROWED, 1 MISSING. Extension scan for the same kind of content (identifiers, metadata, warrant adjectives): further misses are the report's warrant wording for the absence, "extensively validated" and "deeply researched, ontology-harmonized" (L8, L16): E07 keeps only "meaningful, not an oversight" (PRESENT_NARROWED; the adjectives are the unverified warrant of the key absence claim and should be listed as report assertions). Evidence-table titles (L83-97) are not content points. No other miss found in lists, hedges, side remarks, experiments or counter-arguments. Additional narrowing that matters: E13 carries the worm datum correctly but not the report's generalisation "entirely T-type-independent" (L10); suggest adding it to E13 note as an overreach marker.

## C. Reconciliation sample (8 rows)

Rows taken, by first item id: E12/E65/E75, E23, E24/E79 (new_to_legend); E13/E51/E64, E03/E71 (already_present_and_used); E25, E28/E78 (present_not_used); E57/E60 (superseded_or_contradicted; the only row of that class, so the minimum count of 1 holds).

| Row | Pointer check | Verdict |
|---|---|---|
| E12/E65/E75 Orai | `git grep -i orai` outside this folder: only ORAI2 in unrelated target lists (generation_it9_p2 results); `catalogue_resilience_it16_p3_20261101/queue_reconciliation_reports_searched.tsv` line 29 has mibefradil as MENTIONED_ONLY | holds |
| E23 enantiomer | no hit in `ttype_20261107`, `compare_it28_p9_20261105`, `needs`; the word does occur in other, unrelated records (pathograph, commit candidates), so "new" holds only for this thread's perimeter, which the row states | holds, perimeter narrow |
| E24/E79 allele class | no allele-class stratification of a drug response in `ttype_20261107` or `compare_it28_p9_20261105` | holds |
| E13/E51/E64 | `probes.tsv` P2 ("the worm shows PTZ protection with no T-type ortholog") and `output/README.md` line 8 exist as cited; prior brief Part 4 says the worm datum "justifies control for alternative mechanisms and does not show which mechanism operates" | holds; prior_brief_fate "kept" checked against `ttype_20261107/BRIEF.md` |
| E03/E71 | `needs/needs.json` NEED-T-TYPE-CALCIUM O1 exists (ethosuximide null-only, interaction not tested; lithium is in fig7.tsv 7d); BRIEF Part 1 asks for the lithium comparison with Fig 7d | holds; "kept" checked |
| E25 | `experiment.tsv` X3 (slice T-current/burst, null versus wild type, optional) and `chain.tsv` L10 (Cacna1g/h transcripts in P17 null deposits) exist as cited | holds |
| E28/E78 | `chain.tsv` L1-L6, L9 exist; `hif_it10` README lines 15, 47, 63 say direction two-sided and no HIF-target elevation in P17 mouse brain; BRIEF Part 3 forbids preferring CACNA1H for coherence and asks which links are supported in WWOX systems | holds; "narrowed" checked |
| E57/E60 | `ttype_20261107/output/README.md` Part 1 traces the datum to Cheng 2020 Fig 7b; BRIEF says the report "is not in the repository and you do not need it" | holds; "omitted" checked |

prior_brief_fate checked against `ttype_20261107/BRIEF.md` for four rows (E13, E03/E71, E28/E78, E57/E60): all four consistent. Observation: E01/E05 row reports today's single hit versus the report's zero; I reproduced it (D05).

## D. Evidence sample (`evidence.tsv`, all 17 rows)

Quotes checked verbatim: EV01-EV04 (25071191 abstract), EV05-EV07 (24277868 abstract), EV08-EV09 (19052226 abstract), EV10-EV11, EV13 (34399820 main text; gene names are stripped in the extraction, so the quotes read as in the printed text), EV12 (34399820 abstract, gene names restored from the PubMed record), EV14-EV15 (31419467 abstract), EV16 (42276303 abstract), EV17 (41510857 abstract, quote cut at "WWOX" where the list continues). All verbatim, all within 25 words, all carry the stated proposition; locators are section-level only for 34399820 (the paper has no section headings in the extraction).
Gaps: no row carries D01 (hypoglycaemia rescue) or D11 (cca-1 result); EV16 carries only the OD/R firing sentence, not the HIF1alpha-overexpression to Cacna1h and promoter result that D03 rests on (a quote such as "HIF1α overexpression also elevated network activity" would carry it); D02, D05 (queries) and D06 (PubChem) rest on other files. EV05 note says the wording was "reconstructed from the PubMed record": the text I checked is verbatim as quoted.

## Corrections the producer must make

1. `verify/items.md` D06 (and `reconcile.tsv` row "E21,E66,E67,E68", column prior_verification; `probes.tsv` P1/P3/P4 of `ttype_20261107` if reused): replace "Z944, ML218 and TTA-P2 share a piperidine-amide scaffold per the structural paper" with "Z944 and TTA-P2 are both piperidinylmethyl benzamides; ML218 has the same benzamide head with an azabicyclohexane amine; 38605177 studies TTA-P2 and ML218, not Z944".
2. `extraction.tsv` E36 note and D07: state that the paper has no single-CaV3.2 knockout (double knockout only) and that "opposite in sign" (E37) is not shown by it; add to E37 note.
3. `extraction.tsv` E44/E82 and `reconcile.tsv` row "E44,E82": add that, per the Results, TTA-P2 was tested on firing (about 66 percent block) and ethosuximide only on dendritic growth, so the report's two-drug "excitability reversal" is unsupported (moderate confidence, WebFetch summary; recommend one MAIN read of PMC3934715 Results and Figure 5 legend when a full-text route is open).
4. `extraction.tsv` E46: restore "independent" in the content and note that 19052226 and 42276303 share two authors (Bonn) and that convergence 3 (34399820) is a case report whose authors disclaim DEE association.
5. `extraction.tsv`: add a row for the header identifier MONDO:0014533 (L5) and a note on the warrant adjectives (L8, L16) in E07; add the "entirely T-type-independent" generalisation (L10) to E13 as overreach.
6. `evidence.tsv`: add rows for D01 (34747138, Results, hypoglycaemic from week 2, normal glucose after AAV9-SynI-WWOX), D11 (30189284, "unaffected by mutation of cca-1" statement) and the HIF1alpha overexpression quote for D03.
7. `reconcile.tsv` row "E31,E33" (class unverified): D01 is now verified for the hypoglycaemia part (34747138 abstract and Results), so class could be verified_or_corrected for E31; E33 stays unverified (knowledge-base text). Row "E15": add that the 85/77/69 percentages are not in the main text of 30356099 as read.
8. D05 wording: the report says 0 PubMed hits; today the same family of terms gives 1 hit (gene-list cohort); the item already says so, keep.

## Open uncertainties

- 42276303 Methods, species of primary neurons, and any CACNA1H manipulation: full text unreachable (not in PMC/EPMC).
- 24277868 Results: read through a model summary, not verbatim; Figure 5 legend versus text disagree on TTA-P2 concentration.
- 25071191 "no single CaV3.2 KO" rests on the same summary route; the abstract alone is consistent.
- 30356099 tables not retrievable, so the 85/77/69 percentages may be in a table; 42954437 and 22344687 not opened beyond metadata or not at all (22344687 was not in the item list, and the report's "directly confirming" inference at F005 was not re-checked here).
- 41489546 Table 2 and Z941 chemistry not reached; the Z941 relation to Z944 is unverified.
- D11 sample sizes (n 13 to 15) and D14 Fig 7 image not re-checked; D05 Europe PMC 89 hits not screened.
- Europe PMC full-text XML returned HTTP 500 for the PMCIDs tried, so NCBI efetch and the PMC tool were the routes; efetch strips figure/table content.
