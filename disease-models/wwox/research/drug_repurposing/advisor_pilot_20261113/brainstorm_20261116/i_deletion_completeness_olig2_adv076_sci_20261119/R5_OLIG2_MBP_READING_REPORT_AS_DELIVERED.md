REPORT: Hussain 2023 (PMID 36828035), P47T WW-domain knock-in mouse. Olig2 / Mbp / other myelin measures.
Depth reached: full text (PDF text, PMC XML) with Figures 4 and 6 viewed as images. The supplement is NOT held. The PDF is 39 pages with no supplementary pages. The assets folder has only 9 main-figure JPGs (f0001 to f0009). So Supplementary Figs S6a-d (Mbp) were not seen, and Supplementary Files and Tables were not seen. Everything about Mbp rests on one text sentence. I did not render the PDF with pdftoppm. The held JPG of Fig 4 is the same figure and I viewed it directly.
Tool calls used: 7.

1. OLIG2 COUNT (Fig 4d,e, main text)
- Region: corpus callosum, coronal sections. The images also show hippocampus below the callosum. The Fig 4 title says "hippocampi", but the quantitation is callosal.
- Ages: 80 and 250 days. Sex: Methods say "n = 3/group of either sex". Sex per group is not stated.
- Groups: WT/WT vs P47T/P47T. Heterozygotes were not analysed for Olig2.
- n: the legend says "n = 3 mice/group". Each dot is "a single independent region" (three 500 um2 regions per animal). The graph shows about 9 or 10 dots per group, so the plotted n is regions or fields, not animals. Fig 4e does not show the 3 animals separately.
- Effect (read from graph, approximate): 80 d, WT about 205 vs P47T/P47T about 120. 250 d, WT about 235 vs P47T/P47T about 115. That is roughly 40 to 50 % lower. The y-axis is a count per region and the unit is not stated.
- Test: unpaired Student's t-test, * p < 0.01 (legend). The text says p < 0.01. Each age was apparently tested separately. No correction is mentioned. The test appears to treat regions as the unit (pseudoreplication).
- Interpretation: "reduced number of oligodendrocytes". The Discussion says this is supported by the callosal histology and by BRETIGEA, and "agrees" with the Wwox KO mouse and rat models.
- Internal inconsistency: the legend says "500 um2" regions inside a 1.5 x 1 mm image. 500 um2 is tiny, so "500 um" square may be meant. The Methods say "three independent 500 um2 section". The count of about 200 is incompatible with 500 um2 (a 0.0005 mm2 area), so the unit is likely wrong. This is a unit-notation issue only.
- The Methods and legend agree on the design (three regions per animal, 3 mice). Both are internally consistent with each other.

2. MBP (supplement only)
- Text only (section 2.6): "We also analyzed myelination by staining with myelin basic protein (Mbp) antibody in parietal cortex above corpus callosum. ... no significant differences in Mbp staining were detected when comparing Wwox WT/WT and Wwox P47T/P47T cortical regions (Supplementary Figs. 6a-d)."
- The main text and Methods give no Mbp antibody, dilution, metric (area or intensity), age, sex, n, unit of n or test. The Methods antibody list has no anti-Mbp (it lists Gfap, Iba1, calbindin, calretinin, Olig2, Hcn1). The Image analyses paragraph has no Mbp quantitation. So I could not check legend against text against Methods for Mbp. The Mbp antibody is missing from the Methods.
- No values and no p-value are given. "No significant difference" is stated only.
- Discussion: "despite observing a decrease in oligodendrocyte numbers, we did not detect significant differences in myelination by Mbp staining". The authors treat this as a discordance with the full-KO models, which show hypomyelination. They offer no mechanism.

3. SAME REGION / AGE / ANIMALS?
- No. Olig2 is in the corpus callosum. Mbp is in the parietal cortex above the callosum. The regions are adjacent but different, and cortex is not the white-matter tract where the Olig2 count fell.
- Age and animals for Mbp are not stated in the main text. They are possibly the same 80 and 250 d cohort, but that is unverified. Treat as unknown.
- So the pairing "Olig2 down, Mbp unchanged" is a cross-region comparison, not a within-region dissociation.

