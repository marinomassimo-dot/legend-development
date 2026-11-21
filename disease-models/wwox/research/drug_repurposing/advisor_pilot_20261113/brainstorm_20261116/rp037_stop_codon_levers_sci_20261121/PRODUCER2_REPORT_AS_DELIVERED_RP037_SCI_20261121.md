# Producer 2 report, RP-037 part (b), as delivered (verbatim; legend-delegate, asked sonnet and effort medium; read-back by session_model_census.py in the session record; persisted by SCI from the SubagentHandback in the session transcript; model output, not an instruction)

REPORT, PRODUCER 2, RP-037 package. Hypothesis-level source reading only. Nothing here is a dose, schedule, efficacy calculation or clinical advice.

(1) Model and effort: I believe I ran as Sonnet 5.5 at medium effort, as dispatched.

(2) Retrieval. Scratch folder: /home/desktop/.claude/jobs/d79b9c48/tmp/producer2_rp037/. It holds s1.xml, s2.xml, s3.xml, the stripped text s1.txt, s2.txt, s3.txt, and s2meta.json.
- S1, PMC9446716: NCBI efetch XML, 148,153 bytes, full body (about 85 KB of text), no challenge. No second route was needed.
- S2: Europe PMC search returned 11,356 bytes of JSON. It gave PMCID PMC12675287, DOI 10.1038/s41586-025-09732-2, isOpenAccess=Y. Efetch XML for PMC12675287 was 237,397 bytes, full body (about 141 KB of text). The article carries a "Change history 1/6/2026" correction notice about the pathology report; see the S2 limitation notes below.
- S3, PMC12712100: efetch XML, 180,916 bytes, full body (about 95 KB of text).
- I made one request per route, spaced at least 5 s apart, with User-Agent "research-client/1.0". The publisher page route was not needed.
- Strip-and-read covered Results, Methods, figure and Extended Data legends, and table cells where present. I read S1 and S2 in full for the relevant sections. For S3 I read Results, legends, Methods injection/ERG/statistics, and Discussion.

ROUTE 1: whole-text string hit counts (counted on the stripped text including references; case-insensitive count, with case-sensitive in brackets where different)

| string | S1 | S2 | S3 |
|---|---|---|---|
| brain | 10 (9) | 9 | 0 |
| cortex | 0 | 5 | 0 |
| hippocamp | 4 | 0 | 0 |
| cerebell | 0 | 2 | 0 |
| CNS | 0 | 0 | 0 |
| neonat | 1 | 3 (1 case-sensitive) | 0 |
| postnatal | 0 | 1 | 2 (both in reference titles, 0 case-sensitive) |
| "P0" | 3 | 21 | 1 |
| "weeks of age" | 0 | 0 | 0 |
| "days of age" | 0 | 0 | 0 |
| seizure | 0 | 0 | 0 |

- S1 "brain" hits include references.
- S1 "P0" hits are Cat. No. strings or Pitt-Hopkins-type text, not postnatal day 0. S1 "neonat" is in a reference title (neonatal and juvenile Mecp2 knockout).
- S2 "P0": the in-text "postnatal day 0 (P0)" and "P0 neonatal" are real hits. The others are mostly reagent or grant codes.
- S3 "P0" is the reagent code "P0013B" (RIPA buffer).

(3) ROW TABLES

=== S1, Wang 2022, Idua W401X mouse (PMC9446716). IN VIVO rows ===

(1) System and allele: endogenous knock-in locus, Idua W401X homozygous (KI/KI), Jackson Stock 017681, "bred in-house" (Methods, Animal use). Controls: KI/+ and an Idua KO/KO model (Stock 004068). Strain background is not stated.
(2) Stop codon and amino acid: UAG. The sup-tRNA is Tyr (sup-tRNATyr). Cell-based mass spectrometry in HEK293 (Fig. 1f) shows it inserted Tyr, the "single residue that aminoacylates the parental natural tRNA". The in vivo amino acid was not measured.
(3) Age, route 1 (search): "weeks of age" 0 hits, "days of age" 0 hits, "postnatal" 0 hits.
   Route 2, Results text: "treated adult IduaW401X/W401X female knock-in mice" and "In a cohort of adult male KI/KI mice".
   Route 2, ED Fig 5d legend: "KI/KI mice treated with rAAV9.2xsup-tRNATyr ... at various timepoints after treatment at 6 weeks old".
   Route 2, ED Fig 7a legend: "Mice were treated at 6 weeks old, and euthanized at 16 weeks old".
   Readout: 10 weeks after treatment (Fig 3 legend, "at 10 weeks post treatment"), and up to 28 weeks (serum IDUA and urine GAGs, ED Fig 5d, e).
   Age at delivery for the brain experiments (ED Fig 10d, f) is NOT stated as an age. Those legends say "Mice euthanized at 4 weeks post treatment" (f), and "adult" is the only text age.
   Supplementary Table 2 ("Treatment conditions can be found in Supplementary Table 2") was not reachable.
