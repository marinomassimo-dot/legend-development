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
