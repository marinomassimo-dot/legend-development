# Context differences and subgroup hypotheses: a concordance and discordance view across WWOX-loss systems (IT7 package P4, roadmap R4)

Scientist-b, 2026-10-29; revised after the independent verifier report (`locator_audits/2026-10-29_it7_p4_verifier.md`). Exploratory, computational and descriptive. **Transcript level except where a row says otherwise. Nothing here is medical advice.**
Association is not modulation and modulation is not rescue. The reference genotype class is a WWOX-DEE genotype class; no individual-level record is used and none is
inferred. **No response label is assigned to any patient, no computational cluster is turned into a clinical biomarker, and no subgroup is supported by these data (section 6).**
Missing data are not biological absence. Arms with n=1 are descriptive. This cycle opened no primary source and downloaded nothing: every cell comes from an existing cycle
output (named in the `source_ref` column), and every number that came from a local table is re-read from that table by `check_context_matrix.py`. Paper-derived cells are carried from
the cycle texts and are marked `source_paper_carried`; a verifier should treat them as claims to re-check at the source, not as readings made here.

Reused, not repeated: GSE126075 (hNPC and neuron CAGE), GSE156243 (organoid RNA-seq), GSE158681 and GSE158682 (mouse P17), the P10 glial panel, the P3 data census, the P7 rescue-window record,
the P5 function reference, the fly follow-up needs. No LINCS analysis was run. Replicates are never pooled across systems and no combined statistic exists in this folder.

## 1. What is compared

Thirteen contexts (columns) by fourteen pre-declared quantities (rows) give 182 cells, one TSV row each (`context_matrix.tsv`, one header, no trailing notes). A cell holds a direction or UNKNOWN,
the signed centred log2 ratio where a local table gives one, the evidence class, the provenance, the unit of replication, n, the key caveats and the source. The quantities are the
ones the earlier cycles had already computed or carried; none was added after looking at a result.

| Context id | System | Lesion class | Mode of perturbation | Unit of replication, n |
|---|---|---|---|---|
| ORG_KO | human cerebral organoid, week 15 (GSE156243) | knockout by exon deletion (WWOX mRNA not lower) | CRISPR-engineered isogenic knockout, 3D | library; 4 KO vs 2 WT |
| HNPC_KD | shWWOX hNPC, CAGE (GSE126075) | shRNA knockdown, Western-confirmed in the paper (depth not quantified in the text), not visible in CAGE tags | shRNA, clonal 2D line | one library per arm |
| NEUR_KD | same line, day-14 neurons | knockdown about 3 to 4 fold | shRNA | one library per arm |
| MS_HIP | mouse P17 hippocampus, neuron-targeted S (GSE158681) | deletion, Wwox 85 percent lower | Cre-restricted, Cre-line controls | animal; 3 vs 2 |
| MN_HIP | same, progenitor-targeted N | deletion, 94 percent lower | Cre-restricted | animal; 2 vs 2 |
| MNULL_HIP | same, germline null | null, 91 percent lower | germline, WT controls | animal; 2 vs 3 |
| MS_CTX | mouse P17 cortex, neuron-targeted S (GSE158682) | deletion, 68 percent lower, overlapping | Cre-restricted | animal; 3 vs 4 |
| FLY_KD | Drosophila neuronal RNAi, no amyloid | partial knockdown (about 0.55 of mRNA) | pan-neuronal RNAi | head pool or fly; 4 to 6 |
| FLY_KDA | same, with neuronal Abeta42 | partial knockdown on an amyloid background | RNAi plus transgene | head pool or fly; 4 to 6 |
| RAT | rat lde/lde cortex, PND 5 to 21 | 13-base-pair exon 9 deletion | germline mutant | animal; at least 3 per age |
| P47T | mouse P47T homozygote, adult | WW1 missense with residual function | germline knock-in | animal; 5 (RNA-seq) or 3 (histology) |
| ORG_PW | patient-derived organoids, WOREE lines (three individuals), weeks 7 to 16 (PMID 42397075) | severe phenotype, complex heterozygous variants | patient iPSC organoid; add-back vs EGFP | not carried per cell |
| ORG_PS | same, SCAR12 lines (two individuals) | milder phenotype, missense variants | patient iPSC organoid; add-back vs EGFP | not carried per cell |

**Systems are fewer than contexts.** The hNPC and neuron columns are one line in one laboratory. The four mouse columns are one deposit; S, N and null are separate deletions but share stage, assay and, partly, controls.
The organoid column and the two patient-organoid columns come from one laboratory. Fly and rat each count once. Counting models, not columns, there are about six: organoid, shRNA line, the mouse deposit, fly, rat, P47T. This counts models, not laboratories: the P47T mouse and the mouse deposit may come from the same group and pipeline (the deposit names no paper, so this is UNVERIFIED either way), and the organoid and patient-organoid models share a laboratory, so independence in the strict sense is lower still.

