# Audit — the WWOX/HIF1α glycolysis arc, read at source

**Scientist A · 2026-09-21 · READ-ONLY · no canonical file modified**

Both target papers were the last two `UNREAD_PREMISE` entries in the repository. Both have now been
fetched, persisted and read end to end. Neither carried a prior receipt
(`fulltext_read_receipts.jsonl` returned 0 for both PMIDs before fetching).

Sources retrieved from PubMed / PubMed Central.

---

## 0 · VERDICT

**No. As the field itself states it, the HIF1α/glycolysis arc does not support a metabolic
intervention in a WWOX-loss genotype at better than HYPOTHESIS strength: the arc is real but is
measured almost entirely in fibroblasts, muscle, liver, flies and cancer lines; it is never
measured in neural tissue or in a developmental setting; its direction is inconsistent across
conditions within the single primary paper that anchors it; that paper's own Discussion asserts a
protein-level and nuclear-translocation result its own Western blots contradict; and the review
that propagates the arc proposes no metabolic intervention of any kind and elsewhere states the
opposite therapeutic direction for brain — that *increasing* glycolysis may slow
neurodegeneration.**

---

## 1 · Identifiers established at source, and the glosses checked

| | Paper 2 (registry) | Paper 64 (registry) |
|---|---|---|
| PMID | 36271927 | 35328751 |
| PMCID | PMC9691486 | PMC8955937 |
| DOI | 10.1007/s00109-022-02265-5 | 10.3390/ijms23063326 |
| Title (PubMed) | *WWOX and metabolic regulation in normal and pathological conditions.* | *The[WWOX/HIF1A] Axis Downregulation Alters Glucose Metabolism and Predispose to Metabolic Disorders.* |
| Journal | J Mol Med (Berl) 2022;100(12):1691–1702 | Int J Mol Sci 2022;23(6):3326 |
| Date | 2022-10-22 | 2022-03-19 |
| `article_types` | Journal Article; **Review**; Research Support, Non-U.S. Gov't | **Journal Article** — *no Review tag* |
| Authors | Baryła I, Kośla K, Bednarek AK | Baryła I, Styczeń-Binkowska E, Płuciennik E, Kośla K, Bednarek AK |
| Affiliation | Dept. of Molecular Carcinogenesis, Medical University of Lodz, Poland (all) | Dept. of Molecular Carcinogenesis, Medical University of Lodz, Poland (all) |
| Licence | Copyright "© 2022. The Author(s)."; PubMed returned `license.type: null`, `is_open_access: false` with `checked_sources: ["pubmed"]` only — **the flag carries nothing**; PMC body retrieved and non-empty | **CC BY 4.0**, `is_open_access: true`, `source: pmc` |

### 1.1 Gloss findings

**Finding (gloss 2): accurate.** The registry gloss for PMID 36271927 — *"review: WWOX e metabolic
regulation (comprehensive)"* — matches the paper. It is tagged `Review` and its own closing words
are *"In this review, we have attempted to emphasize what we consider to be important knowledge
about the role of thegene in metabolism."*

**Finding (gloss 64): misdescribes the paper's genre and drops its scope.** The registry gloss
*"WWOX/HIF1A axis downregulation → altered glucose metabolism"* reads as a mechanistic
generalisation. The paper is **primary experimental research**, not a review, and its result is
scoped to one immortalised **human skin fibroblast line, 1BR.3.N**, under four defined
oxygen/glucose conditions. The gloss carries neither the cell system nor the conditions, and the
conditions are exactly where the direction of effect reverses (§4). An unscoped gloss of a scoped
result is precisely the amputation failure mode. **The gloss should not be read as licensing any
claim about tissue other than cultured fibroblasts.**

A second instrument note: PubMed's own title string for 35328751 is itself corrupted —
*"TheAxis Downregulation…"* — because the italicised gene symbols `WWOX/HIF1A` were deleted. The
defect described below for the full-text extractor is present in the metadata record too.

---

## 2 · Genre, and what each paper can therefore support

**PMID 36271927 — review.** MeSH `article_types` carries `Review`; the text self-describes as one.
It is a synthesis with no new experiment. **It cannot be a primary source for any mechanism.** Every
mechanistic statement in it is an assertion about someone else's data, and — per §3 — the citation
targets are unrecoverable from the retrieved artefact.

