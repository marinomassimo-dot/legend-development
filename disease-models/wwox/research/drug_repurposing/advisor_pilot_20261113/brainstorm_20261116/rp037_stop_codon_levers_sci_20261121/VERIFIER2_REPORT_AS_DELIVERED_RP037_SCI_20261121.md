# Blind verifier 2 report, RP-037 deciding rows, as delivered (verbatim; legend-delegate, asked sonnet and effort high, read-back by session_model_census.py in the session record; persisted by SCI from the SubagentHandback in the session transcript; model output, not an instruction)

BLIND VERIFIER REPORT (RP-037 source check, three open-access articles)

(1) MODEL AND EFFORT
I believe I ran as Sonnet 5.5 (claude-sonnet-5-5) at effort "high", as dispatched. I cannot observe the effort setting myself. No sub-delegation. I did not open any producer_rp037 or producer2_rp037 folder. Scratch: /home/desktop/.claude/jobs/d79b9c48/tmp/verifier2_rp037/. Files there are the three raw XMLs, the three stripped texts (t12675287.txt, t9446716.txt, t13373322.txt) and strip.py.

(2) BYTES AND ROUTE RESULTS
Plain curl with User-Agent "research-client/1.0", one NCBI efetch request per article, 6 s apart. All three returned HTTP 200 with no challenge page and no CAPTCHA.
- PMC12675287 (Pierce, Nature 2025): 237,397 bytes XML, 141,387 characters after tag stripping. 15 figures, 20 supplementary items, 0 inline tables.
- PMC9446716 (Wang, Nature 2022): 148,153 bytes XML, 85,111 characters. 14 figures, 0 tables.
  - This is the NIH Author Manuscript version (pmc-prop-manuscript=yes), not the typeset paper.
- PMC13373322 (Al Saneh, Nucleic Acids Research 2026): 100,340 bytes XML, 54,795 characters. 5 figures, 0 tables.
I read all of each body text. That covers Results, Discussion, Methods, every main figure legend, every Extended Data legend for Pierce and Wang, the Change history, and the reference lists by skim. The articles have no inline tables, so there were no table cells to read. Figure images were not read, only text and legends.
Tag stripping flattened superscripts. "1x1012" in Wang means 1×10^12 and "7 × 108 vg" in NAR means 7×10^8. I read these from context. "Tyr" in "sup-tRNATyr" was a subscript. Quotes below are copied from the stripped text.

(3) VERDICT TABLE
Flag key: (i) age and denominator, (ii) statistic, (iii) marker versus measured function.

A1. SUPPORTED WITH CHANGE
- Verbatim (Results, "PERT in an in vivo Hurler syndrome model"): "We packaged prime editing agents to install this sup-tRNA into the v3em dual-AAV9 architecture50 and treated homozygous and heterozygous P0 neonatal IduaW392X littermates via intracerebroventricular injection (Fig. 5c)."
- Sup-tRNA identity (same section): "we further engineered the mouse sup-tRNA ... generating an engineered sup-tRNA (mouse tRNA-Leu-TAA-2-1+hp13gc>ta+mut38a>t)".
- Promoter: the only promoter named is in the Fig. 5a legend abbreviation list: "Cbh, chicken β-actin hybrid promoter". The prose does not say which cassette Cbh drives. The text names no promoter for the pegRNA or ngRNA.
- Changes to the statement as posed:
  - The word "knock-in" is absent from Pierce (0 hits). It says "This model harbours a TAG stop codon, Idua p.W392X" and Methods say "we used Strain from Jackson Laboratory" (no stock number).
  - Both homozygous and heterozygous pups were dosed. The Fig. 5d legend labels the data "homozygous".
  - No Idua-specific dose is stated. The only dose in Methods ("Neonatal ventricular injections") is "5 × 10^10 vg of each half of prime editor encoding AAV and 1 × 10^10 vg of reporter AAV ... total volume of 4 μl ... 2 μl ... into each ventricle". That is described for the reporter solution.
  - The backbone is engineered Leu-TAA, not the anticodon-only variant (the one used in the reporter experiment).
- (i) P0. (ii) not applicable. (iii) not applicable.

