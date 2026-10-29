# WWOX public-data census for questions transcripts cannot answer (IT6 P3)

Scientist-b, task IT6-P3, 2026-10-29. Exploratory census, not a review. Not medical advice. Association is not modulation is not rescue.
Reused, not redone: GSE126075 (hNPC CAGE), GSE156243 (organoid RNA-seq), the LINCS matrix, `wwox_systems_comparison_it5_20261029.md`.
No registration, no contact with anyone, no personal string sent to any service, no captcha/403/access-control bypass, no spend.

## 0. Bottom line

1. **No public record was found that measures, in a WWOX-deficient system, any of: protein or phospho-protein abundance (proteome or
   phosphoproteome), translation (ribosome profiling, puromycin incorporation), eIF2alpha phosphorylation or PERK/GCN2 activation,
   or enzymatic/flux readouts (OCR, ECAR, PDH activity, NAD(H)).** The one candidate that could reach pyruvate/TCA pools
   (fly head metabolomics, MTBLS12344) is still not public (re-checked today). Every searched route and count is in section 4.
2. The only WWOX-perturbation records with a *rescue/add-back arm* are whole-animal mouse gene-therapy studies; their molecular
   readouts are Western blots of WWOX itself, survival, weight, glucose and electrophysiology, with no data deposit.
3. An interactome (HEK293T tandem affinity purification; COG proximity labelling) shows who sits next to WWOX in a
   non-neural cell line. It does not show pathway activation, and an overexpressed bait is not a perturbation of WWOX function.
   A normal-tissue atlas (Human Protein Atlas, GTEx, OpenCell tagging) is not a WWOX perturbation.
4. Best *available public* material for P4 (section 6): **GSE158681 (+ GSE158682)**, mouse neuron-targeted and null Wwox deletion,
   hippocampus/cortex, P17, with the deletion visible in the deposit. It is a transcript record. It can narrow the open ISR-sign
   conflict (organoid lower vs hNPC higher) in a third, better-verified neural system; it cannot answer the protein/phospho/flux
   questions, which remain a bench gap.

## 1. Candidate table

Legend: sys = system; pert = perturbation; meas = direct (D) or proxy (P) for the question category; ctrl = controls present;
unit = experimental unit; avail = availability checked at the source on 2026-10-29. Categories: (a) proteomics, (b) translation/ISR,
(c) enzymatic/metabolic function, (d) add-back/rescue, (e) neuronal/glial phenotype, (f) variant residual function.