Vocabulary of the `direction` column: `higher` and `lower` mean distinguishable from noise by the source's own criterion (outside the matched random-set null, or a stated test);
`*_sign_only` means a sign without that support; `no_resolvable_sign` means the value sits inside noise (the signed value is still in `effect_value`); `*_non_specific` means a lower value that an unrelated
control class or a control-vs-control contrast reproduces; `set_dependent` means the answer changes with the gene set; `sparse` means below the 10-tag rule; `changed_unsigned` means a change was reported without a carried direction; `UNKNOWN` means not measured or not computed in any held output.
Evidence classes: measured_transcript, measured_protein (including histology), measured_metabolite, measured_function (electrophysiology, imaging, a whole-cell readout), inferred, none.

## 2. The matrix at a glance (generated by `python3 -I check_context_matrix.py --wide`)

| Quantity | ORG_KO | HNPC_KD | NEUR_KD | MS_HIP | MN_HIP | MNULL_HIP | MS_CTX | FLY_KD | FLY_KDA | RAT | P47T | ORG_PW | ORG_PS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q01 ATF4 mRNA (single gene) | no_resolvable_sign | no_resolvable_sign | sparse | lower_sign_only | lower_sign_only | lower_sign_only | lower_sign_only | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q02 ISR target set, transcript level | lower | higher | higher | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q03 ISR protein or phospho (ATF4 protein, eIF2alpha-P) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | no_resolvable_sign | higher | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q04 UPR branch set, transcript level | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | lower_non_specific | no_resolvable_sign | UNKNOWN | no_resolvable_sign | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q05 Glycolysis and LDHA, transcript level | higher | set_dependent | higher_sign_only | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | higher | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q06 PDK family and PDK1, transcript level | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | no_resolvable_sign | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q07 Lactate, flux or ATP (functional) | UNKNOWN | lower | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | lower_sign_only | higher | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q08 OXPHOS nuclear transcripts | lower_non_specific | at_null_edge | lower_non_specific | lower_non_specific | lower_non_specific | lower_non_specific | no_resolvable_sign | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q09 Mitochondrial translation transcripts | lower | higher | no_resolvable_sign | no_resolvable_sign | lower | no_resolvable_sign | higher | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q10 Progenitor (radial glia) markers | set_dependent | lower | lower | no_resolvable_sign | no_resolvable_sign | higher | no_resolvable_sign | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | higher | no_resolvable_sign |
| Q11 Neuronal markers | set_dependent | lower | lower | no_resolvable_sign | no_resolvable_sign | higher | no_resolvable_sign | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | lower | no_resolvable_sign |
| Q12 Myelin and oligodendrocyte transcripts | UNKNOWN | UNKNOWN | UNKNOWN | lower | lower | lower | lower | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Q13 Glial reactivity | no_resolvable_sign | UNKNOWN | UNKNOWN | changed_unsigned | UNKNOWN | higher | changed_unsigned | UNKNOWN | UNKNOWN | lower | higher | UNKNOWN | UNKNOWN |
| Q14 Network hyperexcitability or seizures | higher | UNKNOWN | UNKNOWN | higher | UNKNOWN | higher | higher | UNKNOWN | UNKNOWN | higher_sign_only | higher | higher | higher |

Of 182 cells, 93 carry a measurement or a carried report and 89 are UNKNOWN. UNKNOWN cells are gaps, mostly because a context was analysed for a different set of quantities. They are not zeros.

## 3. Reading, quantity by quantity

Concordance here means the same resolved sign in at least two independent systems; discordance means resolved opposite signs; everything else is unresolved, single-system or no data.

