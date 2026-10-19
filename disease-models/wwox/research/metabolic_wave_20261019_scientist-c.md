# Metabolic wave 2026-10-19 — scientist-c, group G3 (mitochondria, iron, ferroptosis)

Task METAB-G3-C-20261019 · branch task/METAB-G3-C-20261019 · lot: group G3 of
`metabolic_batch_selection_20261019.md`, tier order. English; nothing here is medical advice; public,
disease-level edition. Per paper: what it MEASURES (system, genotype, tissue, readout) and what that
changes or fails to change in the disease model. The negative is the product. No novelty is claimed;
no hypothesis is promoted to a claim.

Reading discipline: first pass `SOURCE_FIRST` unless stated; comparison phase opened only after the
locators were captured (`FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON`,
named per paper). Receipts are staged under `receipt_staging/scientist-c/`, not appended.

---

## 1. PMID 26355344 — Sze 2015, Cell Death Dis (HELD-partial, re-read with a stated question)

context_policy: QUESTION_DRIVEN. Held before reading: the selection file's statement that the prior
receipt covered introduction and discussion only and results, methods, figures and tables were owed;
the prior receipt (it already carried a genre finding). Stated question: does this deposit contain
any Results, Methods, table or figure DATA on mitochondria under WWOX loss that the earlier reading
missed?

**First pass (artefact: NCBI efetch JATS of PMC4650446, the publisher PDF, and Figure 1 as a 200 dpi
page render; all in the shared `files/` tree).** The deposit is JATS `article-type="news"`: two PDF
pages, no abstract, no Methods, no Results, no table, ten references and exactly one figure, a
two-panel schematic. Figure 1 was opened as an image: panel a draws nucleolus-mitochondrion shuttling
of TPC6A, panel b draws routes i-iii of an aggregation cascade; it carries no axis, scale bar, n or
micrograph. The text restates, with reference numbers, the senior laboratory's own results (the
primary is a different PMID in this repository). The Europe PMC supplementary bundle for the deposit
contains only the figure in two formats.

**Answer to the stated question: no.** The sections the earlier receipt called "owed" do not exist in
this article, so the earlier partial coverage was in fact the whole text. The row is not an
unfinished primary; it is a finished News and Commentary. Its depth is therefore closed at
`complete_fulltext_read` for the article as published, with `abstract`, `methods`, `results`,
`tables`, `limitations` and `supplementary` recorded `not_present`, and `prior_receipt` naming the
partial event with `inadequate_prior_coverage`.

**What it measures:** nothing. It is a self-commentary by the founding laboratory.