**PMID 35328751 — primary research, single-system.** `article_types` is `["Journal Article"]` only.
It has Results (§2.1–2.7), Materials and Methods (§4.1–4.15), and generates new data: CRISPR/Cas9
sgRNA silencing and lentiviral cDNA overexpression in 1BR.3.N human skin fibroblasts (ECACC
90020508), cultured under normoxia/hypoxia × normoglycemia/hyperglycemia. It can support a
mechanism **in that system and under those conditions** and nowhere else.

A caution on the word "KO". Methods describe CRISPR/Cas9 sgRNA transduction with puromycin
selection — a selected polyclonal population, not a validated null clone. The paper's own
confirmation section reports *"The relative expression level of WWOX mRNA was three times lower in
1BR.3.NKO variant in comparison to CONTR"* (§2.1) — a roughly 3-fold mRNA knockdown. **This is
knockdown, not knockout**, and residual WWOX is present throughout. The paper uses "KO" and "silencing"
interchangeably. The genotype of interest here is biallelic loss-of-function; a 3-fold knockdown in
a somatic fibroblast line is not that.

---

## 3 · The evidential basis of the HIF1α arc — traced as far as the artefacts permit

**Tracing is structurally blocked, and this is an instrument result, not a finding about the
papers.** The MCP extractor emptied every inline citation marker and dropped both reference lists:

- PMID 36271927: **169** emptied citation markers (`[]`, `[,]`, `[–]`), **0** brackets containing any
  resolvable identifier, no `References` section in the body.
- PMID 35328751: **125** emptied citation markers, **0** resolvable, no `References` section.

**Per the standing rule, no citation target is reconstructed here from position or plausibility.**
What follows is only what the *surviving prose names in words*.

### 3.1 What the review names in prose

The review names its primary sources by author or by model system only four times:

> "The first report indicating the role of WWOX in metabolism was a study that used-knockout (KO)
> mutant mice bred by **Aqeilan et al.**, which suffer from severe metabolic defects that lead to
> growth retardation and postnatal lethality []."  (36271927, Introduction)

> "**KO mice** demonstrated higher levels of serum lactate []. Additionally, **mouse embryonic
> fibroblasts (MEFs)** from KO embryos [] and **muscles of mice with muscle-specific ablation of**[]
> exhibited increases in HIF1α levels and its activity, and the expression of its target genes,
> which encode key glycolytic enzymes, was increased [,]."  (36271927, Participation of WWOX in glucose metabolism)

> "It has been shown in the**[Drosophila]** model that the**[Drosophila]** ortholog plays an important role in
> controlling aerobic metabolism and ROS formation [,]. In this model, functional WWOX interactions
> with isocitrate dehydrogenase (IDH) and superoxide dismutase (SOD) were identified []."  (36271927)

> "**knockdown in the MCF7 breast cancer cell line** led to the upregulation of HIF1α glycolytic
> genes. Additionally, in **breast cancer samples**, WWOX expression negatively correlated with GLUT1
> levels… Furthermore, in a rescue experiment in **MCF7 breast cancer cells**, the upregulation
> ofsuppressed HIF1α target gene expression []."  (36271927)

Plus the authors' own two contributions, identified in the first person:

> "As a result of our observation in pregnancy-associated diabetes, we proposed that thegene can be
> an essential contributor to the pathogenesis of **gestational diabetes mellitus (GDM)** []."  (36271927)

> "**Our further analysis** of the importance of WWOX in glucose metabolism in a **human fibroblast cell
> line** revealed that in normoxic and normoglycemic conditions,deficiency leads to
> increasedmRNA and protein expression."  (36271927) — this is PMID 35328751.

### 3.2 The arc, as far as prose allows

Assembling only what is named in words, the HIF1α/glycolysis arc rests on a countable and narrow set:

1. **Aqeilan's Wwox-null mouse** and its derivatives — serum lactate, MEFs, muscle-specific ablation.
   Named as the founding observation; the review attributes the HIF1α interaction itself to this line of
   work (*"WWOX physically and functionally interacts with HIF1α and coordinates its transactivation
   function in vitro and in vivo []"*).
2. **MCF7 breast cancer cells** plus breast-tumour correlation — the cancer arm.
3. **Drosophila** — the TCA/ROS/respiratory-complex arm.
4. **The Lodz group's own GDM leukocyte study** — human, but observational and in leukocytes.
5. **The Lodz group's own 1BR.3.N fibroblast study** — PMID 35328751, the second paper audited here.

**This is the finding asked for.** Stripped of synthesis, the arc reduces to *one mouse knockout
programme, one breast-cancer cell line, one fly model, one human observational leukocyte study, and
one human skin-fibroblast knockdown.* No item in that list is neural, none is developmental, and two
of the five are the reviewing group's own work. The review that the reasoning layer has leaned on is
not an independent corroboration of the fibroblast paper; **it is the same group summarising the same
group, plus Aqeilan's mice and a breast line.**

The tracing stops here. The emptied brackets mean nothing further can be attributed without
re-acquiring the reference lists by another route.

---

## 4 · Is the metabolic phenotype ever measured in neural tissue, or in development?

**No. Not in either paper. Not once.**

**PMID 35328751:** the roman-type string counts for `brain`, `neuron`, `neural`, `epilep`, `seizure`,
`WOREE`, `SCAR12` and `organoid` are all **zero** in the retrieved body. These are not italicised
tokens, so these zeros *are* informative. The paper's entire experimental content is 1BR.3.N human
skin fibroblasts. The paper says so itself, and says why it chose them:

> "Especially due to the fact that fibroblasts are the most abundant cell type in connective tissue
> and are involved in producing and remodeling the extracellular matrix []."  (35328751, Introduction)

Nothing in this paper reaches brain.

**PMID 36271927:** the review does reach brain, but *never with a metabolic measurement in neural
tissue attributable to WWOX loss.* Everything that reaches brain is one of three things — a
transcriptome correlation, an observation in a diabetic rat/neuroblastoma line, or a statement about
epileptogenic brain in general. In full:

> "In **Goto Kakizaki rats**, which are a spontaneous model of noninsulin-dependent diabetes mellitus,
> an increase in activated WWOX levels was detected in the brain cortex of younger rats, while a
> decrease was observed in older rats []. In the differentiated **human neuroblastoma SH-SY5Y** cell
> line, activated WWOX was observed after 24 h of culture in high glucose []."  (36271927)

That is WWOX responding to glucose, not metabolism responding to WWOX loss — the arrow points the
wrong way for the therapeutic hypothesis.

> "The **principal component analysis (PCA) of global transcriptome data suggested** that WWOX is
> involved in maintaining basic glucose metabolism in undifferentiated **human neural progenitor cells
> (hNPC)** as well as in differentiated neurons []… Thus, disturbed expression ofin nerve cells
> **most likely** leads to disordered metabolic processes."  (36271927)

This is the closest either paper comes to a developmental neural setting. It is a **PCA of
transcriptome data** — gene expression, not flux, not lactate, not oxygen consumption — and the
review's own mood words are *"suggested"* and *"most likely."* No metabolic phenotype is measured.

> "WWOX has been also implicated in epilepsy [,]. It was observed that the **anaerobic glycolysis and
> concentration of lactate in the epileptogenic brain increased in comparison to the control** []. What
> is important, lactate can act as a signal molecule in brain cells and affect neuronal excitation [].
> **The role of WWOX in the control of glucose metabolism in the context of neurological diseases
> requires further research.**"  (36271927, Participation of WWOX in glucose metabolism)

**This passage is load-bearing and it is weaker than it looks.** The glycolysis/lactate observation
is about *epileptogenic brain as such*, not about WWOX-deficient brain: two separate literatures
placed side by side in adjacent sentences. The review does not claim they are joined — it closes the
paragraph by saying the joint question is open. Any reading that treats this as "WWOX loss raises
brain lactate" is reading a juxtaposition as a finding.

The one genuinely neural, genuinely developmental WWOX result the review cites is **not metabolic**:

> "Currently, the specific **neuronal deletion of murine**which generates phenotypes that resemble what
> is observed in **WOREE patients** was characterized by a significant decrease in transcript levels of
> genes involved in **myelination** in the mouse cortex and hippocampus and reduction of myelinated
> axons []."  (36271927, lipid section)

Myelination and lipid handling — not glycolysis, not HIF1α, not lactate.

**Summary for question 3: the arc is muscle, liver, fibroblast, fly and cancer line throughout. The
only neural data in the metabolic arc is a transcriptome PCA. The distance between that and a
developing human brain is not bridged by either paper, and the review says so explicitly.**

---

## 5 · Direction, stated precisely

### 5.1 What the review asserts (unconditional)

> "This clearly indicates that the downregulation ofexpression and especially a lowratio lead to a
> shift toward anaerobic glycolysis. Additionally, glucose uptake is increased, which is probably due
> to increased GLUT1 expression []."  (36271927)

> "Simultaneously, pyruvate dehydrogenase kinase () upregulation was also observed in-knockout cell
> lines and mouse tissues [,]… The upregulation of PDK1 levels blocks glucose influx into the
> tricarboxylic acid (TCA) cycle."  (36271927)

> "WWOX can play a protective role by controlling HIF1α activity, and it makes the influx of glucose
> into mitochondria possible. Therefore, it is able to correct the operation of the Krebs cycle and
> thus prevents the Warburg effect."  (36271927, Conclusions)

So the review's stated direction is: **WWOX loss → HIF1α up → glycolysis up, PDK up, TCA entry
blocked, lactate up, glucose uptake up.**

### 5.2 What the primary paper actually measured — and it is not consistent

PMID 35328751 measured lactate concentration, hexokinase activity, LDH activity, pyruvate
dehydrogenase activity, citrate synthase activity, 2-DG glucose uptake (± insulin), an HRE-luciferase
transactivation reporter, RT-qPCR and Western blot. **No Seahorse, no ECAR, no OCR** — those roman-type
strings are zero in the body and the zeros are informative. `oxygen consumption` appears once, and
only as a statement about somebody else's mouse.

| Readout | Normoxia / normoglycemia | Normoxia / hyperglycemia | Hypoxia / normoglycemia | Hypoxia / hyperglycemia |
|---|---|---|---|---|
| Lactate | ↑ 1.6× (p<0.01) | ↑ (p<0.001) | ↑ (p<0.001) | ↑ 1.3× (p<0.01) |
| Hexokinase activity | ↑ 1.6× (p<0.01) | no change | ↑ (p<0.001) | no change |
| LDH activity | ↑ 1.4× (p<0.01) | ↑ (p<0.01) | no change | no change |
| PDH activity | no change | no change | no change | no change |
| **Citrate synthase** | **no change** | **no change** | **no change** | **no change** |
| Glucose uptake (−insulin) | **↑** | no difference in total | — | **↓ decreased** |
| Glucose uptake (+insulin) | ↑ (p<0.05) | **↓ ~2-fold** | — | no change |

The single readout that holds in all four conditions is **lactate**. Everything else varies, and two
entries reverse sign:

> "We observed thatsilencing **significantly increased glucose uptake in normoxia normoglycemia and
> reduced glucose uptake in hypoxia hyperglycemia** conditions in the absence of insulin."  (35328751, §2.3)

> "in the 1BR.3.NKO cell line we recognized the increase of HIF1α transactivation function in hypoxia
> hyperglycemia condition. Then, we observed the rise of its targets genes… and a **decrease in glucose
> uptake** without changes in insulin-dependent uptake, with a simultaneous increase in lactate
> concentration (). **We found no changes in the activity of the glycolysis enzymes.**"  (35328751, Discussion)

**The oxidative-phosphorylation half of the direction was tested and came back negative.** Citrate
synthase — the paper's chosen mitochondrial marker — did not move in any condition:

> "Contrary to the enhancement of the glycolysis pathway and the increase of lactate as the result, we
> did not observe any consecutive changes in citrate synthase activity in WWOX depleted cells."  (35328751, Discussion)

> "Nonetheless, in our study, citrate synthase expression and activity were tested and **we did not
> observe WWOX influence on it.**"  (35328751, Discussion)

And PDH activity itself never changed. So in the only human-cell primary in the arc, **glycolysis
output rises, but no measured reduction in oxidative/TCA capacity accompanies it.** The "shift away
from OXPHOS" half of the Warburg framing is, in this system, asserted from PDK mRNA and not
demonstrated by any activity measurement.

**Answer to question 4: the direction is consistent for lactate only. Glucose uptake reverses sign
between conditions. Enzyme activities move in normoxia and stop moving in hypoxia. The oxidative
arm was measured and did not change.**

---

## 6 · Does either paper propose or evaluate a metabolic intervention?

**Neither paper proposes, evaluates, or so much as names a ketogenic diet, dichloroacetate,
metformin, or any dietary or pharmacological metabolic intervention.**

Roman-type string counts in the retrieved bodies — all informative zeros, none of these words is
italicised:

| term | 36271927 | 35328751 |
|---|---|---|
| ketogenic / ketone / ketosis | 0 / 0 / 0 | 0 / 0 / 0 |
| dichloroacetate | 0 | 0 |
| metformin | 0 | 0 |
| diet (any form) | **0** | 0 |
| clinical trial | 0 | 0 |

The only therapeutic language present in either paper is unconditioned future-tense aspiration, and
the mood matters:

> "Thorough understanding of the complex mechanisms of action of the WWOX protein will surely provide
> an understanding of many pathologies and **hopefully pave the way for new therapies**. Thus,
> accumulating reports demonstrating the potential role of WWOX in many types of metabolic disorders
> and metabolic rearrangements in cancer **opens the possibility for its therapeutic implementation**
> while also contributing to our understanding on a basic science level."  (36271927, Conclusions)

> "This is one of the first reports of the participation of theaxis and the Warburg effect in the
> pathogenesis of diabetes, therefore **further research is definitely needed**, which could indicate
> the **potential** clinical use of the obtained information. However, **strategies to normalize glucose
> metabolism by targetingmay have promise as therapies in the future.**"  (35328751, Conclusions)

> "For these reasons, **WWOX targeting may prove to be more effective**."  (35328751, Discussion — said of
> antioxidants versus WWOX, in a diabetes/adipokine context, not a neurological one)

Note the target in every case is **WWOX itself or the axis**, in **diabetes**. Not the metabolism, not
the brain. The mood throughout is *hopefully / possibility / may have promise / further research is
definitely needed.*

There is one further statement in the review that runs **against** a ketogenic rationale and must be
recorded:

> "The changes of the glycolysis are seen early in neurodegenerative diseases [], and some authors
> suggest that metabolic disturbances may be a root cause of neuronal loss []… **It has been shown that
> increasing glycolysis may slow neurodegeneration [].**"  (36271927)

The review's only directional therapeutic statement about brain metabolism points toward *more*
glycolysis, not less.

---

## 7 · WWOX and mitochondria specifically

The review makes three mitochondrial statements. All are secondary; two are non-mammalian or
non-neural; the specific respiratory-complex claim is a fly result.

> "A**[Drosophila]** model with a reduction inexpression showed **reduced mitochondrial respiration by
> decreasing the expression of all six mitochondrial respiratory chain genes** (,,,,, and) []. Then, a
> significant percentage of modified flies presented a phenotype with abnormal eye development []…
> These phenotypes indicate that the decreased expression of mitochondrial respiratory complex genes
> leads to significant cellular dysfunction, so affecting mitochondrial function by WWOX deficiency is
> relevant []. **However, the modification of other pathways underlying these developmental defects by
> WWOX cannot be ruled out.**"  (36271927)

The six gene names are deleted by the extractor (italics), so the specific complexes cannot be named
from this artefact. Note the review's own caveat sentence, which is rarely carried forward.

> "Mice with muscle-specific ablation ofare also characterized by **decreases in mitochondrial mass and
> TCA cycle gene expression** (,,,,,, and) []. Since active HIF1α inhibits the Krebs cycle [],
> disruptions of the WWOX–HIF1α interaction are **probably** responsible for the occurrence of this
> phenotype."  (36271927)

Muscle, and the causal attribution is explicitly hedged as *probably*.

> "WWOX can play a protective role by controlling HIF1α activity, and it **makes the influx of glucose
> into mitochondria possible**."  (36271927, Conclusions)

PMID 35328751's mitochondrial content is the citrate-synthase negative already given in §5.2, plus a
second-hand restatement of the same fly and mouse results:

> "The-deficient mice exhibited a reduction in oxygen consumption and amount of the Krebs cycle
> intermediates [], as well as themodel, which showed reduced mitochondrial respiration by decreasing
> expression of any one of the six mitochondrial respiratory complex genes, sodeficiency affect
> mitochondrial function []."  (35328751, Discussion)

**Nothing in either paper addresses WWOX mitochondrial localisation, membrane potential, or
respiratory-complex assembly or activity** in any system. `membrane potential` is a roman-type zero in
both. The respiratory-complex evidence is *transcript level, in Drosophila,* and nothing more.

---

## 8 · Abstract-versus-results / mood check

**There is divergence, it is in the primary paper, and it is material.** This is not a
"no-divergence" report.

### 8.1 PMID 35328751 — Discussion contradicts its own Western blot

The Discussion opens its own-results paragraph with:

> "We determined that **knock-out ofleads to increasedmRNA and protein level together with its
> translocation to the nucleus** and raise of its transactivation function."  (35328751, Discussion)

The Results section reports the opposite on both counts:

> "Compared with controls, the expression of **HIF1α protein was significantly decreased** in 1BR.3.NKO
> in comparison to CONTR in normoxia normoglycemia (2-fold; < 0.01) and hypoxia normoglycemia (nearly
> 2-fold; < 0.001) in cytoplasm fraction. **We didn't observed WWOX influence on HIF1α protein in
> nuclear fraction.**"  (35328751, §2.6.1)

So: in the fractionated Western blot, cytoplasmic HIF1α protein went **down**, not up, in two of four
conditions, and nuclear HIF1α was **unchanged in all four.** "Translocation to the nucleus" is the one
thing the blot was positioned to detect, and the blot did not detect it.

The only assay that showed a HIF1α protein increase was immunocytochemistry of *total intracellular
content*, and only in normoxia:

> "downregulation resulted in HIF1α increase in normoxia normoglycemia and hyperglycemia condition
> (both < 0.01). **It was not found statistically significant WWOX reduction influence on total
> intracellular content of HIF1α protein in hypoxia normo- and hyperglycemia condition** ()."  (35328751, §2.7)

The transactivation reporter is the robust positive (HRE-luciferase up in KO, down in overexpression,
across conditions). **The transactivation result stands. The protein-level and nuclear-translocation
claims do not, by the paper's own blots.**

### 8.2 PMID 36271927 — the review propagates the Discussion, not the Results

The review, describing this very paper, writes:

> "Our further analysis… in a human fibroblast cell line revealed that in normoxic and normoglycemic
> conditions,deficiency leads to increasedmRNA and protein expression. **Additionally, it increases the
> translocation of HIF1A to the nucleus** and amplifies its transactivation function []."  (36271927)

This reproduces the contradicted sentence. **A claim its own primary left unsupported — indeed
measured and failed to find — is restated in a review as established.** That is the named failure mode,
committed by the same authors across their own two papers, seven months apart.

### 8.3 A second, softer instance in the review

> "The consequence ofdownregulation was the transcriptional upregulation of the glycolytic phenotype
> in leukocytes of patients with GDM []."  (36271927)

The review's own account of that study is correlational — *"the expression of2,,, andcorrelated
with, but only in the GDM patient group"* — and "consequence" is a causal word applied to a
correlation in patient leukocytes. The paper supplies its own counter-evidence in the next breath:
*"We did not observe differences inexpression between the tested groups."*

### 8.4 One place where the review is *more* careful than expected

To be fair to it: the review does not overstate the neural case. It ends that paragraph with *"The
role of WWOX in the control of glucose metabolism in the context of neurological diseases requires
further research"* and flags the fly caveat (*"cannot be ruled out"*). The overstatement is
concentrated in the HIF1α protein/translocation claim, not distributed through the review.

---

## 9 · Independence

**Both papers are from the same laboratory, and it is neither Chang's nor Aqeilan's.**

Every author on both papers lists a single affiliation: **Department of Molecular Carcinogenesis,
Medical University of Lodz, Poland.** Izabela Baryła, Katarzyna Kośla and Andrzej K. Bednarek appear
on both; Ewa Styczeń-Binkowska and Elżbieta Płuciennik appear on the IJMS paper. Bednarek is the
senior author of both.

So:

- **Independent of Chang Nan-Shan (NCKU)?** Yes.
- **Independent of Aqeilan (HUJI)?** Yes — and the review explicitly attributes the founding mouse
  work to Aqeilan as an external source (*"mutant mice bred by Aqeilan et al."*), while the IJMS paper
  benchmarks its results against Aqeilan's MEF data as an outside comparator.

**But the two papers are not independent of each other, and this is the point.** The review is by a
subset of the IJMS authors, published seven months later, and it cites the IJMS paper as *"Our further
analysis."* Two of the five named strands of the arc (§3.2) are this same group's own work. Holding
these as two corroborating entries in the reasoning layer overstates the support: **they are one
laboratory's primary result plus that same laboratory's review of it, sitting on top of Aqeilan's
mouse programme and an MCF7 line.** A third laboratory is present in the arc essentially only as
Aqeilan's mice.

A methodological caution: the surname "Chang" appears zero times as a standalone word in either body
(18 hits for "changes", 3 for "change", 1 for "changed"), and "Aqeilan" appears once and three times.
**These counts cannot establish citation independence**, because both reference lists were destroyed by
the extractor — a laboratory can be cited heavily by number without being named in prose.
Independence above is established from **affiliations**, which are intact, not from name counts.

---

## 10 · What the ketogenic and dichloroacetate hypotheses may now assume — and what remains unmeasured

Nothing in this section is medical advice. No statement here is a recommendation about any diet or
drug. This is an inventory of what the read papers do and do not measure.

### 10.1 What these two papers license

**Supported at the level of a measured result, in the stated system only:**

- WWOX knockdown in human skin fibroblasts raises the HIF1α HRE-transactivation reporter, and WWOX
  overexpression lowers it, across normoxia and hypoxia. This is the arc's most robust single
  observation and it is directly measured.
- WWOX knockdown in those fibroblasts raises extracellular lactate in all four oxygen/glucose
  conditions tested. Lactate is the only readout that holds throughout.
- WWOX knockdown raises hexokinase and LDH activity **in some conditions** and not others.
- Aqeilan's Wwox-null mice show raised serum lactate; muscle-specific ablation shows raised HIF1α
  targets and reduced mitochondrial mass. Named in prose, not traceable to a citation from these
  artefacts.

**Therefore the shared premise of the KD and DCA hypotheses — that WWOX loss produces a
glycolysis-shifted, lactate-elevated state — is supported, at HYPOTHESIS strength, for fibroblasts,
muscle and cancer lines.**

### 10.2 What the hypotheses may NOT assume

1. **That WWOX loss suppresses oxidative phosphorylation in any human cell.** It was measured in the
   one human primary and it did not. Citrate synthase activity and expression were unchanged in all
   four conditions; PDH activity was unchanged in all four. The "away from OXPHOS" half of the
   Warburg framing rests, in human cells, on **PDK transcript** alone. **A DCA rationale targets PDK to
   restore PDH flux; the only human measurement of PDH activity in this arc found PDH activity
   unaltered by WWOX loss.** That is a direct, measured gap under the DCA hypothesis, not a
   speculative one.
2. **That any of this has been observed in neural tissue.** It has not. The complete neural metabolic
   content of both papers is one transcriptome PCA in hNPCs and neurons, which measures expression,
   not flux, and which the review reports with *"suggested"* and *"most likely."*
3. **That any of this has been observed in a developmental setting.** It has not. The fibroblast
   experiments run 6 h or 48 h in a post-mitotic-tissue-derived adult cell line. The one neuronal
   WWOX-deletion mouse the review cites was characterised for **myelination**, not for glycolysis.
4. **That elevated brain lactate in WWOX loss has been demonstrated.** It has not. The review places a
   general statement about epileptogenic brain next to a general statement about lactate and neuronal
   excitation, and then explicitly says the WWOX-specific question is open.
5. **That either paper endorses a metabolic intervention.** Neither names one. "Ketogenic",
   "dichloroacetate", "metformin" and "diet" are all zero in both bodies, and these are informative
   zeros.
6. **That HIF1α protein is stabilised or nuclear-translocated by WWOX loss in human cells.** The
   fractionated blot in the only human primary found cytoplasmic HIF1α *decreased* and nuclear HIF1α
   *unchanged*. Only the transactivation reporter and a total-content ICC support the arc at protein
   level, and the ICC is null under hypoxia.
7. **That a 3-fold knockdown models biallelic germline loss.** It does not, and the paper's own
   §2.1 numbers show what was achieved.

### 10.3 The specific distance that is not bridged

The therapeutic hypotheses require a chain: *WWOX loss → HIF1α-driven glycolytic shift → pathogenic
metabolic state in developing neurons → correctable by shifting substrate or unblocking PDH.* These
two papers supply evidence for link 1→2 **in adult fibroblasts, mouse muscle and cancer lines**. They
supply no measurement whatever for link 2→3, and the one directional statement the review makes about
brain metabolism points the other way (*"increasing glycolysis may slow neurodegeneration"*).

A cancer cell line and an immortalised adult fibroblast are chosen precisely for proliferation under
glycolytic conditions; a developing cortical neuron is not, and its substrate economy, its
astrocyte–neuron lactate exchange, and its developmental HIF1α biology are none of them addressed
here. **The WWOX-specific rationale for a metabolic intervention in this genotype remains, after
reading both papers, an extrapolation across cell type, developmental stage and species — not a
finding.**

### 10.4 What would close the gap (unmeasured, and identified as such)

None of these are proposed as actions; they are named to mark what is absent from the evidence base.

- Any flux measurement (OCR/ECAR, lactate, glucose) in **WWOX-deficient neurons, neural progenitors or
  brain organoids**. Zero such measurement exists in either paper.
- **PDH activity and PDK protein in WWOX-deficient neural tissue** — the DCA hypothesis's direct
  premise, currently unmeasured anywhere in neural tissue and measured-and-null in fibroblasts.
- **In vivo brain lactate** in a WWOX-loss model.
- Whether the HIF1α transactivation effect — the arc's strongest measurement — is present at all in
  post-mitotic neurons, where HIF1α biology differs from that of a proliferating fibroblast.
- Reacquisition of both **reference lists**, so that §3's tracing can be completed rather than stopped.

---

## 11 · Closing declarations

**Author:** Scientist A.
**Date:** 2026-09-21.
**Mode:** READ-ONLY. **No canonical file was modified.** No registry, queue, ledger or current file was
edited. No commit candidate was produced. No git command was run.

**Artefacts written** (full-text bodies only, verbatim, unmodified, untruncated; abstracts excluded from
the artefacts by design):

- `files/fulltext/PMID36271927_PMC_MCPtext.txt` — 32,310 bytes —
  `sha256 d4edaaeed9525efa84e5151dd9c8c46fe6edbdac8a3ee2f072af5e0fa836926d`
- `files/fulltext/PMID35328751_PMC_MCPtext.txt` — 49,311 bytes —
  `sha256 d06eda93653548ab8c4188ca6dcfd9f3dbe917a384ff2090a19a7c7cc038caca`

**Declared limits:**

1. **No figure was inspected.** No figure image is retrievable. Per D-14, no negative asserted only by
   a figure is adjudicated here. Several Results sentences in PMID 35328751 end in an empty
   parenthesis `()` where a figure cross-reference was deleted; the quantitative claims quoted above
   are taken only from prose that carries its own numbers.
2. **Extraction defect, PMID 36271927:** all italicised tokens deleted — every instance of the gene
   symbols *WWOX* / *Wwox* / *WWOX*-related italics, *Drosophila*, *in vitro* / *in vivo*, the italic *P*
   in p-values, and all italicised gene names in enumerated lists (which is why six respiratory-chain
   genes and seven TCA genes appear as `(,,,,, and)`). **169 citation markers emptied; 0 resolvable; no
   reference list.** Figure legends did not survive.
3. **Extraction defect, PMID 35328751:** same class of defect, and additionally the italic *p* of
   p-values is deleted, leaving `(< 0.05)` — the significance values quoted above are reproduced as the
   extractor rendered them. **125 citation markers emptied; 0 resolvable; no reference list.** Section 5
   (Conclusions) heading survived but its body was displaced; the conclusion text quoted in §6 is taken
   from the end of the retrieved body. Tables did not survive; the table in §5.2 above was assembled
   from prose only. **PubMed's own title field for this paper is also corrupted by the same italic
   deletion** (`"TheAxis Downregulation…"`).
4. **Reference lists: neither survived.** Citation tracing in §3 is limited to sources named in prose.
   No citation target was reconstructed from position or plausibility.
5. **String-count classes.** All zeros reported for *ketogenic, ketone, ketosis, dichloroacetate,
   metformin, diet, Seahorse, OCR, ECAR, extracellular acidification, membrane potential, brain,
   neuron, neural, epilep, seizure, WOREE, SCAR12, organoid, clinical trial* are **roman-type** and are
   offered as informative. **No zero for any italicised token (gene symbols, species names,
   in vitro/in vivo) is offered anywhere in this document as evidence.** Independence in §9 is
   established from author affiliations, not from surname counts.
6. **Licence, PMID 36271927:** copyright "© 2022. The Author(s)."; PubMed returned no licence type and
   `is_open_access: false` with `checked_sources: ["pubmed"]` only — PMC was not consulted by that
   call, so the flag is uninformative. The PMC body was retrieved and is non-empty. Reuse terms beyond
   author copyright are not established by the retrieved metadata.
7. **Licence, PMID 35328751:** **CC BY 4.0** (`https://creativecommons.org/licenses/by/4.0/`), open
   access confirmed from PMC.
8. **Nothing in this document is medical advice.** No dietary or pharmacological statement here is
   phrased as, or is to be read as, a recommendation. Any therapeutic reasoning in this model supports
   discussion with a treating clinical team and never substitutes for one.
