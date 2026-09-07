# COMMIT CANDIDATE — decisive experiment design: the sign and driving force of GABA in WWOX LoF

**Candidate ID:** CC-20260826-EGABA-EXPERIMENT-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** experiment design. 🔴 **This is not a therapeutic proposal and contains no therapeutic
recommendation.** Every drug named below is a **pharmacological tool or control**, never a
candidate treatment. Nothing here is medical advice.
**Change class:** MINOR — adds a specified decisive experiment to `RL-GABA-002`, which currently
names a hypothesis with no test attached
**Target WM:** current at BATCH_COMMIT time
**Batch gate:** intentionally untouched

---

## 0. Why this design is owed

`meta_gaba_paradox_current.md` runs to 246 lines and states the crux correctly:

> *"What kind of GABAergic dysfunction exists in WWOX LoF, at which developmental stage, and with
> what functional meaning for the network?"*

Across those 246 lines: **`E_GABA` appears 0 times. "reversal potential" 0 times. "gramicidin"
0 times.** `RL-GABA-002 — GABA depolarization hypothesis` exists as a research line with **no
specified experiment**. `KCC2` and `NKCC1` appear 3 and 4 times — as *molecular proxies for a
functional quantity nobody has measured*.

🔴 **The corpus contains zero measurements of the sign of GABA in any WWOX model.** That is not a
gap in the literature review; it is a gap in the literature. What exists is:

| What exists | What it is | What it is not |
|---|---|---|
| PV⁺/NPY⁺ interneuron counts, `Wwox`-KO hippocampus (`CLAIM 005`, PMID 30290271) | marker-positive **abundance** | inhibitory efficacy |
| GAD65/67 protein levels (same) | **protein abundance** | GABA concentration or synaptic release |
| KEGG "suppression of GABAergic synapses", `P47T` (PMID 36828035) | **expression programme** | a measure of inhibition |
| Cell-attached firing rate ↑6×, `Wwox`-null (PMID 34747138) | **net excitability** | attribution to GABA |
| SWD/spike rate on ECoG (PMID 42422765) | **network output** | a cellular mechanism |

Every row is a proxy. `meta_gaba_paradox`'s own **Hypothesis 2** — *"Quantity and function do not
coincide"* — is precisely the reason none of them can substitute for the measurement, and
PMID 36828035 has now demonstrated abundance≠function for WWOX protein itself
([`CC-20260826-PMID36828035-01`](CC-20260826-PMID36828035-01.md) §2.2).

### 🔴 The "zero measurements" claim was tested against the one premise that could have falsified it

A claim of the form *"nothing in the corpus measures X"* is a **universal negative**, and this
repository has already paid for asserting one without enumerating its denominator — the retracted
*"nobody has ever performed continuous video-EEG on a Wwox-null mouse"* in
[`CC-20260825-ADVERSARIAL-FALSIFICATION-01`](CC-20260825-ADVERSARIAL-FALSIFICATION-01.md). So the
denominator is enumerated here rather than assumed.

`session_self_eval.py` reports **four unread premises** across the whole state. Three
(PMID 25595186, 35328751, 36271927) are cited in `meta_metabolism_current.md` and concern
HIF1A/AMPK metabolism. **Exactly one is cited in `meta_gaba_paradox_current.md`: PMID 36828035** —
listed in its Evidence Base as *"P47T partial LoF → epilepsy, progressive neuroinflammation,
cerebellar degeneration"*.

**It has now been read** (receipt `FTR-20260826-36828035-01`), and its only GABA content is the
KEGG transcriptomic finding in §2.5 of that candidate — *an expression programme, not a functional
measurement*. ⇒ **The one unread premise capable of falsifying "zero measurements of the sign of
GABA" did not falsify it.** The negative stands, and it now stands with its denominator attached.