(4) n:
   - Fig 3 liver, heart, serum, urine: n=4 per group (KI/KI).
   - KI/+ n=3.
   - KO/KO n=3 treated, 8 untreated, KO/+ n=14 (Fig 3g).
   - Long-term serum: KI/+ n=8, KI/KI n=7, treated n=7 (ED5d).
   - Urine GAGs at 28 weeks: n=5 per group, KI/+ n=6 (ED5e).
   - Brain IDUA after IV AAV9: n=4 (ED10d left). Brain after IV AAV.PHPeB: n=5 per group (ED10d right).
   - Hippocampus: "n=4 or 3 per group" (ED10f).
   The unit counted is "individual animals (circles)".
(5) Delivery: AAV9 (CsCl-purified, ddPCR titre). Cassette: U6 promoter driving 2x sup-tRNATyr (also 1x and 4x variants). The cassette also carries CAG promoter-mCherry (Methods, AAV vectors); H1 appears as an alternative promoter (ED4a legend). Route: tail vein IV, "2x10^12 genome copies (GC) per mouse" (Results). The text also says "1x10^12 genome copies (GC) of each AAV9 vector" for the construct comparison.
   Brain-directed arms: AAV.PHPeB IV at "1x10^11 GC (yellow) or 2x10^11 GC (orange)" (ED10d legend). Intrahippocampal AAV9, unilateral, "2.2x10^10 GC" (ED10f legend). Muscle: IM "3x10^11 GC" TA (ED10a).
(6) Tissues examined:
   - Liver, heart, serum, urine, TA muscle, and brain. The brain was examined: "restored brain IDUA activity up to 1.3% of WT level" (PHP.eB IV; Results, last paragraph, ED10d, e). Brain reach was shown by AAV genome copy quantification (ED10e) plus IDUA activity.
   - Hippocampus (unilateral injection), "reaching 10% of WT level" (ED10f).
   - Brain H&E in KI/+ (not KI/KI) mice, treated vs untreated, for gross toxicity (ED7a, b), under "Blind pathological assessment".
   - Verbatim on IV AAV9: "the brain was poorly responsive to IV delivery of rAAV9.2xsup-tRNATyr, likely due to inefficient gene delivery". The brain IDUA value after IV AAV9 is in the ED10d image or source data. It is not stated in the text, so I have not read it.
   - Cortex and cerebellum: 0 hits in the text. Route 2: no brain region other than whole brain and hippocampus appears.
(7) Readout class and magnitude as printed:
   - ENDOGENOUS ENZYME ACTIVITY (IDUA): serum "from undetectable to 2.5% of WT level"; liver 9.5%, heart 27% of WT (Results, Fig 3b, d); TA muscle 0.5% (ED10a); brain 1.3% (PHP.eB); hippocampus 10%.
   - Biochemical and histological correlates: urine and tissue GAGs, LAMP1, glucuronidase, hexosaminidase, in liver and heart.
   - NMD readout: Idua mRNA by ddPCR and NGS.
   - No FUNCTION or PHENOTYPE readout (no survival, behaviour or neurological test): seizure 0 hits.
   - The % of WT denominator: wildtype (+/+) IDUA activity, with KI/+ normalised to 50% of WT. Brain denominator is the same unless the source data say otherwise.
