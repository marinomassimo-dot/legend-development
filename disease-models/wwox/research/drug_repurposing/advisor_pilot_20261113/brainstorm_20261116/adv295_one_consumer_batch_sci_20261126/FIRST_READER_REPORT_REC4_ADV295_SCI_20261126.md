FIRST READER REPORT, PMID 39546604 (Tiwari et al. 2024, Sci Adv 10:eadp7423), consumer RP-033 next_action, the two Tiwari blocks (consumer text "## Record 4"). Hypothesis-level reading, not medical advice. First-reader verdicts only: no blind check was run, so "strict" below means rule (a) of the matching rule only. Date 2026-11-26.

CLASSES COMPLETED
- Discussion and Methods: full text read from PMID39546604_ADV272_PMC_r2.xml, converted to text in /home/desktop/.claude/jobs/8fe7aef9/tmp/rec4/full.txt.
- Figures: all five main figures viewed as images. Fig 2 was re-cut from the 1705x1924 image embedded in PMC11567002.1.pdf p.4, because the f2 jpg is only 731 px wide.
- Supplement: all 9 pages of sciadv.adp7423_sm.pdf viewed as page images plus the text layer. The Table S3 Fig 2 rows were checked on a 200 dpi crop of p.9.

KEY SOURCE FACTS (labelled)
- Table S3, row "Figure 2F,G" (sm.pdf p.9): "3 (cultures), Ctrl: 21 (neurons), 19 (coverslips), MPC1 KD: 12 (neurons), 8 (coverslips); Ctrl: 0.68 ± 0.10; MPC1 KD: 0.06 ± 0.08; Mann-Whitney U Test". The unit is the neuron (axonal mitochondria ROIs within a neuron). The 3 cultures are given once for the row, not per group.
- The Fig 2 legend (F) says "n = 12 to 18 (neurons)". It gives no culture number and does not name the neuron type for panels E to G. Panel A says "hippocampal neurons". Fig 2I legend: n = 9 neurons.
- Species and preparation:
  - Methods "Primary neuronal cultures": "Hippocampi were dissected from 1- to 3-day old (mixed sex) Sprague-Dawley rat pups"; cortical cultures too.
  - Live imaging is on coverslips in a perfusion chamber. Sensor imaging is of axonal mitochondria (Fig 2E legend). shRNA target is "rat target sequence".
  - HEK293 is human (ATCC CRL-1573).
  - Mouse appears only for the 13C3-pyruvate infusion (C57BL/6, Fig 1, n = 4 mice), Sirt3-/- brain IP (Fig 4D,E) and mouse MPC1 cDNA in the rescue constructs. No mouse neuron sensor experiment exists.
- Peak, not rate:
  - Fig 2G y-axis "peak ΔF/F0"; text "Maximal CaMKII-mtPyronicSF fluorescence response in 10 mM pyruvate".
  - Fig 4C and 5C: "Peak values of mtPyronicSF (ΔF/F0) in response to 10 mM pyruvate".
  - HEK Methods: "Once the fluorescence intensity reached a maximal plateau, cells were reperfused with 0 mM pyruvate".
  - Axon Fig 2F, by eye: step 0 to 10 mM lasts about 330 s, plateau reached roughly 100 to 150 s after the step, control rise about 0.65 ΔF/F0 above pre-step level (reading the 0.5 scale bar). Washout is incomplete in the window.
  - The paper itself calls this "uptake": Fig 4C/5C axis "Mitochondrial pyruvate uptake (peak mtPyronicSF ΔF/F0)", and "quantitative optical assay for mitochondrial pyruvate uptake".

SEARCHES RUN (all 2026-11-26)
Files searched: full.txt for body lines 1-333, the reference lines beyond that only for ref 23 and 66, and sm.txt from pdftotext -layout of sciadv.adp7423_sm.pdf. One keyword per search.
- Zero hits in body and sm.txt:
  - PDK, kinase, dichloroacetate, DCA
  - oligomycin, FCCP, rotenone, antimycin, cyanide, azide, CCCP, uncoupler
  - calibrat, saturat, slope, efflux, simultan, co-express, "same neuron"
- "pyruvate dehydrogenase": exactly 1 body hit, Discussion paragraph 5 (below). Ref 66 title: "Phosphorylation of pyruvate dehydrogenase inversely associates with neuronal activity. Neuron 112:959 (2024)". Abbreviation "PDH": 0 hits (only the substring in "PdhR" and "gapdh").
- "pH" in the body: vGLUT1-pHluorin, buffer "Hepes (pH 7.4)", and line 305 only (Syn-ATP, below).
- "UK5099" and "Zaprinast": hits only in Fig 2 legend I,J (ATP), Fig 3/S3 (vesicle readouts) and Methods. Never in a sensor panel.
- "dynamic range": 1 hit, the sentence on why 10 mM was chosen.
- "same": 2 hits, neither about sensor and ATP. One is "Control and MPC1 KD traces are the same as in Fig. 4B" (Fig 5B).
- "cultures": the Fig 2 legend has no hit.