⚠️ **Scope of the negative, stated exactly:** it covers the papers LEGEND has read plus the four
premises it had not. It does **not** cover the ~356 corpus placeholders or the wider WWOX
literature, and it is not a claim that no such measurement exists anywhere — only that none has
entered this model, and that none of the papers this model rests on contains one.

---

## 1. The question, stated so it can be falsified

> **In WWOX LoF neurons, is GABA_A-receptor activation depolarizing relative to rest, and is it
> excitatory, at the developmental stage where network hyperexcitability is already measurable?**

🔴 **Two questions, not one, and conflating them is the standing error in this literature.**
**Depolarizing ≠ excitatory.** A GABA response can be depolarizing and still net-inhibitory
through shunting: the conductance short-circuits the membrane even while the current is outward.
Any design that measures `E_GABA` alone answers half the question and licenses the wrong
inference in either direction.

---

## 2. The design

### `MODEL`

Three arms, chosen so the result attaches to data the corpus already has:

1. **`Wwox^−/−` (Aqeilan allele)** — primary. The **same allele and same laboratory lineage** as
   the only continuous ECoG dataset (PMID 42422765), so a positive result attaches directly to a
   measured network phenotype rather than to a different animal.
2. **`Wwox^+/−`** — the haploinsufficiency arm. `CLAIM 032` asserts haploinsufficiency is not
   deleterious; **no electrophysiology exists in the het at any age.** This arm is cheap here
   because the animals are bred anyway as littermates.
3. **`Wwox^P47T/P47T`** — the chronic/adult arm, viable beyond a year (PMID 36828035), which the
   nulls are not. It is the only WWOX genotype in which an adult E_GABA is obtainable at all.

Littermate `Wwox^+/+` controls throughout. **Genotype blinded** at recording and at analysis.

### `AGE/STAGE`

The mouse chloride switch is a developmental trajectory, so a single age cannot answer a question
about *persistence*. Four windows, all littermate-matched:

| Window | Rationale |
|---|---|
| **P5–P7** | before the switch — both genotypes expected depolarizing; establishes the assay reproduces known biology |
| **P10–P12** | mid-switch — maximum expected genotype separation; also the age Cheng 2020 reports spontaneous seizures beginning (*"after postnatal day 12"*) |
| **P14–P16** | **the ECoG window.** SWDs are already measurable here (PMID 42422765). A persistent depolarizing state here is mechanistically load-bearing |
| **P18–P21** | end of null lifespan; upper bound of what the null permits |

**Adults (>6 wk):** `P47T/P47T` only.

🔴 **Age is a covariate, not a bin.** Record exact postnatal day per animal and model age
continuously; the switch is steep and ±1 day is not noise.

### `CELL_TYPE`

- **CA3 pyramidal neurons** — primary. The classic substrate for `E_GABA` developmental work, the
  region where `CLAIM 005` measures interneuron loss, and where the rat's structural lesion sits.
- **Layer 2/3 pyramidal neurons, dorsal cortex** — secondary, chosen because it is **under the
  ECoG recording electrode** in PMID 42422765. Same tissue, same output.

⚠️ Interneurons are **excluded** from the primary endpoint: their own `E_GABA` trajectory differs
and mixing them inflates variance without answering the question.

### `RECORDING_MODE` — gramicidin-perforated patch, cell-attached first

Per neuron, in this order, **without ever breaking in**:

1. **Cell-attached, loose seal** — spontaneous firing rate; then local agonist application →
   does firing **increase** (excitatory) or **decrease** (inhibitory)? *This is the excitability
   answer, and it is obtained before the membrane is ever perturbed.*
2. **Gramicidin-perforated patch, current clamp** — resting membrane potential `V_rest`.
3. **Gramicidin-perforated patch, voltage clamp** — `E_GABA` by agonist-evoked current across a
   voltage step/ramp series.
4. **Terminal break-in** — deliberately rupture at the end to confirm the perforated
   configuration held (see negative controls).

### `WHY_GRAMICIDIN` — the reason the whole design exists

