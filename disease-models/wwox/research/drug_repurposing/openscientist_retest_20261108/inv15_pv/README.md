# INV-15 PV interneurons: full-input repeat (producer os-15, 2026-11-08)

Non-canonical, not medical advice, no dose or schedule. Reference genotype class only. The report is external AI-generated material, assessed and not trusted. Files here: `extraction.tsv` (61 items), `sources_cited.tsv` (6), `chains.tsv` (8), `phase1_note.md`, `reconcile.tsv` (61 rows), `decisive.tsv` (14), `evidence.tsv` (22 rows after the audit), `queries.tsv` (11), `receipts/FTR-20261108-42583891-39.json` (staged, checker verdict OK). New-source cap: at most 5; used 1 (abstract only), no overrun.

## Answer first

1. DATO. The report's headline, "no PV measurement has ever been reported", is wrong as worded: PV-positive cells were counted 44 percent lower in the global-knockout hippocampus at 2 weeks (PMID 30290271), and the same PubMed conjunction returns 3 hits here, not zero. The report also misreads the electrophysiology model: the sIPSC study (PMID 34634460) is the Synapsin-I-Cre conditional line, not a global knockout.
2. INFERENZA. The core caution survives: in the neuron-targeted cortex, a pyramidal sIPSC readout does not identify PV cells (interneurons were 5 and 6 cells, not PV-identified), so "PV deficit" there is an inference. A marker count in a different model, region and tissue is not a cell-loss count.
3. INFERENZA. The report's strongest argument, that only a postsynaptic GABA-A deficit explains the amplitude fall, is not supported: mIPSC was not recorded, the internal was high chloride, no antagonist is named, and the paper's "postsynaptic" wording concerns glutamatergic mEPSCs. The report also contradicts itself on this (B lowers amplitude in its table at L34 and diagram at L80, yet only F does at L39).
4. IPOTESI, unbridged. The hyaluronan/PNN route is a report-generated link: a measured first step in non-neuronal cells (27845895, where the overexpressed complex kills and the authors tie neuronal protection to less signalling) and a review-level second step (42812881, PNNs most prominently around PV cells). No WWOX bridge was found in bounded searches.
5. The decision-relevant step is unchanged: per-animal, same-section lineage-density and PV comparison in the Cre-positive littermate design with a recombination read-out, before any drug probe. The report's interneuron-restricted line is not needed first; no such WWOX model was found.

## (a) Coverage

Items per kind (Phase 1): observation 14, inference 9, limit 8, experiment 9, alternative_explanation 6, compound 4, other 4, hypothesis_favourable 3, recommendation 2, target 1, open_question 1 (61). Per `legend_class`: already_present_and_used 33, verified_or_corrected 14, present_not_used 4, superseded_or_contradicted 4, new_to_legend 3, unverified 3. Per `prior_brief_fate`: kept 24, modified 18, narrowed 11, omitted 8. Eight chains (`chains.tsv`), fourteen decisive propositions (`decisive.tsv`), six cited identifiers, all identities MATCH.

## (b) What the previous brief kept, narrowed, modified, omitted

The previous brief (`pv_inv15_20261107/BRIEF.md`) told the delegate to correct the report and to assume neither "PV loss shown" nor "no PV data". Kept: the IPSC observation, the single-age limit, the alternatives A1-A7, the HA/PNN datum rows, the net experiment. Modified: absence of PV data (restored 30290271), the model identity, Synapsin-Cre uniformity, cell autonomy as universal requirement, the postsynaptic attribution, the all-experiments gate. Narrowed: drug levers (conditional, no harm claim, global excitation is not selective), the PNN route, and the optogenetic PV-ChR2 test (E49: the prior brief and X2 qualified PV-Cre designs, so the fate is narrowed, corrected after the audit). Omitted: the migration/MGE node (E36), the spheroid and AAV9 replication rows (E41, E42, E45, E56), "avoid agents that suppress inhibition" (E21). Omission does not mean error; E41 and E42 rest on receipts the prior package did not use for this question.