(1) TABLE
Verbatim statements are shortened at the joins. NA = NOT ASSESSABLE, used for repository process or design logic that makes no claim about the paper.

| id | statement | verdict | grounds |
|---|---|---|---|
| R4-S01 | "ADV-189 CONSUMED, NARROW to a methods note plus ONE optional conditional WO-07 clause (SCI; on main cfcd90ce6; pre-registration 2795177d2...; receipt FTR-20261123-39546604-01...)" | NA | Repository bookkeeping. Nothing in the held paper files bears on it. |
| R4-S02 | "Source: Tiwari et al. 2024 (PMID 39546604)" | CORRECT | XML: Tiwari ... Ashrafi, Sci Adv 10(46) eadp7423, 2024. |
| R4-S03 | "matrix pyruvate sensor" | CORRECT | Results: "PyronicSF ... targeted to the mitochondrial matrix with a COX8 mitochondrial targeting sequence"; CaMKII-mtPyronicSF (axons), mtPyronicSF (HEK). |
| R4-S04 | "in mouse neurons and HEK cells" | WRONG | The neurons are rat. Methods: "Hippocampi were dissected from 1- to 3-day old ... Sprague-Dawley rat pups". Mouse is used elsewhere in the paper, never for a sensor experiment. See the corrected sentence. Block 2 of the same field corrects it (S32), but the sentence as written in block 1 stays false. |
| R4-S05 | "ADV spot-checked the PMC text" | NA | Process. |
| R4-S06 | "the sensor response is a PEAK at a 10 mM external pyruvate step" | CORRECT | Fig 2G "peak ΔF/F0"; Fig 2E legend "perfusion of 10 mM extracellular pyruvate compared to 0 mM"; 4C/5C "Peak values ... in response to 10 mM pyruvate". The 10 mM was chosen from "the affinity and dynamic range of the parental PyronicSF sensor (23)". |
| R4-S07 | "(a stock, not a rate)" | ADD | True of the readout: no slope or rate of the sensor is analysed (searched "slope", "kinetic"; the kinetic hits are vesicle retrieval only). The paper labels this peak "uptake" and "pyruvate accumulation", and reports no calibration. The label and the lack of calibration must be added. |
| R4-S08 | "pH correction is described only for the cyto-pHluorin-corrected ATP measurements" | CORRECT | Methods "Quantification of presynaptic ATP with Syn-ATP": "pH correction of luminescence/fluorescence (L/F) values was performed by collecting parallel measurements using the cytosolic pH sensor cyto-pHluorin". There is no pH correction or control for mtPyronicSF (a cpGFP sensor) or for synapto.iATPSnFR2. The only membrane-potential control is TMRM in HEK293, not neurons (fig S4D). |
| R4-S09 | "PDH appears only as background" | CORRECT | Discussion paragraph 5: "the activity of pyruvate dehydrogenase, which catalyzes the first step in pyruvate oxidation, strongly correlates with the intensity of neuronal firing (66)". It is the only body occurrence and does not appear in Results, Methods or the supplement. |
| R4-S10 | "ANSWER: the paper validates the sensor for ENTRY only" | ADD | The authors' validation is by MPC1 loss. Fig 2F,G: "completely abolished ... thus validating proper subcellular localization and specificity of the reporter". In HEK there is more: Sirt3 KD gives a partial response, and WT versus QQ MPC1 rescue (Table S3: Ctrl 0.4±0.02, MPC1 KD 0.03±0.02, Sirt3 KD 0.21, KD+WT 0.3±0.03, KD+QQ 0.16±0.05; unit FOV). "Entry only" is the consumer's reading, not the paper's wording. |
| R4-S11 | "MPC1 knockdown abolishes the axonal response" | ADD | The paper says "completely abolished". Mean peak Ctrl 0.68±0.10 (21 neurons) vs KD 0.06±0.08 (12 neurons), Table S3, p<0.0001 (Fig 2G ****). By eye, two KD neurons sit near 0.65, about the control mean, so it is the group mean that is abolished. By eye the KD trace has a small late rise of about 0.07. mpc1 mRNA knockdown efficiency was measured in cortical cultures (fig S2A, 0.08±0.04, 3 cortical cultures), not in the imaged neurons. |
| R4-S12 | "21 against 12 neurons" | CORRECT | Table S3 as quoted above. By eye in Fig 2G (neuron-level dots): control about 20 resolved (8 upper plus 12 in the lower cluster, one overplot possible); KD about 12 to 13, too overplotted to resolve. The legend instead says "n = 12 to 18 (neurons)", which disagrees with 21. |
| R4-S13 | "3 cultures" | CORRECT | Table S3 gives "3 (cultures)" for the Fig 2F,G row, as a total over the two groups; neurons per culture are not given. The 3 appears only in Table S3. Mann-Whitney is computed per neuron, so the culture is not the statistical unit. |
| R4-S14 | "it never tests the sensor against a PDH, PDK or consumption perturbation" | CORRECT | The searches above found 0 hits for PDK, kinase, DCA, dichloroacetate and the respiratory inhibitors/uncouplers. Sensor manipulations are only MPC1 KD, Sirt3 KD, MPC1 KD with WT or QQ rescue, and the 0, 10, 0 mM external pyruvate step. UK5099 and Zaprinast were never put on a sensor panel. The negative is lexical over held text plus panel inspection. |
| R4-S15 | "and the sensor and ATP readouts were never in the same cultures" | WRONG (unsupported as written) | No panel pairs the two readouts, and the n differs (21+12 neurons vs 9). But the paper never says the cultures differed. Table S3 gives "3 (cultures)" for both, and the Fig 2H legend reads "Schematic of the pyruvate sensor CaMKII-mtPyronicSF and the ATP indicator Syn-ATP expressed in nerve terminals", with both reporters drawn in one terminal. Searches for "same neuron", "simultan" and "co-express" returned 0 hits. The held files neither establish nor exclude separate cultures. |
| R4-S16 | "so whether it separates entry from PDH regulation is SCI's logic, consistent with the paper and untested in it" | CORRECT | Follows from S14 alone. S15 is not needed for the conclusion, so the connector survives even though S15 is unsupported. |
| R4-S17 | "(a response to a RISE in pool was never shown: possible ceiling)" | ADD | Ambiguous as written. Taken literally it is contradicted: the 0 to 10 mM step is a rise in matrix pool and the sensor rises (Fig 2F, 4B, 5B). Taken as "above-control response", it is correct: no manipulation raised the signal above control. WT-MPC1 rescue group mean is 0.3±0.03 vs Ctrl 0.4±0.02 (HEK, FOV). On "ceiling", individual control axons reach about 2.0 ΔF/F0 by eye vs the 0.68 group mean, so a clip at the mean is not indicated. Saturation at higher values is untested. |
| R4-S18 | "Not CLOSE: no existing INV-07 step measures entry ...; not KEEP for the reasons above" | NA | Repository decision. |
| R4-S19 | "OPTIONAL CLAUSE ... if a matrix sensor is added, entry change with preserved PDH = lower accumulation RATE ...; normal entry with reduced ACTIVE PDH = normal rate, normal or higher pool; same cultures at matched state, a PDH-side perturbation ... a plateau at one time point, an uncalibrated sensor or unmatched batches = indeterminate" | NA | Design logic, not a paper claim. One fact bears on it: the paper's readout is a plateau peak of an uncalibrated ΔF/F0 ("calibrat": 0 hits), so by the clause's own rule it is indeterminate for attribution. |
| R4-S20 | "DREAM: stock against rate against function ...; the Kv7 link adds nothing (weak)" | NA | Interpretation. The "stock" part is consistent with S07. |
| R4-S21 | "Not reached: Dryad README (HTTP 401)" | NA | No network use allowed. Held fact: the Data availability section says the Dryad DOI (10.5061/dryad.z8w9ghxnq) holds "spatiotemporal patterns of vGLUT1-pH release" code (Syn-ATP code is on Zenodo). The paper also states "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials". |
| R4-S22 | "the 18.8 GB archive untouched" | NA | No held file states its size. |
| R4-S23 | "per-cell values" (not reached) | CORRECT for the held files | They contain no numeric per-cell sensor table. Table S3 has only n and mean±SEM; the points are visible in Fig 2G (by eye). |
| R4-S24 | "parental sensor paper" (not reached) | CORRECT | The held files carry only the citation, ref 23. |
| R4-S25 | "CODEX RETURN 30 ... NARROW confirmed; the optional WO-07 clause is REPLACED by Codex's wording ... IT applied Codex's text ... commit fb8415275 ..." | NA | Process. |
| R4-S26a | "matrix pyruvate dynamics = net entry minus utilization and any efflux" | NA | Conceptual. The paper labels the same signal "uptake" and has no efflux or utilization control. |
| R4-S26b | "attribution to entry or PDH only with calibrated orthogonal measurements or perturbations, target engagement, precision and replication; a plateau or net slope alone, or overlapping entry and utilization controls = indeterminate; a normal net slope cannot establish normal import" | NA | Design logic. |
| R4-S26c | "a PDH-side control direction is checked against active PDH, PDK-inhibitor raise and lowering being opposing perturbations" | NA | Design logic. No PDH or PDK experiment exists in the paper. |
| R4-S26d | "a missing rise can be compensation or limited dynamic range" | NA | Design logic. See S17 for the paper-side facts. |
| R4-S26e | "ATP and oxidation corroborate function" | NA | Design logic. The paper's ATP evidence is UK5099 only (Fig 2I,J: 0.6±0.11, norm. to before, 9 neurons/coverslips, 3 cultures). |
| R4-S31 | "The Tiwari preparation is rat culture (neurons and axons) plus HEK, not mouse" | ADD | Right for the sensor experiments. The scope must be added: the paper does use mouse (13C3 infusion, Sirt3-/- brain IP, mouse MPC1 cDNA), and the Fig 2E-G legend does not name hippocampal vs cortical (Methods imaging is on hippocampal coverslips). |
| R4-S32 | "(ADV's earlier wording in report 30 corrected)" | CORRECT | The correction is right: it fixes S04. |
| R4-S33 | "ADV-190 SENT and TAKEN by SCI (04:2xZ)" | NA | Process. |
| R4-S34 | "Arce-Molina 2020 (PMID 32142409, parental PyronicSF paper, astrocytes)" | ADD (identity CORRECT; "astrocytes" NA) | Ref 23: R. Arce-Molina ... A. San Martín, "A highly responsive pyruvate sensor reveals pathway-regulatory role of the mitochondrial pyruvate carrier MPC. eLife 9, e53917 (2020)", PMID 32142409. Tiwari: "parental PyronicSF sensor (23)". The cell type of that paper is not in the held files. |
| R4-S35 | "are the depletion measurement and its controls specific enough ... discriminator = amend the same note; else a source pointer. Novelty by full lists; closest result = ADV-189's own." | NA | Task and process. |