**Comparison phase (PRIOR KNOWLEDGE ADMITTED: the registry records for this PMID, one hop).** The
paper registry and the tracking log hold a triage-only placeholder (tier B, "secondary full-text
target", pathway P5). The discovery ledger lead DL-MECH-019 lists this deposit as one of three
sources next to its two primaries. That counts a commentary as an independent source for an SDR
binding map it can only restate. Effect on the model: none gained; one source count corrected (a
commentary is not a fourth observation of the TPC6A-delta / SDR binding). The mitochondria-in-WWOX-null
-neurons question remains answered only by the primary (a separate partial row, listed in the selection
file under HELD with supplement captions owed) and the Drosophila respiration paper that is already
read. Selection-file consequence for the Orchestrator: a PMC XML larger than 5 kB did not imply a
Results section; "OA XML" in the route column should be paired with the JATS `article-type`.

---

## 2. PMID 36364214 — Liu 2022, Molecules: "WWOX Modulates ROS-Dependent Senescence in Bladder Cancer" (tier 1, new)

context_policy: SOURCE_FIRST (selection row's one-line "why it matters" was the only thing held; the
registry was opened only after the locators were captured).

**What it MEASURES.** System: AY-27 rat bladder carcinoma cells in vitro, and an F344 rat orthotopic
AY-27 tumour, day 14. Manipulation: lentiviral WWOX OVERexpression (LV-WWOX, about 2-fold over empty
vector by Western blot, Fig 1b: roughly 5.0 control, 6.2 LV, 12.5 LV-WWOX in the paper's units).
Readouts: proliferation (MTS) and wound closure; WWOX and TNF-alpha by Western blot and
immunofluorescence; ROS as DHE-positive area; SA-beta-gal positive cells; p21 and p27 by Western
blot; tumour volume; p21 IHC. Every comparison is LV-WWOX against uninfected cells and empty vector.
There is no knockdown, knockout, null, neuronal or mitochondrial arm.

**First-pass observations (figures opened at native size).**
- ROS is one DHE stain (control about 13 percent, LV about 31, LV-WWOX about 90 percent positive
  area, Fig 3f). The text says "superoxide and hydrogen peroxide"; DHE reports superoxide-type
  oxidation and not hydrogen peroxide, and no scavenger or mitochondrial probe accompanies it.
- "ROS-dependent" senescence rests on exendin-4 (Fig 4c): one unquantified micrograph per
  condition; no ROS measurement under exendin-4 is reported. Exendin-4 is introduced by citation as a
  ROS-reducing agent; the paper does not show that it did that here. The causal word in the title is
  therefore carried by an illustration.
- Fig 2a shows the LV-WWOX culture as sparse rounded clusters, and the authors' own conclusion says
  "cytotoxicity and the induction of senescence"; overexpression toxicity is a live competitor to a
  senescence-specific reading, and p21/p27 rises (1.4 to 2.6-fold) are modest.
- The abstract claims increased SASP; the body contains the term only in the introduction and
  defines it there (measured in this session on the text rendering: two hits, abstract and
  introduction); no SASP assay is reported. TNF-alpha is the only secreted-factor-type readout.
- Fig 5b: bar heights read by eye are about 12.3 (control), 13.1 (LV), 3.7 mm3 (LV-WWOX). The
  quoted 30.49 and 28.60 percent equal LV-WWOX as a fraction of control and of LV, so the tumour
  volume fell by roughly 70 percent in this plot while the abstract and text say 30.49 percent
  reduction (INFERENZA from approximate bar heights; the values are not tabulated; no n per group is
  stated in the legend or text; recorded as a `panel_qualifies_text` locator).
- Fig 5d compares unlike compartments: control and LV p21 fields are tumour sheets, the LV-WWOX
  field is folded urothelium over connective tissue; no score. It does not show p21 in tumour cells.
- Methods contain an epirubicin-hydrogel cytotoxicity assay and a lentivirus release assay that the
  Results never report, and the Discussion cites GFP-/RFP-tagged proteins where Methods describe
  antibodies, so the Methods text is not fully the experiment that was run.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry records
for this PMID (two unprocessed stubs, one discovery-ledger mention), CLAIM 009 and CLAIM 034 (the sign
of the WWOX-ROS relation), and the dossier of the Drosophila Wwox/ROS paper.

**Comparison.** The repository holds the WWOX-ROS sign as a context-dependent question: CLAIM 009
(deficiency read as coherent with ROS increase, held `in observation`) carries a counter-directional
note from a diabetic mouse photoreceptor (knockdown lowers superoxide), and the Drosophila paper
reads dose and ROS as positively related (overexpression lines raise the CM-H2DCFDA-positive
fraction, loss-of-function mutants lower it). Liu 2022 is a third system with the same local sign
(WWOX up, ROS up), obtained by overexpression in a tumour line. It therefore adds one more
observation that the "deficiency means high ROS" shortcut is not a law, and nothing toward the
opposite law: it has no loss arm, so it cannot say whether loss lowers ROS in bladder cells. A
discovery-ledger line (the corpus note following DL-MECH-057) lists this PMID among already-read
records; no receipt existed, so the earlier "read" was a declaration, and this is its first receipted
reading.

**What it changes in the disease model: almost nothing, and the direction of the nothing matters.**
Transfer to the reference genotype is poor on four independent axes: direction (gain, not loss),
tissue and species (rat urothelial carcinoma, not neurons), no mitochondrial quantity measured, and
the ROS-dependence claim is illustrated rather than shown. What survives: a third system for the
local sign (PAPER-level support for the context principle in CLAIM 034, MINOR), and a methodological
caution for any ROS-lowering rationale (NAC, CoQ10, creatine) built on CLAIM 009: the sign of the
WWOX-ROS relation has now been seen positive in a fly, a mouse photoreceptor and a rat tumour line,
and in none of them in a WWOX-null neuron. RL-003 (metabolic line) is not changed.

---

## 3. PMID 35571988 — Li 2022, Neuro-Oncol Adv: mitochondrial 1555 G>A and childhood glioblastoma, with a WWOX intronic hit (tier 1, new)

context_policy: SOURCE_FIRST (only the selection row's one-line why-it-matters was held; the registry returned
nothing for this PMID, searched across seven surfaces, and that empty result is a statement about the
query and not about the laboratory).

**What it MEASURES.** Germline association in a California registry case-control study: 675 mtDNA SNPs
and about 19 000 nuclear SNPs inside 1318 genes of the GO mitochondrion category, genotyped from
archived dried blood spots on a SNP array; 90 glioblastoma cases (44 European, 43 Hispanic by the
Methods counts) against 2789 controls, European and Hispanic strata analysed separately and
meta-analysed. No expression, no function, no tumour tissue, no WWOX measurement of any kind.

**First-pass observations (Fig 1-2, Tables 1-4, Supplementary Tables S1-S7 opened).**
- The WWOX SNP (an intronic variant, rs62036057) reaches OR 2.99 with P 3.42e-6 in Europeans, just
  under that stratum's Bonferroni threshold (6.28e-6). Supplementary Table S7: Hispanic OR 1.30
  (0.73-2.29, P 0.37) and meta-analysis OR 2.14 (1.50-3.07, P 3.07e-5), which is above the
  meta-analysis threshold (5.63e-6). So the WWOX hit exists in one stratum of about 44 cases, does not
  replicate in the second stratum, and does not survive the combined analysis. The authors name the
  missing replication set and the wide intervals as their major drawback.
- The Fig 2 legend gives the European Q-Q genomic inflation factor as 1.30. A correction of the
  quoted P by that factor is my arithmetic (the paper does not do it): 3.42e-6 corresponds to
  chi-square 21.6, which divided by 1.30 gives 16.6 and P of about 4.6e-5, above 6.28e-6
  (INFERENZA, stated so; the factor is genome-wide for the scan, not for one locus).
- Neither the text nor Table S7 names the effect allele of the WWOX SNP, its frequency or its
  expression effect; there is no regional plot.
- WWOX enters through Gene Ontology membership, not as a hypothesis; the paper's mitochondrial
  sentence about WWOX cites one 2003 tumour-expression paper whose abstract (checked at abstract
  level only) reports mitochondrial association in one fibroblast line before confluence and says
  nothing about brain.
- Mitochondrial headline: m1555 A>G carried by only 3 glioblastoma cases; in Europeans alone the
  point lies below the Bonferroni line (Fig 1A, about 3.5 against about 3.7) and only the
  meta-analysis panel crosses it. The abstract pairs the adjusted OR with the exact-test P (9.5e-4),
  which would not clear the 1.8e-4 threshold; the meta-analysis P of 1.0e-4 does (reader's
  observation, relevant to m1555 not to WWOX).
- Abstract and supplement disagree for the EFHD1 hit: the abstract's 3.57 is the meta-analysis OR,
  the Hispanic OR is 6.19.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query result
(empty) and the working model's silence on cancer-risk genetics of the locus.

**What it changes in the disease model: nothing, and it should not be cited as WWOX-mitochondria
evidence.** The paper supports "a common intronic WWOX variant shows a nominal case-control signal
for childhood glioblastoma in one ancestry stratum"; it does not support "WWOX variation impairs
mitochondrial function in the brain". Heterozygous or hypomorphic loss and tumour risk is a
different question from biallelic-LoF DEE; no allele effect on expression is shown. Revival trigger
for the signal: an independent paediatric glioma set that replicates the SNP in the same stratum, or
an eQTL showing a direction at the locus; absent both, it stays a corpus record.

---

## 4. PMID 40808923 — Xu 2025, Front Neurol: "Ferroptosis and epilepsy: bidirectional pathogenic links and therapeutic implications" (tier 1, new; narrative review)

context_policy: SOURCE_FIRST. WWOX is named zero times in the article (case-insensitive count 0, taken in
this session over the text rendering), so this is a transfer read: what does the epilepsy-ferroptosis
literature, as this review states it, give a seizure phenotype in WWOX loss, and what is its
evidence base worth?

**What it MEASURES.** Nothing; it is a secondhand synthesis with no search method, no inclusion rule
and no appraisal. Observations it carries: injected-iron models (FeCl3, haemoglobin, post-traumatic
epilepsy), chemoconvulsant models (pentylenetetrazole kindling, pilocarpine, kainic acid) with
ferrostatin-1, deferoxamine or Klotho; one 130-versus-128 transferrin-saturation case-control from
2001; susceptibility-weighted imaging reports of iron in mesial temporal lobe epilepsy.

**First-pass observations (five figures opened, Table 1, all 93 references enumerated).**
- Evidence base is acquired-epilepsy models, not genetic epilepsy. The one genetic-epilepsy item is
  ref 17: patient-derived cells from five childhood epilepsy syndromes, mitochondrial-disease-related,
  responding to EPI-743 in a dose-dependent manner (this is the single nearest comparator to a DEE
  and it is cited secondhand; the primary is not read here).
- The authors themselves warn against a simply causal reading, state no trial of ferroptosis
  inhibitors exists, and say imaging and fluid markers are not specific to ferroptosis.
- The review's internal consistency is poor in the places a reader would use it: Table 1 gives
  valproate as raising non-transferrin-bound iron and oxidative stress while section 4.1 says it
  lowered lipid peroxides; Table 1 numbers do not line up with the list (valproate cites a topiramate
  migraine paper; the DHEA row cites the 2001 iron-overload paper); Figure 1 writes the Fenton
  reaction with two hydroxides. The proposed hippocampal iron threshold (1.2 mg/g) has no source and
  is declared unvalidated by the authors.
- The only contact with a WWOX-relevant axis: seizures activating HIF-1a/HO-1 and raising Fe2+ in
  hippocampal neurons (ref 60, a 2023 primary), and one sentence tying iron to myelination and
  catecholamine metabolism.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty), the
selection file's statement that the working model is silent on iron and ferroptosis (term counts 0),
and the registry-held WWOX-HIF1A glycolytic-shift reading.

**Comparison and what it changes.** No claim or record changes. What the paper contributes is a
checklist of readouts that no WWOX record holds: labile iron or ferritin, GPX4 and GSH, lipid
peroxidation (4-HNE, malondialdehyde, ACSL4), susceptibility-weighted iron imaging, and ferrostatin-1
or a chelator as a perturbation, all validated in acquired-seizure models and none in a Wwox-null or
biallelic-LoF background. The one stageable lead (IPOTESI, not a claim, staged for the Orchestrator
because the discovery ledger is a single shared file): the registry-held reading that WWOX loss raises
HIF1A (fibroblast and hepatic systems) meets ref 60's seizure-driven HIF-1a/HO-1 iron accumulation;
a Wwox-null brain might therefore show HO-1, ferritin or labile iron changes independently of the
paper's mechanism. Falsifier: no difference in HO-1, ferritin or lipid-peroxidation readouts between
Wwox-null and control cortex or hippocampus at a pre-lethal age. Counter-evidence: the HIF1A reading is
non-neural, the null mouse is short-lived, and ref 60 is a seizure-induced response, so it cannot
separate cause from consequence of seizures. Transfer to the reference genotype: indirect, readout-level
only; a review, no system match.

---

## 5. PMID 38570643 — Kawabata 2024, Sci Rep: chronic replication stress, parkin and mitochondrial dysfunction (tier 1, new; structural analogue)

context_policy: SOURCE_FIRST (the selection row's one-line why-it-matters was the only thing held; the
registry returned nothing for this PMID across seven surfaces, an empty result that is a statement
about the query, not about the laboratory).

**What it MEASURES.** hTERT-immortalised neonatal human dermal fibroblasts and HEK293A cells given
aphidicolin (300 or 600 nM, 96 h) and then 96 h of recovery: parkin protein by Western blot, parkin
and other fragile-site mRNAs by RNA-seq in the fibroblasts, parkin stability by cycloheximide chase
in HEK293A, mitochondrial ROS by live MitoSOX/MitoTracker overlap, mitophagy by NDUFA9 loss and LC3
colocalisation, 8-oxoguanine, DRP1 phosphorylation and mitochondrial morphology; the rescue is an
ectopic HA-parkin line. The paper names WWOX nowhere in its text.

**First-pass observations (four figures, the nine-page supplement and Table S1 opened).**
- Parkin protein falls only after the recovery period (about 40 percent in fibroblasts, nearly
  absent in HEK293A), with no immediate change; mRNA is "not different" and the degradation rate is
  unchanged.
- That mRNA statement rests on almost no reads: in Supplementary Table S1 PRKN has a baseMean of
  about 6.5 normalised reads (about 4 untreated, 2 to 16 treated), so the reported variability is
  count noise and the transcript is near the floor of detection in these cells.
- The mtROS effect is small: APH about 0.65 against vehicle about 0.6 on a Mander overlap index, with
  rotenone near 0.82 (Fig 2E); significant at some time points only. "Fully restored by ectopic
  parkin" is a non-significant difference with wide error bars in a separate cell population, with no
  treatment-by-construct test.
- The headline attribution to "intrinsic fragility at PARK2" has no fragility assay behind it (no
  breakage, FISH, sequencing, allele-specific expression); the mRNA-quality explanation is labelled
  supposition by the authors. An ectopic cDNA is protected from replication stress for reasons that
  need not involve locus fragility, so the rescue distinguishes "parkin matters" from "replication
  stress matters" and does not separate fragility from any other cause of reduced endogenous
  expression.
- Authors' own limit: post-mitotic neurons are not exposed to replication stress; any effect would
  act in proliferating progenitors during development.
- **The WWOX data point the text never mentions.** Figure 1C plots fourteen fragile-site genes and
  WWOX is one of them: its bar sits below zero with three asterisks. Supplementary Table S1 gives
  WWOX baseMean about 87, log2 fold change about -0.78 (about 42 percent lower mRNA), p 0.0024, padj
  0.011, replicate counts about 88, 115, 127 untreated and 50, 63, 81 treated. Four of the fourteen
  fragile-site genes fell and one rose, the same proportions the text reports, so this is not WWOX
  specific. WWOX protein, FRA16D integrity and mitochondrial readouts were not measured.
  (Locators are a table row from the supplement and a panel reading; a text search of the article
  returns zero WWOX, which is why this was missed by a name search and found by opening the figure.)

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty), the
selection file's framing (closest structural analogue to WWOX as fragile-site gene with mitochondria)
and the repository's fragile-site material by theme.