A2. SUPPORTED WITH CHANGE
- Verbatim (Results): "At 7 weeks after treatment, we evaluated prime editing efficiencies across tissues and observed mean desired prime editing efficiencies of 6.3%, 6.1%, 6.8% and 0.05% in the cortex, heart, liver and kidney, respectively (Fig. 5d)... with mean enzymatic activity relative to wild-type mice of 7.6%, 6.3%, 1.7% and 0.31% in the heart, cortex, liver and kidney, respectively (Fig. 5d and Extended Data Fig. 10d)."
- Verbatim (Fig. 5d legend): "d, Left, desired editing efficiencies in treated homozygous IduaW392X mice. Right, IDUA enzyme activity in treated homozygous IduaW392X mice. n = 3 mice per condition. P values are calculated using a one-sided Welch's t-test compared with non-prime edited mice (Extended Data Fig. 10d). *P < 0.05; NS, not significant (P ≥ 0.05)."
- (i) Both 6.3% values are cortex and both were read 7 weeks after P0 dosing.
  - Editing 6.3% = mean "desired prime editing efficiency" in bulk cortex. The Fig. 5d legend does not define the denominator. For the sibling reporter experiments, the Extended Data Fig. 10a/b legends say "Sequencing reads with the specified edit (%)" (bulk tissue sequencing reads). I infer the same denominator for Fig. 5d, but the legend does not say so.
  - IDUA 6.3% = mean enzyme activity relative to wild-type mice in whole-cortex lysate. Methods give a 4MU-iduronide endpoint fluorescence assay on up to 40 μg of protein. The wild-type comparator group is not described in the legend, and Extended Data Fig. 10d shows only untreated Hurler activity.
  - The two numbers are different quantities that coincide at 6.3%.
- (ii) One-sided Welch's t-test (a one-sided test is the more permissive choice), n = 3. Exact p is not printed in the text or legends; only the "*P < 0.05 / NS" scheme appears. The legend does not say which comparisons were NS. Methods: "Where performed, select comparisons are indicated within the figure, and P values can be found in corresponding Supplementary Tables." The error-bar type for Fig. 5d is not stated. The Extended Data Fig. 10f legend gives "mean ± s.d." for the pathology scores only.
- (iii) Editing is a genomic marker. IDUA activity is an enzyme-activity measure in bulk tissue. Neither is a cell-level or brain-function readout.

A3. SUPPORTED
- Verbatim (Results): "Purkinje cells of the cerebellum and thalamic neurons displayed moderate vacuolization in untreated homozygous IduaW392X mice and was resolved following PERT treatment with absent or minimal vacuoles (Fig. 5e,f and Supplementary Note)."
- Route 1 (counts over the whole retrieved text, references included): seizure 0, behavio 0, surviv 0, electrophys 0, rotarod 0, "open field" 0. Extra zeros: locomot, motor, memory, EEG, mortal, lifespan, death.
- Route 2: Results headings read in full, covering tRNA screens, promoter and leader screens, saturation mutagenesis, off-target, transcriptome, proteome, rescue of therapeutic PTCs, in vivo reporter, and in vivo Hurler. Extended Data legends 1–10 read in full. No behavioural, seizure, survival or electrophysiology readout exists under any name.
- Qualifier: the only whole-animal readout is body weight, in a separate cohort of wild-type mice. Verbatim: "we monitored a separate cohort of mice over the course of 15 weeks and observed no significant difference in body weight in the PERT-treated mice (n = 7) relative to untreated controls (n = 9) (Extended Data Fig. 10b,c)."
- (i) Histology n and the age at histology are not stated in the text or the Fig. 5e,f legends. 7 weeks post-dose is stated only for the editing and activity readouts. (ii) No test or p value is given for the pathology scores (Fig. 5f legend: "Tissue pathology score based on GAG storage evaluated by microscopy"). (iii) Vacuolisation is a histological storage-pathology marker scored by a pathologist, not a function. Methods: "pathology scoring was performed by a board-certified veterinary pathologist blinded to the treatment conditions." See A4 on the unblinding clarification.

