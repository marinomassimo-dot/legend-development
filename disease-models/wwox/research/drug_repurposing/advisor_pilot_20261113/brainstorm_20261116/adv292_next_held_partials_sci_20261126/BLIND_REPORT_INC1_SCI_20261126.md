# ADV-292 increment 1: blind second-reader reports, copied verbatim from the delegate transcript

Delegate: legend-delegate, model sonnet, effort high stated in the dispatch (read back high in all 55 turns, see the RESULT file). Report 1 judged S1a to S4; its S5 line says NOT JUDGED because my extraction of the sentence failed (my error: the S5 block was empty in the file sent). Report 2 judged S5 after the block was added and re-judged S2a under two readings of the word class (the interpretive bracket on S2a in the first file was my own, not the repository's). The reader saw the sentence file and the source folders only, none of the first reader's notes.

## Report 1

ADV-292 INC1 blind second-reader report (independent verifier, sonnet, effort high). I opened only the folder each sentence names, and no files outside the blind directory. I read the article XML and the main figures as images. For folder A I also read supplementary figures S1-S7 and Tables S1-S3. For folder B I read Supp Figs 1-4. For folder C I read the SI PDF, including Fig S4. For folder D I read Table S1 (the sheet dump). Nothing failed to open, except that S5 has no text.

## S5 (folder E): NOT JUDGED, the sentence is missing
`SENTENCES_ADV292_INC1.md` ends at the heading `## S5 (folder E)` followed by an empty line. The file is 39 lines and 5752 bytes, and I checked the tail with `cat -A`. No sentence text exists, so I have no verdict.
- Folder E is one PDF: Ahuja et al., Lab Chip 2026, 26, 1915, "MyeliMAP: a microfluidic-multielectrode array hybrid platform ... human iPSC derived brain-like networks".
- I did not read it further, because a verdict without the sentence would be invented.
- Please resend the S5 sentence.

## Folder A: Wang 2024 (Hispidulin and TP003, GABRA1 variants; HEK293T plus one iPSC line)

Replicate units: Western blots n = 3 independent experiments. Whole-cell currents n = 4-11 cells per group (Fig 4B legend). iPSC imaging is counted in cells (Fig 7C, 7E).

### S1a: MUST CHANGE
Sentence: "GABRA1 receptor-binding modulators raised variant protein and current together (measured in HEK293T, one knock-in iPSC line)".

Separable claims:
1. "Modulators raised variant protein": only some did. The screen (Supp Fig S3) tested 10 GABA-A ligands at 10 µM for 24 h on three variants.
   - Rows: A = D219N, B = G251D, C = P260L. Each has a left and right sub-panel of 6 compounds.
   - Raised total α1 in all three variants: Hispidulin (all ***), TP003 (all ***), Midazolam (**/***/***).
   - CL218872 raised D219N (*) and P260L (***) but not G251D (NS).
   - Did not raise protein: Florazepam, Chlormezanone, GABA, Bretazenil, CGS20625 (all NS in all three variants).
   - ZK93423 lowered D219N α1 (**, to about 0.25 of control), and was NS in G251D and P260L.
   - Verdict: MUST CHANGE. "Receptor-binding modulators" overgeneralises. Four of ten raised protein in at least one variant, and one lowered it.
2. "and current": current was measured only for Hispidulin (10 µM, 24 h) and TP003 (5 µM, 24 h). It was not measured for Midazolam or CL218872.
   - Fig 4B, HEK293T, 8 variants, n = 4-11 cells.
   - Hispidulin raised Imax significantly in all 8 variants (A322D *, D219N *, P260L **, R214C **, S76R ***, G251D ***, M263T *, T289P ***).
   - TP003 was significant in only 6 of 8. D219N and R214C were NS (Fig 4B; the text says "did not reach a significant level").
   - In Fig 4C, TP003-treated P260L stayed significantly below wild type (**).
   - Verdict for the two chaperones: STANDS in HEK293T.
3. "together" for protein and current: STANDS for Hispidulin and TP003 in HEK293T.
   - Surface protein, Fig 4A: Hispidulin significant in 8/8. TP003 significant in 5/8; D219N, P260L and R214C were NS.
   - Total protein at 10 µM: Hispidulin and TP003 raised it in the three variants of Supp Fig S3.
4. "(measured in HEK293T, one knock-in iPSC line)": the iPSC line is correct but is misleadingly bracketed with current.
   - It is one heterozygous α1(G251D) knock-in iPSC line, differentiated to GABAergic neurons.
   - Fig 7B-C: only surface immunofluorescence intensity of α1, γ2 and β2/3 was measured, with Hispidulin and TP003, in cells.
   - Fig 7D-E: proximity-ligation puncta per cell.
   - No current and no total protein were measured in iPSC neurons.
   - Verdict for any reading that current was measured in iPSC: MUST CHANGE. Current is HEK293T only.

Corrected wording: "Two GABA-A benzodiazepine-site positive modulators, Hispidulin and TP003 (of 10 receptor ligands screened; Midazolam and CL218872 also raised total protein, and ZK93423 lowered D219N protein), raised variant α1 surface protein and GABA-evoked current in HEK293T cells for most of eight α1 variants (TP003 not significant for D219N and R214C). In one heterozygous G251D knock-in iPSC line, surface subunit immunofluorescence rose; current was not measured there."

### S1b: ADD
Sentence: "Client-specific rescue ... came from ligands that bind the client..."; only the first clause rests on this paper.
- The two rescuing ligands (Hispidulin, TP003) are described as binding the benzodiazepine site of GABA-A receptors. The paper says "Since Hispidulin and TP003 directly bind GABA A receptors at the benzodiazepine sites" (Results 3.4), with literature citations.
- Binding was not measured in this paper. I searched the full article text for flumazenil, competition, "binding assay", docking and thermal; there were no hits.
- Binding to the variants is a presumption: "Presumably, binding of Hispidulin and TP003 to the α1(G251D) variant improves stability" (3.5).
- Six of the ten receptor ligands screened did not raise protein (see S1a), so binding alone did not predict rescue.
- Verdict: ADD. The clause stands only as "known GABA-A benzodiazepine-site modulators (binding taken from the literature, not tested here) rescued; other binders did not".

### S1c: ADD
I can judge only the content claims, not the ledger metadata (the receipt, manifest and locators are outside the folder).
- "Eight figures": the folder has 8 main figure files (f0001-f0008), matching the paper's Fig 1-8. UNSETTLED beyond that, since I cannot see the ledger.
- "A ligand that binds the client protein itself": binding is asserted from the literature, not measured here (searches as in S1b). Wording should be "known to bind".
- "Best-instrumented quantity-and-function paper in the lot": a comparative judgement I cannot test on one folder. The paper does not use that wording.
- Within this paper, protein, current, FRET, endo H, CHX chase and iPSC readouts exist, but the iPSC readouts are surface protein and proximity-ligation only.

## Folder B: Shah 2025 (SLC6A1/GAT-1, G443D and G443V; HEK293 and Drosophila)

Key data, by panel. Fig 3 means the single-concentration uptake screen. Fig 4 is the Michaelis-Menten kinetics plus Endo H blots (image files are named out of order, so I use the text and legend numbering).
- Fig 3A (WT, uptake as % of untreated WT):
  - 4-PBA 10 mM about 180% (*).
  - Glycerol 10% about 115% (NS).
  - Also raised: pifithrin-μ, 17-DMAG, lumacaftor, liothyronine.
- Fig 3B (G443D, % of WT uptake):
  - Glycerol about 6% (***).
  - 4-PBA about 1.6% (no significance mark).
  - Pifithrin-μ about 2.7% (*).
- Fig 3C (G443V):
  - 4-PBA about 8% (***).
  - Glycerol about 5% (**).
  - Pifithrin-μ, 17-DMAG and lumacaftor about 5% (*).
- Fig 4 kinetics (HEK293, n of at least 3 independent experiments in triplicate):
  - WT control Vmax 298, Km 6.5.
  - WT + glycerol Vmax 556, Km 12.7.
  - WT + 4-PBA Vmax 812, Km 5.7.
  - G443D + glycerol Vmax 165, Km 22.9.
  - G443V + 4-PBA Vmax 116.5, Km 39.2.
  - Mature (Endo H-resistant) bands rose for G443D with glycerol (Fig 4E) and for G443V with 4-PBA (Fig 4G).
  - WT blots (Fig 4B, C) are representative only; there is no densitometry.
- Drosophila (ALRM-Gal4 astrocytes, 3-5-day-old males, food with 1 mM 4-PBA or 10% glycerol for 48 h):
  - WT and G443D expression "not markedly altered" (Fig 6B, C).
  - G443V antennal-lobe volume rose with 4-PBA about 14-fold (Fig 6I, ***). Glycerol had "only a minor effect".
  - Both 4-PBA and glycerol restored presynaptic G443V in ellipsoid-body neurons (Fig 6F, qualitative).
  - Seizures, % of flies, groups of 10 (Fig 6G, H):
    - G443D: control about 46%, glycerol about 42%, 4-PBA about 49%, all NS.
    - G443V: control about 43%; 4-PBA about 20% (***); glycerol about 32% (NS).

### S2a: MUST CHANGE
Separable claims:
- "The class rescued the fully retained variant G443V": STANDS for 4-PBA in HEK293 (Fig 3C, 4F-G) and in flies (Fig 6D, H, I). For glycerol it is HEK293 only (Fig 3C, about 5% of WT, **). In flies glycerol gave minor expression gain and non-significant seizure reduction. ADD the species and chaperone for glycerol.
- "and NOT the partly trafficked G443D": MUST CHANGE for the class as defined (4-PBA plus glycerol).
  - Glycerol did rescue G443D in HEK293: Fig 3B (about 6% of WT uptake, ***), Fig 4D (Vmax 165) and Fig 4E (more mature band).
  - The statement holds only for 4-PBA (Fig 3B; Fig 6G in flies).
  - The repository's own S2c note says glycerol rescued G443D in vitro, so S2a contradicts it.
- "Rescued variants recover part of wild-type capacity with altered affinity": STANDS (Fig 4).
  - G443D Vmax 165 is 55% of untreated WT Vmax 298; Km 22.9 against 6.5.
  - G443V Vmax 116.5 is 39% of 298; Km 39.2 against 5.7.
  - The Fig 3 single-concentration screen gives much smaller fractions (about 6% and 8% of WT), so the fraction depends on the assay.
- "Wild-type capacity is raised too": ADD.
  - HEK293: 4-PBA raised WT uptake (Fig 3A *; Vmax 298 to 812). Glycerol was NS at the screen concentration (Fig 3A), though Fig 4A Vmax rose 298 to 556.
  - Drosophila: WT hGAT-1 expression was not altered (Fig 6B).
- Also, the paper calls G443V "a unique VUS" in the Discussion, while Table 3 lists it as "Likely pathogenic" (ClinVar). The row's "disease variant" wording could carry that qualifier.

Corrected wording: "4-PBA (10 mM in HEK293; 1 mM for 48 h in fly glia) rescued the fully ER-retained G443V but not the partly trafficked G443D; 10% glycerol rescued G443D uptake and surface band in HEK293 and also raised G443V uptake in the HEK293 screen. Rescued variants reach 39-55% of untreated WT Vmax with higher Km. WT uptake was also raised in HEK293 (clearly by 4-PBA); WT fly expression did not change."

### S2b: MUST CHANGE
Sentence: "The class raises wild-type protein in every target of the lot: the effect is not variant-specific." Judged only for the GAT-1 part.
- HEK293: WT hGAT-1 mature glycosylated bands increased with glycerol and 4-PBA. The text says "drastically augmented" (Fig 4B, C), but the blots are representative and unquantified. The quantified WT readout is uptake, and glycerol was NS in Fig 3A.
- Drosophila (this row's species list includes fly): "4-PBA and glycerol did not markedly alter the expression of WT GAT-1" (Fig 6B). In the same flies G443V rose about 14-fold. In vivo the paper's effect was variant-selective, not general.
- Verdict: for this paper, "raises wild-type protein" and "not variant-specific" hold in HEK293 only (unquantified blots plus uptake for 4-PBA). They are contradicted in fly glia.
- Corrected: "In HEK293, 4-PBA and glycerol increased WT hGAT-1 mature band (unquantified blots) and 4-PBA increased uptake; in Drosophila astrocytes neither changed WT expression."

### S2c: STANDS
Every checkable part is supported:
- G443D flies with 1 mM 4-PBA for 48 h: seizures unaltered (Fig 6G, about 46% control vs about 49%). The text says "stayed unaltered".
- Same dose in G443V flies reduced seizures (Fig 6H, ***).
- 10% glycerol was NS in both fly lines (Fig 6G, H).
- 4-PBA 10 mM did not rescue G443D uptake in HEK293 (Fig 3B; "failed to mend the expression or activity").
- Glycerol rescued G443D in vitro (Fig 3B, 4D-E).
- G443D flies show WT-like expression: Fig 6C legend ("similar to the WT hGAT-1 and glial membrane marker"), Fig 6E (presynaptic expression), Supp Fig 4C (broad expression and presynaptic enrichment, similar to WT).
- Minor: the 4-PBA bar for G443D in Fig 3B has no significance mark, and about 1.6% of WT is nominal.

## Folder C: Fu 2025 (IXA62/IXA554/IXA105, IRE1/XBP1s activators)

Replicate units: Western blots n = 3-5 independent experiments. Currents n = 8. Immunofluorescence n = 40-50 cells. iPSC n = 19-36 neurons from at least 3 differentiations.

### S3a: ADD
Sentence: "selective IRE1/XBP1s activators raised post-transcriptionally variant protein, surface protein and current for GABRA1 variants (research compounds, not approved drugs; HEK293T and one iPSC line)".

Separable claims:
- "Selective IRE1/XBP1s activators": STANDS, this is the paper's term.
  - Evidence: XBP1s target genes (Fig 1B), XBP1s protein (Fig 1C), 4μ8C blocks the effect (Fig 1D-F), CHOP unchanged (Fig S1E).
  - Qualifier: IXA62 slightly raised BiP and HerpUD1.
- Variant protein: STANDS. Total protein rose for D219N (2.4-, 1.6- and 2.8-fold for IXA62, IXA554 and IXA105), G251D (Fig 5B, all *-**) and P260L (Fig S4B, all **).
- Surface protein: STANDS with one exception.
  - Biotinylation: D219N all significant (Fig 2H).
  - G251D, Fig 5C: IXA62 *, IXA554 ***, IXA105 no significance mark (text says 2.3-fold). Confocal surface staining was significant for all three (Fig 5E).
  - P260L, Fig S4C: all three significant (1.4-, 1.9-, 1.5-fold).
- "Post-transcriptionally": the unchanged GABRA1 mRNA was shown only in D219N cells at 12 h (Fig 1B). No mRNA test was shown for G251D or P260L. ADD.
- "Current for GABRA1 variants": current was measured only for D219N (Fig 2K-L, 100 µM GABA, n = 8; *, ***, **) and G251D (Fig 5F-G, 1 mM GABA; all ***). It was not measured for P260L (abstract: "α1(D219N) and α1(G251D)"). ADD.
- "HEK293T and one iPSC line": the iPSC line is one heterozygous G251D knock-in line.
  - Only IXA62 and IXA554 were tested in the iPSC neurons (not IXA105).
  - Readouts there are surface α1, β2/3 and γ2 immunofluorescence (all significant) and proximity-ligation puncta (Fig 6A, 6B).
  - No current, total protein or mRNA was measured in the iPSC neurons.
- Corrected wording: "...raised total and surface protein of three α1 variants (D219N, G251D, P260L) in HEK293T and peak current for two (D219N, G251D; P260L not measured); the unchanged-mRNA test was done for D219N only; in one G251D iPSC line, IXA62 and IXA554 raised surface subunit staining and PLA interactions, with no current measured."

### S3b: ADD
- "The adjacent paper does not address" client-agnostic remodelling safety is largely true, with qualifications.
  - Searches of the article text for "toxic", "viab", "cell death" and "safety" found:
    - The paper says IXA554 and IXA105 were tested only up to 10 µM "due to the drug toxicity to cells at 25 µM" (Results). No viability data are shown.
    - The Introduction says prolonged or high IRE1 activation can cause cell death (RIDD, JNK, NF-κB), and frames "moderately activating" as the goal.
    - It tests wild-type α1 only (Fig S2A-D: no increase for IXA62 and IXA554; minimal effect for IXA105) and CHOP only (PERK arm).
  - It reports no other client protein, proteome-wide readout, viability or tolerability assay, or in vivo test.
- "The sources concern a disulphide-bonded glycosylated membrane protein": STANDS. The paper uses a PEGylation assay for the α1 disulfide and Endo H for the Asn38/Asn138 glycans.
- ADD: "The paper tests only α1 (wild-type vs variant) plus CHOP and notes toxicity at 25 µM; it has no viability, other-client or in vivo safety data."

## Folder D: Frick 2026 (zebrafish stxbp1a/stxbp1b, 4-PBA)

### S4: ADD
Sentence: "MEASURED NO RESCUE in null alleles, protein not measured, bath concentration bounded by larval toxicity, assay separation of controls unestablished; INCONCLUSIVE for a protein-expressing missense allele. Encoded NO_CHANGE."

Separable claims:
- stxbp1a movement, no rescue: STANDS.
  - Table S1, Fig 1E (means in mm): stxbp1a control 284; 25 µM 279 (P = 0.9893); 50 µM 300 (P = 0.8493).
  - Fig 1D shows the same. The 16 other candidates: smallest stxbp1a P = 0.1833 (Compound A, 50 µM). The Bonferroni threshold is 0.000714.
- stxbp1b ictal-like events, no change: STANDS.
  - 50 µM, 4-PBA, 9 larvae.
  - Type II events per 15 min: baseline 7.56 ± 2.29 vs 8.22 ± 2.91, P = 0.8593 (unpaired t test, df 16).
  - Window: bath 4-PBA 45-60 min (Fig 1F-G). Underpowered.
- "Null alleles / frameshift nulls": ADD.
  - Results: stxbp1a carries a 4-bp frameshift deletion. stxbp1b carries "a 12-base-pair loss-of-function deletion".
  - Twelve bp is a multiple of 3, so it is arithmetically in-frame (4 codons). Only the Discussion calls both lines "frameshift loss-of-function deletions ... predicted" to give absence or severe truncation.
  - Protein was not measured (see below), so "null" is a prediction.
  - Suggested wording: "stxbp1a 4-bp frameshift; stxbp1b 12-bp deletion described as loss of function; protein not measured".
- "Protein not measured": STANDS (Discussion: "unable to directly assess stxbp1a or stxbp1b protein levels ... lack of suitable validated antibodies").
- "Bath concentration bounded by larval toxicity": STANDS, with a flag.
  - Fig 1C (48 h survival of WT larvae): 10 and 25 µM 100%; 50 µM about 70%; 75 µM about 62%; 100 µM about 10%; 250 µM and 1 mM 0%.
  - Text: toxic "above 50 µM"; 25 and 50 µM are "the highest non-toxic range".
  - Inconsistencies in the paper: the Fig 1D legend says 4-PBA at 10 and 25 µM, while Results, Methods and Table S1 say 25 and 50 µM. The 50 µM arm already shows about 30% mortality in Fig 1C. The C. elegans effective dose was 5 mM.
- "Assay separation of controls unestablished": STANDS.
  - Table S1, Fig 1A: stxbp1a 277 mm vs tetracaine floor; stxbp1a vs tetracaine P = 0.9983. The text says the mutant is "similar" to tetracaine-treated WT and that the floor is about 279 mm.
  - Methods: Z'-factor = -5.936, which the paper calls "satisfactory". A negative Z' normally means the control distributions overlap.
  - There was no positive-control rescue compound.
  - PTZ failed to raise mutant movement.
  - Table S1 internal flaws: the tetracaine mean is printed as 63.38 (a copy of the WT SEM; the text implies about 279); concentrations are labelled "mM"; panel labels do not match the legends (1B MK-801 and caffeine versus PTZ).
- "INCONCLUSIVE for a protein-expressing missense allele": STANDS (Discussion: the findings "may not exclude a potential role for 4-PBA in STXBP1 patients harboring specific missense variants").

## One-line table
S1a | MUST CHANGE | only 4/10 ligands raised protein (ZK93423 lowered it); current tested for 2 only, HEK293T only, not in iPSC
S1b | ADD | binding of Hispidulin/TP003 is literature-based, not measured; 6/10 binders did not rescue
S1c | ADD | "binds" is asserted, not measured; "best-instrumented" is untestable here; ledger metadata not judged
S2a | MUST CHANGE | glycerol rescued G443D in HEK293 (Fig 3B, 4D-E), so "class ... NOT G443D" is true only for 4-PBA
S2b | MUST CHANGE | WT hGAT-1 expression unchanged in Drosophila (Fig 6B); rise is HEK293 only and blots are unquantified
S2c | STANDS | all arms match Fig 6G/6H/6C/6E, Supp Fig 4C, Fig 3B
S3a | ADD | current only D219N and G251D; mRNA control only D219N; iPSC = surface staining with IXA62/554 only; G251D IXA105 surface biotinylation NS
S3b | ADD | paper notes 25 µM toxicity and tests WT α1 and CHOP, but has no viability, other-client or in vivo data
S4 | ADD | stxbp1b 12-bp deletion is in-frame by arithmetic; 50 µM about 70% survival; dose labels inconsistent; rest supported
S5 | NOT JUDGED | sentence text missing from the file (file ends at the "## S5 (folder E)" heading)

## Report 2 (S5 and S2a re-judged)

ADV-292 INC1 addendum from the blind verifier (sonnet, high). It covers the S5 judgement and a two-reading re-judgement of S2a. The earlier verdicts for S1a-S4 are unchanged and are not repeated. Nothing was written to any file. I read only folder E for S5 and only folder B for S2a. The one exception is the S5 text itself, in `SENTENCES_ADV292_INC1.md`.

## Part 1. S5 (folder E: Ahuja et al., Lab Chip 2026, 26, 1915, MyeliMAP)

What the folder holds: a single 15-page PDF, so the supplementary information is not held (Tables S1/S2, Figs S1-S4, Videos S1-S2 are referenced only). I read the full text, Fig 1 (geometry), Fig 3 (TEM) and Figs 4-5. I rendered Fig 5 at 400 dpi and calibrated the axes from the tick pixels.

**Figure readings (Fig 5, weeks 2-8, mean ± SEM, human iPSC-derived cultures).** The unit is networks (n = 15) from N = 5 HD-MEA chips. The conduction-velocity unit is m/s.

| Quantity | S5 claim | My reading | Reading error |
|---|---|---|---|
| Fig 5e, week 8, coculture | about 0.36 m/s | 0.358 | +0.002 |
| Fig 5e, week 8, monoculture | about 0.27 m/s | 0.269 | +0.001 |
| Fig 5c, week 8, monoculture | about 3.15 responses per microchannel | 3.15 | 0.00 |
| Fig 5c, week 8, coculture | about 1.2 responses per microchannel | 1.22 | −0.02 |

- The axis ticks in panel e are 0.40, 0.35, 0.30 and 0.25 (pixel y = 203, 346, 489, 633). The week-8 markers sit at y = 324 (coculture) and y = 577 (monoculture).
- The axis ticks in panel c are 4, 3, 2 and 1 (pixel y = 213, 354, 495, 636). The week-8 markers sit at y = 333 (monoculture) and y = 605 (coculture).
- My own reading uncertainty is about ±0.005 m/s and ±0.03 responses.
- Significance at week 8: speed ***, responses ****. The speed difference is significant only from week 6 (week 6 *, week 7 *, week 8 ***). Monocultures show more responses from week 4 onward (week 4 *, week 5 ****, weeks 6-7 ***, week 8 ****).

**Per-claim verdicts (paper content only).**
1. "Human induced neurons with or without induced oligodendrocytes on a microfluidic electrode platform, no WWOX perturbation, no tested drug": STANDS.
   - iNGN2 neurons come from the hDFa90/1.2 iPSC line. iSOX10 OPCs come from Sigma-iPSC0028 (female), a different line from the neurons.
   - They are cultured in a PDMS microfluidic network on an HD-MEA (MaxOne).
   - Doxycycline and 1 µM SAG are used in differentiation only. No drug is tested and there is no WWOX manipulation.
   - The oligodendrocyte-lineage cells are OPCs that mature partly; the paper says myelination is "partial rather than complete".
2. "At week 8 the plotted means are about 0.36 against 0.27 m/s (co-culture against monoculture)" (Fig 5e): STANDS (see table).
3. "About 1.2 against 3.15 detected responses per microchannel, same figure" (Fig 5c): STANDS (see table).
4. "The authors state that monocultures showed more responses and attribute it to axon excitability, axonal density or arrangement": STANDS.
   - Results: "Neuron monocultures consistently showed a higher number of responses compared to cocultures, likely reflecting differences in axon excitability or axonal density (Fig. 5c)".
   - Discussion: "likely reflecting differences in axonal arrangement ... the physical presence of iSOX10 OPCs ... can partially obstruct axonal trajectories or alter their spatial distribution".
   - The attribution is hedged ("likely").
   - The paper itself defines the number of responses as "reflecting recruited axons present near the recording electrodes".
5. "Speed is the latency at the start of the stimulation train over one path length (1,960 micrometres) assumed for every point": STANDS.
   - Methods: "latency, defined as the time delay between the stimulus and the induced response at the recording site, at the beginning of the stimulation".
   - Methods: distance "approximated to be 1960 μm for all data points, based on the theoretical measurement of shortest possible path and longest possible path".
   - The chamber is 1.96 mm long (Fig 1).
   - The authors also say real routes are non-linear and longer: the open chamber lets axons grow "in non-linear trajectories", and residual Matrigel creates "longer, less direct conduction routes".
   - A numeric note, not an error in S5: 1960 µm over the week-8 mean latencies (Fig 5d: monoculture about 7.45 ms, coculture about 6.05 ms) gives 0.263 and 0.324 m/s. The plotted means are 0.269 and 0.358.
   - So the plotted velocity is not 1960 µm divided by the mean latency. It is presumably a mean of per-unit ratios, and the paper does not state the averaging unit.
6. "Clusters are not tied to identified axons": STANDS as a statement about the paper text.
   - Methods: one electrode per microchannel, spikes within 0.5-30 ms of the artifact, "extracted from the voltage trace" and "each induced response ... extracted via a clustering algorithm" (reference 20).
   - I searched the article for single/identified/individual axon and clustering. The only linkage to axons is the interpretive phrase "responses (reflecting recruited axons present near the recording electrodes)".
   - The details of the clustering are in reference 20, which is not in the folder, so beyond the text the negative is UNSETTLED.
   - The paper also says directionality "was not explicitly analyzed" and that stimulation might evoke backward propagation via synaptic connectivity.
7. "Monocultures are in separate devices": STANDS. Discussion: "neuron monoculture conditions were established in separate devices".
8. "Two co-culture networks were excluded for missing stimulation artifacts": STANDS. Methods: "defective stimulation with missing artifact ... (two coculture PDMS microfluidic network)".
   - Unreconciled in the paper: the Fig 5 legend still gives n = 15 for both conditions. The Methods give "6-15 networks per condition".
9. "Electron microscopy is shown only for co-culture as representative images": STANDS.
   - Fig 3 caption: week 6, "Representative images from N = 2 independent experiments ... coculture with n = 6 PDMS microfluidic networks".
   - Methods: the TEM samples were glass-bottom dishes, not the HD-MEA chips that were recorded.
   - The Discussion says unmyelinated axons were seen by TEM, "data not shown".
   - I found no monoculture TEM (searched for TEM, electron and ultrastruct alongside monoculture).
10. "A faster speed summary can sit beside a smaller responding set; the paper neither shows nor excludes that this explains its speed difference": STANDS.
    - Fig 5c and 5e show exactly this pairing at weeks 6-8.
    - The paper ascribes the speed difference to myelination ("coinciding with the appearance of compact myelin") and gives no analysis of responding-population differences. Myelin was assessed qualitatively and in coculture only.
    - It does acknowledge incomplete myelination and the path-geometry limits.

**Interpretive sections (not judged).** Estimands (a)-(d), the rule, the "stage and tract controls", the energy lead of the portfolio and the Codex review are repository interpretation. Two phrases lean on paper facts, and both check out:
- "distal arrival": Fig 5a places the recording at the opposite microchannel set.
- "viable axons that can be followed": the paper does not follow identified axons, which agrees with claim 6.
- "A subset with fewer distal successes" assumes the coculture responders are a subset of the monoculture responders. The paper does not show or test that.

**S5 verdict: STANDS.** Every statement about the paper's contents is supported, and the figure readings are within graph-reading error. Optional wording additions are the TEM-on-glass-dishes point (item 9) and the authors' own path-geometry caveat (item 5).

## Part 2. S2a re-judged (folder B: Shah 2025, HEK293 and Drosophila glia)

Repository wording: "The class rescued the fully retained variant and NOT the partly trafficked G443D; the rescued variants recover part of wild-type capacity with altered affinity; wild-type capacity is raised too."

Chaperones this paper tests:
- 4-PBA, glycerol 10%, and DMSO 2% (listed by the authors as a "non-specific chemical chaperone"). The others are ligands, noribogaine, HSP70/90 blockers, lumacaftor and liothyronine.
- Bile-acid chemical chaperones are not tested in folder B. I searched the full article text for bile, TUDCA, UDCA, ursodeoxy and tauroursodeoxy and found no hits. I also viewed Supp Figs 1-4. Anything about bile acids cannot rest on this paper.

Data used (Shah 2025):
- Fig 3A, WT uptake, % of untreated: 4-PBA about 180 (*); glycerol about 115 (NS); DMSO about 105 (NS).
- Fig 3B, G443D uptake, % of WT: glycerol about 6 (***); 4-PBA about 1.6 (no mark); DMSO 0.
- Fig 3C, G443V uptake, % of WT: 4-PBA about 8 (***); glycerol about 5 (**); DMSO about 0.6 (NS).
- Fig 4 kinetics, Vmax (pmol per 10^6 cells per min) and Km (µM):

| Condition | Vmax | Km |
|---|---|---|
| WT control | 298 | 6.5 |
| WT + glycerol | 556 | 12.7 |
| WT + 4-PBA | 812 | 5.7 |
| G443D + glycerol | 165 | 22.9 |
| G443V + 4-PBA | 116.5 | 39.2 |

- Mature bands rise for G443D with glycerol (Fig 4E) and for G443V with 4-PBA (Fig 4G). The WT blots in Fig 4B/C are unquantified.
- Flies (ALRM-Gal4 astrocytes, 3-5-day-old males, 1 mM 4-PBA or 10% glycerol for 48 h):
  - G443V antennal-lobe volume rose about 14-fold with 4-PBA (Fig 6I, ***); glycerol had a minor effect.
  - G443V seizures: about 43% of flies in control and about 20% with 4-PBA (***); glycerol about 32% (NS).
  - G443D seizures were unchanged by either compound (Fig 6G).
  - WT and G443D expression was not altered (Fig 6B, C).

**Reading (i): "class" = 4-PBA only. Verdict: ADD.**
- "Rescued the fully retained G443V": STANDS.
  - HEK293 at 10 mM: Fig 3C (***), Fig 4F-G, Vmax 116.5 with Km 39.2.
  - Flies at 1 mM for 48 h: Fig 6D/I (14-fold), Fig 6H (seizures 43% to 20%), Fig 6F (presynaptic).
- "NOT the partly trafficked G443D": STANDS.
  - HEK293: "failed to mend the expression or activity" (Fig 3B, about 1.6% of WT, unmarked).
  - Flies: seizures unchanged (Fig 6G). G443D flies already show WT-like expression, so the fly arm does not test trafficking.
  - The HEK293 test was a single concentration (10 mM, 24 h). There was no kinetics or Endo H blot for 4-PBA on G443D.
- "Part of wild-type capacity with altered affinity": STANDS.
  - Vmax is 39% of untreated WT (116.5/298), or 14% of 4-PBA-treated WT (116.5/812).
  - Km is 39.2 against 5.7 or 6.5.
- "Wild-type capacity is raised too": STANDS for HEK293.
  - Fig 3A (*); Vmax 298 to 812; the mature band rises on the unquantified blot (Fig 4C).
  - It is NOT true in Drosophila, where WT expression was unchanged (Fig 6B).
- What to add: "HEK293 (10 mM, 24 h); fly glia (1 mM, 48 h); WT increase HEK293 only".

**Reading (ii): "class" = 4-PBA plus any chemical chaperone tested (glycerol; DMSO if counted). Verdict: MUST CHANGE.**
- "NOT G443D" is contradicted. Glycerol rescued the partly trafficked G443D in HEK293:
  - Fig 3B: about 6% of WT uptake (***).
  - Fig 4D: Vmax 165, Km 22.9.
  - Fig 4E: more mature band.
- "Rescued the fully retained G443V" holds for glycerol in HEK293 only (Fig 3C, about 5%, **). In flies glycerol gave a minor expression gain and a non-significant seizure change (about 32% against about 43%, NS). DMSO did not rescue G443V.
- "Wild-type capacity is raised too" is not shown for glycerol or DMSO in the screen (Fig 3A, both NS). Only Fig 4A shows a Vmax rise with glycerol (298 to 556, Km 6.5 to 12.7, no statistics).
- Corrected wording under (ii): "4-PBA rescued the fully retained G443V but not the partly trafficked G443D; glycerol, an osmolyte-type chaperone, rescued G443D (and G443V in HEK293), so the partly trafficked branch is outside 4-PBA's reach, not the reach of every chemical chaperone."

Mapping to my first report: the original bracket (4-PBA plus the other chemical chaperone) is reading (ii), so my earlier MUST CHANGE stands for that reading.

## One-line table
S5 | STANDS | all paper-content claims verified; figure readings 0.358/0.269 m/s and 3.15/1.22 responses within graph-reading error; TEM was on glass dishes (Methods), coculture only (Fig 3)
S2a (i) class = 4-PBA only | ADD | G443V rescued, G443D not (Fig 3B-C, 6G-H); WT rise is HEK293 only (flies unchanged, Fig 6B); doses 10 mM vs 1 mM
S2a (ii) class = 4-PBA + other chemical chaperones | MUST CHANGE | glycerol rescued G443D in HEK293 (Fig 3B, 4D-E); WT rise not shown for glycerol/DMSO in Fig 3A; no bile acids tested in this paper