**What it changes in the disease model.** No claim changes. It supplies (a) the first dataset in the
batch where chronic low-dose replication stress lowers WWOX transcript by roughly 40 percent in
non-cancer human cells (one cell type, one schedule, mRNA only); it is a hypothesis-grade route to a
hypomorphic dose of WWOX that does not need a coding variant, bounded by the authors' own point that
it acts in dividing cells and not neurons; and (b) a methodological template and its flaws for the
question "does fragility, rather than loss, matter" (a separate tier 3 row): the template cannot
answer it without a locus-specific assay, which neither this paper nor the repository has. Transfer
to the reference genotype: none for the biallelic disease; developmental-window relevance only for a
hypomorph-dose question. No mitochondrial result transfers: parkin is a different pathway and the
ROS effect is small and unevenly significant. A pre-registered test the repository could state: in
the same schedule, WWOX protein and mtROS in a donor-derived fibroblast line; a null for protein
would close the lead.

---

## 6. PMID 42434280 — Ganapathy 2026, J Gastrointest Oncol: is STAT3 blockade at the epicentre of toosendanin-induced ferritinophagy and ferroptosis? (tier 2, new; commentary)

context_policy: SOURCE_FIRST. The selection row says WWOX is not in the abstract and asks to check the body.

**What it MEASURES.** Nothing. It is a commissioned commentary on a single in vitro gastrointestinal
stromal tumour paper (one cell line) that proposes STAT3 as an upstream explanation; it carries one
hypothesis scheme (Fig 1) with no WWOX box. The peer-review file shows the reviewer asking the
authors to soften the STAT3-centred causal language, and the authors agreeing.

**The WWOX content, in one sentence (body, paragraph 4).** Citing a 2025 hepatocellular carcinoma paper
(ref 14), toosendanin "activation of WWOX" raises p53 activity, suppresses NRF2 activity, lowers GPX4
and SLC7A11 and, as written here, "increased expression of the iron exporter SLC40A1". The source's
own PubMed abstract (abstract-level check only, 2026-10-19; full text is paywalled, no PMC deposit, no
open-access copy) says toosendanin DEcreased SLC40A1 and that the ferroptosis effect depended on WWOX.
The commentary therefore reverses the sign of the iron exporter relative to its source (an
exporter going down is the direction that raises intracellular iron and fits the ferroptosis
reading). One more citation slip in the same paragraph block: the STAT3 SH2 binding statement carries
(17), which in the reference list is a hepatocyte Nrf2 O-GlcNAcylation paper, not the osteosarcoma
STAT3 paper listed as 18.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty) and the
selection file's BLOCKED rows for the WWOX-ferroptosis primaries (Yang 2025 paywalled; Wang 2026 lung
injury paywalled).

**What it changes in the disease model.** Nothing, and what it adds is a sign problem. In the one
WWOX-ferroptosis system that is visible here, WWOX activity is pro-ferroptotic and its loss would be
expected to blunt toosendanin-induced ferroptosis (abstract-level only); the batch selection lists a
second report, paywalled and unread, in which WWOX protects against ferroptosis in acute lung injury.
Both are pharmacological or injury states in cancer or lung models, neither is a genetic-LoF baseline,
and neither says that a Wwox-null neuron is ferroptosis-prone or ferroptosis-resistant. So the iron
and ferroptosis arm of the working model stays empty and the sign of WWOX on ferroptosis is, on the
present sources, context-dependent in the same way the WWOX-ROS sign is. Manual PDF request logged for
ref 14 (carried by the candidate).

---

## 7. PMID 41822170 — Petrillo 2026, Front Cell Neurosci: ferroptosis-induced epileptiform activity in mouse cortical slices (tier 2, new)

context_policy: SOURCE_FIRST (selection row's line only; registry empty; WWOX is not named anywhere in the
artefact).

**What it MEASURES.** Acute coronal cortical slices from wild-type C57BL/6J mice at P30 to P40 treated
with RSL-3 (5 uM, 15 min or 1 h) or 4-HNE (10 uM): GPX4, 15-LOX, GCL and SLC7A11 by Western blot,
GSH enzymatically, cysteine by HPLC, one example whole-cell trace after 4-HNE; and SLC7A11 mRNA in
leukocytes of four children with epilepsy against five controls. Every ferroptosis claim in the
slices is inferred from marker proteins at 15 to 60 minutes; no cell death, lipid ROS or iron
measure and no ferrostatin or chelator control is reported.