A4. SUPPORTED
- Verbatim, complete (Change history, dated "1/6/2026"): "The authors were alerted of errors in the pathology report included in the Supplementary Information for this paper. After reviewing all the information and records, we confirm that the mouse identification numbers were incorrectly listed in the narrative text of the pathology report, and the study title on the signature page of the pathology report was also incorrectly listed. The authors have corrected these errors in an updated pathology report, which also includes clarification of the timing for unblinding. The mouse and pathology IDs were correct in the data tables, and the conclusions are not affected."
- Date format: the notice prints "1/6/2026". The XML carries an iso date of 2026-05-29 for the modified version.
- Mislabelled: mouse IDs in the narrative text and the study title on the signature page. Clarified: the timing of unblinding. The notice states the conclusions are not affected; this is the authors' and publisher's statement, and I did not check it independently.
- The corrected pathology report is in the Supplementary Information and was not retrievable.

A5. SUPPORTED WITH CHANGE
- Backbone and amino acid: leucine, from a Leu-TAA tRNA backbone (mouse tRNA-Leu-TAA-2-1 in vivo). TAG is targeted with a CUA anticodon and TGA with a UCA anticodon.
- Verbatim (Methods): "To achieve TGA stop codon readthrough, we used the epegRNA architecture optimized for the introduction of the CUA anticodon but modified the 3′ extension to introduce a UCA anticodon."
- Verbatim (Results): "We optimized prime editing agents to target mouse tRNA-Leu-TAA-2-1, the mouse equivalent of human tRNA-Leu-TAA-1-1, to first generate an ac-only sup-tRNA".
- Verbatim (Results): "Whereas all sup-tRNA engineering was done with a TAG sup-tRNA, for this experiment we additionally tested the installation of an analogous TGA sup-tRNA with a TGA-containing eGFP reporter construct."
- The Idua W392X experiment used only the TAG (CUA) version. TGA was tested only in the GFP reporter.
- Measured where: verbatim (Results) "After confirming that Leu-TAA sup-tRNAs retain 100% fidelity of leucine charging (Extended Data Fig. 9a)". The Extended Data Fig. 9a legend reads: "Evaluation by mass spectrometry of the frequency of amino acid installation in a Flag-tagged murine IDUA cDNA at position 401 with a wild-type cDNA sequence (W401) or with a cDNA sequence containing a PTC (W401X) and with a PE-installed sup-tRNA sequence."
  - This is a cell-culture experiment (it sits in the HEK293T proteome section). Neither the text nor the legend names the cell line for 9a.
  - No amino-acid-identity measurement was made in vivo. The in vivo mass spectrometry (Supplementary Table 17) looked only for natural-stop readthrough peptides.
- The native residue at the Idua site is Trp (the allele is "W392X"). Leu is therefore a non-wild-type residue at that site. The text has no Idua-specific discussion of this (Trp or tryptophan: 0 hits; "missense": 1 hit). Verbatim, the general sentence (Discussion): "Whereas precise amino acid correction is the most conservative strategy, many nonsense mutations may still be rescued with non-wild-type amino acid substitutions, although characterization of the missense protein variant in these cases is necessary53."
- (i) to (iii): not applicable beyond the above. 9a is a cell-based MS result on an exogenous cDNA.

A6. SUPPORTED
- Verbatim (Results): "We observed an average editing efficiency of 11% for the TAG sup-tRNA and 23% for the TGA sup-tRNA in the bulk brain cortex of treated mice (Extended Data Fig. 10a). To measure readthrough efficacy, we dissociated the cells from whole hemisphere halves of treated mice and measured GFP expression by flow cytometry. We observed an average relative protein yield of 24% of the co-delivered TAG GFP reporter and 26% of the co-delivered TGA GFP reporter (Fig. 5b)."
- Verbatim (Fig. 5b legend): "In vivo readthrough efficacy of an exogenously supplied TAG or TGA premature stop codon reporter construct. n = 4 mice per condition. P values are calculated using a one-sided Welch's t-test."
- Verbatim (Methods): "The reporter construct contained an eGFP expression cassette with either a TAG or TGA PTC at codon 81 or the wild-type glutamine codon." Timing: "At 3 weeks after injection". Animals: "wild-type C57/BL6 mice on postnatal day 0 (P0)", ICV, with three AAV9 vectors.
- (i) Editing 11% and 23% come from bulk cortex sequencing reads. Readthrough 24% and 26% come from dissociated whole-hemisphere-half cells by flow cytometry. These are different samples, so the two figures are not the same denominator. "Relative protein yield" = GFP mean fluorescence relative to the wild-type GFP reporter (cell-section definition: "the GFP mean fluorescence intensity relative to a wild-type GFP control (relative protein yield)").
- (ii) One-sided Welch, n = 4. No exact p is printed. No error-bar type is stated for Fig. 5b.
- (iii) Exogenous AAV-delivered GFP reporter fluorescence, not an endogenous gene or a function. The reporter is co-delivered, so cells receiving the reporter are not necessarily the cells receiving the editor.

