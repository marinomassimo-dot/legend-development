# Generative hypothesis cycle — two DISCOVERY_TRACEs on WWOX-DEE

**Actor:** Scientist H · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Status:** NON-CANONICAL ANALYSIS. This file touches no `*_current.md`, no registry, no queue, no
ledger, no receipt chain and no state manifest. No `BATCH_COMMIT` was run. **No `git` command was
executed, not even read-only.** No external contact, no purchase, no quotation — all `HUMAN_REQUIRED`.
**Nothing here is medical advice, and nothing here is a treatment proposal.** No molecule is named
as a therapy, no dose, no route, no compound screen. A mechanistic hypothesis is not a treatment.
**Alleles and models are never pooled.** `Wwox`-null · `gt/gt` · `P47T` · `S-KO` · `N-KO` ·
`lde/lde` · human WOREE · human SCAR12 are distinct throughout and are never merged into a sentence.

> **Why this file exists.** The session that produced its seed material was overwhelmingly a defect
> hunt — withdrawn premises, misnamed buffers, unmapped antibodies, blind measurements. That work
> was needed. This file is the other half: it is asked to *generate* mechanism the model does not
> hold. It is graded not by how interesting a hypothesis sounds but by whether it changes which
> experiment a real scientist should do next.

---

## 0 · Ordering declaration, and the reason it is the experiment

🔴 **§§ 1.1–1.6 and 2.1–2.6 below were written to disk in a single act, as the first content of this
file, before a single external query was issued.** Everything from `RESULT` onward in each cycle was
appended later. **No prediction below was edited after evidence arrived.** Where a prediction was
wrong it is marked wrong and left standing; a refuted prediction is a good outcome and a
reconstructed one is worthless.

**Novelty protocol, fixed here before use.** For every hypothesis, the repository is checked by
(1) **enumeration** — `find` / `ls` over all 1,451 tracked files, and specifically over all 154
files of `disease-models/wwox/analysis/`; then (2) **UNSCOPED grep** — no `--include`, because this
laboratory has already established today that a phrase living inside a JSON string field is
invisible to a Markdown-scoped grep (failure mode 9), and that a census returns a uniform zero when
the question was asked of the wrong document class (failure mode 10). The repository holds 908 `.md`,
170 `.json` and 17 `.jsonl` files; a grep that sees only the first class sees 60% of the evidence.

**Three candidate lines were enumerated, checked, and KILLED as `REDISCOVERY` before writing.**
They are recorded here rather than silently dropped, because a generative cycle's negatives are
part of its output and because each was, to me, a genuinely attractive idea:

| Killed candidate | Why it is not novel |
|---|---|
| **Cofactor-assisted folding** — that WWOX's SDR is a holo-stabilised protein, so NAD(P) occupancy sets its abundance, and a cofactor-cleft ligand would stabilise it at a site remote from the `ERLIQ 402–406` degron, escaping the "stable but inert" trap | 🔴 **Fully held.** `q230p_therapeutic_mechanism_expansion_20260922.md` carries it as `D4`, tests it as `P2`, **confirms it** from `NmrA` (Tm 48.0→51.6 °C, and the destabilised variant rescued *more*, 38.0→43.8 °C) and from `SDRvv`, ranks it 🥇 RANK 1 — **and then kills it** with the AKR sign-inversion result: the sign of a stabiliser flips with cofactor occupancy, and WWOX's occupancy is unknown. I would have re-derived a conclusion the repository already reached *and already refuted*. |
| **Mitotic dilution of episomal AAV genomes in the postnatally-dividing cerebellar granule lineage** | 🔴 **Fully held**, twice: `cerebellum_layer_localisation_20260922.md` § 8 `H2`, and `purkinje_cerebellar_celltype_wwox_census_20260922.md` `P2`, the latter explicitly labelled *"NOT NEW — this is the sibling file's H2"* and carrying a better falsifier than I had (an **integrating** reporter co-delivered with the episomal one). |
| **A frameshift product with an aberrant C-terminus from `c.1057-2A>G`, degron-less and therefore hyper-stable, selectively dead in the `388–407` GSK3β-docking limb while `WW1`/`WW2` stay intact** | 🔴 **Excluded by reference sequence, not merely anticipated.** `exon9_cryptic_acceptor_test_20260922.md` establishes that the surviving outcome is the cryptic acceptor at `c.1063` giving **`p.Gln353_Gln354del`** — an **in-frame two-residue deletion with no PTC at all**. There is no frameshift and no aberrant C-terminus to reason about. The 8-nt frameshift reading is *"dead by reference sequence"*. My hypothesis had a false premise and the repository had already killed it. |

🔵 That is three attractive ideas dead before a word of hypothesis was written. It is the intended
cost of the novelty protocol, and the ideas that survived it are the two below.

---

# § 1 · TRACE CYCLE 1 — *is the effector limb of this model gated by an isoform nobody recorded?*

## 1.1 OBSERVATION

Three facts sit next to each other in this repository and have not been put together.

1. **DATO.** Tau is not a bystander in the WWOX pathway — it is the **obligatory effector**. Wang
   2012, PMID `22193544`, `PMC3354054`, Results, verbatim as re-read by the Orchestrator in
   `CC-20260922-TAU-DIRECTION-01`: *"**Neither WWOX overexpression nor GSK3β knockdown promoted
   neurite outgrowth in the Tau knockdown condition, indicating that Tau is the effector of both
   WWOX and GSK3β**."* Remove Tau and both interventions the model is built on stop working.
2. **DATO.** The microtubule limb of that same paper is **cell-free** — purified tubulin at
   0.2 mg/ml, turbidity readout — and it is **residue-resolved**: *"the GSK3β-binding deficient
   WWOX, **WWOX L404A, could not restore the microtubule assembly activity**."* So the effector
   step has been reconstituted from purified components, which is the strongest form this limb takes.
3. 🔴 **And the repository's own open item, in `wwox_functional_readout_tractability_20260922.md`
   line 542, verbatim:** *"**The Tau isoform** used (2N4R? 0N4R? a fragment?). Never stated. The
   molar figures in §5.2 carry it."*

> **INFERENZA.** The entire effector limb of this disease model rests on an assay whose effector's
> molecular identity is unrecorded — and **"Tau" is not one molecule.** Adult human CNS expresses
> six isoforms from `MAPT` by alternative splicing of exons 2, 3 and 10, differing in the number of
> N-terminal inserts (0N/1N/2N) and, decisively, in whether the second microtubule-binding repeat is
> present (**3R vs 4R**). The repository has recorded the gap as a *citation* defect. **I propose it
> is a mechanistic one.**

