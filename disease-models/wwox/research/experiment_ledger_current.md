# Experiment Ledger — designed experiments, their decisions, and their results

> **Public edition — de-identified, disease-level.** No identified person, no report or sample
> identifier, no institution, no family-relationship data, no treatment schedule. Where the private
> edition would reason about one child, this reasons about **the reference genotype** — a WWOX-DEE
> genotype class. Donor-derived cells are described as donor-derived. **Not medical advice:** nothing
> here is a clinical recommendation, and no dose, route or schedule appears in this file by design.
>
> **Research layer — non-canonical, append-only. READ-ONLY toward the four canonical current files.**
> An experiment record never becomes a claim. A result recorded here reaches the canonical model only
> through a `COMMIT CANDIDATE` under `BATCH_COMMIT`, with its read receipts and verbatim locators.
>
> Created: 2026-09-26 · Reference WM: see `../registries/working_model_current.md`
> Created by: Harness Engineering, at the operator's instruction, under LEGEND_CORE §21e (T0).

---

## Why it exists

LEGEND already had three research-layer ledgers and a queue:

| Object | Home |
|---|---|
| a **lead** worth pursuing | `discovery_ledger_current.md` |
| a **negative** or a premise that closes a door | `dismissal_ledger_current.md` |
| a **therapeutic hypothesis** | `therapeutic_hypotheses_ledger_current.md` |
| a **paper** waiting to be acquired | `full_text_queue_current.md` |

It had **no home for a designed experiment.** So experiments were being specified inside analysis
files and handoff briefings — `q230p_minimum_discriminator_*`, `proteostasis_discrimination_protocols_*`,
`../handoff/Q230P_HANDOFF_TO_TOOLED_INSTANCE_*` — where three things happen to them:

1. **They are invisible to the next session**, because an analysis file is read for its conclusion,
   not for the experiment buried in its §5.
2. **They are re-derived.** The exon-7 cross-pair amplicon was estimated at "729–1015 bp" in one
   document and resolved to 878 bp in another four days later; the exon 7/8 boundary was carried as
   `UNKNOWN within a 90-nt window` while another surface already held it.
3. **Their pre-registered branches decay into a single expected outcome**, because nothing holds the
   branch table once the prose around it is edited.

This ledger is the home. One record per experiment, from proposal through result, never deleted.

### What belongs here, and what does not

**Here:** anything that would produce a new measurement — wet-lab, computational, or in an existing
model system — together with the decision it settles.

**Not here:** acquiring a paper (that is `full_text_queue_current.md`), reading a figure that an
acquisition document already instructs (same), a defect in the record (that is
`record_repair_queue_current.md`), and a therapeutic hypothesis that names no measurement (that is
the hypotheses ledger). **An object with a home does not get a second one.**

---

## Schema

```
ID            EXP-<YYYYMMDD>-<SLUG>-NN        assigned at proposal, never reused, never renumbered
DECIDES       the one question this settles, phrased so that an answer changes what happens next
DESIGN        arms, readout, and the control that makes a null readable
MATERIAL      NONE | IN_VITRO | CELL_LINE | EXISTING_ANIMAL | HUMAN_REQUIRED
BRANCHES      every outcome, pre-registered, each with its consequence — written BEFORE the run
FALSIFIER     what result would refute the reasoning that motivated the experiment
UNNECESSARY_IF  the cheaper result that would make this experiment pointless
COST          order of magnitude only: hours / days / weeks / months
STATUS        PROPOSED | READY | RUNNING | REPORTED | SUPERSEDED | ABANDONED
RESULT        empty until REPORTED. Then: what was measured, and which branch fired
```

**Status rules.** `PROPOSED` means designed, not yet runnable. `READY` means every prerequisite is
discharged. `SUPERSEDED` names the record that replaced it. `ABANDONED` carries the reason, and
abandonment is the only status that may be applied without a result — never silent deletion.

🔴 **The branch table is written before the run and is not edited afterwards.** If a branch was
missing, the record gains an amendment line with its date; the original stays legible. An experiment
whose branches were rewritten after its result is an experiment that decided nothing.

🔴 **`MATERIAL: HUMAN_REQUIRED` is the programme's scarce reagent.** Every such experiment must state
which other `HUMAN_REQUIRED` records share its harvest, so one donor-derived sample serves all of
them. A harvest protocol written after the material arrives has already wasted it.

---

## Index

