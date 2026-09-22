# `Q230P` — the direct discriminator: one compressed experiment, and the hypothesis × readout matrix it is built from

**Actor:** Scientist I · **Date:** 2026-09-22 · **Reports to:** Orchestrator · **Canonical `main`:** `8d367f3`
**Status:** 🔴 **NON-CANONICAL.** No registry, queue, ledger, receipt chain, state manifest or `*_current.md`
was written. No `BATCH_COMMIT`. **No git command was run.** One output file was created: this one.
**Nothing here is medical advice.** No molecule, dose, route, prognosis or safety claim is recommended
anywhere below. Every inhibitor named is a bench reagent at a published in-culture concentration.
**Genotype classes are held apart throughout.** `Q230P` ≠ `Q230A` ≠ `Q230M` ≠ `P282A` ≠ `P252A` ≠ `G372R`
≠ `P47T` ≠ `A141T` ≠ `L239R`. A measurement on one is never carried to another.
**Source classes are never merged:** `EXPERIMENTAL` · `HOMOLOGY` · `MODEL` · `INFERENCE`, labelled at every
point of use. **A prediction is never a measurement.** `NOBODY_LOOKED`, `UNREAD_PRIMARY` and `UNVERIFIED`
are three different statements and are never collapsed.
**Public edition — this reasons about a WWOX-DEE reference genotype class, not an individual.**

---

## 0 · What I inherited and did not re-derive

Read in full before any act in this file, and treated as **other actors' attestations, not my measurements**:
[`q230p_therapeutic_mechanism_expansion_20260922.md`](q230p_therapeutic_mechanism_expansion_20260922.md)
(esp. §§6, 7, 8, 10) ·
[`q230p_structural_mechanism_20260922.md`](q230p_structural_mechanism_20260922.md) ·
[`function_per_molecule_assay_design_20260922.md`](function_per_molecule_assay_design_20260922.md) ·
[`wwox_engagement_partner_adjudication_20260922.md`](wwox_engagement_partner_adjudication_20260922.md) ·
[`wwox_missense_stability_census_20260922.md`](wwox_missense_stability_census_20260922.md).

Located by the mandatory novelty check (`FIND ISSUE → SEARCH CLAIMS → SEARCH CANDIDATES → SEARCH DISCOVERY
LEDGER`) and treated as **delta-defining prior art**, not as something to rediscover:
[`proteostasis_discrimination_protocols_20260922.md`](proteostasis_discrimination_protocols_20260922.md)
(Scientist C: the ranked protocol shortlist, `Caveat 2`, the bafilomycin correction, the Koch 2011
fibroblast-false-negative) · [`missense_proteostasis_matrix_20260921.md`](missense_proteostasis_matrix_20260921.md)
· [`proteostasis_rationale.md`](proteostasis_rationale.md) · [`mechanism_intervention_map.md`](mechanism_intervention_map.md)
`TX-003` · `HYP-20260709-08` and `DL-BIO-001` in the ledgers.

**Carried forward without re-derivation.** `Gln230`: SASA 0.00 Å², core-buried, helical, pLDDT 98.5; NOT
interface, NOT cofactor site (12.60 Å from the cofactor-cleft axis), NOT substrate pocket, NOT exposed.
φ(230) = −65.4° is already proline-compatible, so **φ is not the lesion**; the operative fact is the modelled
Pro Cδ at 1.60 Å from Glu226 O — a **1.44 Å hard overlap** — with L234 downstream the most buried residue in
the chain, i.e. **no cheap escape**. Mechanism verdict **`MIXED`**: folding primary, degradation as
*consequence* not lesion, aggregation unexcluded. `WWOX homodimerises via the SDR` is `PREMISE: UNVERIFIED`.
ThermoMPNN ΔΔG is **anti-correlated** with every WWOX abundance measurement that exists, so `Q230P`'s +1.514
carries no evidential weight in either direction. **Nobody has ever looked in the pellet, for any WWOX
allele.** No purified folded WWOX SDR exists. Both `Q230P` data points are **`abstract-depth`** (PMID
29808465, closed at Springer): transcript normal, protein not detected on one Western of patient fibroblasts.
`P282A` is **`OVEREXPRESSION-ARTEFACT SUSPECT`** — `rs3764340`, 18 homozygotes enrolled as healthy adult
cancer-free controls, meta-analysis homozygous model null (OR 1.36, CI 0.90–2.04), ClinVar **Benign** — and
**no residual-function magnitude may be inferred from it**. `Q230G` is **EXCLUDED** as a discriminator despite
ranking highest on ΔΔG, because it perturbs side chain **and** backbone at once. In an SDR (Lou 2018, PMID
29141528) **all seven** engineered mutants lost activity, the best retaining 28.7 % — a **methodological
constraint on this design**, not evidence that `Q230P` is unrescuable. **`STABILITY CANNOT PROXY FUNCTION.`**

---

## 1 · PROSPECTIVE DISCOVERY TRACE

> 🔴 **Persisted to this file at 2026-09-22 BEFORE any targeted external search was run.** The only searching
> that preceded it was the mandatory repository novelty check recorded in §1.8, run to avoid re-deriving prior
> art rather than to confirm a hypothesis. **Nothing in §§1.1–1.6 was edited after the searches.** `RESULT`
> (§1.7), the grading (§1.9) and the experiment (§6) were appended afterwards, and where a prediction failed
> it is recorded as failed rather than rewritten.

### 1.1 OBSERVATION

The brief asks for a system that separates four hypotheses — **degradation**, **misfolding/insolubility**,
**stable-but-function-defective**, **mixed** — and offers six candidate readouts, one of which looks like it
"belongs" to each hypothesis: degradation kinetics for degradation, the solubility split for insolubility,
partner engagement for function.

🔴 **That one-to-one mapping is the error, and the whole file turns on seeing it.** Three of the four
hypotheses are **fates of the same molecule population** and differ only in *where the molecule ends up*,
while the fourth describes a **different population** — molecules that are present, soluble and long-lived
and do nothing. A readout that measures one property of one population therefore answers **more than one
column at once and none of them cleanly**: "protein low in a soluble lysate" is the identical observable for
degradation, for insolubility, for a co-translational yield ceiling, and for an antibody that cannot see the
epitope. That is precisely why `Q230P` has one datum and four live explanations after eight years.

**The observation that generates this trace:** every discrimination this brief asks for lives in a **ratio
between two readouts taken on the same molecules**, or in the **slope of such a ratio against induced
abundance** — never in a single readout's value. And every design this repository currently holds
(`HYP-20260709-08`'s five steps; Scientist C's staged shortlist; Scientist D's plate; Scientist H's §7)
pairs readouts to mechanisms **one-to-one and then separates by elimination**. Elimination converts every
detection floor into a conclusion. **The compression asked for is not fewer experiments; it is the same
lysates read as ratios.**

### 1.2 DIVERGE — seven mechanistically distinct discrimination architectures

Each is a genuinely different **principle of separation**, not a different reagent. What distinguishes them
is *what quantity carries the information*.