| Quantity | Reading | Verdict |
|---|---|---|
| Q01 ATF4 mRNA | flat in organoid and hNPC; sparse in neurons; lower in sign in all four mouse contrasts (centred -0.16, -0.71, -0.39, -0.51; animals separated in S and N). The Cre-line controls sit above wild type (47.7 and 49.6 vs 35.8 TPM) while the knockouts sit below it (S 32.5, N 25.2, null 23.5), and control-vs-control values (+0.04, +0.16, -0.11) are as large as the S effect. | **mouse-only decrease that rests partly on the control group**; only the null contrast, against wild type, is free of it, and it is 2 v 3 animals not separated; not an ISR call (ATF4 is translationally controlled) |
| Q02 ISR target set | organoid lower (-0.33), hNPC higher (+0.64), neurons higher (+1.32, composition-sensitive); mouse inside the null in all four contrasts (+0.14, -0.13, -0.02, +0.05) | **DISCORDANT between the two human systems; mouse does not break the tie; overall UNRESOLVED** |
| Q03 ISR protein or phospho | measured only in fly (Atf4 immunofluorescence unchanged without amyloid, higher with Abeta42); no human or mouse WWOX-deficient neural measure exists | NO DATA where it matters |
| Q04 UPR branches | inside the null in 6 of 7 transcript contexts; one mouse contrast outside (null, -0.30) that equals the size of the WT-versus-Cre-control difference | concordant absence of signal |
| Q05 glycolysis, LDHA | higher in organoid (10-gene HIF-type set +0.53) and hNPC (+0.46 on the same set, but the 19-gene panel is inside the null); neurons at the null edge; mouse inside the null with signs from -0.19 to +0.11; fly Ldh higher only with Abeta42 | human-human agreement only on a hand-picked set; **UNRESOLVED across species** |
| Q06 PDK family, PDK1 | inside the null everywhere; Pdk1 has no consistent sign in mouse (-0.20, +0.32, +0.13, -0.10) | concordant absence of support for a raised PDK1 |
| Q07 lactate, flux, ATP | no neural flux measurement anywhere; raw resazurin lower in hNPC; fly lactate higher only in the amyloid double cell | NO DATA (neural) |
| Q08 OXPHOS transcripts | lower in five contexts, but an unrelated control class or a control-vs-control contrast moves as far in most; cortex +0.15 | **not interpretable as a respiratory signal** |
| Q09 mito translation | organoid lower (-0.15), hNPC higher (+0.28), neurons inside, mouse -0.09, -0.16, -0.04 and cortex +0.11 | **DISCORDANT organoid vs hNPC; mouse mixed** |
| Q10 progenitor markers | hNPC and neurons lower (-1.17, -0.50); organoid set-dependent (+0.38 on 9 genes, +0.11 on four canonical); mouse inside the null except germline null (+0.29) | hNPC drop robust, others unresolved or set-dependent; patient organoids: radial-glia proportion higher in WOREE, similar to wild type in SCAR12 |
| Q11 neuronal markers | CAGE neurons lower (-0.76); hNPC at the null edge; organoid set-dependent; mouse positive in sign in all four contrasts (+0.22 to +0.36) and outside the null once; patient organoids: CTIP2 and SATB2 lower in WOREE, wild-type-like in SCAR12 (layer markers, a different readout) | **UNRESOLVED; mouse sign is the expected composition effect, not a cell-state claim** |
| Q12 myelin, oligodendrocyte | lower in all four mouse contrasts (-1.78, -1.02, -1.66, -0.80), whether the deletion is neuronal, progenitor or germline | single system; no other context was computed |
| Q13 glial reactivity | histology higher in null mouse and P47T, lower in rat, no reactive transcript programme in the week-15 organoid, astrocyte-activation genes shifted in the neuron-targeted deletion. The organoid paper itself reports astrocytosis by GFAP and S100B immunofluorescence, qPCR and immunoblot (PMID 34268881) and warns that GFAP also marks radial glia at week 15 | **DISCORDANT by readout, species and age window; the organoid transcript-versus-imaging difference is at least partly assay and marker specificity** |
| Q14 hyperexcitability, seizures | higher in organoid (field potentials), both patient-organoid classes (calcium imaging; at week 16 WOREE about 3-fold above SCAR12), neuron-targeted mouse (seizures, slice bursts), null mouse (ECoG), P47T (video EEG); rat second-hand | **CONCORDANT in direction; the readouts differ (field potential, calcium imaging, ECoG, video EEG, slice bursts), so this is agreement on a function-level hyperexcitability direction, not on one measurement; independent evidence is organoid, mouse, P47T and patient organoids, two of which share a laboratory** |

The pattern is informative in itself. The function-level quantity (Q14) agrees in direction across every system that measured it, including a residual-function allele and both patient-organoid classes, with the caveat above that the readouts differ. The transcript-level metabolic
and stress quantities (Q02, Q05, Q09, Q10, Q11) are the ones that disagree, and they are also the ones measured in the weakest designs (n=1 CAGE arms, 4 v 2 libraries, 2 to 3 animals, bulk tissue).
Agreement at function level with disagreement at transcript level is compatible with a shared downstream phenotype reached through system-specific molecular states, and equally compatible with transcript noise; the held data cannot say which.

## 4. Discordances, the explanations compatible with the data, and the datum that would separate them

