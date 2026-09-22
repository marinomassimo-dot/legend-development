# TX-007 — PERIPHERAL VECTOR-GENOME qPCR: the implementation that makes the follow-up experimentally complete

**Actor:** Scientist A · **Date:** 2026-09-22 · **Axis:** assay implementation only
**Scope:** the three missing components of proposal `B1` — normalisation, standard curve, matrix recovery.

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, every registry,
> every queue, every ledger, every receipt and the state manifest. Nothing promoted, nothing committed,
> no `BATCH_COMMIT`, no receipt claimed, no git command executed, no external contact, no purchase.
>
> 🔴 **Nothing here is medical advice.** No molecule, no dose, no route, no schedule, no clinical framing.
> Every clinical question is `HUMAN_REQUIRED`. 🔴 **Nobody has been contacted and nobody will be by an agent.**
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> 🔴 **Alleles, drivers and species are never pooled.** Everything below concerns the **Aqeilan `Wwox`-null
> mouse** and the AAV9-hSynI-WWOX arms of `PMID 42422765` (2026) and `PMID 34747138` (2021), which are
> themselves **different objects** and never share a row.

---

## 0 · What this file is, and what it deliberately is not

Two sibling files stop at the same sentence. `tx007_peripheral_vector_arrival_20260922.md` establishes that
the programme's own vector-genome qPCR is **recoverable as a relative assay** and that it **must be upgraded
with a single-copy nuclear normaliser, a standard curve and a spiked-matrix recovery control** before a
peripheral reading means anything (`§2.3`, `§3`, ladder row `B1`).
`COMMUNITY_FOLLOWUP_peripheral_vector_qpcr_20260922.md:79-82` names the same three additions and stops.

**Neither file specifies them.** That is the whole gap, and it is the difference between a proposal a
laboratory can decline as under-specified and one it can cost in an afternoon.

🔴 **This file adds nothing to the biology, proposes no new tissue, no new arm, no new timepoint and no new
animal.** It is deliberately the *smallest technically defensible* implementation. Where a component can be
dropped, it says so and states the blind spot that dropping it creates. **It is not a biodistribution
programme** and must not be grown into one.

### 0.1 Provenance and the quotation rule

🔴 **I did not read either primary body in this act.** `files/fulltext/` does not exist in this edition; no
external contact was made. **Every primary quotation below is tagged `SIBLING-ATTESTED` with the repository
file and line it was taken from.** No sequence is invented anywhere in this file.

**Enumeration before filtering** (method bound): plain `ls disease-models/wwox/analysis/` — **175 entries**
including 4 sub-directories (`data`, `near_miss_cases`, `orchestration_reviews`, `scripts`) — and
`ls -R disease-models/wwox/research/` — 24 top-level entries plus `commit_candidates` (113),
`deepdive_manifests` (80), `fulltext_dossiers` (53), `locator_audits` (1), `page_adjudications` (6 PMIDs),
`pattern_audits` (2), `session_evaluations` (42). **Both listings were read end to end before the first
`grep`.** The two mandated files were then read in full and are **not re-derived** here.

### 0.2 The established asset, verified at source and NOT re-derived

**SIBLING-ATTESTED**, `PMID 42422765` Materials and Methods, quoted **first-hand by Scientist C** at
[`cerebellum_layer_localisation_20260922.md:212-215`](cerebellum_layer_localisation_20260922.md):

> "tissue samples (up to 25 mg) were lysed in ATL buffer … DNA integrity and concentration were assessed
> prior to downstream applications by using DeNovix (DS-11FX+). **For qPCR, 50 ng of DNA template was used
> per reaction.** The primer sequences were as follows: forward 5′ GCTCTCTTAAGGTAGCCCCG 3′, reverse
> 5′ CGCCTCATCCTGGTCCTAAA 3′."

| Element | Status | Verified at |
|---|---|---|
| Vector primer pair, 20 nt each | 🟢 published verbatim, transcribed first-hand | [`:214-215`](cerebellum_layer_localisation_20260922.md) |
| 50 ng DNA template per reaction | 🟢 published | [`:213-214`](cerebellum_layer_localisation_20260922.md) |
| ≤25 mg tissue, ATL-buffer lysis | 🟢 published; a **mass** limit, not a tissue restriction | [`:212`](cerebellum_layer_localisation_20260922.md) |
| DeNovix DS-11FX+ quantitation | 🟢 published | [`:212-213`](cerebellum_layer_localisation_20260922.md) |
| Host reference amplicon | 🔴 **DOES NOT EXIST** — validated negative, `reference gene` 0, `single-copy` 0 | [`:217-218`](cerebellum_layer_localisation_20260922.md) |
| Standard curve / absolute copy units | 🔴 **DOES NOT EXIST** — `standard curve` 0, `copies` 0, `diploid` 0 | [`:217-218`](cerebellum_layer_localisation_20260922.md) |
| What the amplicon **targets** | 🔴 `METHODS_INVISIBLE` — 🔴 **do not assume the titration assay's bGH target** | [`tx007_peripheral_vector_arrival_20260922.md:163`](tx007_peripheral_vector_arrival_20260922.md) |
| Perfusion status of the **DNA** tissue | 🔴 **NOT STATED.** Stated only for RNA: *"non-perfused tissue"* | [`:244`, `:259`](cerebellum_layer_localisation_20260922.md) |

🔴 **The primer pair is reproduced here as a locator, not as a design. Anyone reusing it must re-read it at
the source before synthesis.**

### 0.3 🔴 UNDISCHARGED READING DEBT — declared before it is leaned on

**This file cites no PMID other than `42422765` and `34747138`**, both of which carry declared full-text-queue
entries. Everything below that is generic molecular-biology practice — processed-pseudogene burden of mouse
`Gapdh`/`Actb`, the field-standard status of single-copy copy-number reference loci, FFPE fragment-length
behaviour, Poisson sampling at low copy number, liver as an inhibitor-rich matrix — is marked

> `PREMISE: DEFAULT_FROM_TEXTBOOK` · **UNDISCHARGED READING DEBT**

**No conclusion in this file rests on any of it.** Each such premise is used only to *choose between design
options*, and each is paired with a **free in-silico or bench verification** that discharges it before a
single primer is ordered. Where a specific published primer sequence would be needed, **this file does not
supply one and does not invent one** — it supplies the locus and the design criteria, which is what a
laboratory actually needs. 🔴 **A design criterion is not a validated reagent.**

---

## 1 · NORMALISATION — the host reference amplicon

### 1.1 What the fixed-mass design already buys, and exactly where it fails

🟢 Fifty nanograms of murine genomic DNA is a fixed number of nuclei (~6 pg per diploid genome ⇒
~8.3 × 10³ nuclei), so a vector amplicon read against fixed DNA **mass** is already approximately a
per-nucleus quantity — *"cell-density normalisation is built into the assay design"*
([`cerebellum_layer_localisation_20260922.md:222-229`](cerebellum_layer_localisation_20260922.md)).
**That is real and it is not re-derived here.**

🔴 **It fails on one word: `nominal`.** Fifty nanograms *dispensed* is not fifty nanograms *amplifiable*.
Three failure modes sit inside that gap, and all three bias toward **absent**:

1. **Mis-quantitation.** A DeNovix A260 reading counts RNA, free nucleotides and protein-bound nucleic acid
   as DNA. Liver, with high RNA and glycogen content, over-reads most; nerve, with low yield, is read at the
   noisy bottom of the instrument's range.