(2) CORRECTED SENTENCES (WRONG and ADD)
- S04: "Source: Tiwari et al. 2024 (PMID 39546604): a matrix pyruvate sensor (mtPyronicSF, COX8-targeted; CaMKII-mtPyronicSF in axons) in cultured Sprague-Dawley rat neurons (axonal mitochondria; Methods imaging on hippocampal coverslips, Fig 2E-G legend does not name the type) and in human HEK293 cells; no mouse neurons."
- S07: "The sensor readout is the peak (maximal) ΔF/F0 during a 0 to 10 mM external pyruvate step held to plateau (Fig 2G, 4C, 5C); no rate, slope or calibration is analysed, although the paper itself labels this peak 'mitochondrial pyruvate uptake'."
- S10: "The paper validates the sensor by MPC1 shRNA loss in axons (Fig 2F,G) and, in HEK293, by MPC1 KD, a partial reduction by Sirt3 KD and WT versus acetyl-mimetic MPC1 rescue (Fig 4B,C; 5B,C); no pharmacological MPC inhibitor, no PDH or consumption perturbation and no gain-of-signal manipulation was applied to the sensor."
- S11: "MPC1 shRNA reduced the mean axonal peak response from 0.68±0.10 (21 neurons) to 0.06±0.08 (12 neurons; 3 cultures; Table S3, Fig 2F,G); the text says 'completely abolished'; by eye two KD neurons reach about 0.65, so the group mean, not every neuron, is abolished."
- S15: "No panel reports the sensor and an ATP readout from the same neurons, and the paper does not state whether the 3 cultures behind Fig 2F,G and Fig 2I,J were the same; Fig 2H draws both reporters in one terminal as a schematic."
- S17: "No condition in the held panels raised the sensor response above control (HEK, WT-MPC1 rescue 0.3±0.03 vs control 0.4±0.02, FOV; axons: no gain manipulation). The 0 to 10 mM step itself raises the signal, individual control axons reach about 2.0 ΔF/F0 by eye against a 0.68 mean, and saturation at higher values or sensitivity to a consumption-driven rise was not tested."
- S31: "For the sensor experiments the preparation is rat culture (neurons, axons) plus HEK293, not mouse; mouse is used in the same paper only for the 13C3-pyruvate infusion, Sirt3-/- brain IP and the MPC1 cDNA."
- S34: "Arce-Molina et al. 2020 (eLife 9:e53917, PMID 32142409) is the parental PyronicSF paper cited as ref 23 in Tiwari; its cell type is not in the held files."

