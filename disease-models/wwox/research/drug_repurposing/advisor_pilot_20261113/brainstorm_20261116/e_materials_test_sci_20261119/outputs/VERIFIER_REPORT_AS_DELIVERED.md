# Verifier report (blind comparison of X and Y)

Tool calls used: 18 (of 60). Not medical advice. Hypothesis-level comparison only.

## Decision under comparison
Both outputs reach the same headline decision: (b) a distinct experiment, not (a) a pharmacological comparison. Neither asserts a lever on the WWOX WW1 / PPxY branch. Differences therefore lie in the support, the caveats and the experiment design.

## Sources opened, and sources not opened
Opened (primary):
- Schuchardt 2013, Biochemistry (PMC full text).
- Aqeilan 2005, Cancer Res (abstract only; no PMC copy returned).
- Hussain 2019, Neurobiol Dis (PMC full text).
- Hussain 2023, Prog Neurobiol (PMC full text: Results, Methods, KEGG and EEG passages).
- Pressey 2017, J Biol Chem (abstract).
- Mennesson 2020, eNeuro (abstract).
- UniProt REST, NETO2 human and mouse sequences.

Not opened, so "unchecked":
- Rotem-Bamberger 2022.
- Abu-Odeh 2014.
- Hussain 2018.
- Aqeilan 2007.
- Mennesson 2019.
- Wang 2012 (GSK3-beta / SDR domain).
- The "secondary" items (mouse Erbb4 motif positions and the Pvalb note, in X; the UniProt web summary, in Y).
- Both search perimeters; I did not rerun the searches.

## 1. Primary outcome
- **Primary: `EXPERIMENT_SEPARATES_ALTERNATIVES_BETTER`, favouring X.**
  - X's rejection set distinguishes three outcomes: no change in binding or localisation (hypothesis killed); only the null differs (protein needed, but not WW1 binding, so the PPxY route is killed); and the NETO2 pull-down test with a Dvl2 positive control and a mutated-motif negative control. Y's rejection criteria do not separate "protein needed" from "WW1 PPxY binding needed".
  - Both outputs use P47T versus wild type. X additionally names null as the comparator, which is what makes that separation possible.
  - Y adds a parallel functional readout (ICD localisation, Neto2/kainate currents in PV interneurons), which X defers to after the binding step. That is a real strength of Y, but it does not discriminate between alternatives.
- **Secondary: `MORE_DEFENSIBLE_CONDITIONAL_HYPOTHESIS`, favouring Y.**
  - Y reached the full text of Schuchardt and carries forward the quantitative weakness of the peptide binding and the authors' own physiological-relevance caveats. X, working from the abstract, leaves the ERBB4 binding looking stronger than the source supports.
  - Y also separates the SDR-domain partners (GSK3-beta, Tau) from WW1-PPxY partners, a relation-identity point that X lacks.
- The two outputs are close. The call between them rests on design discrimination (X) against evidence-weight caveats (Y). Neither earns `MORE_INFORMATIVE_PHARMACOLOGICAL_COMPARISON`.

## 2. HARM instances (definition applied)
No clear HARM in either output. Borderline or minor items:

**X**
- "NETO2 has no drug." (Q4). This is an absence claim with no compound-search perimeter. Minor.
- Q4 and Q6 name "a kinase inhibitor and a neuregulin-pathway probe" as tools. They are gated on step 6 and the output says no compound is justified now, so this is not harm.
- The Dvl2 and Wbp1 peptides are called "PPPY peptides" and used as the positive control. This is shared with Y; see the shared item below.

**Y**
- "pan-ErbB kinase inhibitors exist (a repurposing-class lever)". The class is named without a source, but the sentence says direction is unclear and no source on selectivity was retrieved. Minor. The Q6 conditional comparison, "ERBB4 pathway tools against kainate-receptor probes", is gated on step 1 being positive, so it is not harm.
- "No small molecule against WW1 was found" and "no approved drug whose action maps onto the branch". These are absence claims with no compound-search perimeter. The perimeter section lists literature searches only. Minor.
- Q5 says the ERBB4 evidence includes "human and monkey cell lines (HeLa, MCF-7, COS)". COS does not appear in the Aqeilan 2005 abstract. I could not verify it; Y labels that paper abstract-only. It is not contradicted, but I could not confirm the COS claim.
- Q6 says "NETO2 ... is expressed in interneurons". This comes from the Mennesson 2019 abstract, which I did not open. Mennesson 2020, which I did open, supports a PV-interneuron maturation effect in the adult amygdala, not expression per se.