2. **Inhibition.** Carried-over haem, salt or ethanol reduces amplification efficiency without reducing the
   measured DNA mass at all.
3. **Fragmentation.** In FFPE or PFA/OCT material a large fraction of the 50 ng is too short to carry any
   amplicon. Mass is intact; templates are not.

> 🎯 **The host amplicon is not a nicety, it is the measurement that converts a nominal mass into a counted
> genome.** It is the only per-well evidence that the denominator exists.

### 1.2 🔴 Why `Gapdh` and `Actb` are the wrong choice for a **DNA**-template assay in mouse

This is the single most common error in transplanting a qPCR normaliser from an RNA assay to a DNA assay,
and it is worth stating mechanically rather than as a warning.

- Both `Gapdh` and `Actb` are highly expressed housekeeping transcripts, and highly expressed transcripts are
  exactly the substrates that retrotransposition converts into **processed pseudogenes**. The mouse genome
  carries a substantial burden of such loci for both genes.
  `PREMISE: DEFAULT_FROM_TEXTBOOK` · **UNDISCHARGED READING DEBT**
- A processed pseudogene is a **reverse-transcribed, intronless, genomically integrated copy of the mRNA**.
  On an **RNA** template it is mostly invisible, because it is usually not transcribed and because the
  standard defence — an **intron-spanning primer pair** — excludes it.
- 🔴 **On a DNA template that defence does not exist.** Genomic DNA contains the introns *and* the
  intronless pseudogenes. An exonic primer pair amplifies every pseudogene copy alongside the parent gene.
- **Direction of the error, and it is the dangerous direction.** The host amplicon is the **denominator**.
  Inflating it by an unknown, *possibly tissue-variable* pseudogene multiplier **deflates** vector-copies-per-
  genome. 🔴 **The bias runs toward "the vector is absent" — which is the conclusion the existing peripheral
  inference already assumes.** A confirmation-shaped artefact is the worst kind available here.
- ⚠️ A second, quieter error: the multiplier need not be constant across tissues if local copy-number or
  amplifiability differs, so a pseudogene-contaminated denominator can manufacture a *spurious tissue
  gradient* — exactly the quantity this experiment is trying to read.

**Also categorically excluded, for reasons the record already states:**

| Excluded class | Why |
|---|---|
| **rRNA loci (`Rn45s` etc.)** | tandem multi-copy arrays with strain- and cell-variable copy number — there is no "per diploid genome" to divide by |
| **Mitochondrial targets** | hundreds to thousands of copies per cell, varying by **orders of magnitude** between liver, nerve and brain; would manufacture a tissue gradient outright ([`tx007_peripheral_vector_arrival_20260922.md:~210`](tx007_peripheral_vector_arrival_20260922.md) §3.1) |
| **rRNA / total-RNA normalisers** | 🔴 **categorically wrong** — the denominator of the *transcript* panel, non-interconvertible with a genome denominator ([`cerebellum_layer_localisation_20260922.md:252-257`](cerebellum_layer_localisation_20260922.md)) |
| **Sex-chromosome loci** | dosage differs between males and females; the 2026 programme ran fertility testing across **20 breeding cages per group**, so both sexes are in the cohort. A sex-linked denominator halves in one sex |
| 🔴 **Anything inside or adjacent to `Wwox`, or inside the human `WWOX` transgene** | the host animal is `Wwox`-**null**: the endogenous locus is disrupted by construction, and the transgene is the numerator. Normalising to either is circular |

### 1.3 The choice, and the reasoning that produces it

**Four properties are load-bearing, in this order:**

| # | Requirement | Why it is load-bearing here |
|---|---|---|
| **R1** | **Single-copy, autosomal, in the mouse reference genome** | so that `copies ÷ 2 = diploid genomes` directly, with no sex term and no ploidy term in the *genome* denominator |
| **R2** | **No processed-pseudogene ambiguity** | §1.2 — the denominator must not be inflatable |
| **R3** | **Short amplicon** — target **60–90 bp**, and **length-matched to the vector amplicon** | the archived peripheral material is plausibly FFPE/PFA-fixed (`tx007_peripheral_vector_arrival_20260922.md` §1.4, 🟡 **PROBABLY EXISTS as FIXED material only**), where DNA is fragmented and cross-linked. Amplification efficiency falls steeply with target length on such template |
| **R4** | **Verified non-cross-reactive** with the vector genome, the packaging plasmid and human `WWOX` | a host primer that touches the transgene destroys the ratio |

**On R3, the part that is usually missed.** A short amplicon is not merely "more robust". 🎯 **What actually
matters is that the host and vector amplicons be of *similar* length.** Fragmentation attenuates a long
amplicon more than a short one; if the host amplicon is 150 bp and the vector amplicon is 80 bp, degradation
alone inflates vector-per-genome — a **false positive** — and the reverse pairing manufactures a **false
negative**. Length-matching makes fragmentation cancel in the ratio instead of biasing it. 60–90 bp is the
band that survives FFPE and still permits a specific primer pair; below ~60 bp primer-dimer discrimination
becomes the limiting problem.

🔴 **The vector amplicon's length is currently unknown** — the paper publishes the sequences and not the
element they sit in, so the product size is not derivable
([`tx007_peripheral_vector_arrival_20260922.md:163`](tx007_peripheral_vector_arrival_20260922.md)).
🟢 **This is cheap to close:** run the published pair once on vector-positive brain DNA or on the packaging
plasmid and size the product on a gel or a fragment analyser. **One lane. It must precede primer ordering,
because the host amplicon is designed *to match* it.**

#### Candidate loci

| Locus | Case for | Case against / to verify |
|---|---|---|
| 🥇 **`Tfrc`** (transferrin receptor) | The field-standard **single-copy autosomal reference for mouse genomic copy-number assays**; it is the locus commercial copy-number reference assays use for mouse, which means efficiency-matched designs and published validation already exist. Not a retrotransposition-prone housekeeping transcript in the `Gapdh`/`Actb` sense. `PREMISE: DEFAULT_FROM_TEXTBOOK` · **UNDISCHARGED READING DEBT** | 🔴 **Verify single-copy status and autosomal assignment in the current mouse reference build before ordering** — a free in-silico step (§1.4). `Tfrc` is expressed, so a pseudogene search is mandatory, not assumed |
| 🥈 **`Rpp30`** (RNase P subunit p30) | The reference target most widely used for **AAV vector-genome copy-number quantification** specifically, in both qPCR and droplet formats — so a peripheral result expressed against it is directly comparable to external AAV biodistribution datasets. `PREMISE: DEFAULT_FROM_TEXTBOOK` · **UNDISCHARGED READING DEBT** | same verification burden; mouse `Rpp30` designs are less widely circulated than human `RPP30` |
| 🥉 **An intronic window in any verified single-copy autosomal gene** | 🎯 **Structurally immune to R2**: a processed pseudogene is reverse-transcribed from mRNA and therefore **contains no introns**, so a primer pair sited wholly *within an intron* cannot amplify one. This converts pseudogene exclusion from a literature question into a design guarantee | requires a bespoke design and its own validation; no off-the-shelf assay to fall back on |

> ### 🥇 Choice: **`Tfrc`, with the primer pair sited so that at least one primer lies in intronic sequence**
>
> **The reasoning, in one line:** `Tfrc` gives the widest existing validation base (R1, and a real fallback if
> a bespoke design fails), and the intronic siting buys the *structural* pseudogene guarantee (R2) that no
> amount of literature reading can fully buy for an exonic target. **`Rpp30` is the named alternate** and is
> preferable if the laboratory already runs an AAV copy-number workflow around it — in that case use what is
> already validated in that lab rather than importing this one. **Either answers the question; neither is
> worth an argument.**

