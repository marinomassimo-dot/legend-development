# Session self-evaluation — Orchestrator, fifth autonomous run (2026-09-22)

**Scope:** `62218b6` → this commit. Three Scientists dispatched (A, B, C); two pre-registered
recursive re-reads run by the Orchestrator; five landings. **The upgrade is the answer, not the
promise of one** — this run ships no script, and §3 argues that shipping one would have been the
wrong answer to what actually went wrong.

---

## 1 · What the run established

| | |
|---|---|
| 🟢 **A positional discriminator for `Q230P` that nobody has proposed** | A two-epitope Puro-PLA ratio straddling residue 230, built by repurposing the founding paper's own **N-versus-C specificity control** as a measurement. It reads *where chains are being lost*, which a CHX chase structurally cannot |
| 🟢 **The paper that "breaks" Puro-PLA validates it for this use** | Hobson 2020 refutes the **spatial** claim and, in the same paragraph, affirms that the signal *"reports primarily on the **cytoplasmic abundance** of puromycylated NPCs"* — which is the only quantity the design needs |
| 🟢 **The flanking antibody pair two prior designs specify CANNOT BE BUILT** | Across 17 censused anti-WWOX primaries the epitope-documented reagents are **N-terminal** or **span 230**. The **C-terminal-only class is empty**. Those designs were unexecutable, not merely unfunded |
| 🟢 **The intersection is empty** | The organs carrying the **unrescued** peripheral phenotypes (bone, spleen, thymus, marrow) and the organs ever **assayed** in a treated animal (liver, pancreas, kidney, testis, ovary, sciatic nerve) **do not overlap at all** |
| 🟢 **Transduction was never measured outside the brain** | Every peripheral WWOX measurement in a treated animal is a **protein blot**. *"No WWOX protein in liver"* bounds **expression** and says nothing about **vector arrival**; the two have been used interchangeably |
| 🟢 **The cheapest decisive systemic experiment needs no treated animal** | The untreated-null **time course** at P3/P7/P10/P14/P18. It is the only route to `R5`, and it converts the baseline from a **point** into a **distribution** — without which no rescue is scorable |
| 🟡 **`CLAIM 038`'s unit is neither ours nor established as theirs** | `TRANSCRIBED FAITHFULLY AND UNADJUDICATED`. Both branches the existing candidate allowed are wrong |
| 🟢 **Creatinine was never measured in the mouse** | Found twice the same day, by two actors who did not read each other |

## 2 · ATTRIBUTION_CENSUS

```
ATTRIBUTION_CENSUS
incidents: 5
machine: 2   blind_auditor: 0   peer: 0   self: 3
severity_high: 1   of which self: 1
undetected_known: 0
```

**`machine: 2`** — (a) the `UNREAD_PREMISE` gate firing at **6 above a baseline of 0** on Scientist
A's method citations, correctly; (b) `growth_anchors` confirming the repair returned it to `0`
rather than my asserting it had.

**`self: 3`** —
1. 🔴 **§2.1 — I was one paragraph from publishing a rediscovery as a discovery.**
2. **The `LEGEND_CORE §26` misattribution**, mine, from an earlier run in this series (§2.2).
3. **I dispatched three heavy delegates simultaneously and lost two hand-backs to a session rate
   limit** (§2.3).

`severity_high: 1` — (1). It would have put a false novelty claim into a packet that goes to the
Operator.

### 2.1 🔴 The defect that did not happen, and why it counts as one

Re-read cycle 3 reconstructed, from `entries[26]`, that a rat glucose of `169 mg/ml` is 16,900 mg/dL
and therefore that the rat table is numerically `mg/dL`. It is a clean argument and I had the
paragraph drafted.

**`enumerate_baseline_before_scoring`, run before writing rather than after, returned two artefacts
I did not know existed**: a commit candidate for this exact defect raised by **Scientist G** earlier
the same day, and the **same glucose argument** already written in the peripheral denominator audit
§3.2. **Both findings were demoted to `REDISCOVERY` before publication, not after.**

🟢 **This is the primitive's first preventive success on the Orchestrator rather than on a delegate**,
and it answers the standing objection recorded against it on the scorecard — that its instances were
delegate-facing and might therefore be measuring hand-back compression rather than a property of the
corpus. **This instance involves no hand-back and no delegate.**

🔴 **And the counting rule is the uncomfortable part.** A near-miss caught by my own check is still a
defect I committed; it is counted, and the fact that the check worked does not remove it from the
census. A census that only counts the ones that got through measures the filter, not the actor.

### 2.2 A misattributed citation in the one sentence called *"the constraint that outranks everything"*

