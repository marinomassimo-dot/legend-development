# IT7 package P4 verifier report: context concordance and discordance matrix

Independent verification of the P4 folder `disease-models/wwox/research/drug_repurposing/context_differences_it7_p4_20261029/`
(README, `context_matrix.tsv` 168 rows by 19 columns, `check_context_matrix.py`). Verifier did not produce the work. Transcript level; nothing here is medical advice.
Paper checks use the full texts already held in the repository's full-text store (the papers themselves) plus PubMed metadata.

## 1. Recomputation

- Producer checker: `python3 -I check_context_matrix.py` prints "rows 168, source-keyed 67, UNKNOWN 78" and "PASS all checks".
- Independent recomputation: all 67 source-keyed cells re-read from the cycle tables with separate code (effect value, in/out of matched null, direction-vs-null consistency). 67 of 67 agree. One label/null tension: Q08/HNPC_KD is OUT_NULL (by about 0.011) but labelled `no_resolvable_sign` (README section 7 discloses it).
- Raw re-computation: both GEO TPM files re-fetched; SHA-256 of both files and of the Ensembl release-92 cDNA key match the committed sums. Own code (transcript-to-gene sum, universe mean TPM >= 1 in both arms, log2 with 0.5 pseudocount, median centring, per-animal log2 score minus per-animal universe median):
  - Set means (centred): H_S +0.135, H_N -0.134, H_null -0.019, C_S +0.051. All match the table.
  - Wwox depth: 85, 94, 91 and 68 percent lower. Match.
  - Atf4 centred: -0.16, -0.71, -0.39, -0.51. Ldha H_N -1.01. Match. (Pdk1 C_S: -0.09 here vs -0.10 in README text; rounding only.)
  - Leave-one-animal-out on animal scores: H_S +0.091 (min -0.061, max +0.231), H_N -0.126 (-0.262, +0.009/+0.011), H_null +0.012 (-0.050, +0.075), C_S +0.092 (+0.033, +0.156). README table reproduced (rounding only).
- Raw-TPM facts that matter for interpretation: Atf4 TPM in controls is S-ctrl 47.7, N-ctrl 49.6, WT 35.8; knockouts S 32.5, N 25.2, null 23.5. Ldha N-ctrl 269.6 vs WT 114.9 vs N-KO 112.1.

## 2. Paper checks (source_paper_carried cells and carried statements)

