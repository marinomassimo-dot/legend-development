# Lodz node discriminator — PMID 32389029 (review) + PMID 33520443 (GDM association)

**Reader:** Scientist B · **Date:** 2026-09-21 · **Branch:** `claude/legend-autonomous-woree-tv6gz8`
**Status:** non-canonical analysis. **READ-ONLY** toward `disease-models/wwox/registries/**`,
`disease-models/wwox/research/**` and `framework/**`. No canonical file was edited, no
`BATCH_COMMIT` was run, no commit candidate was produced, no receipt was recorded. One output file.

**Decision question.** *Does the Lodz (Bednarek / Kośla) node give WOREE (a) a coherent
developmental/neurological sub-programme, and (b) an actionable pathway or independent
corroboration LEGEND does not already have?*

---

## 0 · Ledger check, performed BEFORE reading (mandatory)

| Check | Result |
|---|---|
| `registry_records.py get --pmid 32389029 --hops 1` | **1 identity hit** — `paper_registry_current.md:793` → `## CORPUS-STUB-007`, *"corpus placeholder only"*, **Status: not_processed**, **Claim links: none** |
| `registry_records.py get --pmid 33520443 --hops 1` | **NO RECORD MATCHED** across all seven surfaces (claim, discovery, dismissal, full_text_queue, literature_tracking_log, paper_registry, working_model) |
| `reading_state.py` | **123 papers / 186 receipts.** Neither `32389029` nor `33520443` appears. **Neither carries a receipt.** `31543760` (2 receipts), `35328751` (1) and `36271927` (1) all appear — already read, not re-read here |
| Prior art read first, not re-derived | `next_scientist_scout_20260921.md` §1b/§3 · `hnpc_differentiation_audit_20260920.md` (full) · `AUTONOMOUS_SESSION_STATE.md` · `discovery_ledger_current.md` `DL-MECH-020` (read in place, not grepped for content) |
| The two large registries | **never grepped** — every registry lookup in this file went through `registry_records.py` |

Registry reads were taken at commit `9a2092040523`, working tree clean for the files consulted.

### Retrieval, measured not assumed

`mcp__PubMed__get_full_text_article(["PMC7400721","PMC7811782"])` → `count: 2`, **both bodies
non-empty**:

| PMCID | PMID | `full_text` length | `abstract` length |
|---|---|---|---|
| PMC7400721 | 32389029 | **20,388 characters** | 1,146 |
| PMC7811782 | 33520443 | **52,463 characters** | 1,754 |