🔴 **NO PRIMER SEQUENCE IS GIVEN FOR THE HOST AMPLICON, AND NONE IS INVENTED.** The repository holds no
verified `Tfrc` or `Rpp30` primer pair, and no such sequence is retrievable from repo-held material. **What is
specified is the locus and the design criteria**; the sequence is either taken from a commercial validated
copy-number assay or designed in-house against the current mouse reference build and validated as in §1.4.
**Naming a sequence from memory would be the exact invention this programme forbids.**

### 1.4 Validation before a single sample is run — all of it free or near-free

1. **In-silico specificity.** BLAT/BLAST the candidate host pair against the current mouse reference build:
   require **one** genomic hit. 🎯 **This single step discharges the pseudogene reading debt of §1.2 directly
   and empirically** — if `Gapdh`/`Actb` pairs return many hits and the `Tfrc` intronic pair returns one, the
   textbook premise has been replaced by a measurement, at zero cost.
2. **Cross-reactivity.** Run the same search against the vector genome, the packaging plasmid and human
   `WWOX`. Require zero hits (R4).
3. **Strain-variant check.** Confirm no known strain SNP or indel falls under either primer footprint — a
   variant under a 3′ end shifts efficiency and silently rescales the denominator.
4. **Efficiency matching.** Both amplicons must run at **90–110 % efficiency, R² ≥ 0.99**, over the working
   range (§2). 🔴 **Ratio arithmetic between two amplicons is only valid if their efficiencies match**; this
   is the precondition for the entire normalisation and is measured on the same plate as the standard curve,
   so it costs nothing extra.
5. **Single product.** Melt curve (dye chemistry) or a sized product on one gel lane.

### 1.5 🔴 What the normaliser does and does not fix in **liver**

🟢 **It fixes the denominator.** Vector copies ÷ host single-copy copies ÷ 2 = **vector genomes per diploid
genome**. That quantity is **ploidy-robust**: a tetraploid hepatocyte contains twice the genomes and twice the
host amplicon copies, so the ratio is unchanged. 🎯 **This is a genuine gain over the published fixed-mass
design, in the one tissue where fixed-mass normalisation is weakest.**

🔴 **It does not fix the per-cell interpretation.** "Vector genomes per diploid genome" in polyploid liver is
**not** "vector genomes per cell", and the two differ by the mean ploidy — which this experiment does not
measure and must not silently assume.

> **Reporting rule, stated so it cannot be lost downstream:** the peripheral result is reported in **copies
> per diploid genome**, and the liver row carries the explicit note that **per-cell load is higher than the
> per-genome figure by the unmeasured mean ploidy factor**. 🔴 **Any cell-level statement about liver is
> `NOT RECONSTRUCTIBLE` from this assay** and is not made.

---

## 2 · STANDARD CURVE — the minimum that makes a NEGATIVE interpretable

### 2.1 Two different questions, and only one of them is being asked

| | (a) **Relative arrival / absence** | (b) **Absolute copies per diploid genome** |
|---|---|---|
| **Question answered** | is there vector in this tissue, above a stated floor? | how much vector is in this tissue, in field-standard units? |
| **Needs a calibrant curve?** | 🟢 **YES — for the LOD, not for the magnitude** | 🟢 yes |
| **Needs a host amplicon?** | 🟡 not strictly, but see §1.1 — without it there is no proof the template was loaded | 🟢 mandatory |
| **Needs a *host* calibrant curve?** | 🔴 **no** | 🟢 yes |
| **Comparable to the published brain panel?** | within-panel only | 🟢 yes |
| **Comparable to external AAV datasets?** | 🔴 no | 🟢 yes |

🎯 **The biological question is arrival versus expression. That is a DETECTION question, not a magnitude
question.** Nothing in the four pre-stated outcomes
([`tx007_peripheral_vector_arrival_20260922.md` §4](tx007_peripheral_vector_arrival_20260922.md)) turns on
*how much* vector is present; they turn on **present versus absent**, and on absent being trustworthy.

> ### 🥇 **Decision: absolute quantification is NOT required by the question. A calibrant dilution series that establishes efficiency, LOD and LOQ IS required — and it is required for exactly one reason: without it, a negative means nothing.**

🔴 **The standard curve is not here to put a number on a positive. It is here to put a floor under a
negative.** That is why it cannot be dropped even though absolute copies can be.

### 2.2 The honest arithmetic of "prefer the smaller answer"

The brief says prefer the smaller answer where it truly answers the question. Applied properly, that rule
**does not stop at (a)**, and the reason is arithmetic rather than ambition:

- The **vector** calibrant curve is **mandatory** for (a). It is the LOD.
- 🟢 Once that curve exists and the host amplicon of §1 is already in every well, **(b) costs one additional
  eight-well column**: the same dilution series read with the host primer pair, or a mouse-gDNA mass series.
- ⇒ **(b) is ~95 % paid for by (a).** Declining it saves one column and forfeits comparability to the
  published brain panel and to every external AAV biodistribution dataset.

> **Minimum specification, stated as a floor and a recommendation, so a laboratory can choose:**
>
> 🥇 **FLOOR (non-negotiable):** a **vector-fragment dilution series in matrix-matched vector-free mouse
> genomic DNA**, sufficient to state efficiency, LOD and LOQ. A negative is then reported as
> *"below X copies per 50 ng of genomic DNA (≈ 8.3 × 10³ diploid genomes)"*.
>
> ⭐ **RECOMMENDED (one extra column):** add the parallel **host** calibrant curve and report
> *"below X copies per diploid genome"*. 🎯 **Take the recommended option unless the plate is physically
> full.** It converts a lab-internal floor into the unit the field reads.

### 2.3 The calibrant — and the one thing that must not be got wrong

| Option | Verdict |
|---|---|
| **Linearised plasmid** carrying the vector amplicon | 🟢 standard and adequate. 🔴 **Must be linearised** with a single-cutter **outside** the amplicon: supercoiled DNA amplifies inefficiently and systematically **under**-calls copy number, which would set the LOD too low and make a negative look stronger than it is |
| **Synthetic double-stranded fragment (gBlock-class)** containing the vector amplicon | 🟢 equivalent, avoids the linearisation step, and is supplied at a stated copy concentration |
| ⭐ **A single dual-target synthetic fragment carrying the vector amplicon AND the host amplicon in a 1:1 cassette** | 🎯 **The elegant minimum.** One calibrant, one dilution series, and the two curves are **ratio-locked by construction** — pipetting error between two separate series cannot distort the vector:host ratio, which is the reported quantity. ⚠️ Honest limit: a fused cassette does not reproduce genomic sequence context or chromatin, so it calibrates *copy number*, not *extractability*. Extractability is §3's job, not the curve's |
| 🔴 **Purified vector prep as calibrant** | 🔴 **Avoid.** Its titre was determined by a *different assay with different primers* — *"Viral titers were determined by RT-qPCR using bGH primers"* ([`tx007_per_arm_delivery_reconstruction_20260922.md:169`](tx007_per_arm_delivery_reconstruction_20260922.md)) — so using it as a calibrant imports that assay's unknown accuracy and **silently assumes the tissue amplicon and the titration amplicon are the same target**. 🔴 **They are not established to be the same, and that assumption is explicitly forbidden** ([`tx007_peripheral_vector_arrival_20260922.md:163`](tx007_peripheral_vector_arrival_20260922.md)) |