**First-pass observations (seven figures and the two-page data sheet opened).**
- GPX4 falls 36 and 47 percent and 15-LOX rises 4.5- and 5.3-fold within 15 and 60 minutes (n =
  three experiments, t-tests against control at two time points).
- Cysteine falls but the paper says the values are not significantly different, under a heading
  stating that RSL-3 decreases cysteine; the antiporter protein rises 2.4- to 3.4-fold (read as
  compensation).
- Wording slip: the text says GSH was "decreased to 64 and 52%"; Figure 2A shows about 65 and 85 nmol/mg
  against about 175 in controls, i.e. falls of about 63 and 51 percent (about 37 and 49 percent remaining).
- The only electrophysiology is one control and one 4-HNE trace from one cell; the legend says current
  clamp while the calibration is in pA; no vehicle trace, no cell count, no burst quantification.
- In the 4-HNE blots (Fig 6) the 15-LOX and SLC7A11 bands are faint and close in intensity across
  lanes yet quantified 1.5- to 2.2-fold.
- The data sheet's full blots carry four lanes where the figures show three conditions (lane order
  not labelled), and the beta-actin images for Fig 1A, 2B and 4 show the same band pattern, expected
  if one membrane was reprobed but not stated; no inference beyond that is drawn.
- Clinical arm: four children against five controls, mRNA only, no diagnosis, medication or seizure
  data; presented as a candidate peripheral biomarker mirroring brain changes.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty) and the
ferroptosis review read earlier in this lot.

**What it changes in the disease model: nothing; it is a methods-transfer note.** The assay family
(acute slice, RSL-3 or 4-HNE exposure, GPX4/15-LOX/GSH/xCT readouts, burst scoring) is the kind the
Xu review lacks for genetic models. For a Wwox-null background the slice route has a hard age
constraint: the paper's slices are P30 to P40, while the null mouse is recorded in this repository as
dying within weeks, so a null comparison would need younger slices or a heterozygous or conditional
line. A Wwox-null slice that fires bursts more readily under RSL-3 or 4-HNE, or whose GPX4/GSH baseline
differs, would be a first iron/lipid-peroxide readout for the model; this paper supplies the protocol
shape and the controls that are missing from it (vehicle trace, ferrostatin-1, cell counts). Transfer
verdict: protocol-level only; the findings themselves are wild-type, acute-pharmacological and
unreplicated by the standards of its own methods section.

---

## 8. PMID 42601505 — Puertas-Frias 2026, EMBO Rep: PUFA sequestration and mitochondrial dysfunction-induced ferroptosis (tier 2, new; PARTIAL by choice)

context_policy: SOURCE_FIRST (selection row's line only; registry empty; WWOX is not named anywhere in the artefact).
Depth recorded: `partial_fulltext_read`, because Tables EV1 to EV3 and the five source-data archives
(about 79 MB of per-panel spreadsheets) were inventoried and not opened; every other surface was read
(whole article and Methods, all nine figure images, the Appendix, the Review Process File).

**What it MEASURES.** HEK293 lines lacking complex IV (COX6B1 knock-out, 6BKO), 6BKO rescued by
alternative oxidase (6BAOX) or by COX6B1 re-expression (6BRES), complex II (SDHA) and complex V
(ATP5F1B) knock-outs, wild-type cells at 1 percent oxygen for a week, two immortalised fibroblast
lines from patients with a COX6B1 variant against a control, and plasma from 13 MERRF patients against
23 controls. Readouts: LC-MS metabolomics and lipidomics, 13C-glucose and 13C-glutamine tracing,
proteomics, fatty-acid oxidation, BODIPY lipid-droplet area per cell, GPX4, BODIPY C11 ratio and
CyQUANT proliferation under RSL3 with ferrostatin-1, oleic or palmitic acid and DGAT1/2 inhibitors.

**First-pass observations.**
- Robust descriptive result: OXPHOS-limited cells (knock-outs, hypoxia, patient fibroblasts) store
  more TG, with PUFA-rich TG species up to 9-fold, lipid droplets increase, desaturases (SCD, FADS1,
  FADS2) fall and GPX4 rises; the complex II knock-out shows it with an unchanged NAD+/NADH ratio.
- The causal title claim is thinner than the descriptive result. Desaturase inhibitors do not change
  proliferation; RSL3-induced C11 oxidation is higher in 6BKO, absent in 6BAOX (high GPX4), blocked by
  ferrostatin-1 and by oleic acid. The decisive arm for "sequestration protects" is DGAT1/2
  inhibition plus RSL3 on lipid peroxidation, and Figure 3D has a DGAT1/2i condition only without RSL3;
  in proliferation (Fig 3E), adding DGAT1/2i to RSL3 gives no further fall. Oleic acid is a MUFA
  rescue, not a test of PUFA sequestration. The Review Process File shows one referee stating that no
  causal experiment supports the claims and another asking for exactly the DGAT1/2i lipid-peroxidation
  readout; the authors answered with oleic acid, which they describe as "directly supporting" the
  protective role of sequestration (from my reading of their response: that is an inference beyond the
  experiment).
- A text/panel gap: the text says some highly unsaturated phospholipids rose "up to 40%" in 6BKO;
  Figure 3B bars read by eye show PC and PE species at about 1.6 to 2.2 times WT (INFERENZA from
  approximate bar heights; recorded as a `panel_qualifies_text` locator). Phospholipid PUFAs, the
  peroxidation substrate, therefore rise more than the text says.
- Patients: one control fibroblast line against two patient lines of one variant; plasma 13 versus
  23 with different age ranges, large overlap in the PUFA-TG panel; the authors call it exploratory.
- Statistics: automatic outlier removal (ROUT) and no blinding are stated; proliferation is a DNA
  content read, not a death assay.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty) and, by name
from this lot and the selection file, the WWOX Drosophila respiration/ROS paper (read), the WWOX/HIF1A
glycolytic-shift readings and the WWOX lipid phenotypes (low HDL, hepatocyte-specific knock-out).

**What it changes in the disease model: nothing yet; it supplies one testable bridge and two cautions.**
Bridge (IPOTESI, staged for the Orchestrator because the discovery ledger is one shared file): the
repository holds WWOX loss as raising glycolysis in fibroblasts and as perturbing respiratory function
in the fly; if WWOX deficiency limits OXPHOS even mildly, a lipid-droplet and PUFA-TG signature with
lower desaturase and higher GPX4 would follow in donor-derived WWOX-deficient fibroblasts, readable with
BODIPY area per cell, targeted TG lipidomics and GPX4. Falsifier: no difference in lipid-droplet area or
PUFA-TG species between WWOX-deficient and matched control fibroblasts at equal passage. Counter:
the effect in this paper is driven by knock-outs with abolished respiration (OCR near zero), a far
stronger defect than anything recorded for WWOX; the sign of WWOX on respiration is itself unsettled
(the Drosophila blocked paper, Choo 2015, is unread). Cautions: (1) the paper's "protective
sequestration" title rests on a missing arm and should not be quoted as shown; (2) the MERRF plasma
PUFA-TG panel is exploratory and not a biomarker precedent for a WWOX disease. Transfer verdict:
mechanistic template and readout set, no WWOX content, no system match.

---

## 9. PMID 39995090 — Liang 2026, Neural Regen Res: HIF-1a inhibitor PX-478 and hippocampal ferroptosis in PTZ-kindled mice (tier 2, new)