Status words: COMPATIBLE (the data do not rule it out and something in them points to it), PARTLY (compatible for some contrasts only), NOT SUPPORTED (held data point against it, not a proof of absence),
CANNOT BE ASSESSED (no held datum bears on it). No explanation is excluded by these data, and several can act together.

### D1. ISR target-set sign (Q02, with Q01 and Q03): organoid lower, shRNA lines higher, mouse unresolved

| Explanation | Status | What in the data bears on it | Datum that would separate it |
|---|---|---|---|
| Residual function or lesion class (knockout vs knockdown vs deep Cre deletion) | CANNOT BE ASSESSED for the human pair; PARTLY for the mouse | the organoid is an exon-deletion knockout; the hNPC knockdown was Western-confirmed in the paper but its depth is not quantified in the text and WWOX is not lower at tag level; neurons about 3 to 4 fold lower at tag level. Deep mouse deletions (85 to 94 percent, transcript level) give no resolvable sign, so a simple "deeper loss, lower ISR" has no mouse support. A non-monotonic dose response is conceivable and untested | a graded WWOX-depth series with a protein check in one human neural line; or protein-verified depth in the CAGE line |
| Tissue or cellular composition | COMPATIBLE | the ISR genes that carry the shRNA rise (CHAC1, TRIB3, PSAT1, SESN2) are generally responsive to culture and amino-acid conditions (background knowledge, not WWOX evidence); the silenced line also shows SOX2 -1.7, PAX6 -2.9, HES5 -3.1; the organoid composition shifts (non-cortical +1.52 z, neuronal -0.83 z); mouse myelin transcripts fall 1.7 to 3.4 fold | cell-resolved data (the organoid single-cell record E-MTAB-14792 is not accessible and no release request has been sent); or at least three libraries per arm with a composition covariate |
| Developmental stage or maturity | COMPATIBLE for the organoid, CANNOT BE ASSESSED for ISR | the organoid KO has more progenitor-type signal and glycolysis-type genes fall with culture time, but how the ISR set moves with culture time in WWOX-unperturbed tissue has not been calibrated (only the Wnt set and, by the comparison file, the glycolysis genes were) | the ISR set against days in culture in the WWOX-free spheroid series already used for the Wnt calibration (GSE150123); the predicted organoid shift from marker differences can then be compared with the observed -0.33 |
| Mode of perturbation (CRISPR knockout, shRNA clone, Cre, germline) | COMPATIBLE | no context pairs two modes in one background; a clonal shRNA line has clone and integration effects, the paper states the control carries a scrambled shRNA (the GEO record is silent), so the question is clone and integration effects, not control identity | one line with shRNA, knockout and a cDNA add-back, with a transduction-matched control; a rescue arm separates WWOX-dependence from line state |
| Technical (RNA-seq counts vs CAGE promoter sums; library 51.0 M vs 14.3 M tags; 9 to 61 percent of tags in the gene table; n=1) | COMPATIBLE for the CAGE pair, NOT SUPPORTED for the organoid | the organoid sign is solid for 4 v 2 (CHAC1 t -11.6, TRIB3 -4.1, SESN2 -4.3); the CAGE signs rest on one library per arm and a few genes; neuron uncentred sign flips with the -1.3 log2 shift | at least three libraries per arm in one platform |
| Species and in vivo bulk tissue (why the mouse is flat) | COMPATIBLE | Chac1 is 1.5 to 7 TPM, Trib3 below 1 TPM and Sesn2 5 to 8 TPM, so a fall of organoid size cannot be shown; animal-level differences are +0.09 (SE 0.17), -0.13 (0.14), +0.01 (0.07), +0.09 (0.09); the organoid-sized fall is not excluded in the 2 v 2 progenitor contrast | targeted measurement of the three genes at depth, or sorted cells |
| The sign is a transcript sign and the real change is translational | CANNOT BE ASSESSED | no ATF4 protein or eIF2alpha-P exists in any WWOX-deficient neural system; fly Atf4 protein rises only with amyloid | the matched protein and phospho measurement with target mRNA and a transduction-matched control (already written as the next step) |

### D2. Glycolysis and LDHA (Q05): higher in organoid and shRNA progenitors, unresolved in mouse, amyloid-dependent in fly

