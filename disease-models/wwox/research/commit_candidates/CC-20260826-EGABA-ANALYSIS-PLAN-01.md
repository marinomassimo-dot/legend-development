# COMMIT CANDIDATE — E_GABA: analysis plan, and the cohort map shared with video-EEG

**Candidate ID:** CC-20260826-EGABA-ANALYSIS-PLAN-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** advances [`CC-20260826-EGABA-EXPERIMENT-01`](CC-20260826-EGABA-EXPERIMENT-01.md) from
design to a pre-specified analysis plan, and maps it against the P7–P21 video-EEG design
**Change class:** MINOR — adds to `RL-GABA-002`; **no therapeutic content, no medical advice**
**Batch gate:** intentionally untouched

---

## 1. Primary endpoint, and why it is a difference of differences

**`PRIMARY_ENDPOINT`:** **`DF_GABA` = `E_GABA` − `V_rest`**, in millivolts, measured per neuron by
gramicidin-perforated patch, at **P14–P16**.

**Pre-specified contrast:** `Wwox^−/−` versus littermate `Wwox^+/+`, **at P14–P16 only**. Every
other window and genotype is secondary and is reported with that stated.

🔴 **Not `E_GABA`.** A cell resting at −70 mV with `E_GABA` = −60 is depolarizing; one resting at
−55 with the same `E_GABA` is hyperpolarizing. `E_GABA` alone is uninterpretable, and both terms
must come from the **same** perforated recording or the difference is between two cells.

---

## 2. 🔴 The critical discrimination, as two distinct empirical signatures

The operator's requirement: reduced inhibitory amplitude and depolarizing GABA **must not** be
able to produce the same data.

| Observable | **M1 — reduced inhibitory drive** | **M2 — depolarizing GABA** |
|---|---|---|
| `DF_GABA` (perforated) | **unchanged** | **more positive** |
| `V_rest` | unchanged | unchanged |
| **mIPSC amplitude** (whole-cell, TTX) | **reduced** | unchanged |
| **mIPSC frequency** (TTX) | reduced *if* synapse number falls | unchanged |
| **mIPSC decay τ** | may lengthen (subunit shift) | unchanged |
| Agonist effect on firing (cell-attached) | **less suppression** | **increase** |
| Acute bumetanide on `DF_GABA` | no shift | **shifts negative** |
| KCC2 surface : NKCC1 | may be unchanged | typically lowered |

**They are orthogonal**: M1 lives in `g_GABA`, M2 in the chloride gradient. The design measures
both **on the same neuron**, in a fixed order — cell-attached → perforated → terminal rupture —
because only that order yields both from one cell.

**Four-cell truth table, pre-specified:**

| `DF_GABA` | mIPSC amp/freq | Conclusion |
|---|---|---|
| shifted + | normal | **M2 alone** |
| normal | reduced | **M1 alone** |
| shifted + | reduced | **M1 + M2** — order of correction matters; raising tone before fixing the gradient could worsen |
| normal | normal | **Not GABAergic at this age.** Look at glutamatergic drive |

---

## 3. Units, and the nesting that decides the analysis

| Level | What it is | Role |
|---|---|---|
| **Cell-level unit** | one neuron with a complete cell-attached + perforated record | the **measurement** unit |
| **Animal-level unit** | one mouse | 🔴 **the INFERENTIAL unit** |
| Slice | one acute slice | nuisance level, nested in animal |
| Litter | one litter | nuisance level, nested above animal; carries genotype and dam effects |

**Model:**

```
DF_GABA ~ genotype * age_days + sex + (1 | litter/animal/slice)
```

REML, Satterthwaite denominator df; `age_days` **continuous**, not binned — the chloride switch is
steep and ±1 day is not noise.

🔴 **The unit error this design exists to avoid has already been paid for in this corpus.**
PMID 42422765 panel 7C declares `n = 5` and plots 3 and 2 points, printing a p-value pinned at its
rank-test floor. **Report cells, slices, animals AND litters for every group. All four.**

---

## 4. Windows and contrasts