context_policy: SOURCE_FIRST (selection row's line only; registry empty; WWOX is not named in the artefact).

**What it MEASURES.** Eight-week-old wild-type male C57BL/6 mice, 11 PTZ injections (35 mg/kg every
other day) with or without PX-478 (5 mg/kg i.p. 30 minutes before each PTZ; n = 16 per group for
behaviour, n = 3 for blots and assays, n = 5 for the mitochondrial measure): Racine seizure scores,
kindling success and latencies, H&E, DHE staining, SOD/CAT/GSH-Px activities, MDA, Fe2+, qPCR and
Western for HIF-1a, HO-1, GPX4, PTGS2, FTH1 and transferrin, and mitochondrial length and area by TEM.

**First-pass observations (eight figure images at 394 to 707 px as deposited, Tables 1 and 2).**
- Table 2 (PTZ against PTZ + PX-478): kindled 75.0 against 56.3 percent; kindling latency 16.00 +- 1.21
  against 19.11 +- 1.05 d; seizure latency after the last injection 206.00 +- 10.92 against 215.56 +-
  9.86 s; duration 62.15 +- 3.39 against 48.56 +- 4.72 s. My arithmetic from those values (INFERENZA:
  group sizes for the kindled fraction are taken as 12 and 9 of 16, i.e. the percentages times 16):
  Fisher exact for 12/16 against 9/16 gives P of about 0.46; a t from the summary statistics for
  kindling latency is about 1.9 and for seizure latency about 0.65. So the text's "significantly
  reduced" kindling success and the abstract's prolonged latency are not supported by the table for
  success rate and seizure latency; only seizure duration and the per-injection scores (Fig 2, from
  about the third injection) carry significance marks.
- Text-versus-panel contradiction: the Results sentence lists GPX4 among markers "significantly
  elevated" in PTZ and decreased by PX-478; Figure 6B shows GPX4 mRNA (about 0.45) and protein (about
  0.3) LOWER in PTZ and restored by PX-478 (about 0.9 and 0.8). The Discussion itself says GPX4
  activity falls during ferroptosis. GPX4 is therefore the opposite of the sentence that lists it, and
  the wording appears to lump it with PTGS2, FTH-1 and transferrin (recorded as a
  `text_contradicted_by_panel` locator).
- DHE images (Fig 4A) have no plotted quantification although the Methods describe ImageJ
  quantification; the text says ROS "appeared" higher. H&E (Fig 3) is single fields with no count.
- Ferroptosis is inferred from MDA, Fe2+, marker expression and mitochondrial shape; there is no
  ferrostatin or chelator arm, no lipid-peroxide probe, and no genetic HIF1A manipulation. PX-478 is a
  bis(2-chloroethyl)amino compound (alkylating-type chemistry); the paper treats it as a selective
  HIF-1a inhibitor on the strength of cited work.
- The abstract names CA1 and CA2; Results and figure use CA1, CA3 and DG (abstract not used as
  evidence).

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty) and the
registry-held WWOX/HIF1A readings (glycolytic shift in fibroblasts, hepatic HIF1A).

**What it changes in the disease model: nothing; two connections to name and keep apart.** (a) It is
the second paper in this lot (with the ferroptosis review) that puts HIF-1a/HO-1 and iron between
seizure and neuronal injury, always as a consequence of seizures in wild-type acquired-epilepsy models;
it does not say HIF-1a rises first in a genetic epilepsy. (b) The repository holds HIF1A as raised by
WWOX loss in non-neural systems; a Wwox-null brain showing high HIF1A and HO-1 would be a first iron
route to test, but this paper cannot say which way causality runs. PX-478 is named here only as the
paper's tool: no safety triage was run (BLOCK-1 not reached), and nothing here proposes it for the
reference genotype; its chemistry is a reason for caution, not a lead.

---

## 10. PMID 41002898 — Truong 2025, Membranes: mitochondria-associated membrane dysfunction in neurodegeneration (tier 2, new; narrative review)

context_policy: SOURCE_FIRST (selection row's line only; the selection row says it is the MAM frame for the WWOX
Ca2+ and mitochondrial findings; this read asks whether the article gives any such frame).

**What it MEASURES.** Nothing. It is a narrative review of ER-mitochondria contact sites (tethers
IP3R-GRP75-VDAC1, MFN2, VAPB-PTPIP51, BAP31-FIS1) in Alzheimer, Parkinson, ALS and Huntington disease,
with sections on lipid transfer, calcium and autophagy/apoptosis and a therapy section (a peptide,
SIGMAR1 agonists, curcumin, resveratrol, gene delivery). Counted in this session over the text: the
words epilepsy, seizure, ferroptosis and iron occur zero times, and WWOX zero times.

**First-pass observations.**
- The review does not cover development, epilepsy or inherited metabolic disease, so it cannot
  provide a MAM frame for a WWOX developmental and epileptic encephalopathy; the transfer is by
  vocabulary and candidate readouts only.
- Internal contradictions about direction: the Section 3 summary says MAM changes are increased
  tethering in AD and reduced connectivity in PD and ALS; in the PD paragraph, one sentence says
  PINK1/Parkin loss reduces ER-mitochondria tethering and calcium exchange, and the next says
  PARK2-mutant fibroblasts and Parkin knock-out mice show ER and mitochondria in closer proximity, more
  calcium flow and more MFN2. The direction of the PD change is therefore stated both ways.
- Figure 4's legend describes a schematic with three proteins (MFN2, PACS-2, ATAD3A); the image
  displayed is a different schematic (mitochondrial transfer routes, treatments, and an inset with
  VDAC1, GRP75, Sig-1R, IP3R, RyRs, SERCA) in which none of the three is labelled (recorded as a
  `text_contradicted_by_panel` locator on a legend/figure pair).
- The authors state that whether MAM changes are compensatory or causative remains unclear; the
  trials in Table 3 (curcumin, resveratrol) have amyloid, atrophy or isoprostane outcomes and not MAM
  measures.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted by command the registry query for the
PMID (empty) and `registry_records.py get --theme` for VDAC1, IP3R, ITPR1, MFN2, SIGMAR1, VAPB and HSPA9
(each returned no record; a statement about those queries over the seven surfaces).

**What it changes in the disease model: nothing, and it exposes an empty cell.** No WWOX record in
the repository names any of the seven tether or calcium-channel terms, so the MAM frame has no anchor
here: the selection row's premise (a MAM frame for WWOX calcium findings) was not in the paper and
is not in the registries. A cheap closing step that needs no new reading: look the seven proteins
up in the WWOX interactome already read in this repository (the Hussain 2018 interactome paper has
a complete receipt) and in the Chang laboratory mitochondrial-shuttling papers' text; if none appears,
MAM stays a vocabulary, if one does, it becomes a testable contact-site question. Transfer verdict:
vocabulary only; a review that contradicts itself on the direction of the one disease (PD) most
related to the fragile-site analogue read earlier in this lot.

---

## 11. PMID 25595191 — Lo 2015, Exp Biol Med: "Regulation of cell signaling and apoptosis by tumor suppressor WWOX" (tier 2, new; minireview)

context_policy: SOURCE_FIRST. **Acquisition note (a route, not a result).** The batch selection listed this
deposit as "PMC page/PDF only" and the queue-style routes all failed: PMC efetch XML returned metadata
only, the Europe PMC REST full-text endpoint returned HTTP 500, the Europe PMC render and the SAGE
PDF sat behind a Cloudflare challenge, and the PMC page and PDF returned a reCAPTCHA to both no
User-Agent and a browser-like one; Unpaywall, OpenAlex and Semantic Scholar all point back to the PMC
copy. What worked was the Internet Archive Wayback snapshot of the PMC page (2024-04-18) and, from the
same snapshot, three figure images. It is a lawful free-to-read copy (an author-manuscript PMC
deposit); the digest of the snapshot is in the manifest.

