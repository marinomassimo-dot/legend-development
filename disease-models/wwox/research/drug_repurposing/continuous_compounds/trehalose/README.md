# Trehalose in WWOX loss of function

26 November 2026 · SCI_CODEX · sole active compound · [prespecified comparison](pretest_20261126.md)

**Decision at opening.** Retain trehalose as a test of completed autophagic turnover and glucose handling. Direct neuronal data support a late clearance limit at high nominal exposure in one system. Separate intracellular intact exposure from meal or formulation effects before treating a report of more LC3 or p62 as evidence of greater flux.

## WWOX expression distinguishes uptake from the degradation step

| Prospective marker | P17 mouse cortex TPM | P17 mouse hippocampus TPM | Human week-15 organoid CPM |
| --- | ---: | ---: | ---: |
| SLC2A8, GLUT8 | 19.2 → 10.8 | 20.1 → 11.6 | 19.2 → 18.4 |
| SLC2A1, GLUT1 | 79.1 → 70.5 | 57.6 → 43.6 | 58.5 → 156.3 |
| SLC2A3, GLUT3 | 83.9 → 87.4 | 101.9 → 58.2 | 63.4 → 147.9 |
| RB1CC1, initiation scaffold | 10.4 → 12.7 | 15.7 → 12.2 | 34.6 → 18.5 |
| TFEB, lysosomal transcription factor | 23.7 → 16.6 | 14.4 → 14.5 | 16.4 → 13.5 |
| LAMP2, lysosomal membrane marker | 18.7 → 18.6 | 29.9 → 27.6 | 57.3 → 61.7 |
| CTSD, lysosomal protease | 363.6 → 298.4 | 174.8 → 183.0 | 284.0 → 307.7 |

Values are control → knockout library means. Cortex has 4/3 control/KO libraries, mouse hippocampus 2/3 and organoid 2/4 from a shared human parental line. Directional sensitivity under most single-library omissions depends on the marker. For SLC2A8, log2(1 + abundance) omission intervals for cortex and hippocampus stay below zero (−1.31 to −0.38 and −1.47 to −0.41), while organoid libraries span zero (−0.15 to +0.05). Mouse hippocampal excitatory nuclei go **26.6 → 36.0 CPM** (329 → 372 raw UMIs), inhibitory **43.0 → 54.4**, and astrocytes **35.6 → 36.6**. Across all assigned nuclei the summed count/denominator gives **516/18,437,114 → 656/16,582,476**, or **28.0 → 39.6 CPM**. Thus the bulk and single-nucleus assays have opposite directions even after combining the represented classes. One pooled genotype per nuclear series, capture differences and distinct library units leave biological explanations open. TREH is mapped but very sparse in selected nuclei and low in bulk. The held organoids also have lower EIF4EBP1 and higher MTOR and DEPTOR, consistent with the recorded mixed transcript direction. RNA cannot infer surface GLUT8, flux, hydrolysis, phosphorylated mTOR activity or lysosomal turnover. [Bulk data](contrasts.tsv) · [Assigned nuclei](nuclei.tsv) · [Input checksums](../d_mannose/inputs.tsv)

## Direct neuronal experiment and first exposure boundary

In differentiated SH-SY5Y cells, Yoon et al. Fig. 2C at 48 h shows about **8, 9 and 18 autophagosomes per cell** in bafilomycin, bafilomycin plus trehalose and bafilomycin plus rapamycin, respectively. Panel digitization uses the 0/25 tick centres at y≈501/410, and the group means at y≈473/468/437, on the original 750 × 1132 raster. The caption states the comparison in the opposite direction. The actual bars and the results prose agree that rapamycin gives the greater increment. Fig. 2D and 2E show accompanying LAMP2 signal loss and greater Gal3 puncta, consistent with lysosomal injury or delayed clearance under the high-bath conditions. The primary rat-neuron result concerns changes in LC3-II and p62 under the stated exposures. A tandem reporter depends on acidification and the long inhibitor step can obscure kinetics. Treat the evidence as compatible with impaired late clearance in this model. Separate fusion, acidification and proteolysis in the proposed WWOX comparison. [Primary study and figures](https://doi.org/10.1038/cddis.2017.501) · [Original Fig. 2 raster](https://pmc-oa-opendata.s3.amazonaws.com/PMC5682667.1/cddis2017501f2.jpg)

In a separate mouse comparison at matched administered amount (n=4 per route), Fig. 4A at 30 min shows intraperitoneal about **390 mg/dL** and oral about **20 mg/dL** in serum. Interpolating from y≈224/54 for 0/500 mg/dL and y≈92/217 for the two endpoints gives **388 and 21 mg/dL**, or **11.3 and 0.6 mM** using molecular mass 342.3 g/mol. The oral signal is near the scale floor and uncertainty is large relative to the small estimate. A relative comparison to the **100 mM** culture bath highlights the route and compartment gap. This study used an enzyme-based measurement and gave systemic serum data. Intact parent in neural interstitial fluid and intracellular glucose competition require separate measurements. The later systemic trehalase-deficiency contrast describes low oral exposure even in knockout, so gut hydrolysis alone may not explain the route gap. [Mouse primary study, Figs. 4 and 6](https://doi.org/10.3389/fnut.2025.1580684) · [Original exposure figure](https://pmc-oa-opendata.s3.amazonaws.com/PMC12171462.1/fnut-12-1580684-g004.jpg)

**Next comparison.** Check the actual GLUT8 transport and rescue curves, an independent positive flux reporter in spinal cord, and LC–MS detection after a separately defined non-oral route. Compare pediatric MPS III single-arm feasibility and the adult randomized ALS intravenous formulation, keeping those outcomes and exposures distinct. The discriminating prediction remains faster degradation of a defined cargo at measured intact neural parent and matched glucose flux, while preserving ATP and evoked function. More puncta with slower degradation would favor a late block.

Replay the RNA comparison with `python3 -B flux_screen.py /home/desktop/legend-development/files /tmp/trehalose-wwox-replay`. Original rasters SHA-256: Yoon Fig. 2 `83f973c1e823caa43ad964c8b9927fc3dada07ac7b3f9cc7b4bca22b517510e4`, Yeh et al. Fig. 4 `782a2ddb2f547cd3fca6790ea1fd51b8284e20109bda552752461aff9d23db8a`. Pixel estimates are not measures of biological uncertainty.