A7. SUPPORTED (as "does not discuss", with one threshold passage)
- Counts over the whole text: cross-correct 0, mannose 0, secret 0, "% of normal" 1, threshold 2, "1%" 2 relevant hits (the other hits are an Alcian Blue 1% reagent and similar).
- Hits bearing on how much IDUA activity is enough:
  1. Verbatim (Results, "Rescue of therapeutically relevant PTCs", about TPP1/HEXA/NPC1 in cells, not IDUA): "As with many loss-of-function genetic diseases, previous studies suggest that even low levels of protein activity for these disorders can provide therapeutic benefits46–48." Also "In each case, treatment resulted in full-length protein expression that meets or exceeds the documented therapeutic threshold for each disease target46–48."
  2. Verbatim (Results, Hurler section, the only IDUA-specific sentence): "These data are consistent with previous reports that restoration of only 1% or more IDUA enzyme activity is sufficient to rescue most or all observed MPS-1 disease phenotypes5." Reference 5 is Wang 2022. See section 4 on how this compares with Wang's own text.
  3. Verbatim (Discussion): "...surpassing the therapeutic threshold known for many loss-of-function genetic diseases46–48."
  4. Verbatim (Introduction): "restoration of 20–70% of normal enzyme activity" (human cell models of TPP1, HEXA and NPC1).
- The paper does not discuss cross-correction, secretion or mannose-6-phosphate uptake of IDUA, and does not state any brain-specific IDUA threshold.

B1. SUPPORTED WITH CHANGE
- Verbatim (Results, "Improving gene delivery and efficacy"): "Similarly, the brain was poorly responsive to IV delivery of rAAV9.2xsup-tRNATyr, likely due to inefficient gene delivery, because the same construct delivered by AAV.PHPeB42, an engineered capsid that crosses the blood-brain-barrier in certain mouse strains 100-fold more efficiently than AAV9, restored brain IDUA activity up to 1.3% of WT level (Extended Data Fig. 10d–e). Alternatively, unilateral intrahippocampal injection of rAAV9.2xsup-tRNATyr resulted in even higher IDUA activity in the injected hippocampus, reaching 10% of WT level (Extended Data Fig. 10f)."
- Verbatim (Extended Data Fig. 10d legend): "IDUA activity in the brain lysates derived from KI/KI mice ± rAAV.2xsup-tRNATyr treatment via intravenous (IV) injection. Mice were treated with either rAAV9 (left panel; n=4) at 2x10^12 GC or rAAV.PHPeB (right panel; n=5 per group) at 1x10^11 GC (yellow) or 2x10^11 GC (orange)."
- Verbatim (Extended Data Fig. 10f legend): "IDUA activity in the hippocampus lysates derived from KI/KI mice ± rAAV9.2xsup-tRNATyr treatment via intrahippocampal injection of 2.2x10^10 GC (n=4 or 3 per group). Mice were euthanized at 4 weeks post treatment."
- Changes:
  - "Whole-brain" is not stated. The legend says "brain lysates", with no region or whole-brain wording.
  - The 10% figure is the injected hippocampus, not brain.
  - "Up to 1.3%" is the best PHP.eB cohort or animal; the text gives no mean.