**Shared issue, neither output flags it (could change the experiment)**
- Hussain 2023 Methods list the biotinylated peptides as Dvl2 "HPYSPQHELSSY" and Wbp1 "SGSGGTPTVG". Neither string contains a PPxY motif.
- The Results text calls both "typical WW group I binders containing PPPY motifs". The pull-down used n = 2 per group in Methods.
- Both outputs repeat "PPPY" and propose these peptides as the positive control (X: "Dvl2 as positive control"; Y: "the Dvl2/Wbp1 pull-down as positive control").
- This could be a transcription artefact in the PMC text. It deserves a check against the published PDF before the control is relied on. Counted as traceability for the comparison, but an experiment-design risk for both.

## 3. NO_DIFFERENCE
Not applied. The outputs reach the same decision but differ in experiment discrimination and in evidence-weight caveats; see Section 5.

## 4. Descriptive counts

| | X | Y |
|---|---|---|
| Questions (of 6) with a full-text anchor in the pivotal table that I verified | 3 clear (Q2, Q3, Q6, via Hussain 2019 and 2023), plus Q1 only for non-ERBB4 partners | 3 clear (Q1 via Schuchardt, Q2 and Q6 via Hussain 2023), plus Q3 partly (full-text allele data; the ERBB4 cell data are abstract-only) |
| Q4 and Q5 | No full-text anchor (negative or absence items) | No full-text anchor (negative or absence items) |
| Claims contradicted | 0 | 0 |
| Claims unfindable in cited source | 0 | 0 firmly; the "COS" cell line is not in the Aqeilan 2005 abstract, and I cannot confirm it |
| Pivotal claims not checked | about 5 (Rotem-Bamberger 2022, Abu-Odeh 2014, Hussain 2018, mouse Erbb4 motif positions, Pvalb note) | about 5 (Rotem-Bamberger 2022, Aqeilan 2007, Mennesson 2019, Wang 2012, UniProt web summary as sourced) |

Verification results for the pivotal rows I opened:

**Verified for X**
- Hussain 2019: PV+ interneurons down 44% overall (n = 7 vs 7; DG p < .005, CA1 p < .05).
- Hussain 2019: NPY+ interneurons down 30% in DG only (n = 6 vs 6, p < .05).
- Hussain 2019: GAD65/67 reduced (n = 5 vs 5, p < .05).
- Hussain 2019: 2 weeks old, both sexes; the authors say cause versus consequence needs investigation.
- Hussain 2023: Hcn1+ basket cells unchanged and Purkinje cells reduced; P47T protein and mRNA similar (mRNA n = 6 per group); EEG n = 3 vs 3 over 21 to 53 h.
- UniProt: PPHY at residue 395 in mouse NETO2 (Q8BNJ6). It is also at 395 in the human sequence (Q8NC67), which matches Y's "FDPPHYELF". Both secondary claims about the NETO2 motif are therefore correct.
- Pressey 2017: Neto2 increases total KCC2 abundance in cultured mouse hippocampal neurons.
- Aqeilan 2005 abstract: matches the claims in both outputs (first WW domain, HeLa and MCF-7 retention, YAP coactivation, dose-dependent, mutant has no effect).
- Schuchardt abstract: matches X's WW1 versus WW2 claim and the WW2 "augments" claim.

