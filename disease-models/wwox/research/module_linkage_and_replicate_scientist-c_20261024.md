# Module batch 2026-10-24 — Scientist C: the three LINKAGE_GAP identifiers, and the three REPLICATE endpoints

> Research layer, non-canonical. Read-only toward the four scientific current files and toward
> `mechanism_intervention_map.md`: this record **proposes** identifiers and states endpoints; it
> edits nothing. Every non-WWOX source below is labelled **NOT WWOX EVIDENCE**. No dose, route,
> administration or suitability statement is made or implied anywhere in this file.
> **Not medical advice.**

Task `MODULE-C8-20261024`, ACTOR_ID `scientist-c`, branch `task/module-c8-20261024`.
Input: [`repurposing_batch_selection_20261024_module.md`](repurposing_batch_selection_20261024_module.md)
(rendered from the join, never typed). Prior work this record builds on and does not repeat:
[`module_batch_selection_scientist-c_20261023.md`](module_batch_selection_scientist-c_20261023.md)
(rows Q-R-04..09 and the first pass on the three REPLICATE rows) and Scientist D's held identifier
diff [`drug_repurposing/map_identifier_edits_20261023.diff`](drug_repurposing/map_identifier_edits_20261023.diff).

No new literature search was run for part 2, by instruction: the question there is no longer *where
is the replication* but *what is the endpoint and what would settle it*.

---

## 1 · The three LINKAGE_GAP rows — the identifier each record needs

The join's requirement is one identifier **in the record** that resolves to a PMID. All four PMIDs
named below were put through `pubmed_identity_check.py` on 2026-10-24: every one returned
`MATCH` (stored DOI resolves to the article PubMed describes, title overlap 1.0).

| Row | Record (map line) | Identifier to carry | Resolves to | Identity check | Status of the held proposal |
|---|---|---|---|---|---|
| `Q-R-07` | R-07 Bumetanide (:553) | `DL-MECH-035` | PMID 34268881 — Steinberg 2021, *EMBO Mol Med*, WWOX-KO brain organoids | MATCH | Scientist D's proposal **confirmed** |
| `Q-N-06` | N-06 Lactate / metabolic blood biomarkers (:689) | `DL-BIO-008` | PMID 30362252 (load-bearing), with PMID 25012504 and PMID 24456803 in the same record | MATCH (all three checked: 30362252, and the two named in the record) | Scientist D's proposal **confirmed** |
| `Q-N-08` | N-08 Dichloroacetate (:708) | `PAPER 557`, `PAPER 562` (and `DL-MECH-020` for the metabolic rationale) | PMID 23611579; PMID 36432491 | MATCH (both) | **created** — the diff proposed nothing for N-08 |

### R-07 — the identifier exists, and it does not reduce the uncertainty

`DL-MECH-035` ("GABA depolarizzante negli organoidi WWOX-KO") names **PMID 34268881** as its
`Fonte`. That is exactly the source R-07's own prose describes without citing: the depolarizing-GABA
premise is the authors' `IPOTESI` read off the marker pattern (GAD67 up, VGLUT1 unchanged,
GABRB2/GABRB3 down) in WWOX-KO organoids. The linkage gap closes on a WWOX primary.

What the identifier does **not** do is move the row. 34268881 measures the marker pattern, not the
quantity R-07 depends on: it reports no `E_GABA`, no intracellular chloride, no NKCC1/KCC2
quantification and no GABA pharmacology. `EVIDENCE_LEVEL` stays **T6** and the class stays
`INSUFFICIENT_EVIDENCE`. The row becomes a candidate whose single cited paper demonstrably does not
contain its load-bearing premise — which is a more useful state than `LINKAGE_GAP`, because it is
now checkable.

### N-06 — the identifier exists, and the record is the contradiction

`DL-BIO-008` ("Contraddizione sul lattato") names three PMIDs in its `Fonti` line, and N-06's prose
is a compression of that record: **PMID 30362252** (human WWOX case, MR spectroscopy, cerebral
lactate "extremely low", the HSPG2 confounder N-06 names), **PMID 25012504** (Wwox-KO mouse, serum
lactate raised) and **PMID 24456803** (human WWOX null/null, metabolic screen entirely normal). The
load-bearing citation for the sentence the row rests on — the MRS outlier pointing opposite to the
Warburg prediction — is 30362252.