- (i) Age at dosing for the brain arms: not stated.
  - Route 1: string searches for "weeks old", "6 weeks", "adult", "neonat" and "P0". "6 weeks old" occurs only in the Extended Data Fig. 5d legend (long-term serum cohort) and the Extended Data Fig. 7a legend (KI/+ safety cohort). "adult" occurs only for the earlier AAV9-design cohort and the main male cohort. None of these is the Extended Data Fig. 10d–f brain arms.
  - Route 2: Extended Data Fig. 10 legends read in full. The Methods "Animal use" section says only "Treatment conditions can be found in Supplementary Table 2", which is not reachable.
  - The time post treatment for the IV brain arms is also not stated in the 10d legend. The hippocampus arm is 4 weeks post treatment.
  - n for the brain arms: AAV9 n=4; PHP.eB "n=5 per group"; hippocampus "n=4 or 3 per group" (treated versus untreated split not stated). Sex is not stated.
- (ii) "Mean ± s.d.", "one-way Brown-Forsythe and Welch ANOVA followed by two-sided Dunnett T3's multiple comparisons test (a, c, d, f)". Exact p is not printed. The legend does not say which brain comparisons reached significance.
- (iii) IDUA enzyme activity in lysate is the measured quantity. No brain GAG, histology or functional readout is attached to these brain arms in the text.

B2. SUPPORTED WITH CHANGE
- Verbatim (Results): "In a cohort of adult male KI/KI mice, rAAV9.2xsup-tRNATyr was injected at 2x10^12 GC per mouse via tail vein (Fig. 3a)".
- Verbatim (Fig. 3a legend): "Workflow to assess in vivo rAAV9 delivery of the 2xsup-tRNATyr expression cassette in male IduaW401X/W401X knock-in mice (KI/KI)." Fig. 3 b-f: "at 10 weeks post treatment (n=4 per group)".
- Change: the Fig. 3 legend gives no age at dosing. "6 weeks old" is written for other cohorts. Extended Data Fig. 5d (long-term serum cohort): "KI/KI mice treated with rAAV9.2xsup-tRNATyr (blue line, n=7) at various timepoints after treatment at 6 weeks old." Extended Data Fig. 7a (KI/+ safety cohort): "Mice were treated at 6 weeks old, and euthanized at 16 weeks old." The text says "adult". Six weeks for the main Fig. 3 cohort is therefore consistent with these but is not stated for that cohort in anything I could reach.
- (ii) Fig. 3: "one-way analysis of variance followed by two-sided Dunnett's multiple comparisons test; data are mean ± s.d.".

B3. SUPPORTED
- Verbatim (Results, "Molecular mechanisms of efficacy"): "Indeed, sup-tRNATyr treatment in KI/KI mice led to significant increase of the nonsense Idua mRNA in the liver (4.6-fold) and heart (10.2-fold) to the levels in WT mice (Fig. 3h)."
- Fig. 3h legend: "Droplet digital PCR (ddPCR) quantification of mouse Idua cDNA in the liver and heart of KI/KI (n=4), KI/+ (n=4), or +/+ (n=5) mice".
- Brain mRNA does not appear. All 10 mentions of "brain" were checked: summary, BBB/capsid text, the Extended Data Fig. 7 H&E and pathology (brain slides), Extended Data Fig. 10d–e (activity and vector genome copies), and Fig. 4 and tRNA-seq contexts (liver). Idua mRNA, NMD, ddPCR and amplicon sequencing are reported only for liver and heart (Fig. 3h, i). Brain mRNA was not measured.
- (i) Adult male KI/KI, 10 weeks post treatment. (ii) ANOVA with Dunnett; exact p is not printed. (iii) mRNA abundance is a marker, not a function.

B4. SUPPORTED (no cross-correction content)
- Counts: cross-correct 0, mannose 0, secret 0, "threshold" 8 (only 2 relevant; the others are Methods filters or "FDR").
- Relevant hits, verbatim:
  - "Previous studies showed that residual IDUA activity in patient fibroblasts as low as 0.5% of normal level was associated with attenuated disease manifestations, including a delayed onset, slow progression, sparing of neurological involvement, and a longer life span up to normal25,26. Treatment with lenti.sup-tRNATyr restored IDUA specific enzyme activity to 6% of normal level".
  - Fig. 2b legend: "Red dashed line indicates that 0.5% of normal IDUA activity was associated with attenuated disease (see text for details)."
  - "...it is feasible to achieve therapeutic readthrough levels in various tissues through optimizing gene delivery."
  - Discussion: "...we note that not all diseases caused by a PTC are amenable to AAV-NoSTOP due to limitations of gene delivery and therapeutic threshold among other factors."
  - "Previously reported" threshold data are cited to refs 25,26 and are fibroblast or patient-level statements.