| Window | Purpose | Primary? |
|---|---|---|
| P5–P7 | before the switch — both genotypes expected depolarizing; **assay validation** | no |
| P10–P12 | mid-switch; also Cheng 2020's spontaneous-seizure onset | secondary |
| **P14–P16** | **the ECoG window — SWDs already measurable** | ✅ **PRIMARY** |
| P18–P21 | end of null lifespan | secondary |
| adult >6 wk | `P47T/P47T` only — the sole WWOX genotype where adult recording is possible | exploratory |

**Genotype contrasts:** `Wwox^−/−` vs `Wwox^+/+` (primary) · `Wwox^+/−` vs `Wwox^+/+`
(**no WWOX electrophysiology exists at any age** — see `CLAIM 032`) · `Wwox^−/−` + AAV9-hSynI-WWOX
vs `Wwox^−/−` (rescue) · `P47T/P47T` vs `P47T/+` (adult).

---

## 5. Effect-size and power inputs — still not derivable, and now itemised

🔴 **No `n` is proposed.** None is derivable, because **every input below is unmeasured in this
preparation.** The pilot must produce them before the main study is sized.

| Input | Why it is needed | Source |
|---|---|---|
| **SD of `DF_GABA`** within genotype, per window | denominator of every effect size | WT pilot, ≥6 animals |
| **Smallest meaningful ΔDF_GABA** | must be **declared before data** | consensus; a shift that changes the sign of the response is the natural floor |
| **ICC** between cells of one animal | governs whether extra cells buy anything; with high ICC they buy almost nothing | pilot |
| Cells per animal (yield) | perforated-patch attrition is high and age-dependent | pilot |
| Break-in / drift exclusion rate per window | P5–P7 and P18–P21 will not behave alike | pilot |
| **SD of mIPSC amplitude** | the M1 arm needs its own power | pilot |

**Power model:** simulation-based for the mixed model (parametric bootstrap over fitted pilot
variance components), **not** a closed-form two-sample formula — a closed form assumes independent
cells, which is the error being avoided.

---

## 6. Blinding and randomisation

- **Genotype blinded** at recording and at analysis; codes broken only after exclusions are final.
- **Slice order randomised** within animal; recording order counterbalanced across genotypes
  within a session, so rig drift cannot align with genotype.
- **Exclusion criteria pre-registered**: access resistance bound, drift threshold, `V_rest` bound,
  spontaneous break-in. **The discard count is reported per group** — silent attrition biases
  toward the pipette's answer, the one failure mode that yields a clean wrong result.
- Both sexes; **sex as a fixed covariate**. The rat literature's 95 % audiogenic figure is
  female-only and reached this repository through a figure caption.

---

## 7. Controls

**`POSITIVE_CONTROL`** — 🔴 **the developmental shift in wild type.** WT `DF_GABA` must become
more negative from P5–P7 to P18–P21. **If it does not, the rig is not measuring `DF_GABA` and no
genotype comparison may be reported.** Secondary: acute bumetanide shifts `E_GABA` negative in
immature WT.

**`NEGATIVE_CONTROL`** — the deliberate whole-cell arm with **defined pipette [Cl⁻]**, which must
return the Nernst value for that solution. It proves the rig reports reversal potentials **and**
that the perforated recordings are not silently dialysing, because they give a different answer.
Plus gabazine abolition, vehicle puff, and spontaneous-break-in detection.

**Temperature** 32–34 °C, declared, never mixed across arms — KCC2 transport is strongly
temperature-dependent and a room-temperature preparation biases `E_GABA` **positive**, i.e.
**manufactures M2**.

---

## 8. `NULL_INTERPRETATION` — pre-specified

**A null is a result, not a failure, but only under three conditions:**

1. positive control 1 satisfied (WT shift present);
2. the study powered to the pre-declared ΔDF_GABA;
3. exclusion counts reported.

With all three: *"the chloride gradient is not measurably different at this age in this cell type"*
→ `RL-GABA-002` moves to the **dismissal ledger** with `REVIVAL_TRIGGER`: *a different cell type,
region or age window; or a model with longer survival (`P47T`) where later windows are reachable.*