**Critical detail: the curve must be run in a background of vector-free mouse genomic DNA at the same mass
(50 ng) as the samples.** A curve in water measures the chemistry; a curve in matrix measures the assay. Only
the second yields an LOD that applies to the samples.

### 2.4 LOD and LOQ — stated explicitly, because without them a negative is not a result

| Term | Operational definition used here |
|---|---|
| **Efficiency** | slope over the linear range ⇒ 90–110 %, **R² ≥ 0.99**. Below this, ratio arithmetic between the two amplicons is invalid |
| **LOD — limit of detection** | the lowest copy input detected in **≥ 95 % of replicate reactions**. ⚠️ Near the floor this is **Poisson-limited, not chemistry-limited**: at a mean of ~3 copies per reaction, ~5 % of reactions receive zero template by sampling alone, so a dropout at the bottom is expected and is not assay failure. ⇒ the near-limit dilutions need **many replicates (order 8–20), not three** |
| **LOQ — limit of quantification** | the lowest copy input where the copy-number CV is acceptable (conventionally ≤ 25–35 %). 🔴 **Always higher than the LOD.** A signal between LOD and LOQ is *"detected, not quantifiable"* — a real and reportable state that must not be rounded into either "absent" or a number |

`PREMISE: DEFAULT_FROM_TEXTBOOK` · **UNDISCHARGED READING DEBT** for the conventional numeric thresholds
(90–110 %, ≥0.99, ≥95 %, ≤25–35 %). 🔴 **No conclusion rests on the exact figures** — what is load-bearing is
that the laboratory **states whichever thresholds it used, before the plate is read**, and reports the
achieved values alongside the result.

> ### 🎯 The strongest honest form of a negative
>
> > **"Below `X` copies per diploid genome, at `Y` % spiked recovery, in `N` animals per arm, with host
> > amplicon confirming `Z` genome equivalents loaded per well."**
>
> 🔴 **Anything less is an absence of evidence.** And the reciprocal bound: the parent paper reports `n` for
> nothing — `n =` → **0 tokens in the served body**
> ([`cerebellum_layer_localisation_20260922.md:63`](cerebellum_layer_localisation_20260922.md)) — so `N` must
> be stated here even though the assay being extended never stated it.

### 2.5 🔴 The new risk the upgrade itself introduces

**A standard curve puts a high-concentration amplifiable template on the bench that did not previously exist
there.** Plasmid or synthetic-fragment carryover is the classic source of a false positive in a laboratory
that also holds the vector.

**Minimum mitigation, and it is procedural rather than expensive:** prepare and dilute the calibrant in a
**separate area with dedicated pipettes**, load it **last**, site the blanks **away from the high standards**
on the plate map, and **state in advance** that any amplification in the no-template control or in either
matrix-matched blank **voids the run**. 🎯 **Stated as an honest cost of the upgrade**, not hidden: the
addition that rescues a negative also creates a route to a false positive, and §4 is why that trade is still
strongly worth taking.

---

## 3 · MATRIX RECOVERY — per tissue, and where it can be dropped

### 3.1 The two controls that are usually conflated

| Control | What it measures | Cost |
|---|---|---|
| **Pre-extraction spike** — known vector copies added to vector-free tissue **before** lysis | 🟢 **extraction recovery AND inhibition together** — the full pipeline | one extra tissue aliquot + one extraction |
| **Post-extraction spike** — copies added to the finished eluate / the reaction | inhibition **only**; blind to anything lost on the column | one extra well |
| 🟢 **Host amplicon** (§1), already in every well | 🎯 **a free per-sample inhibition and loading sensor**: a host Ct later than expected for 50 ng flags inhibition or under-loading **in that specific sample** | **zero** — already present |
| 🟢 **Dilution parallelism** — run each sample at 50 ng and at 10 ng | 🎯 a **free inhibition test**: a 5-fold dilution must shift Ct by ~2.32 cycles. A smaller shift means the undiluted well was inhibited | one extra well per sample |

> 🎯 **The single most useful economy in this file:** the host amplicon plus dilution parallelism catch
> **inhibition** in every sample at essentially no cost. What they cannot catch is **extraction loss** — DNA
> that never reached the tube. **Only a pre-extraction spike sees that**, which is why the per-tissue decision
> below is about the *pre-extraction* spike specifically and not about inhibition controls in general.

**Blanks, already established and not re-derived:** `KO+RI` and `WT+RI` are vehicle-injected, guaranteed
zero-vector animals that went through identical surgery at identical age in the identical facility — *"RI"* =
reference item = *"PBS with 5 % sorbitol and 0.001 % pluronic F-68"*
([`fold_of_wt_is_undefined_for_vdna_20260922.md:26-33`](fold_of_wt_is_undefined_for_vdna_20260922.md)).
🎯 **They are also the matrix for the spikes.** No better vector-free tissue exists.

### 3.2 Per-tissue decision

#### 🔴 LIVER — **pre-extraction spike NECESSARY. Do not drop.**

Three concrete reasons, in descending force:

1. **Liver is the inhibitor-rich matrix, concretely.** Residual blood brings **haem and iron**, which are
   direct polymerase inhibitors; liver additionally carries high **glycogen**, **lipid** and **bile salt**
   load, and the highest **RNA** content of the three tissues — RNA both inflates the A260 mass reading on the
   DeNovix (so less DNA is loaded than believed) and competes on a silica column.
   `PREMISE: DEFAULT_FROM_TEXTBOOK` · **UNDISCHARGED READING DEBT** — 🎯 **and this premise is discharged by
   the spike itself**, which measures the inhibition rather than assuming it.
2. **Liver's very high DNA yield per mg is its own failure mode.** 25 mg of liver can **overload** a spin
   column, which degrades wash efficiency and carries chaotropic salt or ethanol into the eluate. 🔴 **The
   `≤25 mg` published input was validated on brain, not liver**, and this is the one place where the published
   protocol most plausibly does not transfer unchanged. ⚠️ Mitigation is trivial — use a smaller liver input
   (e.g. 10 mg) and report it — but the *decision* to do so requires the recovery data.
3. 🎯 **This is where the error is confirmation-shaped, and that is decisive.** Liver carries the strongest
   peripheral protein negative on record — a **both-arm** result
   ([`tx007_per_arm_delivery_reconstruction_20260922.md:154`](tx007_per_arm_delivery_reconstruction_20260922.md)) —
   so ABSENT is the *expected* answer. 🔴 **An inhibited liver reaction returns exactly the expected answer,
   and nothing in the data would look wrong.** An uncontrolled liver negative would be indistinguishable from
   a failed extraction and would be accepted precisely because it agrees with the standing inference.

**Specification: spike `KO+RI` liver at two levels — near-LOQ and ~10× LOQ — before lysis, alongside an
unspiked `KO+RI` liver. Report recovery as a percentage. Pre-state the floor (e.g. recovery < 50 % ⇒ the
liver negative is reported as UNINTERPRETABLE, not as absent).**

#### 🔴 SCIATIC NERVE — **pre-extraction spike NECESSARY, for a different reason.**

🔴 **Here the threat is not inhibition. It is yield, and it is arithmetic.**

- Sciatic nerve is dense collagen and myelin with few nuclei per milligram: DNA yield per mg is **low and
  variable**, and the extraction is the hard part (incomplete lysis of a tough matrix loses template).