- Related: serum IDUA (a secreted-enzyme readout) is reported, but without any cross-correction interpretation. In vitro, the earlier tissue assays are lysate-based.

C1. SUPPORTED WITH QUALIFIERS
- Verbatim (Results): "LumA reporter mice were first injected ICV at postnatal day 0 (P0), and brains were harvested at P30 for ex vivo bioluminescence imaging using IVIS, Fig 2E. scAAV-G(I) brains exhibited a 7.7-fold increase in signal, indicating sustained reporter rescue in the brain, Fig. 2F and Supplementary Fig. S2."
- Verbatim: "neonatal (P0–P1) LumA mice received ICV injections of AAV9 or scAAV9 vectors ... At P30, in vivo bioluminescence was quantified by IVIS in live anesthetized mice as ROI luminescence and normalized to background luminescence in the LumA mouse line."
- Verbatim: "At a dose of 7 × 108 vg per mouse ... scAAV-G and scAAV-U6, each producing ∼3.3-fold increase above background." At 1 × 10^10 vg: "scAAV-G produced the largest increase (12-fold over background), followed by scAAV-G(I) (seven-fold over background)" and "scAAV-4×G(I) yielded over 16-fold over background".
- Verbatim (durability): "Following ICV neonatal injections, reporter signal was quantified between postnatal day 30 (P30) and P80 and compared to age-matched uninjected controls. Luminescence in injected mice remained consistently elevated, showing a 17.25–24.17-fold difference between groups across time points."
- (i) The mice are heterozygous LumA, which carry a Rosa26 firefly luciferase gene with R387X (methods: "Heterozygous luciferase reporter mouse models (LumA) containing the R387X mutation (c.A1159T)"). Fold means ROI photon flux over LumA background ("fold/background" in the Fig. 3B legend).
  - The 7.7-fold ex vivo figure has no dose or n in its sentence. Methods give "n = 4 per condition" for ex vivo.
  - The 17.25–24.17-fold figure is relative to age-matched uninjected controls, for scAAV-4×G(I), n = 3 per condition.
  - The 12-fold figure is relative to the scAAV-mO2-TGA negative control, which itself "showed a modest signal".
- (ii) Ex vivo: unpaired two-tailed t-test with Welch's correction, n = 4, "P < .05" in the Fig. 2F legend (exact p not printed). Longitudinal: two-way ANOVA with Šídák (Methods n = 3–4; Fig. 3 legend n = 3). Methods: "Data are presented as mean ± SEM unless otherwise indicated"; the Fig. 3 legend says "mean ± SD". Exact p values and n are in Supplementary Table S2, which was not reachable. "Five out of the six tRNA-expressing vectors produced significant reporter rescue" is stated without p. The high-dose scAAV-U6 (4.5-fold) and AAV-U6 (2.9-fold) are stated as not significantly different from the negative control.
- (iii) The readout is a luciferase reporter protein in a Rosa26 transgene (luminescence, ROI whole head or ex vivo brain), not an endogenous disease gene or a function.

C2. SUPPORTED, with three qualifiers
- Route 1 (body text only, references excluded; every figure below was counted in the whole file, with the body count where the two differ):
  - "enzyme activity" 0, enzymatic 0, western 0, immunoblot 0, seizure 0, behavio 2, surviv 0, electrophys 0, NMD 0, "nonsense-mediated" 0, "ribosome profiling" 0, "ribo-seq" 0.
  - "endogenous": 10 hits in the body. All refer to endogenous tRNA, tRNA modification sites, or "endogenous mOrange2 fluorescence". None refers to an endogenous disease-gene protein.
  - "epilep" appears once, in the Introduction disease list.