**What it MEASURES.** Nothing. It is a minireview by the group behind much of the WWOX stress,
Zfra and mitochondrial-translocation literature.

**First-pass observations (whole article, three figures).**
- It does consolidate the mitochondrial statements, each as a pointer to a primary: Tyr33-phosphorylated
  Wwox accumulating in mitochondria and nuclei of rodent photoreceptors under constant light (ref 37);
  "WWOX is activated via phosphorylation at Tyr33 and translocates to the cell membrane, mitochondria,
  and nucleus under stress conditions"; Zfra and WWOX translocating to mitochondria after TNF or UV and
  Zfra blocking WWOX-induced cytochrome c release (refs 55 and 57); and "WWOX deficiency decreases
  mitochondrial respiration in mouse embryonic fibroblasts" (ref 54), with the mechanism called
  unexplained. Every context is an acquired stress or a cancer-cell system.
- It states the whole-body Wwox knock-out mouse dies by four weeks, and that the catalytic function of
  the SDR domain is uncharacterised. Nothing concerns biallelic-LoF disease, iron or ferroptosis.
- The one respiration sentence is one the repository can check against its own reading of the cited
  primary: the primary's dossier records reduced Seahorse OCR, lower ATP and NADH, higher lactate and
  normoxic HIF1A in null MEFs, so the minireview's sentence is faithful.
- Housekeeping: a reference (the 2001 tumour-types paper) is listed twice (entries 5 and 30).
- Dependency screen: the reference list contains the 2005 PNAS lung-cancer WWOX restoration paper
  that carries a standing expression of concern (a citation-only dependency here; the repository
  already holds that paper as read).
- Reference reading debt: 57 gene-direct identifiers were read from the page markup; 13 have complete
  receipts, 7 partial, 37 none (counts from `fulltext_receipts.py status` run in this session).

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry stub (unprocessed, clinical relevance
LOW) and, by name, the dossier of the primary behind the respiration sentence.

**What it changes in the disease model: no claim; it records that the mitochondrial-localisation
literature the model cites is a chain of one laboratory's acquired-stress and cancer-cell
observations, restated.** It is the most convenient map of the unread primaries behind those claims:
refs 37 (blocked), 39 (MPP+ and Tyr33 phosphorylation), 55 and 57 (the two Zfra papers), 18 (the 2004
tau paper, one of the three unread primaries the standing brief names). Preserved as a queued block in
the commit candidate so that a later actor can read them in the order the lot prefers.

---

## 12. PMID 34354738 — Munk 2021, Front Genet: an 80 kb PRKN intron deletion lowers its fragility without changing expression (tier 3, new)

context_policy: SOURCE_FIRST. Question the selection row poses: does fragility itself, rather than loss of
expression, matter? Read for what the experiment can and cannot say; WWOX is named nowhere.

**What it MEASURES.** Chicken DT40 lymphoblast cells: PRKN tagged with a tandem Venus-YFP, an 80 kb
deletion of intron 7 (about 55 percent of that intron, about 12 percent of the gene) made by CRISPR
with a floxed blasticidin template; one homozygous clone and two heterozygous clones kept the
full-length allele as an internal control. Readouts: image-cytometry YFP level, RT-qPCR of PRKN and its
co-regulated neighbour PACRG, FISH breakage or constriction at PRKN after aphidicolin, karyotype of the
clones.

**First-pass observations (three figures, three one-page supplements and the tables document).**
- Fragility drops from about 19, 16 and 18 percent of alleles broken (full length, three cell lines)
  to about 8 and 10 percent for the deleted allele of the same cells (P 0.032 and 0.011; Fisher exact
  on counts of 167 to 171 paired alleles, so the alleles within a spread are not independent
  observations; two independent clones only).
- Expression is reported unchanged (reporter, PRKN mRNA); the reporter histogram of the
  homozygous clone sits slightly right of the full-length peak in all three replicates, marked n.s.;
  PACRG is lower in all three clones (about -0.65, -0.27 and -0.17 log2), significant in one and
  put down to clonal variation. So "no impact on expression" is a three-replicate, one-clone result
  for the homozygote, with a visible shift to higher YFP that a strict no-effect reading would not
  predict, although the comparison is marked not significant.
- Two of 14 targeted clones are chromosome 3 trisomic: the targeting itself carries a
  mis-segregation risk, a caveat for any engineered fragile-site gene.
- Authors' own limits: replication timing was not measured; the mechanisms for lower fragility are
  proposed, not tested; the claim to a first controlled experiment on a large intron is theirs.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty) and the
sibling comparator read earlier in this lot (the replication-stress and parkin paper).

**What it changes in the disease model: one sentence of vocabulary, no claim.** It shows in one
system that the breakage frequency of a fragile-site gene and its expression level can be dissociated
(gene length drives fragility without changing mRNA). That is the discrimination the "fragility or
loss" question needs, and the repository has no WWOX counterpart: no record tests FRA16D breakage
against WWOX expression, and the replication-stress paper read earlier shows WWOX transcript falling
after chronic aphidicolin in human fibroblasts, a case where the two may move together. This paper
does not touch human cells, neurons, mitochondria, or phenotype; it cannot say that fragility itself
has a phenotypic consequence, only that it can be changed without changing expression. Transfer: a
design template (an internal control allele, FISH, an expression reporter) and a reminder that a
fragility effect needs a locus-specific assay, which the model does not have.

---

## 13. PMID 27066568 — Schule 2015, Neurol Genet: "Is PARKIN parkinsonism a cancer predisposition syndrome?" (tier 3, new; case note)

context_policy: SOURCE_FIRST. The selection row says it poses "the same two-sided question as WWOX": a
fragile-site gene with neurological and tumour phenotypes. WWOX is not named; read for what the
design can and cannot show.

**What it MEASURES.** One patient: compound heterozygous PARKIN variants (a small deletion and a 118 kb
exon duplication, class-level here), parkinsonism from age 44, a temporal-lobe glioblastoma at 46,
death 14 months after surgery, autopsy findings (infiltrating glioblastoma, severe nigral cell loss,
no Lewy bodies). Two younger brothers are compound heterozygous too, with no statement of their tumour
status. No tumour genotyping, no cohort, no incidence figure for carriers.

**First-pass observations.**
- The inference to a predisposition syndrome rests on the rarity of the combination in one person
  ("may well be more than a coincidence") and a two-hit schematic whose second hit is a placeholder.
- The authors themselves note the combination is rare, that larger studies are needed, and that
  epidemiology points the other way (lower cancer risk in neurodegenerative disease).
- The fragility content is a single sentence: the gene is 1.3 Mb and holds the fragile site
  FRA6E between exons 2 and 8; the paper does not link the patient's variants to fragility
  (an exon duplication is a copy-number event that a fragile site could produce, but it is not argued).

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty).

**What it changes in the disease model: nothing.** The WWOX analogue it invites (biallelic germline
LoF with tumour risk) cannot be asked of the DEE class, whose affected children do not live long
enough for adult tumour ascertainment; it can be asked only of heterozygous carriers, and this note
offers no method for it. It is a reminder, not evidence: a single-case two-hit hypothesis for a
fragile-site gene, with no allele-level or tumour-level data.

---

## 14. PMID 25833766 — Ambroziak 2015, J Appl Genet: PARK2 rearrangement breakpoints in a Polish Parkinson cohort (tier 3, new)

context_policy: SOURCE_FIRST. Read for the one lesson the selection row names (fragile-site instability as a
neurological risk), and for what a mechanism inference from junction sequences can bear.

