# Pre-declaration, IT10 P2.4 (scientist-b), written 2026-10-30 BEFORE any trial output was opened

Exploratory, computational, not medical advice. Reference genotype class: a WWOX-DEE genotype class; no individual-level record.
What had been seen before writing: the IT9 v3 README and candidate-file headers, the GSE156243 declaration, the JUMP bucket listing and metadata column names (WWOX is present as one CRISPR gene id and one ORF id). NOT seen: any profile value, any similarity, any Enrichr output.

## Trial 1 (logic 12, cell morphology, JUMP Cell Painting)
* Question: does WWOX knockout (CRISPR, JUMP U2OS) give a morphological profile that is reproducible beyond a gene-matched null, and, if so, which compounds have a profile opposite to it? WWOX-only input (no seed from Q2, Q5 or Q6); the questions enter only at the comparison step.
* Reference state: WWOX-CRISPR wells versus the non-targeting / no-guide negative-control wells of the same plates, in the JUMP "ALL v1.0c" assembled profiles (wellpos, cc, var, mad, outlier, featselect, sphering, harmony, PCA, corrected; 232 PCs). WWOX profile = mean of its wells. Same for the WWOX ORF (secondary, a "restoration-like" direction).
* Universe: every compound JCP2022 id with wells in that file (DMSO excluded), compound profile = mean over its wells; require wells on >= 2 distinct plates.
* Comparison: cosine of each compound profile with the WWOX-KO profile; "opposing" = negative. Specificity null: the same cosine against the profiles of 1,000 randomly chosen other CRISPR genes (seed 20261030); per compound z = (cos_WWOX - mean_null) / sd_null.
* GATE (decided before ranking): WWOX reproducibility = mean pairwise cosine among WWOX-KO wells from distinct plates, versus the same statistic for 1,000 random CRISPR genes. Pass only if WWOX is at or above the 95th percentile of the null. If the gate fails, the outcome is INCONCLUSIVE-NO-DETECTABLE-PHENOTYPE, the ranking is not interpreted and no candidate is reported (the file is stored for transparency only).
* Method control: PLK1 knockout (a JUMP positive control), same pipeline; expectation: at least one known PLK1 inhibitor (BI-2536, volasertib, GSK461364, onvansertib, rigosertib, TAK-960, ON-01910) among the 100 compounds with the highest positive z, matched by InChIKey skeleton to the repository catalogue by name. Failing the control means the pipeline, not the biology, is the limit.
* Specific opposer (only if the gate passes): z <= -3 and among the 100 most negative z. Specific mimic: the mirror image.
* Evaluation measure: gate result; control result; number of specific opposers; for each, a map to the repository catalogue by InChIKey skeleton (first block); overlap with (a) all compound families listed in generation_it9_p2_20261030/v3/results/candidates_Q2, Q5, Q6 (all arms), (b) the SigCom S1 top-100 reversers (gse156243/derived/sigcom_reverser_summary.tsv). Newness = a catalogue-mapped opposer in neither set.
* Independence: JUMP shares no data with OmniPath/SIGNOR/CollecTRI, none with the WWOX expression data, none with L1000. It shares only the compound identifier mapping. It is a cancer cell line (U2OS), not neural; WWOX expression in U2OS is not verified here. Concordance with the propagation, if any, is not a confirmation of benefit.

## Trial 2 (logic 3, perturbation-signature reversal, a library of a different lineage)
* Question: using the same declared input as the SigCom route (gse156243/derived/query_sets.json: S1 primary, S3 composition-sensitivity, S0 random control, plus the direction-shuffled S1P and S1P2), do drug-perturbation signatures extracted from GEO studies (Enrichr "Drug_Perturbations_from_GEO_up" and "_down", 906 terms; a curation of single GEO experiments, not L1000) reverse the WWOX-knockout organoid signature more than the controls do?
* Reference state: WWOX-KO versus WT organoid, week 15, as already declared; Q2 guard (IT7_READOUT6) noted: the run does NOT score reversal of the six-gene IT7 readout; S1 is a 834-gene set, six of whose genes may appear in it, and no score is computed on those six alone.
* Universe: the 906 terms of the pair of libraries (the service's own gene background, not ours).
* Comparison: reverser score of a term = adjusted p of S1-up in the "_down" library + adjusted p of S1-down in the "_up" library, both as -log10(adjusted p) summed; a term counts only if both arms have adjusted p < 0.05. Terms are reported with their organism/tissue/cell annotation as the term string gives it, never pooled.
* Evaluation measure: number of both-arm terms for S1 versus S0, S1P, S1P2 (a result counts as specific only if S1 has at least 3 times the number of both-arm terms of the largest control, and at least 3); the share of S1 both-arm terms that carry a neural or brain annotation; the overlap of compound names with the SigCom S1 top-100 and with the IT9 v3 candidates (Q2, Q5, Q6). If the controls give as many both-arm terms as S1, the outcome is NO-ADVANTAGE (library responds to the query protocol, not the signature).
* Independence: GEO-extracted signatures are another lineage from L1000, but the CREEDS/Enrichr curation may include some of the same compounds studied in cancer lines; concordance with SigCom is reported as concordance of two libraries, not a confirmation; neither is WWOX evidence.
* Only gene symbols are sent to Enrichr (no e-mail, no identity).

## Common
* Outcome vocabulary: NEW-INFORMATION / KNOWN-RE-FOUND / NO-ADVANTAGE / INCONCLUSIVE (with cause).
* Any deviation will be listed in the README as a deviation, not edited here.