- 🔴 **`≤25 mg` may exceed the whole tissue.** A mouse sciatic nerve segment is a small piece of tissue, and
  **`25 mg` is a ceiling the protocol permits, not a mass this tissue supplies.**
  `PREMISE: DEFAULT_FROM_TEXTBOOK` · **UNDISCHARGED READING DEBT** — 🎯 **and it is discharged by weighing the
  archived nerve, which is free and must happen before the plate is designed.**
- ⇒ **The 50 ng-per-reaction specification may not transfer to nerve at all.** If total recoverable DNA does
  not support 50 ng × (vector + host) × replicates, then **the protocol must be re-specified at the mass
  actually available, and the LOD recomputed at that mass.** 🔴 **A smaller template mass raises the LOD in
  copies-per-genome, and a negative reported against the brain assay's nominal floor would then be
  overstated.**
- 🎯 **And nerve is where the decisive 2×2 of §5 is read.** An uncontrolled nerve negative does not merely
  lose information; it would license the *"protein arrived by axonal transport"* reading on the strength of a
  failed extraction.

**Specification: spike `KO+RI` sciatic nerve before lysis at near-LOQ; report recovery; report the DNA mass
actually obtained per nerve and the template mass actually loaded; state the LOD at that mass, not at 50 ng.**

#### 🟢 SPINAL CORD — **the pre-extraction spike CAN BE DROPPED. This is the one place the minimum shrinks.**

Three reasons it is droppable:

1. **The matrix is the one the published protocol was validated on.** Spinal cord is CNS tissue, closest of
   the three to the four brain regions where the ATL-lysis + 50 ng workflow **demonstrably worked in this lab
   for this paper**. It is not inhibitor-rich and not low-yield.
2. **Spinal cord is the least informative tissue on this axis** — CNS tissue continuous with the injected
   compartment, where *"a positive is nearly expected and should not be scored as peripheral"*
   ([`tx007_peripheral_vector_arrival_20260922.md` §4.3, §4.5](tx007_peripheral_vector_arrival_20260922.md)).
3. **The expected answer is PRESENT**, and a spike protects against a **false negative**. Dropping a control
   against the error you do not expect to make is the correct economy.

> 🔴 **The blind spot this creates, stated plainly:** if spinal cord returns **ABSENT**, that negative is
> **uncontrolled and cannot be asserted**. It would also be a genuinely surprising result.
>
> ⭐ **Contingency, which costs nothing to pre-state and removes the blind spot entirely:** drop the spinal-cord
> spike prospectively; **a spinal-cord ABSENT result triggers a retrospective spike on `KO+RI` spinal cord
> before that negative is reported anywhere.** 🎯 **Pre-stating the contingency is what makes dropping the
> control defensible rather than merely cheap.**

### 3.3 The minimum plate, in full

| Component | Included? |
|---|---|
| Vector amplicon, every sample | 🟢 mandatory |
| Host amplicon (§1), **every well/sample** | 🟢 mandatory — the denominator **and** the free inhibition sensor |
| Vector calibrant dilution series **in vector-free mouse gDNA at 50 ng** | 🟢 mandatory — the LOD |
| Host calibrant series | ⭐ recommended, one column — converts the floor to copies per diploid genome |
| `KO+RI` peripheral tissue, each tissue | 🟢 mandatory — matrix-matched vector-free blank; a signal here **voids the run** |
| `WT+RI` peripheral tissue | 🟢 mandatory — host background and primer cross-reactivity |
| No-template control | 🟢 mandatory |
| **Pre-extraction spike: liver** | 🔴 **mandatory, two levels** |
| **Pre-extraction spike: sciatic nerve** | 🔴 **mandatory, one level** |
| **Pre-extraction spike: spinal cord** | 🟢 **droppable, with the §3.2 contingency pre-stated** |
| Dilution parallelism (50 ng / 10 ng) | 🟢 cheap, catches inhibition per sample |
| Brain region(s) from the same animals | ⭐ **strongly recommended** — an on-plate positive that anchors the peripheral reading to the published panel and proves the run worked. Costs a few wells of already-characterised material |

---

## 4 · THE ASYMMETRY — preserved explicitly, because it decides how the plate is read

🔴 **`ABSENT` and `PRESENT` do not have symmetric evidentiary strength, and the direction favours `ABSENT`.**

**The mechanism.** The vector was injected into an animal and vector particles circulate. A tissue reading
therefore includes whatever vector sits in the **blood inside** that tissue at harvest.
🎯 **Blood contamination can only ADD vector signal.** It biases toward a **false positive** and **cannot
manufacture a false negative**
([`tx007_peripheral_vector_arrival_20260922.md` §3.3](tx007_peripheral_vector_arrival_20260922.md)).

| Confound | Direction |
|---|---|
| Residual blood / circulating vector in tissue | → **false POSITIVE** |
| Extracellular or surface-bound capsid | → **false POSITIVE** |
| Calibrant-plasmid carryover (**new**, §2.5) | → **false POSITIVE** |
| Cross-well contamination from high standards | → **false POSITIVE** |
| Extraction failure / inhibition | → false NEGATIVE — 🟢 **and this is precisely what §3 controls** |
| Episomal dilution by cell division | → false NEGATIVE — 🔴 **not controllable; it bounds the claim, see below** |

> ### 🎯 The consequence, stated as an operating rule
>
> **A technically validated NEGATIVE — stated LOD, demonstrated spiked recovery, host amplicon confirming the
> genome equivalents loaded — is the ROBUST outcome, because every uncontrolled confound on this plate pushes
> the other way.**
>
> **A POSITIVE is the FRAGILE outcome.** It requires the perfusion status resolved, the blanks clean, the
> calibrant segregated, and — for spinal cord — the recognition that CNS tissue continuous with the injected
> compartment is a **delivery-extent** result, not a peripheral one.

🔴 **Perfusion is `METHODS_INVISIBLE` for exactly the tissues that matter.** The source states non-perfusion
**only for RNA** — *"Total RNA was isolated from non-perfused tissue"*
([`cerebellum_layer_localisation_20260922.md:244`, `:259`](cerebellum_layer_localisation_20260922.md)) — and
the perfusion status of the **DNA** tissue is **not stated anywhere in the repository**. The separate perfused
cohort is the **histology** cohort and its protocol names **brains**
([`tx007_peripheral_vector_arrival_20260922.md` §1.4, §3.3](tx007_peripheral_vector_arrival_20260922.md)).
⇒ **Assume non-perfused unless the holding laboratory says otherwise** (`HUMAN_REQUIRED`). ⚠️ Tissues differ
enormously in blood content — **unperfused liver is the most contaminated reading available; unperfused
sciatic nerve among the least** — so the false-positive risk is itself tissue-graded, and it is worst in the
tissue where a positive would be most surprising.

⚠️ **The one asymmetry-breaking caveat, not re-derived:** episomal genomes dilute with cell division, so
**"absent at P30" is not "never arrived"** — it is *"amplifiable vector genomes are below the limit of
detection in this tissue at this age"*
([`tx007_peripheral_vector_arrival_20260922.md` §3.4](tx007_peripheral_vector_arrival_20260922.md)).
🎯 **That is a bound on what a negative CLAIMS, not a weakness in how a negative is MEASURED**, and the two
must not be collapsed.

---

## 5 · THE SCIATIC NERVE 2×2 — stated precisely, without overclaim