| Explanation | Status | What in the data bears on it | Datum that would separate it |
|---|---|---|---|
| Residual function or lesion class | CANNOT BE ASSESSED | same depth problem as D1; mouse deletions are deep and show no resolved rise | graded depth with protein check |
| Composition | COMPATIBLE | organoid KO has more progenitor-type signal; mouse bulk shifts toward neuronal fraction when myelin falls | cell-resolved LDHA in matched cell types |
| Maturity | PARTLY | in the organoid the rise is as consistent with a less advanced tissue as with a metabolic change; in the shRNA line progenitor markers fall while the same genes rise, so one shared maturity story does not cover both | culture-time calibration of the glycolysis set in WWOX-free tissue, and a stage-matched shRNA control |
| Mode and control group | COMPATIBLE for the mouse | the apparent Ldha fall in the progenitor-targeted contrast (-1.01) is a control-group effect (N-control vs WT +0.92, S vs N controls -0.51) | a common control genotype across S, N and null |
| Species | COMPATIBLE | mouse P17 bulk tissue, symbol-based orthology of HK, SLC2, LDH families unverified | a human or mouse neural system measured with the same set and a flux readout |
| Context dependence (fly) | COMPATIBLE | fly Ldh and lactate rise only with Abeta42; no human or mouse system carries that load | an amyloid-bearing WWOX-deficient neural system, or the same fly design without it in a second laboratory |

### D3. Mitochondrial translation (Q09): organoid lower, hNPC higher

| Explanation | Status | What in the data bears on it | Datum that would separate it |
|---|---|---|---|
| Residual function or lesion class | CANNOT BE ASSESSED | knockout vs a Western-confirmed knockdown of unquantified depth | graded depth series |
| Composition and stage | COMPATIBLE | effects are small (-0.15, +0.28); the cytosolic-ribosome control moves with them in the organoid (-0.26); the silenced hNPC line differs in progenitor state | stage-matched controls, replicate libraries |
| Technical | COMPATIBLE | library sizes differ 3.6 fold in the CAGE pair; mouse control-vs-control differences for this class (+0.23, +0.38, -0.13) are as large as the mouse effects | at least three libraries; one common control group in mouse |
| Mode of perturbation | COMPATIBLE | knockout vs shRNA | as in D1 |

### D4. Progenitor and neuronal markers (Q10, Q11): hNPC drop robust, organoid set-dependent, mouse sign opposite to the human neuronal fall

| Explanation | Status | What in the data bears on it | Datum that would separate it |
|---|---|---|---|
| Residual function or lesion class | CANNOT BE ASSESSED | the source itself reports a class difference: radial-glia proportion higher in WOREE and similar to wild type in SCAR12, CTIP2 and SATB2 lower in WOREE and wild-type-like in SCAR12, week-16 firing about 3-fold higher in WOREE; lines come from three WOREE and two SCAR12 individuals. The difference is confounded with variant type (complex heterozygous vs missense), individual and batch, and has not been replicated in an independent laboratory | an independent laboratory or isogenic lines that vary variant type alone |
| Tissue composition | COMPATIBLE | mouse neuronal panels rise in sign because myelin transcripts fall (relative composition); the organoid is a week-15 mixture whose composition differs by genotype | cell-resolved data, or a composition-adjusted model |
| Developmental stage | COMPATIBLE | an organoid week-15 mixture, a 2D progenitor line, day-14 neurons and P17 mouse brain are different points on a differentiation axis; the day-14 neurons of the same line still show lower radial-glia markers (-0.50) | a time course within one system with matched controls |
| Mode and clone | COMPATIBLE | the hNPC drop could be a property of the clone (SOX2, PAX6, HES5 down by 1.7 to 3.1 log2) rather than of WWOX | independent clones and a cDNA add-back |
| Gene-set definition | COMPATIBLE | organoid: 9-gene set outside the null because of NES and VIM, four canonical markers inside; mouse: two definitions disagree in sign in one contrast | pre-declared sets fixed before any value is seen (done for the mouse run only) |

### D5. Glial reactivity (Q13): higher in null mouse and P47T, lower in rat, no reactive programme in organoid transcripts