**What it MEASURES.** DNA from 344 Polish Parkinson patients (171 early-onset, 173 late-onset),
previously Sanger-screened for point variants: MLPA for exon dosage, aCGH for ranges, Sanger sequencing
of breakpoints; eight patients carry deletions or duplications between exons 2 and 7 (2.33 percent of
patients, 1.31 percent of alleles). Junction sequences are scanned for repeats, homology,
palindromes and microhomology and compared with published PARK2 junctions.

**First-pass observations (four figures, three tables).**
- Seven of nine junctions carry 1 to 3 bp of microhomology (two cases carry none); the authors
  conclude this "strongly supports" microhomology-mediated end joining and FoSTeS/MMBIR. My
  arithmetic (INFERENZA, crude chance model): at a chance rate of 0.25 to 0.4 per junction, 7 of 9
  has a binomial probability of about 0.001 to 0.025, so the data do favour microhomology over blunt
  joining; but 1 to 3 bp is also the ordinary scar of NHEJ, so the two named mechanisms are not
  discriminated, and no chance comparison is made in the paper.
- Text against table: the Discussion says no repetitive elements were found within the sequences
  encompassing the breakpoints, while Table 2 lists a LINE-1, SINE/Alu or LTR element on one side in
  four of the eight cases (one-sided repeats do not make homologous recombination, which is the
  authors' point, but the sentence as written is not what the table shows; recorded as a
  `panel_qualifies_text` locator on a table row).
- The caption of Figure 2 names the presymptomatic double-allele carrier "case 6 III-2"; the figure
  has two generations for that case and labels the relative II-3. Recorded as an identifier mismatch
  only; no parent is tied to an exact allele in this record.
- The yield figures are conditional on prior point-variant screening of the same samples.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty for the PMID) and
the theme queries: "microhomology" returns one WWOX paper and the claim that cites it (the B-cell
class-switch junction reading in which Wwox-null primary B cells shift from blunt to long-microhomology
junctions and mutation frequency is unchanged), "FoSTeS" and "MMBIR" return nothing.

**What it changes in the disease model: nothing, and it names one observable that the repository
could put side by side.** The repository holds a murine WWOX-loss measurement that shifts class-switch
junctions toward long microhomology (a repair-pathway-choice endpoint in a claim held in
observation, CLAIM 029) and has no record of the junction structure of human WWOX copy-number
alleles. IPOTESI, stated so and staged for the Orchestrator: published breakpoint junctions of human
WWOX exon deletions (copy-number alleles are among the reported patient alleles; their share was
not re-derived here and the junction sequences of published cases were not looked up) could be scored for microhomology against a chance model, as this paper did for PARK2; a WWOX
rearrangement spectrum with a microhomology share like PARK2's would say the FRA16D alleles arise as
other fragile-site alleles do, while a share different from it would be a first hint of a locus- or
gene-specific repair signature. Falsifier: junction microhomology no different from PARK2 and from
the chance model. Counter: WWOX copy-number alleles in patients are germline events from earlier
generations (meiosis or early embryo), the murine measurement is in B cells, and PARK2 shows only what
a different fragile site does; nothing here tests whether WWOX loss changes the junction type of
its own gene. Transfer: method and comparator only.

---

## 15. PMID 34937577 — Zhang 2021, J Neuroinflammation: "Mitophagy in neurological disorders" (tier 3, new; narrative review)

context_policy: SOURCE_FIRST. The selection row calls it the baseline for the open mitophagy-versus-senolytic
item (CLAIM 010, held as a background-only hypothesis). WWOX is not named and senescence is not
discussed (counted in this session: zero for WWOX, zero for senolytic stems).

**What it MEASURES.** Nothing; a narrative review with a pharmacology table (Table 1) and two
schematics. Epilepsy gets one paragraph: autophagy markers in refractory temporal-lobe epilepsy
tissue, TSC-type mTORC1-pathway mutations raising seizure susceptibility, focal cortical dysplasia with
mTOR over-activation, and rapamycin preventing epilepsy early and reducing seizures late in mice.

**First-pass observations (two figures, Table 1).**
- The conclusions concede that whether targeting mitophagy is more harmful than beneficial is
  unresolved, and the text says the order of mitochondrial dysfunction, defective mitophagy and
  pathogenic-protein accumulation is unclear. Figure 2 draws both lowering mitophagy (3-MA, BNIP3
  silencing, WNT3a, glycine) and raising it (rapamycin, melatonin, NIX, TFEB and others) as leading to
  "neuronal protection".
- The epilepsy evidence is mTOR pathway pharmacology: rapamycin is labelled a mitophagy inducer, yet
  nothing in that paragraph states a mitophagy measurement; the text also misnames rapamycin
  ("silomus") once.