(8) Statistic: two-sided Student t-test, one-way ANOVA with Dunnett's, and for ED10 "Brown-Forsythe and Welch ANOVA followed by two-sided Dunnett T3's"; data are mean ± s.d. Exact p values are not given in the text, only asterisk levels. Blinding: only "Blind pathological assessment" (ED7b). No pre-specification, sample-size or randomisation statement was found in the Methods (route 2 read of the Statistics paragraph).
(9) Off-target and safety: Ribo-seq in treated mouse liver (n=3), "largely restricted to UAG"; tRNA-seq in liver (n=3 each); mRNA-seq "23 upregulated transcripts" in liver; Chop/Bip not elevated; clinical biochemistry and H&E including brain (KI/+ mice): "we did not observe gross toxicity". Global-readthrough work in vivo was in liver only.
(10) NMD: measured. "sup-tRNATyr treatment in KI/KI mice led to significant increase of the nonsense Idua mRNA in the liver (4.6-fold) and heart (10.2-fold) to the levels in WT mice (Fig. 3h)". Brain NMD or mRNA was not measured. The Summary states "synergistic effect of premature stop codon readthrough and inhibition of nonsense-mediated mRNA decay".
(11) Limitations stated: "the brain was poorly responsive to IV delivery ... likely due to inefficient gene delivery" (Results). "not all diseases caused by a PTC are amenable to AAV-NoSTOP due to limitations of gene delivery and therapeutic threshold among other factors" (Discussion). "These and other sup-tRNAs remain to be tested for their in vivo safety and therapeutic efficacy in rescuing endogenous PTC transcripts". Females were "less effective in some assays" (Results; ED6).
Flags: AGE AND DENOMINATOR: delivery at 6 weeks, adult; the brain arms' ages are not stated. Brain value is a % of WT enzyme activity (a marker), with n=3 to 5. STATISTIC: s.d. and asterisks only. MARKER vs FUNCTION: enzyme activity and GAG biochemistry only; no CNS function or phenotype and no CNS GAG measure for KI/KI. The brain H&E was done in KI/+ mice, which have no phenotype.

=== S2, Pierce 2025 (PMC12675287; Nature, DOI 10.1038/s41586-025-09732-2). Two IN VIVO systems ===

Row A: reporter system
(1) System and allele: exogenous AAV9 eGFP reporter with a TAG or TGA PTC at codon 81 (Methods, In vivo prime editing). Wild-type C57BL/6 mice (the Results say "wild-type C57/BL6 mice"). The editing target is the endogenous mouse tRNA-Leu-TAA-2-1 locus (prime editing installs the sup-tRNA in the genome).
(2) Stop codon and amino acid: TAG (CUA anticodon, from a Leu tRNA backbone) and TGA (UCA). The amino acid inserted in vivo is not stated for this reporter; the amino acid read through in the reporter in vivo was not measured.
(3) Age: route 1, "P0" hits include "postnatal day 0 (P0)" (Results). Delivery at P0, intracerebroventricular. Readout "At 3 weeks after injection" (Results), so about 3 weeks of age; "3 weeks" is also in the Methods. Route 2: Methods "Neonatal ventricular injections" confirms neonatal ICV.
(4) n: "n = 4 mice per condition" (Fig 5b legend).
(5) Delivery: v3em dual-AAV9 prime editor, Cbh promoter in the schematic (Fig 5a legend: "Cbh, chicken β-actin hybrid promoter"), ICV. A dose is stated: "5 × 10^10 vg of each half of prime editor encoding AAV and 1 × 10^10 vg of reporter AAV in ... total volume of 4 μl ... 2 μl ... into each ventricle" (Methods).
(6) Tissues: brain was examined, specifically bulk "brain cortex" for editing and "whole hemisphere halves" dissociated for GFP flow cytometry. Reach was shown by sequencing reads (editing %) and flow cytometry of GFP. No other CNS region, and no peripheral tissue, was examined for this experiment.
(7) Readout class: REPORTER (GFP). Printed: editing "11% for the TAG sup-tRNA and 23% for the TGA sup-tRNA in the bulk brain cortex"; "average relative protein yield of 24% of the co-delivered TAG GFP reporter and 26% of the co-delivered TGA GFP reporter (Fig. 5b)". Denominator: the co-delivered wild-type GFP reporter (Fig 5b legend). The exact denominator definition was not stated in the text.
(8) Statistic: "one-sided Welch's t-test" (Fig 5b legend); exact p values are in Supplementary Tables (not reached). Methods: "Litters were randomized for injection with a given AAV composition"; "No statistics were performed to pre-determine sample size". SD is mentioned for ED10f.
(9) Off-target and safety: whole-proteome mass spectrometry of "mouse livers and cortices" at 3 weeks: "we did not detect any peptides corresponding to readthrough of natural stop codons in tissues from mice treated with PERT (Supplementary Table 17)". A 15-week body-weight cohort, PERT n=7 vs untreated n=9, "no significant difference in body weight" (ED10b, c).
(10) NMD: not measured in vivo. The NMD hits are only "nonsense-mediated decay-sensitive reporter construct" (cell screen) plus a reference title.
(11) Limitations stated: "although editing efficiency would benefit from further optimization in mice, cells that receive prime editing agents can achieve readthrough levels that could ameliorate many diseases" (Results).
Flags: AGE AND DENOMINATOR: P0 delivery (neonatal, not adult); readout at 3 weeks. Reporter denominator is the co-delivered WT reporter. STATISTIC: one-sided Welch's t-test, n=4. MARKER vs FUNCTION: reporter only.

