# COMMIT CANDIDATE — E_GABA: the closure conditions, and the axis the truth table was missing

**Candidate ID:** CC-20260826-EGABA-CLOSURE-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** completes [`CC-20260826-EGABA-ANALYSIS-PLAN-01`](CC-20260826-EGABA-ANALYSIS-PLAN-01.md)
with per-mechanism null-closure conditions and one missing discriminator.
**Does not supersede it.**
**Change class:** MINOR — adds to `RL-GABA-002`. **No therapeutic content. Not medical advice.**
**Canonical targets:** `research_lines_current.md` `RL-GABA-002`
**Base head:** `ccddc28939234ad4fe29c417935a0dbe11de86d0` (branch `lettore`)
**Batch gate:** intentionally untouched

> 🔴 **No `n` is proposed anywhere in this document.** None is derivable — every variance input is
> unmeasured in this preparation. The pilot produces them; the main study is sized from them.

---

## 1. Six quantities, kept apart on purpose

The word *"inhibition"* has been carrying six things. They have different instruments, different
failure modes, and — the point of this section — **different null results.**

| # | Quantity | Instrument | What a change in it means | What it does **not** mean |
|---|---|---|---|---|
| Q1 | **`E_GABA`** (mV) | gramicidin-perforated patch | the chloride reversal potential | 🔴 **nothing on its own.** −60 mV is depolarizing at `V_rest` −70 and hyperpolarizing at −55 |
| Q2 | 🔴 **`DF_GABA` = `E_GABA` − `V_rest`** | same recording, same cell | **the driving force** — the sign and size of the GABA response | that the response is excitatory (see §4, shunting) |
| Q3 | **mIPSC amplitude** | whole-cell + TTX | quantal size — postsynaptic receptor number/conductance | synapse number; interneuron firing |
| Q4 | **mIPSC frequency** | whole-cell + TTX | **synapse number or release probability** | interneuron firing — TTX has silenced it |
| Q5 | ⚠️ **sIPSC frequency** | whole-cell, **no TTX** | **interneuron firing × synapse number**, combined | either factor alone |
| Q6 | **Network phenotype** | ECoG / video-EEG in vivo | circuit output: SWD rate, spike rate, behavioural events | any cellular parameter |

### 🔴 The discriminator the prior plan does not carry: Q5 vs Q4

`CLAIM 005` reports **PV⁺ interneuron counts reduced 44 %** in whole hippocampus, with NPY⁺ down in
DG. **A deficit in interneuron *number or firing* moves Q5 and leaves Q4 untouched** — TTX removes
exactly the term that carries it.

⇒ **Recording mIPSCs alone cannot detect the phenotype `CLAIM 005` already reports.** The prior
plan's M1 arm is a `g_GABA` arm; it is blind to an interneuron-count arm. **Both must be recorded,
in the same cell, before and after TTX**, or the design can return "M1 absent" while the
best-documented inhibitory abnormality in this corpus sits in the term it removed.

⚠️ `CLAIM 005`'s own boundary applies and is not weakened here: those are **marker-positive
abundances and area fractions**, not cell loss and not synapse counts. Q5 is where such a deficit
*would* appear; it is not evidence that it does.

---

## 2. The smallest truth table — four outcomes, two axes

**Axes: Q2 (`DF_GABA`) and Q3/Q4 (mIPSC).** Two axes, four cells. Nothing else enters.

| | mIPSC amp/freq **normal** | mIPSC amp/freq **reduced** |
|---|---|---|
| **`DF_GABA` normal** | 🔵 **NEITHER** — GABAergic transmission is not the lesion at this age and cell type | 🟡 **M1 alone** — weak inhibition |
| **`DF_GABA` shifted positive** | 🟢 **M2 alone** — depolarizing GABA | 🔴 **BOTH** — order of correction matters: raising GABAergic tone before fixing the gradient could **worsen** |

🔴 **Q5 and Q6 are deliberately NOT axes of this table.** Q5 is a *third* mechanism (interneuron
number/firing), and folding it in would make a 2×2 into a 2×2×2 with no reagent to separate the
extra cell. Q6 is the *phenotype the mechanisms explain* — putting an outcome on an axis of its own
mechanism table is how a design stops being able to fail. They are reported alongside, never inside.

**Orthogonality, stated so it can be checked:** M1 lives in `g_GABA` (conductance), M2 in the
chloride gradient. Measured on the **same neuron**, in a fixed order — cell-attached → perforated →
terminal rupture — because only that order yields both from one cell without dialysing the gradient
before it is measured.

---

## 3. 🔴 `NULL_CLOSURE` — what closes each mechanism, and what a null is not

**Three gate conditions. A null that fails any one of them means `NOT_TESTED`, never `NOT_DIFFERENT`.**

