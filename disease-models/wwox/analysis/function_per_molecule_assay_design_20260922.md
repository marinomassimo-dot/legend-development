# Function per molecule — the assay design for `Q230P` and WWOX missense rescue

**Actor:** Scientist D · **Date:** 2026-09-22 · **Node:** `MECHANISM_WWOX_SDR_FUNCTION_AND_MISSENSE_RESCUE`
**Status:** NON-CANONICAL design file. No registry, queue, ledger, receipt chain, state manifest or
`*_current.md` was read-modified-written by this act. No `BATCH_COMMIT`. No commit, no stage, no push.
**Nothing here is medical advice.** No molecule, dose, route or therapeutic recommendation for any
person appears anywhere below. Genotype classes are held apart throughout.

---

## VERDICT UP FRONT — one assay, named and committed to

> ## 🟢 **RECOMMENDED: a donor-saturation NanoBRET WWOX–partner engagement assay, in which the NanoLuc donor channel IS the abundance denominator.**
>
> **Full name:** *expression-titrated, ratiometric bioluminescence-resonance-energy-transfer
> measurement of WWOX engagement with an SDR-span partner (`POLE4` primary), in live WWOX-depleted
> human cells, with the NanoLuc donor emission from the tagged WWOX molecules serving as the
> same-molecule abundance denominator; `P282A` as the stable-but-inert positive control; a
> WW1-dependent partner as the domain-specificity control; and a soluble/insoluble split on the same
> lysates to qualify the denominator.*
>
> **Why this one and not the others, in one sentence:** every other candidate reads abundance on an
> immunoblot, and the immunoblot floor is the exact instrument that produced *"protein not
> detected"* for `Q230P` — so every other candidate has **no denominator for the allele the question
> is about**, whereas a luminescent donor channel measures that denominator orders of magnitude below
> a blot and turns *"absent"* into a number.
>
> 🔵 **What it honestly measures, named at its true strength and no higher: engagement competence
> per molecule.** It is a fold-integrity-and-partner-engagement readout, **not** a demonstrated
> physiological function, because WWOX has no demonstrated physiological function of any kind
> (`TX-003`; substrate undefined; `PREMISE: NOBODY_LOOKED` on turnover, solubility and aggregation
> for every allele). **That is the ceiling available today, and naming it is part of the
> recommendation.**
>
> 🔴 **The enzymology bridge is CLOSED, deliberately, for the discrimination question** — with one
> element carved out and preserved (§5). The 2011 catalytic assay cannot discriminate any `Q230P`
> mechanism because **it has no denominator**, and an assay with no denominator cannot answer a
> per-molecule question. That is a structural property of the assay, not a fixable detail.
>
> 🟠 **No `HUMAN_REQUIRED` decision packet is needed in place of a recommendation** — the honest
> answer does not require a new research programme. Four **external actions** are nonetheless parked
> as `HUMAN_REQUIRED` (§7); none of them blocks the design.

---

## 0 · Read depth, declared before any finding