**The background fact, verified and not re-derived.** WWOX protein **is** detected in sciatic nerve of
HD-treated mice — **SIBLING-ATTESTED**, `PMID 42422765` Results, from
[`PMID42422765_partial_locators.md:253`](../research/fulltext_dossiers/PMID42422765_partial_locators.md):

> "WWOX protein was also detected in the sciatic nerve of HD-treated mice (Figures S6E–S6G), thus supporting
> functional relevance in the peripheral nervous system. In contrast, no WWOX expression was detected in the
> liver following either LD or HD treatment"

🔴 **And that positive is not evidence of local transduction.** The sciatic nerve contains **axons of neurons
whose cell bodies sit in spinal cord and DRG**, so the protein is fully explicable by **axonal transport from
a transduced central or ganglionic neuron, with no local transduction whatever**
([`tx007_peripheral_vector_arrival_20260922.md` §3.6(4)](tx007_peripheral_vector_arrival_20260922.md)).
🎯 **That is precisely why the genome measurement is informative rather than confirmatory.**

### 5.1 The four cells

| | **WWOX protein PRESENT** | **WWOX protein ABSENT** |
|---|---|---|
| **vDNA PRESENT** | **③ Local transduction PLAUSIBLE** — delivery and output coincide in this tissue. 🔴 **NOT cell-type resolved:** the genomes may be in Schwann cells, fibroblasts, perineurium or endothelium, and the protein may still be axonal. Co-occurrence in a bulk lysate assigns nothing to any cell | **② DELIVERY OCCURRED; local expression/output is poor or absent** — the vector arrived and the tissue does not make detectable WWOX. 🎯 **Expected under a neuron-restricted `hSynI` promoter: silence in a non-neuronal tissue is the design working, not a failure** |
| **vDNA ABSENT** | **① Consistent with protein TRANSPORTED AXONALLY** from a transduced central or DRG neuron — **NOT local transduction.** 🔴 *"Consistent with"* and not *"demonstrates"*: it excludes local arrival within the assay's limits and leaves transport as the leading remaining explanation, not the proven one | **④ NO LOCAL ARRIVAL within the assay's detection limits** — 🔴 **and only if the LOD is established (§2) and spiked recovery demonstrated (§3.2).** Without both, this cell is not a result at all |

### 5.2 🔴 Four bounds that apply to every cell

1. **The protein axis is weaker than the genome axis.** The sciatic-nerve protein positive is **HD only**,
   **unquantified against WT**, with band intensity spanning **strong to barely detectable across seven
   animals** ([`therapeutic_translation_second_pass.md:591`](therapeutic_translation_second_pass.md)).
   🔴 **It is a detection statement, not a magnitude, and this file does not upgrade it.** **LD was never
   assayed in this tissue at all**, so the 2×2 is an **HD** table and no LD cell exists.
2. **Cell ③ is not cell-type resolution, and no amount of qPCR makes it so.** The only route that assigns
   arrival to a cell type is vector-specific ISH/DNA-FISH on sections — proposal `C1`, the one place where the
   cheaper option is genuinely **not** comparable
   ([`tx007_peripheral_vector_arrival_20260922.md` §6](tx007_peripheral_vector_arrival_20260922.md)).
3. **Cells ① and ④ are conditional on the LOD and on the nerve-specific recovery problem of §3.2** — where
   the achievable template mass may be well below 50 ng, raising the floor.
4. 🔴 **None of the four cells says anything about whether peripheral WWOX is DOING anything.** Presence is not
   contribution, in either direction.

---

## 6 · REVISED COMMUNITY_FOLLOWUP BLOCK

> 🔴 **This is a one-page block for a human to read and decide on. It is NOT an email, NOT a draft message and
> NOT addressed to anyone. Nobody has been contacted and nobody will be by an agent. All outreach is
> `HUMAN_REQUIRED`.**

---

### **EXISTING ASSET**

🟢 **The vector-genome qPCR is already published by the same laboratory, for the same vector, in the same
paper** — forward `5′ GCTCTCTTAAGGTAGCCCCG 3′`, reverse `5′ CGCCTCATCCTGGTCCTAAA 3′`; **50 ng DNA template
per reaction**; **≤25 mg tissue** lysed in **ATL buffer**; **DeNovix DS-11FX+** quantitation
([`cerebellum_layer_localisation_20260922.md:212-215`](cerebellum_layer_localisation_20260922.md), first-hand).
🟢 **Matrix-matched vector-free blanks already exist as animals:** the vehicle-injected `KO+RI` and `WT+RI`
arms. 🟢 **The tissues were necessarily dissected:** 2026 liver (**both arms**), sciatic nerve (**HD**),
spinal cord (**HD**). 🔴 **No sequence is invented; the primer pair is a locator and must be re-read at source
before synthesis.**

### **OPEN QUESTION**

**Did the vector ARRIVE in the periphery and fail to express, or did it never arrive?** The peripheral
negative on record is a **protein** negative; vector genomes were **never quantified outside four brain
regions** in either study. The standing inference — *the vector is not in the periphery, therefore anything
that changes there changes through the brain* — is drawn from an expression assay, and it sits beside a
measured fact: **WWOX protein IS present in sciatic nerve and spinal cord.**

### **MINIMAL EXPERIMENT**

Run the programme's own qPCR on DNA from the already-harvested 2026 **liver, sciatic nerve and spinal cord**,
same plate design, `KO+RI` and `WT+RI` as matrix-matched blanks — **with exactly three additions, and no
others:**

1. 🥇 **Normaliser** — a **single-copy autosomal nuclear** host amplicon: **`Tfrc`**, primers sited so at
   least one lies in **intronic** sequence (a processed pseudogene is intronless, so this is a *structural*
   guarantee, not a literature bet); **`Rpp30`** is the named alternate, preferred if the laboratory already
   runs an AAV copy-number workflow on it. **Amplicon 60–90 bp and length-matched to the vector amplicon**, so
   that fragmentation in fixed/archived DNA cancels in the ratio instead of biasing it. 🔴 **`Gapdh` and
   `Actb` are excluded**: their processed pseudogenes are amplified from a DNA template, inflating the
   denominator and biasing the result toward *"absent"* — the confirmation-shaped direction. 🔴 **No host
   primer sequence is supplied here and none is invented** — the locus and the design criteria are; the
   sequence comes from a validated commercial copy-number assay or an in-house design, checked in silico for a
   single genomic hit and zero hits against vector, plasmid and human `WWOX`.
2. 🥇 **Standard curve** — a **vector-fragment (linearised-plasmid or synthetic-fragment) dilution series run
   in vector-free mouse genomic DNA at 50 ng**, establishing efficiency (90–110 %, R² ≥ 0.99), **LOD** and
   **LOQ**. 🔴 **Absolute copies are NOT required by the question; the LOD is, because without it a negative
   means nothing.** ⭐ One additional column of host calibrant converts the answer into **copies per diploid
   genome** and makes it comparable to the brain panel and to external AAV datasets — take it unless the plate
   is full.
3. 🥇 **Spiked-matrix recovery** — **pre-extraction spike mandatory for LIVER** (inhibitor-rich: haem, iron,
   glycogen, lipid, bile salts; high yield can overload the column; and ABSENT is the *expected* answer there,
   so an inhibited reaction would be silently accepted) **and for SCIATIC NERVE** (low, variable yield; ≤25 mg
   is a ceiling the protocol permits, not a mass this tissue supplies — the 50 ng/reaction specification may
   not transfer, and the LOD must then be restated at the mass actually loaded). 🟢 **Droppable for SPINAL
   CORD** — closest matrix to the validated brain protocol, least informative tissue, and the expected answer
   is PRESENT. ⭐ **Blind spot removed by a pre-stated contingency: a spinal-cord ABSENT triggers a
   retrospective spike before that negative is reported.** 🟢 The host amplicon in every well plus a 50 ng /
   10 ng dilution-parallelism check catch **inhibition** for free in every sample; only the pre-extraction
   spike sees **extraction loss**.