| Gate | Condition |
|---|---|
| **G1 — positive control** | WT `DF_GABA` must become more negative from P5–P7 to P18–P21. **If the developmental shift is absent, the rig is not measuring `DF_GABA`** and no genotype comparison may be reported at all |
| **G2 — powered** | to the effect size **declared before unblinding**; simulation-based over pilot variance components, **not** a closed-form two-sample formula, which assumes independent cells |
| **G3 — attrition reported** | exclusion counts per group, per window. Silent attrition biases toward the pipette's answer — the one failure mode that yields a clean wrong result |

### Per-mechanism closure

| Mechanism | 🔴 The null that closes it | Then | `REVIVAL_TRIGGER` |
|---|---|---|---|
| **M2 — depolarizing GABA** | `DF_GABA` in `Wwox^−/−` **not distinguishable** from littermate `+/+` at P14–P16, **with G1 satisfied in the same cohort**, **and** acute bumetanide producing **no** shift in either genotype | *"The chloride gradient is not measurably different at this age, in this cell type, in this region."* → `RL-GABA-002` M2 arm to the **dismissal ledger** | a different cell type, region or age window; or `P47T`, where later windows are reachable |
| **M1 — weak inhibition (`g_GABA`)** | mIPSC **amplitude and frequency and decay τ** all not distinguishable, **and** the whole-cell negative control returns the Nernst value for the defined pipette [Cl⁻], **and** gabazine abolishes the events | *"Quantal inhibitory transmission is not measurably reduced."* → M1 arm dismissed **for `g_GABA` only** | a synaptic-density or receptor-subunit measurement; evoked IPSC input–output |
| ⚠️ **M3 — interneuron number/firing (Q5)** | **sIPSC frequency** not distinguishable **while TTX-insensitive mIPSC frequency is also unchanged**, i.e. the ratio Q5:Q4 is preserved | *"Inhibitory drive from interneuron firing is not measurably reduced."* | any PV⁺/NPY⁺ **stereological** count, or optogenetic interneuron drive |
| 🔴 **All three null together** | every closure above satisfied **in the same animals** | 🔴 **GABAergic transmission is not the lesion at this age.** `RL-GABA-002` closes and the search moves to **glutamatergic drive, intrinsic excitability, and gap-junction coupling** — named now so the pivot is pre-registered rather than improvised | a positive result on any axis at any other age or region |

### 🔴 What no null in this design can close

**`Q6` — the network phenotype.** SWDs at P14–P21 are `DATO`
([`CC-20260826-FIVECLAIM-PACKAGE-01`](CC-20260826-FIVECLAIM-PACKAGE-01.md) `CLAIM 040`). A null on
Q1–Q5 does **not** make them go away; it relocates their cause. **No cellular null may be written
as "the network phenotype is unexplained, therefore absent."**

Likewise **`EPILEPTOGENESIS` is untouched by this design** and stays `UNRESOLVED`. Measuring it
needs the transition observed — a latent period, a documented conversion, or a manipulation that
shifts it. This experiment observes a state, not a transition.

---

## 4. ⚠️ The outcome most likely to be misreported, restated because it is the one that matters

**`DF_GABA` shifted positive AND agonist application *suppresses* firing** → GABA is
**depolarizing and inhibitory** (shunting inhibition).

That result **confirms M2 and refutes the hyperexcitability inference drawn from M2**. It is not a
partial win and must not be written as one. It is named here, before data, so that it cannot be.

⚠️ Its mirror: `DF_GABA` normal but the **network** phenotype present. That is not a failed
experiment — it is Q6 surviving a Q2 null, which is exactly the case §3's last row is for.

---

## 5. Two measurement hazards that manufacture a result

| Hazard | Direction of the artefact | Control |
|---|---|---|
| **Temperature** | KCC2 transport is strongly temperature-dependent; a room-temperature preparation biases `E_GABA` **positive** — it **manufactures M2** | 32–34 °C, declared, **never mixed across arms** |
| **Silent whole-cell dialysis** during a "perforated" recording | dialyses the gradient toward the pipette solution — **manufactures whichever answer the pipette holds** | the deliberate whole-cell arm with defined [Cl⁻] must return the Nernst value, and the perforated recordings must give a **different** one. If they agree, the perforated seal broke |

🔴 **The unit error this design exists to avoid has already been paid for twice in this corpus:**
PMID 42422765 panel 7C declares `n = 5` and plots 3 and 2 points with a p-value pinned at the
rank-test floor; and PMID 36828035 Figs 3–5 run unpaired t-tests over **subfields** from `n = 3`
mice. **Report cells, slices, animals AND litters for every group. All four.**

---

## 6. What this candidate refuses to do

- **Does not invent an `n`**, an effect size, or a variance.
- **Does not fold Q5 or Q6 into the truth table.**
- **Does not claim `E_GABA` has ever been measured in a WWOX model.** Zero measurements exist in
  the corpus; that is the reason the line is open.
- **Does not change `RL-GABA-002`'s status**, which is `high-interest / unresolved` and stays there
  until data exist. This candidate replaces its `Next action` — *"look for WWOX-specific data on
  the chloride gradient"* — with a design, and nothing else.
- **Is not medical advice** and proposes no treatment.