One thing to carry forward with the identifier: N-06's prose says "**four** independent human
sources show normal metabolism" and `DL-BIO-008` names **one** complete human metabolic screen. The
other three are not identified in either the record or the lead. That is an unsourced count inside a
negative, not a linkage gap, and it is flagged here rather than repaired.

### N-08 — an identifier had to be created, and what it resolves to is not WWOX evidence

The diff proposed no `Source ids:` line for N-08; nothing in the record pointed anywhere. Two papers
were read for this exact row in the module batch of 2026-10-23 by `scientist-b` (task
`MODULE-B-20261023`), registered by the integrator as class-level substitutes, with receipts and
strict-PASS manifests:

| PAPER | PMID | What it is | Label |
|---|---|---|---|
| `PAPER 557` | 23611579 | Abdelmalak 2013, open-label long-term follow-up in congenital lactic acidosis; receipt `FTR-20261023-23611579-01`, 8 locators | 🔴 **NOT WWOX EVIDENCE** — T4, no WWOX allele, zero WWOX occurrences in the read artefacts |
| `PAPER 562` | 36432491 | Lee 2022, wild-type rat seizure model; receipt `FTR-20261023-36432491-01`, 8 locators | 🔴 **NOT WWOX EVIDENCE** — T4, no WWOX-deficient system |

So the honest identifier for N-08 is **`PAPER 557`, `PAPER 562`** for the class-level toxicity and
seizure-injury statements, plus **`DL-MECH-020`** (the WWOX Warburg/HIF1α rationale, which is the
only WWOX-side anchor the row has) for the mechanism. And the uncertainty is recorded, not
dissolved: **no paper, in this repository or named by this record, measures dichloroacetate in any
WWOX system.** The row's intervention arm is non-WWOX throughout. Linking it to two non-WWOX papers
closes a *linkage* gap and leaves the *evidence* gap exactly as wide as it was — which is the point
of labelling them.

Carried forward from `scientist-b`'s reading, because it travels with the identifier: the map's
paediatric-neurotoxicity wording is **stronger than 23611579 supports** (what the paper carries is
asymptomatic nerve-conduction worsening in a minority of a small paediatric series, with the drug
paused or reduced; the symptomatic-neuropathy statement sits in an older-adult trial that is not
this paper). And the map's "dominated by R-05" is **not tested in any paper read**. Both are
wording repairs for the record owner, not identifier questions, and no edit is proposed here.

---

## 2 · The three REPLICATE rows — the endpoint, the verdict, and the experiment

All three were screened `BIND FIRST: UNVERIFIED`. The common finding, now stated plainly: in none of
the three is the replication question well-posed as the handoff asks it, and in two of the three the
`ONE_PAPER` state is a binding artefact. Searching further for a replication is not the next act.