`LEGEND_SCIENTIFIC_DISCOVERY_METHOD_V0_PROPOSAL.md` §0 attributes the no-new-gates rule to
*"`LEGEND_CORE` §26."* **`LEGEND_CORE.md` ends at §22.** The rule is the **operator's directive** §26
— which is how **every commit candidate in this repository** cites it, and which
`governance/candidates/CAND-20260819-ORCHSURF.md:444` had **already disambiguated in writing**
(*"directive §26, not body §26"*). The proposal is the **only** file that gets it wrong, and it is
mine. Corrected.

**The lesson is not "check citations."** It is that a wrong address survives longest in the sentence
nobody argues with, because a reader checking a constraint is checking the **constraint**, not its
**address** — the identical shape as the uncited premise found inside a *limitations* bullet in
candidate 2 of the Operator packet.

### 2.3 🔴 Three heavy delegates at once cost me two hand-backs

Scientists A and C both terminated on a session rate limit **after writing their files completely**
(748 and 775 lines, both ending in their own closing statements) but **before handing back**. Nothing
was lost from the repository; what was lost was the **structured summary**, so I read ~1,500 lines
myself to extract what a hand-back would have given me in one screen.

> **Rule this run adds: a hand-back is a deliverable, and it is the one produced last.**
> Staggering the third dispatch would have cost wall-clock and preserved it. **The file surviving is
> luck, not design** — a delegate cut off ten minutes earlier would have left a half-written artefact
> in the tree with no marker saying so.

⚠️ **Related, and it cuts the other way from the fourth run's lesson.** That run established *"a
census cannot be verified on a tree that already holds the census"* — the working tree was the wrong
surface. **Here the working tree was the right one**: the `UNREAD_PREMISE` gate fired on an
**untracked** file and was correct to, because that file was about to be committed. ⇒ **The rule is
not "prefer the committed tree." It is "name the surface, and name why that surface is the one the
claim is about."**

## 3 · The upgrade, and why it is not a script

The fourth run shipped `census_verify.py` because its defect was **measurable and repeatable**. This
run's defects are not of that kind: a misattributed citation, a near-miss caught by an existing
habit, and a scheduling decision. **§26 forbids answering a scientific mistake with a new gate,
authority, auditor, registry or workflow, and a tool built for any of these three would be exactly
that** — a compliance surface for a thinking move.

**What shipped instead** is
[`framework/instruction/LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md`](../../../../framework/instruction/LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md):
**instrumentation with no ledger, no gate and no dependency.** Its §2 records the finding that
justifies it existing at all — 🔴 **the directive's seven candidate primitives and the scorecard's
eight are not the same list.** The **two primitives with the most recorded outcome-changing
instances** (`verify_the_omitted_clause`, `gate_is_not_quantity`) are **absent from the directive's
list**, and **two of the directive's candidates have no recorded instances at all**. A V0 assembled
from either list alone would be assembled from the wrong evidence.

🟡 **And one of the seven may not be a primitive.** `adversarial_verify` enters
`PROVISIONAL — SUSPECTED DUPLICATE`: LEGEND already ships **`legend-locator-audit`**, a *blind*
adversarial audit in which the auditor never sees the dossier, the reader's name or the conclusions.
That is strictly stronger than the habit, and **proposing a primitive that duplicates a better
existing tool is itself the §26 failure.**

## 4 · What I deliberately did NOT do

- **No canonical propagation.** Seven candidates gated; `BATCH_COMMIT` not run.
- **No unit normalised and no unit repaired**, although the arithmetic is one-sided. The directive
  says verify first; verification returned `UNADJUDICATED`, and *"almost certainly mg/dL"* is not a
  licence to rewrite a source.
- **No re-litigation of Scientist G's science.** `-01`'s conclusion is **correct**; only its
  sufficiency claim on the evidence chain is narrowed, and I said so in those words.
- **No new gate for the hand-back problem** (§2.3). It is a scheduling rule, recorded, not enforced.
- **No contact with any researcher**, and no correspondence drafted or prepared.
- **No `git add -A`.** Every commit staged explicit paths, per the rule adopted after the fourth
  run's incident, with delegates writing into the tree throughout.

## 5 · The rule this run adds

> **A check inherits its confidence from the surface it ran on — so name the surface, and name why
> that surface is the one the claim is about.** The working tree is wrong for verifying a census that
> is already in it, and right for a gate on a file about to be committed. *Neither is the default.*

**Corollary, earned by candidate 7:** 🔴 **an instrument that was pointed at the right place is not
evidence about what it did not report.** A render that restores `±`, `<`, `⁺` and `⁻` on a table row,
and never names that row's unit, says nothing whatever about the unit — and a needle built from the
corrupted layer cannot adjudicate the character it is made of.