| # | Record | Cat | Sys | Perturbation | Meas | Controls | Unit (n) | Avail | Size |
|---|---|---|---|---|---|---|---|---|---|
| 1 | MTBLS12344 (MetaboLights), Brain Commun 2026 (DOI 10.1093/braincomms/fcag385) | c | fly head, pan-neuronal | Wwox RNAi x Abeta42 (2x2) | D for pools of pyruvate/TCA/lactate if tested (untested in public text) | RNAi control line, LacZ | pool of 10 heads (N=5) | **NOT public** (folder 404; absent from public listing; API 401) | n/a |
| 2 | E-MTAB-14948 and E-MTAB-14949 (ArrayExpress), same paper | b,c,d | fly head, pan-neuronal | RNAi knockdown (14948); CRISPRa overexpression (14949); each with and without Abeta42 | P (mRNA) | RNAi control; control gRNA | pool of 10 heads; 4 per cell (16 samples; 15 in 14949, one missing) | public: per-sample featureCounts + SDRF | about 4.5 MB x 31 = about 135 MB |
| 3 | GSE158681 (hippocampus), GSE158682 (cortex), GSE158684 (hippocampal nuclei, snRNA), parent GSE158685 | e,d | mouse brain, P17 | null; neuron-targeted deletion ("S"); neural stem/progenitor deletion ("N") | P (mRNA) | Cre-negative littermate controls | mouse; hippocampus null 2 v WT 3, S 3 v 2, N 2 v 2; cortex S 3 v 4 | public: TPM tables (transcript-level, Salmon); raw in SRA | 4.6 MB + 2.5 MB |
| 4 | GSE215425, P47T knock-in (paper PMID 36828035) | f,e | mouse brain regions | partial-loss missense knock-in, WW1 domain | P (mRNA) | WT littermates | mouse; 5 v 5 per region; 37 samples | public; raw in SRA | not measured (37 samples) |
| 5 | E-MTAB-14792 (scRNA, Brain 2026 organoids, DOI 10.1093/brain/awag239) | e | human organoid | WWOX loss | P (mRNA) | control organoids | cells | **403 not accessible**; release request drafted, not sent | n/a |
| 6 | GSE229210 (CAGE; paper PMID 37781246) | c,d | four human glioma lines | WWOX overexpression into low-WWOX lines | P (mRNA) | empty-vector virus | 3 cultures x 4 lines x 2 arms (24) | public | not measured |
| 7 | PMID 30619736 (Front Oncol 2018), tandem affinity purification-MS | a | HEK293T | SFB-tagged WWOX overexpressed (bait) | interactome only | IgG for Western follow-up; no stated empty-tag proteomic control found | 2 replicates, 1,006 unique proteins | supplement-only (Supplementary File 1); no PRIDE deposit stated in text | not measured |
| 8 | PXD071676 (PRIDE), bioRxiv 2026 (DOI 10.64898/2026.06.16.732723; PMID 42523332) | a | RPE1, HEK293T, HeLa | COG-TurboID proximity labelling; WWOX is a *prey*; separate WWOX siRNA knockdown with lectin/IF readouts | interactome + imaging | parental cells | 4 to 5 repeats | **PRIDE API 404 today (not yet public)** | n/a |
| 9 | PXD024909 (OpenCell, PRIDE) | a | HEK293T | endogenous tagging atlas | interactome atlas | n/a | n/a | public | not measured; whether a WWOX line exists UNVERIFIED |
| 10 | Mol Ther Adv 2026 (PMID 42422765; DOI 10.1016/j.omta.2026.201791) | d,e | mouse (severe null), AAV9 | add-back: neuron promoter, oligodendrocyte promoter, ubiquitous promoters; dose, timing | D for survival, weight, glucose, WWOX protein (Western), electrophysiology, myelination; no ISR/metabolic flux | reference-item-injected KO and WT | mouse; n 3 to 6 per arm | "Data availability: Not relevant"; figures and Document S1 only | n/a |
| 11 | EMBO Mol Med 2021 (PMID 34747138) | d,e | mouse, neonatal AAV9-neuron | add-back; neuron-specific deletion | D for survival, seizures, myelination, electrophysiology | injected controls | mouse; n 4 per group (weight) | "no data deposited in external repositories" (but see GSE158681 in row 3) | n/a |
| 12 | Acta Neuropathol Commun 2020 (PMID 32000863) | c,e | mouse cortex, hippocampus, cerebellum, P14 | null | D for pGSK3beta by Western (blot images) | WT, heterozygote | mouse n=3 | figures only; no deposit | n/a |
| 13 | Mol Metab 2019 (PMID 30755385) | c | mouse skeletal muscle (non-neural) | muscle-specific deletion | D for serum lactate (MS) and glucose handling | floxed controls | mouse; n 4 to 6 | figures and supplement | n/a |
| 14 | Cell Mol Life Sci 2022 (PMID 35984507), Zfra1-31 | c | neuronal cell lines, high glucose | WWOX inhibition by a peptide, not a WWOX variant | claimed mitochondrial readouts; not read (not open access) | not read | not read | closed; content beyond title/abstract UNVERIFIED | n/a |
| 15 | GSE22689 (fly; PMID 21075834) | c | whole fly | Wwox loss; oxidative-stress and aerobic-metabolism phenotypes | P | not read | 9 arrays | public | not measured |
| 16 | BioPlex / DepMap / CCLE proteomics | a | cancer and HEK293 lines | none specific to WWOX loss in neural cells | atlas-type | n/a | n/a | not searched in depth; not a WWOX perturbation in a neural system | n/a |

Reused and not repeated: GSE126075, GSE156243 (and PMID 34268881 that deposits it), see `wwox_systems_comparison_it5_20261029.md`.

## 2. Per-candidate limits