Row B: Idua W392X
(1) System and allele: endogenous knock-in Idua p.W392X (TAG), described as orthologous to human IDUA p.W402X. "we used Strain from Jackson Laboratory"; strain background is not stated.
(2) Stop codon and amino acid: TAG. Sup-tRNA is the engineered mouse tRNA-Leu-TAA-2-1+hp13gc>ta+mut38a>t. The inserted amino acid in vivo is not measured. For "PE-installed sup-tRNAs" in cells, ED Fig 9a evaluates amino acid installation in the Flag-IDUA W401X cDNA.
(3) Age: "treated homozygous and heterozygous P0 neonatal IduaW392X littermates via intracerebroventricular injection (Fig. 5c)"; readout "At 7 weeks after treatment" (Results). Route 1 gives "P0"; route 2 (Results and the Methods neonatal injection section) agrees. Age at readout is about 7 weeks, since 7 weeks after P0.
(4) n: "n = 3 mice per condition" (Fig 5d legend), homozygous IduaW392X. Fig 5f pathology n is not stated; the ED Fig 10 legend gives no n for the pathology score.
(5) Delivery: v3em dual-AAV9. Route ICV at P0. A per-vector dose for the Idua experiment is not stated in the Results or the Fig 5 legend. The only dose text in Methods is for the reporter experiment (5 × 10^10 vg each half, 4 μl). I could not confirm that the same dose was used for Idua. Treat it as not stated.
(6) Tissues: brain was examined. Editing: "6.3%, 6.1%, 6.8% and 0.05% in the cortex, heart, liver and kidney" (Fig 5d). Enzyme activity relative to WT: "7.6%, 6.3%, 1.7% and 0.31% in the heart, cortex, liver and kidney" (Fig 5d, ED10d). Histology: brain (cerebellar Purkinje cells, thalamic neurons), liver, spleen, and heart. Hippocampus: 0 hits. Cerebellum is named only in the histology. Reach was shown by editing efficiency (HTS) plus enzyme activity. The brain was examined as cortex for editing and enzyme activity.
(7) Readout class: ENDOGENOUS ENZYME ACTIVITY (IDUA, relative to WT mice) plus histopathology of GAG storage. Magnitude: cortex 6.3% of WT; histology: "Purkinje cells of the cerebellum and thalamic neurons displayed moderate vacuolization in untreated homozygous IduaW392X mice and was resolved following PERT treatment with absent or minimal vacuoles (Fig. 5e,f and Supplementary Note)". This is a histological phenotype in brain, not a behavioural or electrophysiological function. No survival, behaviour, seizure or ERG readout (seizure 0 hits). The GAG pathology score (Fig 5f) is semi-quantitative.
(8) Statistic: "one-sided Welch's t-test compared with non-prime edited mice (Extended Data Fig. 10d)"; "*P < 0.05; NS". Exact p values are in Supplementary Tables (not reached). Pathology: "scoring was performed by a board-certified veterinary pathologist blinded to the treatment conditions". The correction notice (Change history, 1/6/2026) states the pathology report's mouse IDs were mislabelled in the narrative, the study title on the signature page was incorrect, and a corrected report "includes clarification of the timing for unblinding"; the conclusions are said to be unaffected. I could not read the corrected pathology report. No sample-size pre-specification ("No statistics were performed to pre-determine sample size for each group").
(9) Off-target and safety: "any off-target editing using two genome-wide detection methods" and "did not observe any evident toxicity"; whole-proteome MS in liver and cortex in the reporter cohort. These safety measures were made in the reporter-editing cohort and body-weight cohort, not in the Idua mice.
(10) NMD: not measured in the Idua mice; no mRNA measurement is in the text.
(11) Limitations stated: "editing efficiency would benefit from further optimization in mice" (Results) and the Discussion paragraph on the unexplained determinants of sup-tRNA effectiveness ("remain incompletely understood"). No limitation specific to the brain data was stated.
Flags: AGE AND DENOMINATOR: P0 delivery (neonatal); the denominator is enzyme activity relative to wild-type mice, n=3. STATISTIC: one-sided Welch's t-test on n=3, asterisks only in the legend, with a pathology-report correction notice affecting labelling and unblinding timing. MARKER vs FUNCTION: enzyme activity plus histology (brain H&E in cerebellum, thalamus); no behavioural or physiological function.