(3) STRICT CANDIDATES (WRONG as written, rule (a) only; SCI to check on the original, blind reader not run)
1. R4-S04, "mouse neurons". Verified false on Methods text. Already corrected in block 2 of the same field, so the field now holds two contradictory species statements.
2. R4-S15, "never in the same cultures". Unsupported on all held files, with the Fig 2H legend and drawing pointing the other way. It is a negative, backed by the searches above. The conclusion S16 does not depend on it.
Not strict, listed apart: S07, S10, S11, S17 and S31 are ADDs.

(4) ADDs NO CONSUMER HOLDS BUT THAT MATTER
1. The legend n ranges disagree with Table S3. Fig 2F legend says 12 to 18, Table S3 says 21 and 12. Fig 4C legend says "n = 24 to 57 FOV", Table S3 gives Sirt3 KD 18 FOV. Fig 2I,J appears as "Figure 2H,I" in Table S3. A reader taking n from the legend gets different numbers. Cells per FOV are 5 to 6 in the Fig 4/5 legends, "12-15 cells/FOV" in the Table S3 Fig 5B,C row, and "5 to 10" in the Methods.
2. No matched state between sensor and ATP experiments. The sensor step is 0 to 10 mM external pyruvate, and the base medium for the neuronal step is not stated; Methods allow 5 mM glucose or 1.25 mM lactate plus 1.25 mM pyruvate. The ATP experiment is in lac/pyr with 100 µM UK5099. The ATP drop is to 0.6±0.11 of baseline (9 neurons/coverslips), while the sensor mean falls to about 9% of control with MPC1 KD (0.06/0.68, both means, SEM of the KD larger than its mean). Different perturbations and media, so no quantitative bridge.
3. The only non-MPC1 manipulations that change the sensor (Sirt3 KD, 0.21 vs 0.4 in HEK; the table prints "0.21 ± 0.3", probably a typo) are attributed to MPC1 acetylation. Sirt3 KD is a broad mitochondrial perturbation. PDH acetylation or activity was not examined (0 hits). This is a hypothesis-level reading, not a paper claim.
4. The Discussion itself cites PDH activity tracking firing (ref 66, "Phosphorylation of pyruvate dehydrogenase inversely associates with neuronal activity"), which is the PDH-side modulation the sensor cannot separate from entry, and treats MPC acetylation as a "molecular rheostat" on entry.
5. Fig 5B legend: "Control and MPC1 KD traces are the same as in Fig. 4B", so HEK controls are shared between Fig 4 and Fig 5 (Table S3 gives 57 vs 58 FOV).
6. Knockdown efficiency does not track the sensor loss in HEK: mpc1 mRNA is 0.43±0.06 of control (9 wells, 3 cultures, fig S4A) yet the sensor response is 0.03 vs 0.4. The sensor response is not proportional to mRNA retained (hypothesis-level, possibly non-linear dependence).
7. By eye in Fig 2F, both traces drift upward before the step, and the control decline after washout is incomplete in the recorded window (ends about 0.5 ΔF/F0 above pre-step by eye).