**1. MTBLS12344.** The only record that could hold pyruvate, citrate, succinate or NAD-related pools in a neural-targeted WWOX
loss model. Re-checked today with the same two requests as the 2026-10-26 note (`lucas_clarke_followup_20261026/mtbls12344.md`):
the public folder returns 404 and the study is still absent from the public study listing; the web-service call needs
permissions. Reopening condition unchanged (appears in the listing). Even if released: metabolite pools in whole fly heads are not PDH
activity or flux; the paper's metabolite statistics are on the top 200 features of 2,355 peaks.

**2. E-MTAB-14948 / 14949.** A real factorial design (RNAi control and knockdown, each with LacZ or Abeta42; same for CRISPRa) with 4
pooled-head replicates per cell. I downloaded all 31 featureCounts files (about 135 MB) into the scratchpad only, to test whether the
perturbation is visible in the deposit. It is not: Wwox counts per million assigned reads, mean of 4 libraries, are 15.7 (knockdown, LacZ)
vs 15.9 (control, LacZ); 17.2 vs 16.8 with Abeta42; CRISPRa 13.3 vs 11.1 (LacZ) and 14.2 vs 13.3 (Abeta42). Wwox is a low-count
gene here (about 20 to 120 reads per library, libraries of 1.5 to 6.0 M assigned reads; three libraries with fewer than 2.1 M: I3, J3, K2).
RNAi can act without lowering the steady-state transcript, and a whole head dilutes neuronal signal, so this is not evidence that knockdown
failed; it means the deposit offers no check of perturbation depth, and the paper's text has no knockdown-efficiency statement
(0 hits for "knockdown efficiency"/qPCR in the full text; the paper's knockdown evidence is phenotypic). The paper's Atf4 evidence is
immunofluorescence intensity in 6 fly brains in the knockdown-plus-Abeta42 comparison only (images, not deposited). Fly ortholog
mapping to the human ISR target set is not one-to-one. No protein measurement is in the deposit.

**3. GSE158681/2/4/5.** Mouse neural tissue, true cell-targeted deletion, three deletion genotypes. In the hippocampal TPM table the
summed Wwox TPM over its 9 annotated transcripts is 3.3 to 4.3 in controls and WT, 0.3 to 0.8 after the "S" deletion, 0.1 to 0.4 after
the "N" deletion and 0.3 to 0.4 in the null: the deletion is visible in the deposit (my own sum of the deposited table, descriptive). In
the cortex ("S" arm) controls range 8.0 to 26.5 and knockouts 3.8 to 9.0: depth is less clear and control-to-control spread is large.
Limits: transcript level; Salmon transcript TPM, no integer counts in the deposit (SRA holds raw reads); 2 to 3 animals per arm; whole-tissue
composition is altered by the phenotype (the series summary itself reports reduced oligodendrocyte maturation and myelination transcripts);
null mice at P17 are systemically ill (growth, glucose), so null-versus-WT contrasts carry systemic confounds that the cell-targeted
deletions reduce but do not remove. The identity of the "S" and "N" Cre drivers (synapsin, nestin) comes from LEGEND's earlier reading
of the deposit and the series text ("neurons", "neural stem and progenitors"); the driver names are UNVERIFIED at the source.
Series metadata carry no PubMed link; the EMBO Mol Med paper (row 11) says no external deposit, so the link between GSE158681 and a paper is
inferred from the summary text, UNVERIFIED. Already used by LEGEND for T-type transcripts only (not for ISR/PDK/glycolysis sets).

**4. GSE215425 (P47T).** The only in-vivo model of a missense variant with residual function (WW1 domain, impaired PPxY binding), but
mRNA only; no protein or activity readout in the deposit. It addresses category (f) only through a phenotype and a transcriptome of a
different residue in a different domain from the reference genotype class's lesions; transfer is not established.

**5. E-MTAB-14792.** The sole single-cell human neural record; not accessible. The release question is in
`ebi_access_request_E-MTAB-14792_draft.md` (not sent; the operator decides). Nothing here changes that.

**6. GSE229210.** Overexpression into glioma lines (tumour-derived, not a deficiency model; the lines are not neural-developmental);
useful only as a "direction under gain" transcript read. Not a rescue of a deficient neural system.

**7. Tandem affinity purification-MS.** Overexpressed bait in a non-neural line; two replicates; the text I read states the
bait was SFB-tagged WWOX and that an IgG was the negative control for Western follow-up. A matched empty-tag proteomic control is not stated
in the text (UNVERIFIED in the supplement). It lists neighbours; it does not show activation of any pathway.

**8. COG-TurboID (PXD071676).** WWOX appears as an enriched neighbour of the COG complex in RPE1 (and, "data not shown", HEK293T). The WWOX
knockdown experiment (siRNA, effect on Golgi area, lectin binding, COPB2 localisation) is imaging with n = 30 cells per readout; cells,
not independent cultures, are the stated unit. Non-neural, not deposited yet.

**9. OpenCell.** A tagging atlas in HEK293T; not a perturbation.

**10 and 11. Gene therapy.** Add-back evidence exists and is strong at the phenotype level (survival, growth, glucose, seizures,
myelination), but the readouts are not the ones this census asks for (no ISR, phospho, flux, or protein-level pathway readout), the rescue
tissue is not public, and one record says "Not relevant" for data. Rescue of a phenotype is not rescue of a pathway, and it does not
tell which arm of the pathway moved.

**12 and 13.** Western images (GSK3beta) and serum lactate in a non-neural tissue: low n, no deposit; indirect for the questions above.

**14 to 16.** Not usable for P4 (closed text; whole fly; atlas).

## 3. Category summary (what exists, what is missing)

| Category | Found | Missing |
|---|---|---|
| (a) proteomics / phosphoproteomics | interactomes only (rows 7, 8, 9); one DepMap-type atlas class not a perturbation | any proteome or phosphoproteome of a WWOX-deficient or WWOX-null system, neural or not |
| (b) translation / ISR measures | one fly brain Atf4 immunofluorescence (row 2 text, images) | ribosome profiling, puromycin incorporation, eIF2alpha-P, PERK/GCN2-P, ATF4 protein in any human or mouse WWOX-deficient neural system. Full-text search of open-access papers with WWOX in the title/abstract and eIF2/PERK/ATF4-protein terms in the body returned 0 |
| (c) enzymatic / metabolic function | fly lactate (not public yet), mouse muscle serum lactate, mouse blood glucose in gene-therapy papers | OCR/ECAR, lactate production, PDH activity or phosphorylation, NAD(H) in a WWOX-deficient neural system |
| (d) add-back / rescue | mouse AAV9 phenotype rescues (rows 10, 11); fly CRISPRa overexpression with Abeta42 (row 2); glioma overexpression (row 6) | any add-back with molecular (protein/flux) readouts; any human neural add-back |
| (e) neuronal / glial phenotypes | mouse neuron-targeted deletion transcripts (row 3), electrophysiology, myelination (papers) | cell-type-resolved protein data; the human organoid scRNA is locked (row 5) |
| (f) variant residual function | P47T mouse (row 4) | any functional assay (activity, stability, interaction) for the missense variants of the reference genotype class in a neural system; LEGEND's own stability census (`analysis/wwox_missense_stability_census_20260922.md`) is predictive, not experimental |

## 4. Searches actually run (2026-10-29)

Europe PMC REST (`/search`, `resultType=lite`), counts are total hits at run time:
- `WWOX AND (proteomic* OR phosphoproteom* OR "mass spectrometry")` any field: 502; same restricted to title/abstract: 66.
- `WWOX AND (PXD* OR PRIDE OR MassIVE OR ProteomeXchange)` title/abstract: 15; `"WWOX" AND (PXD0* OR MSV0*)` any field: 19. Screened by hand:
  none is a WWOX-perturbation proteome; hits are atlases, networks and method papers.
- `WWOX AND (ribosome profiling OR puromycin OR eIF2 OR ATF4 OR "integrated stress response")` any field: 148; the title/abstract set with ISR/UPR/translation terms: 88;
  with a neural term: 45. Body-text query for p-eIF2, p-PERK, ATF4 protein: **0**. Body-text query for puromycin/SUnSET/polysome/ribosome profiling: 20 (puromycin
  appears as a selection marker; none is translation measurement in a WWOX-deficient neural system on screening titles, not every full text read).
- `WWOX AND (seahorse OR "oxygen consumption" OR lactate OR "pyruvate dehydrogenase" OR NAD)` any field: 329; title/abstract with mitochondria/glycolysis terms: 188;
  body-text Seahorse/ECAR/OCR/lactate production/PDH activity/NAD+/NADH: 8, none neural WWOX-deficient flux.
- `WWOX AND (rescue OR add-back OR re-expression) AND (neuron* OR glia* OR ...)`: 324; WWOX with iPSC/patient-derived/knock-in/CRISPR terms: 195; variant/missense with functional terms: 960 (any field) and 113 with a neurological qualifier.
- Data-availability and accession extraction by script from the open-access full text of: PMC13343157, PMC13684411, PMC10613160, PMC12767083,
  PMC10835625, PMC8350905, PMC6300487, PMC6437662, PMC8609180, PMC7300205, PMC8649866, PMC6990504, PMC10487847, PMC13405132.
PubMed (MCP): proteomics query 18 hits; ISR/translation query 2 hits (one is Wwox fly paper, one a cholangiocarcinoma p38 study); metabolism-in-neural query 1 hit.
NCBI GEO DataSets (`db=gds`): `WWOX[All Fields] AND gse[Entry Type]`: 39 series (Wwox and WWOX give the same list); with knockout/knockdown/mutant/siRNA/shRNA: 16.
All 39 titles screened; WWOX-perturbation series in a neural system: GSE126075, GSE156243, GSE158681/2/4/5, GSE215425 (rows reused or 3 and 4);
others are cancer, SNP arrays or unrelated.
PRIDE REST (`/search/projects?keyword=`): WWOX 1 (PXD024909), Wwox 1, "WW domain-containing oxidoreductase" 0, FRA16D 0, WOREE 0, "WWOX knockout" 0, "WWOX knockdown" 0. EBI Search `pride` and
`metabolights` domains match "WWOX" fuzzily to "wood" (189 and 44 entries, all wood/plant); no WWOX entry. Treated as no hit.
MassIVE: the public dataset listing (20,484 datasets, about 31 MB JSON, metadata only) was filtered locally for WWOX, WOX1, Wwox, FRA16D and the full protein name in
title, description and keywords: 0 true hits (three apparent matches were base64 hash strings). Raw-file annotations are not searched.
MetaboLights: the public study folder and listing for MTBLS12344 re-checked (404; absent). ArrayExpress/BioStudies: `biostudies-arrayexpress` WWOX 27 entries (listing screened; two Wwox fly studies are the only neural ones).
Direct file reads: BioStudies file listing and SDRF for E-MTAB-14948/14949; GEO series pages and supplementary listings for GSE158681, GSE158682, GSE215425, GSE229210; PRIDE project endpoint for PXD071676 (404).

Not done / limits of the search: Google Scholar and closed-access supplements were not opened; bioRxiv API was not available (not authorised in this session); closed full texts (row 14) were not read;
Chinese-language and conference literature not searched; "data in supplement" statements were checked only where open-access full text exists.

## 5. Claims not verified at the source (UNVERIFIED)

- Whether the COG-TurboID deposit PXD071676 contains any WWOX-perturbation sample (it is not public today).
- Whether OpenCell contains a WWOX-tagged line (the OpenCell API redirected and was not followed to its end).
- Identity of the "S" and "N" Cre drivers of GSE158681 (series text says neurons and neural stem and progenitors).
- Whether a proteomic empty-tag control exists in the supplement of the tandem affinity purification study (supplement not opened).
- Content of PMID 35984507 beyond title and abstract; .
- Whether MTBLS12344 contains pyruvate (unreleased).

## 6. Selection for P4

**Verdict on the question P3 posed:** no public dataset is adequate for the protein, phospho, translation or flux questions. Concrete insufficiencies:
(i) no proteome/phosphoproteome exists for a WWOX-deficient system; (ii) no eIF2alpha-P, PERK/GCN2-P, ATF4 protein, puromycin or ribosome-profiling data exist in
any WWOX-deficient neural system; (iii) no OCR/ECAR/PDH/NAD data in a neural WWOX-deficient system; (iv) the metabolomic deposit that could help is not public; (v) the add-back studies have no molecular
readout and no deposit; (vi) interactomes cannot show activation. These stay a bench gap (the matched protein/phospho plus target-mRNA experiment already written in
`wwox_systems_comparison_it5_20261029.md` section 3.1(c)).

**Single most informative available public material: GSE158681 (hippocampus; 14 libraries), with GSE158682 (cortex; 7 libraries) as the second region.**
Why this and not the fly records: the deletion is visible in the deposit (section 2, row 3), the cell-targeted arms reduce the systemic confound of the null, three genotypes
give a built-in consistency check, and the data are mouse neural tissue. The fly records show no visible perturbation depth. This selection narrows the *transcript* ISR-sign conflict; it does not
touch the protein questions, and P4 must say so in its first line.

Pre-declaration inputs for P4 (to be committed before any analysis):

| Item | Content |
|---|---|
| Question | In neuron-targeted Wwox deletion (and in the null) at P17, are the pre-declared ISR target set, mitochondrial-translation set, glycolysis/lactate set and the PDK/PDH genes (Pdk1 to Pdk4, Pdha1) moved in the sign seen in the knockout organoid (ISR lower, mito translation lower, glycolysis higher) or in the shWWOX progenitor line (ISR higher, mito translation higher)? Or neither? |
| Contrast | Hippocampus: S deletion (n=3) vs S control (n=2); N deletion (n=2) vs N control (n=2); null (n=2) vs WT (n=3); cortex: S deletion (n=3) vs S control (n=4). Each contrast analysed on its own; none pooled with the others or with the organoid/hNPC data |
| Experimental unit | the animal (one library per animal); genes and transcripts are not units |
| Method | exactly the P7 same-set method (`hnpc_gse126075_it5_20261029/p7_organoid_same_sets.py`): per-arm normalised mean, log2 ratio, median centring, expression-decile-matched random sets, 10,000 draws; transcript TPM summed to gene by Ensembl gene id, mouse symbols mapped to the human sets by orthology table fixed beforehand; sets frozen from `p7_params.json` |
| Controls | the Cre-negative controls of each genotype; a negative-control set (cytosolic ribosome, as in P7); the Wwox loss itself as a positive check of perturbation depth (summed Wwox TPM per arm reported first; a contrast with less than 50 percent reduction is declared uninformative before looking at other genes) |
| Decision criterion | A set counts as "moved" only if its centred log2 ratio sits outside the 2.5th to 97.5th percentile of its own matched null AND the sign agrees in at least two of the three hippocampal contrasts; "concordant with organoid" or "concordant with hNPC" is declared only when this holds for the ISR set; otherwise the ISR sign stays unresolved. A set moving together with the ribosomal control is declared non-specific |
| Known limits | transcript-level only; ATF4 is translationally controlled so its mRNA is uninformative; 2 to 3 animals per arm (the minimum single-gene permutation p is limited by n); bulk tissue composition shifts (myelination, oligodendrocyte maturation) can mimic set changes; null at P17 is systemically ill; transcript TPM tables without integer counts; mouse versus human ortholog mapping; cortex "S" controls vary 8 to 26 TPM in Wwox; no protein, phospho, translation or flux inference may be drawn; the result does not validate any drug-signature reversal |
| Download size | 7.1 MB (4.6 MB hippocampus + 2.5 MB cortex TPM tables); already fetched into the scratchpad for this census; nothing needs more than 2 GB. Raw SRA reads (not needed) are not fetched |
| Second choice, only if P4 wants a factorial design | E-MTAB-14948/14949 (about 135 MB), pre-declare the interaction term Wwox knockdown x Abeta42 for the fly Atf4 ortholog (crc, FBgn0000370), Ldh (FBgn0001258), Pdk (FBgn0017558), and read the CRISPRa arm as a direction-of-effect check; but perturbation depth is not visible in the deposit, which weakens any negative |
| Reopening condition for the better dataset | MTBLS12344 appears in the public MetaboLights listing: then read pyruvate, citrate, succinate, fumarate, malate, alpha-ketoglutarate and NAD-related rows for the four cells (pool of 10 heads, N=5), as a pool, not a flux |

Nothing in this section is an efficacy claim, a pathway-activation claim or a rescue claim.