=== S3, Ren 2025, RPE65 R44X rd12 mouse (PMC12712100) ===

(1) System and allele: endogenous Rpe65 R44X (rd12) mouse, from Jackson Laboratory. WT controls: C57BL/6J from Chengdu Dossy. Also an AAV8 ABCA4-R681X EGFP reporter in a photoreceptor reporter experiment (Supplementary Fig 7, not reached as a figure).
(2) Stop codon and amino acid: UGA (R44X, "PTC site (TGA) at codon 44"). The sup-tRNA is Arg, engineered "sup-tRNAArg-A4T1", in a scAAV8 vector; it introduces arginine, as intended. In vivo identity of the inserted amino acid was not measured (MS was in HEK293).
(3) Age: route 1, "weeks of age" 0 hits, "days of age" 0 hits, "postnatal" only in reference titles, "P0" = reagent code. Route 2: Results "injected into the subretinal space of 2-week-old rd12 mice" and Methods "At the age of two weeks, subretinal injections were performed". Readout: ERG at "the age of 5 weeks and 14 weeks" (Fig 3c, f legends); RPE65 protein and flat-mount "at 12 weeks post injection"; a 36-week follow-up cohort (Supplementary Fig 12, not reached as a figure).
(4) n: ERG n = 6 per group; Western blot "four biological replicates"; RPE flatmounts n=4; ddPCR "three biological replicates"; H&E "untreated (n = 3), scAAV8.TCT-1 treated (n = 5) or scAAV8.A4T1 treated (n = 6)"; visual cliff n=6 WT and untreated, n=8 treated; open field n=12; water maze n=6. The ERG unit is mice (legend: "n = 6 in each group").
(5) Delivery: scAAV8, hU6 promoter (Methods: "hU6 promoter and U6 terminator flanked by scAAV2 ITRs"). Route: subretinal. Dose as written: "1 × 10^9 GC per eye" (and "1 × 10^8, 3 × 10^8, or 1 × 10^9 genome copies (GC) per eye"), "1 μL" per eye (Methods).
(6) Tissues: RPE/choroid/sclera complex, retina (H&E, flat-mount, PNA-lectin and M-opsin for cones), eye. Brain: 0 hits for brain, cortex, hippocamp, cerebell, CNS, neonat; the only CNS-adjacent strings are "optic nerve" (3 hits, anatomical landmark in methods). Route 2: no brain, visual cortex or optic-pathway tissue appears in Results headings or legends. Neural retina was examined (histology, ERG, flat-mount), not brain.
(7) Readout class: FUNCTION or PHENOTYPE (ERG, visual cliff, open-field and water-maze behaviour), plus ENDOGENOUS PROTEIN (RPE65 Western blot, RPE65 flat-mount immunofluorescence) and mRNA. Magnitudes as printed: "an average of 36.0% RPE65 positive cell in scAAV8.A4T1-treated eyes and 4.5% in scAAV8.TCT-1-treated eyes (Fig. 2c)"; "rescued 21.3% and 35.6% of the a- and b-wave amplitudes in scotopic ERG (Fig. 3c) and rescued 83.0% and 76.9% of the a- and b-wave amplitudes in photopic ERG (Fig. 3f)" with "compared with those of the wild-type mice" as the denominator; Western blot at 2 weeks injection: "an average of 16.4% (8.0-30.1%) RPE65 protein compared with that of the WT control (Supplementary Fig. 6e)" (dose "high" arm, 3 weeks after injection); water maze success: WT 91.7%, untreated 12.5%, TCT-1 41.7%, A4T1 58.3%.
(8) Statistic: SEM. One-way ANOVA with Dunnett's, two-sided t-test, "two-tailed Mann-Whitney U-test (b, e)" (Fig 3 legend), GraphPad Prism 9. Exact p values were not read. Methods: "Blinding was not used for the study ... Littermate mice were randomized among experimental groups ... Sample sizes were chosen based on other similar studies. No data were excluded".
(9) Off-target and safety: RNA-seq of RPE ("26 upregulated and 178 downregulated transcripts"), no NTC readthrough, no UPR induction ("no gross toxicity, NTC readthrough or induction of the UPR pathway was observed", Discussion), H&E and ONL thickness at 12 and 36 weeks.
(10) NMD: measured and stated. "The mRNA level of RPE65 in rd12 mice was reported to be approximately 50%-60% of that in WT mice ... This should be ascribed to a moderate level of NMD. scAAV8.A4T1 stabilized the expression of RPE65-R44X mRNA at levels similar to those of RPE65-R44 (Fig. 2d)."
(11) Limitations stated: "the specific mutations we generated may not be universally applicable to sup-tRNAs carrying other amino acids" (Discussion). It is a "proof-of-concept study". Also "The overall lower efficacy observed in this reporter system compared with rd12 mice is likely attributable to ... limited AAV transduction efficiency for photoreceptors, the dual-AAV strategy" (photoreceptor reporter).
Flags: AGE AND DENOMINATOR: dosed at 2 weeks of age (not neonatal P0); ERG at 5 and 14 weeks; denominators are WT mice for ERG and WT RPE65 for Western blot. STATISTIC: SEM; n=6 for ERG; no blinding. MARKER vs FUNCTION: both; function (ERG, behaviour) is present, and it is for the retina only.