🔵 **`PREMISE_TAG` on everything below.** That the six CNS isoforms differ in microtubule-assembly
competence, and that their proportions change with brain development, is
🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` at the moment of writing. **A `DEFAULT_FROM_TEXTBOOK` is not a
foundation; it is a research target.** §1.7 tests it and reports what it finds, including if it
falsifies me.

## 1.2 DIVERGE — six readings, distinct because they predict different measurements

| # | mechanism | what it predicts that the others do not |
|---|---|---|
| **E1** | **Isoform-indifferent.** GSK3β's Tau sites `S396`/`S404` lie in the C-terminal region common to all six isoforms; WWOX acts on the *kinase*, so any Tau reports the same rescue. | Rescue magnitude **equal** for `0N3R` and `2N4R` at matched molarity. The null, and it is a real possibility. |
| **E2** | **Repeat-domain gated (R2).** `4R` Tau carries a fourth microtubule-binding repeat and higher intrinsic assembly competence, so a fixed GSK3β phospho-load costs it **less**; the WWOX rescue is correspondingly smaller because the deficit it repairs is smaller. A **ceiling** effect. | The **GSK3β-alone** turbidity drop is smaller for `4R` — i.e. the isoform effect is visible *before* WWOX is added. This is E2's signature and nothing else predicts it. |
| **E3** | **Projection-domain gated (0N/1N/2N).** The N-terminal inserts, not R2, set the difference, by changing spacing and inter-microtubule geometry. | The ordering across six isoforms follows **N-inserts**, so `0N4R` vs `2N4R` separate **more** than `0N3R` vs `0N4R`. E2 predicts the exact opposite ordering. |
| **E4** | **Priming-gated, not isoform-gated.** GSK3β is a primed kinase; `S396`/`S404` phosphorylation depends on prior phosphorylation by another kinase. The gate is **priming-kinase availability**, and isoform is a confound that travels with it. | The isoform difference **vanishes in the cell-free assay** (no priming kinase present) and **appears only in cells**. Uniquely, E4 predicts the two assay formats disagree. |
| **E5** | **Tubulin-side gated.** The readout is turbidity of *tubulin*; commercial brain tubulin is a mixed isotype and mixed-PTM pool (tyrosination, detyrosination, βIII content), and neuronal tubulin differs from it. The isoform question is the wrong axis. | **Swapping the tubulin source moves the rescue more than swapping the Tau isoform.** Only E5 makes the control the main effect. |
| **E6** | **Occupancy, not identity.** Apparent isoform effects are apparent-affinity effects; at matched *bound* Tau rather than matched total Tau, all curves superimpose. | A Tau titration **collapses** the isoform curves onto one when plotted against bound Tau. E6 is the one reading under which a positive result in the discriminator would still mean nothing. |

🔴 **E1 and E6 are the two that would kill this cycle, and they are listed first and last on purpose.**
A diverge set in which every branch supports the hypothesis is not a diverge set.

## 1.3 CONNECT — developmental `MAPT` biology, with the split made explicit

**Imported field:** developmental neurobiology of `MAPT` / Tau isoform regulation, and the
comparative (mouse-vs-human) literature on the **3R→4R switch**.

| | |
|---|---|
| ✅ **WHAT TRANSFERS** | (i) That `MAPT` exon-10 inclusion is **developmentally regulated**, so the 3R:4R ratio of a brain is a function of its age — meaning "Tau" in a neonatal brain and "Tau" in a 5-year-old brain are **different molecular populations**. (ii) That 3R and 4R are **not functionally interchangeable** for microtubule assembly — this is the field's founding biochemical result, not a speculation. (iii) The **assay convention**: a Tau paper is expected to declare its recombinant isoform, which is why its absence in Wang 2012 is informative rather than routine. (iv) That the **mouse and human switch clocks differ**, which makes any mouse-to-human transfer of this limb a clock comparison and not a dose comparison. |
| 🔴 **WHAT DOES NOT** | (i) **No tauopathy disease mechanism transfers.** WWOX-DEE is not a tauopathy. Nothing about neurofibrillary tangles, seeding, propagation, hyperphosphorylation-as-toxicity, or 3R/4R-selective aggregation (Pick vs PSP/CBD) has any bearing here, and importing it would be the exact error `CC-20260922-TAU-DIRECTION-01` exists to prevent: **in this pathway Tau is the thing being made functional, not the toxin.** (ii) **No `MAPT`-splicing disease transfers** — `FTDP-17` exon-10 mutations shift the 3R:4R ratio in *adults* and are mechanistically unrelated. (iii) **No therapeutic modality transfers whatsoever**, and in particular **Tau-lowering is directionally forbidden here** and is named only to forbid it. (iv) The absolute switch timings are **species facts to be verified, never assumed**, and §1.7 reports what I could and could not establish. |

🔴 **The `DOES NOT` column is longer than the `TRANSFERS` column and that is deliberate.** The
failure mode this laboratory has already had once — *"an analogy imported without the `DOES NOT`
half becomes a premise"* — is exactly what a tauopathy import would do here.

## 1.4 HYPOTHESIS

> ## **H-A (IPOTESI).** The WWOX → GSK3β → Tau → microtubule-assembly limb is **Tau-isoform-gated**, and therefore **age-gated**: its repairable deficit is largest against 3R-dominant (immature) Tau and smaller against 4R-containing Tau. Consequently the leverage available from this limb **declines as the developing brain completes its 3R→4R transition**, on a clock that runs at a different rate, relative to the treatment window, in mouse and in human.

**What H-A predicts that the current model does not.** The working model's
*"SDR-domain function is measurable"* section states the `388–407` / `L404` docking mechanism and
its two consequences (the degron design constraint, the phospho-`S9` blindness) as **time-invariant
molecular facts**. H-A says the *size of the benefit* delivered through that mechanism is a function
of the brain's developmental age **through a molecule that is not WWOX and not GSK3β** — and that
the mouse model, whose untreated animals die at ~3 weeks, may spend its entire natural history on
the favourable side of a switch a human child crosses and then lives past for years. Nothing in the
model has an age-dependent *effector composition* term.

## 1.5 PREDICTION, with its falsifier

| # | Prediction, committed before searching | Falsifier |
|---|---|---|
| **A-P1** | In the Wang 2012 cell-free turbidity assay, everything else fixed and Tau matched by **molarity**, WT-WWOX's restoration of GSK3β-suppressed assembly is **≥1.5×** larger with a 3R isoform than with a 4R isoform | Δrescue(3R) ≤ Δrescue(4R), **or** the two within 20% of each other ⇒ **E1**, and H-A is dead |
| **A-P2** | The **3R→4R switch is a documented developmental event in human brain**, essentially postnatal, such that a neonate is 3R-dominant and an older child is not | No developmental regulation of exon 10 in human brain ⇒ the age-gating leg collapses regardless of A-P1 |
| **A-P3** | **Mouse and human switch clocks differ**, and the mouse completes its switch **before or around P21** — i.e. inside or at the edge of the untreated `Wwox`-null lethal window (43% dead by 72 h, 77% by day 17, none past weaning) | Mouse switch completes well **after** P21 ⇒ the species-mismatch corollary is wrong, though H-A's biochemical leg could still stand |
| **A-P4** | 3R and 4R Tau **differ measurably in microtubule-assembly competence** in cell-free assays, in the published biochemistry, by ≥2-fold on some standard metric | No published difference ⇒ **E1** is the field's own answer and H-A was never plausible |
| **A-P5** | **No paper connects WWOX to Tau isoform composition**, in any system | Such a paper exists ⇒ `REDISCOVERY`, graded as such |
| **A-P6** | The SH-SY5Y RA-differentiated system used by Wang 2012 is **3R-dominant / fetal-Tau-like**, so the published result was obtained on the favourable side of the gate | It is 4R-dominant ⇒ the published effect size is already the pessimistic one, which **weakens H-A's practical consequence while leaving its mechanism intact** |

🔴 **A-P1 is the load-bearing prediction and it is the one I cannot test from a desk.** A-P2 through
A-P6 are literature-checkable; A-P1 requires a bench. I state that asymmetry now rather than letting
a confirmed A-P2 be read as support for A-P1.

## 1.6 DISCRIMINATOR

**One experiment, and it is a repeat of an assay that has already been run once.** The Wang 2012
cell-free turbidity assay, with the single change that the Tau is **declared and varied**:
recombinant `0N3R` and `2N4R`, matched by molarity not mass, same tubulin lot, factorial
± GSK3β, ± WT-WWOX, ± `L404A` WWOX.

- **Isoform-indifferent** (equal rescue) ⇒ **E1**, H-A dead, one afternoon.
- **Isoform-dependent, with the split already visible in the GSK3β-alone arm** ⇒ **E2**.
- **Isoform-dependent, ordering by N-inserts** ⇒ **E3** — requires `0N4R` as a third arm.
- **Cell-free flat but cellular split** ⇒ **E4**; separable by adding a priming-kinase arm.
- 🔴 **E5 and E6 are controls, not afterthoughts:** one tubulin-source swap and one Tau titration.
  Without them a positive result is uninterpretable, and **E6 is the branch under which a positive
  result means nothing at all.**

🔴 **`L404A` is the specificity control and it is not optional.** It is the arm that makes the
readout WWOX-specific rather than "something was added to the tube", and Wang 2012 already
established it works.

<!-- ▲▲▲ CYCLE 1 TRACE SEALED. Nothing above this line was written or edited after any search. ▲▲▲ -->

---

# § 2 · TRACE CYCLE 2 — *is the missing Q230P protein lost before it ever exists, and does that make the standard experiment lie?*

## 2.1 OBSERVATION

Four facts, all held here before today's act.

1. **DATO.** `Q230P` is **buried**: `SASA 0.0 Å²`, `relSASA 0.000`, burial 200 (83.8th percentile),
   22 heavy-atom contacts within 5 Å. It sits on helix **αE (226–251)**, at the fifth position of
   that helix, and the segment `226–240` has **max relSASA 0.107 — no exposed face at all**.
2. **DATO.** The substitution is to **proline**, and it is ~51 residues N-terminal of the catalytic
   triad `S281`/`Y293`/`K297`. `q230p_direct_discriminator_20260922.md` already notes it perturbs
   *"side chain **and** backbone at once."*
3. **DATO.** Mild hypothermia (27–32 °C) *"reduces the degradation rates of **all** mRNAs and
   proteins examined"* (Roobol 2008, CHO-K1 / P19 / 3T3) — on which ground
   `q230p_minimum_discriminator_20260922.md` **cut the permissive-temperature arm entirely**, as the
   file's *"main intellectual result"*, because a band appearing at 30 °C is ambiguous between
   *"it folded"* and *"it stopped being cleared."*
4. **DATO.** **Nobody has ever examined an insoluble fraction in any WWOX missense abundance
   measurement (0/13)**, and no WWOX turnover measurement exists in this corpus in any tissue or
   species.

> **INFERENZA, and it is the observation.** The repository cut the temperature arm because the
> confound is **global**. But **a global effect is a common-mode effect, and common-mode effects
> cancel out of a ratio** — a primitive this very session applied, correctly and at length, to the
> TX-007 dose-unit ambiguity (*"a common-mode multiplier cannot change a ratio"*). **The primitive
> was never carried across to the temperature arm.** That is the uneven-application failure mode
> `designed_for_growth.md` § 5 names as the characteristic defect of a system growing by accretion.

🔴 **But a ratio is only worth measuring if some mechanism predicts it departs from 1.** Supplying
that mechanism is the actual content of this cycle; the normalisation alone is bookkeeping.

## 2.2 DIVERGE — five loss routes, distinct because each predicts a different assay to behave differently

| # | mechanism | when the molecule is lost | what it uniquely predicts |
|---|---|---|---|
| **F1** | **Thermodynamic marginality of a folded species.** The chain folds, reaches a native-like state, is marginally stable, exposes a degron, is cleared. The textbook chaperone case. | after folding | A **CHX chase shows a shortened half-life**, and hypothermia helps `Q230P` and WT **equally** (ratio = 1) |
| **F2** | **Kinetic partitioning at a proline-limited folding step.** An `Xaa–Pro` bond introduced into a buried helix creates an obligatory *cis/trans* isomerisation with a large activation barrier; the on-pathway step slows, so a larger fraction of chains is captured off-pathway (aggregate or QC) before reaching native. Loss happens **during folding**, not after it. | during folding | 🎯 **Hypothermia is supra-global for this allele (ratio > 1)**, because temperature reduction favours the lower-activation-energy on-pathway branch over the off-pathway one — *and* 🔴 **a CHX chase reads NORMAL**, because chains that never folded are gone before the chase labels a pool |
| **F3** | **Ribosome-associated triage.** Loss is co-translational QC acting on the nascent chain; the folding landscape is never reached at all. | during synthesis | **Translation-rate manipulation moves the result**; hypothermia's benefit comes through *slower synthesis*, so it should be **mimicked by sub-inhibitory translation slowing at 37 °C** — which F2 does not require |
| **F4** | **Off-pathway aggregation as the terminal state**, the chain reaching an insoluble deposit rather than being degraded. | during or after folding | **Mass is in the pellet and is recoverable**; the total (`T`) lane is normal while the soluble (`S`) lane is empty — and 🔴 **raising synthesis is harmful here, not neutral** |
| **F5** | **No loss at all — detection floor / epitope artefact.** A near-normal quantity of a conformationally altered protein that the antibody cannot see. | nowhere | **Two antibodies with stated flanking epitopes disagree with each other**; and the whole abundance axis is moot |

🔴 **F1 and F2 are the pair this cycle exists to separate, and they are separated by the SIGN OF A
RATIO and by whether a standard experiment returns a false negative.** F4 and F5 are the
repository's already-held `D3` and `D5` and are carried here **only** so the discriminator is not
double-counted as evidence for F2 — they are not claimed as new.

## 2.3 CONNECT — protein-folding kinetics, with the split made explicit

**Imported field:** the kinetics of protein folding, specifically (a) proline *cis/trans*
isomerisation as a rate-limiting step and the peptidyl-prolyl isomerases that catalyse it, and
(b) the kinetic-partitioning framework in which folding and aggregation/degradation compete as
branches with different activation energies — the framework that underlies the universal practice
of **lowering the temperature to raise folded yield** in recombinant expression.

| | |
|---|---|
| ✅ **WHAT TRANSFERS** | (i) The **structural fact** that an `Xaa–Pro` peptide bond interconverts slowly between *cis* and *trans* with a high activation barrier, so introducing a proline can install a new slow step into a folding pathway. (ii) The **kinetic-partitioning logic**: if folding and the loss branch compete, the *partition ratio* — not the equilibrium stability — decides yield, and temperature changes the partition ratio whenever the two branches have different activation energies. (iii) The **operational consequence** the whole recombinant-expression field runs on: lowering temperature raises folded yield **selectively for aggregation-prone constructs**, which is precisely an allele-selective effect on top of a global one. (iv) The **measurement discipline** that a chase experiment measures only the pool that survived to be labelled. |
| 🔴 **WHAT DOES NOT** | (i) **No bacterial expression conclusion transfers to a human fibroblast.** *E. coli* at 18 °C and a patient fibroblast at 30 °C are not the same experiment, and the repository has already been bitten once by importing a temperature arm whose source did not cover its own condition. (ii) **Nothing about proline isomerase *drugs* transfers**, and none is named — the immunophilin ligands are immunosuppressants and naming one as a lever here would be exactly the therapy proposal this file is forbidden to make. (iii) **The presence of a proline does not establish that its isomerisation is rate-limiting** for this chain; that is the hypothesis, not a premise. (iv) 🔴 **Whether the `Q229–P230` bond would even be *cis* or *trans* in the folded state is unknown and unknowable from an AlphaFold model of the wild type, which has no proline there at all.** |

## 2.4 HYPOTHESIS

> ## **H-B (IPOTESI).** `Q230P` protein is lost predominantly by **kinetic partitioning during folding at a newly-installed proline-limited step**, not by accelerated turnover of a folded species. Two consequences follow that the model does not hold: **(1)** mild hypothermia's effect on `Q230P` is **allele-selective** — larger than its global effect on WT WWOX in the same cells — so the arm the repository cut is **recoverable by normalisation rather than lost**; and **(2)** 🔴 **a cycloheximide chase on `Q230P` will return a half-life indistinguishable from wild type, and that normal result will be a FALSE NEGATIVE**, because chains lost before folding never enter the chaseable pool.

**What H-B predicts that the current model does not.** The model holds `Q230P`'s cause as
*"unresolved — impaired translation, insolubility, or premature degradation"* and treats the three
as a disjunction to be settled by measuring abundance under degradation inhibitors. H-B says the
disjunction is mis-parsed: **"degradation" splits into a post-folding branch and a during-folding
branch that the planned experiments cannot tell apart**, and that the single most standard
turnover experiment in the field — the CHX chase, which appears in ~25 files of this repository —
is **predicted to give the wrong answer with a clean-looking result**. 🔴 A clean false negative is
worse than a failed experiment, because nobody re-runs it.

## 2.5 PREDICTION, with its falsifier

| # | Prediction, committed before searching | Falsifier |
|---|---|---|
| **B-P1** | 🎯 In paired cells at 37 °C vs 30 °C, **(`Q230P` at 30 °C / `Q230P` at 37 °C) ÷ (WT at 30 °C / WT at 37 °C) > 1.3** — the variant gains more than the global effect | Ratio ≤ 1.1 ⇒ the hypothermia response is purely common-mode ⇒ **F1**, and H-B's leg (1) is dead |
| **B-P2** | 🎯 A CHX chase on `Q230P` gives a decay rate **within 25%** of WT, despite steady-state abundance being at or below the detection floor | A clearly shortened `Q230P` half-life ⇒ **F1**, H-B's leg (2) is dead, and the textbook chaperone case is live |
| **B-P3** | The proposition *"proline cis/trans isomerisation can be the rate-limiting step in protein folding"* is **established, not contested**, in the folding literature | Contested or superseded ⇒ the `CONNECT` import is unsound |
| **B-P4** | The proposition *"lowered temperature raises folded yield selectively for aggregation-prone constructs"* is **established**, i.e. the allele-selectivity of a temperature effect has precedent | No precedent for selectivity ⇒ B-P1's mechanism has no support and the ratio has no reason to depart from 1 |
| **B-P5** | **Zero** occurrences of `isomeris*`, `isomeriz*`, `cyclophilin`, `FKBP` anywhere in this repository, and **zero** of any statement that a CHX chase could return a false negative through co-translational loss | Any hit ⇒ downgrade the novelty claim accordingly |
| **B-P6** | 🔴 **No WWOX-specific evidence of any kind exists on folding kinetics, isomerisation, or temperature-dependence for any allele.** I expect this to be a **true zero of the field, not of my query**, and I will report it as a query result and not as a biological fact | Any WWOX folding-kinetics measurement exists ⇒ it outranks everything in this cycle and should be read instead |

## 2.6 DISCRIMINATOR

**Two lanes and an incubator.** Both legs ride on the *same* harvest and neither needs a compound,
a screen or a molecule of any kind.

- **Leg 1 — the recovered arm.** Paired plates, 37 °C and 30 °C, `Q230P` fibroblasts **and**
  control fibroblasts **in the same experiment**, harvested as `S`/`P`/`T` by the protocol already
  specified in `q230p_minimum_discriminator_20260922.md` (equal **cell-equivalents**, total-protein
  stain, never β-actin/GAPDH/α-tubulin — those partition differently and change under hypothermia).
  🔴 **The WT lane is not a courtesy control: it is the entire instrument.** It measures the
  common-mode term so the ratio can cancel it. **Ratio > 1 ⇒ F2. Ratio = 1 ⇒ F1.**
- **Leg 2 — the false-negative test.** CHX chase on the same two genotypes. 🔴 **Its value is
  inverted from the usual:** a *normal* `Q230P` half-life is the **informative** outcome here and is
  predicted by F2, whereas under F1 it would be a refutation. This is the only design in which the
  boring result carries the information, which is why it must be pre-registered — read post hoc, a
  normal half-life would simply be filed as "no turnover defect" and the question would close.
- **Separating F2 from F3** needs one further arm: sub-inhibitory translation slowing at 37 °C. If
  that reproduces the 30 °C gain, the mechanism is synthesis-rate, not isomerisation.
- 🔴 **F4 is not separated by this design and is not claimed to be.** The `P` lane detects it; it
  does not distinguish an aggregate reached *via* the kinetic trap from one reached otherwise.

<!-- ▲▲▲ CYCLE 2 TRACE SEALED. Nothing above this line was written or edited after any search. ▲▲▲ -->

---

## 1.7 RESULT — what the search returned

> **Source discipline.** According to PubMed, and every record below is cited with its DOI. Read
> depth is stated per row and is `abstract-depth` unless marked otherwise — **no full text was
> retrieved in this act**, and nothing below is a `FULLTEXT_READ_RECEIPT`-bearing read. Quotations
> are verbatim from the PubMed abstract surface.

### 1.7.1 🎯 The founding measurement — and it gives H-A a number it did not have

**Goedert & Jakes 1990**, *EMBO J* 9(13):4225–30, PMID `2124967`,
[DOI](https://doi.org/10.1002/j.1460-2075.1990.tb07870.x). Six recombinant human tau isoforms,
purified, assayed for tubulin polymerisation. Verbatim:

> *"The rates of assembly were **2.5–3.0 times faster for isoforms containing four repeats** when
> compared with three-repeat containing isoforms, **with no significant contribution by the
> amino-terminal insertions**."*

and, on development:

> *"In **fetal human brain** extracts treated with alkaline phosphatase one of the two major tau
> bands aligned with the **three-repeat containing isoform with no insertions**"* — while adult
> human cerebral cortex carries four major bands comprising **both** 3R and 4R species.

| Prediction | Verdict |
|---|---|
| **A-P2** — 3R→4R is a developmental event; neonate 3R-dominant, older brain not | 🟢 **CONFIRMED.** Fetal human brain = 3R-with-no-inserts; adult human = 3R **and** 4R |
| **A-P4** — 3R and 4R differ ≥2-fold in assembly competence | 🟢 **CONFIRMED, and the margin is larger than my threshold: 2.5–3.0×** |
| **E3** (projection-domain gating) | 🔴 **DEAD BY LITERATURE, before any experiment.** *"no significant contribution by the amino-terminal insertions."* One of my six diverge branches is eliminated at zero cost, and the discriminator loses its `0N4R` arm |

Corroborating the developmental leg from a second, independent direction — **Smith 2011**,
*Hum Mol Genet* 20(20):4016–24, PMID `21807765`,
[DOI](https://doi.org/10.1093/hmg/ddr330): *"miR-132 is inversely correlated with PTBP2 during
**post-natal brain development at the time when 4R-tau becomes expressed**."* Exon-10 inclusion is
postnatally regulated and has an identified splicing-regulator mechanism.

### 1.7.2 🔴 A-P3 IS REFUTED IN ITS DIRECTION, and the correction matters more than the prediction did

**Hosokawa 2022**, *Brain* 145(1):349–361, PMID `34515757`,
[DOI](https://doi.org/10.1093/brain/awab289). Verbatim:

> *"most use 4R human tau transgenic mice or **adult wild-type mice expressing only endogenous 4R
> tau** … These deficiencies may reflect **differences between human and rodent tau isoforms in the
> brain**."*

and the human side, from the same abstract: Alzheimer's disease is described as *"3R and 4R
tauopathy"*, i.e. the adult human brain contains and can accumulate **both**.

> ## 🔴 **I predicted the species mismatch. I predicted its DIRECTION BACKWARDS.**
>
> **A-P3 as written:** *"the mouse completes its switch before or around P21"*, with the stated
> corollary that the mouse therefore **over**-reports the benefit available from this limb.
>
> **What the evidence says:** the **adult wild-type mouse expresses ONLY 4R** — the isoform that
> assembles microtubules **2.5–3.0× faster**, i.e. the isoform with the *smaller* deficit for this
> limb to repair. The **adult human retains a substantial 3R fraction for life**, and the human
> **infant** — the patient — is the most 3R-dominant of all.
>
> ⇒ Under E2's ceiling logic the mouse is the **conservative** host, not the optimistic one, and
> the corollary inverts: **the `Wwox`-null mouse is predicted to UNDER-report the leverage of the
> downstream WWOX→GSK3β→Tau limb relative to a human patient.**

🔴 **The partial verdict is recorded exactly as it stands.** `A-P3` is **REFUTED in direction,
CONFIRMED in existence**: a species mismatch is real, documented by a primary source, and points
the other way. **The inverted direction is a NEW `IPOTESI` arising from evidence, NOT a prediction
I made**, and it is labelled so wherever it appears below. I did not go back and edit §1.4.

🔴 **And one thing I could not establish:** the **exact postnatal day** at which mouse exon-10
inclusion completes. `A-P3`'s arithmetic against the `Wwox`-null lethal window (43% dead by 72 h,
77% by day 17, none past weaning) therefore **cannot be closed** — I have the endpoint (adult mouse
= 4R only) and not the trajectory. `COULD NOT ESTABLISH`, §5.

### 1.7.3 A-P1, A-P5, A-P6

| Prediction | Verdict |
|---|---|
| **A-P1** — WWOX rescue ≥1.5× larger with 3R than 4R | ⚪ **UNTESTED and untestable from a desk.** 🔴 **Goedert & Jakes measured the assembly rate of tau ALONE. `A-P1` is about the size of a WWOX rescue of a GSK3β-SUPPRESSED baseline. A confirmed A-P4 is NOT support for A-P1**, and I refuse to let it read as such — that is the exact substitution `epistemic_discipline.md` § 1 forbids |
| **A-P5** — no paper connects WWOX to tau isoform composition | 🟢 **CONFIRMED.** `WWOX tau isoform` → `total_count: 2`, and **both are about the TRAPPC6AΔ isoform, not a tau isoform**: PMID `25650666` ([DOI](https://doi.org/10.18632/oncotarget.2876)) and PMID `27551439` ([DOI](https://doi.org/10.1038/cddiscovery.2015.3)). ⚠️ Reported as a **query result on two query strings**, not as a biological zero |
| **A-P6** — RA-differentiated SH-SY5Y is 3R-dominant | ⚪ **NOT ESTABLISHED.** `SH-SY5Y retinoic acid differentiation tau isoform expression` → 5 records, **none stating the tau isoform composition of the system**. The nearest (PMID `11520906`, [DOI](https://doi.org/10.1046/j.1471-4159.2001.00475.x)) reports only that *"tau and MAP2b remained unchanged"*. 🔴 **This is a `PREMISE: NOBODY_LOOKED` about the cell line the entire effector limb was demonstrated in** |

### 1.7bis 🔴 THE FOURTH KILL — and it is the closest call of the run

My cycle-1 search returned **Castaño 2010**, *J Neurochem* 113(1):117–30, PMID `20067585`,
[DOI](https://doi.org/10.1111/j.1471-4159.2010.06581.x), and I very nearly recorded it as the best
finding of this file. Its abstract states that GSK-3 is three enzymes; that **silencing the
neuron-specific `GSK-3β2` INHIBITED retinoic-acid-induced neurite outgrowth in SH-SY5Y** — the
**opposite sign** to Wang 2012's GSK3β knockdown, in the same cell line, same stimulus, same
readout; that **Axin associates more readily with β1 than with β2**; and that *"GSK-3 inhibitors
that target the **Axin-binding site** in GSK-3 will preserve the beneficial effects of GSK-3β2 on
axon growth"* — **the very site WWOX docks at (`388–407`, `L404`)**.

> 🔴 **All of it is already held here, and held better than I had it.**
> `discovery_ledger_current.md` `DL-MECH-067` states the WWOX/Axin-site bridge, calls it *"il lead
> terapeuticamente più interessante emerso finora sull'asse GSK3β"*, tags the β1-preference premise
> `PREMISE: INFERENZA`, and names the decisive experiment. `DL-MECH-068` adds **primary
> biochemistry I did not have** (Saeki 2011, PMID `21212533`, [DOI](https://doi.org/10.1248/bpb.34.146),
> full text read, 14 page-anchored locators): β2 phosphorylates tau `S396` ~3–10× less than β1
> while being **equally active on other substrates**, the C-terminal tail is indispensable for β2
> and nearly dispensable for β1, and **UniProt P49841** places the β2 insert **13 residues after
> `K303`** — four residues downstream of the `N285–H299` docking loop, with the ATP site identical
> between isoforms. `DL-BIO-013` already proposes the β1:β2 ratio as a severity modifier. Even the
> Wang-vs-Castaño sign contradiction is recorded, as *"Wang cita Castaño (rif. 27) solo per
> ammettere una contraddizione sulla direzione."*
>
> ⇒ **`REDISCOVERY`, complete, on every leg. Claimed as novelty by me for approximately four
> minutes, and caught by the enumerate-then-unscoped-grep protocol, not by luck.** It is the fourth
> attractive idea this file has had to kill, and the reason the protocol is mandatory rather than
> advisory. 🔵 **One residue survives and is carried forward as `HYP-3` in § 3** — not the bridge
> itself, but a 2×2 nobody has crossed.

## 1.8 GRADE — cycle 1

| Axis | Grade | Reason |
|---|---|---|
| **Prediction quality** | 🟢 **A−** | Six numbered predictions, five literature-checkable, thresholds stated as numbers (≥1.5×, ≥2-fold, ±20%). Four resolved, one refuted **in direction**, one untestable by construction and declared so in advance |
| **Diverge quality** | 🟢 **A** | Six branches; **E3 was eliminated by evidence**, E1 and E6 were kill-branches included on purpose, and each branch named a different measurement |
| **Connect quality** | 🟢 **A** | `DOES NOT` longer than `TRANSFERS`; the tauopathy-import ban was written **before** searching and the search returned four tauopathy papers that would have been easy to misuse |
| **Hypothesis survival** | 🟡 **C+** | H-A's **biochemical leg survives and gained a quantitative anchor (2.5–3.0×)**; its **species corollary was refuted and inverted**; its load-bearing prediction A-P1 is untested |
| **Honesty of the refutation** | 🟢 **A** | The inversion is recorded as a refutation of my prediction and as a *new* IPOTESI, not retrofitted. §1.4 is unedited |
| **Novelty discipline** | 🟢 **A** | The novelty check cost me three ideas before writing and one more after searching (§ 1.7bis) |
| **Overall cycle 1** | 🟢 **B+** | A real, checkable hypothesis; a genuine directional refutation that is *more useful than the prediction*; and it is honest about the leg it could not test |

## 1.9 EXPERIMENT — cycle 1, as revised by the result

**The discriminator loses an arm and gains a control.** `0N4R` is cut — E3 is dead, so the
N-terminal-insert arm buys nothing. What replaces it is the measurement A-P6 showed is missing.

| # | arm | cost | what it decides |
|---|---|---|---|
| **1** ⭐ | Wang 2012 cell-free turbidity, **declared** `0N3R` vs `2N4R`, matched **molarity**, one tubulin lot, factorial ± GSK3β, ± WT-WWOX, ± `L404A` | one afternoon, two recombinant proteins, an assay already published | **A-P1.** Isoform-flat ⇒ **E1**, H-A dead. Split already visible in the GSK3β-alone lane ⇒ **E2** |
| **2** | **Declare the tau isoform composition of RA-differentiated SH-SY5Y** — isoform-resolved immunoblot or RT-PCR across exon 10 | one gel | **A-P6**, currently `PREMISE: NOBODY_LOOKED` about the system the whole limb rests on |
| **3** | Tau titration (E6) and one tubulin-source swap (E5) | two extra plates | 🔴 **Not optional.** Under **E6** a positive result in arm 1 means nothing |
| **4** | Mouse exon-10 inclusion time-course, P0→P30 | a published figure, if one exists | Closes the `COULD NOT ESTABLISH` of §1.7.2 and decides whether the inverted corollary has a real clock |

🔴 **Not proposed, and named so it cannot be smuggled back in:** no compound, no `MAPT`
splice-switching agent, no tau-lowering anything (**forbidden in direction** by
`CC-20260922-TAU-DIRECTION-01`), no animal cohort, no clinical measurement, no therapy.

---

## 2.7 RESULT — what the search returned

### 2.7.1 B-P3 CONFIRMED — and the sentence beside it cuts my mechanism in half

**Alderson 2017**, *Chembiochem* 19(1):37–42, PMID `29064600`,
[DOI](https://doi.org/10.1002/cbic.201700548). Verbatim:

> *"slow cis–trans Pro isomerization in the unfolded state **is often found to be a rate-limiting
> step in protein folding**."*

🟢 **B-P3 CONFIRMED.** Reinforced by **Roderer 2015**, *Chembiochem* 16(15):2162–6, PMID `26382254`,
[DOI](https://doi.org/10.1002/cbic.201500342), which manipulates exactly that step — *"the
rate-limiting trans-to-cis isomerization of the `Ile75-Pro76` peptide bond in the folding of
`E. coli` thioredoxin"* — and **accelerates folding ninefold** by substituting a proline analogue.
The step is real, rate-setting, and manipulable.

> ## 🔴 **AND THE ADJACENT CLAUSE, WHICH I WENT LOOKING FOR BECAUSE THIS LABORATORY HAS A NAMED PRIMITIVE FOR IT (`verify_the_omitted_clause`), CUTS H-B's MECHANISM IN HALF.**
>
> Same abstract, two sentences earlier: *"**Folded proteins predominantly contain trans-Pro
> bonds**"*, and *"cis-Pro populations at all of its five X-Pro bonds are **less than 5%**"* — an
> effect the authors attribute to prior studies having overestimated cis-Pro using short charged
> peptides.
>
> ⇒ The rate-limiting cases are those requiring a **trans→cis** isomerisation, i.e. proteins with a
> **cis**-proline in the **native** state. 🔴 **I cannot establish that `Q230P`'s native state — if
> it has one — would place a cis proline at 230, and it is unknowable from an AlphaFold model of a
> wild type that has no proline there at all.** I wrote that exact caveat into §2.3's `DOES NOT`
> column before searching, and the evidence has now made it load-bearing rather than decorative.
>
> **Consequence, stated plainly: the proline-isomerisation route is the WEAKENED leg of H-B.** What
> survives is the **kinetic-partitioning-versus-post-folding-turnover distinction**, which does not
> depend on the proline mechanism at all — and, with it, **both predictions**, since B-P1 and B-P2
> follow from *when* the molecule is lost, not from *why*.

### 2.7.2 B-P4 CONFIRMED — the allele-selective temperature effect is a canonical phenomenon, with a qualifier

**Sharma 2000**, *J Biol Chem* 276(12):8942–50, PMID `11124952`,
[DOI](https://doi.org/10.1074/jbc.M009172200) — `ΔF508` CFTR, the paradigm case. Verbatim:

> *"The consensus notion is that `ΔF508` imposes a **temperature-sensitive folding defect** and
> targets newly synthesized CFTR for degradation at endoplasmic reticulum"*, with escape *"induced
> by **reduced temperature and glycerol**."*

🟢 **B-P4 CONFIRMED in the form that matters:** a low-temperature rescue that acts on the **mutant**
and not on a wild type that needs no rescuing **is** an allele-selective temperature effect, and it
is the most-studied one in human genetics. My ratio has a precedent.

> 🔴 **And again the adjacent clause narrows my own discriminator.** The same paper: *"rescued
> `ΔF508` CFTR has a **temperature-sensitive stability defect in post-ER compartments**, including
> the cell surface … **more than 4–20-fold accelerated degradation rate between 37 and 40 °C**."*
>
> ⇒ In the canonical case, temperature acts at **two** steps — folding **and** a separate
> post-folding stability defect. **Therefore a ratio > 1 does NOT cleanly install `F2` over `F1`.**
> It establishes *"something about this allele is temperature-sensitive in a way the wild type is
> not"*, which kills **F1-as-a-purely-global-effect** but leaves a temperature-sensitive-degradation
> variant of F1 alive. **My §2.6 discriminator is less discriminating than I claimed it was**, and I
> am recording that against myself rather than restating the claim.

### 2.7.3 B-P5 and B-P6

| Prediction | Verdict |
|---|---|
| **B-P5** — zero repository occurrences of `isomeris*`, `isomeriz*`, `cyclophilin`, `FKBP`, and zero on a chase false-negative | 🟢 **CONFIRMED, unscoped over all 1,451 files.** `isomeris*` **0** · `isomeriz*` **0** · `cyclophilin` **0** · `FKBP` **0** · `cotranslational` **0** · `co-translational degrad` **0**. ⚠️ `Pin1` returns **1** hit, in `corpus_seed_pubmed_20260806.jsonl` — a **corpus-seed title row**, not a reasoning surface. `cis-trans` returns **1**, in `learned_gates_registry.md`, and is **not about proline** |
| **B-P6** — no WWOX folding-kinetics / temperature evidence exists for any allele | 🟡 **Query returned `total_count: 0`.** 🔴 **Reported as a query result and NOT as a biological fact.** The query AND-chained five concept groups, which is precisely the shape that manufactures a false zero; and this laboratory has established today that a census returns a uniform zero when asked of the wrong document class. **`PREMISE: NOBODY_LOOKED` is the correct label, not "no such evidence exists."** |

## 2.8 GRADE — cycle 2

| Axis | Grade | Reason |
|---|---|---|
| **Prediction quality** | 🟢 **A** | Six predictions, numeric thresholds on the two that matter (`>1.3`, `within 25%`), and **B-P2 pre-registers a BORING result as the informative one** — which is the only way that result can ever carry information |
| **Diverge quality** | 🟢 **A−** | Five branches keyed to *when* the molecule is lost; F4/F5 explicitly carried as the repository's already-held `D3`/`D5` and **excluded from the novelty claim** rather than quietly recounted |
| **Connect quality** | 🟢 **A** | The import was narrowed by its own sources, twice, at the `DOES NOT` clauses I had written in advance |
| **Hypothesis survival** | 🟡 **C** | 🔴 **The proline-isomerisation mechanism is substantially weakened** (cis-Pro < 5%; folded proteins predominantly trans). The *predictions* survive intact because they never depended on it |
| **Discriminator quality** | 🟡 **C+** | Honestly downgraded by §2.7.2: the ratio separates less than §2.6 claimed |
| **Honesty** | 🟢 **A** | Two self-inflicted narrowings, both found by reading the sentence next to the one I wanted, both recorded against myself |
| **Overall cycle 2** | 🟡 **B** | The mechanism story lost; **the experimental consequence — a predicted false negative in the experiment the model is most likely to run — is the most actionable item in this file and survived untouched** |

## 2.9 EXPERIMENT — cycle 2, as revised by the result

| # | arm | cost | what it decides |
|---|---|---|---|
| **1** ⭐ | **CHX chase, `Q230P` and control, same harvest** | one chase | **B-P2.** 🔴 A **normal** half-life is the informative outcome and is predicted by F2; under F1 it is a refutation. **Must be pre-registered or it will be filed as "no turnover defect" and close the question** |
| **2** ⭐ | **Pulse-label (short metabolic pulse: AHA/click or short SILAC) on the same two genotypes** | one extra plate | 🔴 **The arm that arm 1 CANNOT substitute for.** A chase sees only the pool that survived to be labelled; a short pulse sees synthesis and the earliest loss. **Under H-B this is where the difference lives, and no one has run it for any WWOX allele** |
| **3** | 37 °C vs 30 °C paired plates, both genotypes, `S`/`P`/`T`, equal **cell-equivalents**, total-protein stain | one incubator, one extra harvest | **B-P1.** 🟡 Now stated at its **corrected** power: ratio > 1 ⇒ allele-selective temperature sensitivity, **not** folding-versus-degradation |
| **4** | Sub-inhibitory translation slowing at 37 °C | one plate | Separates **F2** from **F3** |

🔴 **Not proposed:** no compound, no PPIase ligand of any kind (the immunophilin ligands are
immunosuppressants and naming one here would be the therapy proposal this file is forbidden to
make), no molecule, no dose, no route, no screen.

---

# § 3 · THE RANKED FINAL LIST — five hypotheses, ranked

> **Ranking criterion, stated before the list.** Not *"how interesting does it sound"* but
> **"does it change which experiment a real scientist should do next, and at what cost."** A
> hypothesis that changes nothing is ranked last and **labelled as changing nothing**, not dressed
> up. All five are `IPOTESI`. None is canonical, none is a claim, none is medical advice, and none
> names a therapy.

---

### 🥇 HYP-1 · The cycloheximide chase on `Q230P` will return a NORMAL half-life, and that normal result will be a FALSE NEGATIVE

**1 · NOVELTY ORIGIN: 🟢 `AGENT-NOVEL`.** The *mechanism class* is held — `q230p_therapeutic_mechanism_expansion_20260922.md` `D1`, *"co-translational folding-yield ceiling … ribosome-associated QC triages it before a native-like species ever exists."* 🔴 **The consequence for the measurement is not held anywhere.** Unscoped over all 1,451 files: `cotranslational` **0**, `co-translational degrad` **0**, and **no statement that a chase could mislead**, while `CHX chase` appears across **~22 files** and the chase is a standing component of the proteostasis programme.

**2 · What it predicts that the current model does not.** The model treats *"impaired translation / insolubility / premature degradation"* as a three-way disjunction settled by abundance under degradation inhibitors. HYP-1 says **"degradation" is itself two branches — during-folding and post-folding — that the planned assays cannot separate**, and that the standard turnover experiment is **structurally blind to the during-folding branch**, because a chase measures only the pool that survived long enough to be labelled. The model currently predicts nothing at all about what a `Q230P` chase would show.

**3 · Cheapest measurement that would refute it.** 🎯 **One cycloheximide chase, `Q230P` fibroblasts and control, same harvest.** A clearly shortened `Q230P` half-life refutes it outright and installs the textbook chaperone case (`F1`). 🔴 It must be **pre-registered as predicting the boring outcome**, because read post hoc a normal half-life is filed as *"no turnover defect"* and the question closes.

**4 · What it would change if true.** The chase **stops being sufficient** and must be paired with a **short metabolic pulse-label** — an arm nobody has run for any WWOX allele, in any system. It also changes how a null result is written: *"turnover is normal"* would become *"turnover of the surviving pool is normal, and the pool that did not survive was not measured."* 🔴 **This is the item most likely to prevent a real, clean, wrong answer**, because the experiment is cheap, standard, and about to be run.

---

### 🥈 HYP-2 · The WWOX→GSK3β→Tau limb is tau-isoform-gated — and the mouse UNDER-reports its human leverage

**1 · NOVELTY ORIGIN: 🟡 `CROSS-DOMAIN-DERIVED`, with an 🟢 `AGENT-NOVEL` connection.** The component facts are standard `MAPT` biology and belong to that field, not to me. **The connection to WWOX is absent here and absent from the literature.** Repository, unscoped: `4R tau` **0** · `isoform switch` **0** · `fetal tau` **0** · `MAPT isoform` **0** · `0N3R` **0**; the single `2N4R` hit is an **unanswered methods question** (*"The Tau isoform used (2N4R? 0N4R? a fragment?). Never stated"*). PubMed: `WWOX tau isoform` → **2 records, both about the TRAPPC6AΔ isoform**. 🔵 **Adjacent but distinct from `DL-BIO-013`**, which proposes the *GSK3B* `β1:β2` splice ratio as a modifier — a different gene, a different splice event, the other side of the same kinase–substrate pair.

**2 · What it predicts that the current model does not.** The working model states the `388–407`/`L404` mechanism as a time-invariant molecular fact. HYP-2 adds an **age- and species-dependent term located in a molecule that is neither WWOX nor GSK3β**: 4R tau assembles microtubules **2.5–3.0× faster** than 3R (Goedert & Jakes 1990); the **adult wild-type mouse is 4R-only**; the **human is 3R+4R for life and 3R-dominant as an infant**. 🔴 **Direction, which is a new IPOTESI from evidence and NOT something I predicted — I predicted the opposite:** the `Wwox`-null mouse is the **conservative** host for this limb, so mouse data may **understate** the human ceiling of the downstream arm. Nothing in the model carries an age-dependent effector-composition term in either direction.

**3 · Cheapest measurement that would refute it.** 🎯 **The Wang 2012 cell-free turbidity assay, run once with `0N3R` and `2N4R` declared and matched by molarity**, ± GSK3β, ± WT-WWOX, ± `L404A`. Isoform-flat rescue ⇒ **E1**, dead. One afternoon, two recombinant proteins, a published assay. 🔴 The `L404A` arm and a tau titration are not optional (**E6**).

**4 · What it would change if true.** (a) A **reporting rule**: every WWOX/tau experiment must declare its tau isoform — **none currently does, including the one the model's effector limb rests on.** (b) It reverses the usual direction of caution in mouse→human extrapolation **for this limb only**, which is the kind of correction that is invisible until someone writes it down. (c) It makes the composition of RA-differentiated SH-SY5Y a `PREMISE: NOBODY_LOOKED` that one gel would close.

---

### 🥉 HYP-3 · The GSK3β-isoform × tau-isoform 2×2 has never been crossed, and the β1-sparing-β2 logic has an untested dependency on it

**1 · NOVELTY ORIGIN: 🟢 `AGENT-NOVEL`, and it is what survived a `REDISCOVERY`.** 🔴 **The bridge itself is NOT mine** — `DL-MECH-067` and `DL-MECH-068` already hold that WWOX docks the Axin site, that Axin prefers β1, that tau is a disfavoured β2 substrate, that the β2 insert sits 13 residues after `K303`, and that an ATP-competitive inhibitor cannot separate the isoforms. I re-derived all of it independently and graded myself `REDISCOVERY` (§1.7bis). 🔵 **What is new is a variable neither ledger entry carries:** both hold the **GSK3β** isoform axis, HYP-2 supplies the **tau** isoform axis, and **the repository explicitly records that the second was never measured** — `DL-MECH-068`: *"Ser404 non è stato testato da nessuno per isoforma"*, and Saeki's β1-vs-β2 comparison was run on **one undeclared tau isoform**.

**2 · What it predicts that the current model does not.** That Saeki's **~3–10× β1/β2 difference on tau `S396` is not a constant but a function of the tau isoform used**, because the 4R-specific repeat changes the substrate's engagement with the C-terminal tail that Saeki showed is **indispensable for β2 and nearly dispensable for β1**. ⇒ a **2×2 interaction term** between kinase isoform and substrate isoform, on a pair the model treats as two independent one-dimensional facts.

**3 · Cheapest measurement that would refute it.** 🎯 **Saeki's own published in-vitro kinase assay, run as a 2×2**: recombinant β1 and β2 × `0N3R` and `2N4R`, reading **both** `S396` **and** `S404`. No interaction term ⇒ refuted, and the existing one-dimensional readings stand as written.

**4 · What it would change if true.** It places a measured dependency under the repository's own **self-declared most interesting open therapeutic hypothesis on this axis** (`DL-MECH-067`). If the β1/β2 discrimination is tau-isoform-dependent, then a WWOX-mimetic's predicted isoform selectivity is **conditional on the developmental tau population**, and its safety argument versus a non-selective ATP-competitive inhibitor is conditional too. 🔴 **That is a constraint on a live hypothesis, not a new hypothesis competing with it.**

---

### 4️⃣ HYP-4 · The cut permissive-temperature arm is recoverable by normalisation, because its confound is common-mode

**1 · NOVELTY ORIGIN: 🟡 `CORPUS-DERIVED` primitive, 🟢 `AGENT-NOVEL` application.** The primitive — *"a common-mode multiplier cannot change a ratio"* — is this session's own, developed at length in `tx007_dose_unit_forensics_20260922.md` and `CC-20260922-TX007-DOSE-CHALLENGE-01.md` for the dose-unit ambiguity. 🔴 **It was never carried across to the temperature arm**, which `q230p_minimum_discriminator_20260922.md` cut as its *"main intellectual result."* This is textbook `designed_for_growth.md` § 5 uneven application: *"the correct pattern existed in this repository, applied at one site and not carried to the second."*

**2 · What it predicts that the current model does not.** That the variant:WT hypothermia response ratio departs from 1 — a quantity the model does not have, because it never measured a WT lane alongside the variant under temperature. `ΔF508` CFTR is the precedent that an allele-selective low-temperature rescue is real (Sharma 2000).

**3 · Cheapest measurement that would refute it.** 🎯 **One extra lane**: a control-fibroblast WWOX lane in the same 37/30 °C experiment. Ratio ≤ 1.1 ⇒ purely common-mode, the cut stands and was correct.

**4 · What it would change if true.** It **recovers a cut experimental arm for the cost of one lane** — a real but bounded gain. 🔴 **And I have downgraded my own claim about it:** §2.7.2 shows temperature acts at **two** steps in the canonical case, so a ratio > 1 establishes *allele-selective temperature sensitivity*, **not** folding-versus-degradation. It is therefore **weaker than HYP-1, and it is ranked below it for that reason and not by preference.**

---

### 5️⃣ HYP-5 · The cell-free microtubule limb is tubulin-source-dependent, so its magnitude is not portable

**1 · NOVELTY ORIGIN: 🟡 `CROSS-DOMAIN-DERIVED`.** Standard tubulin biochemistry (isotype composition, tyrosination state, βIII content of neuronal versus commercial brain tubulin). Carried forward as diverge branch `E5`.

**2 · What it predicts that the current model does not.** That the **magnitude** of Wang 2012's turbidity rescue — the anchoring measurement of `CLAIM 035`'s microtubule limb — is a function of the tubulin preparation, so the number does not transfer between laboratories or to a neuronal context.

**3 · Cheapest measurement that would refute it.** One tubulin-source swap within the same assay. No shift ⇒ refuted.

**4 · What it would change if true.** 🔴 **Close to nothing anyone would do differently, and I am saying so rather than dressing it up.** It would attach a portability caveat to a number nobody is currently extrapolating from. It earns its place only as a **mandatory control** on HYP-2's discriminator — without it a positive isoform result is confounded by the tubulin pool — and **not** as a finding in its own right. **Ranked last on merit.**

---

# § 4 · WHAT I LOOKED FOR AND DID NOT FIND

> A generative cycle's negatives are as informative as its positives, and **four of the five items
> below are ideas I wanted to be true.**

| # | What I looked for | What I found instead |
|---|---|---|
| **1** | **Cofactor-assisted folding as an escape from the "stable but inert" trap** — a NAD(P) cleft ligand stabilising WWOX far from the `ERLIQ 402–406` degron | 🔴 `REDISCOVERY`, and **already refuted downstream of itself**. `q230p_therapeutic_mechanism_expansion_20260922.md` holds it as `D4`, confirms it (`NmrA` Tm 48.0→51.6 °C; the destabilised variant rescued *more*, +5.8 vs +3.6 °C), ranks it 🥇, then kills it on AKR sign-inversion: **the sign of a stabiliser flips with cofactor occupancy, and WWOX's occupancy is unknown.** I would have re-derived a conclusion *and* missed its refutation |
| **2** | **Mitotic dilution of episomal AAV in the granule lineage** | 🔴 `REDISCOVERY`, twice, and the second instance carries a **better falsifier than mine** (an integrating reporter co-delivered with the episomal one) |
| **3** | **A degron-less, hyper-stable, domain-selective frameshift product from `c.1057-2A>G`** | 🔴 **False premise, already excluded by reference sequence.** The surviving outcome is the `c.1063` cryptic acceptor giving **`p.Gln353_Gln354del`** — in-frame, two residues, **no PTC at all**. There is no frameshift to reason about |
| **4** | **WWOX as an Axin-site-binding, β1-selective, β2-sparing endogenous GSK3 inhibitor** | 🔴 `REDISCOVERY`, complete, on every leg — `DL-MECH-067`, `DL-MECH-068`, `DL-BIO-013`, with primary biochemistry and UniProt residue positions I did not have. **Held for ~4 minutes as my best finding.** §1.7bis. One residue survives as HYP-3 |
| **5** | **The tau isoform composition of RA-differentiated SH-SY5Y** — the system the entire effector limb was demonstrated in | ⚪ **NOT FOUND.** 5 records on the query; **none states it.** `PREMISE: NOBODY_LOOKED`, and one gel would close it |
| **6** | **The exact postnatal day of mouse `Mapt` exon-10 switch completion** | ⚪ **NOT ESTABLISHED.** I have the endpoint (adult mouse = 4R only) and not the trajectory, so HYP-2's arithmetic against the `Wwox`-null lethal window **cannot be closed** |
| **7** | **Any WWOX folding-kinetics, isomerisation or temperature measurement, any allele** | 🟡 `total_count: 0` — 🔴 **reported as a query result, not a biological fact.** The query AND-chained five concept groups, the shape that manufactures false zeros. **A PubMed zero is not evidence** |

🔵 **Four ideas killed before or during writing, and the protocol — enumerate, then grep
UNSCOPED — is what killed all four.** Three would have been graded `REDISCOVERY` after the fact
and one rested on a premise the repository had already destroyed.

---

# § 5 · `REVIVAL_TRIGGER`s and `COULD NOT ESTABLISH`

**`REVIVAL_TRIGGER`s** — nothing here dies in silence. Each names what evidence reopens it.

| Killed / weakened | `REVIVAL_TRIGGER` |
|---|---|
| **E3** — projection-domain (0N/1N/2N) gating, dead by Goedert & Jakes | A measurement in which N-terminal inserts **do** change assembly, under conditions Goedert & Jakes did not test — phosphorylated tau, or a non-tubulin-only system |
| **H-A's original species direction** (mouse over-reports) | A demonstration that **3R is the WORSE substrate for this limb specifically** — i.e. that the WWOX rescue is *larger* against 4R. The 2.5–3.0× figure is a baseline rate, not a rescue magnitude, so this is genuinely open |
| **H-B's proline-isomerisation mechanism**, weakened by cis-Pro < 5% | Any evidence that a **cis**-proline is present or favoured at or near residue 230 in a `Q230P` fold — an experimental structure, an NMR observation, or a folding-kinetics measurement showing a slow phase |
| **HYP-4's discriminating power**, downgraded by `ΔF508`'s two-step temperature sensitivity | A `Q230P` design that separates the temperature effect on folding from the temperature effect on post-folding clearance — e.g. a pulse-label at each temperature |
| **My `REDISCOVERY` of the WWOX/Axin-site bridge** | Not a revival — `DL-MECH-067` is already open and active. 🔵 The independent re-derivation is recorded as **corroboration by an actor with no access to that ledger entry at the time of deriving it**, which is worth something, and **nothing more** |

**`COULD NOT ESTABLISH`** — stated so no later reader mistakes silence for absence:

1. The **exact mouse `Mapt` exon-10 switch trajectory** (P0→P30). Endpoint known, clock unknown.
2. The **tau isoform composition of RA-differentiated SH-SY5Y** — the system Wang 2012 used.
3. **Which tau isoform Wang 2012's cell-free assay used.** Still *"never stated."* Every molar figure in the repository's per-molecule argument carries this unknown.
4. **Whether `Q230P`'s hypothetical native state places a cis or trans proline at 230.** Unknowable from a wild-type AlphaFold model that has no proline there.
5. **Any WWOX folding-kinetics or temperature-dependence measurement, for any allele.** Query zero, **not** a biological zero.
6. 🔴 **No full text was read in this act.** Every external source above is `abstract-depth`. **No `FULLTEXT_READ_RECEIPT` was generated and none is claimed.** By `gold_is_in_the_details.md`, **an abstract is not a read** — and four of the five hypotheses rest on abstract-depth sources, which is a real and stated ceiling on all of them.

---

# § 6 · SELF-GRADE

**Per hypothesis.** Graded on the ranking criterion — does it change the next experiment, at what
cost, at what evidential depth. 🔴 **Nothing is graded F, because nothing that would have earned an
F was allowed into § 3** — the four that would have are in § 4, killed.

| # | Hypothesis | Grade | Justification, including against itself |
|---|---|---|---|
| **HYP-1** | CHX chase returns a false negative | 🟢 **A−** | Genuinely `AGENT-NOVEL` on an unscoped check; predicts a **specific wrong answer in an experiment the model is about to run**; refutable by one chase; adds a pulse-label arm nobody has run. **Not an A**: it rests on `D1`, which is the repository's, and its mechanistic parent (proline isomerisation) was weakened in the same act |
| **HYP-2** | Tau-isoform gating, species direction inverted | 🟢 **B+** | Clean repository zero; a real quantitative anchor (2.5–3.0×); a one-afternoon discriminator; and **its most useful content came from a prediction I got backwards**, which is a mark in favour of the method and against my priors. **Not higher**: `A-P1`, the load-bearing prediction, is **untested**, and I must not let a confirmed `A-P4` stand in for it |
| **HYP-3** | The uncrossed GSK3β × tau 2×2 | 🟢 **B** | `AGENT-NOVEL` on the crossing; attaches a measurable dependency to the repository's own most-valued open hypothesis; cheap 2×2 refutation. **Not higher**: it is a **modifier of someone else's hypothesis**, it arrived attached to a full `REDISCOVERY`, and it inherits HYP-2's untested premise |
| **HYP-4** | Common-mode recovery of the cut temperature arm | 🟡 **C+** | Correct, cheap, recovers a cut arm — and **self-downgraded** in §2.7.2, because `ΔF508` shows temperature acting at two steps. The primitive is the repository's, not mine; only the transfer is mine |
| **HYP-5** | Tubulin-source dependence | 🟡 **C−** | Honest, real, and **changes almost nothing anyone would do**. Earns its place as a mandatory control on HYP-2 and on no other ground. **Ranked and graded last on merit** |

**Overall: 🟢 B+.**

**What earns it.** Two complete pre-registered traces, sealed before searching and **not edited
afterwards**. A prediction refuted **in direction**, recorded as a refutation, with the corrected
direction labelled a *new* IPOTESI rather than retrofitted. Two `CONNECT` imports narrowed by their
own sources at the `DOES NOT` clauses written **before** the search. Four attractive hypotheses
killed by the novelty protocol, three of them `REDISCOVERY` and one on a false premise. A diverge
branch (**E3**) eliminated by evidence at zero cost. And a discriminator I **downgraded against
myself** after reading the clause beside the one I wanted.

**What holds it down, and these are not rhetorical.**
1. 🔴 **No full text was read.** Every external source is `abstract-depth`. That is a ceiling on all five hypotheses and it is not a small one.
2. 🔴 **The single most load-bearing prediction in the file, `A-P1`, is untested and untestable from a desk** — and the file's most-cited confirmation (`A-P4`, 2.5–3.0×) is *not* evidence for it.
3. 🔴 **The strongest thing I found, I did not find** — it was already in `DL-MECH-067`/`068`, in more detail, with better sources. Four minutes of believing otherwise is the honest measure of how easily this fails.
4. **Two of five hypotheses are transfers of primitives or facts owned by others** (the repository's common-mode argument; the `MAPT` field's biochemistry). The agent-novel content is the **connection**, which is real but smaller than a whole hypothesis.
5. **HYP-5 is weak and is in the list only because it is a required control.** Four strong items would have been a better list than five.

🔵 **What is deliberately NOT restated as a finding:** the seed material — the `46.2 kDa` band under
a changed antibody, the Lou/Atanasov decoupling, Tau-as-effector, `NeuN`-cannot-see-Purkinje, the
global hypothermia effect, `0/13` insoluble fractions, `Q230P`'s burial, terminal-exon NMD escape.
**Those are this session's inputs.** They appear above only where a new inference is built on them,
and never as a result of this file.

---

**END.** Non-canonical. No `*_current.md`, registry, queue, ledger, receipt or state-manifest file
was created, read for modification, or written. No `BATCH_COMMIT`. No `git`. No external contact,
no purchase, no quotation — `HUMAN_REQUIRED`. **Nothing here is medical advice, and no hypothesis
above is a treatment proposal.**

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V1 · 🥇 `HYP-1` is the best thing this session has generated, and it converges with a design cut made independently

> **A cycloheximide chase on `Q230P` will return a normal half-life, and it will be a FALSE
> NEGATIVE** — chains lost during folding never enter the chaseable pool.

🎯 **Endorsed, and it is stronger than the file claims, because a sibling reached the same place
from the opposite direction and neither knew.** Scientist B **cut the CHX chase** from the minimum
discriminator on the ground that it owns no matrix cell. `HYP-1` says something sharper: the chase
is not merely uninformative, it is **actively misleading**, because the pool it measures is defined
after the loss it is meant to detect. **Two independent actors, one cutting for economy and one for
validity, removed the same component.** That convergence is itself evidence.

🔴 **And the argument for spending money on it is the right shape:** the chase is cheap, standard
and *about to be run*; a clean-looking normal half-life would be filed as *"no turnover defect"* and
**nobody re-runs a clean result**. A false negative is worse than a failed experiment. The paired
short metabolic pulse-label — never run for **any** WWOX allele in any system — is the only arm that
can see the branch the chase is structurally blind to. One harvest, two readouts.

⚠️ **Novelty accepted with its stated ceiling.** `AGENT-NOVEL` on an unscoped sweep
(`cotranslational` 0, `co-translational degrad` 0, no chase-misleads statement anywhere, against
`CHX chase` in ~22 files). **All of it is `abstract-depth`** — no full text was read and none is
claimed, which is a real bound on all five hypotheses and the file says so.

## V2 · 🟢 The refuted prediction is worth more than the prediction was

`HYP-2` predicted the mouse **over**-reports the WWOX→GSK3β→Tau limb. The evidence went the other
way: adult wild-type mouse is **4R-tau only**, 4R assembles microtubules **2.5–3.0× faster** than
3R, and the human retains 3R for life and is 3R-dominant as an infant. ⇒ **the `Wwox`-null mouse may
be the conservative host and UNDER-report the human ceiling of the downstream arm.**

🟢 **Recorded as a refutation of its own prediction and a new `IPOTESI`, not retrofitted** — which is
precisely what pre-registration is for. If it holds, it inverts the usual direction of a
mouse-to-human caution, and that is the kind of finding that changes how a result is read rather
than merely adding one.

⚠️ `abstract-depth`; the isoform facts carry `PREMISE: UNREAD_PRIMARY`. And the file's own
`COULD NOT ESTABLISH` names the sharpest consequence: **the tau isoform used in Wang 2011's
cell-free assay is still unstated, and every molar figure in this repository's per-molecule argument
depends on it.**

## V3 · 🟢 Four ideas killed by the novelty protocol — this is the section I would show a sceptic

Cofactor-assisted folding (held as `D4`, then refuted by AKR sign-inversion); AAV episomal dilution
in the granule lineage (held twice, with a better falsifier); a degron-less frameshift product from
`c.1057-2A>G` (dead — the outcome is in-frame `p.Gln353_Gln354del`, no PTC); and the closest call,
the WWOX/Axin-site β1-selective bridge, *"which I believed was my best finding for about four
minutes"* before finding `DL-MECH-067`/`068`/`DL-BIO-013` already holding it **with primary
biochemistry the delegate did not have**.

🎯 **Four rediscoveries caught before publication, by an actor checking its own novelty rather than
being corrected afterwards.** This is `enumerate_baseline_before_scoring` executed properly, on the
first attempt, by a delegate — the **second** clean success of that primitive today after three
failures, and the first by someone other than me.

## V4 · Two self-inflicted narrowings, both endorsed

🟢 The proline-*cis/trans* mechanism behind `HYP-1` is **substantially weakened** — folded proteins
predominantly carry *trans*-Pro and unfolded *cis* populations are <5 %, so the rate-limiting case
needs a *cis*-proline the file cannot establish. 🟢 **The predictions survive anyway**, because they
depend on **when** the molecule is lost, not **why** — and separating those two is the correct move.
🟢 `HYP-4`'s discriminator is **less discriminating than claimed**: in ΔF508 CFTR, temperature acts
at **two** steps, so a ratio > 1 establishes allele-selective temperature sensitivity, not
folding-versus-degradation.

🔴 **`HYP-4` also partially reopens something I withdrew today**, and I want the tension recorded
rather than resolved prematurely. I withdrew the 26–30 °C arm because mild hypothermia is a global
degradation inhibitor. `HYP-4` argues the confound is **common-mode and cancels in a variant:WT
ratio** — the same argument I myself used for the TX-007 dose-unit problem, where the unknown
convention cancels in `HD/LD`. **The analogy is apt and the conclusion is not yet earned**: a dose
multiplier cancels exactly, whereas temperature sensitivity of degradation may differ between a
wild-type and a misfolded substrate, which is the whole premise of the experiment. The arm stays
withdrawn; `HYP-4` is the right way to argue it back, and it would need a WT-versus-variant
temperature-sensitivity measurement first. `C+` is the right grade.

## V5 · What this file is for

This session has been overwhelmingly a defect hunt. **This is the file that is not**, and its
honesty is what makes it usable: two sealed traces, one prediction refuted in its direction, four
attractive ideas killed, one hypothesis (`HYP-5`) admitted to *"change almost nothing anyone would
do"* and ranked last instead of dressed up, and a stated ceiling that **no full text was read**.

**Grades endorsed as given**, including `C−` for `HYP-5` and `C` for cycle 2's hypothesis survival.
**Nothing graded F**, and the four that would have been are in §4, dead.

**No hypothesis here is canonical, none is a therapy, none is proposed for `BATCH_COMMIT`.**
Nothing is medical advice.