## (c) Sustainable favourable reasons

DATO: the inhibitory current is halved in the neuron-targeted model at P13-17 and heterozygotes carry a partial burst phenotype in the module; PV-marker counts are lower in the global knockout; interneuron AP amplitude is lower (5 against 6 cells). INFERENZA: these make a PV or fast-spiking contribution plausible and worth a direct per-animal test. PNNs do surround PV cells most prominently. None shows fewer PV cells in the neuron-targeted model.

## (d) Errors and counter-evidence found

- Model misidentified as global knockout (E11); "no PV data" (E03, E04) contradicted by 30290271 and by the PubMed hit count.
- Recombination "in essentially all neurons" (E09) is not established; the only reporter figure is an adult whole-brain Mecp2 value from another allele (NeuN-high nuclei, 36 percent, via the consumer note).
- Heterozygotes are pooled as controls in 34634460 although they differ in several measures; "design is sound" (E43) is therefore partial.
- Statistics: the report says pseudoreplication cannot be determined; the paper declares cells and animals, with printed inconsistencies, and does not declare the unit of its tests. With one value per cell, 10 of 18 printed KS p values lie below the exact-test floor, compatible with events as units. No contradiction of the paper is asserted (the unit is undeclared).
- Internal inconsistency B/F (L34, L39, L80), and "five plus a sixth" explanations against a six-row table in which C does not explain the observed fall.
- The 33914858 double citation is not an error: that paper holds both the Synapsin-Cre mouse and a small human stem-cell spheroid model (3 and 4 patched cells; field power from 9 and 6 slices of 3 and 2 organoids). It describes the deletion as "particularly in most of the differentiated neurons", not "essentially all".
- 27845895 is cited only for loss-of-signalling; in knockout MEFs Smad4 relocation is delayed (about 4 h) rather than absent, and the WWOX-negative lines are MDA-MB-231 and MDA-MB-435S cancer cells with little WWOX, all non-neuronal; its main finding is death when the complex is overexpressed, and nuclear accumulation in apoptotic rat neurons. The Has3 seizure link in the review runs through extracellular space volume, independent of PV and nets. The review 42812881 also carries counter-evidence neither the report nor this producer first carried: germline PV-cell Acan deletion removed WFA-defined nets with limited change in adult PV-cell electrophysiology (compensation noted; keyword-searched by the verifier, not read start to finish), which limits the step "disrupted nets delay PV maturation".
- Statistics wording stays at the operator level: the unit of the KS tests is undeclared and the 10-of-18 observation is "compatible with events as units"; no contradiction of the paper is asserted.

## (e) Hypotheses still explorable, and what would weaken them

Fewer lineage cells (A1), lower PV per cell or delayed program (A2/A3), intrinsic fast-spiking change (A4), changed release or input (A5/A6), postsynaptic change (A7), or several at once (A8). Each weakens if the corresponding per-animal measure is unchanged (see `decisive.tsv`). The PNN route weakens if net per PV cell does not differ at a measurable age, if WFA differences follow PV number, or if matrix genes and proteins do not differ.

## (f) Priority question or experiment

IPOTESI. Per animal, same sections, Cre-positive littermate design, P14 and P17: PV protein and Pvalb mRNA, a lineage denominator, a recombination reporter in PV cells, with the animal as the unit. It decides whether a counts-first or a function-first line continues. Interneuron-restricted deletion is a later step, not a prerequisite.

## (g) Consequence for drug repurposing, with novelty class