- The one HIF contact: NIX/BNIP3-mediated mitophagy under hypoxia and HIF1-alpha stabilisation.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted by command the three registry records for
the theme "mitophagy" (CLAIM 009's pathway line, CLAIM 010 and its working-model mirror); BNIP3 returns no
record.

**What it changes in the disease model: nothing, and it is not the baseline the row says.** CLAIM 010
asks whether damaged mitochondria, not senescent cells, are the target. This review contains no
senescence content, so it cannot arbitrate; it supports only the generic statement that mitophagy has
context-dependent effects (the claim's own caveat). Across this lot the WWOX-adjacent facts that bear
on CLAIM 010 are indirect and point in different directions: WWOX overexpression produced ROS and a
senescence marker in rat tumour cells (Liu 2022); chronic replication stress lowered WWOX transcript
and raised mtROS in human fibroblasts without mitophagy being the mechanism (Kawabata 2024); and
nothing here measures mitophagy in any WWOX-deficient cell. A stageable pointer (IPOTESI, not a
claim): the registry-held WWOX loss raising HIF1A meets BNIP3/NIX-type mitophagy under HIF1-alpha
stabilisation; BNIP3 and NIX are absent from the repository, so a first step is reading BNIP3 and
BNIP3L transcript and LC3/TOMM20 colocalisation in the WWOX-deficient fibroblast lines. Falsifier:
no change in those readouts. Counter: no WWOX paper in the repository measures BNIP3 and the HIF1A
targets it lists are glycolytic.

---

## 16. PMID 42219438 — Bjorklund 2026, Biometals: "Iron dysregulation in the central nervous system: implications for autism spectrum disorder" (tier 3, new; narrative review)

context_policy: SOURCE_FIRST. The selection row calls it the only iron-in-neurodevelopment review found and notes
iron is entirely absent from the repository. WWOX is not named (zero); ferroptosis occurs 30 times,
myelin 27, epilepsy once (as an ASD comorbidity), seizure zero (counts from the text in this session).

**What it MEASURES.** Nothing. It relays: fetal iron supply (placenta, blood-brain barrier), maternal
and neonatal deficiency and autism risk, single-gene association findings (TFRC, SLC40A1, CP, FTL and
others; Table 2), serum markers and susceptibility-weighted MRI in children (Table 1), and
management (supplementation, chelation).

**First-pass observations (four figures, two tables).**
- The review is internally uneven on its central premise: the text says children with autism show lower
  serum ferritin and haemoglobin, while Table 1 lists a study with no significant ferritin difference;
  an elevated-transferrin cohort is labelled "causal-level evidence"; Mendelian-randomisation support is
  cited secondhand; the authors conclude the findings are heterogeneous and do not support a single
  pathogenic role.
- GPX4 is stated both ways with one reference: the text says autistic progenitor cells resist
  ferroptosis through upregulated GPX4 and overgrow; Table 2 lists GPX4 as reduced antioxidant
  defence with increased ferroptosis susceptibility, citing the same paper (recorded as a
  `panel_qualifies_text` locator between a table row and a text sentence).
- "Iron-dependent superoxide dismutase" is named in autism patients; mammalian superoxide dismutases
  are Cu-Zn and Mn enzymes (domain knowledge, flagged as not checked against a source).
- The developmental-window figure (Fig 3) is a conceptual colour map without a scale; it states that
  about 80 percent of brain iron accumulates in the late prenatal and early postnatal windows.
- It states systemic iron overload is not common in autism, so the ferroptosis argument rests on
  regional accumulation seen by susceptibility imaging.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry query (empty) and the
working model's recorded hypomyelination reading (the neuronal-deletion mouse, CLAIM 003, a
non-cell-autonomous result).

**What it changes in the disease model: nothing, and it names the iron-related observables the
repository lacks.** Its iron readouts for a developing brain are serum ferritin, transferrin
saturation, hepcidin, TFRC, ferroportin and ceruloplasmin genotypes, and susceptibility MRI of deep
grey matter and cortex, with myelination as a downstream process. For WWOX there is no record of any
of them: no plasma ferritin or transferrin saturation in WWOX-DEE case reports (not searched
beyond the registry), no brain-iron imaging. A closing step that needs no new reading: scan the
case reports already in the repository for a stated ferritin, haemoglobin or susceptibility imaging
value and record "none stated" per report. The review does not touch the WWOX-ferroptosis literature
and does not discuss genetic epilepsies; transfer is the readout list only.

---

## 17. PMID 27551439 — Chang and Chang 2015, Cell Death Discov: HELD-partial resume (the primary behind the Sze commentary)

context_policy: QUESTION_DRIVEN. Held before reading: the prior receipt FTR-20261003-27551439-02 (complete
article reading except the supplement) and its manifest, and the selection file's note that the
supplement was owed. **Stated question:** what do the fifteen supplementary time-lapse movies, the two
supplementary figures and the four main figures not declared in the first manifest show about
nucleolus-mitochondrion shuttling and aggregation of TPC6A-delta, and do the movie numbers cited in
the text match the movies?

**Acquisition (the debt was a missing decoder).** The first manifest recorded that the fifteen
movies were not decoded because no video decoder was installed. The movies are small mp4 files on the
PMC open-access S3 mirror; a static ffmpeg build (version 7.0.2) was installed from the imageio-ffmpeg
wheel into the session scratch area and six frames per movie were tiled and opened. This is a
capability finding, not only a reading: see the micro-upgrade in the self-evaluation.

**What the supplement and the unopened figures show.**
- Videos 1 to 3 (one cell, three channels, 6.1 s each, no clock, no scale bar): the cell rounds and
  retracts a tail; no cytoplasmic puncta are resolved in the sampled frames.
- Video 6 (S35G mutant with WWOX): after rounding, a dense bright clump and fragments, an
  apoptotic-body morphology; Videos 4 and 5 are 0.83 s clips with no visible nucleolar translocation.
- Video 8 (EYFP-TPC6A-delta with MitoTracker Red): the transfected cell's cytoplasm turns yellow over
  the frames, which a diffuse cytoplasmic protein overlapping a mitochondrial network also produces;
  there is no colocalisation measure, so mitochondrial relocation is not separable from cytoplasmic
  spread in the movie.
- Videos 10 and 11 (ECFP-TPC6A-delta, CCCP, with and without the MitoTracker channel) show cells
  swelling, blebbing and fragmenting; discrete aggregates are not visible before the last frames.
- Videos 12 to 15 (SDR/D3 run) are four channels of one field; Video 14 (the DIC channel) shows many
  small granules spreading across the field as cells round and bleb, which the authors call
  exosome-like particles; the movie does not characterise them.
- **Cross-reference errors, checked against the movies themselves.** The text cites Videos 8 and 9
  for the CCCP experiment (the movies of that experiment are Videos 10 and 11, as the Figure 6 legend
  says), Videos 10 to 13 for the SDR/D3 run (the legend and the movies are Videos 12 to 15), and Video
  12 for the exosome-like particles (they are in Video 14); Video 8 is cited for two different
  experiments.
- **Text against panel (Figure 6a).** The text puts TPC6A-delta's relocation at hour 3, its
  aggregation at hour 6 and the loss of mitochondrial red signal "in less than 1 h"; the panel is
  sampled at 0, 6, 12, 18 and 24 h, the arrows sit at 12, 18 and 24 h, and the red signal is still
  present at 6 h.
- Supplementary Figures S1 and S2 are human post-mortem Alzheimer hippocampus (TIAF1, phospho-TPC6A,
  TPC6A, WOX1, amyloid-beta), single fields without quantification and without a WWOX-genotype
  comparator or a mitochondrial marker.
- Main figures 1, 4, 5 and 6 add to the earlier reading: Figure 4 shows wild-type TRAPPC6A and the
  delta isoform killing transfected cells to the same extent at every dose in two lines
  (electroporation alone kills about a third), and WWOX overexpression kills too; Figure 6c to f
  show FRET binding of TPC6A-delta to the D3 tail/SDR peaking at about 3 to 3.5 h and to the WW
  domain at 8 to 12 h, with no binding for the SDR alone.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: the earlier reading's locators (the
overexpression-only cell-death readout, the Y112F and S35G contradiction, the unpublished-data
attributions, the Wwox-null cortex immunostaining).

**What it changes.** Nothing in a claim; it narrows what the repository can say about the mitochondrial
arm. The shuttling and aggregation of TPC6A-delta are shown in transfected COS7 and HEK293 cells with
fluorescent fusions under TGF-beta1; the Wwox-null element is one immunostaining and a MEF shuttling
time reported in the text; the movies do not show a mitochondrial endpoint that survives a diffuse-
protein overlap, and the cited movie numbers do not map to the experiments the text names. The
commentary read first in this lot (the Sze deposit) restates the model, so the model's evidence base
is this one laboratory's overexpression system plus two supplementary AD tissue panels; no
WWOX-null neuron measurement of mitochondrial aggregation exists in either paper.

---

## 18. PMID 41677633 — Su 2026, Cells: HELD-partial resume (figures only)

context_policy: QUESTION_DRIVEN. Held before reading: the prior receipt FTR-20261003-41677633-02 and its manifest
(figures recorded captions_only; Figures 2, 3 and 6 not declared as opened). **Stated question:** do
Figures 2, 3 and 6 show what the text says about WWOX induction by serum starvation and hydrogen
peroxide in human SCC-15 cells and mouse fibroblasts, and about Bcl-XL and Mcl-1 mRNA in
Wwox+/+ and Wwox-/- fibroblasts?

**What the three figures show.**
- Figure 2 (SCC-15): the RT-PCR densitometry peaks at 24 h under serum starvation (about 1.37), the
  qPCR of the same condition peaks at 12 h (about 1.6) and is below baseline at 48 h (about 0.8); under
  H2O2 both rise to 48 h. Two assays, two peak times; the text's "negative feedback after 48 h" matches
  the qPCR and not the densitometry.
- Figure 3 (MEFs): the Wwox signal is absent in the null in blot and RT-PCR (specificity confirmed);
  the protein and RT-PCR bar charts in 3A and 3B quantify one representative gel with no error bars or
  statistics, so the "at least four repeats" of the text are visible only in the qPCR of 3C (about 2.6
  and 4.0-fold under serum starvation, about 2.6 and 2.1-fold under H2O2, wild type only).
- Figure 6 (MEFs): Bcl-XL and Mcl-1 mRNA do not fall under serum starvation in either genotype, as the
  text says; the null carries more Bcl-XL mRNA than the wild type at 48 h (about 1.33 against 1.15, a
  significant difference) which the text does not mention.

**What it changes.** Nothing in a claim. The prior reading's direction stands (under serum starvation the
WWOX-null fibroblast is the surviving cell and the mitochondrial membrane potential falls with WWOX
present); the three panels remove an uncertainty about whether the induction and the non-
transcriptional reading were visible in the images. The receipt is closed at complete depth with the
earlier coverage carried and stated as carried.