| # | Claim | Verdict | Note |
|---|---|---|---|
| 1 | Organoid astrocytosis at weeks 15 and 24 (README D5, section 7) | SUPPORTED, and the open item is answerable | The report is Steinberg 2021 (PMID 34268881), not PMID 42397075. Assay: GFAP and S100B immunofluorescence at weeks 15 and 24 (WT W15 n=9 from 3 batches, KO 16 from 3), qPCR of astrocytic markers, immunoblot at week 20/24 (KO n=4 from 1 batch). The paper itself warns that GFAP also marks radial glia, abundant at week 15, so early-stage GFAP is noisy. README lists "which marker and assay" as UNVERIFIED; it is stated in the paper. |
| 2 | Q14/ORG_KO higher spontaneous activity week 7 | SUPPORTED | Same paper: LFP at week 7, KO higher. Recording n is 14 slices (WT 5 organoids, KO 8), not "4 KO vs 2 WT libraries" (the RNA-seq n in the cell). Paper also reports KO activity decreasing over time. |
| 3 | P47T Gfap-positive about 39 then 56; Iba1-positive about 34 | SUPPORTED as absolute cell counts, NOT percent increases | Fig. 4b/3b bars: Gfap+ cells WT about 25 and 27 vs P47T about 39 (80 d) and 56 (250 d); Iba1+ WT about 22 vs about 34 at both ages. Area fractions are separate (Gfap about 24 and 40 percent). Each data point is a subfield (about 9 points) from n=3 mice per group, and tests are on those points, so the paper is pseudoreplicated; the matrix does not say so. Numbers are not in the text, only in the figure. |
| 4 | P47T heterozygote "no differences (data not shown)" | SUPPORTED | Verbatim. |
| 5 | P47T chronic spontaneous seizures in adults | SUPPORTED | Video EEG, n=3 per genotype, more than 4 seizures per 24 h in each homozygote. |
| 6 | Fly Atf4 immunofluorescence higher only with Abeta42 (U 0, P 0.0022) | SUPPORTED | Unit of n is brains (N=6); the matrix says "individual fly (imaging)". The Atf4-unchanged cell without amyloid (t 0.0894, P 0.9305) and the "1.0 to 1.2-1.3 relative" magnitude are in supplementary panels not available here: UNVERIFIABLE. |
| 7 | Fly lactate interaction F 23.606, padj 0.0174, +1.30 log2; Ldh +1.29 log2 over Abeta42 alone | SUPPORTED | Also Abeta42 alone raises Ldh by 1.19 log2 (README says about 1.1). Lactate rises "only when Abeta42 was also present". Metabolomic pool count: UNVERIFIABLE here. Lactate -0.43 log2 in the knockdown-alone cell: UNVERIFIABLE (supplement). |
| 8 | Fly ATP flat | SUPPORTED | No differences for knockdown, Abeta42 or interaction, N=4. |
| 9 | Rat GFAP-positive cells about half of wild type from PND 5; Iba1 equal at PND 5 then lower; GFAP western lower at PND 15 only | SUPPORTED | Number lower PND 5 to 21 (GFAP), Iba1 cells lower PND 10 to 21, Iba1 western lower at all ages. |
| 10 | Rat Wwox absent from microglia; sound-evoked seizures after PND 16 second-hand | SUPPORTED | Both as stated; seizure statement is cited from earlier work. |
| 11 | Null mouse IBA1 and GFAP area up, Il6 up at 2 weeks | SUPPORTED (text) | Il6 above 1.5 fold, significant; Tnf not. The "3.7 to 23.7" and "4.5 to 7.6" values come from a supplement of a different paper: UNVERIFIABLE here. |
| 12 | hNPC resazurin readout lower | SUPPORTED, with a correction | PrestoBlue (resazurin) "mitochondrial redox potential" in shWWOX hNPC, 5 h kinetics, unpaired t test. It is a redox readout, as the cell says. |
| 13 | hNPC "knockdown of undemonstrated depth" and "control shScrambled vs untransduced not stated" | NOT SUPPORTED as phrased | The paper states the control cells carried a scrambled shRNA and that silencing was confirmed by Western blot (supplementary). Only the GEO record is silent. The depth is not quantified in the text, but "undemonstrated" and the control question are answered in the source. |
| 14 | Patient organoids: WOREE and SCAR12 both hyperactive at week 7; AAV9 normalises firing at week 16 | SUPPORTED, with omissions | Readout at week 16 is calcium imaging, not electrophysiology. At week 16 WOREE firing is about 3 fold higher than SCAR12, versus similar at the earlier time point. This line difference is not in the matrix. |
| 15 | Layer-marker response: rise in WOREE after AAV9, not in SCAR12 (already WT-like) | SUPPORTED | Verbatim; also WOREE CTIP2 and SATB2 lower than WT at baseline. The matrix says the baseline direction is "not carried"; it is. |
| 16 | "Radial-glia abnormalities present in patient-derived organoids, not corrected" (Q10/ORG_PT) | OVERSTATED | RG expansion is reported for knockout and WOREE; SCAR12 shows an RG population similar to WT. AAV9 did not change RG genes in WOREE. |
| 17 | "One patient line per lesion class" (README sections 1, 4 D4, 6, CH7) | NOT SUPPORTED | The 2026 paper uses patient lines from two SCAR12 and three WOREE individuals (previous lines plus new compound heterozygous lines), with isogenic knockouts. The AAV9 comparison may use one each, but the cohort is larger. |