- No compound is supported. Kv3 positive modulation: class lever transferred from a rat phencyclidine model (42583891, abstract only); not tested in any WWOX preparation. Novelty class: already_in_legend (Q-PVfire, thin pharmacology); literature-novel not assessed.
- GABA-A benzodiazepine-site potentiation: already_in_legend (`function_pharm_it14_p3_20261101`, hypothesis H1); locus of the lost current still unmeasured.
- Excitatory-input modulators: already_in_legend as a cautioned class; global excitation is not selective.
- PNN-modifying agents: already_in_legend only as a conditional arm; no bridge.
- Optogenetic PV-ChR2 per-connection test: partly known (optogenetic interneuron drive is named as the M3 discriminator in `commit_candidates/CC-20260826-EGABA-CLOSURE-01.md`); the PV-specific per-connection design is new; literature-novel not assessed. IPSC/PV endpoints in spheroid and AAV9 paradigms: partly known (`analysis/mechanism_intervention_map.md` E-2), with a precondition: dorsally patterned organoids commonly lack interneurons (`analysis/interneuron_sparing_rule_test_20260923.md`); the AAV9 half is new_to_legend. MGE migration route: new_to_legend as an idea; literature-novel not assessed.
- GABAergic drugs: none tested in any WWOX experimental preparation; a vigabatrin case report in two children (PMID 41442931, abstract only, found by the verifier) is a clinical exposure, not a test.

## (h) Consumers to update

None beyond the existing deltas: `pv_inv15_20261107/output/README.md` already carries the corrections. Suggested small additions for the integrator: record that the report's model identification and zero-hit statement are wrong; add the B/F inconsistency to the report-assessment note; keep INV-15 rank unchanged.

## (i) Not reachable or not done

Figures of the PV papers not viewed; 34747138 not reopened (inhibitory-readout absence unverified); the migration/MGE claim not checked; Europe PMC hits screened by title only (25 of 93 and 25 of 52); PMID 37247333 and 34831305 not opened; no registries or working model opened for the MGE node. No access challenge met; no e-mail or contact sent.

## (j) Queries run

See `queries.tsv` (Q1-Q11). New source read: 42583891 abstract only (staged receipt `FTR-20261108-42583891-39`, validated). All other sources reused from earlier receipts and not reopened.

## Audit appendix (blind verifier vf-15, 2026-11-08)

Verdicts on the 14 decisive propositions: 13 SUPPORTED (D12 at lower confidence for a single attribution, D10 with a narrowed perimeter), 1 PARTLY (D08: the locus is unmeasured and the arithmetic holds, but "no GABAergic drug tested" needed the perimeter "experimental preparation"; the recombinant-receptor primaries were not reopened). None NOT SUPPORTED, none unverifiable. Coverage check of the first extraction: 12 points sampled across the report, 11 present, 1 narrowed (E49 lacked the clause "isolates the PV-specific contribution"), 0 missing; the clause is now in the row. Reconciliation sample: 8 rows; 6 fully accurate, E49 and E56 had an overstated novelty and E49 a wrong fate. Evidence sample: all quotes verbatim; V08 carried only D14 and V09 was a Discussion sentence, both repaired. Narrowings applied: D03 locator (Methods 5.3 and 5.4); D08 perimeter and the vigabatrin case report; D10 titles-only Europe PMC screening and the full-text-only blind spot; D11 slice and organoid structure; D12 inferred attribution and "most of the differentiated neurons"; 44 percent PV reduction is a full BK5-Cre knockout, n 7 against 7, optical fractionator, no cell-death or pan-neuronal count; MEF relocation delayed (about 4 h); the Acan counter-evidence in the review; E49 novelty and fate; E56 novelty and the organoid-interneuron precondition; the report text has 143 lines. Not reached: figure images of 30290271 and 34634460; the 34634460 supplement; 34747138; 40507943 and 34831305; a direct reread of the 35966957 PMC page; the review 42812881 beyond keyword passages; the recombinant-receptor primaries behind the GABA-A lever. Open need, not run (no new read beyond the cap): a direct reread of 35966957 to confirm the 36 percent attribution to the Synapsin-I-Cre line. One note from the audit worth keeping: the same Cre-line study found incomplete cortical deletion, which also weakens the report's premise that the recorded pyramidal cell is itself Wwox-null (explanation F).