Gramicidin forms channels permeable to **monovalent cations but not to Cl⁻**. It gives electrical
access to the cell while leaving the **native intracellular chloride concentration intact**.

🔴 **Conventional whole-cell patch dialyses the neuron with the pipette solution and therefore
sets `[Cl⁻]ᵢ` to whatever the experimenter put in the pipette.** In whole-cell mode `E_GABA` is
an artefact of the internal solution — the measurement destroys the quantity it purports to
measure. This is not a refinement; it is the difference between an answer and a number.

Perforated-patch `E_GABA` is also the reason this experiment has not been done by accident: it is
slow, has high attrition, and drifts. Those costs are in §`SAMPLE_STRUCTURE`, not wished away.

### `E_GABA_ENDPOINT`

- **Agonist: isoguvacine** (selective GABA_A agonist) by brief local pressure puff, or focal
  photolysis of caged GABA. **Isoguvacine over GABA** because GABA also engages GABA_B receptors
  and GAT transporters, and transporter current contaminates the reversal estimate.
- **Endpoint 1 — `E_GABA`:** reversal potential of the isoguvacine-evoked current, from the
  I–V relation across the step series.
- 🔴 **Endpoint 2 — `DF_GABA` = `E_GABA` − `V_rest`. This is the primary endpoint, not `E_GABA`.**
  A cell with `E_GABA` = −60 mV is depolarizing if it rests at −70 and hyperpolarizing if it rests
  at −55. `E_GABA` alone is uninterpretable without the rest potential **measured in the same
  cell**, which is why both must come from the same perforated recording.
- **Endpoint 3 — sign of the effect on firing** (from the cell-attached step): the excitatory /
  inhibitory answer, independent of both potentials.
- **Corrections, pre-specified:** liquid junction potential corrected and the value reported;
  series resistance monitored throughout and cells excluded on a pre-declared drift threshold;
  access re-checked at start and end.

### `INTRACELLULAR_CHLORIDE`

Derived, not assumed: `[Cl⁻]ᵢ` from `E_GABA` via the Nernst relation.

⚠️ **With the bicarbonate caveat stated in the claim, not buried.** GABA_A channels carry
appreciable HCO₃⁻ as well as Cl⁻, so `E_GABA` ≠ `E_Cl` exactly, and a Nernst inversion that
ignores it overestimates `[Cl⁻]ᵢ`. Either use the Goldman–Hodgkin–Katz form with a declared
HCO₃⁻ permeability ratio, or report `[Cl⁻]ᵢ` explicitly as an **upper bound**.

**Orthogonal confirmation (optional, if the colony permits crossing):** a genetically encoded
ratiometric Cl⁻ indicator (SuperClomeleon / ClopHensor class) for a population-level,
non-invasive `[Cl⁻]ᵢ` distribution. Independent physics, independent failure modes. **Not a
substitute** — indicator calibration in situ is its own problem.

### `KCC2/NKCC1_SECONDARY_READOUTS`

Secondary, and explicitly **correlates, not the endpoint**:

- **KCC2 total** and — the part usually skipped — **surface KCC2** by surface biotinylation or
  non-permeabilised immunolabelling. Total KCC2 can be normal while surface expression is not.
- **Phospho-KCC2 Ser940** (stabilising, ↑ surface) and **Thr1007** (inhibitory). Phosphorylation
  state changes transport without changing abundance.
- **NKCC1 total**, and the **KCC2:NKCC1 ratio**.
- Same animals, same hemisphere where possible, so the molecular and functional readouts are
  paired rather than merely from the same genotype.

🔴 **`PREMISE_TAG: DEFAULT_FROM_TEXTBOOK` on "KCC2 down ⇒ GABA depolarizing".** That inference is
the reason this experiment is owed. It may **not** be used to interpret the result; the direction
of evidence runs from `DF_GABA` to the molecules, not back.

### `POSITIVE_CONTROL`