| Explanation | Status | What in the data bears on it | Datum that would separate it |
|---|---|---|---|
| Residual function or lesion class | PARTLY | the residual-function P47T homozygote shows gliosis, so complete loss is not needed; allele differs across rat, null and P47T | the same readout in the same region and age across alleles |
| Seizure-driven rather than glia-intrinsic | COMPATIBLE | the organoid has no microglia and no seizures and shows no reactive programme; the neuron-targeted deletion (astrocytes expected to keep Wwox) already shifts astrocyte-activation genes; the mouse reads are all after seizure onset; P47T is read in seizing adults | a pre-onset (P5 to P8) time course and EEG-coupled glial reads in one species; a seizure-controlled neuron-targeted vs null comparison |
| Tissue, region and cell composition | COMPATIBLE | rat is cortex, null mouse region unstated, P47T hippocampus; rat Wwox is absent from microglia; astrocyte-specific deletion was never scored for gliosis | the same region and assay in all three |
| Developmental window | COMPATIBLE | the rat deficit is present from PND 5 (before sound-evoked seizure competence), all mouse reads are P14 or later | one species, ages spanning the first spike |
| Mode of perturbation and readout | COMPATIBLE | cells per mm2 (rat), area fraction (null mouse), cell number (P47T), bulk transcript (organoid); the organoid paper itself (PMID 34268881) reports astrocytosis at weeks 15 and 24 by GFAP and S100B immunofluorescence, qPCR and immunoblot, while the deposited libraries show GFAP flat (135 vs 154 CPM); the paper warns GFAP also marks radial glia, abundant at week 15, so assay and marker specificity are a likely contributor (the same libraries were not imaged) | the same imaging and transcript readout on the same organoids |
| Technical | CANNOT BE ASSESSED | histology n of 3 per group; antibody and thresholding not compared | blinded, same-pipeline quantification |

### D6. Atf4 mRNA lower in sign in mouse, not in the human systems (Q01)

| Explanation | Status | What in the data bears on it | Datum that would separate it |
|---|---|---|---|
| Residual function | PARTLY | mouse deletions are deep at transcript level while the human organoid keeps the WWOX transcript and the shRNA knockdown depth is Western-confirmed but unquantified in the text | protein-verified depth in all systems |
| Control group | COMPATIBLE for the Cre-line contrasts; NOT SUPPORTED for the null contrast | control-vs-control Atf4 values (+0.04, +0.16, -0.11) are as large as the S effect (-0.16); Cre-line controls are 47.7 and 49.6 TPM against 35.8 in WT, with S-KO 32.5, N-KO 25.2 and null 23.5. The null, the only contrast against WT, is -0.39 but 2 v 3 animals not separated | a common control genotype across the three arms; WT littermate controls for the Cre lines |
| Composition | COMPATIBLE | bulk tissue, myelin transcripts fall | cell-resolved Atf4 |
| Species | COMPATIBLE | no human system with a deep, cell-targeted deletion and bulk tissue exists | -- |
| Meaning | CANNOT BE ASSESSED | one gene, 2 to 3 animals, no animal-level test; mRNA is not activity; the ISR set does not move with it | Atf4 protein and target mRNA in the same animals |

## 5. Contextual hypotheses (UNVERIFIED_HYPOTHESIS; none is a claim about WWOX or a patient)

Each is written so that a named comparison, not yet made, would support or weaken it.

- **CH1. The ISR sign differs between the organoid and the shRNA lines because the shRNA contrast is a contrast of differently staged clones, and stress-responsive genes (CHAC1, TRIB3, PSAT1, SESN2) follow culture state, whereas the organoid contrast is isogenic.**
  Missing comparison: ISR-set behaviour against culture time in WWOX-free tissue, and an shRNA line with a cDNA add-back and a transduction-matched control. Weakened if the add-back leaves the rise intact.
- **CH2. The mouse ISR set shows no resolvable sign because the genes that carry the organoid effect (Chac1, Trib3, Sesn2) are at the measurable floor in bulk P17 tissue, not because the biology is absent.**
  Missing comparison: targeted, deeper measurement of those genes or sorted cells; a 2 v 2 progenitor-targeted contrast cannot exclude an organoid-sized fall.
- **CH3. Glycolysis-type genes are higher in organoid and shRNA progenitors for different reasons: less advanced tissue in the organoid, line state in the shRNA clone.**
  Missing comparison: culture-time calibration of the glycolysis set, stage-matched shRNA controls, and a flux readout. The held data already show the two maturity stories point in opposite directions for progenitor markers.
- **CH4. The apparent mouse Ldha fall in the progenitor-targeted contrast is a control-group difference, not a deletion effect.**
  Missing comparison: all three mouse arms against one control genotype. Supported by the N-control vs WT value of +0.92.
- **CH5. Glial excess in the null mouse and P47T is downstream of seizures, and the rat deficit reflects a pre-onset window; the organoid, with neither seizures nor microglia, shows no reactive transcript programme.**
  Missing comparison: glial density before the first spike (P5 to P8 in the mouse) in the same species and region, with EEG. Weakened if glial density is already above wild type before seizures.
- **CH6. The mitochondrial-translation sign differs between organoid and hNPC because the effects are small and move with library composition (the unrelated ribosome class moves with them), not because mitochondrial biogenesis is regulated in opposite directions.**
  Missing comparison: at least three libraries per arm on one platform with the ribosome control reported.