| Source | Depth reached by **me**, in this act |
|---|---|
| `PMID 35243249` / `PMC8866893` (Omachi 2022, *iScience*, Alport PTC readthrough) | 🟢 **full body fetched and read — 47 282 characters measured.** The one body I read this session |
| `PMID 41908531`, `39623381`, `39550037`, `38570462`, `35655435`, `32810216`, `32311225`, `28540421`, `40864204`, `40559528` | ⚪ **abstract-depth** — PubMed metadata retrieved by me this session, nothing more |
| `wwox_missense_stability_census_20260922.md`, `q230p_structural_mechanism_20260922.md` | 🔵 **another actor's attestation, this session's branch.** Read by me in full; their contents are their measurements, not mine |
| `missense_rescue_methodology_census_20260921.md`, `wwox_activity_sensor_census_20260921.md`, `mave_portability_to_wwox_20260921.md`, `wwox_sdr_function_per_molecule_census_20260921.md`, `missense_proteostasis_matrix_20260921.md`, `lectin_readout_domain_dependence_20260921.md`, `wwox_missense_cma_degradation_audit_20260921.md`, `CC-20260921-WWOX-ENZYMOLOGY-P306-01.md` | 🟡 **another actor's work on another branch, imported at `b30dfbf`.** Several are **built from abstracts — an abstract is not a read.** Cited as those actors' attestations throughout |
| `PMID 21476439` (the only WWOX enzymology paper) | 🔴 **NOT READ BY ANYONE HERE.** No PMCID, no DOI in the PubMed record, De Gruyter, three independent PMC checks negative (Scientist A's attestation). `PREMISE: UNREAD_PRIMARY` — *owed a reading, not doubted* |
| `PMID 29808465` (the only `Q230P` paper) | 🔴 **NOT READ BY ANYONE HERE.** `pmc_id: null`, `unrecoverable_by_these_routes`. Both `Q230P` data points are `abstract-depth` |
| `PMID 41124647` (the `P252A`/`P282A` paper) | 🟡 **repo-held verbatim**, read by a prior wave. 🔴 **Its variant superscripts were deleted by the extractor** — see the flag in §3.4, which is the most important caveat in this file |

**Bibliographic source of every new record: PubMed.** DOI links are given at first use, as the
retrieval tool's terms require. No figure panel was inspected anywhere in this file.

🔴 **A prediction is never a measurement.** ΔΔG, LLR, pLDDT and SASA are predictions, and the
sibling stability census establishes that this repository's ΔΔG is **inverted** against the six WWOX
measurements that exist. Nothing below rests on a predictor.

---

## 1 · What "function per molecule" requires, stated as measurable criteria

The phrase is used loosely across this repository. Stated as criteria an assay either meets or
fails, it decomposes into **eight**, and **no existing WWOX assay meets more than three**.

| # | Criterion | Measurable test of the criterion | Why it is not optional |
|---|---|---|---|
| **C1** | **A NUMERATOR: a WWOX-dependent output, graded, not binary** | The output must move on WWOX loss **and** move back on WWOX restoration — bidirectional perturbation — and must be shown to respond to *partial* WWOX, not only to presence/absence | A binary output scores nulls. Every WOREE missense question is a hypomorph question. `wwox_activity_sensor_census_20260921.md` § 6.2 item 5 makes this point against the lectin candidate and it generalises |
| **C2** | **A DENOMINATOR that stays linear BELOW the immunoblot floor** | The abundance readout must return a number, with a stated floor in % of wild type, for a construct whose protein is *not detected* by Western blot | 🔴 **This is the criterion that eliminates almost everything.** `Q230P`'s single protein datum is *"protein not detected"* on a blot (Johannsen 2018, `abstract-depth`). An assay whose denominator is a blot has **no denominator for this allele** |
| **C3** | **SAME-MOLECULE attribution** | Numerator and denominator must derive from the same molecular population in the same sample, ideally in the same physical measurement — not two gels with two linear ranges | Otherwise the ratio is an artefact of two calibrations. `CLAIM 030` already records that WWOX abundance measurements across the allelic series are **not commensurable** |
| **C4** | **DOMAIN RESOLUTION, with an internal control that must stay NORMAL** | A second output, known to depend on a **different** domain (WW1), measured in the same experiment, that an SDR lesion should **not** break | 🔴 Published and decisive: `PMID 27869163` — *"a GST-fused SDR fragment did not bind HA-Brca1 (lane 6)"* and the `W44F/P47A`-vs-`Y293F` dissociation (another actor's attestation). **A WW1-dependent assay scores an SDR-mutant protein as normal.** Without the paired control, a flat result cannot be told from assay blindness |
| **C5** | **ABUNDANCE-INDEPENDENCE DEMONSTRATED, not assumed** | The ratio must be shown invariant, or shown to vary in a *fitted and modelled* way, across ≥10-fold wild-type expression — a measured titration, reported | "Matched expression" that was never verified across a range is the failure mode that produced the confound this whole node exists to remove: `PMID 41124647`'s own prose, *"likely due to the **low abundance** of the unstable"* mutant, followed by *"directly correlated"* doing causal work |
| **C6** | **A POSITIVE CONTROL FOR THE DISSOCIATION ITSELF** | The assay must be shown to return *"present but inert"* for a variant known to be stable and dead, and *"absent"* for a variant known to be cleared | 🔴 **`P282A` is not only the brake on this question — it is the assay's positive control.** An assay that cannot reproduce `P282A` cannot be trusted on `Q230P`. `P252A` supplies the opposite pole |
| **C7** | **A DECLARED FLOOR, in molecules or % of wild type** | State the lower limit of the denominator numerically | *"Absent"* and *"2 % of wild type"* are different molecular diseases with different interventions, and the present evidence base cannot tell them apart (Scientist A's `T8`) |
| **C8** | **A DECLARED POOL for the denominator** | State whether the denominator counts soluble, total, or aggregated protein — measured, not assumed | 🔴 **The subtlest criterion and the one nobody has stated.** A denominator that counts aggregated, engagement-incompetent protein **inflates the denominator and manufactures a false "inert" verdict**. Since nobody has ever looked in the pellet for any WWOX allele, this criterion is unmet by construction today — which is precisely where the solubility split earns its place (§4) |

**The compressed statement of the requirement:** *a graded WWOX-dependent output, divided by the
number of soluble WWOX molecules that produced it, both measured in the same sample, on a scale that
survives an allele that a blot cannot see, with a domain control that must stay normal and a
stable-but-dead allele that must score as inert.*

🔴 **Stated that way, it is immediately visible that the binding question and the abundance question
are the same measurement, not two.** That is why §3 recommends one assay and not a programme.

---

## 2 · Candidate assay classes, scored

Scoring is `✅` met, `🟡` partly met or met only with added work, `🔴` failed. **Material availability**
uses the brief's own tiers: **(a)** runnable on material that already exists · **(b)** published,
transferable methodology · **(c)** modest new reagents · **(d)** `HUMAN_REQUIRED`.

| Candidate class | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Material tier | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|---|
| **A · Matched-input co-IP binding panel, SDR partner vs WW1 partner** *(the standing design in `missense_proteostasis_matrix_20260921.md`)* | 🟡 | 🔴 | 🟡 | ✅ | 🟡 | ✅ | 🔴 | 🟡 | **(c)** | 🥈 **RUNNER-UP, and the fallback.** Logic is correct and already specified; **fails C2 fatally** — its denominator is a Western blot, on the one allele a Western blot cannot see. Per-sample, semi-quantitative, and a matched level must be *hit* rather than *fitted* |
| **B · Matched-expression constructs (pick the doses where the bands are equal)** | 🟡 | 🔴 | 🔴 | n/a | 🔴 | n/a | 🔴 | 🔴 | (c) | 🔴 **REJECT as a standalone.** It presupposes you can drive `Q230P` to wild-type level, which is unknown and may be impossible; and "equal bands" at one dose is C5 unverified. It is a *step inside* another assay, not an assay |
| **C · Inducible expression titration** | 🟡 | 🔴 | 🟡 | n/a | ✅ | n/a | 🔴 | 🔴 | (c) | 🟡 **NOT an assay — it is the correct ABSCISSA.** Its value is entirely in what you titrate *against*. Adopted **inside** the recommendation |
| **D · Purified-protein specific activity per mole folded monomer** *(Scientist A's `T1`, SGC orphan-SDR format)* | 🟡 | ✅ | ✅ | 🔴 | ✅ | 🟡 | ✅ | ✅ | **(d)** | 🔴 **REJECT for this question, and I disagree with the sibling census here.** See §2.1 — it is the right answer to a different question, it fails the pruning constraint, and it is blind to the non-catalytic half of the SDR |
| **E · Cellular pathway readout at equivalent protein level** *(Wnt/β-catenin TCF reporter, `PMID 19465938`)* | ✅ | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | **(b)** | 🔴 **REJECT.** Best-validated WWOX-dependence in the whole census (bidirectional: over-expression inhibits, knockdown stimulates) — and **the readout destroys the cell, is several nodes downstream with every node a confounder, and its domain attribution is unknown**, so an SDR lesion may not register at all. C4 unmeetable |
| **F · Ratiometric luminescent engagement with the donor channel as denominator** *(modernised from Scientist A's `T9`)* | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | **(c)** | 🥇 **RECOMMENDED — §3** |
| **G · Solubility split (soluble supernatant + resuspended SDS pellet, same membrane)** | 🔴 | 🔴 | n/a | 🔴 | n/a | 🔴 | 🔴 | ✅ | **(a)** | 🟢 **RUN IT — but it is not this assay.** It is the **only** candidate at tier (a), it decides the aggregation branch, and it is the **prerequisite that makes C8 meetable**. It is not a function assay and cannot be reported as one. §4 |
| **H · MAVE / VAMP-seq abundance map ± function** | — | — | — | — | — | — | — | — | — | ⛔ **PRUNED, not scored.** A materially new research programme and the Operator's decision. The sibling census says so explicitly and this file holds that line |
| **I · A single-cell fluorescent WWOX activity sensor** | — | — | — | — | — | — | — | — | — | ⛔ **PRUNED, not scored.** Same reason. **None exists** (sibling census, 24 queries) and building one is the programme, not the assay |

### 2.1 🔴 Where I disagree with a sibling census, and why — the purified-protein route

`wwox_sdr_function_per_molecule_census_20260921.md` § 8 names **"deorphanise the WWOX SDR domain"**
as *"the single cheapest missing experiment"* and grades the SGC protocol *"Low cost — standard
enzymology."* **I reach a different verdict for the question I was asked, and the disagreement is
about the question, not about the science.**

Four reasons, in order of weight:

1. 🔴 **It fails the pruning constraint.** Express → purify → report yield/Tm/monomer fraction →
   substrate screen → kinetics → triad controls → then alleles is **six sequential unsolved steps**,
   the first of which is conceded new: *"even the field's structural-biology group has only ever
   purified WW fragments"*. The only WWOX biophysics in existence covers **residues 16–91**
   (`PMID 35716775`, [DOI](https://doi.org/10.1016/j.jbc.2022.102145), another actor's attestation).
   By the same standard that correctly prunes a MAVE and an activity sensor, **a de-novo
   deorphanisation of an orphan enzyme is a research programme.** It is the Operator's decision, not
   an assay recommendation.
2. 🔴 **It is blind to the half of the SDR that the disease most plausibly runs through.** The
   repository's own `DL-MECH-019` records a *"funzione non catalitica di scaffold/anti-aggregazione"*
   in the SDR, and `PMID 27869163`'s `Y293F` shows at least one WWOX function is **indifferent to
   SDR catalysis**. A catalysis-only readout scores a fold-competent-but-catalysis-dead protein and a
   catalysis-competent-but-engagement-dead protein identically — and `P282A`, the one allele that
   defines this question, has never been shown to be catalytically dead.
3. 🟡 **`Q230P` is not predicted to be a catalytic lesion.** Scientist B's geometry, re-measured
   independently by the Orchestrator: **12.60 Å** from the cofactor-cleft axis, **10.01 Å** from
   `TGANSGIG`, S281 **6.79 Å**, Y293 **9.37 Å**, K297 **9.68 Å**, side chain **141°** away from
   Y293-OH. Verdict **NOT cofactor, NOT substrate pocket**. So a catalytic readout would report this
   allele only *indirectly*, through folding — which a cellular engagement readout reports more
   directly and in a mammalian compartment.
4. ⚠️ **The direction of the reaction is unresolved and an assay must choose one.** The 2011 primary
   reports **oxidation only** (*"with the same substrates and reduced cofactors (NADH and NADPH)
   reduction activity was not observed"*); a 2015 review proposes a **reversible** retinal
   oxidoreductase. `CC-20260921-WWOX-ENZYMOLOGY-P306-01` records that *"they disagree on
   reversibility, which is the one property an assay design must choose, and no experiment has ever
   been run that could tell them apart."* **You cannot design the assay before that is settled.**

**What I keep from that census, without reservation:** its conclusion that a WWOX catalytic assay
with controls would be transformative; its `T8` (absolute quantification) as the right way to state
C7; its `T9` as the germ of the right answer; and `C-2`, its narrowing of the earlier
*"it is not anywhere"* overclaim. **My disagreement is one of ranking against a constraint, and the
constraint was given to me and not to it.**

---

## 3 · THE ONE RECOMMENDED ASSAY

### 3.1 The design, in one paragraph

**Place a NanoLuc donor on WWOX and a HaloTag acceptor on an SDR-span partner; express the WWOX
donor from a doxycycline-titratable promoter in a WWOX-depleted human cell line; and for each allele
build a full curve of BRET ratio against donor luminescence across a ≥10-fold expression range.**
The donor emission counts the WWOX molecules; the acceptor/donor ratio reports what fraction of them
are engaged. Fit each allele's curve and compare the **fitted, expression-independent parameters**
(BRET<sub>max</sub> and the half-maximal donor:acceptor ratio) rather than comparing single wells.
Run the same plate against a **WW1-dependent partner** as the domain control that must stay normal,
and include **`P282A`** (stable, engagement-dead), **`P252A`** (cleared), **wild type** and
**`L404A`** as the four controls that calibrate the scale. Then repeat the plate under the two
abundance-raising conditions — **30 °C** and **chloroquine** — and ask the only question that
matters therapeutically: *when the abundance of `Q230P` is raised, does its engagement per molecule
rise with it, or does the curve stay flat?*

### 3.2 Why each element is there, and what it buys

| Element | Why | Criterion it satisfies |
|---|---|---|
| **NanoLuc donor on WWOX** | Luminescence spans orders of magnitude and has no autofluorescence background. It converts *"not detected on a blot"* into a **number**, and that number is the denominator | **C2, C7.** 🔴 The single reason this design exists |
| **BRET (energy transfer), NOT split-complementation** | 🔴 **A deliberate choice against the sibling census's `T9`.** Split reporters (NanoBiT: LgBiT + SmBiT) carry **intrinsic affinity between the two tags**, which can rescue a weakened interaction and can stabilise the tagged protein — i.e. the reporter can mask the exact defect being measured. BRET adds no affinity between donor and acceptor | **C1, C6** integrity |
| **Ratio, not difference** | The BRET ratio is acceptor/donor from the **same photons-producing molecules**, in one well, in one read | **C3** |
| **Donor-saturation TITRATION and curve fitting** | 🔴 **This is the abundance control, and it is the part that is usually got wrong.** A BRET ratio is *not* automatically expression-independent — at donor excess a smaller fraction of donors finds a partner, so the raw ratio falls with expression. What *is* expression-independent is the **fitted BRET<sub>max</sub>** (the ratio at acceptor saturation) and the **BRET<sub>50</sub>**. **Fitting the curve converts the abundance confound into the x-axis instead of pretending it away** | **C5**, and it is the reason candidates **B** and **E** fail |
| **WWOX-depleted host cell** | Endogenous WWOX competes for partners and dilutes the signal, and its own level varies | **C1** attribution |
| **A WW1-dependent partner on the same plate** | An SDR lesion must leave it normal. If both outputs fall together, the protein is globally unfolded or the tag is broken — **a different finding, and one this design can report rather than mistake** | **C4** |
| **`P282A` on every plate** | Must read **engagement-dead at normal donor signal**. If it does not, the assay is not sensitive to the lesion class and nothing else on the plate means anything | **C6** — the go/no-go gate |
| **30 °C arm** | A published, reagent-free folding-rescue lever: the Parkin atlas reports that *"at 29 °C the low abundance peak almost disappeared entirely and most variants now appeared stable"* (`PMID 38378758`, another actor's locator `L-10`; the authors hedge with *"Presumably"*) | The **rescue** half of the question |
| **Chloroquine arm** | The published in-culture condition that restored a WWOX missense band (CQ 40 µM / 24 h, `PMID 41124647`) — an orthogonal second route to a raised level. ⚠️ Lysosomotropic and lysosome-wide; **never the only route to level-matching** | Second, independent rescue route |
| **Soluble/insoluble split on the same lysates** | States which pool the denominator counted | **C8** — §4 |

### 3.3 The partner choice, and the flag that must travel with it

**Primary numerator: `POLE4` engagement.** The reason is specific and it is the strongest
single argument available: **`POLE4` binding is the only WWOX readout in the entire literature
that has been reported to fail in an SDR-span missense protein *that had no stability defect*.**
It is therefore the one candidate numerator with a demonstrated **abundance-independent** failure —
which is the property C6 requires and which no other WWOX readout has. `POLE4` is also ~117 aa,
so a tagged construct is trivial, unlike BRCA1.

🔴 **FLAG FIRST — and this flag is the single most load-bearing caveat in this file.**
The `P282A` → loss-of-`POLE4`-binding attribution rests on a **body whose variant superscripts were
deleted by the text extractor.** Two repository files independently reconstruct it as `P282A`
(`wwox_missense_cma_degradation_audit_20260921.md` § *"For **P282A**, by contrast, function is lost
without a stability defect … mechanistically attributed to loss of POLE4 binding"*, and
`therapeutic_hypotheses_ledger_current.md:414`), and the proteostasis matrix quotes
*"the WWOX[?]mutant protein was not able to bind to POLE4"* with the label stripped. **The
reconstruction is probably right and I have not verified the label.** `PREMISE: UNVERIFIED` at the
label level. Three further bounds ride with it, all already on the repository's books:

1. ⚠️ **The paper's own two statements differ in strength.** Abstract: *"POLE4 … interact with WWOX,
   but not with the WWOX[?]mutant."* Results: the mutant *"**appeared to** lose its interaction with
   POLE4."* Take the Results wording as the bound.
2. 🔴 **`POLE4`'s functional relevance is conceded unproven by the authors**: *"the functional
   relevance of WWOX-POLE4 interaction in nucleotide excision repair remains to be elucidated"*, and
   **no NER assay is performed in that paper.** So this is **engagement**, not demonstrated function
   — `D-04` applies in full: *a binding readout may be reporting occlusion rather than function.*
3. ⚠️ **The same paper's `P252A` `POLE4` result is explicitly confounded by abundance** by the
   authors themselves — *"likely due to the low abundance of the unstable"* mutant. **That confound
   is the disease this assay is built to cure**, and its presence in the source is the reason the
   titration is non-negotiable.

**Verification owed BEFORE the first construct is ordered:** re-read `PMID 41124647`'s `POLE4`
figure and its panel labels and confirm which variant lost the interaction. **If the label resolves
to `P252A` rather than `P282A`, the numerator loses its abundance-independent credential and the
primary partner must change** — to **tau** or **GSK3β** (SDR-span-mapped via `DL-MECH-019`;
`CLAIM 035` gives GSK3β residue resolution at 388–407 with `L404` strictly necessary, and records
that **no WWOX-DEE allele was ever tested**). **`FLAG FIRST. SCORE ONLY AFTER MECHANISM + REAGENT +
ALLELE VERIFICATION.`** No score is assigned to this assay's expected result here.

**Secondary/confirmatory SDR numerator:** tau or GSK3β, same format, same plate. **This is one assay
with its controls, not a panel of assays** — one construct architecture, one instrument, one read.

### 3.4 What it discriminates — the discrimination table

| Observation on the plate | Mechanistic reading | Therapeutic consequence |
|---|---|---|
| `Q230P` donor signal **unmeasurable even at maximal induction**, wild type fine | The protein cannot be accumulated at all in this system — **synthesis/folding-yield ceiling** | 🔴 An abundance-raising strategy has nothing to act on. Stop, and go to the synthesis arm |
| `Q230P` donor signal **low but measurable**; curve **superimposable on wild type** after fitting | **ABUNDANCE-ONLY lesion. Engagement per molecule intact** | 🟢 The one result under which restoring abundance is on-mechanism. **It is also the only result that would license the boost axis, and it has never been obtained for any WWOX allele** |
| `Q230P` donor signal restored at 30 °C or under CQ, but curve **stays flat** | 🔴 **STABLE-BUT-INERT — the `P282A` outcome at this allele.** Abundance restored, engagement not | 🔴 **An abundance-only rescue readout would have called this a success.** The boost axis fails for this allele on its own merits |
| Both SDR **and** WW1 numerators fall together | Global misfolding, or a broken tag | Re-pilot the tag; **do not report a domain result** |
| Donor signal present, but the soluble/insoluble split shows the donor mass in the pellet | 🔴 **Denominator was counting aggregated protein.** C8 violated; the "inert" verdict is an artefact | 🔴 **And an aggregation branch makes a non-allele-specific boost dangerous** — stop the boost axis, regardless of the BRET result |
| `P282A` reads **normal** engagement | 🔴 The assay is insensitive to the lesion class | **Discard the plate.** Nothing on it is interpretable |

🔵 **The compression claim, made honestly.** One construct architecture, one instrument, one plate
series delivers: **absolute-scale abundance per allele** (donor channel, calibrated) · **engagement
competence per molecule** (fitted BRET<sub>max</sub>) · **domain resolution** (paired partner) ·
**folding-rescuability with function measured at the rescued abundance** (30 °C and CQ arms) ·
and, on the same lysates, **the soluble/insoluble partition**. **That is four of the brief's
candidate classes collapsed into one measurement.** ⚠️ **And one thing it does not do: it does not
replace the solubility split on patient fibroblasts, which is a different question on different
material** (§4).

### 3.5 What it cannot do — stated as hard limits, not as caveats

1. 🔴 **It is not a physiological function assay.** WWOX has no demonstrated physiological function,
   no assigned substrate and no validated cellular activity readout. **Engagement competence is a
   proxy**, and `D-04` stands. A paper reporting this assay must call it what it is.
2. 🔴 **It measures a tagged, over-expressed transgene, not the endogenous allele.** The synthesis
   rate is set by the vector. ⚠️ **This is the correct trade and it must be argued rather than
   hidden: over-expression is a confound for the *abundance* question and an ENABLER for the
   *per-molecule* question** — to control abundance you must be able to *set* it, and only a
   titratable heterologous system lets you. The endogenous question stays with §4.
3. 🔴 **The tag may break WWOX.** WWOX is Golgi/membrane-associated and partly mitochondrial;
   `RISK 1` in `mave_portability_to_wwox_20260921.md` § 6.A is unresolved, and a 2026 group reported
   that *"commercial anti-WWOX antibodies did not show any specific signal for IF prompting us to use
   a myc-WWOX"* — so even the antibody floor under this protein is weak. **Mandatory pilot: N- and
   C-terminal donor placements, tested against localisation and against wild-type engagement,
   before any allele is scored.** The published precedent that makes this non-optional is in §6.
4. 🔴 **Nothing about neurons, myelination, the developmental window, seizures or clinical course.**
   Every host cell available for this is a proliferating line.
5. 🔴 **It cannot measure catalysis** (no substrate), **cannot measure half-life as a number**
   (needs the CHX chase), and **cannot measure aggregation of the endogenous protein**.
6. ⚠️ **A flat curve has two readings** — inert protein, or an engagement that was never
   SDR-fold-dependent in the first place. **The published standard of proof for the second is set out
   in §6 transfer T-4 and WWOX does not meet it today.**

### 3.6 What would make me prefer a different assay — falsifiers of this recommendation

| # | Observation | New recommendation |
|---|---|---|
| **1** ⭐ | The `POLE4` panel label in `PMID 41124647` resolves to **`P252A`**, not `P282A` | Numerator loses its abundance-independent credential → switch primary partner to **tau/GSK3β**, and demote the whole design one confidence step (no WWOX readout would then have a demonstrated abundance-independent failure) |
| **2** ⭐ | The tag pilot shows **either terminus** of NanoLuc-WWOX mislocalises the protein or abolishes wild-type engagement | Fall back to **candidate A** — matched-input co-IP with small epitope tags — accepting its C2/C7 failure, and pair it with targeted MS (`T8`) to supply the denominator a blot cannot |
| **3** | Someone reads `PMID 21476439` and it reports **purified** enzyme with a **catalytically-dead triad control** and a settled reaction direction | The enzymology route becomes a real function assay → recommend **purified-protein specific activity per mole folded monomer** (candidate D), which meets C1–C3 and C5–C8 outright |
| **4** | A WWOX SDR construct is shown to express **soluble and monodisperse** with a reported yield, Tm and monomer fraction | Same as #3 — the tier-(d) barrier under candidate D falls |
| **5** | `WWOX` turns out to be in the **OpenCell endogenous split-mNeonGreen2 library** (a web lookup; the sibling census flags it as *"the single highest-value unresolved check"*) | An endogenously tagged per-cell abundance line already exists → use it as the denominator and drop the transgene for the abundance half |
| **6** | A published experiment establishes an **SDR-catalysis-dependent cellular readout** for WWOX (catalytic-site **and** cofactor-site point mutants both abolishing it — the ENV9 standard, §6 T-4) | That readout becomes the numerator and outranks engagement, because it would be a demonstrated **function** rather than a proxy |

---

## 4 · Where the solubility split sits — honestly

> ## 🟢 **RUN IT. FIRST. AND DO NOT CALL IT A FUNCTION ASSAY.**

**What it is:** lyse `Q230P` patient-derived fibroblasts in a non-denaturing buffer, spin, and blot
the **soluble supernatant and the resuspended SDS pellet on the same membrane at the same
exposure.** One extra lane. The design belongs to the sibling stability census § 9.1 arm 1 and I
adopt it unchanged.

**Its four honest properties, and none of them is negotiable:**

| Property | Assessment |
|---|---|
| **Cheapest and only tier-(a) candidate** | ✅ Existing material, existing reagents, ~1 day. **The only item in this file that needs nothing new** |
| **It decides the aggregation branch** | 🟢 **Protein in the pellet ⇒ insoluble/aggregating ⇒ a non-allele-specific boost is actively dangerous and the axis stops there.** No other single measurement in this node can stop a therapeutic axis by itself |
| **It is NOT a function assay and does not satisfy function per molecule** | 🔴 **Fails C1 outright — it has no numerator at all.** It measures where protein is, not whether protein works. Reporting a pellet-vs-supernatant blot as evidence about function would be the precise error `P282A` exists to prevent |
| **It is a PREREQUISITE of the recommended assay, not a competitor** | 🔵 **This is the placement that I think has been missed.** C8 says the denominator must declare its pool. A denominator that silently counts aggregated, engagement-incompetent protein **inflates the denominator and manufactures a false "stable but inert" verdict** — the exact wrong answer, arrived at rigorously. **So the split is what makes the recommended assay's denominator interpretable.** It runs on the same lysates inside the design (§3.2) *and* on patient fibroblasts outside it |

**Where it sits, in one line:** **the split answers the ENDOGENOUS question (is the patient's protein
in the pellet?) and it answers it about the real allele in the real cell; the recommended assay
answers the PER-MOLECULE question (when protein is present, does it work?) and it can only answer it
in a system where abundance can be set.** They are complements. **Only the second answers the
question I was asked** — and 🔴 **only the first can stop the therapeutic axis**, which is why it
goes first in time even though it ranks second in relevance.

⚠️ **One bound the split cannot escape:** it needs `Q230P` patient-derived fibroblasts, and their
availability is not established in this repository. That is a `HUMAN_REQUIRED` item (§7), not an
assumption. `PREMISE: UNVERIFIED` on material availability.

---

## 5 · The enzymology bridge — element by element, then closed

**The question asked, exactly:** *can any element of the historical WWOX catalytic assay
(`PMID 21476439`, Sałuda-Gorgul / Bednarek 2011) be repurposed into a modern assay that
DISCRIMINATES between the `Q230P` mechanisms?* No assumption of physiological-substrate validity,
disease-allele applicability, mammalian-cell validity or function-per-molecule validity.

**The `Q230P` mechanisms to be discriminated are four**, and they must be named before any element
is judged: **(i)** reduced synthesis / co-translational folding yield · **(ii)** insolubility /
aggregation · **(iii)** accelerated turnover · **(iv)** present, stable and inert (the `P282A`
outcome). All four are `PREMISE: NOBODY_LOOKED` for this allele.

### 5.1 The element inventory, and the verdict on each

| Element | What the abstract reports | Can it discriminate (i)–(iv)? | Verdict |
|---|---|---|---|
| **E1 · Heterologous expression route** — *"using **two bacterial expression systems**, we have cloned WWOX fusion proteins"* | A route by which WWOX constructs were expressed and yielded activity in lysate | 🟢 **PARTIALLY YES — and it is the only element that can.** A heterologous host has **no lysosome and no ubiquitin-proteasome quality control of the mammalian kind**, so a soluble-vs-inclusion-body partition of wild type against `Q230P` in the same host **separates intrinsic folding/solubility (i, ii) from host-specific clearance (iii)** — which no mammalian assay can do, because in a mammalian cell the two are entangled by construction | 🟢 **PRESERVE.** §5.2 |
| **E2 · Crude-extract activity readout** — *"oxidoreductase activity in a **crude extract**"* | A spectrophotometric cofactor-cycling rate in unfractionated lysate | 🔴 **NO, and the reason is structural.** The assay has **no denominator.** Activity ↓ is equally consistent with less protein, insoluble protein, degraded protein and inert protein — i.e. with **all four mechanisms at once.** An assay with no denominator cannot answer a per-molecule question, and adding one requires purified protein, which is precisely the tier-(d) barrier | 🔴 **CLOSE** |
| **E3 · Steroid substrate panel** — *"a course of enzymatic reactions for **selected** steroid substrates"* | A defined candidate-substrate set | 🔴 **NO.** The substrates were *selected on a prior hypothesis* (*"Due to its potential role in sex-steroid metabolism"*) — **not discovered.** The field declined to adopt them: the Adelaide review, ten years later, states *"the substrate and product of the enzyme reaction that it catalyses are yet to be discovered"*, and an unrelated 2025 paper restates it (another actor's locators `L-3`/`L-5`) | 🔴 **CLOSE** as a readout; 🟡 keep as a *starting set* if and only if candidate D is ever opened |
| **E4 · Km values** | Kinetic constants | 🔴 **NO.** A Km on wild-type protein in crude extract with no dead-enzyme control is a property of *a lysate*, not of a molecule. **And the numbers are unread** — the body is unreachable | 🔴 **CLOSE** |
| **E5 · Cofactor directionality** — NAD⁺/NADP⁺ reactive, *"with … NADH and NADPH reduction activity was not observed"* | A direction | 🔴 **NO — and it is worse than neutral: it is in open conflict.** A 2015 review proposes a **reversible** retinal oxidoreductase. **They disagree on the one property an assay must choose, and no experiment has ever been run that could tell them apart.** ⚠️ Also, *"reactive both in the presence of NAD⁺ and NADP⁺ for **all** examined steroid substrates"* is what unsubtracted *E. coli* dehydrogenase background looks like as much as what a promiscuous SDR looks like | 🔴 **CLOSE** |

### 5.2 🔴 A correction owed to the record, which is the substantive finding of this section

Two statements this repository currently holds simultaneously are in tension:

- **Established fact, from the sibling stability census § 3.4:** *"The SDR domain has never been
  expressed or purified by anyone"* — resting on `PMID 35716775`, whose constructs are **residues
  16–91** only.
- **The 2011 abstract (`L-1`, another actor's locator):** *"using **two bacterial expression
  systems**, we have cloned WWOX fusion proteins **showing oxidoreductase activity in a crude
  extract**."* Activity in a lysate implies **soluble, folded, active protein in that lysate.**
- **And a third datum, repo-held from `PMID 27869163`:** *"a **GST-fused SDR fragment** did not bind
  HA-Brca1 (lane 6) and does not contain either WW domain."* **A GST–SDR fragment was expressed and
  used in a pull-down.**

> 🔵 **The narrowed statement that survives all three: no *purified*, *folded*, *biophysically
> characterised* WWOX SDR protein exists — no reported yield, no Tm, no monomer fraction, no
> monodispersity — but *heterologous expression* of WWOX constructs containing the SDR has been
> reported at least twice. "Never been expressed" is too strong; "never been purified and never been
> characterised" is exact.**

**Why the correction matters and what it does NOT license.** It moves the cost of any
purified-protein route from *"an unsolved problem"* to *"unreported but twice attempted"* — which is
a real change in the cost estimate under candidate D and falsifier #4. ⚠️ **It licenses nothing
more.** Neither report gives a yield, a purity, a monomer fraction or a Tm; neither claims
purification; the 2011 construct **boundaries are unread** (the abstract says *"WWOX fusion
proteins"*, not which fragment); and a GST fusion used as bait in a pull-down is not evidence of a
folded, monodisperse SDR. `PREMISE: UNREAD_PRIMARY` on the 2011 route; `repo-held, another actor's
attestation` on the GST fragment.

### 5.3 The closure, stated cleanly

> ## 🔴 **The catalytic readout route is CLOSED for the `Q230P` discrimination question.**
>
> **Five independent reasons, each sufficient on its own:**
> 1. **No denominator.** A crude-extract rate cannot be divided by a number of folded molecules, so
>    it cannot discriminate *inert* from *absent* — which is the entire question.
> 2. **No attribution.** *E. coli* lysate carries endogenous NAD(P)-dependent dehydrogenases; there
>    was **no catalytically-dead triad control** (`S281A / Y293F / K297A` exist only as *"Aldaz
>    laboratory unpublished observations"*, read out by **localisation**, with no data shown).
> 3. **Wrong lesion class for this allele.** Measured geometry puts `Gln230` **12.60 Å** from the
>    cofactor-cleft axis and **6.79–9.68 Å** from the triad, side chain **141°** away from Y293-OH:
>    **NOT cofactor, NOT substrate pocket.** A catalytic readout reports this allele only
>    indirectly, through folding.
> 4. **The reaction direction is unresolved** between the 2011 primary and a 2015 review, and an
>    assay must choose one.
> 5. **The method is unread.** No PMCID, no DOI in the record, publisher egress blocked, three
>    independent PMC checks negative. **You cannot modernise a method nobody has read.**
>
> 🟢 **What survives closure, and it is not nothing: E1.** The heterologous-expression route is the
> one element with genuine discriminating power, because a host without mammalian quality control
> separates *intrinsic* folding failure from *cellular* clearance. **It is preserved as the minimum
> modernisation of E1 only** — *express wild type and `Q230P` SDR constructs side by side in one
> heterologous host and blot the soluble fraction against the inclusion-body pellet, with no activity
> readout at all* — which is **tier (c)**, needs no substrate, needs no purification, and answers a
> question no mammalian experiment can. ⚠️ **What does NOT transfer from it: bacterial folding is
> not mammalian folding**, there are no chaperones of the human kind, no Golgi, no post-translational
> modification; a `Q230P` that partitions soluble in *E. coli* has **not** been shown to fold in a
> neuron. It is a **prior**, at best — and it is strictly a ranked-second companion to §3, never a
> substitute for it.
>
> 🔵 **A clean closure is a real result**, and it is the correct output here: the honest reading is
> that the 2011 paper is *owed a reading* (`PREMISE: UNREAD_PRIMARY` means owed, **not** doubted) and
> that its **activity** is not the bridge. Its **expression route** is.

---

## 6 · Analogical transfers — method, pattern and assay only, never a disease conclusion

🔴 **NOT ONE DATUM IN THIS SECTION IS ABOUT WWOX.** Every row states what transfers and what does
not. According to PubMed, the records in rows T-1 to T-5 and T-11 were retrieved by me in this act
at the depth declared in § 0; rows T-6 to T-10 are **carried from sibling files as those actors'
attestations**, at the depth those files declare (mostly `abstract-depth`).

| # | Source | WHAT TRANSFERS | WHAT DOES NOT |
|---|---|---|---|
| **T-1** ⭐ | **`KCNJ2` p.Glu293Lys, Andersen–Tawil syndrome.** Déri 2021, *Cardiovasc Res* 117(8):1923–34, `PMID 32810216`, `abstract-depth`, [DOI](https://doi.org/10.1093/cvr/cvaa249). A disease missense at a **cytoplasmic-domain interface**, assayed by **NanoBiT split-reporter subunit co-assembly**, with **two tag topologies**: *"Reporter constructs carrying NanoBiT tags on the intracellular termini produced no bioluminescent signal above background with the p.Glu293Lys variant … Extracellularly presented reporter tags, however, generated comparable bioluminescent signals"* | 🟢 **The design pattern and its most important control.** (a) A split/ratiometric luminescent reporter *can* resolve an assembly/engagement defect caused by a single disease missense. (b) 🔴 **Tag topology determines the answer** — the same variant scored *dead* with one placement and *normal* with another. **This is why §3.5 item 3's two-terminus pilot is mandatory and not a formality.** (c) They combined interaction + localisation + a functional endpoint — the compression pattern | 🔴 An ion channel, a tetrameric membrane protein, a cytoplasmic-domain **interface** lesion with a dominant-negative effect and a salt-bridge network. **`Q230P` is SASA 0.00 Å², fully core-buried, and NOT an interface residue** (topology-independent exclusion). No `KCNJ2` result says anything about WWOX, and the dominant-negative framing must not be carried across |
| **T-2** ⭐ | **Alport syndrome PTC readthrough.** Omachi 2022, *iScience* 25(3):103891, `PMID 35243249` / `PMC8866893`, 🟢 **full body read by me — 47 282 chars**, [DOI](https://doi.org/10.1016/j.isci.2022.103891). **Two reporters on the same variant set:** *"a NanoLuc-based **translation reporter** system to evaluate which nonsense variants are susceptible to readthrough"*, and then *"a **split-NanoLuc-based** collagen IV α3α4α5 **heterotrimer formation assay** … measuring the luminescence produced by the proximity of NanoLuc fragments"*. Their stated motive: *"If such a substitution impairs the function of the protein, **it may be difficult to rescue the variant phenotype even if a full-length protein is produced**"* | 🟢 🔴 **THE PATTERN, and the closest structural analogue of the WWOX question in the literature.** A rare inherited disease asked *"if our therapy restores the protein, is the restored protein functional?"* and answered it with **an amount reporter plus an orthogonal assembly reporter, in the same luminescent system, on the same variants** — and found that some products *"retained the ability to form α3α4α5 heterotrimers"* while others did not. **That sentence of theirs is the WWOX brief's premise written by someone else, four years earlier, and then answered experimentally.** Also transferable: they read the output **intracellularly and extracellularly**, i.e. in two compartments | 🔴 Collagen IV, a secreted obligate heterotrimer with an assembly step that is itself the disease mechanism; nonsense variants and readthrough drugs, not a buried missense; and their normalisation was to *"constitutively expressed firefly luciferase"* — a **transfection** normaliser, **not a per-molecule denominator**. 🔴 **No Alport conclusion, no readthrough conclusion, and nothing about WWOX's partners transfers** |
| **T-3** | **Alport VUS scored by NanoBiT for clinical interpretation.** Cai 2026, *Front Pediatr* 14:1706611, `PMID 41908531`, `abstract-depth`, [DOI](https://doi.org/10.3389/fped.2026.1706611). 31 patient VUS, HEK293T, *"luminescence intensity of all 31 plasmids carrying VUS … reduced by more than 50% compared with the WT plasmid"*, sensitivity 96.77 %, specificity 100 % | 🟢 That a split-luciferase interaction readout is **mature enough to be proposed for clinical variant interpretation** — i.e. the methodology tier is (b), published and transferable, not experimental. It also shows the **effect sizes are large** (>50 %) and therefore detectable | 🔴 **AND IT IS THE CAUTIONARY CASE.** On the abstract, **no abundance denominator is described**: a variant whose plasmid simply makes less protein would read as *"reduced luminescence"* and be scored as functionally impaired. 🔴 **That is exactly the failure mode this file's C2/C5 exist to prevent, in a paper published this year.** ⚠️ `abstract-depth` — the body may contain a normaliser I have not seen; the criticism is of what the abstract states, not a verdict on the paper |
| **T-4** ⭐ | **`ENV9`, a yeast SDR orthologous to human `RDH12`.** Siddiqah 2017, *Curr Genet* 63(6):1053–72, `PMID 28540421`, `abstract-depth`, [DOI](https://doi.org/10.1007/s00294-017-0702-y). *"Similar site-directed point mutations in the predicted Env9 **oxidoreductase active site (N146L)** or **cofactor-binding site (G23-24A)** abolished its reductase activity in vitro … **The same residues were essential for affecting LD size and number in vivo**"* | 🟢 **THE STANDARD OF PROOF for calling a cellular readout SDR-dependent**, and WWOX does not meet it. To claim a cellular output reports SDR function, you must show that **both** an active-site **and** a cofactor-site point mutant abolish it — *in vitro* and *in vivo*. 🔴 For WWOX the equivalent evidence is **one unpublished observation** (`S281A/Y293F/K297A` → perinuclear localisation, *"Aldaz laboratory unpublished observations"*, no data shown, readout = localisation), against a **published** WW1-routed alternative. This is why §3.5 item 6 is a hard limit and why falsifier #6 exists | 🔴 Yeast; lipid droplets; `RDH12`/Leber congenital amaurosis; a *reductive* direction. **No WWOX substrate, no WWOX phenotype and no disease conclusion transfers.** And the *"predicted"* active site is theirs, by homology |
| **T-5** | **`ACKR4` C-terminal tagging.** Gerken 2024, *Cell Commun Signal* 22(1):576, `PMID 39623381`, `abstract-depth`, [DOI](https://doi.org/10.1186/s12964-024-01961-8). *"Addition of a C-terminal tag **selectively** affected the function of ACKR4, but not other ACKRs … led to a shift from a βarrestin-dependent towards a βarrestin-independent endocytosis pathway"* | 🟢 **A published, quantified instance of a tag silently changing the biology of one protein and not its close relatives** — the concrete evidence that `RISK 1` is real and **cannot be reasoned away by precedent from other proteins.** Transfers as an obligation: pilot the tag on *this* protein, with a localisation and a function check, before scoring any allele | 🔴 A GPCR, βarrestin recruitment, chemokine scavenging, a PDZ-binding C-terminal motif. **Nothing about WWOX's tolerance of a tag is established by it** — it establishes only that the question must be asked |
| **T-6** | **11β-HSD2 (`HSD11B2`), apparent mineralocorticoid excess.** Atanasov 2007, `PMID 17314322`, **another actor's attestation, `abstract-depth`**, [DOI](https://doi.org/10.1681/ASN.2006111235). WT `t½` **21 h** → Tyr338His **3 h**, Arg337His **4 h**; activity partly retained at **26 °C** or with **glycerol / dexamethasone**; degradation *"occurs through the **proteasome** pathway"* | 🟢 **The complete experiment shape for an SDR disease missense, in one paper: a measured half-life, a temperature-rescue arm, a chemical-chaperone arm, and a route determination.** And 🔴 the decisive methodological lesson: **activity was read at the rescued condition, not merely a band** — the discipline this whole node is about | 🔴 **The route does not transfer.** 11β-HSD2 is **proteasomal**; the only WWOX route ever measured (`P252A`) is **MG-132-negative and lysosome-dependent**. 🔴 **The fold fixes neither the route nor the outcome, and it must be measured per allele.** Kidney, mineralocorticoid, a known substrate — none of which WWOX has |
| **T-7** | **`HSD17B10`/`SDR5C1`, HSD10 disease.** Oerum 2017, `PMID 28888424`, another actor's attestation, `abstract-depth`, [DOI](https://doi.org/10.1016/j.bbadis.2017.09.002). p.V12L → *"reduced stability"*; p.V176M → *"impaired kinetics and complex formation"* — *"two distinctive molecular mechanisms"*. With Vilardo 2015, `PMID 25925575`, [DOI](https://doi.org/10.1093/nar/gkv408): *"Some mutations disrupt the homotetramerization … and/or impair its interaction with TRMT10C"* | 🟢 **Two missense in ONE SDR can fail by two different mechanisms** — the fold-family restatement of `P252A` vs `P282A`, and the direct justification for **no cross-variant generalisation**. Also: a **stability lesion and an interaction lesion are distinguishable within one protein**, which is the discrimination §3.4 is built to make | 🔴 Mitochondrial, a homotetramer, an RNase-P partner, a known dehydrogenase activity. 🔴 **And the tetramerisation half must not be carried:** *"WWOX homodimerises via the SDR"* is `PREMISE: UNVERIFIED` — a fully-expanded query census found no published source, and the one dimerisation record is p-WWOX/p-p53 **hetero**-dimers |
| **T-8** | **17β-HSD from *Cochliobolus lunatus*.** Brunskole 2008, `PMID 18775764`, another actor's attestation, `abstract-depth`, [DOI](https://doi.org/10.1016/j.mce.2008.07.023). *"Phenylalanine substitutions introduced **at the dimer interface** produced **inactive aggregates and oligomers with high molecular masses**"* | 🟡 **Transfers only as the specification of a trigger that `Q230P` is NOT.** The documented SDR aggregation trigger is **interface** substitution; `Q230P` has SASA **0.00 Å²** and is ≥12.5 Å from either documented SDR interface element, so it is **not that class.** That removes an identified red flag | 🔴 A fungal enzyme; designed hydrophobic substitutions; no human disease. 🔴 **And "not the known trigger" is not "will not aggregate":** a core-misfolding lesion is a generic aggregation risk and **nobody has looked in the pellet.** 🔴 The transfer's premise — a WWOX SDR homodimer — is itself `PREMISE: UNVERIFIED`, so this row cannot be used in either direction |
| **T-9** | **Parkin proteostasis atlas.** Clausen 2024, *Nat Commun* 15:1541, `PMID 38378758`, another actor's attestation with quoted locators. `L-9`: *"high abundance is a **necessary, but not sufficient** criterion for a variant to be functional"*. `L-10`: *"at 29 °C the low abundance peak almost disappeared entirely and most variants now appeared stable"* (⚠️ authors' hedge *"Presumably"*). `L-11`: *"treatment with the activator **did not confer any substantial differences** in Parkin abundance"* | 🟢 Three things. (a) **`L-9` is the brief's thesis stated by an independent group in print.** (b) **`L-10` is the 29–30 °C arm as a demonstrated, reagent-free folding-rescue lever** — adopted in §3.2. (c) 🔴 **`L-11` is a published NEGATIVE that must be imported:** a compound that modulates the wild-type enzyme's activity **failed to stabilise the destabilised variants.** An activity modulator is not automatically a variant stabiliser | 🔴 Parkin is a RING-domain E3 ligase with a **mitophagy** readout and a known catalytic output; the abundance assay is a VAMP-seq-class multiplexed design (⛔ pruned here). **No Parkin conclusion and no parkinsonism inference transfers**, and the 29 °C result is explicitly hedged by its authors |
| **T-10** | **CYP2C9 and CYP2C19 variant-effect maps.** Amorosi 2021, `PMID 34314704`, [DOI](https://doi.org/10.1016/j.ajhg.2021.07.001) — *"activity **and** abundance"*; Boyle 2024, `PMID 39319420`, [DOI](https://doi.org/10.1093/genetics/iyae156) — *"a **substrate specificity–abundance tradeoff**"*. Both another actor's attestation, `abstract-depth`, both `UNTESTED` for retrievability by that census's own declaration | 🟢 **The reporting discipline: two axes, measured separately, on the same variants, in an oxidoreductase.** And the empirical fact that within one oxidoreductase family **abundance and activity come apart at scale** — the population-level counterpart of `P282A`. This is what justifies C1–C3 being separate criteria rather than one | 🔴 Cytochromes P450 **have known substrates and a scoreable turnover**; WWOX does not, and that asymmetry is what closes the catalytic route (§5). 🔴 Both are **multiplexed** designs — ⛔ pruned. No pharmacogenomic inference transfers |
| **T-11** ⚠️ | **`PNPLA3` I148M.** Wang 2024, *J Hepatol* 82(5):871–81, `PMID 39550037`, `abstract-depth`, [DOI](https://doi.org/10.1016/j.jhep.2024.10.048). *"We quantified and compared the physical interactions … using **NanoBiT complementation assays** … **No differences were seen in the strength of the interactions** between ABHD5 with PNPLA3(WT) and PNPLA3(148M)"*, while purified-protein activity work showed the variant's hydrolase activity was reduced and the pathogenic mechanism lay elsewhere | 🔴 **The most important cautionary transfer for my own recommendation, and it cuts against it.** A published case in which a **luminescent interaction readout scored a genuinely pathogenic missense variant as entirely NORMAL** — because the lesion was not in that interaction. 🔴 **Therefore: a normal BRET curve for `Q230P` does NOT establish that `Q230P` protein is functional; it establishes that this engagement is intact.** §3.5 item 6 and the `P282A`/WW1 controls are the mitigation, and they are only partial | 🔴 A lipid-droplet hydrolase, a **gain-of-function** variant, a triglyceride readout, a liver disease. **Nothing about `PNPLA3` biology transfers**, and in particular its *"reducing, rather than increasing, expression"* conclusion is **about `PNPLA3` only** and must never be carried to WWOX |

🔵 **The one cross-cutting lesson of the table, stated once:** **four independent fold- or
method-neighbours (T-6, T-7, T-9, T-11) each found that the mechanism was somewhere other than where
the obvious readout looked.** That is not an argument against measuring; it is the argument for a
design that carries its own dissociation control (`P282A`) and its own blindness control (WW1).

---

## 7 · `HUMAN_REQUIRED` — parked external actions, and why none of them is a substitute for §3

🔴 **No `HUMAN_REQUIRED` decision packet replaces the recommendation.** The brief's condition for
that substitution — *"only a materially new research programme would work"* — **is not met.** The
recommended assay is tier (c): commercial reagents, two plasmid families, site-directed mutagenesis,
a plate reader. The items below are **external actions I am forbidden to take** (no emails, no
laboratory contact, no material requests), parked and not pursued.

| # | Action | Why it is `HUMAN_REQUIRED` | What it would change |
|---|---|---|---|
| **H-1** ⭐ | **Obtain the body of `PMID 29808465`** (Johannsen 2018) — the `n`, the Western-blot controls, the densitometry, and the qRT-PCR amplicon position | `pmc_id: null`, `unrecoverable_by_these_routes`, closed at Springer. Author contact / WWOX Foundation / ILL — all external | 🔴 **Both of the only two data about the most recurrent WWOX allele in the disease — 8 patients, 6 families — are `abstract-depth`.** It would also give the blot's detection floor, which C7 needs |
| **H-2** ⭐ | **Obtain the body of `PMID 21476439`** (Sałuda-Gorgul 2011) — construct boundaries, whether any purification preceded the activity measurement, the substrate list with cofactor conditions, the Km table with dispersion | No PMCID, no DOI in the PubMed record, De Gruyter; three independent PMC checks negative | It is falsifier #3. If it reports purified enzyme with a dead-triad control, **candidate D becomes the recommendation instead of §3** |
| **H-3** | **Confirm availability of `Q230P` patient-derived fibroblasts**, and of an isogenic knock-in pair if obtainable | Material transfer is an external action | 🔴 **The solubility split (§4) — the only tier-(a) item and the only one that can stop the therapeutic axis — depends entirely on it.** `PREMISE: UNVERIFIED` today |
| **H-4** | **Any wet-lab execution of §3 or §4** | LEGEND has no wet-lab capacity | — |
| **H-5** | *(zero-spend, no external contact — noted here only because it is the cheapest open check in the node)* **Look up whether `WWOX` is in the OpenCell endogenous split-mNeonGreen2 library** | `opencell.czbiohub.org` is unreachable from this checkout; needs a machine with egress, not a person | Falsifier #5 |

---

## 8 · What I could not establish

1. 🔴 **Which variant lost `POLE4` binding in `PMID 41124647`.** The extractor deleted the variant
   superscripts; two repository files reconstruct it as `P282A`; **I did not verify the panel label.**
   `PREMISE: UNVERIFIED`. **This is the verification that gates the primary partner choice** (§3.3,
   falsifier #1) and it is the most consequential unresolved item in this file.
2. 🔴 **Whether a NanoLuc or HaloTag fusion is tolerated by WWOX.** Unknown for this protein, with a
   published precedent that it matters (T-5) and a published precedent that tag *topology* changes
   the answer (T-1). **Not assessable without the pilot.**
3. 🔴 **Whether WWOX–`POLE4`, WWOX–tau or WWOX–GSK3β engagement is SDR-**fold**-dependent to the
   standard T-4 sets.** The only WWOX evidence pointing that way is **unpublished** (*"Aldaz
   laboratory unpublished observations"*, readout = localisation, no data shown), and a **published**
   WW1-routed alternative to the same class of effect exists. `PREMISE: UNVERIFIED`. **A flat curve
   therefore has two readings and this file cannot narrow them** (§3.5 item 6).
4. 🔴 **The numerical detection floor of any WWOX readout, in molecules or % of wild type.** C7 is
   unmet by every existing measurement, including the one that produced *"protein not detected"*.
   Nobody has stated it, so I cannot state what the recommended assay must beat — only that
   luminescence beats a blot by orders of magnitude, which is an instrument property, not a measured
   WWOX number.
5. ⚠️ **Whether the 2011 bacterial constructs still exist**, and what they contained. Body unread;
   custodianship is an external question (H-2).
6. ⚠️ **Whether the >50 % effect sizes in T-3 were abundance-normalised in that paper's body.**
   Abstract-depth; my criticism is of the abstract's description, not a verdict on the paper.
7. 🔴 **Everything downstream of the assay.** Whether engagement competence predicts anything about
   neurons, myelination, the developmental window, seizures or clinical course. **This design cannot
   reach any of it**, and no result from it may be read as if it could.
8. **Whether `PMID 32810216` (T-1) has a retrievable body.** No PMCID in the returned metadata; I did
   not attempt a fetch. `abstract-depth`, and the tag-topology quote is from its abstract.
9. ⚠️ **A small internal inconsistency in the repository, found in passing and not adjudicated.**
   `CC-20260921-WWOX-ENZYMOLOGY-P306-01` states of `PMID 21476439` that *"no DOI is present in the
   record and none is asserted here"*, while `wwox_activity_sensor_census_20260921.md` § 4.5 cites
   `10.1515/znc-2011-1-210` for the same record. **Both can be true** — a publisher DOI can exist
   while the PubMed record carries none — but the two files read as contradicting each other.
   **I did not re-query the record to settle it**, and I assert no DOI for that paper anywhere above.

---

## 9 · Declared limits of this file

- **One body was read by me in this act** (`PMC8866893`, 47 282 chars measured). Everything else is
  abstract-depth, repo-held, or another actor's attestation, as declared in § 0. **An abstract is
  not a read, and no receipt is claimed anywhere.**
- **No claim is created. No score is assigned.** `FLAG FIRST` is honoured: the assay's expected
  result is not predicted and the therapeutic sign is not moved by one step. The boost axis stands
  exactly where Scientist B left it — **NOT-DANGEROUS-ON-THIS-EVIDENCE and STILL UNDETERMINED**,
  `IPOTESI`.
- **Abundance, stability, solubility and function are held apart throughout** — four different
  lesions, four different therapies. **No cross-variant generalisation:** `Q230P` ≠ `P47T` ≠ `P252A`
  ≠ `P282A` ≠ `G372R` ≠ `A141T`.
- **`WWOX homodimerises via the SDR` is `PREMISE: UNVERIFIED`** and nothing here is built on it.
- 🔴 **The `Q230P` namespace trap is not walked into:** `GTPBP3` p.Q230P / `c.689A>C`
  (`PMID 41957021`) is a **different gene** with a measured aggregation result at an identical
  coordinate, and it appears nowhere in this design as evidence.
- **The transfer arguments are mine**, not any author's. No paper cited in §6 mentions WWOX.
- **The engineering argument that a fitted BRET<sub>max</sub> is expression-independent is my
  reasoning about the measurement**, presented as such and not as any paper's claim.
- **No new research programme is proposed. No MAVE. No activity sensor.** Both remain the Operator's
  decision and this file holds that line.
- **No external human action was taken:** no laboratory contacted, no author emailed, no material
  requested. Parked at §7.
- **Nothing here is medical advice, and no therapeutic recommendation for any person appears
  anywhere.** The reference genotype is a WWOX-DEE genotype class; no individual-level record is
  reintroduced.

---

**END OF FILE — complete run.** Nine sections, all written. Non-canonical research-layer file. No
registry, queue, ledger, receipt chain, canonical file or state manifest was read-modified-written.
No `BATCH_COMMIT`, no commit, no stage, no push. According to PubMed, the new literature content
above derives from the records cited, each with its DOI linked at first use where the PubMed record
carries one; `PMID 21476439` carries **no DOI in its PubMed record** and none is invented here.
