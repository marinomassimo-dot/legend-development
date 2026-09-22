# "Fold of WT" is undefined for vector genomes — I tried to dissolve the flag and the attempt failed

**Date:** 2026-09-22 · **Actor:** Orchestrator · **Class:** logical adjudication, no new source read
**Depends on:** `cerebellum_layer_localisation_20260922.md` (Scientist C) findings 1 and 2
**Not medical advice.**

---

## 1 · The flag being tested

Scientist C localised the forebrain–cerebellum divergence to **layer 2, VECTOR GENOME**, and named its
own hostage:

> **Fig 5A–5D's y-axis definition decides whether that finding stands.** The caption is
> **repo-attested** as *"normalized to WT levels"* — 🔴 **undefined for vDNA**, because wild-type
> animals receive no vector.

## 2 · The escape route I tested, and why it looked promising

The paper **has a wild-type injected arm**, labelled `WT+RI`, and the Methods state *"WT littermates
received identical injections to control for procedural effects."* If `RI` were the **vector**, then
*"normalized to WT levels"* would be perfectly well defined for vDNA — normalised to the vector load
in vector-injected wild-type animals — and C's flag would dissolve.

## 3 · 🔴 It fails. `RI` is the VEHICLE.

Verbatim from the paper, first-hand on the served body:

> *"KO mice injected with the **reference item (RI)**"*
> vehicle composition: *"**PBS with 5% sorbitol and 0.001% pluronic F-68**"*

⇒ `WT+RI` and `KO+RI` are **vehicle-injected**, not vector-injected. **They carry zero vector
genomes.**

> **So there is no vector-injected wild-type arm anywhere in this study, and therefore NO panel in
> this paper can be "normalized to WT" for any vector-derived quantity.** The escape route is closed,
> and **C's flag stands more firmly than before it was tested.**

## 4 · What remains — two possibilities, both attestation problems rather than biology

| | possibility | consequence |
|---|---|---|
| **A** | The caption clause is **boilerplate spanning a multi-panel caption** and belongs to the **protein/mRNA** panels, not to 5A–5D | 5A–5D plots **raw copies per reaction** ⇒ **C's per-nucleus reading stands** |
| **B** | The attestation itself is **mis-scoped** — a prior actor attached a clause from elsewhere in the caption to these panels | same as A, with the defect in our record rather than the paper |

🎯 **Both possibilities point the same way, and that is the useful part:** neither is a biological
alternative, and under both the per-nucleus reading survives. **The residual risk is not that C is
wrong about the biology — it is that we cannot yet cite the axis.** ⚠️ A third possibility cannot be
excluded without the caption: that the panels plot something else entirely.

**Testable prediction about the caption's scope:** *"normalized to WT levels"* should be found
attached to panels measuring a quantity wild-type animals **possess** (WWOX protein, WWOX mRNA) and
**not** to the vDNA panels. `REVIVAL_TRIGGER`: the Fig 5 caption, from any route.

## 5 · The synthesis this produces — "fold of WT" fails in TWO different ways in one paper

| quantity | why "fold of WT" is unsafe | status |
|---|---|---|
| **vector genomes** | 🔴 **WT value is ZERO** — the ratio is not merely unmeasured, it is **undefined**; there is no vector-injected WT arm | **§ 3, first-hand** |
| **WWOX protein** | 🔴 **the WT REGIONAL baseline was never measured**; 2021 asserts uniformity by citation, and GTEx contradicts it (cerebellum **1.6–2.2× higher**) | C's finding 2 |

> **One paper, one phrase, two incompatible failure modes: undefined in one case, unmeasured in the
> other.** Every cerebellar "fold-of-WT" number in the record inherits one of them, and the two need
> different repairs — the first needs a **caption**, the second needs a **mouse-protein baseline**.

🟢 **And the result that escapes both** is the within-region dose ratio, because `HD/LD` **cancels the
baseline exactly, whatever it is**: vDNA **2.28×**, mRNA **2.57×**, protein **0.74×** (cerebellum) and
**0.98×** (hippocampus). ⇒ genome and transcript track dose, protein does not, **in both
compartments** — so the ceiling sits at **transcript → protein** and, being shared, **cannot produce
the regional divergence.**

## 6 · Consequence for the record

- ⚠️ **Do not cite any cerebellar fold-of-WT figure** without naming which failure mode it inherits.
- 🟢 **Prefer the within-region dose ratios** for any claim about where the dose ceiling sits — they
  are baseline-free by construction.
- 🔴 **Do not restate C's per-nucleus finding as established** until the Fig 5 caption is read. It is
  **well-argued and currently unciteable**, and those are different things.
- ⚪ Nothing here reopens the closed dose non-monotonicity premise.