| # | architecture | the quantity that carries the information | what it fails on |
|---|---|---|---|
| **V1** | **Serial elimination** — blot, then inhibitor panel, then chase, then pulse-label; each branch closed in turn (the repository's current design) | the **order of negatives** | 🔴 Each negative is a **detection floor**, not a zero. Four floors in series produce a conclusion nobody measured. And branch (a) is reached only *by elimination*, which Scientist C states explicitly and which is weaker than measurement |
| **V2** | **Same-molecule ratio** — one photon source reports both the number of molecules and the fraction engaged, in one well | **acceptor/donor ratio at fitted saturation** | Needs a tag; tag may break the protein; says nothing about where the un-engaged molecules are |
| **V3** | **Isogenic same-position substitution series as the internal ruler** — `WT`/`Q230A`/`Q230M`/`Q230P` at matched induction, in one cell population | **allele-to-allele contrast within one plate**, not patient-vs-control | Cannot speak to the endogenous allele's abundance in a patient; needs the series to be non-degenerate (if all three read dead, the ruler is gone) |
| **V4** | **Perturbation-response fingerprint** — the *pattern* of responses to 30 °C, bafilomycin A1, chloroquine, MG-132, rather than any single response | **which levers move the level and which do not** | A negative lever is a potency statement, not a mechanism statement (Schultz 2018: chloroquine negative where bafilomycin was strongly positive, same protein, same cells) |
| **V5** | 🔴 **Partition-shift under abundance raising** — not the pellet fraction, but **d(pellet fraction)/d(induced abundance)** | **the second derivative: does raising the level push mass into the pellet?** | Requires a titration and a fractionation on the *same* lysates; needs a window in which wild type is fully soluble |
| **V6** | **Two-partner specificity contrast with deliberately opposite fold-sensitivity** — one numerator suspected fold-sensitive, one ruler suspected fold-insensitive | **the ratio between the two channels on the same molecules** | Both suspicions are `PREMISE: UNVERIFIED`; if they are wrong in the same direction the contrast is empty |
| **V7** | **Conformational susceptibility** — limited proteolysis / protease-sensitivity fingerprint on the same lysates: a direct fold readout that does not depend on level at all | **protease-resistant core footprint** | Needs protein mass a near-undetectable allele does not supply; no WWOX precedent of any kind |

🔵 **V3, V5 and V6 are the three the brief's framing would skip.** V5 in particular is not a readout at all in
the brief's list — it is a *derivative* of two readouts the brief does list, and it is the only quantity that
separates *"aggregation is why abundance is low"* from *"aggregation is what happens when you raise
abundance"*. **Those two have opposite therapeutic signs and the repository currently cannot tell them apart.**

### 1.3 CONNECT — four adjacent domains, each asked for one thing

| domain | what is being asked of it | why it is adjacent, not decorative |
|---|---|---|
| **C1 · Variant-abundance/function atlases** (VAMP-seq, Parkin, `PTEN`) | The **base rate of discordance**: how often does a variant with restored abundance still fail on function, measured at scale in one system? | It is the only literature that has measured abundance and function **as separate axes on the same variants**. If discordance is rare, the engagement channel can be cut and this design shrinks by half |
| **C2 · Resonance-transfer assay methodology** (BRET donor saturation; bystander/collision transfer) | Whether a **high local density of donor** produces transfer **without a specific interaction** | 🔴 If it does, an aggregating allele can produce a *rising* BRET that reads as engagement — the aggregation branch would **masquerade as the function branch**, and a non-interacting acceptor control becomes mandatory, refuting the minimality claim |
| **C3 · Expression-level control of the soluble/insoluble partition** | Whether the partition is **dose-dependent** for model proteins, i.e. whether a transgene pellet result is interpretable at all without a matched-expression comparator | It decides whether V3 is a nicety or a structural requirement of any transgene solubility measurement |
| **C4 · Conformation-selective cellular fold probes** (limited proteolysis, DARTS, thermal-shift in lysate) | Whether a **level-independent** fold readout exists that could replace the solubility split | If one exists and is cheap, V7 displaces V5 and the design changes shape. The repository holds **zero** occurrences of `limited proteolysis`, `LiP-MS`, `DARTS` or `thermal proteome` |

### 1.4 HYPOTHESIS

> **The minimum system that separates the four hypotheses is not four readouts but TWO RATIOS AND ONE
> PERTURBATION AXIS, read across an induction series against a same-position substitution ruler.**
>
> The two ratios are **engagement per molecule** (partner BRET at fitted saturation ÷ donor luminescence)
> and **insoluble fraction per molecule** (pellet donor signal ÷ total donor signal). The perturbation axis is
> the lever panel (30 °C · bafilomycin A1 · chloroquine · MG-132). The ruler is `WT`/`Q230A`/`Q230M`/`Q230P`
> at matched induction in one cell population.
>
> **And two of the six candidate readouts change no cell of the resulting matrix and must be cut:
> degradation KINETICS (the cycloheximide-chase half-life) and LOCALISATION.** The degradation *axis* is
> retained — by block-and-rescue, which is measurable at zero baseline, where a chase is not.

### 1.5 PREDICTION — ex-ante, before any targeted search

Each is written to be falsifiable by a specific literature observation, and each has a stated consequence for
the design. **A prediction that fails is recorded as failed.**

| # | prediction | consequence if REFUTED |
|---|---|---|
| **P1** | **Abundance and function are discordant often enough, in the atlases that measured both, that an abundance-only readout misclassifies a material fraction of variants.** Expected: a published statement that a substantial subset of variants is low-function-normal-abundance and/or that abundance rescue does not imply function rescue | 🟢 If abundance predicted function well, **the engagement channel could be cut** and the minimum set halves to abundance + solubility. This is the prediction whose refutation would most simplify the design |
| **P2** | **A cycloheximide chase started from a near-detection-floor band is not done in practice** — published chases start from an accumulated or over-expressed pool | The kinetic readout re-enters the minimum set and the cut in §1.4 is wrong |
| **P3** | **Localisation microscopy cannot assign aggregation vs degradative routing**, because puncta are reported for both | Localisation re-enters as a discriminator rather than as a tag-pilot control |
| **P4** | **No published design uses a same-position substitution series as the internal comparator for a SOLUBILITY or abundance readout in mammalian cells.** I expect the series precedent to be structural/thermodynamic only | 🔵 If one exists, V3 is a rediscovery and must be graded `A`, not `C` |
| **P5** | **Expression level is a documented determinant of the soluble/insoluble partition**, so a transgene pellet result is uninterpretable without a matched-expression comparator | The matched-expression ruler becomes optional rather than structural, and the design could use a simple over-expression plate |
| **P6** | **A level-independent conformational probe exists (limited proteolysis / DARTS / LiP-MS) but requires protein mass that a near-undetectable allele does not supply**, so V7 stays out of the minimum set | If it is cheap and works at low abundance, **V7 displaces the solubility split** and the whole architecture changes |
| **P7** | 🔴 **Donor-saturation BRET produces a non-specific, density-dependent transfer ("bystander"/collision BRET) at high donor expression** | **If SUPPORTED, my minimality claim is REFUTED**: a non-interacting acceptor control must be added to the minimum set, because an aggregating allele would otherwise produce a rising BRET that reads as engagement |

### 1.6 DISCRIMINATOR — what separates my hypothesis from the obvious alternative

**Alternative hypothesis (the brief's implicit one):** each of the four mechanisms needs its own dedicated
readout, so the minimum set is four or more.

**The observations that decide between them, stated ex-ante:**

1. 🔴 **P7 SUPPORTED ⇒ my hypothesis is REFUTED as stated**, because the two-ratio set is not sufficient: a
   density-dependent bystander signal makes the engagement ratio ambiguous exactly in the condition
   (aggregation) that the solubility ratio is there to detect, and a third acceptor channel is forced in.
2. 🟢 **P1 REFUTED ⇒ my hypothesis is over-built**: the engagement ratio is redundant and the minimum set is
   one ratio plus the levers.
3. 🔵 **P2 or P3 REFUTED ⇒ the two cuts in §1.4 are wrong** and the set is five or six readouts, i.e. the
   brief's list survives intact and this file's contribution reduces to the matrix.
4. **P5 REFUTED ⇒ V3 is a convenience, not a requirement**, and the compressed experiment could be run
   without the `Q230A`/`Q230M` arms — which would make it cheaper and weaker.

**None of these is decidable from the repository**, which is why they are searchable predictions and not
assertions.

### 1.7 RESULT

> *Appended after the targeted searches of §2. Written without editing §§1.1–1.6.*

🟢 **FILLED — see §2, which is §1.7 in full.** Two predictions REFUTED (`P6`, `P7` in its consequence for my minimality claim; `P4` refuted for abundance), one NOT SCOREABLE (`P2` — already held in the repository), one AMBIGUOUS (`P3`), three SUPPORTED (`P1`, `P5`, `P7`).

### 1.8 The repository novelty check, with counts

Run **before** the trace was written, over the tree at the working checkout, with this file not yet created
(so no self-contamination is possible; `grep -ril` over `disease-models/wwox/`):

```
donor saturation            0 files      limited proteolysis         0 files
non-interacting acceptor    0 files      LiP-MS                      0 files
DARTS                       0 files      thermal proteome            0 files
bystander                   6 files  →  ALL are base-editing bystander-cytosine or "tau is not a bystander".
                                         ZERO are resonance-transfer bystander signal.
Q230A / Q230M / Q230G       0 files outside this session's own wave files
```

`insoluble fraction` (12 files) and `VAMP-seq` (7 files) are held, and are cited above as prior art rather
than claimed. 🔴 **The concepts this file's minimality argument turns on — donor-saturation bystander
transfer, the non-interacting acceptor control, and level-independent conformational probes — are absent from
the repository in every spelling checked.**

### 1.9 GRADE

> 🟢 **FILLED — see §10.** Highest grade claimed: **E (experiment-generating)** for §7. Two items at **D**, five at **C**. 🔴 **No item is graded F.**

---

## 2 · RESULT — the targeted searches, filling §1.7

**Read depth, declared before any finding.** Every literature item below is **`passage-depth`** via
`Scholar_Gateway semanticSearch` — passage retrieval of published bodies, which **cannot substitute for a
full read**, and whose `ai_generated` summary I did not use and do not cite. **No `FULLTEXT_READ_RECEIPT` is
claimed anywhere in this file and none is owed.** One record is PubMed metadata retrieved by me in this act
(PMID 41124647). **No figure panel was inspected.** No PMID or DOI below was reconstructed from memory.

### 2.1 The prediction table, scored

| # | prediction | outcome | what actually came back |
|---|---|---|---|
| **P1** | abundance and function discordant often enough that abundance alone misclassifies | 🟢 **SUPPORTED** | *"DMS signals typically **conflate** a substitution's effects on protein function with those on in vivo protein abundance; this limits the resolution of mechanistic insights that can be gleaned from DMS data. **Distinguishing functional changes from abundance-related effects is particularly important for substitutions that exhibit intermediate outcomes** (e.g., partial loss-of-function)"*; and, on ten substitutions at each of six positions, *"the six tested positions showed **diverse substitution sensitivities for function and abundance**."* — Sreenivasan, Fontes & Swint-Kruse 2025, *Protein Science* 34(8), [DOI 10.1002/pro.70225](https://doi.org/10.1002/pro.70225). ⚠️ The same passage's abundance range renders as `~45fold` in an extraction that strips hyphens throughout (`oneatatime`, `proteasomemediated`), so it is **either ~4–5-fold or ~45-fold and I do not know which** — **I therefore use no magnitude from it**, only the qualitative separation. 🔴 **The engagement channel cannot be cut** |
| **P2** | a chase from a near-floor band is not done in practice | ⚪ **NOT SCOREABLE — already held in the repository.** Scientist C's `Caveat 2` states it and proposes the inhibitor-first correction | Recorded as a **weak prediction**: it asked for something the repository already knew. No credit taken |
| **P3** | localisation cannot assign aggregation vs degradative routing | 🟡 **AMBIGUOUS — and the cut survives for a partly different reason** | The aggresome is *"a juxtanuclear, membrane-free, cytoplasmic **inclusion containing misfolded, ubiquitinated protein**"* forming *"when the capacity of the proteasome is exceeded by the production of aggregation-prone misfolded proteins"* — i.e. **one punctum that is simultaneously an aggregate and a degradation-routing structure**, so localisation alone cannot assign ([DOI 10.1111/febs.15617](https://doi.org/10.1111/febs.15617)). 🔴 **But the same literature shows it CAN be assigned with co-stains** (LAMP1, LC3, p62, MTOC). ⇒ **the cut holds on cost and reagents, not on impossibility** — three extra channels, and this repository records that *"commercial anti-WWOX antibodies did not show any specific signal for IF"* |
| **P4** | no published design uses a same-position substitution series as the internal comparator for a solubility/abundance readout | 🔴 **REFUTED for abundance. Still open for solubility.** | The Mpro study is exactly that design: *"We generated **10 substitutions at each of six positions** and **separately measured effects on function and abundance**."* ⇒ 🔵 **V3 is a `CROSS-DOMAIN-DERIVED` method transfer, not an agent-novel idea, and is graded down accordingly.** No instance was found for the **solubility** partition, which stays `UNTESTED` |
| **P5** | expression level determines the soluble/insoluble partition | 🟢 **SUPPORTED, precisely and usefully** | *"SNAP-HDQ72 forms aggregates **regardless of expression level, but expression level determines aggregate formation rate, distribution and morphology**, as well as aggresome size"*, in a study that built synthetic promoters specifically so that *"expression levels … are **within the physiological range**"* — Lu *et al.* 2015, *Biotechnol Bioeng*, [DOI 10.1002/bit.25606](https://doi.org/10.1002/bit.25606). 🔵 **The nuance is better than the prediction:** level does **not** create the propensity, it sets the **rate and morphology** — so a transgene pellet result at unmatched expression is **quantitatively uninterpretable**, while the same result at **matched expression across alleles in one cell population** is interpretable. **That is the structural justification for V3** |
| **P6** | a level-independent conformational probe exists but needs protein mass a near-undetectable allele cannot supply | 🔴 **REFUTED, and this is the most consequential failure in the trace** | **Pulse proteolysis + quantitative Western ("Pulse and Western")** was built for exactly this: *"we have developed a method to determine the **thermodynamic stability of low abundant proteins in cell lysates** … combining pulse proteolysis with quantitative Western blotting … This method allows the investigation of conformational energetics of proteins in cell lysates **without cloning, purification, or labeling**."* — Kim, Song & Park 2009, *Protein Science* 18(5):1051–1059, [DOI 10.1002/pro.115](https://doi.org/10.1002/pro.115). Corroborated as a class by the label-free review [DOI 10.1002/med.21788](https://doi.org/10.1002/med.21788) (pulse proteolysis, limited proteolysis, DARTS, CETSA, SPROX) and by DARTS practice in whole-cell lysate ([DOI 10.1002/iub.1697](https://doi.org/10.1002/iub.1697), which also names the honest limitation: *"the influence of binding affinity, **protein abundance**, and the susceptibility of the protein to endogenous proteolysis"*). 🔴 **Consequence taken, not dodged — see §2.2** |
| **P7** | donor-saturation BRET produces a density-dependent non-specific transfer | 🟢 **SUPPORTED — and it BOTH refutes my minimality claim and repairs it** | *"If the obtained BRET signal results from **random collision (bystander BRET)** between the energy donor and acceptor, the BRET should increase **almost linearly** with the increase of the acceptor fusion protein and may reach saturation only at very high levels"*; *"in the case of a **specific** protein-protein interaction, the BRET ratio increases **hyperbolically and rapidly saturates**"*; and, decisively for this allele: *"**avoid massive protein expression that may cause protein aggregation and microdomain crowding and lead to a nonspecific BRET signal ('bystander BRET')**."* — Hamdan, Percherancier, Breton & Bouvier 2006, *Curr Protoc Neurosci* 34(1):5.23.1–5.23.20, [DOI 10.1002/0471142301.ns0523s34](https://doi.org/10.1002/0471142301.ns0523s34) |

### 2.2 🔴 What the two refutations did to the design — taken, not absorbed

**P7 first, because it fires on my own §1.6 discriminator 1.**

🔴 **My minimality claim in §1.4 is REFUTED AS STATED.** An aggregating `Q230P` raises local donor density,
and the source says in as many words that aggregation and crowding produce a non-specific BRET. **The exact
condition the solubility ratio exists to detect is a condition that manufactures a false engagement
signal** — so two ratios alone are not sufficient, and I recorded ex-ante that this would refute me.

🔵 **And the same source repairs it, at zero additional cost, in a way I did not anticipate.** The control
is **not** a third acceptor channel. It is a **model comparison on data the titration already produces**:
specific engagement is **hyperbolic and saturates**; bystander transfer is **quasi-linear and does not**.
⇒ **Every allele's acceptor titration must be fitted to BOTH a hyperbolic and a linear model, and the model
comparison reported.** 🔴 **This converts a confound into a free readout:** a `Q230P` curve that is
quasi-linear where wild type is hyperbolic is **positive evidence of crowding/aggregation from the
engagement channel itself**, independently corroborating the pellet measurement.

🔴 **P7 also exposes a real error in the architecture I inherited, and it must be corrected before the design
is executable.** The repository's design says *"donor-saturation titration … the slope of engagement against
**donor luminescence**"*. The source is explicit that a BRET saturation curve is built the other way:
*"the Rluc fusion protein is **kept constant** while the concentration of the expressed energy acceptor
fusion protein is **increased**"*, and `BRET_50` is *"the amount … of **acceptor divided by the amount of
donor**"*. ⇒ **There are TWO titrations on TWO axes and they were conflated.** The **donor** titration is the
*abundance calibration* — it is how alleles are brought to matched expression. The **acceptor** titration,
run **at that matched donor level**, is the saturation curve from which `BRET_max` and `BRET_50` are fitted.
**Fitting `BRET_max` against a varying donor is not a saturation curve and the parameter is not defined
there.** This is the single most load-bearing correction in this file and it costs nothing to adopt.

**P6 second.** I predicted a level-independent fold probe would be out of reach. It is not. **Pulse
proteolysis gives a fraction-folded and a thermodynamic stability for a low-abundance protein in a lysate,
with no purification** — which matters because *no purified folded WWOX SDR exists and expressing one is
itself an unsolved problem in this literature*, so this is the only physical stability measurement that WWOX
can currently support at any price.

🔴 **And it does change a cell of my matrix, which is the test I set myself.** My set folds two
therapeutically opposite outcomes into one column: a protein that is **soluble, natively folded and inert**
(the `P282A` shape — no stabiliser helps) and a protein that is **soluble, NOT natively folded and inert**
(a folding lesion that has not yet partitioned — a stabiliser is at least on-mechanism). **Nothing else in
the set separates them**, and the Lou 2018 anti-correlation makes the distinction decisive rather than
academic. ⇒ **Pulse-and-Western is admitted to the design as the ONE CONDITIONAL ADD-ON, triggered by exactly
one matrix row (`R7`), not as a sixth always-on readout.**

⚠️ **One tempting shortcut is refused.** It is *not* established that a NanoLuc fusion's proteolysis can be
read by luminescence instead of by blot: NanoLuc is itself unusually protease- and thermo-resistant, so the
luminescent readout could report the **tag's** resistance rather than WWOX's. `IPOTESI`, untested, and the
quantitative-Western route is the one specified in §6.

### 2.3 🔴 Four PubMed / retrieval traps hit in this act, and how each was cleared

| # | trap | what happened | how it was handled |
|---|---|---|---|
| **1** | ⭐ **Trap (f) — the over-conjoined query.** `VAMP-seq variant abundance mass spectrometry multiplexed assay abundance function separate classes PTEN` → **`total_count: 0`** | The `query_translation` shows **nine `AND` blocks**, and one of them expanded **`separate` → `"divorce"[MeSH Terms]`**. A nine-term conjunction returns zero from any corpus | 🔴 **Reported as a meaningless zero and used as evidence of nothing.** The same question was then answered at passage depth by a different tool |
| **2** | **Trap (d) — a wrong-MeSH expansion, again, and on a different word.** In the same query, `separate` reached **`"divorce"[MeSH Terms]`** | Visible **only** by reading the `query_translation` | Recorded. 🔵 The repository already holds `Millet → "millets"[MeSH]` (the cereal); **this is the same failure on a common verb rather than a surname**, which widens the trap's known footprint |
| **3** | **A bare-concept zero.** `bystander bioluminescence resonance energy transfer donor saturation nonspecific collision membrane density` → **`total_count: 0`**, with a flawless expansion | 🔴 **The method is named only in a Methods/Protocols body**, which is trap (e) — *"a method named only in Methods is invisible even with a perfect expansion"* | Re-queried through `Scholar_Gateway semanticSearch`, which returned the protocol body and the exact sentences. 🟢 **Trap (e) fired and the documented route cleared it** |
| **4** | **A hyphen-stripping extractor.** The passage renderer deletes hyphens (`one-at-a-time` → `oneatatime`) | 🔴 `~4-5-fold` and `~45-fold` become the **same string** | **The magnitude was discarded and only the qualitative claim used** (P1 row). A number that cannot be disambiguated is not a number |

🟢 **Not walked into, because the repository's tripwires held:** bare `"Q230P"` was never queried (two
**GTPBP3** records at an identical `c.689A>C`); `CBR3`'s wild-type proline at position 230 (PMID 18983987)
was not confused with `Gln230` in WWOX — **a number coinciding is not a position coinciding**; and no
`is_open_access: false` record was skipped rather than ordered.

---

## 3 · THE HYPOTHESIS × READOUT DISCRIMINATION MATRIX

### 3.0 The five measured quantities, defined so a technician could execute them

| symbol | quantity | how it is obtained | units / categories |
|---|---|---|---|
| **A** | **attainable abundance** | NanoLuc donor luminescence per cell at maximal doxycycline, ÷ wild type at maximal doxycycline | `≈WT` · `low-but-matchable` (some dox level equalises the donor signal to WT's working level) · `floor` (no such level exists) |
| **S** | **insoluble fraction** | non-denaturing lysis → spin → SDS/urea-resolubilised pellet vs supernatant, **quantitative Western against the TAG epitope**, at **matched donor signal** | pellet ÷ (pellet + soluble), relative to WT |
| **dS/dA** | 🔴 **partition shift** — *the quantity that is in no prior design* | the **slope** of S against induced A across the dox series | `flat like WT` · `rising` |
| **E** | **engagement per molecule** | fitted `BRET_max` of the WWOX–`POLE4` **acceptor** titration performed **at matched donor**, ÷ WT; **plus the hyperbolic-vs-linear model comparison** | fraction of WT `BRET_max`; curve shape `hyperbolic` · `quasi-linear` |
| **G** | **the ruler** | the same fit for WWOX–`GSK3β` | fraction of WT `BRET_max` |
| **L** | **lever response** | does A rise under bafilomycin A1 · chloroquine · MG-132 · 30 °C? | per-lever yes/no |

🔴 **Every one of these is read at MATCHED DONOR SIGNAL except A itself.** That is the whole point: A is the
only quantity allowed to differ between alleles, because it is the quantity being controlled for.

### 3.1 The matrix

**Columns are mechanisms. Rows are result patterns. Each cell says what that pattern means for that
mechanism.** `✅ REQUIRES` = the pattern is what this mechanism must produce · `❌ EXCLUDES` = this mechanism
cannot produce this pattern · `⚪ silent` = compatible but not diagnostic.

**Mechanism columns.** **M1** degradation (post-folding clearance of a folded or near-folded species) ·
**M1′** synthesis / co-translational triage (folding-yield ceiling — *the fifth mechanism, separated for
free*) · **M2** misfolding / insolubility · **M3a** stable, **folded**, function-defective · **M3b** stable,
**soluble but not folded**, function-defective · **M4** mixed.

| # | **RESULT PATTERN** (A · S · dS/dA · L · E · G) | **M1 degradation** | **M1′ synthesis/triage** | **M2 insolubility** | **M3a folded-inert** | **M3b unfolded-inert** | **M4 mixed** |
|---|---|---|---|---|---|---|---|
| **R1** | A low-but-matchable · S ≈WT · dS/dA flat · L **baf +** · E ≈WT, hyperbolic · G ≈WT | ✅ **REQUIRES.** Clearance is the bottleneck; the molecules that survive are fully competent | ❌ EXCLUDES — a lever recovered protein, so synthesis is not the ceiling | ❌ EXCLUDES — pellet is normal | ❌ EXCLUDES — E is normal | ❌ EXCLUDES | ❌ EXCLUDES — one lesion, not two |
| **R2** | A **floor** · S ≈WT · L **all negative** (baf, CQ, MG-132, 30 °C) · E, G not measurable | ❌ EXCLUDES — blocking every route recovered nothing | ✅ **REQUIRES.** Nothing is reaching a stable species; the lesion is upstream of clearance | ❌ EXCLUDES — nothing in the pellet either | ⚪ silent — untestable, there is no protein to test | ⚪ silent | ⚪ silent |
| **R3** | A low · S **elevated** · dS/dA **flat** (pellet fraction constant across induction) · L 30 °C shifts mass to soluble | ⚪ silent | ❌ EXCLUDES — protein was made, it is in the pellet | ✅ **REQUIRES, and it is INTRINSIC** — the partition does not depend on how much you make, so it is the allele, not the dose | ❌ EXCLUDES | ⚪ silent | ⚪ silent |
| **R4** | A low · S elevated · dS/dA 🔴 **RISING** · L baf + but pellet rises with it | ⚪ silent | ❌ EXCLUDES | 🟡 **REQUIRES — but DOSE-DRIVEN, not intrinsic.** 🔴 **The only cell in the matrix that says raising abundance CREATES the aggregate rather than revealing it** | ❌ EXCLUDES | ⚪ silent | ✅ compatible |
| **R5** | A ≈WT · S ≈WT · E **low** · G ≈WT · E curve **hyperbolic** | ❌ EXCLUDES — abundance is normal | ❌ EXCLUDES | ❌ EXCLUDES | ✅ **REQUIRES.** Present, soluble, specifically engaged-defective — the `P282A` shape at this allele | 🟡 not excluded until `R7` is run | ❌ EXCLUDES |
| **R6** | A ≈WT · S ≈WT · E **low** · G 🔴 **low** | ⚪ silent | ⚪ silent | ⚪ silent | ❌ **EXCLUDES** | ⚪ silent | ⚪ silent → 🔴 **NOT A MECHANISM ROW. Global collapse, or a broken construct/tag.** `DISCARD THE PLATE` or re-pilot. **This row exists only because G is in the set** |
| **R7** | `R5`, **plus** pulse-and-Western shows a **reduced folded fraction / lowered C_m** at matched abundance | ❌ EXCLUDES | ❌ EXCLUDES | ❌ EXCLUDES — it is soluble | 🔴 **EXCLUDES** | ✅ **REQUIRES.** Soluble, not folded, inert. 🟢 **The one function-defective outcome for which a folding-directed lever is on-mechanism** | ⚪ silent |
| **R8** | A low-but-matchable · S ≈WT · L baf + · E **low at matched A** · G ≈WT | ✅ partially — clearance is real | ❌ EXCLUDES | ❌ EXCLUDES | ✅ partially — the surviving molecules are inert | ⚪ silent until `R7` | ✅ **REQUIRES. `MIXED = degradation + engagement defect`.** 🔴 **The boost restores molecules and not function** |
| **R9** | A low · S elevated · dS/dA rising · L baf + · E **low at every accessible A** · G ≈WT | ✅ partially | ❌ EXCLUDES | ✅ partially | ⚪ silent | ⚪ silent | ✅ **REQUIRES. `MIXED = folding-primary`, degradation and aggregation both downstream.** ⭐ **This is the pattern the inherited structural verdict predicts for `Q230P`** |
| **R10** | A ≈WT · S ≈WT · E ≈WT · G ≈WT, for `Q230P` | ❌ EXCLUDES | ❌ EXCLUDES | ❌ EXCLUDES | ❌ EXCLUDES | ❌ EXCLUDES | ❌ EXCLUDES → 🔴 **No lesion detected in this system.** Either the tagged transgene does not reproduce the allele, **or** the original *"protein not detected"* was a **detection-floor / epitope artefact** (`D5`) — which this row makes a live, testable reading rather than a caveat |
| **R11** | 🔴 **E curve QUASI-LINEAR and non-saturating for `Q230P` where WT is hyperbolic** | ⚪ silent | ⚪ silent | ✅ **CORROBORATES `M2` from the engagement channel** — bystander transfer from crowding | ❌ **EXCLUDES — and this is the trap:** without the model comparison this reads as *preserved or even increased engagement* | ⚪ silent | ⚪ silent |

### 3.2 🔴 The orthogonal axis — the substitution series, which is a different question and must not be merged

The rows above are read **per allele**. The series is read **across** them, and it answers *what kind of
lesion*, not *what fate*:

| `Q230A` (side chain removed) | `Q230M` (amide removed, bulk kept) | `Q230P` (backbone) | reading | consequence |
|---|---|---|---|---|
| 🟢 ≈WT | 🟢 ≈WT | 🔴 affected | **PROLINE-BACKBONE-SPECIFIC** | 🔴 The hardest reading for any ligand or chaperone axis: **no ligand restores a hydrogen bond the chain cannot donate** |
| 🔴 affected | 🔴 affected | 🔴 affected | **SIDE-CHAIN POLAR NETWORK** | 🟢 A packing/network lesion of the class ligands and osmolytes can in principle shift — **and it falsifies the sequence model's preference for A over Q at 230** |
| 🟢 ≈WT | 🔴 affected | 🔴 affected | **amide hydrogen-bonding specifically** | Residue-resolved network lesion |
| 🔴 affected | 🟢 ≈WT | 🔴 affected | **volume / packing**, not chemistry | Points at core repacking |

🔵 **And the series does a second job that is the reason it is structurally required rather than merely
informative:** P5's source shows that **expression level sets aggregate rate and morphology**, so a transgene
pellet number is uninterpretable on its own. `Q230A` and `Q230M` are **the same protein, the same tag, the
same promoter, the same cells and the same induction** — they are the matched-expression baseline that makes
`Q230P`'s S and dS/dA mean something. 🔴 **Without them, every row of §3.1 that uses S is confounded by
over-expression.** ⚠️ `Q230G` is **excluded** throughout: it perturbs side chain **and** backbone at once.

---

## 4 · THE MINIMUM READOUT SET — and what each cut readout would have added

### 4.1 The rule, applied mechanically

**A readout stays only if there is at least one cell of §3.1 that no other readout can fill.** Applied to the
brief's six candidates, one at a time:

| candidate readout | cells it uniquely owns | verdict |
|---|---|---|
| **1 · total protein** | `R1`/`R2` vs `R5`/`R6` — the low-vs-normal abundance split — **and** it is the denominator without which `E` is not per-molecule | 🟢 **KEEP.** But note what it is: 🔴 **on its own it discriminates nothing**, because "low in a soluble lysate" is the shared observable of M1, M1′, M2 and a detection-floor artefact. It earns its place as the **denominator and the x-axis**, not as a discriminator |
| **2 · soluble/insoluble fraction** | `R3`, `R4`, `R9` — **and via `dS/dA`, the intrinsic-vs-dose-driven distinction in `R3` vs `R4`, which nothing else can see** | 🟢 **KEEP — highest-value single readout in the set.** `PREMISE: NOBODY_LOOKED` for every WWOX allele, and it owns the one cell that can stop a therapeutic axis |
| **3 · degradation KINETICS** (cycloheximide-chase `t½`) | 🔴 **NONE.** Row by row: `R1` vs `R2` is decided by **L**, not by `t½`; `R1` vs `R9` by **S**; `R5` vs `R1` by **A**. Every pair `t½` could separate is already separated | 🔴 **CUT** — see §4.2 |
| **4 · localisation** | 🔴 **NONE.** `R3`/`R4` are owned by **S** quantitatively; `R5` and `R10` both predict normal localisation | 🔴 **CUT as a discriminator; retained ONLY as a wild-type-only tag-qualification control** — see §4.2 |
| **5 · `POLE4` engagement** | `R5`, `R8`, `R9`, `R11` — **the entire function axis.** Without it there is no column M3a/M3b and no M4 | 🟢 **KEEP — the numerator** |
| **6 · `GSK3β` engagement** | 🟡 **Exactly one: `R6`.** It owns no mechanism column of its own | 🟢 **KEEP — by the minimum possible margin, and re-labelled.** See §5 |

**Plus one perturbation axis and one conditional add-on, neither of which is on the brief's list:**

| | | |
|---|---|---|
| **L — the lever panel** (30 °C · bafilomycin A1 · chloroquine · MG-132) | owns `R2` outright, and is the operative separator in `R1` | 🟢 **KEEP.** It is the **cheapest substitute for the cut kinetic readout, and the only one measurable at zero baseline** |
| **Pulse-and-Western folded fraction** | owns `R7` | 🟡 **CONDITIONAL.** Run **only** if the plate reads `R5`. Admitted because prediction **P6 was refuted** |

> ### 🟢 **THE MINIMUM SET: `A` · `S` (with its slope `dS/dA`) · `E` (with its curve-shape test) · `G`, all read at matched donor signal, across one lever panel, against the `Q230A`/`Q230M` ruler. Four measured quantities, two read types, one conditional add-on. Two of the brief's six candidates are cut.**

### 4.2 🔴 What each cut readout would have added — stated as a loss, not waved away

**Cut 1 — degradation kinetics (`t½` by cycloheximide chase).**

- **What is lost:** the **magnitude** of the turnover defect as a number with confidence intervals; the
  ability to compare `Q230P`'s route quantitatively with `P252A`'s; and the ability to say *"`t½` was
  restored from x to y"* after an intervention. **All three are post-hoc quantifications of a mechanism the
  set already assigns.**
- 🔴 **What is NOT lost, and the distinction is load-bearing: the degradation AXIS is retained in full.** I am
  cutting the **kinetic implementation**, not the mechanism. Block-and-rescue answers *"is clearance the
  bottleneck, and by which route"* — and **it is measurable at zero starting abundance, where a chase is
  not**. *You cannot chase a band you cannot see* is the repository's own `Caveat 2`, and it is the
  executability argument, not merely a preference.
- **What would re-admit it:** the design reaching `R1` or `R8` — i.e. a **measurable accumulated pool** —
  at which point a chase becomes interpretable and is the correct **second** experiment.

**Cut 2 — localisation.**

- **What is lost, and it is a genuine blind spot I am choosing to accept:** a **compartment/trafficking**
  mechanism that is **not among the four hypotheses at all** — for instance a failure of mitochondrial import
  in a protein this repository records as cytosolic/mitochondrial. **The minimum set would score such an
  allele as M3a (present, soluble, inert) and would be wrong about why.** 🔴 **Stated plainly as the cost of
  the cut.**
- **What is also lost:** the ability to see an aggresome directly, and the `P252A` LAMP1 co-localisation
  format.
- **Why the cut still holds, on three independent grounds:** (i) 🟡 **P3** — one punctum can be both an
  aggregate and a degradation-routing structure, so localisation *alone* cannot assign; (ii) assignment
  requires ≥3 co-stain channels (LAMP1 · LC3/p62 · an MTOC marker), which is not a compression; (iii) 🔴 the
  reagent floor — this repository records that *"commercial anti-WWOX antibodies did not show any specific
  signal for IF, prompting us to use a myc-WWOX"*, so endogenous localisation is not currently measurable and
  transgene localisation reports the tag as much as the protein.
- 🟢 **What is retained from it:** a **wild-type-only** localisation check in the mandatory two-terminus tag
  pilot. That is a construct-qualification step, **not a matrix column**, and it is not scored.

---

## 5 · THE MATCHED-ABUNDANCE METHOD — one chosen, and why the others lose

> ## 🟢 **CHOSEN: doxycycline-inducible expression titration from a SINGLE-COPY genomic landing pad in a WWOX-depleted human line, calibrated per allele to equalise NanoLuc donor luminescence — with the donor channel as the same-molecule denominator, and the ACCEPTOR titration run at that matched donor level as the saturation curve.**

**It is one method with three non-negotiable parts, and dropping any one of them breaks it:**

1. **Single-copy genomic integration**, not transient transfection. Transient delivery produces an enormous
   per-cell copy-number distribution; a population-average BRET at "matched mean dose" can be the average of
   a bimodal population. The landing-pad format — *"engineered 'landing pad' HEK 293T cells … resulting in
   **one variant per cell**"* ([DOI 10.1111/cts.12758](https://doi.org/10.1111/cts.12758)) — removes that
   variance. 🔴 **This is a construct FORMAT borrowed from that literature. It is NOT a MAVE: no library, no
   pooled selection, no sequencing readout, five arrayed constructs. §9 says so again.**
2. **Doxycycline titration as the calibration step**, run and read **before** any BRET measurement, whose only
   output is *"the dox concentration at which each allele's donor luminescence equals wild type's working
   level."* 🔴 **If no such concentration exists for `Q230P`, that is result row `R2` and it is an answer, not
   a failure** — see §7.
3. **The acceptor titration at matched donor** as the actual saturation curve, fitted for `BRET_max` and
   `BRET_50` **and** tested hyperbolic-vs-linear. Corrected from §2.2.

### 5.1 Why each alternative loses — stated as a mechanism of failure, not a preference

| alternative | why it loses |
|---|---|
| **Plasmid-dose titration** | 🔴 **It matches the INPUT, not the quantity the question is about.** A construct that is degraded yields *less protein at the same dose* — which is precisely the variable being controlled for, so "matched dose" is systematically **not** matched abundance, and the error is **largest for exactly the allele of interest**. Compounded by construct-dependent transfection efficiency and by the copy-number spread of (1) |
| **Quantitative IP / matched-input co-IP** | 🔴 **You cannot match an input you cannot measure.** The immunoblot floor is the exact instrument that produced *"protein not detected"* for `Q230P`. Its denominator is unavailable for the one allele the experiment exists for. Secondarily, wash steps discriminate against weakened interactions non-linearly, so the numerator is biased in the same direction as the lesion |
| **Luminescent complementation (NanoBiT / split reporters)** | 🔴 **The tag fragments carry intrinsic affinity for each other**, which can (i) *rescue* a weakened interaction — masking the exact defect being measured — and (ii) stabilise the tagged protein, corrupting the denominator as well as the numerator. **A reporter that can repair the phenotype is the wrong instrument.** Not validated for any WWOX pair. ⚠️ Kept out **by name** because the brief lists it as *"if validated"* and it is not |
| **"Normalised interaction signal per WWOX molecule"** | 🟡 **This is not a method — it is the QUANTITY.** Naming it as an option is a category error: it still needs an implementation, and the implementation is what the choice is about. It is what the chosen method *produces* |
| **Purified-protein specific activity per mole folded monomer** | 🔴 **Unavailable at any price today.** No purified folded WWOX SDR exists; expressing one is itself an unsolved problem in this literature, and WWOX has no validated substrate |
| **Endogenous knock-in at the WWOX locus, patient or isogenic** | 🟢 **Scientifically superior and it is the honest right answer for the ABUNDANCE question** — and it loses **this** contest for one reason: 🔴 **to control abundance you must be able to SET it, and an endogenous locus cannot be titrated.** ⚠️ Over-expression is a confound for the abundance question and an **enabler** for the per-molecule question. That trade is argued here, not hidden — and §7 states what it costs |

### 5.2 🔴 The honest limit of the chosen method, which no prior file states

**Matched abundance is only reachable inside the overlap window.** If `Q230P`'s maximal attainable donor
signal lies **below** wild type's usable working range, **there is no matched point** and the per-molecule
comparison cannot be made at all. ⇒ **The dox calibration must report the overlap window as a primary
result**, and an empty overlap is row `R2` — reached **by elimination**, which is weaker evidence than
measurement, and must be labelled as such wherever it is reported.

---

## 6 · PARTNER-CHANNEL VERDICT — two channels, and only one of them is a numerator

> ## 🟢 **KEEP TWO. But they are NOT co-primary numerators. `POLE4` is the numerator; `GSK3β` is the RULER. The matrix forces this, and it is a correction to the inherited co-primary call.**

**The argument is the cut rule, applied to `G`:**

- **`G` owns exactly one cell — `R6`** — and it owns **no mechanism column**. A *low* `G` means *something
  global is wrong*; a *normal* `G` means almost nothing, because 388–407 is a **linear docking motif at the
  extreme C-terminal end of the span, 174 residues from `Q230`, and whether presenting it requires the SDR
  core fold has never been measured.**
- 🔵 **That asymmetry is exactly what a ruler is.** ⇒ **`G` is used only in its strong direction (loss ⇒
  global) and never in its weak direction (normal ⇒ folded).** 🔴 **A normal `GSK3β` curve for `Q230P` is
  WEAK evidence of an intact fold and this design does not use it as evidence of one.**
- **It cannot be cut**, because without it `R5` (a specific engagement lesion — M3a) and `R6` (global
  collapse or a broken construct) **are the same observation**, and the design would report a mechanism where
  it had a reagent failure.
- 🔴 **A wild-type control does not substitute for it.** WT-normal shows the *architecture* works **for WT**.
  `G` on the **same `Q230P` molecules** is the only within-allele control there is.

**Two things the reassignment buys that the co-primary framing did not:**

1. 🟢 **It tests its own premise for free.** If `G` is **low for `Q230P`** while WT, `Q230A` and `Q230M` are
   normal, that is the first evidence anyone has that **SDR core folding is required for 388–407
   presentation** — converting `PREMISE: UNVERIFIED` into a measurement, at no extra cost. If `G` is normal
   across the board, the ruler is behaving as a fold-insensitive control, **and the plate finds that out by
   itself**.
2. 🟢 **It resolves the ±UV collision by demoting it from a design-breaker to a gate.** Every WWOX–`POLE4`
   measurement in existence was made **after UV**, and UV perturbs the same stress pathways as the 30 °C and
   bafilomycin arms — so `POLE4` and the levers cannot be co-equal partners in the same wells. As a
   **numerator with a ruler**, the ±UV question becomes a **wild-type-only pre-test** (§7 Step 0) rather than
   a full factorial arm.

🔴 **What `POLE4` does NOT bring, carried forward verbatim so no score is rounded up:** its binding site on
WWOX is **unmapped** (`SDR` / `short-chain` / `dehydrogenase` = **0** in the body); "SDR-span" is the
**reader's arithmetic** from `P282A`'s position, not the authors' claim; the authors write that *"the precise
molecular mechanism underlying the loss-of-function of the WWOX P282A variant is still unknown"*; and
`P282A`'s own credential is now **`OVEREXPRESSION-ARTEFACT SUSPECT`**. 🔴 **`P282A` is therefore on the plate
as a DIRECTION and never as a magnitude, and the plate's sensitivity claim rests on the `Q230A`/`Q230M`
series instead.** According to PubMed, the `POLE4`, `P282A`, `P252A` and `HSC70` facts inherited here are
from Zhang *et al.* 2025, *Adv Sci* 13(1):e07602, PMID 41124647,
[DOI 10.1002/advs.202507602](https://doi.org/10.1002/advs.202507602), read by prior actors and not by me.

🔴 **`HSC70` is NOT in the minimum set**, and cutting it is a departure from the inherited design. Applying
the rule: its two informative readings are *"flat engagement + HSC70 positive ⇒ misfolded and being
cleared"* and *"flat engagement + HSC70 negative ⇒ stable and inert"* — **and `S`, `dS/dA` and `L` already
separate those**, at higher resolution and without a co-IP. **What is lost:** the degron-surface-exposure
sign, and the only figure in the WWOX literature carrying both poles of the `P252A`/`P282A` dissociation
side by side. 🟡 **It is the strongest candidate for the first thing added back if a channel becomes free.**
⚠️ And the repository's bound rides with it: `KFERQ`-like `LRSVQ` 187–191 is **predicted and never mutated**,
`LAMP2A` never manipulated — so the route is *lysosome-dependent, proteasome-independent*, **not** CMA.

---

## 7 · THE ONE COMPRESSED EXPERIMENT, fully specified

> ## 🟢 **One cell line, five constructs, two acceptors, one instrument, one lever panel, one fractionation — and the levers are read on the DONOR channel only, which is what makes it one experiment instead of a programme.**

### 7.0 The compression argument, in one sentence

**`L` is a readout on `A`, not on `E`** — the levers exist to establish *whether a matched abundance is
attainable at all*, and engagement only ever needs measuring **at** the matched abundance. ⇒ **the full
acceptor titration is run once, at matched dox, and not under every lever.** That single observation cuts the
plate roughly four-fold against the inherited design and loses no cell of §3.1.

### 7.1 Material

| | |
|---|---|
| **Host** | A **WWOX-depleted** human line carrying a **single-copy genomic landing pad** under Tet-On control. Endogenous WWOX competes for partners and its own level varies; a landing pad removes copy-number variance. 🔴 **A proliferating line — see §9** |
| **Donor constructs (5)** | NanoLuc–WWOX **`WT`** · **`Q230A`** · **`Q230M`** · **`Q230P`** · **`P282A`**. 🔴 **`Q230G` is excluded** (perturbs side chain **and** backbone). 🔴 **`P282A` is a DIRECTION, never a magnitude** |
| **Acceptor constructs (2)** | HaloTag–**`POLE4`** (117 aa — the numerator) · HaloTag–**`GSK3β`** (420 aa — the ruler) |
| **Levers** | 30 °C · bafilomycin A1 · chloroquine 40 µM/24 h · MG-132 (expected negative) · vehicle. 🔴 **Bafilomycin is non-optional:** chloroquine alone has been reported negative where bafilomycin was strongly positive on endogenous protein in primary fibroblasts, so a CQ-only negative **is not interpretable as "not the lysosome"** |
| **Deliberately absent** | 🔴 No 4-PBA/TUDCA (wrong compartment) · no NAD(P)/cofactor arm (**the sign inverts with cofactor occupancy and WWOX's occupancy is unknown**) · no ±UV factorial (gated at Step 0) · no `tau` (`INDETERMINATO`) · no `Zfra` (it changes the denominator) · no CHX chase · no pulse-label · no MD, docking or purified protein |

### 7.2 Step 0 — two gates, wild type only, before any allele is scored

| gate | what is run | what fails it |
|---|---|---|
| **G0a · tag pilot** | N- **and** C-terminal NanoLuc placements on `WT`, scored on localisation and on wild-type engagement to both acceptors | Both termini mislocalise `WT` or abolish `WT` engagement ⇒ **F2**, fall back to §5's matched-input co-IP and accept its denominator loss |
| **G0b · ±UV gate** | `WT` donor + `POLE4` acceptor, **without UV** vs after UV | 🔴 No constitutive `WT`–`POLE4` engagement ⇒ **F1**. The numerator is UV-dependent, it cannot share wells with the lever arms, `GSK3β` becomes the sole numerator and **rows `R5`/`R6` lose their resolution.** This is the design's largest single unknown and it is tested first, on four wells |

### 7.3 Step 1 — the matched-abundance calibration (donor channel only)

**5 alleles × 8 doxycycline concentrations × 3 biological replicates = 120 wells.** Read **NanoLuc donor
luminescence only.** No acceptor, no BRET.

**Primary outputs, both of which are results in their own right:** (i) the dox concentration at which each
allele's donor signal equals wild type's working level; (ii) 🔴 **the OVERLAP WINDOW.** An empty overlap for
`Q230P` is row **`R2`**, reached by elimination — **weaker than measurement, and labelled as such**.

### 7.4 Step 2a — the lever panel and the fractionation (donor channel only)

**5 alleles × 5 conditions × 3 replicates = 75 wells**, at matched dox plus a 4-point dox sub-series for the
slope. From every well:

- **`A`** — donor luminescence per cell, ± each lever.
- **`S`** — non-denaturing lysis, spin, SDS/urea-resolubilised pellet vs supernatant, **quantitative Western
  against the TAG epitope, not against WWOX.** 🔵 **This is a deliberate and consequential choice:** it gives
  one validated antibody, one epitope, identical for every allele — which sidesteps both the repository's
  record that commercial anti-WWOX antibodies are unreliable **and** the `D5` concern that an anti-WWOX
  epitope might overlap the distorted 226–240 segment. ⚠️ **Its own failure mode, named:** a tag-epitope blot
  reports the **tag**, so a truncated WWOX carrying an intact tag would be miscounted ⇒ **score by band size,
  not by signal alone** (**F8**).
- **`dS/dA`** — the slope of `S` across the 4-point dox sub-series. 🔴 **The quantity that separates `R3` from
  `R4`, i.e. "aggregation is why abundance is low" from "raising abundance is what makes the aggregate", and
  it exists in no prior design in this repository.**

🔴 **Step 2a can stop the experiment.** A `Q230P`-specific elevated `S` that `Q230A` and `Q230M` do not show
is the aggregation branch, on a matched-expression internal comparator — and no engagement number is worth
reading until that is known.

### 7.5 Step 2b — the saturation curves, at matched abundance

**5 alleles × 2 acceptors × 6 acceptor points × 3 replicates = 180 wells — one 384-well plate.** Donor held
**constant** at the Step-1 matched dox; **acceptor titrated**; x-axis = acceptor ÷ donor. Run at vehicle, and
repeated at **the one lever that Step 2a showed to work**, if any.

**Fit each curve to BOTH models and report the comparison:**

| fit | meaning |
|---|---|
| **hyperbolic, saturating** ⇒ report `BRET_max` and `BRET_50` | specific engagement. `BRET_max` ÷ wild type's = **`E`** |
| 🔴 **quasi-linear, non-saturating** | **bystander transfer from crowding/aggregation — row `R11`.** 🔴 **Without this test it reads as preserved or increased engagement, which is the single most dangerous misreading available on this plate** |

### 7.6 Step 3 — the conditional add-on, and the only thing not on the plate

**Trigger: the plate reads `R5`** (abundance ≈WT, solubility ≈WT, `E` low, `G` normal, curve hyperbolic).
**Then, and only then:** pulse proteolysis + quantitative tag-epitope Western on the matched-donor soluble
fraction across a urea series → **fraction folded and `C_m`**, separating `M3a` (folded and inert — no
stabiliser helps) from `M3b` (soluble, unfolded and inert — a folding-directed lever is at least
on-mechanism). 🔴 **Admitted only because prediction P6 was refuted**; it is the one physical stability
measurement WWOX can support without purified protein.

### 7.7 Read order — and why it is not negotiable

```
G0a tag pilot ─┐
G0b ±UV gate ──┴─▶ Step 1 dox calibration ─▶ Step 2a  A · S · dS/dA · L   ◀── CAN STOP HERE
                                                 │
                                                 ▼
                                          Step 2b  E · G · curve shape
                                                 │
                                                 ▼
                                          Step 3 (only if R5)  folded fraction
```

**Every arrow is forced by the matrix, not by convenience.** `E` is defined only at matched abundance, so
Step 1 must precede Step 2b. `S` can invalidate the denominator, so Step 2a must precede Step 2b. And the two
gates must precede everything, because a broken tag or a UV-only numerator makes every downstream number
uninterpretable.

### 7.8 What this experiment is NOT

🔴 **It is not a function assay.** WWOX has **no demonstrated physiological function, no assigned substrate
and no validated cellular activity readout.** `E` is **engagement competence per molecule** — a proxy — and
a report of this experiment must say so. **`STABILITY CANNOT PROXY FUNCTION`, and neither can engagement
prove function.** 🔴 **It is not a MAVE and not a sensor programme:** five arrayed constructs, no library, no
pooled selection, no sequencing readout — only the *integration format* is borrowed from that literature.
🔴 **It is not the endogenous allele**, and it says nothing about neurons, myelination, the developmental
window, seizures or clinical course. 🔴 **It is not medical advice, and no molecule, dose, route, prognosis
or safety claim follows from any part of it.**

---

## 8 · WHAT WOULD FALSIFY THE DESIGN — stated as observations, not doubts

| # | observation | consequence for the design |
|---|---|---|
| **F1** ⭐ | **`WT` NanoLuc-WWOX shows no `POLE4` engagement without UV** (gate G0b) | 🔴 The numerator is a **stress-dependent assembly** and cannot share wells with the lever arms. `GSK3β` becomes sole numerator, **`R5` and `R6` collapse into one row**, and the M3a/M3b axis is lost. **The largest single unknown in the design, and the first thing tested** |
| **F2** | **Both NanoLuc terminal placements mislocalise `WT` or abolish `WT` engagement** | Fall back to matched-input co-IP + targeted MS for the denominator, accepting that the floor that produced *"not detected"* returns |
| **F3** | **No dox concentration brings `Q230P` into wild type's working range** — empty overlap window | The per-molecule question is **unanswerable in this system**. The result is `R2` **by elimination**, and must be reported as elimination, not measurement |
| **F4** | **`Q230A` AND `Q230M` both read as affected as `Q230P`** | 🟡 The series stops being a backbone-vs-side-chain discriminator **and the matched-expression solubility comparator is lost with it** — every `S` number becomes over-expression-confounded again. ⚠️ **The finding itself is valuable** (side-chain-network lesion, a ligand-shiftable class) but the design loses its internal ruler |
| **F5** | **Wild type itself partitions into the pellet at the working induction** | 🔴 The solubility axis is **saturated by over-expression artefact**. Lower the induction until `WT` is fully soluble; if no such window exists, **the solubility question returns to patient fibroblasts and this design cannot answer it** |
| **F6** | **`GSK3β` engagement is absent or non-saturating for `WT`** | The ruler is unavailable ⇒ `R5` and `R6` are indistinguishable ⇒ **no M3 call may be made** from this plate |
| **F7** | **A published WWOX cellular readout appears meeting the `PMID 28540421` standard** (active-site **and** cofactor-site mutants each abolishing it) | 🟢 That readout **outranks every engagement channel here**, because it would be demonstrated function rather than a proxy. The numerator should be replaced |
| **F8** | **The tag-epitope Western shows intact-tag bands at anomalous size** | The denominator is counting tag, not WWOX ⇒ score by size, add an anti-WWOX confirmation lane, and treat every `S` number as provisional until it resolves |
| **F9** | 🔴 **The whole design** — a demonstration that WWOX is an obligate **holo** protein with a measured cofactor `K_d` | Then the apo monomer that every inherited geometry number rests on is the wrong conformation, folding and cofactor capture are one reaction, and a **cleft-ligand arm** — currently refused because *the sign inverts with occupancy* — becomes the lead experiment instead of a forbidden one |

---

## 9 · WHAT I COULD NOT ESTABLISH

| # | open item | why it did not resolve | cheapest move |
|---|---|---|---|
| **1** ⭐ | **Whether `Q230P` protein exists at all in a patient cell** | 🔴 **This design cannot answer it, and that is the price of choosing the transgene.** It answers the *per-molecule* question; the *endogenous abundance* question stays with the fibroblast blot | The soluble/pellet blot on `Q230P` patient fibroblasts. ⚠️ `HUMAN_REQUIRED` — material availability is `PREMISE: UNVERIFIED` |
| **2** ⭐ | **Whether WWOX–`POLE4` engagement exists without UV** | 🔴 `without UV` / `no UV` / `untreated` / `mock` = **0** in the only body. Not searchable further from here | Gate G0b — four wells. **It is inside the experiment, which is the correct place for it** |
| **3** | **Whether 388–407 presentation requires the SDR core fold** | `PREMISE: UNVERIFIED`; never measured for any allele | 🟢 **The design tests it for free** (§6). No extra cost |
| **4** | **Whether `Q230P` fibroblasts, or an isogenic knock-in pair, are obtainable** | Not a scientific question and not mine to act on | `HUMAN_REQUIRED` **H-4** below. **No external action was taken** |
| **5** | **The body of PMID 29808465** — both `Q230P` data points remain `abstract-depth` | `pmc_id: null`, closed at Springer, `unrecoverable_by_these_routes` on three prior independent checks; **not re-attempted here** | `HUMAN_REQUIRED` **H-1**. 🔴 The antibody **epitope** is the datum that decides whether `D5` is live, and row `R10` is the only place this design can see it |
| **6** | **Whether WWOX binds NAD(P), and in which redox state** | PMID 21476439 `PREMISE: UNREAD_PRIMARY`, no PMCID | `HUMAN_REQUIRED` **H-2**. It gates **F9** |
| **7** | **Whether the solubility partition of ANY protein has been calibrated by a same-position substitution series** | 🟡 **P4 refuted for abundance, unresolved for solubility.** The Mpro precedent measured function and abundance, **not** the partition | An open gap, recorded as one. The design would produce the first such calibration for WWOX |
| **8** | **Whether NanoLuc's own protease resistance permits a luminescent pulse-proteolysis readout** | `IPOTESI`, untested anywhere I looked | A one-afternoon control on `WT`: proteolyse, read luminescence **and** blot, compare. **Would collapse Step 3 onto the plate if it worked** |
| **9** | **The magnitude of the abundance contribution in the Mpro rheostat study** | 🔴 An extractor that strips hyphens made `~4–5-fold` and `~45-fold` the same string | **Discarded rather than guessed.** Only the qualitative claim is used |
| **10** | **Anything about neurons** | Every host cell available for this format is a proliferating line; and the published instance of a disease-relevant insoluble species forming **only in patient neurons and not in the same patients' fibroblasts** means a negative `S` in any non-neuronal system **cannot close the aggregation branch** for the disease-relevant cell type | An unresolved, structural limit. Recorded, not solved |

### 9.1 `HUMAN_REQUIRED` — parked, not pursued. **No external action was taken.**

🔴 **No email was sent, no author or laboratory was contacted, no material was requested, no purchase was
made, and no molecule, dose or route is recommended anywhere in this file.**

| # | item | why it needs a human |
|---|---|---|
| **H-1** ⭐ | Obtain **PMID 29808465** (Johannsen 2018) — specifically **the antibody and its epitope**, plus n, controls, densitometry and the qRT-PCR amplicon position | Both experimental facts about **the most recurrent WWOX allele in the disease — 8 patients, 6 families** — are `abstract-depth`. The epitope decides whether `D5` is live and whether row `R10` has a second reading |
| **H-2** | Obtain **PMID 21476439** — the only WWOX enzymology paper ever published | The only source that could say whether WWOX binds NAD(P). It gates falsifier **F9** |
| **H-3** | Obtain **Figure S9 (Supporting Information) of PMID 41124647** — `P252A`'s `POLE4` co-IP | Still the highest-value unopened item for the numerator's credential |
| **H-4** | Confirm whether **`Q230P` patient-derived fibroblasts or an isogenic knock-in pair** exist and are obtainable | The endogenous half of the question (§9 item 1) cannot run without material, and this design deliberately does not depend on it |
| **H-5** | 🔴 **A PROGRAMME DECISION, not a task: whether to commission a WWOX activity readout meeting the `PMID 28540421` standard.** This file deliberately does **not** propose one | It is the only development that would replace engagement-as-proxy with demonstrated function (**F7**). Stating it as `HUMAN_REQUIRED` is the correct output here, not a workaround |

---

## 10 · GRADE — conservative, per item

| item | grade | justification, and what it is NOT |
|---|---|---|
| **The pattern × mechanism matrix (§3)** | **C — novel connection** | It reorganises readouts the repository already holds into a form in which the cut rule is computable. 🔴 **Not D:** it generates no new hypothesis by itself |
| **The two cuts, with their stated losses (§4)** | **C** | The *argument* is new here; both readouts were already in prior designs. **Not graded higher because a cut is a subtraction** |
| **`dS/dA` — the partition shift (V5)** | **D — novel testable hypothesis** | Separates *"aggregation causes the low abundance"* from *"raising abundance creates the aggregate"* — two readings with **opposite therapeutic signs** that the repository currently cannot tell apart. Zero occurrences in the tree. Rests on `P5`, which is `passage-depth` and from polyglutamine biology, not WWOX |
| **The bystander-BRET curve-shape test (`R11`, §7.5)** | **D** | Turns a confound that would have been read as *preserved engagement* into a **free second aggregation readout**. 🔴 **Arrived by a REFUTATION of my own minimality claim**, which is the only reason it is in the file |
| **The donor-axis / acceptor-axis correction (§2.2)** | **C** | A **correction to an inherited design**, from a protocols body. Corrections are not discoveries |
| **Tag-epitope Western as the fractionation readout (§7.4)** | **C** | Sidesteps the anti-WWOX antibody floor **and** the `D5` epitope concern with one substitution. Method-level, and it carries its own failure mode (**F8**) |
| **`GSK3β` demoted from co-primary numerator to ruler (§6)** | **C** | A re-derivation from the matrix of a partner set another actor assembled. **The reagents are theirs; the assignment is mine** |
| **The same-position series as the matched-expression solubility comparator (V3)** | **C, not D** | 🔴 **Downgraded because P4 was REFUTED:** the same-position-series-with-separate-abundance-measurement design is published. `CROSS-DOMAIN-DERIVED`, not agent-novel. Its application to the **solubility partition** is the part that remains unfound |
| **The compressed experiment (§7)** | **E — experiment-generating** | Fully specified, executable, gated, falsifiable, with a stated read order and a stop condition |
| **Therapeutic expansion** | 🔴 **NOT GRADED F, and explicitly so** | Nothing here is a therapy, a therapeutic class or a therapeutic recommendation. The brief warned against grading F merely because it asked about a therapy, and the warning applies |

---

## 11 · Declared limits of this file

🔴 **Non-canonical.** No registry, queue, ledger, receipt chain, state manifest or `*_current.md` was written.
No `BATCH_COMMIT`. **No git command was run.** One file was created: this one. It proposes; the Orchestrator
verifies and lands.

**Read depth.** Every external item is **`passage-depth`** via `Scholar_Gateway semanticSearch`, whose
`ai_generated` summary was not used and is not evidence, plus **one PubMed metadata record** (PMID 41124647).
🔴 **No body was read in full by me in this act. No `FULLTEXT_READ_RECEIPT` is claimed and none is owed.**
No figure panel was inspected. Other actors' files are cited as **their** attestations, never as my readings.

**Self-contamination.** Every repository count in §1.8 was taken **before this file existed**; no count
anywhere above was obtained by grepping a tree containing this file.

**Certainty classes are held apart throughout.** `EXPERIMENTAL` (Zhang 2025's co-IPs; Lou 2018's activity
losses; the `rs3764340` genotype counts) · `HOMOLOGY` (the SDR fold family) · `MODEL` (the AlphaFold monomer,
every distance, every ΔΔG) · `INFERENCE` (every row of §3.1 that has not been measured). **A prediction is
never a measurement.** **Prediction ≠ measurement; abundance ≠ stability ≠ solubility ≠ function**, and the
matrix exists precisely to keep them apart. `NOBODY_LOOKED` ≠ `UNREAD_PRIMARY` ≠ `UNVERIFIED`.

**No cross-variant generalisation.** `Q230P` ≠ `Q230A` ≠ `Q230M` ≠ `P282A` ≠ `P252A` ≠ `G372R` ≠ `P47T` ≠
`A141T`. Every transfer from another gene (`NPC1`, `SOD1`, polyglutamine, Mpro, H-ras, 7α-HSDH, CBR3) is a
**method or pattern transfer only**, never a disease conclusion, and the firewalls travel with each one.

**A `DISCOVERY` is not a `CANDIDATE` and not `CANONICAL`.** `dS/dA`, the `R11` reading, the `M3a`/`M3b` split
and the `GSK3β` reassignment are `IPOTESI` throughout.

**Nothing in this file is medical advice.** No molecule, dose, route, prognosis or safety claim is
recommended anywhere above. No prognosis attaches to a genotype class, and this file makes none.

---

**END OF FILE — `q230p_direct_discriminator_20260922.md`.** Sections present: inherited bounds §0 ·
prospective `DISCOVERY_TRACE` §1 (persisted before targeted search; `RESULT` appended at §2 with **two
refuted predictions recorded as refuted and one recorded as not scoreable**) · the searches and the traps
§2 · **the hypothesis × readout discrimination matrix §3** · the minimum readout set and the cost of each cut
§4 · the matched-abundance method and why the alternatives lose §5 · the partner-channel verdict §6 ·
**the one compressed experiment §7** · what would falsify the design §8 · what could not be established and
the `HUMAN_REQUIRED` park §9 · the grading §10 · declared limits §11.

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V0 · The declared protocol breach

One read-only `git status --porcelain`, self-declared before I asked. Nothing staged, committed or
branched; no canonical, registry, queue, ledger or manifest file touched — confirmed against the
working tree. **Accepted, recorded, not repeated.** Declaring it unprompted is the behaviour the
rule exists to produce.

## V1 · 🔴 The axis correction is CONFIRMED verbatim against the primary methods source

I verified it myself rather than on the delegate's attestation. Hamdan FF, Percherancier Y,
Breton B, Bouvier M, *Monitoring Protein-Protein Interactions in Living Cells by Bioluminescence
Resonance Energy Transfer (BRET)*, *Curr Protoc Neurosci* 2006;34(1):5.23.1–5.23.20,
[DOI](https://doi.org/10.1002/0471142301.ns0523s34) — passage-depth, publisher-side surface:

> *"…so-called 'BRET titration curves,' where the **Rluc fusion protein is kept constant while the
> concentration of the expressed energy acceptor fusion protein is increased**."*

> *"The BRET₅₀ is calculated as the **amount … of acceptor divided by the amount of donor** required
> to obtain 50% of the maximal BRET signal."*

🟢 **CONFIRMED.** The inherited design in `wwox_engagement_partner_adjudication_20260922.md` §5.1
describes a *"donor-saturation NanoBRET architecture"* with fitted `BRET_max`/`BRET_50` against
the **donor** channel. **Donor titration is the abundance calibration; acceptor titration at fixed
donor is the saturation curve. They are two experiments on two axes and the design conflated
them.** The correction is free to adopt and the plate is not executable without it.

The bystander discriminator is likewise verbatim: specific BRET *"increases hyperbolically and
rapidly saturates"*, bystander *"increases almost linearly and may eventually saturate only at very
high levels."* 🟢 **CONFIRMED** — so `R11` is a real free readout, not an analogy.

## V2 · 🎯 A SECOND free discriminator in the same curves, which this file did not take

The same source, two paragraphs on (citing Percherancier 2005):

> *"In the case of **affinity changes** … the calculated BRET₅₀ should change … but the **maximum
> BRET signal attained at saturation should remain constant**. In the case of a **conformational
> change** where the affinity … is not changed, the **BRET₅₀ should remain constant and only the
> maximum BRET is expected to change**."*

**`BRET_50` and `BRET_max` are separate channels, and the file's quantity `E` currently merges
them into one number.** Split, on data the plate already collects:

| `BRET_50` | `BRET_max` | Reading for `Q230P` |
|---|---|---|
| right-shifted (larger) | unchanged | **affinity loss** — the binding surface or the fold that presents it is compromised |
| unchanged | changed | **geometry change within a complex that still forms at wild-type affinity** — a conformational lesion, not an engagement lesion |
| both change | | mixed, or an orientation change accompanying affinity loss (the source names this case explicitly) |

This matters because the matrix's `M3a` (**folded and inert**) currently has to be reached by
elimination. A `BRET_50`-unchanged / `BRET_max`-changed result is **positive** evidence for it.

⚠️ **Two constraints that come with it, both from the same source, both binding:**
1. 🔴 *"when the energy donor and acceptor are very close, subtle variations in the BRET signal may
   be missed, since that BRET signal is already at its saturation plateau (zone 1)."* **The
   conformational channel is unreadable if the tags sit too close.** The two-terminus tag pilot
   the design already mandates is therefore not only about fusion tolerance — it decides whether
   this second channel exists at all. Score the pilot on that too.
2. 🔴 `BRET_50` comparison is valid only *"provided that proteins B and C are expressed to the same
   levels in the titration curve."* The landing-pad calibration in §5 equalises **donor**
   luminescence per allele. **`BRET_50` comparison across alleles additionally requires the
   acceptor titration series to be matched across allele plates** — a different matching
   requirement, cheap to meet (one shared acceptor dilution series) and invalidating if missed.

## V3 · What I endorse without amendment

🟢 **The two cuts.** Degradation kinetics and localisation each own zero cells; *"you cannot chase
a band you cannot see"* is the correct reason, and the blind spot the localisation cut creates
(a trafficking lesion misscored as `M3a`) is stated rather than hidden. 🟢 **`G` as a ruler, not a
numerator**, used only in its strong direction — this corrects an inherited co-primacy call and
does so by applying the file's own cut rule to itself. 🟢 **Fractionation blotted against the tag
epitope, not WWOX**, with its failure mode named. 🟢 **`dS/dA`** is the genuinely new quantity and
the sign argument behind it (intrinsic vs dose-driven aggregation ⇒ **opposite therapeutic signs**)
is the most decision-relevant thing in the file. 🟢 **`Q230G` excluded throughout**, per the
standing constraint.

## V4 · Grades

**E** for the experiment, **D** for `dS/dA` and the bystander curve-shape test, **C** for the rest —
endorsed unchanged, and the refusal to grade anything **F** is correct: no therapy, class or
recommendation appears anywhere in the file.

I note the one that should be read first: **`P7` was scored SUPPORTED and it refuted the delegate's
own minimality claim**, and the repair — turning the confound into a second readout — is worth more
than the claim it destroyed. Two of the file's three highest-value items arrived by self-refutation.

**No row is canonical; none is proposed for `BATCH_COMMIT` here.** The V2 split is offered as an
amendment to the design, not as a finding about `Q230P`, about which this file correctly concludes
that **we do not know whether the protein exists.**
