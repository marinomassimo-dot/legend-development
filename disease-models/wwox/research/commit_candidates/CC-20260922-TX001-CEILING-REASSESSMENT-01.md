# CC-20260922-TX001-CEILING-REASSESSMENT-01

**Status:** 🔴 **PROPOSED — NOT PROPAGATED**
**Target:** `therapeutics/therapeutic_strategies_current.md` → `TX-001` (Mechanism; Provisional
scoring commentary) · `tx001_experiment_decision_packet_20260921.md` (design section)
**Class:** reassessment of a named strategy's expected value. **It cuts against the strategy.**
**Depends on:** `36ee7bb` (NMD premise withdrawal), `CC-20260922-NMD-PREMISE-WITHDRAWAL-01`
**Produced by:** Orchestrator, from Scientist P's architecture derivation + my own structural work

---

## 1 · The unconditional finding: TX-001's design prior is architecturally inapplicable

`TX-001`'s Mechanism paragraph treats four outcomes as open:

> *"Exon skipping, cryptic acceptors, intron retention or multiple isoforms could emerge."*

And its own 2026-09-21 audit records that the field's entire empirical prior points one way:

> *"Su tutte e quattro le misure del censimento **ogni prodotto riportato è uno skipping**: nessuno
> riporta ritenzione d'introne né sito criptico."*

🔴 **Exon skipping cannot occur at this allele.** The lesion destroys the acceptor of **exon 9**, and
**exon 9 is the terminal exon** — there is no exon 10 to splice to, and no intron in the 3′UTR out to
`c.*385`. Skipping a terminal exon is not a splice outcome; it is the absence of one.

> **So four of four published WWOX splice-allele measurements report the one outcome that is
> structurally impossible here.** The field's prior is not weak evidence for this allele — it is
> **inapplicable**, and `TX-001` currently inherits it as though it were informative.

This half is **unconditional** and does not depend on any prediction.

## 2 · The conditional finding: the ceiling

Under the surviving outcome — cryptic acceptor at `c.1063` — the transcript is **in-frame**, carries
**no premature termination codon**, and encodes a **412-aa** protein (`p.Gln353_Gln354del`) rather
than a truncation.

> 🔴 **If that is what the allele does, splice correction recovers two residues, not a protein.**

`TX-001`'s stated efficacy endpoint is *"la frazione di trascritto correttamente spliced."* Against a
transcript that is already near-full-length and already escaping NMD, that endpoint can move a long
way while the **protein** endpoint barely moves at all. The strategy's ceiling is not set by how well
an ASO redirects splicing; it is set by **how much the two missing residues cost** — and my
structural work puts that at a **six-contact polar staple plus the helix N-cap**, which is
consequential but is **not** the difference between a protein and no protein.

**This half is CONDITIONAL and must be labelled so.** `DS_AG 0.64` is **moderate and has never been
measured**. The competing outcome — intron-8 retention — gives the opposite answer: a retained
**779-kb** intron yields no functional protein at all, and against *that* baseline correction recovers
essentially everything.

## 3 · What the reassessment actually is: bimodal, not negative

| if the real outcome is… | what correction recovers | TX-001's value |
|---|---|---|
| cryptic acceptor `c.1063` (in-frame, no PTC) | **2 residues** | 🔴 **low** — the allele already makes near-full-length protein |
| intron-8 retention / intronic poly(A) | **a protein, from none** | 🟢 **high** |
| a mixture | proportional to the retained fraction | 🟡 intermediate, and the **ratio is the endpoint** |

> **`TX-001`'s expected value is bimodal, and the experiment that resolves it is the experiment
> `TX-001` already names as its mandatory gate.** The finding therefore does **not** retire the
> strategy. It **raises the value of the gating assay** while **lowering the expected payoff
> conditional on one branch** — and it makes the gate's *design* load-bearing in a way the current
> packet does not capture, because a badly designed assay returns the wrong branch rather than no
> answer.