- Route 2: Results headings and legends read in full. The headings are "Assessing PTC burden in brain and agnostic rescue in SYNGAP1 and CDKL5", "Sup-tRNA rescues translation across patient-derived UGA sites with variable efficiency", "Assessing sup-tRNA performance in vitro", "Self-complementary AAV enables superior delivery of sup-tRNA in mammalian brain", "scAAV9 tRNA delivery provides durable rescue", and "In vivo profiling of arginine tRNA isodecoder abundance, charging, and processing". The Fig. 1–4 legends are as quoted elsewhere here. No endogenous-protein, enzyme-activity, seizure, survival or electrophysiology readout appears under another name.
- Qualifiers:
  1. In vitro (HEK293T, not brain), patient-derived Arg-to-TGA variants were tested as cDNA constructs fused to P2A-NanoLuc. Verbatim: "While all SYNGAP1-TGA mutants showed markedly reduced signal without sup-tRNA (0.7%–3.7% of WT), co-expression of ArgUCA tRNA increased luminescence for every mutant (37%–104% of WT)". CDKL5: "Rescue was weakest at R134X (8.2% of WT)". These are plasmid-expressed constructs read by NanoLuc luminescence in cells, not endogenous genes and not in brain.
  2. In brain there are two further readouts besides luciferase: native mOrange2 fluorescence in sections (reporter payload "scAAV-G(I) delivery of the mO2-TGA reporter") and cleaved caspase-3 immunohistochemistry ("Cleaved caspase-3 staining was not detectable").
  3. A single behaviour sentence exists. Verbatim (Discussion): "Notably, we observed no obvious changes to mouse behavior or physiology, although additional studies will be needed to expand this analysis to subregions of the brain and to perform more detailed behavioral assessments." It is a narrative observation with no method, no n and no test. It is not a behavioural readout in the sense of C2, but it is the only behaviour text in the paper.
- (iii) All brain readouts are reporter-based (luciferase, mOrange2) or safety markers (tRNA-seq, caspase-3).

C3. SUPPORTED, with a denominator qualifier
- Verbatim (Results): "Within the cytosolic Arg tRNA isodecoder dataset, all species showed similar fractional abundances between the two groups, with the sup-tRNA readily detected in the injected mouse brains and comprising only 1.2% of the ArgUCU tRNA anticodon family, Fig. 4B."
- Verbatim (Results on endogenous Arg tRNAs): "Additionally, the charging fractions for the global tRNAs as well as the Arg tRNAs in both groups were not different". Verbatim (Fig. 4B legend): "tRNA-Arg isodecoder-level abundance in both conditions, showing detection of ArgUCA tRNA only in injected brains with no apparent changes across endogenous Arg-tRNAs."
- Verbatim (Results): "...it is possible that viral expression of a sup-tRNA may alter the expression balance ... ICV-injected LumA mouse brains were harvested at P30, and tRNA were extracted for full sequencing and analysis."
- Verbatim (Introduction): "shows that the anti-codon edited tRNA can achieve macroscopic rescue with expression levels at roughly ∼2% of the native parental Arg-TCT-1–1 tRNA".
- (i) P30 brain after P0–P1 ICV scAAV-G(I). Dose and construct dose are not stated for the tRNA-seq cohort in the retrieved text. The denominators differ: 1.2% of the ArgUCU anticodon family (Results) versus roughly 2% of the parental Arg-TCT-1-1 tRNA (Introduction).
- (ii) Methods: "analyses were performed with n = 3 per group where both comparison groups were present", with multiple unpaired t-tests with Welch's correction or Welch ANOVA "as specified in Supplementary Table S2" (not reachable). No exact p in the text. "Similar", "not different" and "no apparent changes" are claims from n = 3 per group. The comparison is injected versus uninjected, not versus a negative payload.
- (iii) tRNA-seq abundance, charging and modification profile: markers of tRNA homeostasis, not function.