| ID | Decides | Material | Status |
|---|---|---|---|
| [`EXP-20260926-Q230P-SUBSTITUTION-01`](#exp-20260926-q230p-substitution-01) | Whether escaping the proline is a therapeutic route at all | `CELL_LINE` | `PROPOSED` |
| [`EXP-20260926-WWOX-GT-PHENOTYPE-02`](#exp-20260926-wwox-gt-phenotype-02) | Whether a small increment above zero is informative or therapeutic | `EXISTING_ANIMAL` | `PROPOSED` |
| [`EXP-20260926-Q230P-PROTEIN-FATE-03`](#exp-20260926-q230p-protein-fate-03) | Whether any Q230P protein exists, where, and above what floor | `HUMAN_REQUIRED` | `PROPOSED` |
| [`EXP-20260926-EXON7-ARCHITECTURE-04`](#exp-20260926-exon7-architecture-04) | Whether the transcript contains the exon carrying the variant | `HUMAN_REQUIRED` | `READY` |
| [`EXP-20260926-SDR-INTEGRITY-READOUT-05`](#exp-20260926-sdr-integrity-readout-05) | Whether a readout exists that a WW1-competent, SDR-dead rescue would fail | `CELL_LINE` | `PROPOSED` |
| [`EXP-20260926-WWOX-COFACTOR-BINDING-06`](#exp-20260926-wwox-cofactor-binding-06) | Whether WWOX binds a dinucleotide cofactor at all | `IN_VITRO` | `PROPOSED` |
| [`EXP-20260927-DOMINANT-NEGATIVE-07`](#exp-20260927-dominant-negative-07) | Whether the mutant protein interferes with a supplied wild-type copy — the gate on gene replacement | `CELL_LINE` | `PROPOSED` |

**Shared harvest:** `-03` and `-04` are the same donor-derived sample. Neither is run alone.

**Cheapest first, and it is not a coincidence.** Four of these seven need **no donor material**:
`-01`, `-05`, `-06` and `-07` run in cell lines or in vitro, and `-02` uses an animal that already
exists. Only `-03` and `-04` are `HUMAN_REQUIRED`, and they share one harvest. The programme is
therefore not blocked on access to material — a conclusion worth stating plainly, because the
preceding handoff had ordered the work the other way round.

---

## EXP-20260926-Q230P-SUBSTITUTION-01

**DECIDES** — Is "escape the proline" a therapeutic route? The lesion at codon 230 is a **backbone**
lesion: `Gln230` sits at helix position N4 of αE, the first residue whose backbone amide donates an
`i,i−4` hydrogen bond (N230←O226 **3.03 Å**, measured; the three preceding positions have no such
bond at 9.35, 10.25 and 6.88 Å). A proline has no amide hydrogen. **Any** non-proline restores the
donor — so the question is not whether glutamine can be restored, but whether a *different* residue
is tolerated.

This matters because of a hard chemistry bound: reverting `c.689A>C` requires a `C•G → A•T`
transversion, which mature mammalian base editors do not perform. A cytosine base editor, however,
reaches two non-proline outcomes inside the mutant codon.

**DESIGN** — Four arms as cDNA in a WWOX-deficient human cell line: wild type · Q230P · **Q230L** ·
**Q230S**. Readouts: steady-state level, **solubility (S/P/T)**, and subcellular localisation — not
abundance alone, per the design rule in `record_repair_queue_current.md` `REP-11`. Controls: empty
vector; and a catalytic-dead arm built as **`N232A` / `S260A` / `Y293F` / `K297A`** — 🔴 **never
`S281A`**, see `REP-01`.

**Why these two residues and no others.** Measured on the mutant CDS this session: with the SpCas9
PAM `GGG` at `c.703–705`, the protospacer is `c.683–702` and the canonical editing window
`c.686–690` reads `TTCCA`. It contains **exactly two cytosines, both inside codon 230**.

| Edit | Codon 230 | Residue |
|---|---|---|
| `c.689C>T` | `CTA` | **Leu** |
| `c.688C>T` | `TCA` | **Ser** |
| both | `TTA` | **Leu** |

Every outcome removes the proline. The flanks protect themselves: `c.685–687` is `TTT` (no cytosine)
and **`c.690–696` is `AGTGAAT` — no cytosine at all**, so `Val231` and, critically, the catalytic
`Asn232` (`AAT`) cannot be hit. The nearest deleterious bystander positions sit **outside** the
window.

**BRANCHES**

| Result | Consequence |
|---|---|
| Q230L stable, correctly localised | 🟢 The base-editor route has a validated product. Proceed to editor design and off-target work |
| Q230L stable but mislocalised | 🟡 Backbone repaired, side chain insufficient. Route survives only if prime editing to true reversion is also pursued |
| Q230L and Q230S both behave as Q230P | 🔴 Route dead. Only **prime editing to true reversion** remains among editing approaches |
| Q230S worse than Q230L | Expected — Ser leaves a cavity at a fully buried position. Record and drop Q230S |
| Q230P itself stable in this system | 🔴 Reframes everything: the instability is cell-type- or context-dependent, and the founding negative is about the donor cell type |

**FALSIFIER** — The reasoning says the lesion is a backbone lesion. If Q230L is as unstable as
Q230P, the backbone account is insufficient and the side chain is load-bearing.

🔴 **The prior is unfavourable and is recorded as such — and it worsened on 2026-09-27.** Three
arguments against tolerating any substitution here:

1. **Conservation.** `Gln230` is **invariant across 20 of 21 orthologues** with alignment coverage,
   from primates through chicken, *Xenopus*, zebrafish, coelacanth and *Drosophila melanogaster*;
   only one basal chordate carries a different residue. Stricter purifying selection than the
   catalytic-asparagine position two residues away.
2. 🔴 **The side chain does real work, and this is the argument that most damages the hypothesis.**
   `Gln230`'s side chain makes **four** polar contacts and staples **three** structural elements
   together — its own helix, the 221–223 loop and the 182–187 helix. Verified here to the hundredth
   of an ångström: `OE1`···`Thr221` OG1 **2.54 Å** · `NE2`···`Asp223` OD2 **2.72 Å** ·
   `NE2`···`Ala185` O **3.20 Å** · `NE2`···`Leu184` O **3.46 Å**. Two of those partners are
   annotated cofactor-binding residues, so this residue holds the catalytic helix against the
   cofactor-binding loop. **Neither leucine nor serine can make four hydrogen bonds.** A proline
   abolishes five interactions — the four above plus the backbone donor; leucine and serine restore
   the backbone donor and replace little else.
3. The programme's earlier framing of `Gln230` as a *second-shell* residue is therefore **withdrawn**.
   It is a packing determinant, not a passenger.

🟡 **One counter-indication, kept at low weight because its own source is discredited here.** A
structure-based missense classifier scores `Q230A` and `Q230G` as *likely benign* while scoring
`Q230P` as likely pathogenic — i.e. it attributes the damage to the proline specifically rather than
to loss of the glutamine, which would favour this experiment's premise. But the same classifier
scores **two WWOX variants that are experimentally null as likely benign**, in this very protein. A
same-protein counterexample retires the classifier as evidence in either direction.

🎯 **Why the experiment's value went UP while its prior went DOWN.** Two independent analyses of this
variant now hold **opposite predictions** for a non-proline substitution at 230 — one from the
hydrogen-bond network, one from the classifier's per-residue pattern — and **two site-directed
mutants separate them**. An experiment that decides between two documented, opposed predictions is
worth more than one that confirms a consensus. A negative retires an entire therapeutic route for the
cost of two mutants, and it is the cheapest route-retirement available to this programme.

**UNNECESSARY_IF** — `-03` shows Q230P protein is abundant and functional untreated.

**COST** — days. **MATERIAL** — `CELL_LINE`. **STATUS** — `PROPOSED`. **RESULT** — —

---

## EXP-20260926-WWOX-GT-PHENOTYPE-02

**DECIDES** — Is a small increment of WWOX above zero *informative* or *therapeutic*? Every
protein-raising proposal in this programme is scored against a threshold nobody has measured.

**DESIGN** — The `Wwox^gt/gt` gene-trap line, which has *"no detectable"* Wwox protein in most
tissues and is nonetheless **viable**, where the full null dies at 3–4 weeks. Measure, in that
existing line: **brain WWOX by calibrated immunoblot with a standard curve** (the quantity has never
been measured), EEG, seizure threshold, and a behavioural battery. Compare against wild type and,
where available, the null.

🎯 **This is the only system sitting at a low-but-nonzero WWOX dose, and it has never been asked the
therapeutic question.** Published 2007. Nothing about it is expensive.

**BRANCHES**

| Result | Consequence |
|---|---|
| Brain WWOX low-but-measurable **and** neurodevelopment substantially spared | 🟢 A small increment is plausibly therapeutic. The strongest argument the programme could obtain for any protein-raising approach |
| Brain WWOX low-but-measurable **and** severe EEG/behavioural phenotype | 🔴 Survival and neurodevelopment have different thresholds. Protein-raising is informative, not therapeutic. Redirects the programme to correction and replacement |
| Brain WWOX genuinely undetectable on a calibrated assay | 🟡 The viability itself becomes the finding, and the floor question moves to the assay |

**FALSIFIER** — The pro-rescue argument rests on undetectable-but-nonzero differing from zero. A
severe neurological phenotype in this line refutes the therapeutic reading of that difference while
leaving the survival reading intact.

🔴 **Tumour axis, recorded here because this line carries it:** the same hypomorph shows a *"higher
incidence of spontaneous B-cell lymphomas"* and testicular atrophy. Any partial-restoration strategy
inherits that signal. See `REP-12`.

**UNNECESSARY_IF** — nothing cheaper answers it. No in-vitro experiment can.

**COST** — weeks to months. **MATERIAL** — `EXISTING_ANIMAL`. **STATUS** — `PROPOSED`. **RESULT** — —

---

## EXP-20260926-Q230P-PROTEIN-FATE-03

**DECIDES** — Does any Q230P protein exist, in which fraction, and above what **quantified** floor?
The founding measurement examined a RIPA-soluble supernatant, discarded the pellet, and stated no
limit of detection. *"Not detected"* there is the identical observable for **never made**,
**destroyed**, and **sitting in the pellet** — and half of every drug table in this programme points
the wrong way until they are separated.

**DESIGN** — One donor-derived harvest, shared with `-04`. Three fractions from one lysate: `S`
detergent-soluble supernatant · `P` pellet resolubilised in SDS/urea · `T` no-spin total.
`S + P ≈ T` in the control lane is the design's own validity check.

🔴 **Normalisation: load by input-equivalents (equal cell-equivalents), never by equal total protein
per fraction.** The hypothesis is that the protein has *moved* from `S` into `P`; normalising each
lane to the same µg re-scales every fraction to a common denominator and divides out exactly the
redistribution being measured. Total-protein stain is a transfer control, never the normaliser.

🔴 **Urea at ≤ 50 °C.** Above ~50 °C, 8 M urea carbamylates lysines and shifts the band the
experiment exists to detect.

🔴 **A wild-type human dermal fibroblast lane is mandatory, and this is new.** WWOX protein
expression was reported **absent in normal connective tissue**, and the founding blot used cancer
lines and HEK293 as positive controls — **no wild-type fibroblast lane exists**. Mitigating evidence
that the model is not void: the transcript is present in the donor-derived cells, and another group
detected *and* knocked out WWOX in cultured human skin fibroblasts. ⇒ **The limit of detection is
not a technicality; it is the whole question.** If WWOX is barely detectable in the control lane, the
experiment does not need a larger gel — it needs enrichment or mass spectrometry.

**Orthogonal, epitope-free arm.** The census finding that **0 of 17** anti-WWOX antibodies has an
epitope C-terminal to residue 230 is an **immunoassay** constraint, not a folding-readout constraint:
peptide-based methods read tryptic peptides, not epitopes. Five tryptic markers were verified this
session as **proteotypic** — unique to `Q9NZC7` across 20,431 canonical and 42,562 isoform-inclusive
human sequences, and still unique with Ile/Leu collapsed:

| Peptide | Residues | Reports |
|---|---|---|
| `NVPLHVLVCNAATFALPWSLTK` | 201–222 | exon 7 present |
| `FTDINDSLGK` | 265–274 | exon 7 present |
| `NVFTDINDSLGK` | 201–202 ⁀ 265–274 | **exon 7 skipped — junction** |
| `DGLETTFQVNHLGHFYLVQLLQDVLCR` | 223–249 | residue 230 = Gln |
| `DGLETTFPVNHLGHFYLVQLLQDVLCR` | 223–249 | **the variant protein is present** |

With isotope-labelled synthetic standards the floor is reported in **absolute quantity** rather than
cell-equivalents. 🔴 **But the two diagnostic markers have zero background by construction, so no
natural sample can validate that they are detectable.** The light synthetic peptide must be spiked
into a control digest and seen **in matrix** before its absence is used to assert anything. That is
the programme's own positive-control rule applied to mass spectrometry.

**Fallback if the 27-mer does not fly:** Glu-C yields `c.`227–245, a **19-mer with no cysteine**
covering residue 230. Ordered only if the tryptic marker fails, since a second protease costs a
second standard, a second uniqueness check, and the loss of the single-digest design.

**Synthesis-vs-turnover arm.** A **short metabolic pulse-label** read as S/P/T separates all three
routes: low incorporation at the shortest pulse ⇒ impaired synthesis; label present early and gone
next ⇒ co-translational disposal; label reaching a stable pool then decaying ⇒ post-translational
degradation; label in the pellet ⇒ aggregation, which has never been looked for in any WWOX allele.
🔴 **A cycloheximide chase cannot do this** — it is structurally blind to co-translational failure.

**BRANCHES**

| Result | Consequence |
|---|---|
| Protein in `P`, absent from `S` | 🟡 Insoluble sequestration. 🔴 **Raises rather than lowers the safety bar** — forcing more aggregation-prone protein into a neuron is a hazard, not a rescue |
| Protein in neither, control lane strong | 🟢 A real quantified negative, cell-type-matched for the first time |
| Protein in neither, **control lane weak** | 🔴 The assay is underpowered by biology. Escalate to mass spectrometry; do not report a biological negative |
| Pulse-label low at t=0, raised by proteasome block | Co-translational disposal. The whole proteostasis drug table is aimed at the wrong compartment |

**FALSIFIER** — the premise that Q230P behaves as a null. Any quantified soluble pool refutes it.

**UNNECESSARY_IF** — nothing. This is the fork.

**COST** — days once material exists. **MATERIAL** — `HUMAN_REQUIRED`, shared harvest with `-04`.
**STATUS** — `PROPOSED`. **RESULT** — —

---

## EXP-20260926-EXON7-ARCHITECTURE-04

**DECIDES** — Does the mature transcript contain exon 7, the exon carrying the variant? Currently
`UNKNOWN`, never interrogated by any published assay. 🎯 **If exon 7 is absent, every protein
measurement so far looked for a ~46 kDa species when the product would be ~39.8 kDa and would not
contain residue 230 at all** — and the proteostasis programme would be targeting a protein that does
not exist.

**DESIGN** — Endpoint RT-PCR across exon 7 on donor-derived RNA. Both published primer pairs bracket
exon 7 and cover none of it; two crossings do span it. All coordinates below were computed this
session from `NM_016373.2` and validated against four published observables that reproduce exactly
(277 bp, 200 bp, 593 bp, 504 bp).

| Pair | Spans exon 7 | WT | Δexon-7 | Shift |
|---|---|---|---:|---:|
| **primary** — published pair, exon 4 → exon 8 | yes | **593 bp** | **407 bp** | 31 % |
| **confirmatory** — cross-pair, exon 4 → exon 9 | yes | **878 bp** | **692 bp** | 21 % |

The primary pair is preferred because it is **published and working**, has paired melting
temperatures, and resolves a 31 % shift. The earlier preference for the cross-pair rested on the
reverse primer's exon being unknown; it is **exon 8** (`c.951..969`), so that reason has lapsed.
🔴 **And the anti-genomic argument once offered for the cross-pair was wrong and is withdrawn** —
all four pairs span ≥ 271 kb of intron and are equally genomic-incompatible (`REP-10`).

🔴 **Sanger-sequence the amplicon in EVERY branch, not only on a shifted band.** A wild-type-sized
band establishes that exon 7 is present at the expected length; it does **not** establish that
`c.689A>C` is in the mature transcript. Only the sequence does, and the amplicon is already
sequenceable, so the cost is nil.

**BRANCHES**

| Result | Consequence |
|---|---|
| WT size only, variant confirmed by sequence | 🟢 `-03` proceeds as designed |
| Δ186 only | 🔴 `-03`'s gel window and antibody choice are both wrong. Confirm the junction against **`NM_016373.2`**, never the current RefSeq |
| Both bands | 🟡 Quantify proportion and confirm both identities first. **A long-amplicon size ratio is not an isoform ratio** |
| No product | 🔴 Assay failure or RNA quality. **Never a biological negative.** Re-run with an independent amplification control in the same tube |

**FALSIFIER** — none needed; this is a measurement, not an inference. Its value is that three of its
four branches change `-03`.

🟡 **The prior moved on 2026-09-27, and the experiment did not.** Two independent splice predictors
run on the reference transcript return **no predicted splicing effect** — acceptor gain 0.000,
acceptor loss 0.001, donor gain 0.001, donor loss 0.002, with the native exon-7 donor essentially
unchanged (0.978 → 0.980) — and a second tool agrees. This programme had never run a splice predictor,
so it is new evidence, and it makes the skipped branch **less likely**.

🔴 **It does not close the question and does not lower this experiment's rank.** A prediction is not a
measurement; the branch that the prediction disfavours is the branch that would invalidate the gel
window and the antibody choice of `-03`; and exon-7 abundance, allele-specific expression and
transcript half-life remain unmeasured whatever the splice-site scores say. The experiment costs hours
and shares a harvest it does not consume alone.

**Standing derivation, now fact.** The CDS is **byte-identical across `NM_016373.2`, `.3` and `.4`**
(1245 nt, 414 aa); the versions differ only in UTR length, so `c.` coordinates do not move. Exon 7 is
`c.606–791`, 186 nt, in-frame. A skipped product is **`p.(Pro203_Arg264del)`**, 352 aa,
**39.795 kDa**, and the junction codon is `GTA` = Val — identical to wild-type residue 202, so **no
novel residue is created**. 🔴 That product would delete the putative catalytic **Ser260** and eight
cofactor-pocket-wall residues while retaining both WW domains: **SDR-dead, WW-competent** (`REP-08`).

**UNNECESSARY_IF** — nothing. **COST** — hours once material exists. **MATERIAL** — `HUMAN_REQUIRED`,
shared harvest with `-03`. **STATUS** — `READY` — no prerequisite remains. **RESULT** — —

---

## EXP-20260926-SDR-INTEGRITY-READOUT-05

**DECIDES** — Is there a readout that a **WW1-competent but SDR-dead** rescue would *fail*? Without
one, no rescue experiment in this programme can be interpreted.

🔴 **The trap this exists to avoid.** The only reporter published in human fibroblasts reads a
**WW1-mediated** interaction. A rescue producing SDR-inert but WW1-competent protein would **pass**
it — a false positive. And the structure predicts exactly that product: `Gln230` is **3.42 Å** from
the catalytic `Asn232`, two residues away on the same helix, and the `i,i−4` register a proline
destroys is the register that positions that asparagine. **The wrong readout would report success on
the precise failure mode the geometry predicts.**

**DESIGN** — Build an **SDR-integrity-dependent** readout. Leading candidate: a partner deletion-
mapped to the **N-terminal SDR**, with a published endogenous co-immunoprecipitation in a human
cell, and whose PPxY motif lies **outside** the binding region — therefore immune to the WW1 false
positive. One figure must be read to fix the residue boundaries. Second candidate: localisation
dependent on an intact SDR domain — 🔴 currently sourced to a **review**, and its primary source was
searched for and not found (`REP-04`). Threshold, copied from a regulator-accepted amenability
assay: **≥ 3 % of wild type in absolute terms AND ≥ 1.2-fold over the variant's own baseline** —
both clauses required, the absolute clause killing noise amplification on near-zero baselines and the
relative clause killing trivial bumps.

**BRANCHES** — Readout is SDR-dependent and continuous ⇒ 🟢 the programme has its instrument, and
every rescue experiment becomes interpretable. Readout is WW-dependent after all ⇒ 🔴 record as a
**necessary-condition gate only**: fail ⇒ dead, pass ⇒ **not shown to work**.

**FALSIFIER** — a readout that moves when only the WW domains are intact is not an SDR readout,
however it was labelled.

🎯 **A second, sharper readout was identified on 2026-09-27, and it comes with a distinctive
signature.** `Gln230` is in **direct contact with the KFERQ-like chaperone-mediated-autophagy motif
`LRSVQ` at 187–191** — measured here at **3.95 Å**, to `Leu187` — and two of its four hydrogen-bond
partners (`Leu184`, `Ala185`) lie in the same helix as that motif. That motif is a **demonstrated**
HSC70 recognition site in WWOX for a different allele, not a sequence coincidence. Also at 3.46 Å from
the motif: **`L239R`**, another disease-associated position on the same helix.

⇒ **Falsifiable hypothesis with its own experimental signature:** the substitution locally unfolds the
184–191 helix and **exposes the CMA motif**, routing the protein to a lysosomal rather than
proteasomal fate. Signature: **rescued by lysosomal inhibition, not by proteasomal inhibition.**

🔴 **Recorded as `SPECULATIVE` and bounded three ways.** The precedent allele is **surface-exposed**
(relative accessibility 0.53) and **20.6 Å away**; its work used **overexpressed tagged constructs in
a cancer line**, not endogenous protein in a neural cell; and a buried helix-core substitution is at
least as likely to be triaged to the proteasome or to aggregate. What the precedent legitimately
licenses is narrow: that a WWOX missense allele *can* be cleared without proteasome involvement, and
that the motif is functional. It licenses **no pathway assignment** for this allele.

**Confirmatory tier, not screening tier.** Patient-derived neural organoids carry a genuine human
functional readout that **gene therapy has been shown to normalise**. Using organoid
electrophysiology as the *primary* screen would be the classic error. Two bounds: **no donor line
carrying this allele exists**, and delivered protein lands between **0.4× and 7× wild type** across
lines given the same vector, with the wild-type-versus-treated bracket never drawn.

**UNNECESSARY_IF** — nothing. This is the bottleneck. **COST** — weeks. **MATERIAL** — `CELL_LINE`.
**STATUS** — `PROPOSED`. **RESULT** — —

---

## EXP-20260926-WWOX-COFACTOR-BINDING-06

**DECIDES** — Does WWOX bind a dinucleotide cofactor at all? Every structure-based stabilisation
proposal presupposes it, and it has never been measured.

**What is established, and it is structure only.** Measured this session on `AF-Q9NZC7-F1`, with
identical values on the superseded v2.0 coordinates the repository holds: the Rossmann glycine-rich
motif is **`T130-GANSGIG-137`**, the canonical `TGxxxGxG`; the catalytic pair is **`Y293xxxK297`**;
the tetrad is **Asn232–Ser260–Tyr293–Lys297**; the cleft is lined by 64 residues within 8 Å of the
glycine-rich loop with Tyr293 **7.94 Å** from it — one contiguous site. **`Gln230` is not part of
that pocket wall**, at 9.37 Å from Tyr293 and 12.05 Å from the motif. That is the geometry of a
remote-site stabilisation target, the mode that works for several marketed stabilisers.

🔴 **And it is all `ECO:0000250` — inferred by sequence similarity, not experiment.** No WWOX protein
has ever been shown to bind NAD or NADP by any direct measurement. Catalytic activity was measured
**exactly once**, in a crude bacterial extract, wild type only, oxidation only, no purified enzyme,
no dead control, never replicated. The only experimental WWOX structure in existence covers **WW2
alone**; the SDR domain has **zero** residues of experimental coverage.

**DESIGN** — Differential scanning fluorimetry on recombinant human WWOX, ± the four cofactor
species **separately**: NAD⁺, NADH, NADP⁺, NADPH. Positive control: a protein with a known
cofactor-induced thermal shift, in the same run.

**Why the four species are separated.** A repurposing proposal to raise intracellular NAD(P) with
precursors was **refuted on occupancy grounds** — the natural cofactor is already abundant in the
donor-derived cells and already failed to preserve the protein, unlike sub-saturating hepatic
cofactor loading in another disease. One reservation survives and this arm settles it: **oxidised
NADP⁺ is the scarcest of the four species in the cytosol**, and the single enzymology report
describes activity with the oxidised forms and none with the reduced ones. A shift specific to NADP⁺
would reopen a door the occupancy argument otherwise closes; a shift with none of the four closes it
for good.

**BRANCHES** — Shift with any species ⇒ 🟡 the site is real and occupiable; a designed non-natural
higher-affinity ligand becomes conceivable, though it needs a structure that does not exist. No shift
with any ⇒ 🔴 the pocket is vestigial, the cofactor-stabilisation class is dead, and the programme
keeps only the proteostasis-machinery and correction routes.

🔴 **Selectivity bound, recorded now so it is not discovered later:** the dinucleotide cleft is the
worst available selectivity target for a central-nervous-system agent in an infant, because it
inherits the whole dehydrogenase proteome. A positive result here licenses a mechanism, not a
molecule.

🔴 **And a harder bound, obtained independently on 2026-09-27, which this programme had reasoned its
way to but never measured.** A curated target-tractability assessment returns, for this gene:
**no approved drug, no clinical candidate, no chemical probe, and every small-molecule tractability
bucket `false` — including both "high-quality pocket" and "medium-quality pocket".** Combined with
zero experimental coverage of the domain, a selective stabiliser for this allele is a **de novo
discovery programme starting from no structure and no pocket**, not a repurposing exercise. That is
a curated assessment rather than an inference, so it is the stronger form of the conclusion this
programme had already reached, and it belongs wherever a stabiliser is proposed.

**FALSIFIER** — the structural inference that the cofactor site is functional.

**UNNECESSARY_IF** — nothing cheaper. **COST** — days. **MATERIAL** — `IN_VITRO`, purchasable
protein. **STATUS** — `PROPOSED`. **RESULT** — —

---

## EXP-20260927-DOMINANT-NEGATIVE-07

**DECIDES** — Does the mutant protein interfere with wild-type WWOX? This gates **gene replacement**,
which is currently the only modality with demonstrated functional rescue in a patient-derived model —
so it gates the programme's strongest route, and nobody has tested it.

**Why it is its own record and not an arm of `-03`.** When this experiment was first proposed to the
operator it was described as an arm of the patient-cell protein-fate experiment. That was wrong:
`-03` is `HUMAN_REQUIRED` and this is a co-expression experiment in a cell line. Binding it to `-03`
would have made the programme's strongest gate wait on its scarcest reagent, for no reason.

**The gap it closes.** Every efficacy datum for gene replacement comes from a **null** background —
an animal with no protein at all — not from a missense knock-in. Gene addition assumes the supplied
wild-type copy works in the presence of whatever the mutant allele produces. If the mutant protein is
insoluble or aggregation-prone — the branch `-03` may return — that assumption is not safe: an
aggregating species can sequester its correctly-folded counterpart.

**DESIGN** — Co-express wild-type WWOX with the variant, across a titration of mutant-to-wild-type
ratio, in a WWOX-deficient cell line. Ask of the **wild-type** protein: is its abundance reduced, its
solubility shifted, or its function (read on the `-05` readout) impaired, relative to wild type
expressed alone at the same level? Controls: wild type alone at matched expression; empty vector
co-expression to control for promoter competition; and a catalytic-dead arm
(**`N232A` / `S260A` / `Y293F` / `K297A`** — 🔴 never `S281A`, `REP-01`; 🔴 never `T266A`, `REP-19`)
to separate interference from loss of activity.

**BRANCHES**

| Result | Consequence |
|---|---|
| Wild type unaffected at every ratio | 🟢 Gene addition is not gated on this. The strongest route loses a bound it currently carries |
| Wild-type abundance or solubility reduced | 🔴 Dominant-negative. **Gene addition may be insufficient by itself**, and the design question becomes addition *plus* removal — or correction instead of addition |
| Wild-type function impaired without abundance change | 🟡 Interference at the interface, not at the level of protein fate. Names a mechanism and keeps the route with a monitor |
| Effect only at supraphysiological mutant load | 🟡 An artefact of the assay's own overexpression. Report the ratio at which it appears and do not transfer it |

**FALSIFIER** — the assumption, currently unstated wherever gene replacement is proposed, that the
mutant allele is inert toward a supplied wild-type copy.

**UNNECESSARY_IF** — `-03` shows no mutant protein anywhere at a quantified floor, in which case there
is nothing to interfere. 🔴 **Note the asymmetry: that is the same result which would make the
proteostasis routes pointless and the replacement route unobstructed.** One measurement, opposite
consequences for two classes — which is why `-03` outranks every molecule question.

**COST** — days. **MATERIAL** — `CELL_LINE`. **STATUS** — `PROPOSED`. **RESULT** — —

---

## Independent corroboration — a blind external analysis, 2026-09-27

A separate analysis of the same variant, built from a different tool set and without access to this
repository, was compared against these records. It is logged here because it changes the **confidence**
attached to several premises above, and because what it got wrong is as useful as what it got right.

**Reproduced exactly, from independent code on the same public model** — the strongest validation
available to a computational premise, since two implementations agreeing to the hundredth of an
ångström is not a shared assumption:

| Premise | Both |
|---|---|
| Backbone amide → `Glu226` carbonyl, the first helical `i,i−4` bond | **3.03 Å** |
| `Gln230` ↔ catalytic `Asn232`, minimum heavy atom | **3.42 Å** |
| `Gln230` → `Tyr293` · → the glycine-rich motif | 9.4 · 12.1 Å |
| Relative solvent accessibility of `Gln230` | **0.00** |
| Mapping of the published primers; both amplicons bracket exon 7 and sample neither | identical spans |
| Exon 7 in-frame, 186 nt = 62 codons | identical |
| The founding blot sampled the soluble fraction only, with a single discontinued polyclonal of undeclared epitope, **and no matched control fibroblast line** | identical |
| One experimental structure exists, covering a WW domain; the catalytic domain has **zero** coverage | identical |
| "Missense → normal protein level" is false as a WWOX generalisation | identical |
| **The pivotal question — would restoring abundance restore function — is `UNKNOWN`, and every stabilisation strategy is gated on it** | identical |

**Where it was wrong, and the programme is right:** it adopted a curated profile's active-site
annotation naming a residue that sits **12.56 Å** from the catalytic tyrosine — recorded as
`REP-19`, with the insertion that causes the mis-transfer named. 🔴 It had **measured the correct
residue at 4.09 Å and written it down**, then deferred to the database.

**Where the programme was wrong, and it is right:** four findings this analysis had never made, all
verified here before adoption — the four-hydrogen-bond network that retires the *second-shell*
framing of `Gln230` (`EXP-...-01`), the contact with the chaperone-mediated-autophagy motif
(`EXP-...-05`), the closest structural analogue being absent from the analogue set (`REP-23`), and
four guards the record lacked (`REP-20` to `REP-22`, `REP-24`).

**Where each found something the other could not.** The external analysis did **not** find the
catalytic-serine error (`REP-01`) — it bypassed the literature that carries it — and it **closed the
base-editing route one step early**, concluding that because reversion needs a transversion no editor
performs, base editing is inapplicable. `EXP-...-01` exists because the lesion is a *backbone* lesion,
so the goal is not restoring the glutamine but removing the proline. Conversely it supplied the
strongest argument **against** that route, in the hydrogen-bond network.

🎯 **The routing lesson, which generalises past this variant.** The external analysis is markedly
stronger on **variant annotation** — population frequency, clinical aggregation, splice prediction,
target tractability, domain profiles, orthologue depth, deep-mutational-scan coverage. This programme
is markedly stronger on **full-text reading and record integrity** — a figure-level read that moved a
therapeutic status, a full-text mechanism that overturned a protocol design rule, and the internal
contradictions in this queue. These are different capabilities, not degrees of the same one, and work
should be routed accordingly rather than duplicated.

---

## Amendments

**2026-09-27** — `-01` prior sharpened and the *second-shell* framing withdrawn; `-04` prior moved by
splice prediction with the branch table unchanged; `-05` gained a second readout and a falsifiable
clearance hypothesis; `-06` gained a curated tractability bound; `-07` opened. **No branch table was
edited.** Every change above is an addition to context or a new record; the pre-registered outcomes of
`-01` through `-06` stand as written on 2026-09-26.