## 3. Discordance explanations (README section 4) and CH1 to CH8

Good: each row names a separating datum, no explanation is excluded outright, and the statuses are mostly proportionate. CH4 is well founded (N-control Ldha 269.6 TPM vs WT 114.9; N-KO 112.1 is at WT level). CH2, CH3, CH5, CH6 each name a comparison not yet made and what would weaken them.

Defects:
- D6 "Control group: NOT SUPPORTED" is overstated. Control-vs-control Atf4 values (+0.04, +0.16, -0.11) are as large as the S-contrast effect (-0.16). Raw TPM shows the Cre-line controls sit above wild type (47.7 and 49.6 vs 35.8 TPM) while S-KO (32.5) is about 9 percent below wild type. Q01/MS_HIP `lower` and the "lower in all four mouse contrasts" reading rest partly on the control group. Only the null contrast (against wild type) is clean of this.
- D1 "lesion class" and "technical/mode" lines say the knockdown depth is unproven and the control state unknown; both are partly answered in the source paper (item 13).
- D4 and CH7 premise "one line per class, baseline not carried" is contradicted by the source (items 15 and 17). CH7's missing comparison (baseline layer markers against wild type, more than one line) largely exists in the paper; the hypothesis should be restated as tested-in-source but confounded by allele type (nonsense/copy-number vs missense), one laboratory, and mixed cohorts.
- D5 cannot-assess items on organoid astrocytosis assay can be closed from Steinberg 2021 (IF, qPCR, immunoblot; GFAP also marks radial glia). The "GFAP flat in deposited libraries" discordance is then explained at least in part by marker (GFAP in radial glia at week 15) and by assay (protein/IF vs bulk transcript).
- D3 and CH6 are reasonable; the "technical" explanation for mouse mito-translation is supported by control-vs-control values (+0.23, +0.38, -0.13).
- README section 6 (cell-type targeting) says germline-contrast differences in progenitor, neuronal, UPR and glycolysis sets reflect control differences "by as much as the deletion". Control tables: UPR (CC_SW -0.65, CC_NW -0.55 vs null -0.30) and OXPHOS yes; progenitor (control contrasts -0.13 and -0.02 vs null +0.29) and neuronal (+0.25 vs control contrasts -0.38, -0.42, opposite sign) no. The claim is true for UPR and OXPHOS, not for Q10 and Q11.

## 4. Labels against the source verdicts

- Q04/MNULL_HIP is `lower`, but UPR_branches is also outside the null in CC_SW and CC_NW with larger values; by the folder's own vocabulary it is `lower_non_specific`.
- Q08/MS_HIP and Q08/MNULL_HIP are `lower`, although the source verdict says all three control-vs-control contrasts are outside the null for OXPHOS.
- Q12 all four `lower`: the source verdict was "NOT MOVED" because control-vs-control CC_NW and CC_SN are outside the null and the ribosome control moves; the effects (-0.8 to -1.8) are much larger than control differences (-0.44, +0.15), so `lower` is defensible, but the README should say it departs from the source verdict.
- Q14/MNULL_HIP and Q13/MNULL_HIP carry "n 2 vs 3 animals" although the histology and EEG come from other papers and animals.

## 5. Leave-one-animal-out statement

The README table is a correct recomputation of an animal-score statistic. But the source set_summary.tsv already carries a different leave-one-out (gene-mean centred R, drop one animal): all-same-sign is False for H_S, True for H_N, False for H_null, False for C_S. The README's "sign stable only in C_S, unstable in the three hippocampal contrasts" is the reverse for H_N and C_S under the source statistic. The conclusion (no stable ISR sign) is unchanged under both (three of four unstable either way), but the README must say which statistic it uses and that the other gives a different pattern. H_null's animal-score difference (+0.012) has the opposite sign to the pooled centred value (-0.019), which itself shows sign is not assignable.

