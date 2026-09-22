# Adelaide (Richards / O'Keefe) node — discriminator read

**Date:** 2026-09-21 · **Actor:** Scientist A · **Branch:** `claude/legend-autonomous-woree-tv6gz8`
**Mode:** READ-AND-REPORT. **READ-ONLY toward every canonical file.** No registry edited, no
BATCH_COMMIT, no commit candidate, no receipt recorded. One output file, this one.

**Decision question.** *Does the Adelaide (Richards / O'Keefe) Drosophila + metabolism node give
WOREE a therapeutic lever or a practical drug-repurposing screening platform that LEGEND does not
already have?*

**Sources read in full this session** (PubMed / PMC open-access subset, via
`mcp__PubMed__get_full_text_article`):

| PMID | PMCID | Body retrieved | DOI |
|---|---|---|---|
| 26302329 | PMC4547717 | **37,561 chars** — complete, Introduction→Supporting Information | [10.1371/journal.pone.0136356](https://doi.org/10.1371/journal.pone.0136356) |
| 34210081 | PMC8305172 | **26,370 chars** — complete, §1→§5.2 | [10.3390/cells10071637](https://doi.org/10.3390/cells10071637) |

Neither body came back empty. Abstracts of the two **unobtainable** Adelaide primaries
(`26390919`, `23765596`) were additionally retrieved via `get_article_metadata` and are used
**only** to cross-check the review's characterisation of them; they are labelled as abstracts
throughout and are **not** reads.

---

## STEP 0 — ledger check, performed before reading

| Check | Result |
|---|---|
| `registry_records.py get --pmid 26302329 --hops 1` | **Known.** `CORPUS P270` / `LIT-0270`, Tier **C**, status *screened — corpus placeholder*, primary pathway *P5 — metabolism / mitochondria / redox*, clinical relevance **LOW**, **claim links: none — triage only**, next action *background-only; escalate only on convergence signal* |
| `registry_records.py get --pmid 34210081 --hops 1` | **Known.** `CORPUS-STUB-019`, status *not_processed*, *corpus placeholder only*, **claim links: none** |
| `reading_state.py` | **123 papers, 186 receipts. Neither 26302329 nor 34210081 carries a receipt.** Neither 26390919 nor 23765596 carries one either |
| `next_scientist_scout_20260921.md` §1a, §3 | Node already **DEMOTED on acquisition, not on merit**; this read is wave item #2 and #3, designed as *"the decisive cheap test of the standing baseline candidate"* |
| `AUTONOMOUS_SESSION_STATE.md` | `DL-MECH-021` already **lowered medio → basso**; domain-sufficiency arc already **demoted to author assertion**; seizure bridge already withdrawn. Accessible reading queue **empty**; `UNREAD_PREMISE` ratchet at **0** |

> Both papers are genuinely unread and neither currently carries a claim. Nothing in this file
> re-litigates a settled item: the scout demoted the node on *acquisition*; this file settles it
> on **evidence**.

---

## 1 · VERDICT

> ### **NO.**
> **The Adelaide node gives WOREE neither a therapeutic lever nor a practical screening platform,
> and the single fact that decides it is the review's own statement that the fly carries no
> baseline phenotype to rescue —** *"deficiency indisplays no phenotypic consequences"* **— so
> every Adelaide readout is a modifier assay in a sensitised oncogenic or mitochondrial
> background, and in both readable assays the sign runs backwards for WOREE: WWOX *promotes*
> cell death, and losing it is *protective*.**

**The one non-null deliverable, and it is not a lever.** Traced through the review to an
unobtainable primary (`26390919`), the node holds a **construct-scope constraint**: suppression of
a mitochondrial-deficiency phenotype by raising WWOX **requires the SDR catalytic active site**
(Y288F abolishes it). That bears on `TX-007` (does an AAV construct need catalytically competent
WWOX?) and on `TX-003` (is stabilising an SDR missense the right target?). It is held
**second-hand, in a review, with no receipt** — the exact failure mode the Chang chain exposed —
and it is a **necessity** result, **not** the domain-**sufficiency** result `DL-MECH-021` wants.

---

## 2 · Per-paper sections

### 2a · PMID 26302329 — O'Keefe LV et al., *PLoS One* 2015;10(8):e0136356

**What was actually done.**

| Axis | What the paper reports |
|---|---|
| Organism / stage | *Drosophila melanogaster*. Wandering / late **third-instar larval** imaginal discs (eye, wing); **adult** eyes; adults 0–1 day old for Western. **No embryonic stage, no CNS, no adult behaviour.** |
| Gene manipulated | The **fly WWOX ortholog** (antibody is *anti-C-DmWWOX*). Gene-symbol tokens are elided by the extractor throughout — see §6 |
| Direction | **BOTH.** *Loss-of-function*: three independent RNAi lines (VDRC v9152, v22536, v108350), heterozygous **null** allele, heterozygous **insertion** allele, and **trans-heterozygous** for independent alleles = *"WWOX function is completely removed"*. *Gain-of-function*: UAS-WWOX **cDNA** and UAS-WWOX **ORF** |
| Tissue / driver | Eye disc posterior to the morphogenetic furrow (GMR-GAL4, name elided → **inferred**); posterior wing-disc compartment (an *engrailed*-class driver, name elided → **inferred**) |
| Sensitising insults | (i) low-level ectopic **Egr/TNFα**; (ii) **p53**; (iii) **Hid**; (iv) MARCM mitotic clones of the polarity gene *scribbled* |
| Readouts | Adult eye area (ImageJ), ommatidial patterning, necrotic-lesion size class, cleaved **Caspase 3** area fraction, **CellRox** ROS, GFP clone area fraction, **Elav** (photoreceptor differentiation), adult eclosion viability, Western vs β-tubulin |
| n | **10 eyes per genotype**, hand-traced. **Minimum n = 20 eye discs per genotype** for clonal analysis. **30 female flies per Western sample** |

**What was found.**

1. **WWOX is pro-apoptotic and rate-limiting for Egr/TNFα-induced death.** RNAi knockdown
   *suppressed* the Egr/TNFα rough-eye phenotype (bigger, better-patterned eyes); overexpression
   *enhanced* it. Mirrored in the wing disc as **decreased** Caspase 3 area on WWOX knockdown and
   **increased** Caspase 3 area on WWOX overexpression.
2. **Specificity.** No modification of **p53** or **Hid** eye phenotypes by altered WWOX, in either
   direction.
3. **WWOX alone does nothing.** Overexpression of WWOX by itself produced **no** eye phenotype.
4. **Cell competition.** Reducing WWOX inside *scrib* tumorigenic clones increased their persistence
   (clone area up, whole-disc area unchanged) and cut adult viability from **74.1% → 31.9%** of
   expected (p = 0.0016). The same held when WWOX was reduced or completely removed animal-wide.
5. **Localisation.** Ectopic WWOX stayed **cytoplasmic** under Egr/TNFα — no nuclear relocation
   detected, contrary to the mammalian literature the paper cites.

**What was NOT tested — and this is the operative half.**

- **No neural, neuronal, glial or CNS readout of any kind.** `neuro`, `brain`, `neuron`, `glia`,
  `myelin`, `seizure`, `epilep` return **zero** in the body. These are ordinary English words, not
  italicised gene tokens, so this count is admissible. **Elav** appears, but solely as a
  differentiation marker scoring *"absence of differentiated photoreceptors"* inside tumour clones
  in an epithelial disc — a cell-fate stain in an oncology assay, **not** a nervous-system readout.
- **No domain-level construct.** No WW-only, no SDR-only, no catalytic-dead allele. Only full-length
  cDNA and full-length ORF. **The paper contributes nothing to the domain-sufficiency question.**
- **No drug, no diet, no compound, no dose.** `drug` and `screen` return **zero**.
- **No rescue of a WWOX-loss phenotype by anything.** SOD1 and SOD2 overexpression suppress the
  **Egr/TNFα** eye phenotype — a *different* phenotype. SOD was never crossed to a WWOX-loss animal.
- **No metabolic measurement in this paper.** No respirometry, no ATP, no lactate, no glycolytic
  flux. The word "metabolism" appears only as background and in the hypothesis.
- **ROS was never measured in a WWOX-altered animal here.** CellRox was applied only to Egr/TNFα
  discs and controls. The WWOX↔ROS arm of the paper's own model (Fig 7) is **imported by citation**
  from `21075834` (already read by LEGEND), not measured in this study.

**Results-first check — two mood/attribution findings, no inversion.**

- The abstract's *"WWOX does have an integral role in metabolism"* has **no Results counterpart in
  this paper**. It is a background assertion carried into the abstract. Not an inversion, but a
  claim that would be mis-sourced if taken from the abstract.
- The abstract's ROS→metabolism link is explicitly **hypothesised**, and the paper says so:
  *"We now hypothesise that…"*. Mood preserved: this is a hypothesis, not a finding.
- The abstract's closing *"provides novel possibilities for the development of therapeutic
  approaches"* is an aspiration with **no therapeutic experiment anywhere in the paper**.

**Is the assay scalable? No — measured, not assumed.**

Throughput actually demonstrated: **10 hand-traced eyes** and **≥20 hand-dissected discs** per
genotype, across roughly a dozen genotypes, scored in ImageJ. Further, the clonal analysis carries
a **differential exclusion**: *"Significant disruption to eye disc morphology was observed in 13/52
pairs of the [scrib] clones and 31/50 pairs [scrib; WWOX-RNAi] clones and these were not included
in these analyses"* — **25% vs 62%**, and the discarded discs are the most severely affected ones,
i.e. exclusion is *correlated with the genotype and with the effect direction*. The surviving
"mild but significant" clone-area difference was measured on the less-affected remainder. This is
low-throughput modifier genetics with a genotype-correlated exclusion rule, not a screening deck.

---

### 2b · PMID 34210081 — Lee CS et al., *Cells* 2021;10(7):1637 — **REVIEW, treated as review**

**Everything below is an author assertion until traced to the experiment.** The review contains no
new data. Its value here is exactly what the scout commissioned it for: what the two Adelaide
primaries LEGEND cannot open actually claim, in the same laboratory's own words.

**On `26390919` — "WWOX moderates the mitochondrial respiratory complex" (review §3, ¶6).** The
review reports: altered WWOX modulates cellular-outgrowth phenotypes caused by **mitochondrial
respiratory-complex deficiencies**; reduced WWOX **worsens** them; raising WWOX **suppresses** them;
and the suppression **requires the SDR catalytic active site**, with **Y288F** abolishing function
(fly Y288 ≡ **human Y293**). Cross-checked against the primary's own PubMed abstract, which says
*"This modulation requires the enzyme active site of WWOX"* and adds that the outgrowths are
*"mediated by reactive oxygen species, dependent upon the Akt pathway and sensitive to levels of
autophagy and hypoxia-inducible factor."* **The review and the abstract agree.**

🔴 **Note the direction.** This is the **only** Adelaide assay whose sign is WOREE-congruent (less
WWOX = worse). But the phenotype being suppressed is a **mitochondrial-deficiency** phenotype, not a
WWOX-loss phenotype: the experiment asks what WWOX does *for* damaged mitochondria, not what rescues
a WWOX-deficient animal. And the readouts — *"loss of tissue, cellular outgrowths and presence of
ectopic structures"* — are imaginal-tissue oncology endpoints.

**On `23765596` — "metabolic reprograming in cells" (review §3, ¶4).** The review reports that in
human HEK cells WWOX is *"both a regulator of metabolism and is regulated by metabolism"*: forcing
**oxidative phosphorylation raises** WWOX transcript, **hypoxia/glycolysis lowers** it. The primary's
abstract concurs and specifies the manipulation as a glycolysis→OXPHOS switch in **HEK293** cells
with **galactose**, and the measurement as **transcript** level. *(Minor fidelity flag: the review
writes "HEK392T"; the primary's MeSH term is "HEK293 Cells". A typo, recorded, not load-bearing.)*

**Domain sufficiency — the direct answer: NO.**
The review states catalytic-site **necessity**, never domain **sufficiency**. It says the active
site is *required for the suppression* and that Y288F *abolishes* function. **It nowhere states
that the ADH/SDR domain alone rescues anything, in any organism.** `DL-MECH-021`'s
domain-sufficiency arc gains **no** support here, in any species. The nearest adjacent statement is
about a *segment*, not a domain, and it is a human-genetics inference rather than a rescue
experiment: the **G372R** SCAR12 allele in the C-terminal substrate-specificity region *"indicates
that this highly conserved C-terminal segment is vital for [WWOX] function, having the same clinical
consequences as that of the P47T mutation located in the first WW domain"* — i.e. two different
domains, same clinical outcome, which argues **against** any single domain being sufficient.

**Protein stability / folding / degradation / abundance for missense variants — the direct answer:
NOTHING.** All six occurrences of `stabil*` in the review are **"DNA instability"**; `misfold`,
`proteasome`, `chaperone`, `missense` and `variant` return **zero**; the single `degrad*` hit is a
generic statement that *"Proteins containing PEST domains are rapidly degraded"*, about wild-type
WWOX, not about any variant. The two `abundanc*` hits concern a **metabolite**, not protein. **The
review makes no statement whatever about missense-variant WWOX protein stability, folding,
degradation or abundance.** This is a clean negative and it is recorded as one.

**What the review does contain that is therapeutically shaped — all of it speculative, and the
authors mark it so.** Three proposals, none with an experiment behind it:
(i) fly compensation for WWOX loss implies WOREE-class pathology *"is likely to be treatable, with
identification and targeting of the compensating pathway(s)"*; (ii) reduce the abundance of the
metabolite that accumulates behind the stalled enzyme; (iii) activate compensatory pathways. **All
three are blocked on the same unknown**, stated in the review's own first line of §3: *"the
substrate and product of the enzyme reaction that it catalyses are yet to be discovered."*

---

## 3 · VERBATIM LOCATORS

Every quote below was copied character-for-character from the retrieved body text and
programmatically re-matched against it. **Gene symbols, species names and all citation numbers are
elided by the extractor** — this is why several quotes read as run-together words (*"deficiency
indisplays"*) and why **no quote can carry its citation number**: the review's citation markers
render as empty `[]`, `[,]`, `[–]` throughout. See §6.

| # | Proposition | Exact quote | Section anchor |
|---|---|---|---|
| L1 | 🔴 **Decisive.** The fly has no baseline WWOX-loss phenotype, so there is nothing for a compound to rescue | `deficiency indisplays no phenotypic consequences [] and, therefore, might be considered a poor model for those species (including humans) for whichis necessary.` | 34210081 · §3 *WWOX in Metabolism*, ¶1 |
| L2 | The node's treatability claim is an inference from fly compensation, not a result | `On the contrary, the ability ofto compensate for the lack ofindicates that pathology caused by deficiency ofis likely to be treatable, with identification and targeting of the compensating pathway(s).` | 34210081 · §3, ¶1 |
| L3 | 🔴 The one deliverable: SDR **catalytic-site necessity** (not domain sufficiency), second-hand | `Conversely, the tissue disruption phenotypes were suppressed by increasinglevels, with the SDR enzymatic active site required for the suppression. Amino acid Y288 inis an essential component of the catalytic active site in the SDR region, with Y288F mutation abolishing its function []` | 34210081 · §3, ¶6 (reporting `26390919`) |
| L4 | Every therapeutic proposal in the node is blocked on an unidentified substrate/product | `Despite more than twenty years of research on theprotein, the substrate and product of the enzyme reaction that it catalyses are yet to be discovered.` | 34210081 · §3, ¶1 (opening sentence) |
| L5 | The downstream-metabolite lever is a blueprint with an unknown target | `The identity of this metabolite, together with targeted methods to reduce its abundance, represent a plausible target for treating metabolic dysfunction due to perturbation of.` | 34210081 · §5.2, final ¶ |
| L6 | The compensatory-pathway lever is conditional and untested | `Alternatively, if the product(s) ofact as negative regulators or rate-limiting determinants of a metabolic process, then the activation of compensatory pathways such as those acting in[] may provide a means of reducing the clinical impact ofdeficiency.` | 34210081 · §5.2, final sentence |
| L7 | Two different domains, same clinical outcome — argues against single-domain sufficiency | `The G372R mutation located within the putative substrate specificity region indicates that this highly conserved C-terminal segment is vital forfunction, having the same clinical consequences as that of the P47T mutation located in the first WW domain of[].` | 34210081 · §5.2 *What Does WWOX the Enzyme Normally Do?* |
| L8 | 🔴 Sign inversion: in the fly, **losing** WWOX is protective | `Decreased WWOX activity together with ectopic expression of Egr/TNFα in the posterior portion of the disc resulted in a decrease in the relative area of Caspase 3 staining (). Conversely, increased WWOX expression increased the relative area of Caspase 3 staining ().` | 26302329 · Results, *WWOX modifies Caspase 3 staining in response to ectopic Egr/TNFα* |
| L9 | No WWOX-alone phenotype in the fly eye either — nothing to screen against | `Ectopic expression of WWOX alone does not result in any obvious cell death-induced phenotype in the biological context of the.eye ().` | 26302329 · Results, *Altered WWOX modulates ectopic Egr/TNFα eye phenotypes* |
| L10 | Throughput actually demonstrated for the adult-eye readout: ten hand-traced eyes | `For determination of adult eye sizes the outline of ten different randomly selected eye photos were traced using ImageJ and total area (in pixels) for each image was measured.` | 26302329 · Materials and Methods, *Analyses of Adult Eyes* |
| L11 | 🔴 Genotype-correlated exclusion in the clonal assay (25% vs 62%), removing the worst discs | `GFP indicative of clones and a minimum n = 20 eye discs were analysed per genotype). Significant disruption to eye disc morphology was observed in 13/52 pairs of theclones and 31/50 pairs;clones and these were not included in these analyses.` | 26302329 · Materials and Methods, *Clonal analyses* |
| L12 | The whole-animal endpoint the node would front a screen with — viability, n at the cross level | `showing a survival rate of 31.9% of that expected compared to 74.1% for flies with themutant clones alone (**p = 0.0016)` | 26302329 · Results, *Requirement for WWOX tumor suppressor activity* |
| L13 | Localisation negative, mood preserved as "no evidence", not "absent" | `Thus there was no evidencefor nuclear localisation of detectable levels of ectopic WWOX in response to Egr/TNFα expression in eye or wing imaginal discs.` | 26302329 · Results, *WWOX remains cytoplasmically localised…* |
| L14 | The node's own therapeutic framing is aspirational and directed at cancer, not deficiency | `Understanding the conserved cellular pathways to which WWOX contributes provides novel possibilities for the development of therapeutic approaches to restore WWOX function in cancer.` | 26302329 · **Abstract**, final sentence (abstract field, not body) |
| L15 | The metabolic-reprogramming claim, in the review's words: transcript level, human cells | `Under hypoxic conditions where metabolism is steered towards glycolysis, the expression oftranscript is markedly decreased, whereas a switch to oxidative phosphorylation has the opposite effect.` | 34210081 · §3, ¶4 (reporting `23765596`) |

---

## 4 · NEGATIVE RESULTS — what this node cannot do

Preserved explicitly. Each is a claim, not an absence of one.

| # | Negative | Basis | Strength |
|---|---|---|---|
| N1 | **No nervous-system readout exists anywhere in the node's one readable primary.** No brain, no CNS, no neuron, no glia, no behaviour, no excitability | 26302329 read end-to-end; Elav used only as a photoreceptor-differentiation stain inside tumour clones | **Strong** — rests on the read, not on a string count |
| N2 | **No domain-level construct in 26302329**, and **no domain-sufficiency statement in 34210081** for any organism | Full read of both | **Strong** |
| N3 | **`DL-MECH-021` gains nothing.** The zebrafish SDR-alone-rescue arc is neither corroborated nor contradicted here; the review's only domain statement (L3) is **necessity**, and L7 cuts against sufficiency | §5.2 and §3 of the review | **Strong** |
| N4 | **No compound, diet, dose or drug anywhere in either paper.** The node has never dosed anything | Both reads | **Strong** |
| N5 | **Nothing has ever rescued a WWOX-loss phenotype in the fly** — because per L1 there is no WWOX-loss phenotype to rescue. SOD1/SOD2 rescue the **Egr/TNFα** phenotype and were never crossed into a WWOX-loss animal | 26302329 Results + Methods | **Strong** |
| N6 | **The review says nothing about missense-variant protein stability, folding, degradation or abundance.** All `stabil*` hits are "DNA instability" | Full read + term audit on non-italic English words | **Strong** |
| N7 | **No metabolic measurement in 26302329.** The node's metabolic authority rests on `21075834` (already read) and on two papers LEGEND cannot open | 26302329 read | **Strong** |
| N8 | **WWOX↔ROS was not measured in 26302329**; it is imported by citation from `21075834` | Results + Methods; CellRox applied only to Egr/TNFα discs | **Strong** |
| N9 | **The demonstrated throughput is ~10 eyes / ~20 discs per genotype, hand-scored**, with a genotype-correlated 25%-vs-62% exclusion. Not screening throughput | L10, L11 | **Strong** |
| N10 | **No WWOX effect on p53- or Hid-driven death**, in either direction — a genuine in-paper negative the authors report and that narrows the mammalian p53 literature | 26302329 Results + S2 Fig | **Strong** — a clean primary negative |
| N11 | ⚠️ **Not established either way:** whether a fly WWOX null has *any* phenotype under a **neural or metabolic stress** that nobody applied. L1 is "no phenotypic consequences" **as tested**. Do not convert to "the fly null is normal" | L1, mood preserved | **Boundary — `PREMISE: NOBODY_LOOKED`** |

---

## 5 · Therapeutic classification

Exactly one label per intervention-like item. Nothing here was dosed in an animal.

| Item | Source | Classification |
|---|---|---|
| **SOD1 / SOD2 overexpression** suppressing the Egr/TNFα eye phenotype | 26302329, **in-paper** | **MECHANISTIC PROBE ONLY** — rescues a TNFα phenotype, never crossed into WWOX loss |
| **RNAi knockdown of WWOX** suppressing Egr/TNFα death and promoting tumour-clone survival | 26302329, **in-paper** | **NOT TRANSFERABLE TO WOREE** — this is the disease state acting as the "therapy". Sign is inverted. It also adds a **fourth** independent line to the standing category objection: every lever this literature produces acts by *removing* WWOX |
| **Raising WWOX** to suppress mitochondrial-deficiency outgrowths, SDR active site required | `26390919`, **second-hand via review — no receipt** | **MECHANISTIC PROBE ONLY** — the fly analogue of restoration, but the phenotype rescued is a *mito-deficiency* phenotype, not a WWOX-loss one. Becomes a genuine constraint on **WWOX RESTORATION** design (`TX-007` construct scope) only if the primary is obtained |
| **Akt pathway / autophagy / HIF** as modifiers of the outgrowth phenotype | `26390919` **abstract only** | **DOWNSTREAM/WWOX-INDEPENDENT** — druggable nodes in principle, but they modify the *mitochondrial* phenotype, not WWOX loss. Not transferable as read |
| **Galactose / forced OXPHOS raising WWOX transcript** in HEK293 | `23765596`, **second-hand via review — no receipt** | **UPSTREAM/WWOX-DEPENDENT** — the nearest thing in the node to a lever, and its entire benefit is contingent on the upregulated allele encoding functional protein. **Transcript measured; protein not reported** |
| **"Reduce the abundance of the accumulating metabolite"** | 34210081 §5.2 — author speculation | **DOWNSTREAM/WWOX-INDEPENDENT** — target **unidentified** (L4) |
| **"Activate the compensating pathway(s)"** | 34210081 §3 and §5.2 — author speculation | **DOWNSTREAM/WWOX-INDEPENDENT** — target **unidentified** (L4) |

---

## 6 · Instrument reading — extraction damage measured, not assumed

The MCP extractor stripped **italicised gene/species tokens** *and* **every citation number** from
both bodies. Evidence on the face of the output: the returned titles are
`"Molecular Biology of theGene That Spans Chromosomal Fragile Site"` and
`"Tumor Suppressor WWOX Contributes to the Elimination of Tumorigenic Cells in"`; citation markers
render as `[]`, `[,]`, `[–]` throughout.

**Consequences, applied:**

1. **The brief's request to quote the review's sentences "with their citation numbers" cannot be
   satisfied from this route.** The numbers are not in the retrieved text. Attribution of L3 to
   `26390919` and L15 to `23765596` was made by **content match against those primaries' PubMed
   abstracts**, not by citation number — and both matched. This is stated rather than hidden.
2. **No negative in §4 rests on a zero count of an italicised token.** N1's term audit uses ordinary
   English words (`brain`, `neuron`, `glia`, `seizure`), which the extractor does not italicise, and
   N1 is anchored in the complete read regardless.
3. **Driver names (GMR-GAL4, engrailed-GAL4) are inferred** from positional description; the tokens
   were elided. Marked as inferred in §2a, asserted nowhere.
4. **No finding in this file rests on a figure panel.** Figure *legends* appear in the body text and
   are quotable; panel images are not inspectable in this checkout and were not used.

---

## 7 · Genotype transferability

WOREE genotype classes. "Transfers" means *the finding would bear on that class if the underlying
primary were obtained and held up*.

| Finding | null/null | splice/null | splice/missense | missense/missense | residual-protein | large deletion / CNV |
|---|---|---|---|---|---|---|
| **SDR catalytic site required** (L3, second-hand) — as a **construct-scope constraint** on gene therapy / AAV | ✅ applies | ✅ applies | ✅ applies | ✅ applies | ✅ applies | ✅ applies |
| **SDR catalytic site required** — as a **target-validity** signal for stabilising a missense | ❌ n/a | ❌ n/a | ⚠️ only if the missense spares the catalytic site | ⚠️ same | ⚠️ same | ❌ n/a |
| **Galactose / OXPHOS raises WWOX transcript** (L15, second-hand, transcript-only, HEK293) | ❌ **nothing to upregulate** | ❌ | 🔴 **potentially adverse** — more transcript from a splice-defective allele may mean more truncated unstable product (cf. `DL-MECH-045`), not more function | ⚠️ only if the missense protein retains partial function | ⚠️ **the only class with a coherent rationale**, and still transcript≠protein≠function | ❌ **nothing to upregulate** |
| **Cell-competition / pro-apoptotic WWOX** (L8, L12) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ — sign is anti-therapeutic in every class |
| **"Compensating pathway" treatability inference** (L2) | ⚠️ class-agnostic **because the pathway is unidentified**; transfers to none until named | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |

🔴 **The transferability table is where the node dies for WOREE.** Its only expression-raising
manoeuvre (L15) is useless in exactly the two classes where LEGEND most needs a lever
(**null/null**, **large deletion/CNV** — nothing to raise), is **potentially adverse** in the
**splice** classes, and is coherent only for **residual-protein** — the class that least needs it.

---

## 8 · ACQUISITION ASK

Precise, not general. Both are `Genes, Chromosomes & Cancer` (Wiley), no PMCID, unreadable here.

### A · `PMID 26390919` — Choo A, O'Keefe LV, …, Richards RI 2015, *GCC* 54(12):745–761, [10.1002/gcc.22286](https://doi.org/10.1002/gcc.22286)

**Ask for, in this order of value:**

1. 🔴 **The Results sentence and the figure panel + full legend for the Y288F experiment.** The
   question that decides `TX-007` construct scope is a *necessity-vs-sufficiency* question the
   review does not answer: **was the construct full-length WWOX carrying Y288F (necessity), or was
   an isolated SDR domain also tested (sufficiency)?** Request the transgene name exactly as
   Methods gives it (e.g. `UAS-Wwox-Y288F` vs `UAS-Wwox`) and the genotype list.
2. 🔴 **Any Western blot — panel + legend — showing Y288F protein is expressed at wild-type
   levels.** Without it, *"abolishing its function"* is not separable from *"the mutant protein
   isn't there"*. **Protein abundance ≠ function**, and the converse trap applies equally.
3. **The n per genotype and the statistic** for the outgrowth-suppression scoring — the readable
   sibling paper runs n = 10 eyes / n ≥ 20 discs, and the same ceiling probably applies.
4. **Whether any WWOX-loss phenotype was observed *without* the mitochondrial co-insult** — this is
   the direct test of L1 and of N11, and it is the single fact that would reopen the platform
   question.
5. The Methods sentence naming the **mitochondrial-complex deficiency alleles** used as the
   sensitising background, and the Results sentences on the **Akt / autophagy / HIF** modifiers
   (currently held from the abstract only).

### B · `PMID 23765596` — Dayan S, O'Keefe LV, Choo A, Richards RI 2013, *GCC* 52(9):823–831, [10.1002/gcc.22078](https://doi.org/10.1002/gcc.22078)

**Ask for:**

1. 🔴 **The Results sentence and figure giving the fold-change, n and statistic** for WWOX transcript
   under galactose/OXPHOS versus glucose, and under hypoxia.
2. 🔴 **Whether WWOX *protein* was measured at all — and if so, the Western panel + legend showing
   whether protein followed transcript.** *This is the single sentence that decides whether the
   metabolic-lever question has an answer.* A transcript-only result cannot support an
   expression-raising therapeutic rationale.
3. **Whether the effect was reproduced in any non-HEK293, non-transformed, or neural cell type**,
   and whether it was ever shown in a **primary** cell.
4. **Whether the raised transcript was shown to be the full-length, correctly spliced isoform** —
   directly relevant to the splice-class adverse-direction risk flagged in §7.

> **One-line framing for the human.** *"For 26390919: was the SDR domain tested alone, or only
> full-length protein bearing Y288F — and is there a Western showing Y288F protein is present at
> normal levels? For 23765596: was WWOX protein measured, or only mRNA?"* Those two questions
> settle everything this node could still contribute.

**Routing.** Both belong in the **acquisition packet**, as the scout already proposed; this read
converts two vague entries into four specific, answerable questions. Neither should be re-queued for
automated retrieval — no PMCID exists.

---

## 9 · DEFAULTS_TAKEN

Decisions made without instruction, each recorded so it can be overturned.

1. **Citation numbers.** The brief asked for the review's sentences *"verbatim with their citation
   numbers."* The extractor deletes all citation markers (§6). **Default:** quoted verbatim without
   numbers, attributed by content-match against the primaries' PubMed abstracts, and the limitation
   stated in §3 and §6 rather than silently dropped.
2. **Use of the two unobtainable abstracts.** Retrieved `26390919` and `23765596` via
   `get_article_metadata` to cross-check the review's characterisation. **Default:** used **only**
   as a fidelity check on the review, labelled "abstract only" at every use, **no receipt implied,
   no read claimed.** They agreed with the review; had they disagreed, that would have been the
   headline finding.
3. **Species of the transgene in 26302329.** Gene tokens elided. The detection antibody is
   *anti-C-DmWWOX*. **Default:** treated the manipulated gene as the **Drosophila ortholog**, stated
   as such, with the elision flagged.
4. **Driver identity.** GMR-GAL4 and an *engrailed*-class posterior driver **inferred** from
   positional description. **Default:** marked inferred; no finding rests on driver identity.
5. **Verdict grain.** The node yields one item of real value (L3, construct scope) that is neither a
   lever nor a platform. **Default:** the verdict answers the question **as posed** — **NO** — and
   the construct-scope constraint is surfaced immediately beneath it rather than being allowed to
   soften the verdict into a PARTIAL it does not earn.
6. **Scope.** Wrote exactly one file, at the path given. No canonical file touched, no receipt
   recorded, no commit candidate created, no claim proposed.

---

## 10 · What this changes, and what it does not

**Changes nothing canonical.** No claim is created, narrowed, reversed or revived by this file.

**Settles, on evidence rather than on absence** (as the scout asked): the Richards / O'Keefe node is
**off-axis oncology for WOREE purposes**. Its demotion no longer rests on acquisition failure — it
rests on two complete reads. **The node does not need to be reopened if `26390919` and `23765596`
later arrive; only the two narrow questions in §8 do.**

**Leaves standing, unchanged:** `DL-MECH-021` at `basso` (N3 gives it nothing either way);
`DL-MECH-020`; `HYP-20260709-01` (the ketogenic rationale's primaries were already read, and
**nothing in either paper here bears on it** — no diet was ever tested in this node).

**Adds one observation to an existing pattern, without proposing it as a claim:** 26302329 is a
**fourth** independent demonstration that in this literature the tractable direction is *removing*
WWOX. Here, knocking WWOX down is the phenotype-improving move (L8). In a genotype already short of
functional WWOX, that direction is unavailable. This corroborates the standing category objection
recorded in `AUTONOMOUS_SESSION_STATE.md` §"three results"; it is **not** a new claim and is
**not** proposed for commit.

---

*Sources: PubMed / PubMed Central. O'Keefe LV et al., PLoS One 2015;10(8):e0136356 —
[10.1371/journal.pone.0136356](https://doi.org/10.1371/journal.pone.0136356). Lee CS et al.,
Cells 2021;10(7):1637 — [10.3390/cells10071637](https://doi.org/10.3390/cells10071637). Abstracts
only: Choo A et al., Genes Chromosomes Cancer 2015;54(12):745–61 —
[10.1002/gcc.22286](https://doi.org/10.1002/gcc.22286); Dayan S et al., Genes Chromosomes Cancer
2013;52(9):823–31 — [10.1002/gcc.22078](https://doi.org/10.1002/gcc.22078); O'Keefe LV et al.,
Hum Mol Genet 2011;20(3):497–509 — [10.1093/hmg/ddq495](https://doi.org/10.1093/hmg/ddq495).*

*Not medical advice. Non-canonical analysis file, research layer.*
