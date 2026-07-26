# Proteostasis rationale for WWOX missense alleles — and the repair that narrowed it

> **Status: HYPOTHESIS, conditional / not design-ready.** This document is the written rationale behind three artifacts that ship in this repository — `data/WWOX_proteostasis_hypothesis.png`, `data/WWOX_residue_rescuability.csv`, `data/WWOX_pathogenic_missense_classified.csv` — and behind the "chaperone lever" arm of [`variant_triage_rescuability.md`](variant_triage_rescuability.md).
>
> It is included **together with the correction that later narrowed it** (2026-07-14, a MAJOR baseline reversal). Publishing the rationale without the repair would misrepresent the current state of the model. **Not medical advice.**

---

## 1. The idea in one sentence

A destabilizing WWOX missense allele may not produce a *dead* protein: it may produce a protein that **misfolds and is cleared**, while its catalytic machinery stays intact. If that is true, a therapeutic class absent from the standard WWOX dossier becomes rational — **recover the protein** (pharmacological chaperones, kinetic stabilizers, proteostasis regulators) instead of replacing it. It is allele-specific and orthogonal both to downstream levers and to gene addition.

Worked example throughout: **p.Gln230Pro (Q230P)**, a buried SDR-core residue.

---

## 2. What the structural analysis established — and what was later retracted

The rationale rested on four steps. **One of them still stands. Three were retracted** by the 2026-07-14 canonical repair (§4). They are shown here with their status inline, because presenting them first and correcting them later is exactly the failure mode this repository is built to prevent.

### ✅ Step 1 — Q230 is not directly a catalytic residue *(stands, with its scope stated)*

The SDR active site was located empirically on the **wild-type** AlphaFold model: the **Ser281 / Tyr293 / Lys297** triad (canonical YxxxK motif plus the catalytic serine). Measured on that same wild-type geometry:

- Q230 lies **6.8–9.7 Å** (closest atom) from the catalytic residues — it is **not directly a catalytic residue**;
- Q230 is **deeply buried** (27 Cα neighbours within 10 Å; 88th percentile of core packing) — a *core-packing* position, not a surface/interface one;
- Q230 sits in an **α-helix** (i, i+4 spacing ≈ 6 Å) of the kind proline disrupts.

> ⚠️ **Scope of this step.** Every number here is measured on **wild-type geometry**. Wild-type geometry **does not prove** anything about the mutant: it does not establish that the mutant folds, that the active site survives substitution, or that any residual activity remains. **Mutant function is unknown.** What the step licenses is narrow and real — *the substituted position is not itself part of the catalytic machinery*, so "dead enzyme by direct active-site destruction" is not the expected first hypothesis. That is a question worth asking, not an answer.

### ❌ Step 2 — the ΔΔG "recoverability" threshold *(retracted as a predictor)*

ΔΔG(Q230P) = **+1.51 kcal/mol** (ThermoMPNN) was read as falling inside a therapeutically favourable band (roughly 0.8–3.5 kcal/mol) by analogy with CFTR correctors and storage-disorder chaperones.

> 🔴 **Retracted.** That band is a **heuristic borrowed from other proteins, and it has no demonstrated predictive value for WWOX** — no WWOX variant has ever been shown to be chaperone-responsive, so there is nothing to calibrate it against. A ΔΔG number predicts neither degradation, nor amenability, nor recovery of function. It is retained only as a *descriptive* quantity, never as a GO criterion.

### ❌ Step 3 — the "misfolding-dominant" tally *(retracted)*

Classifying the 13 pathogenic ClinVar missense variants by mapped ΔΔG produced a tally (7 inside the band, 1 catalytic, 5 other) that was read as evidence that WWOX missense pathology is misfolding-dominated, and therefore that a stabilizer would serve an identifiable sub-population.

> 🔴 **Retracted.** The tally inherits its meaning entirely from the band in step 2. Once the band is not a predictor, counting variants inside it measures nothing about amenability. The underlying per-variant table (`data/WWOX_pathogenic_missense_classified.csv`) is still shipped as **data**; the population inference drawn from it is not.

### ❌ Step 4 — P47T is **not** a read-across bench *(withdrawn; comparator only)*

The P47T mouse was read as belonging to the same mechanistic class — destabilizing, far from the active site, partial LoF, animal surviving > 1 year — and therefore as a bench where any proteostatic molecule effective on the class would transfer.

