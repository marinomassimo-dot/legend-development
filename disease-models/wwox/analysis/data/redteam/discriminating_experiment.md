# The single most discriminating experiment

## The gap it closes
Every mechanistic observation in the model comes from **P252A** (Zhang 2025). **Q230P — the actual patient allele — has never been assayed for degradation, HSC70 binding, or lysosomal routing.** The mechanism for Q230P is entirely extrapolated. Worse, the data cannot distinguish three live models:

- **M0/M2** — destabilization exposes a *specific* KFERQ motif (LRSVQ *or* ERLIQ) → HSC70 → CMA.
- **M1** — *global* SDR misfolding → generic quality-control degradation (lysosomal), motif-agnostic.
- **M4** — Q230P is a co-translational folding-yield defect, not post-translational degradation at all.

## The experiment: cycloheximide-chase degradation panel with **degron epistasis in cis**
A single Western-blot series (transient transfection, HEK293T or patient-genotype fibroblasts), one experimenter, ~2 weeks. Constructs, all C-terminally tagged (tag away from both candidate degrons):

| Arm | Construct | Tests |
|-----|-----------|-------|
| 1 | WT | baseline half-life |
| 2 | **Q230P** | *does the patient allele actually get degraded?* (never done) |
| 3 | Q230P + **Q191A** | knock out the LRSVQ Gln (in cis) |
| 4 | Q230P + **Q406A** | knock out the ERLIQ Gln (in cis) |
| 5 | P252A | positive control (reproduce Zhang) |
| 6 | C299R | negative control for the degron route (should degrade via *catalytic* misfold or be stable) |

Each arm read at steady state and under: **(a) cycloheximide chase** (half-life), **(b) chloroquine or NH₄Cl** (lysosome), **(c) MG-132** (proteasome), **(d) HSPA8/HSC70 siRNA**.

### Why the glutamine, not L187A/V190A
The dossier's draft plan mutated L187A/V190A to kill the degron. **Those residues are fully buried (RSA ≈ 0)** — mutating them destabilizes the fold itself, so reduced protein would be uninterpretable (structural, not degron, effect). **The essential KFERQ glutamine is the clean knockout:** Q191 (RSA 0.28) and Q406 (RSA 0.58) are exposed, carry little structural load, and the Q is the non-substitutable recognition residue for HSC70. Q→A abolishes recognition without unfolding the protein.

## Outcome matrix — every result interprets

| Q230P degraded? | CQ rescue? | MG-132 rescue? | Q191A rescues? | Q406A rescues? | ⟹ Conclusion |
|---|---|---|---|---|---|
| yes | yes | no | **yes** | no | **M0 confirmed** — LRSVQ is the operative degron, CMA route, Q230P = P252A mechanism |
| yes | yes | no | no | **yes** | **M2** — same CMA mechanism but degron is **ERLIQ 402-406**, not LRSVQ (model survives, premise corrected) |
| yes | yes | no | no | no | **M1** — global misfolding, lysosomal but motif-agnostic; the "specific degron" premise is **refuted** |
| yes | no | **yes** | — | — | proteasomal, not CMA — the whole CMA framing is wrong for Q230P |
| **no** | — | — | — | — | **M4** — Q230P is a translation/folding-yield defect; the degradation model is **refuted** for the patient allele |

## The correction that pays for the experiment
Zhang's own data show **MG-132 is mute** on WWOX. A team defaulting to MG-132 as the primary degradation probe would see no rescue and wrongly conclude "degradation is not the bottleneck" — a false negative that kills the best therapeutic hypothesis. **CQ/NH₄Cl must be the primary probe; MG-132 is the specificity control, not the readout.** Cost of getting this right: two extra wells.

## Two arms added after an independent second red-team
- **Route resolution (CMA vs eMI vs bulk lysosomal).** Chloroquine/NH₄Cl block *all* lysosomal degradation and cannot tell the routes apart; HSC70 co-IP is shared by CMA and eMI. Add a **LAMP2A knockdown** arm (blocks CMA only) and a **VPS4/ESCRT block** arm (blocks eMI only). Zhang read out with LAMP1 (generic lysosome), not LAMP2A (CMA receptor), so the "CMA" label is not yet earned even for P252A.
- **Function in parallel with abundance.** The canonical degron ERLIQ 402-406 contains **L404**, implicated in WWOX–GSK3β binding. Measure a GSK3β/Tau functional readout alongside protein level, so a degron-knockout arm that restores abundance but kills function is caught immediately — the "stable-but-inert" NO-GO, detected before any stabilizer is built.

## Two caveats from the second audit (adopted)
- **CHX chase does not measure synthesis.** Johannsen's open fork is *translation-impaired OR degraded*; a CHX chase only reports decay of already-made protein. To close the fork you must **measure nascent synthesis directly** (35S or puromycin/OP-Puro pulse, or a pulse-chase) as step 1 — before any half-life readout. If Q230P is barely synthesized, the whole degradation panel is moot.
- **Tag placement is not free.** A C-terminal tag sits only ~8 residues from **ERLIQ 402-406**; it could mask or mimic that degron. Use an **N-terminal tag** (or compare N- vs C-terminal) so the readout does not itself perturb the C-terminal motif under test. Do the epistasis on WT background too, not only Q230P, to separate degron effects from destabilization effects.

## What it cannot do
- It cannot prove the *helix* is the trigger (that needs the helix-restoring second-site suppressor, a separate experiment). It tests the *degron/route*, which is where the model is weakest.
- Transient overexpression can saturate CMA; confirm the key arms at endogenous level in patient fibroblasts (Aqeilan/Johannsen have Gln230 lines).