### **NEW ANIMALS?**

🟢 **Potentially NONE** — conditional entirely on material retention. 🔴 **Whether any DNA-bearing 2026
peripheral material still exists is `A-f4`: `HUMAN_REQUIRED`, unknowable from a repository, and not guessed
anywhere in this file.** If the material is gone, the finding is that the question needs **one tissue punch at
a future terminal harvest**, not a new cohort — and **no new arm is proposed here.**

### **EXPECTED OUTCOME BRANCHES**

| Branch | Reading | The bound that travels with it |
|---|---|---|
| 🥇 **ABSENT** (below a stated LOD, at demonstrated recovery) | CNS-restricted **delivery** is promoted from inference to a genome-layer result; the central-control reading of the peripheral rescue stands on firmer ground | 🔴 *"absent at P30"* ≠ *"never arrived"* — episomal genomes dilute with cell division. 🎯 **This is the ROBUST branch:** every uncontrolled confound on the plate biases toward a false POSITIVE |
| **PRESENT + protein ABSENT** | the peripheral negative is reclassified from **biodistribution** to **expression/output**; a neuron-restricted promoter silent in non-neuronal tissue is the construct **working as designed** — a transferable design and safety datum | genomes are not transcripts; assigns nothing to a cell type. Conditionally licenses one cheap next step: peripheral **RT-qPCR** with the already-published transcript primer pair |
| **PRESENT + protein PRESENT** | the CNS-only rescue reading must be re-evaluated **for that tissue** | 🔴 **Spinal cord scores separately** — CNS tissue continuous with the injected compartment; a positive there is a **delivery-extent** result, not a peripheral one. 🎯 **This is the FRAGILE branch:** it needs perfusion status resolved, blanks clean and the calibrant segregated |
| **MATERIAL NOT AVAILABLE** | park with revival triggers | 🔴 **Not a negative result.** It nonetheless answers `A-f4`, which gates several existing-material proposals at once |

🎯 **In the sciatic nerve specifically, the 2×2 is the point:** vDNA **absent** + protein **present** is
consistent with **axonal transport from a transduced central or DRG neuron — not local transduction**; vDNA
**present** + protein **absent** means **delivery occurred and local output did not**; **both present** makes
local transduction plausible but **still not cell-type resolved**; **both absent** means **no local arrival
within the assay's detection limits — and only if the LOD is established.**

### **WHAT IT CHANGES**

It splits **arrival** from **expression** — the one distinction the entire peripheral record currently
collapses into a single word. It is the **only** available measurement that can either confirm or refute
broader biodistribution, and the only one that tests whether *"CNS-restricted rescue"* is a **delivery** fact
or an **expression** fact. 🔴 **It changes nothing about causality, nothing about which cells hold genomes,
nothing about the 2021 arm, and it does not make the periphery a therapeutic target.** It is one plate, on
tissue that already exists, answering a question that was never asked of it.

---

## 7 · What remains `HUMAN_REQUIRED`, and what I could not establish

### 7.1 🔴 `HUMAN_REQUIRED` — no agent may do these

1. 🥇 **Material retention (`A-f4`).** Whether any 2026 peripheral tissue, FFPE/OCT block or extracted DNA
   still exists. **The known gate. Unknowable from a repository, and not guessed.**
2. **Perfusion status of the 2026 DNA tissue.** Stated for RNA only. Only the holding laboratory can answer.
3. **Any contact with the holding laboratory, for any of the above.**
4. **Re-reading the primer pair at the published source before synthesis.**
5. **Every clinical question.** Nothing in this file is medical advice; no molecule, dose or route appears.

### 7.2 🔴 Could not be resolved from available information — stated rather than invented

1. **The host primer SEQUENCE.** No verified `Tfrc` or `Rpp30` mouse primer pair is held in this repository or
   retrievable from repo-held material. 🔴 **None is invented.** The locus, the intronic-siting rule, the
   60–90 bp target and the five validation steps are specified instead.
2. **The vector amplicon's target element and LENGTH.** `METHODS_INVISIBLE` — the paper publishes the
   sequences, not the element. 🔴 **The titration assay's bGH primers must NOT be assumed to be the tissue
   target.** 🟢 **One gel lane closes this**, and it must precede primer ordering, because the host amplicon is
   designed to match it.
3. **The DNA mass actually recoverable from an archived mouse sciatic nerve.** Determines whether 50 ng per
   reaction transfers at all. 🟢 **Closed by weighing the tissue and extracting one control nerve** — free, and
   required before the plate is designed.
4. **Cycling conditions, polymerase, chemistry (probe vs dye), replicates and `n`** for the original assay.
   `METHODS_INVISIBLE`; `n =` → **0 tokens** in the served body. ⇒ **the peripheral extension must state its
   own**, and this file requires that it does.
5. **Whether the 2026 supplementary S6 already contains a peripheral vDNA panel.** Five retrieval routes
   failed. **The one residual way the question could already be answered in print.**

### 7.3 🔴 Undischarged reading debt, listed

`PREMISE: DEFAULT_FROM_TEXTBOOK` for: mouse `Gapdh`/`Actb` processed-pseudogene burden; the field-standard
status of `Tfrc` and `Rpp30` as single-copy copy-number references; FFPE fragment-length behaviour; Poisson
sampling at low copy number; liver as an inhibitor-rich, high-yield matrix; mouse sciatic nerve mass.
🔴 **No conclusion rests on any of them.** Each is used only to choose between design options, and **each is
paired in §1.4, §2.4 and §3.2 with a free in-silico or single-lane bench check that replaces the premise with
a measurement before any reagent is bought.** 🎯 **A design criterion is not a validated reagent, and this
file never treats one as the other.**

---

## Summary for the orchestrator

- **NORMALISER — 🥇 `Tfrc`, primers sited with at least one in intronic sequence; `Rpp30` the named alternate.**
  Requirements met: single-copy autosomal (so `copies ÷ 2` = diploid genomes, no sex term), structurally free
  of processed-pseudogene ambiguity (a processed pseudogene is intronless, so an intronic pair cannot amplify
  one), and **60–90 bp, length-matched to the vector amplicon** so that fragmentation in archived/FFPE DNA
  cancels in the ratio instead of biasing it. 🔴 **`Gapdh`/`Actb` excluded**: their pseudogenes amplify from a
  DNA template, inflate the denominator and bias toward *"absent"* — the confirmation-shaped direction. Also
  excluded: rRNA, mitochondrial, sex-linked, and anything in or near `Wwox` or the transgene. 🔴 **No sequence
  invented — locus plus design criteria only.** 🟢 Bonus: the ratio is **ploidy-robust**, which is the right
  partial answer to polyploid liver (per-cell load remains unmeasured and is reported as such).