> 🔴 **Retracted.** P47T is **not** mechanistically equivalent: it has **normal protein levels** and a **WW1/PPxY binding defect** — a different lesion in a different domain. It remains a legitimate *comparator model*, not a read-across bench, and no proof about a buried SDR missense can be routed through it. G372R likewise is a natural-variant comparator, **not** a validated negative control. See `MECHANISM_TRANSFER_FIREWALL` in [`../../../framework/eval/learned_gates_registry.md`](../../../framework/eval/learned_gates_registry.md).

---

## 3. What pharmacological chaperones actually are (three distinct families)

Common principle: if a protein is *present but unstable*, the cell clears it. These molecules do not replace it — they aim to **stabilize it so it survives and works**. Nothing below is demonstrated for WWOX.

1. **Pharmacological chaperones (site-specific).** A small molecule binds the target protein *directly* — often in the active site or an allosteric pocket — and rigidifies it. Requires a binding pocket. The most targeted option.
2. **Kinetic stabilizers.** The molecule binds and *slows unfolding*, shifting the equilibrium toward the folded state. Does not have to be the catalytic site.
3. **Proteostasis regulators (indirect).** They do not touch the target protein; they boost the cell's *folding capacity* (heat-shock response activation, HSP70/HSP90 induction) or reduce degradation. Less targeted, but applicable with no known binding pocket.

### Real precedents — approved drugs (other proteins)

| Drug | Disease | Mechanism |
|---|---|---|
| **Migalastat** (Galafold) | Fabry disease | Pharmacological chaperone: binds a *mutant but partially functional* α-galactosidase A, stabilizes it, restores its levels. A **variant-specific assay precedent**, not a direct mechanistic analogue for WWOX. |
| **Tafamidis** (Vyndaqel) | Transthyretin amyloidosis | Kinetic stabilizer: binds TTR and prevents it from falling apart. |
| **Elexacaftor/tezacaftor/ivacaftor** (Trikafta) | Cystic fibrosis | Folding "correctors" for CFTR-F508del — recover a protein that would otherwise be degraded. |
| **Sapropterin** (Kuvan, BH4) | Phenylketonuria | Cofactor/chaperone stabilizing certain PAH mutants. |
| **Ambroxol** | Gaucher / GBA-Parkinson | An old mucolytic *repurposed* as a glucocerebrosidase chaperone — a repurposing precedent. |
| **4-PBA, TUDCA** | Various | Indirect proteostasis regulators already in paediatric use — the family that needs no known ligand. |

### The honest obstacle

A classic *site-specific* chaperone (migalastat-style) needs a ligand that enters the active site. WWOX's endogenous SDR substrate/cofactor **is not characterized** — WWOX is an "orphan" oxidoreductase with undefined physiological activity. That makes route 1 hard and shifts weight to **route 2 (allosteric/kinetic stabilizer)** and **route 3 (proteostasis regulators)**, neither of which requires knowing the natural ligand. Hence the first experiment is a **blind stability screen**, not a specific molecule.

A stabilizer targeting the SDR domain remains **`conditional / not design-ready`**, and must avoid both the functional region (388–407 / L404) and perturbation of the putative catalytic machinery.

---

## 4. 🔴 The repair (2026-07-14) — the premise that failed

The rationale above rested on a premise that was never itself checked: *normal mRNA + absent protein = post-translational degradation*. **That premise was withdrawn.** The primary source (Johannsen 2018) explicitly states **two** alternatives — impaired translation **or** premature degradation — and does not discriminate between them.

| Element | Status after the repair |
|---|---|
| "Normal transcript, protein not detected" (human, exact variant) | **Still a datum.** Unchanged. |
| Q230 buried, helical, non-catalytic, 6.8–9.7 Å from the active site | **Still stands** — a structural statement. |
| "Therefore the protein is degraded" | **Withdrawn.** Synthesis, insolubility and turnover are three separate questions. **CAUSE UNRESOLVED.** |
| The ΔΔG recoverability band as a predictor | **Withdrawn** — a heuristic with no demonstrated predictive value. |
| The "misfolding-dominant" population tally | **Withdrawn** — it inherited its meaning from the band. |
| P47T ↔ Q230P mechanistic equivalence / read-across bench | **Withdrawn** — P47T has normal protein and a WW1/PPxY defect. Comparator only. |
| C299R as a validated catalytic / off-site control | **Withdrawn** — sequence distance is not structural independence (`CONTROL_TOPOLOGY_CHECK`). |
| CMA route, the `LRSVQ` motif, the helix-lid model | **Hypotheses transferred from P252A / AlphaFold**, not a mechanism for this variant. |
| An SDR stabilizer as a design-ready lever | **`conditional / not design-ready`.** |