**Verified for Y**
- Schuchardt Methods and Results: human WW1 residues 16-50; 12-mer peptides; ITC.
- Schuchardt Results: "a little over 100 μM" for PY3; "hundreds of micromolar" for PY1 and PY2; WW2 no binding; tandem "more than two-fold stronger".
- Schuchardt Conclusions: the PY1/PY2 physiological-relevance caveat and the short-peptide caveat.
- Schuchardt: Y85W is a protein-engineering idea.
- Hussain 2023: interictal spikes 0-3098/h versus 0-68/h; 11-22 seizures in 43-53 h; the KEGG statement "Suppression of GABAergic and glutamatergic synapses in CTX and HPC".
- Mennesson 2020: adult (not P23) reduction in PV and PNN markers.

## 5. Items found by one output and not the other

**Found by X only**
1. Hussain 2019 quantified endpoints (44%, 30%, n, tests) at full-text level. Could not change the comparison; strengthens traceability.
2. The mouse Erbb4 PPxY motif positions (PPIY 1032, PPAY 1053, PPPY 1298) from a secondary scan. I did not check these. They would feed the peptide design in the experiment, so they could change the experiment if wrong, and are unchecked.
3. Hcn1+ basket cells unchanged in the cerebellum of the P47T mouse. Could not change the comparison.
4. Null versus P47T as the discriminating rejection criterion, and the explicit rule that a change only in null kills the PPxY route. Could change the experiment (this is the main point in X's favour).
5. NETO2 PPHY pull-down with a mutated-motif peptide as negative control. Could change the experiment.
6. Hussain 2018 TAP-MS reported as not listing ERBB4 or NETO2. Not checked by me; if right, it is a retrieval of a useful negative, but it could not change the comparison alone.
7. Explicit ceiling on the 2019 PV finding: no maturation control. Could not change the comparison.

**Found by Y only**
1. The weak peptide affinities (hundreds of micromolar for PY1 and PY2; a little over 100 μM for PY3) and the authors' own relevance caveats. Could change the comparison. It lowers the credibility of ERBB4 as a physiologically relevant WW1 partner.
2. Aqeilan 2007, breast cancer, Wwox correlated with membranous ERBB4 (556 tumours, P = 0.0003). I did not open it. It adds a human tissue association, but in cancer. Could not change the comparison.
3. GSK3-beta and Tau bind through the SDR domain, not WW1-PPxY (Wang 2012, unchecked). This is a relation-identity guard against over-counting neural partners. Could change the comparison if confirmed.
4. Mennesson 2019 and 2020: Neto2 knockout alters PV-interneuron maturation in adult amygdala and reduces synaptosomal GluK2/3 and GluK5. I verified the 2020 abstract. It shows NETO2 matters in PV-interneuron circuits, but nothing about WWOX. Could not change the comparison; it does shape the NETO2 functional readout in the experiment.
5. Functional readouts in the same experiment (ICD localisation; Neto2/kainate currents in PV interneurons) and a conditional pharmacological comparison after a positive step 1. Could change the experiment. Note the conditional comparison is a downstream plan, not support for a lever.
6. Age note: the null interneuron findings are from 2-week mice, whereas P47T mice survive more than a year. Could change the experiment (age selection). X makes a related point in Q5, restricted to the P47T interneuron count.
7. Europe PMC REST and UniProt REST searches added to the perimeter. Narrows the NETO2 absence claim. Could not change the comparison.

## Net
- X has a more discriminating experiment and the stronger full-text quantification of the neural phenotype.
- Y has the better-calibrated reading of the ERBB4 binding evidence and a richer functional readout.
- Neither output contains a HARM instance. The shared PPPY positive-control question is the only point I would send back to both before the experiment is designed.
- Decision-relevant conclusion for the caller: (b), the distinct binding and localisation experiment; no pharmacological comparison until it is positive.

Sources used via PubMed: Schuchardt 2013 (doi 10.1021/bi400987k), Aqeilan 2005 (doi 10.1158/0008-5472.CAN-05-1150), Hussain 2019 (doi 10.1016/j.nbd.2018.09.026), Hussain 2023 (doi 10.1016/j.pneurobio.2023.102425), Pressey 2017 (doi 10.1074/jbc.M116.767236), Mennesson 2020 (doi 10.1523/ENEURO.0541-19.2020).