1. 🔴 **The developmental shift itself, in wild-type littermates.** WT `E_GABA` must become more
   negative from P5–P7 to P18–P21. **If it does not, the rig is not measuring `E_GABA` and no
   genotype comparison may be reported.** This is the control that validates the assay against
   known biology rather than against itself.
2. **Acute bumetanide** (NKCC1 blocker, tool compound) on immature WT neurons must shift `E_GABA`
   negative. Confirms the pharmacology and that `[Cl⁻]ᵢ` is NKCC1-dependent in this preparation.
3. **Known-depolarizing benchmark tissue**, if a suitable model is available in-house, to anchor
   the absolute scale across rigs.

### `NEGATIVE_CONTROL`

1. 🔴 **The deliberate whole-cell arm.** A subset of cells recorded in conventional whole-cell
   mode with a **defined pipette [Cl⁻]** must yield `E_GABA` at the value Nernst predicts for that
   pipette. This does two things: it proves the rig reports reversal potentials correctly, **and**
   it demonstrates that the perforated recordings are *not* silently dialysing — because they give
   a different answer.
2. **Gabazine / picrotoxin** abolishes the evoked current → confirms GABA_A mediation.
3. **Spontaneous break-in detection:** perforated recordings monitored for the abrupt `E_GABA`
   shift toward the pipette value that signals membrane rupture. **Cells that break in are
   discarded, and the discard count is reported** — silent attrition here biases toward the
   pipette's answer, which is the one failure mode that would produce a clean, wrong result.
4. **Vehicle puff** (no agonist) → no current, excluding mechanical artefact from the puff itself.

### `SAMPLE_STRUCTURE`

🔴 **The unit of analysis is the animal, not the cell.** Cells within a slice are not independent;
slices within an animal are not independent. The corpus has already been bitten by exactly this
(PMID 42422765 panel 7C: a declared n = 5 with 3 and 2 points plotted, and a p-value pinned at its
rank-test floor).

- **Hierarchy:** cells → slices → animals → litters.
- **Analysis:** linear mixed-effects model with `animal` (nested in `litter`) as a random effect;
  fixed effects genotype × exact postnatal day. **Not** a t-test over pooled cells.
- **Report** the number of cells, slices, animals **and** litters for every group. All four.
- **Pre-register** exclusion criteria (access resistance, drift, break-in, `V_rest` bound) before
  recording.
- Both sexes, sex included as a covariate — the rat literature's 95%-audiogenic figure is
  female-only, a caveat that reached this repository only through a figure caption.

### `POWER_ANALYSIS_INPUTS` — what must be measured before an `n` can be stated

🔴 **No sample size is proposed here, because none is derivable from anything currently in the
corpus.** Proposing one would be inventing it. The pilot must supply:

| Input | Why it is needed |
|---|---|
| **SD of `DF_GABA` within genotype, per age window**, from WT pilot cells | the denominator of every effect size; unknown in this preparation |
| **Smallest physiologically meaningful ΔDF_GABA** | a consensus-set threshold — the difference that would change the mechanistic reading, declared *before* data |
| **Intraclass correlation** of `DF_GABA` between cells from the same animal | governs how much a cell adds versus an animal; with high ICC, extra cells buy almost nothing |
| **Yield: successful perforated recordings per animal** | perforated patch attrition is high and age-dependent |
| **Attrition: break-in / drift-exclusion rate per age** | P5–P7 and P18–P21 will not behave alike |

With those five, the animal-level `n` follows from a mixed-model power calculation. **Without
them, any stated `n` is decoration.**

---

## 3. Pre-specified interpretation

Declared **before** data, so the result cannot be read to taste.

### `WHAT_RESULT_SUPPORTS_DEPOLARIZING_GABA`

- `DF_GABA` **significantly more positive** in `Wwox^−/−` than in littermate WT at **P14–P16** —
  the window where SWDs are already measurable — with the WT developmental shift intact
  (positive control 1 satisfied); **and**