Two disciplines now bind whatever remains:

- **Stabilizing ≠ restoring function.** "Stable but inert" is a demonstrated WWOX phenotype (the P282A observation in the public literature). A stability readout without a function readout cannot support a GO. See `FUNCTIONAL_ORTHOGONALITY_PANEL`.
- **The clearance route must be measured, not assumed.** The textbook default "polyubiquitination → proteasome" is false as stated. K48 chains commonly support proteasomal turnover; K63 chains are multifunctional and can participate in trafficking and selective-autophagy pathways, but do not alone establish CMA. A proteasome-only experiment could return an uninformative result that reads as a false negative. See the *defaults that bit us* table in [`../research/dismissal_ledger_current.md`](../research/dismissal_ledger_current.md).

> **Why the document is published rather than deleted.** What survives is a **structural observation and an open question** — a buried, helical, non-catalytic residue in a protein whose absence is documented, with the cause unresolved. That is a legitimate research direction. What was deleted is every step that turned it into a *therapeutic expectation*. Keeping both visible, in order, is the point: this is what a repair actually looks like when it propagates.

---

## 5. The experimental path, in order

1. **Separate the causes first.** Before any stabilizer question: discriminate **synthesis vs insolubility vs turnover** on variant-carrying cells against WT/null and, as soon as possible, an isogenic knock-in — qRT-PCR/RT-PCR, metabolic labelling, cycloheximide chase, soluble/insoluble fractions, brief proteasome *and* lysosome perturbations with viability controls. Abundance and function must be measured **together**.
2. **Only if a turnover defect is demonstrated:** a cellular stability assay (thermal shift / DSF plus in-cell level readout), then a mini-screen of approved compounds and proteostasis regulators with pre-specified endpoints.
3. **Promote only hits that recover at least two orthogonal readouts** — abundance/localization *and* a directional functional output. A hit that raises protein without restoring function is not a hit.

There is **no** validated read-across bench for this class. P47T can be used as a comparator with the difference stated, never as a transfer route.

---

## 6. Honest limits

- ΔΔG values and distances are **predictions** on an AlphaFold structure, not experimental measurements of stability or degradation.
- The recoverability threshold used in the original analysis was a **retracted heuristic**; it is not a guarantee, not a predictor, and no longer a selection criterion.
- **Nothing shows that a re-stabilized destabilizing missense retains catalytic activity** — and WWOX's physiological activity itself is undefined. This is the first assumption to test, not a background belief.
- The mechanism by which the protein disappears is **unresolved**. Every downstream lever is conditional on resolving it.
- The value of this analysis is that it provides a **written rationale, the data, and an explicit list of what was withdrawn** — enough to ask a precise question of a laboratory instead of a generic one.

---

## 7. Where this work would live

Communities whose existing models and expertise this rationale would need (public, factual — no endorsement or relationship is implied):

- **Laboratories already working on WWOX**, which hold the organoid, mouse and gene-therapy models in which a proteostatic molecule could be tested.
- **Proteostasis and chaperone laboratories**, which know how to design a stability screen and have defined the stabilizer concept.
- **Rare-disease repurposing platforms** (e.g. translational-science screening centres running approved-compound collections), which fit route 3.
- For **splice-type alleles** the route is entirely different — an n-of-1 antisense programme, not a chaperone. See [`variant_triage_rescuability.md`](variant_triage_rescuability.md): lever assignment is per allele.

---

## Artifacts in this repository

| File | Content |
|---|---|
| `data/WWOX_proteostasis_hypothesis.png` | Stability-vs-catalytic map + class composition |
| `data/WWOX_residue_rescuability.csv` | Per-residue class (mean ΔΔG, distance from the active site) |
| `data/WWOX_pathogenic_missense_classified.csv` | The 13 pathogenic ClinVar missense variants, classified |
| `data/WWOX_ThermoMPNN_saturation.csv` | Source ΔΔG values |
| `data/WWOX_Q9NZC7_AlphaFold.pdb` | Source structure (active site, distances and burial recomputed from it) |
| `data/redteam/` | The adversarial red-team of this rationale (premises table, falsification matrix, discriminating experiment) |