(4) STATEMENTS THE SOURCES QUALIFY OR CONTRADICT
1. Pierce's body-weight control is described two ways. The text says "untreated controls (n=9)". The Extended Data Fig. 10c legend gives "N = 3 female sup-tRNA mice, 5 female Dnmt1 mice, 4 male sup-tRNA mice, 4 male Dnmt1 mice", and Methods describe "a control +5 G-to-T edit in the Dnmt1 locus". The control group was apparently the benign Dnmt1-edited group, not untreated.
2. Pierce's allele numbering is inconsistent within the paper and against Wang. Pierce uses "W392X" in the text and Fig. 5. The Extended Data Fig. 9a legend uses "position 401" ("W401"). Wang names the model "Idua-W401X, TGG→TAG", "Stock No. 017681". Pierce says the model "has been used previously to evaluate PTC readthrough in vivo5,51" (ref. 5 is Wang). I could not resolve from the sources whether these are the same line.
3. Pierce's "1% or more" threshold attribution. Pierce writes "restoration of only 1% or more IDUA enzyme activity is sufficient to rescue most or all observed MPS-1 disease phenotypes5" and cites Wang. The Wang text I retrieved does not contain that sentence. Wang states "as low as 0.5% of normal level was associated with attenuated disease manifestations ... sparing of neurological involvement" and cites its own refs 25,26. A match for "1%" in Wang finds only "11%", the FDR 1% filter and similar. So Wang does not state Pierce's 1% figure in its own text; the supplement was not reachable.
4. NAR's Hurler/UGA statement versus the two primary papers. NAR (Introduction): "Recent efforts with virally delivered anticodon-edited arginine tRNA have focused on UGA stop codons that cause Hurler syndrome (mucopolysaccharidosis type I, MPS I); however, rescue in these cases remains subtherapeutic [<8% of wild-type (WT) protein] potentially reflecting limitations in AAV titers and/or payload designs." Wang's model is "Idua-W401X, TGG→TAG" with a Tyr sup-tRNA. Pierce's Hurler allele is a TAG (CUA anticodon) with a Leu backbone ("This model harbours a TAG stop codon, Idua p.W392X"). So the UGA/arginine attribution is not supported by the Wang and Pierce texts. NAR cites Wang 2024 (Neurotherapeutics) and Wang 2022 ([22],[23]) and Xu 2026 ([27], "An engineered UGA suppressor tRNA gene for disease-agnostic AAV delivery"). I did not retrieve ref. 27.
5. NAR internal statistics. Methods say "mean ± SEM unless otherwise indicated" while the Fig. 3 legend says "mean ± SD". Methods give n = 3–4 for longitudinal in vivo imaging while the legend gives n = 3. The Fig. 2F legend gives "P < .05" with no exact p.
6. NAR's two denominators for sup-tRNA abundance (1.2% of the anticodon family versus about 2% of the parental tRNA) are given above.
7. Wang is an NIH Author Manuscript, so figure numbering or wording may differ from the typeset version. Wang's Fig. 3 legend states no age at dosing (B2). Wang's brain arm legends omit age, sex and time post treatment for IV arms (B1).

(5) NOT CHECKED AND WHY
- Supplementary files for all three papers: Pierce Supplementary Information (Supplementary Note with the pathology report and the corrected pathology report), Supplementary Tables 1–17, Source Data Fig. 5; Wang Supplementary Tables 1–5 (including Table 2, treatment conditions and ages), source data and Supplementary Figure 1; NAR Supplementary Tables S1–S3 and Supplementary Figs S1–S4. Not in the efetch XML, and following those routes was outside the one-request perimeter.
- Figure images: I read text and legends only. Values plotted in Fig. 5d/e/f (Pierce), Extended Data Figs 10d–f (Wang) and Figs 2F, 3, 4 (NAR) are not extractable from the XML. Specifically unchecked: which individual comparisons were marked significant, per-animal values, and whether the "up to 1.3%" is a mean or a single animal.
- Typeset versions: Wang was read as an author manuscript only. No PDF was fetched for any article, and there was no second route (for example the typeset PDF) for the absence claims A3 and C2. Both absence claims rest on two internal routes within the same text (string counts and a full read of headings and legends).
- The corrected pathology report and the blinding timeline (A3, A4) were not seen.
- References cited by these papers (Wang 2022 ref. 25/26 for the 0.5% and "sparing of neurological involvement" statement, Pierce refs 5/46–48, NAR refs 22/27) were not retrieved.
- No conclusion about any disease gene or drug is drawn here, as dispatched.