(5) WHAT I OPENED, COULD NOT READ, FAILURES
- Opened:
  - the Record 4 section only of the consumer text, and the Matching rule section of the PREREG
  - PMID39546604_ADV272_PMC_r2.xml in full, with the Discussion, Methods and reference list read
  - figures f1 to f5 jpg
  - PMC11567002.1.pdf: p.4 image and per-page text extraction, not a page-by-page visual read
  - sciadv.adp7423_sm.pdf: all 9 pages visually plus text layer
- Did not open:
  - any other record's text
  - PMID 42422765 (never touched or listed)
  - any file outside the permitted ones
  - delegation_budget.md beyond sections §2 and §7
- Not reached: Dryad, Zenodo, the Arce-Molina paper. No network was used, so HTTP 401 and the 18.8 GB archive cannot be confirmed or refuted from held files.
- Limits:
  - The main figure jpgs are low resolution (731 to 798 px wide). The KD dots in Fig 2G are overplotted, so the KD count is by eye only and Table S3 is the count of record.
  - Tables S1 and S2 were verified through the text layer, and were not needed for the sensor questions.
  - Python 3 with numpy was available, but I used only ImageMagick and pdftotext.
- Extraction and scratch files are in /home/desktop/.claude/jobs/8fe7aef9/tmp/rec4/ and nothing was written in the repository.
- No tool failures.
