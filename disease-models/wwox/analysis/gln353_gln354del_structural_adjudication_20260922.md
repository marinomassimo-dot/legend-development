# `p.Gln353_Gln354del` — structural adjudication of the in-frame deletion

**Date:** 2026-09-22 · **Actor:** Orchestrator · **Class:** in-silico structural analysis
**Epistemic tag:** 🟡 `INFERENZA` throughout. **Nothing here is `DATO`.** The input is an AlphaFold
model, not an experimental structure. **Not medical advice.**
**Input:** `analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` (AlphaFold Monomer v2.0, Q9NZC7, 414 residues)
**Method:** direct numpy geometry — backbone dihedrals, CA–CA spans, heavy-atom neighbour counts,
polar-contact inventory. No DSSP and no biopython in this deployment; every number below is
computed from atom coordinates and is reproducible from the scripts recorded in §7.

---

## 0 · Why this question, and why now

The transcript-level consequence of the reference-genotype acceptor allele was settled earlier this
session: the cryptic acceptor is over-determined, the exon starts at `c.1063`, and the event is
**in-frame `p.Gln353_Gln354del`**. The canonical label was then, correctly,
**`PREDICTED at transcript level — protein consequence UNKNOWN`**.

`D-30` states why it could not be settled by the usual route: **in-frame is a statement about the
reading frame, not about the fold.** Its corollary is sharper — *the relSASA of a **deleted** residue
is a claim about that side chain, not about the fold* — which **invalidates `DL-MECH-037`'s
discriminator here**, because that discriminator was calibrated on **substitutions**.

So the methodological question had to be answered before the biological one:
**what discriminator is valid for a short in-frame deletion?** §5 answers it.

## 1 · Sequence identity confirmed against the reference model

```
1-based   350  351  352  353  354  355  356  357  358
residue    K    S    M    Q    Q    G    A    A    T
```

Residues **353 and 354 are both GLN** in the reference structure. `p.Gln353_Gln354del` deletes the
`QQ` dipeptide exactly. The flanks are M352 and G355, so the two-residue unit is **unique** — there
is no HGVS 3′-shift ambiguity to resolve. ✅ This is an **independent confirmation of the
transcript-level adjudication from a source that was not used to make it.**

## 2 · Method positive control — REQUIRED before any number below is believed

The repository independently records, from a separate AlphaFold + SASA/SSE analysis, that **Gln230
sits in the SDR core in a well-confident helical segment** (`CLAIM 034` source block).

| measure | my computation for Q230 | repo's independent record | agrees |
|---|---|---|---|
| secondary structure | helical (φ −65.4°, ψ −50.3°) | "segmento elicoidale" | ✅ |
| confidence | pLDDT **98.50** | "ben confident" | ✅ |
| burial | neighbour count **201** (chain Q3 = 184, max = 233) | "nel core SDR" | ✅ |

**The method reproduces a fact it was not tuned to.** Without this control none of §3–§4 would be
usable.

## 3 · 🔴 Two things the repository says about this site are wrong

### 3.1 "model confidence lowest exactly there" — **FALSE**

| residue | pLDDT |
|---|---|
| **353** | **85.81** |
| **354** | **87.25** |
| chain min / Q1 / median / max | 29.5 / **82.8** / 93.2 / 98.9 |

353 and 354 sit **above the chain's first quartile**. The genuine confidence minimum is **≈10–14
residues upstream**, at **340–347 (pLDDT 35.1–46.7)** — a different structural element entirely.

**This matters in the direction that makes the analysis stronger, not weaker.** The prediction at the
deletion site is more trustworthy than the repository has been saying, and part of the justification
for "structurally contested" rested on a false premise. *(Backbone confidence ≈86 is good; **side-chain
rotamers are less reliable than backbone at any pLDDT**, which is why §4.2 is tagged more weakly
than §4.1.)*

### 3.2 "mid-α-helix" — **FALSE, and this is the load-bearing correction**

The contiguous helix is **352–363** (12 residues). The ψ boundary is unusually clean: ψ(351) = **+159.8°**
(extended) → ψ(352) = **−35.8°** (helical). So:

> **353 and 354 are at helix positions 2 and 3 — the N-terminal EDGE of the helix, directly adjacent
> to the 348–351 coil.** Nine helical residues lie **downstream**; none lies upstream.

"Mid-helix" would have made the deletion nearly unsurvivable (§4.1). The true position is what puts
a shock absorber next to the lesion.

## 4 · The adjudication, in two halves that point opposite ways

### 4.1 Backbone — 🟢 **a low-strain local accommodation EXISTS**

A 2-residue deletion inside an α-helix imposes on everything downstream a rotational register shift
of **2 × 100° = 200°** and a translation of **2 × 1.5 Å = 3.0 Å** (3.6 residues/turn). The nine
downstream residues are **among the most buried in the protein**:

| residue | 355 | 356 | 357 | 358 | 359 | 360 | 361 | 362 | 363 |
|---|---|---|---|---|---|---|---|---|---|
| burial | 197 | 210 | 219 | 223 | 216 | 226 | 213 | 220 | 205 |

*(chain Q3 = 184, max = 233 — **every one is above the 75th percentile**.)* A forced 200° rotation of
that set would repack the core face of the helix. **That is the catastrophe scenario — and the
geometry refuses it.**

**The span test.** After deletion, M352 bonds directly to G355. Maximum CA–CA reach is ≈3.8 Å per
peptide bond:

| pair | bonds after deletion | max reach | observed now | verdict |
|---|---|---|---|---|
| 352→355 | 1 | 3.8 Å | **4.97 Å** | 🔴 STRAINED by 1.17 Å |
| **351→355** | 2 | 7.6 Å | **6.32 Å** | 🟢 OK, 1.3 Å slack |
| 350→355 | 3 | 11.4 Å | 6.33 Å | 🟢 OK, 5.1 Å slack |
| 349→355 | 4 | 15.2 Å | 9.49 Å | 🟢 OK |

**Read it correctly.** Holding *both* M352 and G355 fixed is infeasible — by only 1.2 Å. But release
the residues **upstream** of 352, which are **already coil** (ψ: 349 = +131°, 350 = +148°, 351 = +160°),
and the requirement is met with slack to spare. The structural solution is therefore:

> **the helix simply starts two residues later; its N-terminal turn frays back into the pre-existing
> 348–351 coil; and the deeply-buried 355–363 segment keeps its register and its position.**

**The fold does not have to collapse.** Had the deletion fallen at 358–359 — mid-helix, buried on both
sides, no adjacent coil — no such solution would exist. It is off by about six residues.

### 4.2 Side chains — 🔴 **the deletion removes a six-contact tertiary staple**

Q353 and Q354 are **not inert spacers**. Their side chains make six polar contacts, and **four reach a
segment 210–245 residues away in sequence**:

| donor/acceptor | partner | distance | note |
|---|---|---|---|
| **Q353 NE2** | **OE2 (Glu139)** | **2.69 Å** | strong, charged — **Δseq 214** |
| Q353 NE2 | OG (Ser143) | 3.20 Å | Δseq 210 |
| Q353 OE1 | N (Ala113) | 3.41 Å | backbone amide — Δseq 240 |
| Q353 OE1 | N (Met114) | 3.33 Å | backbone amide — Δseq 239 |
| **Q354 NE2** | **O (Ser110)** | **2.80 Å** | strong — **Δseq 244** |
| **Q354 OE1** | **N (Ser351)** | **2.85 Å** | ⭐ the helix's own **N-cap** |
| Q354 OE1 | OG (Ser351) | 3.59 Å | same interaction, second atom |

Two consequences, and neither is repaired by §4.1:

1. **A tertiary staple is lost.** These two glutamines pin helix 352–363 against the **110–143**
   element. Sliding the helix start does **not** put a glutamine amide back where Glu139 and Ser110
   are being hydrogen-bonded — the accommodation in §4.1 is precisely a motion that **breaks** them.
2. **The helix loses its own N-cap.** Q354-OE1 satisfies the free backbone NH of Ser351 (2.85 Å) —
   a textbook capping interaction. After deletion that NH is unsatisfied and the new helix
   N-terminus is **M352→G355**; Met is a poor N-cap and Gly is a helix breaker.

### 4.3 It is a packing lesion, not an active-site lesion — 🟢 **and that is therapeutically load-bearing**

The canonical SDR catalytic motif `Y-x-x-x-K` occurs at **Y293…K297**. Distances from CA(353):

| to | distance |
|---|---|
| Y293 | **22.9 Å** |
| K297 | **21.0 Å** |

At >20 Å this is **not** a catalytic-site lesion. It is a **tertiary-packing / stability** lesion.
That distinction is not cosmetic: a packing-and-stability defect is the class a pharmacological
chaperone could in principle address (the `TX-003` logic), whereas an active-site lesion is not.
⚠️ **This licenses a hypothesis, not a therapy.** It does not show the protein is made, folded,
stable or functional, and `TX-003`'s own precondition still stands: **separate synthesis, solubility
and turnover, and tie abundance to a functional readout, before calling anything rescuable.**

## 5 · The methodological answer — what discriminator is valid for a short in-frame deletion

This is the transferable result, and it closes the gap `D-30`'s corollary opened.

| discriminator | valid for a **substitution** | valid for a short **in-frame deletion** |
|---|---|---|
| ΔΔG-style folding predictors (ThermoMPNN etc.) | ✅ | ❌ — no residue to substitute; the chain **length** changes |
| relSASA / burial **of the affected residue** | ✅ | ❌ — `D-30` corollary: it describes a side chain that **no longer exists** |
| LLR from a sequence model (ESM) | ✅ | ⚠️ trained overwhelmingly on substitutions |
| **span feasibility** (can the shortened chain reach, with upstream/downstream anchors released?) | n/a | 🟢 **yes — the primary test** |
| **register-shift exposure** (how much buried helix lies downstream, with no coil between?) | n/a | 🟢 **yes** |
| **lost-contact inventory** (what do the deleted side chains hold?) | n/a | 🟢 **yes** |