- **STANDARD CURVE — absolute quantification is NOT needed; the LOD is, and it is non-negotiable.** Floor: a
  **vector-fragment dilution series in vector-free mouse gDNA at 50 ng**, giving efficiency (90–110 %,
  R² ≥ 0.99), **LOD** (≥95 % detection, Poisson-limited at the bottom ⇒ many replicates) and **LOQ** (CV-based,
  always above the LOD). ⭐ One extra column of host calibrant converts the floor into **copies per diploid
  genome** — ~95 % pre-paid, take it. 🔴 **The curve is not there to quantify a positive; it is there to put a
  floor under a negative.** ⚠️ Honest cost: it introduces a **new false-positive route** (calibrant carryover)
  requiring segregated preparation and a pre-stated void-the-run rule.
- **RECOVERY — 🔴 LIVER mandatory** (haem/iron/glycogen/lipid/bile inhibition; column overload at 25 mg; and
  ABSENT is the *expected* answer there, so an inhibited well would be silently accepted). 🔴 **SCIATIC NERVE
  mandatory**, for yield rather than inhibition — ≤25 mg is a protocol ceiling, not a mass this tissue
  supplies, so 50 ng/reaction may not transfer and the LOD must be restated at the mass actually loaded.
  🟢 **SPINAL CORD droppable**, with the blind spot removed by a pre-stated contingency (a spinal-cord ABSENT
  triggers a retrospective spike before it is reported). 🟢 Free everywhere: the host amplicon as a per-sample
  inhibition sensor plus 50/10 ng dilution parallelism — these catch inhibition but **not** extraction loss,
  which is why the pre-extraction spike is the thing actually being decided.
- **ASYMMETRY preserved.** Residual blood, surface-bound capsid, calibrant carryover and cross-well
  contamination all bias toward a **false POSITIVE**; only extraction failure biases toward a false negative,
  and §3 controls it. ⇒ **a technically validated NEGATIVE is the robust outcome and a PRESENT is the fragile
  one.** 🔴 Perfusion is stated in the source **only for RNA (non-perfused)** and is `METHODS_INVISIBLE` for
  the DNA tissues — assume non-perfused until the laboratory says otherwise.
- **SCIATIC NERVE 2×2** stated in §5.1 with its four bounds: the table is **HD-only** (LD was never assayed
  there), the protein axis is a **detection statement, not a magnitude**, cell ③ is **not cell-type resolved**
  (only ISH/DNA-FISH does that), and cell ④ is a result **only if the LOD is established**.
- **STATUS — the proposal is now EXPERIMENTALLY COMPLETE at the assay layer**, and deliberately no larger. All
  three missing components are specified to the minimum that works, with the droppable one named and its blind
  spot closed by contingency. 🔴 **It is NOT complete at the material layer: `A-f4` — retention — remains
  `HUMAN_REQUIRED`**, together with perfusion status, all outreach, and re-reading the primer pair at source.
  Three sub-problems could not be resolved from available information and are **stated rather than invented**:
  the host primer sequence, the vector amplicon's target and length, and the DNA mass recoverable from an
  archived nerve — 🟢 **and the last two are each closed by one free bench step that must precede ordering.**

*End of file. Scientist A, 2026-09-22. READ-ONLY toward every canonical file; one file written; no commit; no
external contact; nothing here is medical advice.*

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V1 · 🎯 The normaliser finding is the most important line in this file, and it is a CONFIRMATION-SHAPED artefact

The reasoning is sound and checks out on its own terms:

- a **processed pseudogene is reverse-transcribed from mature mRNA and is therefore intronless**, so a
  primer pair sited in **intronic** sequence **cannot amplify one**. That converts pseudogene
  exclusion from a literature bet into a **structural guarantee** — a genuinely better move than
  choosing a locus reputed to be clean;
- `Gapdh` and `Actb` carry many mouse processed pseudogenes, and on a **DNA template** the
  intron-spanning defence that protects them in RT-qPCR **does not exist**;
- therefore exonic primers over-count the host locus, **inflating the denominator**, which
  **deflates** vector-copies-per-genome.

🔴 **And that bias points at "absent" — which is precisely the conclusion the standing peripheral
inference already assumes.** A naive normaliser choice would have manufactured support for the
prior belief through a methodological artefact, in the one experiment built to test it. That is the
most consequential thing in the file, and it would not have been visible without asking which
*direction* the error runs.

The **amplicon length-matching** point is the same class of thinking: in fragmented archival DNA a
longer amplicon is attenuated more, so a **length mismatch between vector and host amplicons turns
degradation into a systematic ratio bias**. Matching matters more than shortness. 🔴 Gated on the
vector amplicon's length, currently `METHODS_INVISIBLE` — closed by one gel lane, before primers are
ordered.

## V2 · 🟠 REFINEMENT — the sex argument is right, for a stronger reason than given

The file justifies an **autosomal** locus partly because *"the cohort contains both sexes."*
Checked at source (`tx007_per_arm_delivery_reconstruction_20260922.md:165`, `:310`): 🔴 **per-arm sex
composition is `UNSTATED`.** The only sex statements in the source are *"both male and female
**HD-treated** mice"* (behaviour) and *"no significant sex-dependent differences observed"* (body
weight).

**The recommendation stands and is strengthened.** The reason is not that both sexes are present —
it is that **the composition is unknown**, so a sex-linked locus could not be copy-number corrected
**at all**, in either direction. An unknown mixture is a worse problem for a sex-linked normaliser
than a known one.

## V3 · The control logic is correctly placed where failure is invisible

**Liver spike mandatory** — because `ABSENT` is the *expected* answer there (both arms
protein-negative), so **an inhibited reaction returns the expected answer and nothing looks wrong.**
That is the correct principle: a control is most needed where failure is indistinguishable from the
anticipated result.

**Sciatic nerve mandatory for *yield*, not inhibition** — `≤25 mg` is a protocol **ceiling**, not a
mass a mouse sciatic nerve supplies, so 50 ng/reaction may not transfer and the LOD must be restated
at the mass actually loaded. An uncontrolled nerve negative would license the axonal-transport
reading **on a failed extraction**.

**Spinal cord droppable**, with the blind spot closed rather than accepted: a spinal-cord `ABSENT`
triggers a retrospective spike **before that negative is reported anywhere**.

## V4 · Two further things done right, and the honest cost

🟢 **The purified vector prep is rejected as calibrant** — its titre was set by a *different* assay
using **bGH** primers, so calibrating against it would silently assume the tissue amplicon is bGH.
That assumption is explicitly forbidden and the file refuses it.

🟢 **The curve's purpose is stated correctly:** *not* to quantify a positive, but **to put a floor
under a negative.** Absolute copies/diploid genome are declared **recommended, not required** —
the smaller answer that actually answers the question.

⚠️ **The upgrade's own cost is disclosed rather than hidden:** a calibrant introduces a
**new false-positive route** (carryover) that the original assay did not have, with segregated prep
and a pre-stated void-the-run rule.

## V5 · Status

**Experimentally complete at the assay layer, and deliberately no larger** — no new tissue, arm,
timepoint or animal. **Not complete at the material layer**, and that is unchanged: retention
(`A-f4`), perfusion status of the DNA tissues, and all outreach remain `HUMAN_REQUIRED`.

🟢 **No host primer sequence was invented.** Locus plus five free validation steps, one of which
(a single genomic BLAT hit) *discharges the pseudogene premise empirically at zero cost* rather than
leaving it as a textbook assumption. Textbook-grade premises throughout are tagged
`PREMISE: DEFAULT_FROM_TEXTBOOK`, carry no conclusion, and are each paired with a free check that
replaces the assumption with a measurement.

LINT `PASS`, growth anchors `PASS`, no new reasoning-layer PMID (only `42422765` and `34747138`,
both queue-covered — verified independently at 7 and 6 hits).