🔴 **Without those three, a null means "not tested", not "not different"** — the same distinction
already forced on panel 7C of PMID 42422765.

⚠️ **The outcome most likely to be misreported**: `DF_GABA` shifted positive **and** agonist
application **suppresses** firing → GABA is depolarizing **and inhibitory** (shunting). That
**refutes the hyperexcitability mechanism while confirming the chloride phenotype**, and it is
named here so it cannot be written up as a win.

---

## 9. `VIDEO_EEG_EGABA_RESOURCE_MAP` — one cohort, two readouts, in the only order that works

### What can share a cohort

| Measurement | Destructive? | Shareable |
|---|---|---|
| Continuous video-EEG, P7–P21 | **no** — chronic implant, animal survives | ✅ |
| Terminal slice electrophysiology | 🔴 **yes** | ✅ **only as the terminal step** |
| KCC2/NKCC1 biochemistry (contralateral hemisphere) | terminal | ✅ same animal |
| Behavioural seizure scoring | no | ✅ concurrent with EEG |

### What cannot

- 🔴 **Slices cannot precede EEG.** The animal is dead.
- 🔴 **Slices cannot be taken from an EEG animal at the age EEG is still running** — the recording
  ends when the animal does. A P14 `DF_GABA` measurement in an animal you also want P21 EEG from
  is impossible. **This is the binding constraint and it forces two sub-cohorts, not one.**
- ⚠️ **The implant is a craniotomy.** Slices from an implanted hemisphere carry surgical
  inflammation. **Take slices from the contralateral hemisphere**, and record which.

### The design that preserves causal interpretability

```
Litter → genotype at P0 → randomise within litter

  ARM A  (n animals)   EEG P7 → P21 continuous, then terminal slices at P21
                       → within-animal pairing of NETWORK output and CELLULAR state
                       → answers: does SWD rate covary with DF_GABA in the SAME animal?

  ARM B  (n animals)   no implant; terminal slices at P5-7 / P10-12 / P14-16
                       → the DEVELOPMENTAL TRAJECTORY, uncontaminated by surgery
                       → answers: when does DF_GABA diverge, if it does?

  ARM C  (n animals)   AAV9-hSynI-WWOX at P0-P1; EEG P7→P21; terminal slices at P21
                       → answers: does restoring WWOX normalise BOTH readouts?
                       → dose reported as DELIVERED regional protein relative to WT,
                         never as injected vg  (CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01)
```

**Temporal sequence and what it buys:**

1. **Arm B first.** It is cheapest, needs no surgery, and answers whether there is a phenotype at
   all. **If Arm B is null with its positive control satisfied, Arms A and C are not run** — that
   decision gate is the main resource saving in this map.
2. **Arm A second**, only if B is positive. Its value is entirely in the **within-animal pairing**:
   a correlation across cohorts would be confounded by litter and rig; within one animal it is not.
3. **Arm C last**, and only if A shows covariation. Rescue is expensive and uninterpretable before
   the phenotype is characterised.

🔴 **Do not fuse Arms A and B.** The trajectory needs unimplanted animals; the pairing needs
implanted ones. Forcing one cohort would give a trajectory contaminated by surgery **and** a
pairing at only one age — losing both questions to save one cohort.

**Shared with the video-EEG design already on the queue**
([`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md) §5): Arm A
**is** that study, with a terminal slice step appended. The `Wwox^+/−` arm both designs need is the
same animals. **Adopt the Hussain 2023 montage** — bilateral frontal + parietal, four channels —
because a single channel cannot resolve the bilateral synchrony that distinguishes a generalized
discharge from a focal artefact.

---

## 10. What this plan still does not do

- **Does not test a drug.** Bumetanide is a bench tool throughout.
- **Does not measure epileptogenesis.** Four cross-sectional windows are a trajectory of a cellular
  property, not the acquisition of an epileptic state. Arm A's *age of first electrographic event*
  is the closest available proxy and is **not** the same thing.
- **Does not resolve the human genotype.** All arms are mouse.
- **Is not medical advice.**

---

## Review required

None for queueing — this modifies nothing.