> **A deletion is a geometry problem before it is an energetics problem.** Ask first whether the
> remaining chain can still reach; only then ask what the loss costs.

## 6 · Verdict, and the exact permitted wording

🔴 **The label `PREDICTED at transcript level — protein consequence UNKNOWN` should NOT be promoted
to "functional" or demoted to "null".** It should be **made specific**:

> **Permitted:** *The in-frame deletion sits at the N-terminal edge of helix 352–363, adjacent to a
> pre-existing coil, so the backbone admits a low-strain local accommodation and the fold is not
> required to collapse (in-silico, AlphaFold model). The same deletion removes both partners of a
> six-contact polar network staking that helix to the 110–143 element, including the helix N-cap.
> The site is >20 Å from the SDR catalytic tetrad, so this is a packing/stability lesion rather than
> an active-site lesion.*

> **NOT permitted:** *"the protein folds"* · *"the allele is a hypomorph"* · *"residual activity is
> expected"* · *"the deletion is tolerated"* · any statement that the protein is **made**, **stable**
> or **functional**. None of that is measured, here or anywhere.

**What would settle it, cheapest first:** (1) expression of the deletion construct with a solubility
split — synthesis vs aggregation vs degradation, the `TX-003` precondition; (2) thermal shift against
wild type; (3) an SDR activity readout on the recovered protein. ⚠️ **None of these has been done for
any WWOX in-frame deletion**, so the honest premise tag on the whole node remains
`PREMISE: NOBODY_LOOKED`.

## 7 · Reproducibility

Computed with three scripts (backbone/φψ/pLDDT/burial · span test · contact inventory) against
`analysis/data/WWOX_Q9NZC7_AlphaFold.pdb`. Helix assignment uses φ ∈ [−100°, −30°], ψ ∈ [−80°, −5°];
the 352 boundary is robust to the cutoff because ψ jumps **+159.8° → −35.8°** across it. Burial is a
heavy-atom neighbour count within 10 Å of CB (CA for Gly), reported against the chain-wide
distribution rather than as an absolute.

**Limits, stated plainly.** This is a **predicted** structure. Backbone confidence at the site is good
(pLDDT ≈ 86) but **side-chain rotamers are the least reliable part of any such model**, so §4.2's
contact inventory is a **hypothesis about contacts**, not a measurement of them — it is the part of
this analysis most likely to be wrong, and it is the part carrying the most weight. §4.1 rests on
backbone geometry only and is correspondingly firmer. No molecular dynamics was run; a static model
cannot show whether the frayed N-terminus is stable in solution.

---

## 8 · Provenance of the error — added after Scientist P's return

Scientist P, adjudicating the transcript half independently and without this analysis, wrote:

> *"whether that protein folds/localises/functions is UNKNOWN and structurally contested (`D-30` —
> **mid-helix deletion at pLDDT 60–76**…)"*

Both halves are wrong, and the second is wrong in a way that names its own source:

| pLDDT | 349 | **350** | **351** | 352 | **353** | **354** | 355 | 356 |
|---|---|---|---|---|---|---|---|---|
| | 53.19 | **60.47** | **76.38** | 82.44 | **85.81** | **87.25** | 86.06 | 93.69 |

> 🔴 **"60–76" is residues 350–351, exactly.** The figure was misattributed to 353–354 — an
> **off-by-three residue error**. And 350/351 are precisely the residues my §4.1 identifies as the
> **coil that absorbs the deletion**; their lower confidence is expected for a loop and says nothing
> about the helix.

P did not invent this: it inherited the characterisation from the repository, which is the same
place my §3.1 and §3.2 found it. **One error, propagated to two independent workers, and visible
only because the coordinates were measured rather than quoted.** The repository's phrasing —
*"mid-α-helix, one turn from a buried face, model confidence lowest exactly there"* — should be
withdrawn in all three of its parts.

⚠️ **P's supporting analogy is also unsound.** *"The exon-7 case in this same session was in-frame
and lethal"* compares a **62-residue** deletion through the ADH/SDR domain interior with a
**2-residue** deletion at a helix N-terminus adjacent to a coil. `D-30` says in-frame is not about
the fold; it does **not** say every in-frame deletion behaves alike. **The two cases differ by a
factor of 31 in length and by their entire structural context.**

**What this does NOT license.** None of it makes the protein functional, and §6's permitted wording
is unchanged. The correction runs in one direction only: the site is **better predicted** and
**better placed** than the repository claimed, so "structurally contested" overstated the doubt —
while §4.2's six lost contacts, which nobody had inventoried, understated a different one.