- cell-attached agonist application **increases** firing in `Wwox^−/−` while decreasing it in WT.

**Both**, or the finding is *depolarizing but not demonstrated excitatory* and must be reported
in exactly those words.

Supporting but not sufficient: `[Cl⁻]ᵢ` elevated (as an upper bound), KCC2 surface expression
reduced or Thr1007 phosphorylation increased, KCC2:NKCC1 ratio lowered.

### `WHAT_RESULT_REFUTES_IT`

- `DF_GABA` **indistinguishable** between genotypes at every window, with the WT shift intact and
  the study powered to the pre-declared ΔDF_GABA. **A null with the positive control satisfied and
  adequate power is a real negative** — and it would move `RL-GABA-002` to the dismissal ledger
  with a `REVIVAL_TRIGGER` of *"a different cell type, region or age window"*, not to silence.
- Or: `DF_GABA` more positive **but** agonist application **suppresses** firing → GABA is
  depolarizing **and inhibitory** (shunting). 🔴 **This outcome refutes the hyperexcitability
  mechanism while confirming the chloride phenotype**, and it is the result most likely to be
  mis-reported as a win. It is named here for that reason.

### What no outcome licenses

🔴 **No result of this experiment is a therapeutic finding.** A positive result would say that a
chloride-gradient mechanism is *live* in a mouse model at one age — not that any intervention is
indicated, safe, or transferable to a human genotype. NKCC1-blocker trials in human neonatal
seizure disorders have a discouraging record and a known ototoxicity signal; that history is a
reason this design keeps bumetanide strictly as a **bench tool**, and any move toward the
therapeutic space is a separate object with a BLOCK-1 gate in front of it.

---

## 3b. 🔴 HARDENING — the two mechanisms the model currently holds together

**The operator's question: *which result would distinguish two mechanisms the model today keeps
fused?*** The answer names the design's real failure mode.

### The two mechanisms

`meta_gaba_paradox`'s integrated model lists outcomes **A** (loss of mature inhibitory
interneurons → hyperexcitability) and **B** (markers present but immature/depolarizing function →
hyperexcitability) as alternatives with a *"convergent final output"*. **Convergent output is
exactly why they have never been separated.** They predict the same network phenotype and the
same `CLAIM 005` marker data.

| | **M1 — WEAK INHIBITION** | **M2 — DEPOLARIZING GABA** |
|---|---|---|
| Lesion | fewer/weaker GABAergic synapses; less GABA released; fewer receptors | chloride gradient not yet reversed; `E_GABA` above rest |
| `DF_GABA` | **unchanged** (normal chloride) | **shifted positive** |
| IPSC **amplitude** | **reduced** | may be normal or larger |
| IPSC **frequency** | reduced | unchanged |
| Effect on firing | reduced *suppression* | **increased firing** |
| Bumetanide | no effect on `DF_GABA` | shifts `DF_GABA` negative |
| Therapeutic direction | **raise** GABAergic tone | 🔴 raising GABAergic tone may **worsen** it |

🔴 **The two mechanisms recommend opposite interventions.** That is why fusing them is not a
tidiness problem.

### The measurement that separates them, and why the current design would miss it

**`DF_GABA` alone cannot distinguish M1 from M2 in the direction that matters.** A cell with
normal `DF_GABA` but half the inhibitory conductance is M1, and the perforated-patch reversal
measurement would call it normal. **`E_GABA` is a property of the gradient; `g_GABA` is a property
of the synapse. The design as written measures only the first.**

**Added endpoint 4 — inhibitory conductance and its kinetics**, on the *same* cells, after the
perforated recording is finished and the terminal break-in of §`RECORDING_MODE` step 4:

- **spontaneous IPSC amplitude, frequency and decay τ** (whole-cell, high-Cl⁻ internal, gabazine-
  reversible), and