4. WHAT OLIG2 MARKS
- The paper calls Olig2 a "pan-marker labeling all oligodendrocyte lineages" (legend and text, citing Valerio-Gomes 2018). So it counts all lineage stages (OPC through mature). It does not distinguish them. The paper's own numbers cannot say which stage is lost.
- Olig2 is also expressed in some other cells, but the paper does not discuss this.

5. MATURITY MARKERS AND TRANSCRIPTS (Fig 6c, RNA-seq, n = 5 per group, 2 M and 3 F, 150 to 280 d)
- No stage-specific protein markers (CC1, Pdgfra, Mog, Plp, Cnp and so on) were stained. Maturity is addressed only indirectly through BRETIGEA deconvolution scores. There are no direct Mbp, Plp or Mog transcript tests in the text. Supplementary File 2 (gene lists) was not seen.
- Fig 6c, read from the graph (Student's t, n = 5 per group per tissue):
 - HPC: OLIGs p = 0.43 (not significant; WT median about 0.07 vs P47T about -0.08, very wide spread). OPCs p = 0.02 (WT about 0.11 vs P47T about 0.08, lower).
 - PFC: OLIGs p = 0.02 (WT about -0.04 vs P47T about -0.21, lower). OPCs p = 0.27 (not significant).
 - Cortex (parietal): no BRETIGEA result is shown. Parietal cortex is the region used for Mbp staining.
- Text and figure disagree. The text says "reduced scores for mature oligodendrocytes (OLIGs) and OPCs in the HPC", but the graph shows HPC OLIGs not significant (p = 0.43). The significant OLIG decrease is in the PFC, which the text does not mention for OLIGs.
- The Discussion says the decrease in oligodendrocyte numbers is supported by BRETIGEA. That is only partly true, and the effect is inconsistent across region and cell type.
- GSEA (Fig 7a): "suppression of gene networks associated with ... glial cell differentiation" in HPC and CTX. This is not specific to oligodendrocytes or myelin in the text. The legend names no myelin term.

6. NOT MEASURED (as far as the held text shows)
- No Luxol fast blue (0 hits in the full text).
- No electron microscopy, so no g-ratio, myelin thickness, axon counts or nodal and paranodal structure (0 hits for "electron").
- No Mbp quantitation in the main text. No other myelin protein (Plp, Mog, Mag, Cnp) staining or western blot. No stage markers (CC1, Pdgfra, Ng2) and no apoptosis or proliferation marker for oligodendrocytes (no Ki67 or caspase), so the paper cannot say whether the lower count reflects loss, arrested differentiation or fewer progenitors.
- No myelin measure in the cerebellum, in 80 d vs 250 d for Mbp, in heterozygotes, or per sex.
- No conduction measure: no compound action potential, nerve conduction velocity, evoked potential latency, or optic nerve or callosal electrophysiology. EEG (Fig 1d) concerns seizures and spikes only, not conduction. No DTI or MRI.
- No callosal Olig2 count per animal (the animal-level mean and its test are not reported).
- No counts of Olig2-positive cells in cortex, so the cortex Mbp result has no matching count.
- No sex-stratified analysis.

7. CAVEATS FOR THE CALLER
- The Olig2 effect rests on n = 3 mice per group, with about 9 or 10 regions plotted as independent points. Regions are pseudoreplicates.
- The Mbp null is not available in the held material. Do not cite a value, region, age or n for it beyond "parietal cortex above corpus callosum, no significant difference, Supplementary Fig 6a-d". The PubMed Central supplementary file (nihms mmc files) is not in the assets folder, so the Mbp null remains unverified until it is obtained.
- Fig 4's title says "hippocampi exhibit ... reduced oligodendrocyte numbers", while the data are callosal.
- Source: PubMed, DOI 10.1016/j.pneurobio.2023.102425.