⚠️ **The honest counter-consideration, recorded rather than buried:** even under the low branch,
`TX-001` is not worthless — two residues that carry a tertiary staple and an N-cap are not nothing,
and the missense allele on the other chromosome is untouched by any of this. What collapses is the
*framing* of `TX-001` as restoring a protein that is otherwise absent.

## 4 · Four design constraints, each of which otherwise forces a FALSE NEGATIVE

These are not refinements. Each one, alone, makes the assay return the wrong branch:

1. **The aberrant product is 6 nt SHORTER, not `+8` longer.** `+8` is a genomic offset, not an
   amplicon size change. 6 nt on a ~271 nt amplicon is **2.2%** ⇒ **capillary/GeneScan, denaturing,
   with a 6-nt sizing standard. Not agarose. Not native PAGE.** *(This defect was already repaired in
   the packet on 2026-09-21; it is restated because constraints 2–4 are new and the set must be read
   together.)*
2. 🔴 **An intron-8-anchored reaction plus 3′ RACE is MANDATORY.** A retention species **has no exon
   9**, so an exon-8→9 assay cannot see it — and its absence would be silently misread as
   *support for the cryptic outcome*. **This is the single most likely way the experiment produces a
   confident wrong answer**, because it fails in the direction of the hypothesis being tested.
3. 🔴 **The ±cycloheximide arm has less power than the packet implies.** Under the surviving outcome
   there is **no PTC**, so there is nothing for EJC-dependent NMD to act on. Keep the arm — to catch a
   competing PTC species and to probe long-3′UTR NMD — but with a vehicle twin and an **endogenous
   NMD-sensitive positive control**, and do not read a null as informative about the main branch.
   ⚠️ **And a 779-kb retained intron is likely nuclear-retained and exosome-cleared — not NMD, and
   cycloheximide-insensitive.** A CHX-insensitive loss must **not** be scored as NMD.
4. 🔴 **Do not normalise to the exon 4–6 core.** Davids measured that the short isoform's exon 5–6
   junction **rises** when the long isoform is lost, so that denominator **moves with the lesion** and
   would compress the very ratio the assay exists to measure.

## 5 · Proposed edits (exact, none applied)

1. **Mechanism paragraph** — strike *"Exon skipping"* from the list of possible outcomes and state
   that it is **excluded by architecture** (exon 9 terminal, no exon 10, no 3′UTR intron); add that
   the four published WWOX splice measurements all report skipping and are therefore
   **inapplicable**, not merely weak.
2. **Add a ceiling note** carrying §2 and §3 verbatim, explicitly tagged **CONDITIONAL — the
   `c.1063` outcome is PREDICTED (`DS_AG 0.64`), never measured.**
3. **Packet design section** — add constraints 2, 3 and 4 as rows, each with its false-negative
   direction named.
4. **Provisional scoring** — do **not** re-score. `FLAG FIRST; SCORE ONLY AFTER MECHANISM + REAGENT +
   ALLELE VERIFICATION`, and none of the three is satisfied. Attach the flag instead.

## 6 · What this candidate does NOT do

- ❌ It does **not** retire or down-rank `TX-001`. §3 is a bimodal expected value, not a negative one,
  and §4 of the proposed edits explicitly refuses to re-score.
- ❌ It does **not** treat the `c.1063` outcome as established. It is `PREDICTED at transcript level`;
  the protein consequence is separately unresolved.
- ❌ It does **not** claim the 412-aa protein is made, folded, stable or functional.
- ❌ It does **not** touch `TX-003`, `TX-007`, or the missense allele's arm.

## 7 · Why gated

A non-zero scientific delta on a therapeutic strategy record, outside the current authorization's
scope. And §2 rests on a prediction whose measurement is precisely the experiment under discussion —
propagating a ceiling revision from an unmeasured branch would commit the error this candidate is
written to prevent.