## 6. Subgroup verdict and forbidden content

- "No subgroup supported" is correct for patients and for the data held. No response label, clinical biomarker or cluster appears anywhere in README or TSV (searched for responder, biomarker, cluster, stratification, subtype, endotype; hits are only the disclaimers). No allele string or individual-level record appears.
- The "Patient line" row is understated for model systems: the source paper itself reports a WOREE vs SCAR12 organoid difference in RG proportion, layer markers and week-16 firing across several lines. That is a candidate model-system class difference (confounded with variant type and laboratory), not a patient subgroup. Wording "no subgroup is supported ... for model systems" should be narrowed to "no subgroup survives resampling in the held transcript data; one source-reported class difference exists and is untested for replication".

## 7. About six independent systems

Defensible as a count of models (organoid, shRNA hNPC line, mouse deposit, fly, rat, P47T) but loose as independence: the organoid and patient-organoid columns share a laboratory (declared); the P47T mouse and the mouse deposit are very likely from the same group and pipeline (the deposit has no linked paper, so this is UNVERIFIED either way); fly knockdown results are mostly amyloid-dependent and not WWOX-DEE evidence. For Q14 "concordant in every measured system", independent evidence is organoid, mouse, P47T and patient organoids (one laboratory for two of these), with rat second-hand and sign-only. The readouts also differ (LFP power, video seizures, ECoG spikes, slice bursts, calcium imaging), so "concordant" means same direction of a function-level hyperexcitability readout, not same measurement.

## 8. Severity-ranked defect list

1. HIGH. Atf4 control-group explanation marked NOT SUPPORTED (D6) while control contrasts equal the S effect and the Cre-line controls are above wild type in raw TPM; Q01 labels `lower` for MS_HIP and MN_HIP and the README "mouse-only decrease" overreach.
2. HIGH. "One patient line per lesion class" and "baseline direction not carried" contradict the source (two SCAR12 and three WOREE individuals; WOREE lower CTIP2/SATB2, SCAR12 WT-like); CH7, D4 and the subgroup row rest on them. Q10/ORG_PT overstated for SCAR12 (RG similar to WT). Week-16 firing difference (about 3 fold WOREE over SCAR12) missing.
3. MEDIUM. Leave-one-animal-out table presented without noting the source's own leave-one-out gives a different pattern (H_N stable, C_S unstable).
4. MEDIUM. hNPC knockdown "undemonstrated" and control "not stated" contradicted by the paper (Western-confirmed, shScrambled control).
5. MEDIUM. Labels inconsistent with the folder's own vocabulary: Q04/MNULL_HIP, Q08/MS_HIP, Q08/MNULL_HIP (should be non-specific); Q12 departs from the source verdict unannounced; Q08/HNPC_KD outside null but `no_resolvable_sign`.
6. MEDIUM. Section 6 claim that germline-contrast differences in Q10 and Q11 equal control differences is not true for those two sets.
7. LOW. Open items answerable from sources: organoid astrocytosis assay (Steinberg 2021, IF GFAP/S100B, qPCR, immunoblot), P47T values are counts not percent increases (and pseudoreplicated subfields), fly Atf4 n is brains.
8. LOW. The astrocytosis paper is PMID 34268881; PMID 42397075 (2026) is the patient-organoid paper. The cell and README should name the correct PMID per claim.
9. LOW. n columns for histology/EEG-derived cells (Q13 and Q14, MNULL_HIP and ORG_KO) show the RNA-seq n; the unit mismatch should be flagged.
10. LOW. "About six systems" is a count of models, not of laboratories; state that Q14 concordance combines different readouts and two same-laboratory pairs.

Unverifiable at the source here: fly Atf4-unchanged cell and its relative magnitudes, fly lactate in knockdown alone, metabolomic pool counts (supplement or unreleased deposit); null-mouse GFAP and Iba1 percent-area values (supplement of another paper).