- **CH7. Lesion class modulates the cortical-layer response to wild-type add-back: the WOREE line responds in layer markers and the SCAR12 line is already near wild type.**
  This has been tested inside its source: WOREE organoids have lower CTIP2 and SATB2 than wild type and respond to add-back, SCAR12 organoids are wild-type-like, with lines from three and two individuals and week-16 firing about 3-fold higher in WOREE. What is missing is separation from variant type (complex heterozygous vs missense), individual and batch, and replication in an independent laboratory. It is the only hypothesis that bears on residual function directly with human cells.
- **CH8. A residual-function allele reproduces the glial and seizure phenotype but its ISR and metabolic transcript profile is unknown.**
  Missing comparison: the pre-declared sets of iteration 5 applied to the public P47T deposit (GSE215425). This is a proposal for a follow-up, not something done here.

## 6. Subgroup verdict

**No patient subgroup is supported, and no subgroup survives resampling in the held transcript data.** One class difference is reported by a source (WOREE vs SCAR12 organoids, row below); it is a candidate model-system contrast, confounded and unreplicated, not a subgroup. No clustering was performed, so there are no computational clusters to interpret, and none is offered as a biomarker. R4 requires that a grouping survive appropriate resampling or independent data; each candidate below fails on one of them.

| Candidate grouping | Why it fails |
|---|---|
| Lesion class (null or knockout vs knockdown vs missense) | for most quantities there is one context per class; the classes also differ in species, stage, tissue, assay and laboratory at once, so a class effect is not separable; hNPC and neurons are one line; P47T has no ISR or metabolic quantity at all |
| Cell-type targeting of the deletion (neuron vs progenitor vs germline) in mouse | the only design that varies a single factor (same deposit, stage, assay). It shows ISR with no resolvable sign in all three, myelin lower in all three, and differences elsewhere (progenitor, neuronal, UPR, glycolysis) only in the germline contrast against WT controls. For UPR and OXPHOS the control-vs-control differences (UPR -0.65 and -0.55 against the null contrast's -0.30) are as large as the effect; for progenitor and neuronal markers they are not (progenitor +0.29 against control contrasts -0.13 and -0.02; neuronal +0.25 against -0.38 and -0.42, opposite in sign), so those two germline-only differences are not explained by the control difference, but they are single-contrast, 2 v 3 animals, outside the null in one contrast only, and composition-confounded (myelin transcripts fall). Resampling (below) does not keep an ISR sign. Nothing differs by targeting that survives |
| Developmental stage (progenitor vs neuron stage of the shRNA line) | one library per arm; the ISR rise is present at both stages and mito translation differs, but no resampling exists |
| Region (hippocampus vs cortex, neuron-targeted) | cortex has a weaker and noisier deletion (68 vs 85 percent), so region and depth are confounded; OXPHOS and mito translation change sign, with deletion depth as an equally good explanation |
| Model-system class: WOREE vs SCAR12 organoids | the source (PMID 42397075) reports a difference in radial-glia proportion, layer markers (lower in WOREE, wild-type-like in SCAR12) and week-16 firing (about 3-fold higher in WOREE) from lines of three and two individuals, while week-7 hyperactivity is similar. It is confounded with variant type, individual and batch, comes from one laboratory and is untested for replication, so it stays a contextual hypothesis (CH7). It is a model-system observation and gives no label to any patient |
| Any partition of patients or any response label | no patient-level data are held, no treatment response exists in these systems, and the model contexts are not patients. None is offered |

Resampling that is possible with the held data. Two leave-one-animal-out statistics exist and they give different patterns, so both are shown.

(a) `--animal-loo`: per-animal ISR score, KO mean minus control mean, dropping one animal at a time (this folder's statistic):

| contrast | n_ko | n_ctl | diff_all | loo_min | loo_max | sign_stable_under_leave_one_animal_out |
|---|---|---|---|---|---|---|
| H_S | 3 | 2 | +0.091 | -0.062 | +0.230 | no |
| H_N | 2 | 2 | -0.126 | -0.262 | +0.011 | no |
| H_null | 2 | 3 | +0.012 | -0.050 | +0.074 | no |
| C_S | 3 | 4 | +0.093 | +0.035 | +0.156 | yes |

(b) `--source-loo`: the mouse cycle's own table (`results/set_summary.tsv`), the centred set mean recomputed after dropping each animal; one sign per dropped animal:

| contrast | leave_one_out_signs | all_same_sign |
|---|---|---|
| H_S | ++-++ | False |
| H_N | ---- | True |
| H_null | +---- | False |
| C_S | ++++-++ | False |

Under (a) the sign is stable only in the noisy cortex contrast (C_S). Under (b) it is stable only in the progenitor-targeted contrast (H_N, 4 animals, all negative) and unstable in H_S, H_null and C_S. The two statistics therefore disagree for H_N and C_S, and the H_null difference under (a) is +0.012 while its pooled centred value is -0.019, so the sign there is not assignable by either. In both, three of four contrasts are unstable. This does not show absence of an effect; it shows that no ISR sign can be assigned in the held mouse data, so no ISR-based grouping can survive.

Independent data that would be needed to revisit this: a second replicate of each human perturbation, protein-verified depth, and the same pre-declared sets in an independent mouse or human deposit.

## 7. UNVERIFIED and open items

- Everything marked `source_paper_carried`: values were carried from the cycle texts (P7, P10, fly follow-up, comparison file). In the revision after the verifier report the following were re-read in the held full texts: the patient-organoid paper (PMID 42397075: lines from two SCAR12 and three WOREE individuals; WOREE CTIP2/SATB2 lower, SCAR12 wild-type-like; radial glia higher in WOREE, similar to wild type in SCAR12; week-16 firing about 3-fold higher in WOREE; calcium imaging), the organoid paper's slice recordings (PMID 34268881: 14 slices from 5 WT and 8 KO organoids), and the hNPC paper (PMID 31543760: scrambled-shRNA control, Western-confirmed silencing). The verifier's reading of the other papers (P47T counts, fly units, rat, resazurin) was accepted, not repeated.
- Not available for re-check: the fly Atf4-unchanged statistic and relative magnitudes, the fly lactate in the knockdown-alone cell and the metabolomic pool counts (supplement or unreleased deposit), and the null-mouse P20 percent-area values (supplement of another paper).
- Cre drivers of S and N, the control genotypes, sex and batch, the allele, and the link between GSE158681/2 and any paper (the deposit states none). The N control is called N-WT in the design text and N-Control in the samples.
- Whether the organoid GFAP-flat transcript result and the paper's imaging astrocytosis would agree on the same organoids (assay and marker specificity are the stated candidate; not tested).
- The hNPC pan-neuronal marker set: mean -0.687 against a null 2.5th percentile of -0.653 (rank 0.041) is technically outside, while the P6 text and the comparison file call it inside; matrix cell Q11/HNPC_KD follows the table and carries the discrepancy in its caveat. Similarly Q05/NEUR_KD exceeds its null upper bound by about 0.006 only, and Q08/HNPC_KD (centred -0.004, labelled `at_null_edge`) by about 0.011.
- P47T histology is pseudoreplicated (subfields from 3 mice per group), so its P values are not animal-level.
- Whether oligodendrocyte-lineage cells exist in the week-15 organoid; the organoid and CAGE myelin cells are UNKNOWN for that reason as well as because no set was computed.
- P47T Oas1f (+6 to +7 log2 in forebrain) is unexplained and a strain or passenger effect was not tested; it is not used here.
- The rat's sound-evoked seizures after PND 16 are second-hand.
- The mouse symbol-based orthology of the HK, SLC2, SLC16, LDH and PDK families.
- Nothing in this folder establishes an ISR, metabolic or glial sign for any patient or for WWOX function.

## 8. Next measurements that would change this view (proposals, not done)

1. Matched ATF4 protein, eIF2alpha-P and target mRNA in one WWOX-deficient human neural system with a transduction-matched control and an add-back arm (separates D1 mode, composition and the translational explanation at once).
2. The ISR and glycolysis sets against culture time in the WWOX-free spheroid series (public, already used for the Wnt calibration) to price the maturity explanation in D1 and D2.
3. The iteration-5 sets, pre-declared, on the public P47T deposit (the only residual-function allele with data in hand).
4. A glial time course spanning the first spike in one species, region and assay (D5).
5. A shared control genotype across the S, N and null mouse arms (D2, D3 and the control-group artefact generally).

## 9. Files and reproduction

| File | What it is |
|---|---|
| `README.md` | this reading |
| `context_matrix.tsv` | 182 rows (14 quantities by 13 contexts), 19 columns, one header, no trailing notes |
| `check_context_matrix.py` | `python3 -I check_context_matrix.py` (exit 0 when structure, vocabulary, every keyed number against its local source table, sign rules and the README table all agree); `--wide`; `--animal-loo`; `--source-loo`; `--help` does no work |

The checker reads only local files from the cycle folders named in `source_ref` and never touches the network. It cannot check `source_paper_carried` cells against the papers; that is the verifier's task.
No needs, cards, current files, ledger or registry were edited. Suggested landing for the integrator: one sentence in `roadmap_current.md` R4 pointing here, and the subgroup verdict ("none supported") recorded wherever R4 status is tracked.