| Row | The exact endpoint, with its unit | Independent primary evidence? |
|---|---|---|
| `Q-N-16` | normalized **spontaneous burst frequency** in acute neocortical slices, LFP field recording, dimensionless ratio to the slice's own pre-drug baseline (baseline = 1.0), under a selective pannexin-1 blocker and at washout; `Wwox` S-KO, P13–P17. Secondary: proportion of bursts whose maximal phase-amplitude-coupling range shifts delta-gamma → delta-HFO | **No.** No WWOX system other than PMID 34634460 has ever received a pannexin-1 blocker |
| `Q-R-01` | **survival to a fixed census age**, and **spike-wave discharge rate** (events per hour, continuous ECoG), after vector delivery in a Wwox-deficient mouse; with myelin readouts secondary | **No.** And the question is ill-posed against the bound paper |
| `Q-R-03` | **nuclear β-catenin abundance** in WWOX-KO cerebral organoids as a **fold-ratio to the isogenic parental line** (the record's ≈1.7×), nuclear-fraction western or quantified nuclear IF; secondary AXIN2/LEF1 transcripts and cortical-layering rescue | **No** for a developing neural system. Molecular-direction corroboration exists only in cancer cells |

### Q-N-16 — pannexin-1 blockade

The handoff says the record "declares no endpoint (no bold span in its decisive test)". It does
declare one, in prose: the quantity is the normalized burst frequency above, and the value behind the
`DEPRIORITIZE` is ≈2.55 during the blocker arm and ≈2.6 at washout against a baseline of 1.0,
carrying **no significance marker and no reported test** (panel attestation, manifest
`PMID34634460.json` entry 3, receipt `FTR-20260810-34634460-02`).

**Independent primary evidence: none, and this is a bounded statement.** The only other pannexin
paper read for this row, PMID 33053775 (🔴 **NOT WWOX EVIDENCE**), is from the **same laboratory** as
the bound paper — shared authors, same institution — so it is a second model, flagged and not
counted; and its endpoint is the *incidence of convulsant-triggered seizure-like events per slice*,
not spontaneous burst frequency, so it neither replicates nor contradicts. PMID 29848662 (🔴 **NOT
WWOX EVIDENCE**) is a different laboratory but non-WWOX tissue with a different endpoint; abstract
only, parked.

**The discriminating experiment.** What the published arm cannot do is separate a drug effect from a
time-dependent run-up of burst frequency over the recording, because it had **no vehicle
time-control** — and an upward drift would produce the same two numbers at "during" and "washout".

- **Measurement:** burst frequency from LFP field recording, reported both in bursts per minute and
  normalized to the in-slice pre-drug baseline, with the per-burst PAC-range classification as the
  secondary readout. Unit of analysis: the slice. A declared statistical test, and n fixed by power
  on the variance the published arm actually shows.
- **Arms:** (1) `Wwox`-null slice + selective pannexin-1 blocker; (2) **`Wwox`-null slice + vehicle,
  recorded for the same duration** — the control arm the design needs; (3) littermate-control slice +
  blocker; (4) `Wwox`-null slice + a structurally unrelated pannexin-1 blocker, or pannexin-1 genetic
  deletion on the `Wwox` background, to separate on-target from the dye-class compound's off-target
  effects. Developmental stage crossed as a factor: an **earlier** window against P13–P17, since the
  earlier stage is what the record's own revival trigger names.
- **What each outcome means:** blocker below vehicle at the matched time, at the earlier stage →
  the revival trigger is met and the node returns as live. Vehicle drifting upward to the published
  degree → the ≈2.55/≈2.6 was run-up, the arm was neither a no-effect arm nor an adverse one, and the
  only WWOX pannexin datum is withdrawn rather than reinterpreted. Blocker above a flat vehicle →
  pannexin-1 blockade is adverse in this network, and `DEPRIORITIZE` stops resting on an untested
  point estimate and becomes a measured negative. Blocker indistinguishable from a flat vehicle →
  the paper's own prose ("minimal effect") is established, which its numbers currently do not do.

Staged: `lead_staging/scientist-c/lead_n16_experiment.json`.

### Q-R-01 — AAV9-hSynI-WWOX

**The replication question is ill-posed against the bound paper.** PMID 42128308 is a **Review** by
PubMed article type; the map cites it only at class level in `KNOWN_MAJOR_SAFETY_CONSTRAINTS`
(🔴 **NOT WWOX EVIDENCE** for the WWOX ganglion question — no such assessment exists in either WWOX
paper). It measures nothing, so "an independent measurement of the same endpoint" has no referent.
The measurements are **PMID 34747138** and **PMID 42422765**, manifests present, **one laboratory**.
The row's true state is therefore *two papers, one laboratory* — not `ONE_PAPER` — and a
second-laboratory vector study of these endpoints was not found on 2026-10-23 and is not searched for
again here.

**The discriminating experiment.** The open question is not whether gene addition works; it is
whether the untested post-onset exterior is a **boundary** or an **artefact of the null model's
lethality**. The source's own authors attribute the untested exterior to model-specific constraints
rather than a limit of responsiveness, and `NOT_MEASURED ≠ SMALLER` is already written into the row.

- **Measurement:** survival to a fixed census age; spike-wave discharge rate (events/hour) from
  continuous ECoG; myelin as area fraction of a myelin marker with a tract-thickness measure.
- **Arms, in a long-surviving hypomorphic allele rather than the null:** (1) hypomorph + vector
  **after documented seizure onset**; (2) hypomorph + vector in the published early window — the
  **positive control** without which a null result in a new model cannot be told from a model that
  does not respond at all; (3) hypomorph + vehicle by the source's own route and volume, unchanged —
  the control arm the design needs, since the procedure itself is not inert in neonates; (4)
  littermate wild-type + vector, because over-dosage of this gene is a stated harm and "neither too
  little nor too much WWOX" has to be an arm, not a caveat. One intermediate arm specified **only as
  a fraction of the source's own high arm** — the absolute figures are uncertain by a factor of two
  while the ratio is invariant, so no absolute value is reproduced here.
- **What each outcome means:** post-onset matching the early arm → the window stops being the row's
  main translational risk, and the `SPLIT` class widens for the three ready endpoints. Post-onset
  improving discharge rate but not myelin → the `SPLIT` is confirmed and refined endpoint by
  endpoint, which is what the class was created to express. No benefit at either time in the
  hypomorph, with the published effect reproduced in the null → the hypomorph is not a competent test
  system, and nothing is learned about the window. Benefit only in the early arm → the window is a
  real boundary and the ready class stays confined to it. Intermediate arm rescuing survival → the
  threshold sits below the high arm; not rescuing → the threshold is in the upper bracket and "a
  lower, safer dose" stays refused by the data.

Staged: `lead_staging/scientist-c/lead_r01_experiment.json`.

### Q-R-03 — Wnt / tankyrase inhibition

**The bound paper never measures the endpoint.** PMID 38203337 is a psoriasis-keratinocyte paper on
NF-κB, calcium and PKC; the join reached it through `CLAIM 028`, which cites it for the
context-dependence of WWOX output, not for β-catenin. So `ONE_PAPER` here is not weak — it is
meaningless. The endpoint lives in **PMID 34268881**, which reports the fold-ratio on **2 wild-type
and 4 knockout organoids, run twice**. **PMID 42397075** (same laboratory) adds a TCF4 western cited
to a supplement that could not be obtained — recorded `UNVERIFIED`, no value written — and is in any
case a different readout.

**Independent primary evidence: none in a developing neural system.** Outside-laboratory measurements
of the molecular direction exist only in cancer cells: PMID 32368285 (WWOX silencing raises nuclear
Dvl), PMID 19465938 (the original Dvl mechanism), PMID 42790938 (abstract only) — all 🔴 **NOT WWOX
NEURAL EVIDENCE**, and by the module's own rule a cancer-cell measurement is a second system for a
**molecular** endpoint and not for a network or developmental one. The molecular direction has
cross-system support; the endpoint this row rests on has one measurement in one laboratory at n = 2
versus 4.

**The discriminating experiment** — the record's own two-armed design, plus the control arm it lacks.

- **Measurement:** nuclear β-catenin as a fold-ratio to the isogenic parental line, by
  nuclear/cytoplasmic fractionation western **and** a quantified nuclear-IF replicate (fractionation
  purity is the usual failure of this measurement); AXIN2 and LEF1 by qPCR; cortical layering as the
  radial distribution of layer markers — the functional readout the molecular one is a proxy for.
- **Arms:** (1) WWOX-KO organoids + vehicle; (2) **isogenic parental + vehicle**; (3) WWOX-KO +
  tankyrase inhibitor (Wnt down); (4) WWOX-KO + a GSK3β-inhibitor Wnt agonist (Wnt up) — the
  two-direction pair that fixes the sign in the right context; (5) WWOX-KO + WWOX re-expression — the
  WWOX-dependence control; (6) **isogenic parental + the same tankyrase inhibitor** — the arm the
  design has never had, and without it a layering improvement in arm 3 cannot be told from layering
  being Wnt-dose sensitive in **any** organoid.
- **What each outcome means:** layering improves in arm 3, not in arm 6, and arm 5 reproduces it →
  the excess is WWOX-downstream and directionally correctable, and R-03 moves from
  `TRANSFER_HYPOTHESIS` to a direction measured in the right context. Layering changes in arm 3 **and**
  arm 6 → the effect is Wnt-dose sensitivity of organoid layering, not correction of a WWOX-specific
  excess, and the row closes. Arm 4 (Wnt up) improving layering → the sign in developing neurons is
  the opposite of the oncological intuition and the axis inverts. No nuclear β-catenin difference
  between arms 1 and 2 at adequate n → the **premise** fails, not the modality, and the row's
  `WWOX_DIRECT_EVIDENCE` line is what needs the repair.

Staged: `lead_staging/scientist-c/lead_r03_experiment.json`.

---

## 3 · Outputs, and what was deliberately not done

- Three identifier proposals (§1), to be applied by the record owner. **No edit to
  `mechanism_intervention_map.md` is made here**, and none to the four scientific current files.
- Three staged leads, all `OK` under `discovery_lead.py check` with `falsifier` and `transfer_limit`
  present; staged under `lead_staging/scientist-c/`, **never appended** — numbering and append happen
  on `main` by `append --staged --apply`.
- No receipt was produced: no new full text was read in this task. Nothing was staged under
  `research/receipt_staging/scientist-c/` and nothing was recorded.
- No new literature search for part 2, by instruction. Where independent evidence does not exist,
  this record says so and writes the experiment instead of extending the search.