Both were read end to end. Source: PubMed / PMC.
Review: Kośla K, Kałuzińska Ż, Bednarek AK, *Exp Biol Med* 2020;245(13):1122–1129 —
[DOI 10.1177/1535370220924618](https://doi.org/10.1177/1535370220924618).
Primary: Baryła I, Płuciennik E, Kośla K, Wojcik M, Zieleniak A, Żurawska-Kliś M, Cypryk K,
Woźniak LA, Bednarek AK, *PeerJ* 2021;9:e10604 —
[DOI 10.7717/peerj.10604](https://doi.org/10.7717/peerj.10604).

### 🔴 Two instrument limits that bound everything below

1. **The review's citation apparatus does not survive extraction.** Every superscript reference
   marker is stripped, and **there is no reference list in the retrieved body** — the single string
   `References` at line 109 is a *column header inside Table 1*. The only two surviving reference
   numbers in the entire artefact are the Table 1 cells `68` (astrocytoma row) and `84`
   (neuroblastoma row). **The task's instruction "quote verbatim with citation numbers" therefore
   cannot be satisfied for any statement in the body: the numbers are not there to quote.** Every
   attribution below is made on *content* — a distinctive finding matched to a primary and then
   verified against `registry_records.py` — and is labelled as such. This is not a novel defect:
   `AUTONOMOUS_SESSION_STATE.md` records the corpus-wide measurement from
   `extraction_damage_report.py` over all 29 local artefacts — **29/29 reference list ABSENT**.
2. **Italicised gene tokens are elided in both artefacts.** In the review, `WWOX` vanishes wherever
   it is italicised, leaving strings such as `"thegene"` and `"aknockout mouse model"`. In the GDM
   paper **every gene symbol in the Results sentences is gone**, leaving `"leukocyte,,,,( all<
   0.0001 )"`. Quotes below are reproduced **exactly as extracted**, elisions included. Any string
   count for a gene symbol is an instrument reading and **never** a biological negative. Counts for
   *roman* words (`gestation`, `splice`, `missense`, `residual`, `proteasome`) are informative.

---

## 1 · VERDICT

> **(a) Is there a coherent developmental/neurological line at Lodz? — NO.**
> The fact that decides it: across 20,388 characters of a review titled *"The WWOX gene in brain
> development and pathology"*, the strings `embryonic day`, `gestation`, `fetal`, `fetus`,
> `trimester`, `cortical plate`, `lamina`, `radial glia` and `postnatal` occur **zero** times (all
> roman words, so the zeros are informative) — the review contains **not one developmental
> timepoint**, and every developmental statement in it is a restatement of somebody else's mouse or
> rat experiment. Lodz's own contribution to brain development remains exactly what the scout said
> it was: **one primary (`31543760`, already read and already audited) and this review of it.**

> **(b) Does the node give WOREE an actionable pathway or independent corroboration LEGEND lacks? — NO.**
> The fact that decides it: `33520443` is **Baryła I … Bednarek AK, Department of Molecular
> Carcinogenesis, Medical University of Lodz** — the *same first author and same senior author, in
> the same department*, as `35328751`, which LEGEND read on 2026-09-21 and for which `DL-MECH-020`
> already records **«peso di corroborazione: uno»**. `35328751`'s own abstract cites this paper as
> its prior evidence (*"It has been proven in the normoglycemic mice cells and in gestational
> diabetes patients."*). Adding it therefore **cannot** raise the corroboration weight of the
> WWOX/HIF1A branch above one, and it is *weaker in evidence class* than what is already held: it
> contains **no perturbation of any kind**.

**Corollary the two papers do produce, and it is not nothing:** the review **propagates forward, in
its own voice, the abstract-versus-Results inversion LEGEND found in `31543760`** — including the
non-significant arm and the expression-versus-secretion slip — one year later, over the same senior
author's signature. See §4.

---

## 2 · Per paper — what was actually done, found, and not tested

### 2a · PMID 32389029 — Kośla, Kałuzińska, Bednarek 2020 (REVIEW)

**Treated throughout as a review. Nothing in it is primary evidence; every assertion is an author
assertion until traced to an experiment.** PubMed `article_types`: `["Journal Article", "Research
Support, Non-U.S. Gov't", **"Review"**]`.

| Field | Value |
|---|---|
| Design | Narrative review, 3 authors, single department (Molecular Carcinogenesis, Medical University of Lodz) |
| Structure | Introduction · Encephalopathy · Neurodegeneration · Brain cancers (Astrocytomas / Glioblastomas / Neuroblastomas) · Table 1 · Conclusion · 2 figures |
| n / experiments | **Zero.** No new data of any kind |
| Centre of gravity | Measured by section: the three brain-cancer subsections plus Table 1 occupy roughly half the body; `proliferation` ×5 vs `interneuron` ×1, `oligodendrocyte` ×1, `Purkinje` ×1 |
| Licence | CC BY-NC 4.0, PMC OA subset |

#### What prenatal / embryonic findings does it state?

**Three, and only three — and all three are restatements.** The review has no developmental data of
its own and assigns no developmental date to anything.

| # | Statement (verbatim, elisions as extracted) | Content-matched primary | Held by LEGEND? |
|---|---|---|---|
| 1 | *"Recently, it has been reported thatknock out in mice indeed cause a disruption of neuronal migration in developing cerebral cortex, hippocampus, and cerebellum. Neuronal migration disorders in KO mice result in foliation impairment and brain malformation. Furthermore, Purkinje cell loss and granular cell apoptosis in the cerebellum and severe hypomyelination were found in the examined animals."* | **PMID 32000863** — Cheng 2020, *Acta Neuropathol Commun*, Wwox-null mouse, GSK3β/seizure axis | ✅ **`PAPER 019`**, `Status: processed`, **`complete_fulltext_read`** (`FTR-20260804-32000863-01`, 5 locators, strict PASS). Claim links 015, 016 |
| 2 | *"A recent study on lde/lde rats, a model of WOREE syndrome, found defects in CNS development that concern both dendrite outgrowth and oligodendrocyte myelination."* | **PMID 32581702** — Iacomino 2020, *Front Neurosci* | ✅ **`PAPER 020`**, `Status: processed`. Source of `CLAIM 039` |
| 3 | *"Studies on aknockout mouse model found the number of hippocampal GABA-ergic interneurons to be reduced accompanied by reduced GABA synthesis and the appearance of neuroinflammation markers."* | **PMID 30290271** — Hussain 2019, *Neurobiol Dis* | ✅ **`PAPER 006`**, `Status: integrated`. Claim links 005, 036 |

**Cortical layering:** *not stated anywhere*. `layer` occurs twice, both in non-neural prose;
`cortical plate`, `lamina`, `radial glia` = 0. The review reports **migration** disruption (item 1)
and never converts it into a laminar readout — correctly, since `32000863` did not measure layers
either.

**Neural progenitor proliferation/differentiation:** stated only through the authors' own hNPC
paper (§4 below). No progenitor kinetics, no cell-cycle exit, no clonal analysis.

**Interneuron vs excitatory lineage:** item 3 is the *only* interneuron statement in the paper.
`excitatory` = **0**. The review therefore carries the GABAergic-interneuron deficit with **no
excitatory comparator at all** — the inhibitory/excitatory balance question is not posed.

**Myelination onset:** *not stated*. What is stated is a retardation, without a timepoint —
> *"So far it is known that the presence of incorrect WWOX protein levels results in myelination retardation, as well as disorders in neurotransmitter management."*

and a severity, also without a timepoint (item 1, *"severe hypomyelination"*). No PND, no
myelin-basic-protein trajectory, no onset date anywhere.

**Timing of Wwox expression in development:** ⚠️ **NOT STATED — and this is the sharpest negative in
the paper.** The review's *own lab's* primary `31543760` contains a FANTOM5 datum (fetal brain
9.2 vs adult 17.7 TPM RLE, recorded in `hnpc_differentiation_audit_20260920.md` §Q4b) that bears
directly on developmental expression timing. **The review does not carry it.** A review of
*"the WWOX gene in brain development"* omits the only expression-versus-developmental-stage number
its own group had published.

The only two statements the review makes that *sound* developmental are both **modal or hedged**,
and their mood must be preserved:

> *"On the other hand, germline mutations are observed very rare and in great majority **may be** lethal in embryonic development."* — Conclusion

> *"In the CNS context, thegene has been found to be pleiotropic, playing a pivotal role in embryonic neural development,neuronal injury, and damage,and in preventing neurodegeneration by limiting pathological protein aggregation."* — Conclusion

⚠️ **Abstract-versus-body mood mismatch.** The Abstract renders the same territory as a flat
declarative — *"A lack of WWOX protein as a consequence of germline mutations results in brain
development disturbances and malfunctions."* — where the Conclusion says *"may be"*. Mild, but it
is the same direction of travel as the inversions in §4, and an abstract-only reader acquires a
certainty the body does not assert.

#### Does it cite any primary LEGEND does not already hold?

**On the evidence retrievable here: NO — and the enumeration is bounded, not exhaustive.**

Because the reference list is absent and every superscript is stripped, a complete crosswalk is
**impossible from this artefact**. What was possible was to take every statement whose content is
distinctive enough to identify a unique primary, resolve it by PubMed field search, and check it
with `registry_records.py`. **Nine were resolvable. All nine are already held.** See §6.

#### Does it state any intervention or rescue in any WWOX-loss model?

**NO — and this is a clean, valuable negative.** `rescue` occurs exactly once, `therapy` once,
`drug` once (in *"drug-resistant epilepsy"*), `treatment` twice (one is MPP⁺ neurotoxin
administration, i.e. disease *induction*). **Every intervention the review reports is WWOX
re-expression in a cancer cell line with intact or mutant p53.** Not one intervention, rescue,
pharmacological or genetic, is reported in any WWOX-loss neural, neuronal, progenitor,
developmental or animal model.

> *"Rescue experiments with ectopic expression ofin tumor cell lines restore a more physiological phenotype of breast cancer, ovarian cancer, or glioblastoma cells, among others."* — Introduction

> *"The level of WWOX expression is thought to be regulated by the circular RNA CircMTO1: CircMTO1 upregulated WWOX production inhibits proliferation in the U251 glioblastoma cell line."* — Glioblastomas

> *"Furthermore, overexpression of thegene in glioblastoma cells is associated with increased radiosensitivity. Interestingly, this effect only occurs on lines with fully functional p53."* — Glioblastomas

> *"Studies of a T98G cell line with exogenously increasedexpression identified a reduction of cell malignancy."* — Glioblastomas

#### Protein stability / folding / degradation / abundance for missense variants? Residual function?

**On WWOX's own protein stability for missense alleles: NOTHING.** `proteasome`, `ubiquitin`,
`half-life`, `abundance`, `residual` = **0** (all roman words — informative zeros). `missense` =
**0** as a string; the concept appears once, worded as *"hypomorphic sense mutations"*.

The one `chaperone` and the one `stability` in the paper are about **WWOX stabilising Tau**, i.e.
WWOX as the chaperone *of a substrate*, never WWOX as the folding-compromised species:

> *"In addition, WWOX can also physically bind Tau protein by its SDR domain and stabilize it."*

> *"It has been hypothesized that WWOX may act as a chaperone that stabilizes Tau from misfolding and aggregation."* — note the mood: *hypothesized*, *may*.

**Residual function is asserted once, at class level, with no measurement and no allele:**

> *"The severity of neuropathological symptoms varies, depending on whether the mutation deprives the protein of some of its functionality or completely prevents its formation."*

Adjacent, and the only quantitative-sounding statement about WWOX dose in the paper — but it is a
**cancer haploinsufficiency** argument, not a WOREE one:

> *"it is not subject to Knudson's two-hit hypothesis: an inactivation of both gene alleles is rare but the loss of one of its alleles predisposes the bearing cells to cancerogenesis due to the insufficient amount of protein produced by the intact allele (haploinsufficiency)."*

#### Does it distinguish WOREE genotype classes?

**It distinguishes exactly TWO classes, and the reference genotype fits NEITHER.**

> *"Two neuropathological phenotypes ofgene mutation have been distinguished."*

> *"The first form is characterized by the presence of hypomorphic sense mutations in thegene exon, causing partial loss of function of the encoded protein, and resulting in the development of SCAR12 spinocerebellar ataxia-12 (MIM 614322)."*

> *"In the second form, the presence of premature STOP codons in two alleles results in a complete lack of WWOX expression and the development of WOREE WWOX-related epileptic encephalopathy (MIM 616211)."*

🔴 **Three consequences, and the third is a fidelity finding.**

1. **`splice` = 0** in the entire artefact (roman word — informative). **Splice alleles do not exist
   in this review's taxonomy.**
2. **`deletion` ×2, both in the cancer sections** (*"deep focal deletions"*, *"copy number
   variations"*). **CNV / whole-exon deletion is absent from the WOREE taxonomy.**
3. 🔴 **The review is NARROWER than its own group's primary, one year earlier.** `31543760`
   (`hnpc_differentiation_audit_20260920.md` §Q5, verbatim) says: *"The WOREE patients exhibiting
   more severe neurological disorders harbor **nonsense/frameshift mutations and/or robust
   deletions of whole exons** of [WWOX] gene."* The review, same senior author, reduces this to
   *"premature STOP codons in two alleles"* — **the deletions are dropped**. That is an unfaithful
   restatement in the direction of over-simplification, and it matters because the dropped class is
   a real WOREE genotype class.

**Net effect for the reference genotype (a destabilising SDR missense allele + a canonical
splice-acceptor allele, carried as decoupled public worked examples):** the review's binary would
force it into the *SCAR12 / hypomorphic* box on the missense allele and has **no box at all** for
the splice allele. The compound-heterozygous WOREE genotype — which `PAPER 063`-era cohort work
(`PMID 40875931`, N/N vs N/M vs M/M) treats as a first-class category — is not represented.

#### What was NOT tested / NOT stated (review)

`gestation`, `fetal`, `fetus`, `trimester`, `embryonic day`, `postnatal`, `cortical plate`,
`lamina`, `radial glia`, `excitatory`, `splice`, `missense`, `residual`, `abundance`, `half-life`,
`proteasome`, `ubiquitin` — all **zero occurrences**, all roman words, all informative. No figure
panel was inspectable; both figure legends (*"Pleiotropic role of WWOX in the development and
function of the central nervous system"*, *"Theinvolvement in neuronal cells differentiation and
maintenance"*) are quotable and were read, and neither carries data.

---

### 2b · PMID 33520443 — Baryła et al. 2021, *PeerJ* (PRIMARY, association)

#### Exact design

| Field | Value (verbatim where quoted) |
|---|---|
| **Species** | **Human.** No animal, no cell line, no organoid |
| **Tissue** | **Maternal peripheral-blood leukocytes**, whole unfractionated population. Not placenta, not fetal tissue, not brain, not nerve |
| **n, cross-sectional arm** | *"A total of 135 Caucasian pregnant women consisted of 37 women with normal glucose tolerance (NGT) and 98 women with GDM"* — **98 cases / 37 controls** |
| **n, longitudinal arm** | **8** (3 months postpartum, group B) and **12** (1 year, group C), each paired against their own first-visit measurement (groups A1, A2) |
| **Timing** | *"the first during the third trimester of pregnancy (at 24–28 weeks' gestation or later if it was not possible during this period) when the patients were diagnosed for GDM, followed by the postpartum second and third visits at 3 months and one year, respectively."* |
| **What was measured** | **mRNA only.** RT-qPCR, 11 genes + 3 housekeeping (`RPLP0`, `RPS17`, `H3F3A`), duplicate reactions, Pfaffl method, universal human reference RNA calibrator. **No SNP. No genotyping. No protein. No enzyme activity. No flux.** |
| **Genes** | WWOX, HIF1A; transport `SLC2A1`, `SLC2A4`; glycolysis `HK2`, `PFK`, `PKM2`, `LDHA`; Wnt `DVL2`, `CTNNB1`; inflammation `NFKB1` |
| **Primary endpoint** | Differential leukocyte mRNA expression of the WWOX/HIF1A-axis genes, GDM vs NGT, at diagnosis. Secondary: postpartum change; gene–gene and gene–phenotype Spearman correlations |
| **Statistics** | Mann–Whitney U (unpaired), Wilcoxon signed-rank (paired), Spearman. Declared α: *"A-value <0.05 was considered as significant."* |
| **Treatment confound, explicitly excluded by design** | *"Of note, because GDM women had not been in receipt of any therapy at the time of inclusion into the study, changes in their metabolic parameters are a result of solely the disease."* |

#### What was found

> *"Quantitative RT-PCR expression data showed that leukocyte,,,,( all< 0.0001 ),(= 0.0004),(= 0.0015)and(= 0.002) mRNA levels were significantly higher, whereas leukocyteexpression was significantly lower (= 0.0134) in the patients with GDM in comparison with the subjects with NGT ()."* — Results

> *"the/index was decreased by approximately 6.5-fold (<0.0001) in the GDM group compared to the NGT group; thus it appears to be a better indicator of leukocyte transcriptional response of the two related genes to GDM than each of these two genes separately, as evidenced by an 1.4- fold decrease forand a 3.8-fold increase forin the diabetic patients."* — Results

**So the headline WWOX effect is a 1.4-fold mRNA decrease.** The "six times reduction" of the
abstract is a **ratio of two ratios**, not a WWOX effect: 1.4 × 3.8 ≈ 5.3, and the ratio statistic
inherits the variance of both. This is not an abstract-vs-Results *inversion* — the Results state
it plainly — but the abstract's *"approximately six times reduction"* invites a reader to attribute
six-fold movement to WWOX, which the Results do not support.

> *"Strikingly, we found significantly higher postpartumexpression in women with prior GDM compared to that displayed by the same women with diagnosed GDM, but its level was comparable to that observed in normal pregnancy."* — Discussion

⚠️ **A "tendency" that sits below the paper's own α.** Results: *"There was also a tendency for
lower leukocyteexpression in the women with GDMthe controls with NGT (= 0.0406)."* — **p = 0.0406
against a declared threshold of p < 0.05 is significant by the authors' own rule, yet is voiced as
a tendency.** Which gene this is cannot be read off the extraction (symbol elided). Arithmetic on
the Results sentence plus the figure-panel enumeration (A=WWOX … L=ratio) and the Discussion's own
statements (*"In the present study, no significant change was found in leukocytegene expression
profile between the GDM and NGT groups"* → `HK2` unchanged; *"a significant decrease in
leukocytemRNA expression was detected"* → `SLC2A4`/GLUT4 down) accounts for 8 up + 1 down + 1
"tendency" + 1 unchanged = 11, and **most plausibly assigns p = 0.0134 to `WWOX` and p = 0.0406 to
`SLC2A4`**. 🔴 **That assignment is a RECONSTRUCTION, not a quote, and is marked as such.** What is
certain and quotable without it: the paper voices one sub-0.05 result as a *tendency* in Results
while its Discussion calls one of the two downregulated genes *"a significant decrease"*.

#### Is there any mechanism? Any perturbation?

**NO, and NO — and the authors say so themselves.**

> *"however, whether these associations have functional relevance for the development of GDM remains to be determined"* — Discussion

> *"The limitation of our research is the fact that it was not possible to investigate the reason for the decrease in WWOX expression in GDM patients."* — Discussion

> *"However, the validity of these findings need to be confirmed in larger studies with more statistical power and with the analysis of protein expression of the components of the WWOX/HIF1A axis in leukocytes of GDM subjects."* — Conclusion

**There is no knockdown, no knockout, no overexpression, no inhibitor, no hypoxia challenge, no
glucose challenge in vitro, no reporter assay — nothing is done to WWOX or to HIF1α anywhere in
this paper.** Direction of causality is unaddressed: GDM→WWOX↓ and WWOX↓→GDM are equally compatible
with every number reported, as is confounding by leukocyte-subset composition, which the authors
raise themselves:

> *"Any discrepancies in our results in relation to the literature data may also result from the fact that leukocytes are examined as a whole population of different cells."* — Discussion

🔴 **The paper's own causal verbs outrun its design**, and LEGEND must not carry them:
Abstract — *"The obtained results **suggest** a significant contribution of thegene to glucose
metabolism"* (hedged, acceptable); Discussion §(iii) — *"an **important contribution** of thegene
to the pathogenesis of GDM by modulation HIF1α activity"* (unhedged causal); Conclusion — *"the
WWOX gene is **proposed as an important contributor to the pathogenesis of GDM**"*. **Association
only. Police the verbs on reuse.**

#### What was NOT tested (GDM paper)

No protein (stated by the authors as future work) · no WWOX genotype or SNP · no splice analysis ·
no enzyme activity · no flux (no Seahorse, no OCR, no ECAR) · no fetal or neonatal outcome · no
placental tissue · no neural tissue, no brain, no seizure, no developmental endpoint of any kind ·
no iron status (the authors flag this as unmeasured, bearing on their anomalous HbA1c result) · no
multiple-comparison correction across 11 genes × 2 groups × many correlations.

⚠️ One internal anomaly the authors flag and cannot resolve: *"Unexpectedly, maternal HbA1c levels,
reflecting glycemic status over the preceding 2–3 months, were significantly lower in the GDM than
NGT group"* — the wrong direction for a hyperglycaemia cohort, left unexplained.

---

## 3 · VERBATIM LOCATORS

Every quote copied character-for-character from the retrieved artefacts, elisions as extracted.
Anchors are the section headings in the PMC body; **no page or reference number is available** (§0).

### 32389029 — PMC7400721

| # | Proposition | Exact quote | Anchor |
|---|---|---|---|
| R1 | The review recognises exactly two WOREE-adjacent genotype classes | *"Two neuropathological phenotypes ofgene mutation have been distinguished."* | Encephalopathy |
| R2 | Class 1 = hypomorphic "sense" mutation → partial LoF → SCAR12 | *"The first form is characterized by the presence of hypomorphic sense mutations in thegene exon, causing partial loss of function of the encoded protein, and resulting in the development of SCAR12 spinocerebellar ataxia-12 (MIM 614322)."* | Encephalopathy |
| R3 | Class 2 = biallelic premature STOP → no WWOX → WOREE. **Deletions/CNV and splice alleles are absent from the taxonomy** | *"In the second form, the presence of premature STOP codons in two alleles results in a complete lack of WWOX expression and the development of WOREE WWOX-related epileptic encephalopathy (MIM 616211)."* | Encephalopathy |
| R4 | Residual function is asserted at class level, unmeasured, allele-free | *"The severity of neuropathological symptoms varies, depending on whether the mutation deprives the protein of some of its functionality or completely prevents its formation."* | Encephalopathy |
| R5 | The migration/cerebellar statement — a restatement of `32000863`, which LEGEND holds with a complete read | *"Recently, it has been reported thatknock out in mice indeed cause a disruption of neuronal migration in developing cerebral cortex, hippocampus, and cerebellum. Neuronal migration disorders in KO mice result in foliation impairment and brain malformation. Furthermore, Purkinje cell loss and granular cell apoptosis in the cerebellum and severe hypomyelination were found in the examined animals."* | Encephalopathy |
| R6 | The `lde` rat statement — restatement of `32581702` (`PAPER 020`) | *"A recent study on lde/lde rats, a model of WOREE syndrome, found defects in CNS development that concern both dendrite outgrowth and oligodendrocyte myelination."* | Encephalopathy |
| R7 | The GABA statement — restatement of `30290271` (`PAPER 006`); the only interneuron sentence in the paper | *"Studies on aknockout mouse model found the number of hippocampal GABA-ergic interneurons to be reduced accompanied by reduced GABA synthesis and the appearance of neuroinflammation markers."* | Encephalopathy |
| R8 | 🔴 **Unfaithful restatement #1** — a human transcriptome is said to have *confirmed* a mouse cell-count + metabolite finding | *"This finding was confirmed in our previous research on human neural progenitor cells (hNPC), in which major changes in the transcription of genes related to neurotransmitter synthesis and management were observed aftersilencing."* | Encephalopathy |
| R9 | 🔴 **Unfaithful restatement #2** — the `31543760` abstract's inversion propagated verbatim (see §4) | *"Consistently, neuronal progenitor cells with silencedshowed enhanced adhesion to extracellular matrix proteins, downregulation of MMP2/9 expression, and impaired 3D growth."* | Encephalopathy |
| R10 | ✅ **Mood correctly preserved here** — "probably" retained on the migration inference | *"WWOX also demonstrated a profound influence on adhesion, cytoskeleton organization, and cellular signaling in hNPC, thus probably contributing to proper neurodifferentiation and neuron migration."* | Encephalopathy |
| R11 | Myelination: a retardation with no onset, no timepoint, no trajectory | *"So far it is known that the presence of incorrect WWOX protein levels results in myelination retardation, as well as disorders in neurotransmitter management."* | Encephalopathy |
| R12 | Embryonic lethality is **modal**, not a finding | *"On the other hand, germline mutations are observed very rare and in great majority may be lethal in embryonic development."* | Conclusion |
| R13 | "Pivotal role in embryonic neural development" is an unsourced-here assertion with no timepoint | *"In the CNS context, thegene has been found to be pleiotropic, playing a pivotal role in embryonic neural development,neuronal injury, and damage,and in preventing neurodegeneration by limiting pathological protein aggregation."* | Conclusion |
| R14 | ⚠️ Abstract states declaratively what the Conclusion states modally | *"A lack of WWOX protein as a consequence of germline mutations results in brain development disturbances and malfunctions."* | Abstract |
| R15 | The only "rescue" in the paper — tumour cell lines | *"Rescue experiments with ectopic expression ofin tumor cell lines restore a more physiological phenotype of breast cancer, ovarian cancer, or glioblastoma cells, among others."* | Introduction |
| R16 | An upstream lever that raises WWOX — glioblastoma line, WWOX-competent | *"The level of WWOX expression is thought to be regulated by the circular RNA CircMTO1: CircMTO1 upregulated WWOX production inhibits proliferation in the U251 glioblastoma cell line."* | Glioblastomas |
| R17 | WWOX overexpression → radiosensitivity, **conditional on intact p53** | *"Furthermore, overexpression of thegene in glioblastoma cells is associated with increased radiosensitivity. Interestingly, this effect only occurs on lines with fully functional p53."* | Glioblastomas |
| R18 | The only `stability` statement is about **Tau**, not about WWOX | *"In addition, WWOX can also physically bind Tau protein by its SDR domain and stabilize it."* | Neurodegeneration |
| R19 | The only `chaperone` statement — and it is hypothesis-mood, about Tau | *"It has been hypothesized that WWOX may act as a chaperone that stabilizes Tau from misfolding and aggregation."* | Neurodegeneration |
| R20 | The WWOX/HIF1α mechanism, restated from `PAPER 024` (`25012504`) which LEGEND holds | *"WWOX has been found to physically interact with HIF1α destabilizing this protein and inhibiting its transcriptional activity against aerobic glycolytic genes under physiological conditions."* | Glioblastomas |
| R21 | WWOX dose-sensitivity is argued as **cancer haploinsufficiency**, not as WOREE residual function | *"it is not subject to Knudson's two-hit hypothesis: an inactivation of both gene alleles is rare but the loss of one of its alleles predisposes the bearing cells to cancerogenesis due to the insufficient amount of protein produced by the intact allele (haploinsufficiency)."* | Introduction |

### 33520443 — PMC7811782

| # | Proposition | Exact quote | Anchor |
|---|---|---|---|
| G1 | Design: human, cross-sectional, 98 cases / 37 controls, Lodz clinic | *"A total of 135 Caucasian pregnant women consisted of 37 women with normal glucose tolerance (NGT) and 98 women with GDM were enrolled and studied at the Outpatient Diabetological Clinic in Lodz, Poland."* | Materials & Methods — Study participants |
| G2 | Sampling window: third trimester, 24–28 weeks or later. **Maternal, not fetal** | *"the first during the third trimester of pregnancy (at 24–28 weeks' gestation or later if it was not possible during this period) when the patients were diagnosed for GDM, followed by the postpartum second and third visits at 3 months and one year, respectively."* | Materials & Methods — Study participants |
| G3 | Primary result — gene symbols elided by the extractor | *"Quantitative RT-PCR expression data showed that leukocyte,,,,( all< 0.0001 ),(= 0.0004),(= 0.0015)and(= 0.002) mRNA levels were significantly higher, whereas leukocyteexpression was significantly lower (= 0.0134) in the patients with GDM in comparison with the subjects with NGT ()."* | Results |
| G4 | ⚠️ A p = 0.0406 result voiced as a "tendency" against a declared α of 0.05 | *"There was also a tendency for lower leukocyteexpression in the women with GDMthe controls with NGT (= 0.0406)."* | Results |
| G5 | **The WWOX effect is 1.4-fold; the "six-fold" is a ratio of ratios** | *"the/index was decreased by approximately 6.5-fold (<0.0001) in the GDM group compared to the NGT group; thus it appears to be a better indicator of leukocyte transcriptional response of the two related genes to GDM than each of these two genes separately, as evidenced by an 1.4- fold decrease forand a 3.8-fold increase forin the diabetic patients."* | Results |
| G6 | Postpartum reversal, on n = 8 and n = 12 | *"Strikingly, we found significantly higher postpartumexpression in women with prior GDM compared to that displayed by the same women with diagnosed GDM, but its level was comparable to that observed in normal pregnancy."* | Discussion |
| G7 | 🔴 **The authors themselves decline causality** | *"however, whether these associations have functional relevance for the development of GDM remains to be determined"* | Discussion |
| G8 | 🔴 **No mechanism was investigable** | *"The limitation of our research is the fact that it was not possible to investigate the reason for the decrease in WWOX expression in GDM patients."* | Discussion |
| G9 | 🔴 **No protein was measured — stated as future work** | *"However, the validity of these findings need to be confirmed in larger studies with more statistical power and with the analysis of protein expression of the components of the WWOX/HIF1A axis in leukocytes of GDM subjects."* | Conclusion |
| G10 | Underpowered longitudinal arm, declared | *"there was a relatively small population size of postpartum patients with prior GDM (= 8 and= 12 at 3 months and 1 year postdelivery, respectively) compared to the number of GDM women who participated in the study (= 98), limiting our statistical significance."* | Discussion |
| G11 | Unresolved confound: unfractionated leukocytes | *"Any discrepancies in our results in relation to the literature data may also result from the fact that leukocytes are examined as a whole population of different cells."* | Discussion |
| G12 | Treatment confound excluded by design (a genuine strength) | *"Of note, because GDM women had not been in receipt of any therapy at the time of inclusion into the study, changes in their metabolic parameters are a result of solely the disease."* | Materials & Methods — Study participants |
| G13 | A clean internal negative: HK2 unchanged | *"In the present study, no significant change was found in leukocytegene expression profile between the GDM and NGT groups."* | Discussion |
| G14 | An unexplained anomaly the authors flag | *"Unexpectedly, maternal HbA1c levels, reflecting glycemic status over the preceding 2–3 months, were significantly lower in the GDM than NGT group, although their values were within the normal range in both groups with an A1C<6.5%"* | Discussion |

---

## 4 · The fidelity finding — the inversion propagates into the review literature

LEGEND already holds, from `hnpc_differentiation_audit_20260920.md`, that `31543760`'s **abstract**
states a non-significant result as a finding and mislabels an assay:

- ECM-mixture adhesion: Results *"(= 0.0626)"*, figure caption *"the tendency not reaching the
  statistical significance (0.0626)"*, against a declared α of 0.05 — yet the abstract conjoins it
  with the significant fibronectin arm.
- MMP2/9: Results say **secretion** (gelatin zymography on conditioned medium); the abstract says
  **expression**.

🔴 **The 2020 review reproduces both errors, in its own voice, over the same senior author's
signature** (locator R9):

> *"Consistently, neuronal progenitor cells with silencedshowed enhanced adhesion to extracellular matrix proteins, downregulation of MMP2/9 expression, and impaired 3D growth."*

*"extracellular matrix proteins"* (plural, unqualified) carries the **p = 0.0626 arm** as a finding
and drops the fibronectin qualifier that was the only significant one; *"MMP2/9 expression"* carries
the assay mislabel. **The review is citing its own abstract, not its own Results** — the same
failure mode `DL-MECH-020` recorded on 2026-09-21 for `36271927` citing `35328751`'s Discussion
over its Results. That is now **twice, in two different Lodz reviews, on two different axes.**

🔴 **A second, independent fidelity defect** (locator R8): the review says the mouse GABAergic
finding *"was confirmed in our previous research on human neural progenitor cells (hNPC)"*. It
cannot have been. `30290271` measured **interneuron counts, GABA synthesis and neuroinflammation
markers in mouse hippocampus**; `31543760` measured **CAGE transcript abundance in a human
H9-derived progenitor monoculture in which, by the authors' own statement, every differentiated
cell was MAP2⁺/TUJ1⁺ and GFAP⁻/GalC⁻** — there is no interneuron, no GABA measurement and no glia
in that system. A transcriptional correlate in a different species, a different measurement class
and a cell population that contains none of the measured entity **is not a confirmation**. It is a
consistency observation at best. **Strength-of-evidence inflation; flag wherever R8 is reused.**

✅ **One restatement that is faithful, and should be recorded as such** (locator R10): the review
keeps *"probably"* on the migration/neurodifferentiation inference — correctly, since `31543760` ran
no migration assay (GO enrichment at FDR < 0.25 only). The authors were capable of preserving mood;
they simply did not do so in R8 and R9.

---

## 5 · Can 33520443 serve as independent corroboration of `DL-MECH-020`? — NO

`DL-MECH-020` carries the standing caution: *"il ramo HIF1α/WWOX è stato lavorato anche dal gruppo
Bendinelli/Desiderio (CORPUS P396, Eur J Cancer 2013), oggi in watchlist per ritrattazioni seriali →
non usare quella linea come corroborazione indipendente."* The brief asks whether the Lodz line can
replace that branch. **It cannot, for four independent reasons, any one of which is sufficient.**

1. 🔴 **It is not an additional voice — it is the same voice, upstream.** Authors:
   **Baryła I, Płuciennik E, Kośla K, …, Bednarek AK**, Department of Molecular Carcinogenesis,
   Medical University of Lodz. `35328751` (already read, receipt `FTR-20260921-35328751-01`):
   **Baryła I, Styczeń-Binkowska E, Płuciennik E, Kośla K, Bednarek AK**, same department. Same
   first author, same senior author, same institution. Worse: `35328751`'s own abstract names this
   paper as its prior evidence — *"It has been proven in the normoglycemic mice cells and in
   gestational diabetes patients."* `DL-MECH-020` already scored this arc at **corroboration weight
   one**. Reading its upstream member does not make it two.
2. 🔴 **It is the weakest evidence class on the axis, not a stronger one.** `25012504`/`PAPER 024`
   (Abu-Remaileh & Aqeilan) had a genetic and pharmacological HIF1α perturbation that **reverted**
   glucose uptake. `35328751` had a CRISPR-polyclonal knockdown with a measured lactate readout.
   `33520443` has **no perturbation at all** (G7, G8). An association study cannot corroborate a
   mechanism; it can at most be consistent with one.
3. 🔴 **It measures the wrong layer.** mRNA only, no protein (G9), no activity, no flux — and
   `DL-MECH-020`'s live defect is precisely that *"la metà «via dall'OXPHOS» della cornice Warburg,
   nell'uomo, non è misurata: è inferita da un mRNA."* **This paper adds another mRNA to a
   deficiency that is already an mRNA deficiency.** It makes the debt larger, not smaller.
   *(Protein abundance ≠ function — and here there is not even protein abundance.)*
4. 🔴 **Wrong tissue, wrong life stage, wrong direction of interest.** Maternal peripheral
   leukocytes in the third trimester. `brain`, `neuron`, `seizure`, `development` play no part.
   "Gestational" in the title refers to the **mother's** metabolic state, not to fetal or embryonic
   biology — nothing fetal, placental or neonatal was sampled. The one real asset — a human tissue
   in which WWOX and HIF1A move in opposite directions — is a tissue with no bearing on a
   neurodevelopmental encephalopathy.

✅ **What it does contribute, stated at its true weight:** a **human**, in-vivo, non-cancer,
non-transformed tissue in which reduced WWOX mRNA co-occurs with elevated HIF1A mRNA and elevated
HIF1α-target glycolytic transcripts, **and reverses when the metabolic stress lifts** (G6). That is
a genuine and non-trivial observation, and it is the strongest *consistency* datum the WWOX/HIF1A
axis has outside cancer and MEFs. It is **consistency, from inside the existing node** — not
corroboration, and not independence.

⚠️ **And it inherits the tension `DL-MECH-020` already recorded** against the ketogenic rationale
`HYP-20260709-01`: this paper's framing is that **HIF1α-driven glycolysis is the pathology**, while
the review's neighbour `36271927` states *"increasing glycolysis may slow neurodegeneration."* The
axis still points in two directions depending on the tissue asked.

---

## 6 · NEW PRIMARIES

**None. Zero genuinely new primaries were identified — and the enumeration is bounded, not
exhaustive, for a stated instrument reason.**

Because the review's reference list is absent from the extraction and every superscript marker is
stripped (§0), an exhaustive crosswalk is impossible from this artefact. What was done instead:
every statement whose content uniquely identifies a primary was resolved by PubMed field search and
then checked with `registry_records.py`. **Nine resolved. Nine already held.**

| Review statement | Resolved primary | `registry_records.py` verdict |
|---|---|---|
| KO-mouse migration / foliation / Purkinje / hypomyelination (R5) | **32000863** Cheng 2020 *Acta Neuropathol Commun* | ✅ `PAPER 019`, `processed`, `complete_fulltext_read` `FTR-20260804-32000863-01` |
| `lde/lde` rat dendrite + oligodendrocyte myelination (R6) | **32581702** Iacomino 2020 | ✅ `PAPER 020`, `processed`, source of `CLAIM 039` |
| Hippocampal GABAergic interneuron reduction + neuroinflammation (R7) | **30290271** Hussain 2019 | ✅ `PAPER 006`, `integrated`, claims 005/036 |
| "our previous research on human neural progenitor cells" (R8/R9/R10) | **31543760** Kośla 2019 | ✅ read, 2 receipts, audited `hnpc_differentiation_audit_20260920.md` |
| TAP-MS, 216 WWOX interactors, ER/Golgi/endosome/lysosome/trafficking, Dvl1/Dvl2 top hits | **30619736** Hussain/Aldaz 2018 *Front Oncol* | ✅ `PAPER 032`, `claim_linked`, source of `CLAIM 026` |
| WWOX physically destabilises HIF1α, inhibits glycolytic transactivation (R20) | **25012504** Abu-Remaileh & Aqeilan 2014 | ✅ `PAPER 024`, `processed` |
| Drosophila aerobic metabolism / Idh / Cu-Zn SOD | **21075834** (Adelaide) | ✅ read, `complete_fulltext_read` in `reading_state.md` |
| CircMTO1 → WWOX → U251 proliferation (R16) | **31456594** | ✅ 2 identity hits in registry |
| Astrocytoma IHC, 38 patients, survival, supratentorial (Table 1 ref `68`) | **23675860** | ✅ 2 identity hits in registry |
| "A detailed review … published by Serin" | **30094525** Serin 2018 *Neurol Sci* — **a review, not a primary** | ⚠️ no identity record, but **already queued**: `FT-032`, priority MEDIA-ALTA, flagged as *"la correlazione genotipo-fenotipo pre-Oliver"*. Known, not new |

**Declared residue (honest debt).** The review's unresolvable citations are concentrated in its
oncology sections — esophageal/colon/stomach/bladder/uterine deletion studies, the 67-patient GBM
LOH/methylation cohort, the neuroblastoma study behind Table 1 ref `84`, the p53-dependent
U373MG/U87MG apoptosis work, the MPP⁺ Parkinson model, the steroid-receptor/NSYK work. Some of
these are probably absent from LEGEND. **None of them would change a WOREE conclusion**, and none
is developmental. I am not listing them as acquisition targets, because a speculative oncology PMID
recovered without its citation number is a guess dressed as a lead.

**`33520443` cites no primary of WOREE relevance** — its bibliography is diabetes epidemiology,
HIF1α metabolism and methylation.

---

## 7 · NEGATIVE RESULTS — preserved explicitly

A clean negative is a valid output. These are the negatives, stated as negatives.

### From 32389029 (review)

| # | Negative | Grounds |
|---|---|---|
| N1 | **No developmental timepoint exists anywhere in the review.** `embryonic day`, `gestation`, `fetal`, `fetus`, `trimester`, `postnatal` = 0 occurrences (roman words → informative) | string census over the 20,388-char body |
| N2 | **No cortical-layering statement.** `cortical plate`, `lamina`, `radial glia` = 0; `layer` ×2, both non-neural | ibid. |
| N3 | **No excitatory-lineage comparator.** `excitatory` = 0; `interneuron` ×1 | ibid. |
| N4 | **No myelination-onset date.** `myelin`-family ×3, all severity or retardation, never onset | R11, R5 |
| N5 | **No intervention or rescue in ANY WWOX-loss neural, neuronal, progenitor, developmental or animal model.** Every intervention in the paper is WWOX re-expression in a cancer cell line | R15, R16, R17 |
| N6 | **Nothing on WWOX's own protein stability, folding, degradation or abundance for missense alleles.** `proteasome`, `ubiquitin`, `half-life`, `abundance`, `residual`, `missense` = 0 (roman) | §2a |
| N7 | **Splice alleles do not exist in the review's genotype taxonomy.** `splice` = 0 (roman) | R1–R3 |
| N8 | **CNV / whole-exon deletion is absent from the WOREE taxonomy**, although the same group's 2019 primary included it | R3 + `31543760` Introduction via the hNPC audit |
| N9 | **The review does not carry the fetal-vs-adult WWOX expression datum from its own group's primary** (9.2 vs 17.7 TPM RLE) | absence, verified by census N1 |
| N10 | 🔴 **"Not stated" is not "absent."** Every one of N1–N9 is a statement about *this review*, never about WWOX biology. The review is an author assertion layer; nothing it omits is thereby untrue |

### From 33520443

| # | Negative | Grounds |
|---|---|---|
| N11 | **`HK2` mRNA: no significant difference, GDM vs NGT.** A measured, reported negative, contradicting a rodent literature the authors cite | G13 |
| N12 | **No protein was measured**, stated by the authors as required future work | G9 |
| N13 | **No perturbation of any kind.** No causal claim is licensed by this design | G7, G8 |
| N14 | **No WWOX genotyping, no SNP, no splice analysis.** Despite "association" in the title, this is an *expression* association study, not a genetic one | Methods |
| N15 | **No fetal, placental, neonatal or neural tissue.** "Gestational" is maternal | G1, G2 |
| N16 | **No multiple-comparison correction** across 11 genes and many correlations | Statistical analysis |
| N17 | ⚠️ **A p = 0.0406 result is voiced as a "tendency" against the paper's own α = 0.05**, and the Discussion calls one of the two downregulated genes "a significant decrease." Gene identity not recoverable from the extraction; reconstruction in §2b is marked as reconstruction | G4 |

---

## 8 · Therapeutic classification

Each intervention-like item receives **exactly one** label.

| Item | Source | Classification | Why |
|---|---|---|---|
| Ectopic WWOX re-expression restores a "more physiological phenotype" in breast/ovarian/GBM cell lines | R15 (review, 2nd-hand) | **NOT TRANSFERABLE TO WOREE** | The endpoint is malignancy reduction in a transformed line with an intact endogenous locus. It is WWOX-restoration *in kind*, but nothing about a cancer line's phenotype reversal speaks to a developing brain, and no neural or developmental endpoint was measured |
| WWOX overexpression in T98G → reduced malignancy, adhesion, 3D growth | R-Glioblastomas (review, 2nd-hand; Lodz's own prior work) | **NOT TRANSFERABLE TO WOREE** | Same as above. It is also the assay panel the hNPC study reused, which is why that study has no neurodevelopmentally specific readout |
| CircMTO1 → upregulated WWOX production → inhibits U251 proliferation | R16 (review, 2nd-hand) | **NOT TRANSFERABLE TO WOREE** | Conceptually an **UPSTREAM/WWOX-DEPENDENT** lever — it raises WWOX from an intact locus. In biallelic LoF WOREE there is no competent transcript to upregulate in null/null, and for splice or destabilising-missense alleles raising output of a defective product is unvalidated. Reclassify only if evidence of residual functional protein plus a neural endpoint appears |
| WWOX overexpression → radiosensitisation, **only in p53-wild-type lines** | R17 (review, 2nd-hand) | **NOT TRANSFERABLE TO WOREE** | Radiosensitisation is an oncology endpoint; the p53 conditionality makes it context-locked |
| WWOX pro-apoptotic function (pTyr33) "may be blocked by JNK1"; MPP⁺ Parkinson model | R-Neurodegeneration (review, 2nd-hand) | **MECHANISTIC PROBE ONLY** | MPP⁺ is disease induction, not therapy; the JNK1 statement is about endogenous regulation of *elevated* WWOX — the opposite direction from WOREE, where WWOX is reduced or absent |
| WWOX binds and stabilises Tau via the SDR domain; WWOX-as-chaperone | R18, R19 (review, 2nd-hand, hypothesis-mood) | **MECHANISTIC PROBE ONLY** | An interaction and an explicit hypothesis, not an intervention. Note for LEGEND's proteostasis line: this is WWOX chaperoning a *substrate*, and is **not** evidence about WWOX's own foldability |
| The whole of `33520443` | — | **no intervention exists to classify** | Zero perturbations. The only therapeutic aspiration the Lodz metabolic line expresses anywhere targets **WWOX in diabetes**, i.e. the opposite disease direction — already recorded under `DL-MECH-020` |

**Summary: the Lodz node yields no therapeutic candidate for WOREE at any classification level.**

---

## 9 · Genotype transferability

For the WOREE genotype classes LEGEND tracks. "Transfer" means: could a finding in these two papers
change a conclusion about that class?

| Genotype class | 32389029 (review) | 33520443 (GDM) |
|---|---|---|
| **null / null** (biallelic nonsense/frameshift) | ⚠️ **Partially — but only as second-hand restatement.** This is the only class the review's taxonomy names for WOREE (R3), and its three developmental restatements (R5–R7) all derive from **full-null mouse or rat models**, which map to null/null. LEGEND already holds all three primaries directly, so the transfer adds nothing it did not have first-hand | ❌ No — no genotype was measured; the subjects are metabolically stressed but genotypically unselected adults |
| **splice / null** | ❌ **No.** `splice` = 0 in the review; the class is absent from its taxonomy (N7). The reference genotype's splice-acceptor allele has no representation here | ❌ No |
| **splice / missense** (the reference genotype class) | ❌ **No, and the review would actively mis-sort it** — the missense allele would be pushed into the SCAR12/hypomorphic box (R2) and the splice allele has no box (N7). Do not use R1–R4 as a classifier for compound heterozygotes | ❌ No |
| **missense / missense** | ⚠️ **Only as a naming convention**, via R2 (hypomorphic sense mutations → partial LoF → SCAR12). The review offers **no** protein-level stability, folding or residual-activity datum (N6) that could discriminate one missense from another | ❌ No |
| **residual-protein alleles** | ⚠️ **One class-level assertion only** (R4), unmeasured and allele-free. R21's haploinsufficiency argument is about *cancer risk in carriers*, not about residual neural function, and must not be repurposed | ❌ No |
| **large deletion / CNV** | ❌ **No — actively omitted** (N8). The review's `deletion` occurrences are somatic cancer deletions, and it drops the whole-exon-deletion class its own group's 2019 primary had included |
| **Any class, on the metabolic axis** | — | ⚠️ **Class-agnostic at best.** The WWOX↓ in these subjects is *acquired* transcriptional downregulation in a stressed adult tissue. It is a statement about a *rheostat*, not about a germline lesion, and the mapping from "1.4-fold lower leukocyte mRNA in a diabetic pregnancy" to "a constitutive biallelic loss in a developing brain" is not supported by anything in the paper |

**Bottom line on transferability: nothing in either paper transfers first-hand to any WOREE
genotype class. Every transferable item arrives second-hand from a primary LEGEND already holds
with a receipt.**

---

## 10 · DEFAULTS_TAKEN

1. **Attribution by content, not by citation number.** The brief asked for citation numbers; the
   extraction has none (§0). I resolved primaries by matching distinctive findings via PubMed field
   search and verifying with `registry_records.py`, and labelled every such attribution as
   content-matched. **An alternative default — reporting "cannot answer" — would have suppressed a
   real and checkable answer.**
2. **The gene-identity reconstruction in §2b is marked as a reconstruction, not a quote.** I showed
   the arithmetic (8 up + 1 down + 1 "tendency" + 1 unchanged = 11) and the two Discussion sentences
   that pin `HK2` and `SLC2A4`, rather than asserting the assignment or silently dropping the
   finding. The p = 0.0406-called-a-tendency observation stands **without** the reconstruction.
3. **`31543760` was not re-retrieved.** Per instruction. All statements about it come from
   `hnpc_differentiation_audit_20260920.md`, which quotes it verbatim. Where the fidelity comparison
   in §4 depends on a `31543760` quote, that quote is the audit's, and is attributed to the audit.
4. **Fidelity of restatement treated as a first-class finding**, per the brief's instruction that
   unfaithful restatement is itself a finding. §4 is therefore a section, not a footnote.
5. **No exhaustive oncology-citation recovery was attempted.** The nine resolvable primaries were
   checked; the oncology residue was declared as debt in §6 rather than guessed at. Cost/benefit:
   a speculative PMID with no citation number is not a lead.
6. **Independence judged on institution + author + citation direction**, following the `lde`-node
   lesson in `next_scientist_scout_20260921.md` §1c ("disambiguate on affiliation"). Here the
   affiliation check was decisive and ran the other way: it collapsed an apparently separate paper
   into a node LEGEND had already weighted.
7. **Nothing was recorded, queued, promoted or receipted.** `32389029` remains `CORPUS-STUB-007 /
   not_processed` and `33520443` remains absent from every registry. This file is a discriminator,
   not a reading of record. If either is ever promoted, this file is the reading it should start
   from, not replace.

---

## 11 · 🔴 Gate state this file creates, declared rather than routed around

**`legend_lint.py .` → `BLOCK_BATCH_COMMIT`, caused by this file, on exactly one citation:**

```
[UNREAD PREMISE] PMID 33520443 cited in lodz_node_discriminator_20260921.md
unread_premises: 1/0
[BLOCK_BATCH_COMMIT] UNREAD_PREMISE: 1 reasoning-layer citations lack any read receipt,
registry full-text declaration or queue entry — above the baseline of 0.
```

Verified by removal: with this file absent the same tree lints **PASS**. `32389029` clears the
check; `33520443` does not, because it has **no record on any surface** (§0).

**Why it is here and was not evaded.** `unread_premises()` clears a citation on exactly three
grounds — a persisted `complete_fulltext_read` receipt, a registry record declaring the full text
reviewed, or a full-text-queue entry. **The correct ground applies: 33520443 was read end to end
this session, all 52,463 characters.** The receipt is precisely the artefact this task forbade me
to write (READ-ONLY toward every canonical file; exactly one new file). So the gate is reporting a
true fact about the *repository* — no receipt exists — and a false one about the *reading*.

The detector's own docstring says declared debt is legitimate and *"Silence is not."* Renaming the
token to `PMCID PMC7811782` or to a bare DOI would silence the check without changing the state,
which is the behaviour the code comment names as the failure to avoid. **The citation stays in the
`PMID 33520443` form, and the block stays visible.**

**Scope of the block:** `GATE: only BATCH_COMMIT blocked — DEEP_DIVEs may proceed.` Nothing else in
the tree is affected, and no canonical file was touched by this session.

**Remedy, for whoever holds the authority this task withheld — one of:**
1. Record `FTR-<date>-33520443-01` (`complete_fulltext_read`; the reading is in §2b/§3 of this
   file) via `fulltext_receipts.py record`, then re-run `legend_lint.py`. **This is the correct
   fix**, because it makes the ledger true; or
2. Add `33520443` to `full_text_queue_current.md` as declared reading debt — cheaper, but it
   records the paper as *unread*, which it is not; or
3. Raise `unread_premise_baseline:` in `framework/state/state_manifest_current.md` from 0 to 1 —
   **do not do this.** The ratchet was driven to 0 on 2026-09-21 and `growth_anchors` reported
   `RATCHET_IMPROVED`; giving that back to paper over a receipt nobody was allowed to write would
   be the worst of the three.

---

*Source: PubMed / PMC, retrieved 2026-09-21 via `mcp__PubMed__get_full_text_article`.
Kośla K, Kałuzińska Ż, Bednarek AK. Exp Biol Med (Maywood). 2020;245(13):1122–1129.
[DOI: 10.1177/1535370220924618](https://doi.org/10.1177/1535370220924618).
Baryła I, Płuciennik E, Kośla K, Wojcik M, Zieleniak A, Żurawska-Kliś M, Cypryk K, Woźniak LA,
Bednarek AK. PeerJ. 2021;9:e10604. [DOI: 10.7717/peerj.10604](https://doi.org/10.7717/peerj.10604).
Comparators named and verified against the registries via `registry_records.py`:
[DOI: 10.3389/fncel.2019.00391](https://doi.org/10.3389/fncel.2019.00391) ·
[DOI: 10.1186/s40478-020-0883-3](https://doi.org/10.1186/s40478-020-0883-3) ·
[DOI: 10.3389/fnins.2020.00644](https://doi.org/10.3389/fnins.2020.00644) ·
[DOI: 10.1016/j.nbd.2018.09.026](https://doi.org/10.1016/j.nbd.2018.09.026) ·
[DOI: 10.3389/fonc.2018.00591](https://doi.org/10.3389/fonc.2018.00591) ·
[DOI: 10.1038/cdd.2014.95](https://doi.org/10.1038/cdd.2014.95) ·
[DOI: 10.3390/ijms23063326](https://doi.org/10.3390/ijms23063326).
**Not medical advice.***