(4) ONE SENTENCE PER SOURCE
- S1 (Wang 2022): Yes, brain was examined after sup-tRNA delivery, but only as IDUA enzyme activity in whole-brain lysate (IV AAV.PHPeB, "up to 1.3% of WT level") and hippocampus (intrahippocampal AAV9, 10%), plus brain H&E in KI/+ mice for toxicity (ED Fig 10d, e, f; ED Fig 7); the main cohort was dosed at 6 weeks old, adult, with readout at 10 to 28 weeks later (Fig 3; ED Fig 5d, 7a; the brain-arm ages are not stated as a number in the text), and the readout was endogenous enzyme activity (no function).
- S2 (Pierce 2025): Yes, brain cortex and hemisphere were examined, with mice dosed at P0 by ICV (Results, Fig 5a, c; Methods Neonatal ventricular injections), and the readouts were a GFP REPORTER at 3 weeks (24% and 26%) plus endogenous IDUA enzyme activity in cortex (6.3% of WT) and brain H&E vacuolization (cerebellar Purkinje cells and thalamic neurons) at 7 weeks (Fig 5d to f; ED Fig 10), with no behavioural or physiological function measured.
- S3 (Ren 2025): No, no brain tissue was examined (0 hits for brain, cortex, hippocampus, cerebellum, CNS; Results headings and legends cover only RPE, retina, ERG and visual behaviour); mice were dosed subretinally at 2 weeks old, and the readouts were endogenous protein (RPE65) and function (ERG, visual cliff, water maze; Figs 2 to 4).

(5) What I could not check, and why
- All three sources: supplementary files, source data, Supplementary Tables and Notes were not reachable by this route. This includes S1 Supplementary Table 2 (treatment conditions, possible ages), S2 Supplementary Tables (exact p values, Table 17 MS data) and the corrected pathology report, and S3 Supplementary Figs 6, 7, 12.
- S1: the brain IDUA values after IV AAV9 (ED Fig 10d left) are in the figure panels or source data, not the text. Age of the brain-arm mice is not stated.
- S2: Idua W392X dose per vector is not stated in the main text or legends; the Methods dose applies to the reporter experiment (I did not confirm it applies to Idua). The Fig 5f n and the exact amino acid inserted in vivo are not stated. Supplementary Discussion and Note were not read. The pathology correction (Change history 1/6/2026) affects mouse IDs and unblinding timing; the corrected report was not read.
- S3: figure images and Supplementary Figs not viewed; only text, legends and tables were read. Exact p values were not given in the text.
- The S1 text lines 60 to 127 (Methods blocks on histology, tRNA-seq, Ribo-seq) were not read line by line, only the Animal use, AAV vectors, Statistics and legend sections that bear on the question. The remaining Methods blocks do not concern tissue, age or dose, so I expect no change, but I have not confirmed that by reading them.
- No conclusions about any disease gene or drug are drawn.