- **miniature IPSCs in TTX** — mIPSC **amplitude** reports postsynaptic receptor number, mIPSC
  **frequency** reports synapse number or release probability. **That is the M1 decomposition**,
  and it is free because the cell is already patched.

| Result | Reading |
|---|---|
| `DF_GABA` shifted positive **and** mIPSC amplitude/frequency normal | **M2 alone** |
| `DF_GABA` normal **and** mIPSC amplitude and/or frequency reduced | **M1 alone** |
| both abnormal | **M1 + M2** — and the therapeutic order matters: correcting tone before the gradient would be harmful |
| neither | the phenotype is **not** GABAergic at this age; look at glutamatergic drive |

⚠️ The whole-cell arm is **terminal to that cell** and its `E_GABA` is meaningless. That is fine —
it is already the negative control of §`NEGATIVE_CONTROL`.1. **One cell yields both measurements
only in this order**: perforated first, ruptured second, never the reverse.

### The remaining hardening items

- **`CHLORIDE_PRESERVATION_RATIONALE`** — beyond gramicidin: use the **lowest workable pipette
  chloride** in the perforated internal so that an accidental rupture moves `E_GABA` *away* from
  the depolarizing answer, not toward it. 🔴 **The artefact must not point at the hypothesis.**
- **`RECORDING_TEMPERATURE`** — 🔴 **near-physiological (32–34 °C), declared, and never mixed with
  room-temperature recordings.** KCC2 transport is strongly temperature-dependent; a
  room-temperature preparation biases `E_GABA` **positive** and manufactures M2. If any arm must
  be run at room temperature, **all** are, and the value is reported.
- **`NETWORK_STATE`** — record whether spontaneous network activity is present; a depolarizing
  `E_GABA` measured in a silent slice and one measured under barrage are different quantities.
  Report holding current and input resistance per cell.
- **`CELL_IDENTITY`** — post-hoc confirmation, not position alone: biocytin fill plus a marker, or
  a reporter line. Excluded interneurons must be excluded **by evidence**.
- **`RESCUE_CONTROL_LOGIC`** — 🔴 the arm that converts association into cause. **AAV9-hSynI-WWOX
  at P0–P1, then measure `DF_GABA` and mIPSCs at P14–16.** If restoration normalises `DF_GABA`,
  the chloride phenotype is downstream of neuronal WWOX; if it normalises mIPSC amplitude instead,
  the lesion is synaptic. This is the same design that produced the corpus's only
  genotype→phenotype→rescue triad, pointed at the cellular question.
  ⚠️ **Dose must be reported as delivered genome copies per region**, not as injected vg — see
  [`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md).

---

## 4. What this design deliberately does not do

- **It does not measure epileptogenesis.** Four cross-sectional windows are a trajectory of a
  cellular property, not the acquisition of an epileptic state.
- **It does not resolve the human genotype.** All three arms are mouse; the reference genotype is
  a compound heterozygote and is not modelled here.
- **It does not test a drug.**
- **It does not settle the interneuron-loss axis** (`CLAIM 005`). Counting cells and measuring
  driving force are different questions, and a normal `DF_GABA` would not contradict reduced PV⁺
  counts.

---

## 5. Relationship to the other decisive experiment now on the queue

[`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md) §5 specifies
a five-arm continuous video-EEG study. **These two share animals.** The EEG study needs
`Wwox^−/−`, `Wwox^+/−` and littermate WT across P7–P21; this study needs the same genotypes across
P5–P21. Running them on one breeding cohort — EEG in vivo, then slices from the same animals —
would give **paired network and cellular measurements in the same individual**, which neither
study can produce alone and which is the only design that could attribute an SWD to a chloride
state rather than merely correlate them across cohorts.

**Proposed:** record both in `RL-GABA-002` as a single cohort with two readouts.

---

## Review required

None for queueing — this modifies nothing. It is offered as the specified test that
`RL-GABA-002` has been missing.
