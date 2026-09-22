# COMMIT CANDIDATE — CC-20260922-POSTDIAGNOSIS-WINDOW-01

**Source:** Scientist G, `DOMAIN_G_FILTER_2`
([`postdiagnosis_window_evidence_20260922.md`](../../analysis/postdiagnosis_window_evidence_20260922.md)).
Debt declared by the delegate itself as `FT-132`, nine PMIDs, **none stripped**.
**Change class:** **MINOR** in edit size; 🔴 **it reverses the direction of a conclusion this session
landed and reported**, so the review floor is raised accordingly.
**Target:** `analysis/superior_node_search_20260922.md` §4 · `discovery_ledger_current.md`
`DL-MECH-011` · `claim_registry_current.md` `CLAIM 014` (title-vs-body mismatch, flagged only).
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R3.**
**Proposes:** `D-31` — *"the set of ages an experiment tested is not the window it measured."*

---

## 1 · 🔴 The filter that killed the most candidates is stated more strongly than our own evidence

**Two LEGEND files disagree about the same sentence, and the weaker one is the one being used.**

`superior_node_search_20260922.md` §4 states filter 2 as *"**P1–P5 in the mouse**"* and uses it to
**remove** candidates from the portfolio. But this repository's own locator file for that very paper,
`fulltext_dossiers/PMID42422765_partial_locators.md`, records the authors saying the opposite —
verified verbatim by the Orchestrator:

> *"the inability to assess later intervention likely reflects a combination of **model-specific
> biological constraints and technical limitations, rather than a definitive boundary for
> therapeutic responsiveness**"*

🔴 **So `P1–P5` is the set of ages that were tested, not a window that was measured — and the primary
says so itself.** The distinction is `D-31`, and it matters because four therapeutic arms have been
pruned against it.

⚠️ **This corrects the Orchestrator, not only the file.** I relayed that filter to the Operator as
*"the binding one"* after taking it from a delegate's summary **without checking it against the
repository's own locator file** — the exact failure mode I had corrected in three delegates earlier
the same day. **Recorded as `self`.**

**Proposed:** `superior_node_search_20260922.md` §4 and `DL-MECH-011` restate filter 2 as
*"efficacy demonstrated P0–P5; **upper bound unknown and unmeasurable in this model**, which dies at
3–4 weeks"* — and stop using it to remove candidates until an upper bound exists.

---

## 2 · The mouse→human translation will not carry a number, and that is the finding

`DL-MECH-011`'s chain sentence *"P1–P5 murino ≈ perinatale/tardo-gestazionale umano"* carries **no
method and no source** (`G2-C2`). Given one, via Semple 2013 (PMID 23583307, full text read by the
delegate), the spread is disqualifying:

- 🔴 **One human age maps to two rodent ages a factor of ~2.8 apart** — human term is rat **P7.4** on
  one milestone and rat **P20.4** on another, *from the same paragraph*, which draws the conclusion
  itself: *"equating ages based upon a single milestone or event may lead to misinterpretation."*
- The one sourced interval is already **9 weeks wide** (23–32 gestational weeks).
- **Every anchor available is rat or unqualified "rodent", while `DL-MECH-011`'s window is a mouse
  result** — and the two species do not even share a neural-tube date.
- The one formal model (`translating time`) **explicitly disclaims the postnatal range that matters.**

> **Verdict: too uncertain to support a clinical inference. No number is given.**

What survives is a **direction, not a boundary**: every index sourced places rodent P1–P5 **at or
before human term birth**, none after. ⚠️ But *"the window is closed"* does **not** follow, because
`P1–P5` is not a window. **The correct statement is neither closed nor open: the experiment that
would find the upper bound has never been run, and the model it was defined in cannot run it.**

---

## 3 · 🔴 Nobody has ever reported age at molecular diagnosis in a WWOX cohort

Checked in the two largest retrievable cohorts, both read in body by the delegate, plus one against
its manifest:

| cohort | n | age at molecular diagnosis |
|---|---:|---|
| **Piard 2019** (PMID 30356099) | 20 | 🔴 **not one age** — meticulous about *how* (MLPA 4, aCGH 4, Sanger 2, panel 2, ES 9, GS 1), silent about *when* |
| **Oliver 2023** (PMID 36779245) | 13 + 62 | 🔴 none |
| **Gao 2025** (PMID 40875931) | 50 | 🔴 no locator |

**Query census with a validated control:** `WWOX AND "age at diagnosis"` → **0**, and the
`query_translation` **expanded** (the `wwox protein human` supplementary concept fired), so this is a
parsed query and a real zero — not the parser failure this session proved twice. Control
`WWOX AND (epileptic encephalopathy OR WOREE)` → **72**.

**What IS measured is presentation age**, and it is early: Oliver cohort median **5 weeks** (n=13,
1 day–10 months); Oliver literature median **8.6 weeks** (n=62); Piard mean **1.6 months** (n=20).
Epileptic spasms in **10/13**, median 3.5 months.

> **⇒ The only defensible statement for filter 2 is a one-sided bound: intervention acts at or after
> ≈1–2 months of postnatal life, with NO measured upper bound — because nobody wrote the diagnosis
> date down.**

🔵 **And the observation-floor rule bites here too:** seizure onset is a **presentation** floor, not
disease onset. Development was abnormal **from birth in 11/13**; only 2/13 had no prior concerns —
and Oliver caveats it directly: *"With EIDEE, it is often difficult to ascertain whether early
development is normal prior to seizure onset."* ⭐ **The `ORCHESTRATOR ADDENDUM`'s discriminating
question is answered for the first time, and only at the clinical level:** *acquired* microcephaly in
**10/13** is a genuine earlier-normal, converting a floor into a bound **for head growth and nothing
else** — and ⚠️ *"acquired"* is a label, not a tabulated trajectory; **no birth OFC is printed by
either cohort**. At tissue level the answer stays **no**.

---

## 4 · 🎯 The intersection is not empty — and it is empty exactly where the portfolio needs it

**The compartment the portfolio assumed closed is measurably open.** Sanai 2011 (PMID 21964341,
*Nature* 478:382–6, [DOI](https://doi.org/10.1038/nature10487)) — identity and central time course
**verified by the Orchestrator in the abstract**; the section-level quotes are the delegate's
full-text read:

> *"the infant human subventricular zone and RMS contain an extensive corridor of migrating immature
> neurons **before 18 months of age**… this germinal activity subsides in older children and is
> nearly extinct by adulthood… we describe a major migratory pathway that **targets the prefrontal
> cortex** in humans… These pathways represent **potential targets of neurological injuries affecting
> neonates**."*

10 neurosurgical resections + 50 autopsied brains. DCX⁺ declines **25-fold across the first 6
months**; the RMS is uninterrupted at 1 day, 1 week, 1, 3 and 6 months; a **medial migratory stream
to ventromedial prefrontal cortex is present at 4–6 months and absent at 8–18 months**.

**So, at the median 5-week presentation, human radial glia and tangential neuronal migration are
documented still running — in human tissue.**

| | verdict |
|---|---|
| **IN the intersection** | **myelination** (human *"delayed myelination"* from **day 19**, serial MRI showing progression; rodent MBP/CNPase PND5–21) · **dendritic/neuritic growth** (human 3-decade course; rat MAP2 reduced PND5–21 with neuron number, thickness and layering intact) — this puts a *measured* human time course under `NODE 1`'s filter-2 claim · circuit refinement, weakly |
| 🔴 **OUT for want of a WWOX measurement, NOT for want of plasticity** | synaptogenesis/pruning (**zero** WWOX synaptic data anywhere) · **postnatal SVZ neurogenesis + tangential migration (zero, any species, any age)** |
| **Candidate, deliberately NOT joined** | ventricular-wall radial glia — human limb to ~6 months, WWOX limb in organoids at culture weeks 8–15 **with no gestational mapping.** Joining them would be the error this file exists to avoid |
| **OUT because closed** | cortical projection neurogenesis · cortical layering / callosal assembly |

🔴 **The negative, unsoftened, and both halves must travel together.** The four arms filter 2 is
staked on all act on the progenitor/corticogenesis compartment, and **there the intersection IS
empty — empty on the WWOX side, not the plasticity side.** The human tissue is measurably open to
6–18 months; it is the **WWOX measurement** that does not exist. **The portfolio has been pruning
candidates on a premise it never measured, and the compartment it assumed closed is measurably
open.**

🧪 **One experiment decides it, and it needs no new model, no animal and no molecule:** measure WWOX
transcript, protein and the MYC readout **in human postnatal SVZ tissue across the first 18 months**.
Sanai shows the tissue is obtainable and already banked. **A missing readout, not a missing
experiment.**

---

## 5 · 🔴 `G2-C6` — a rule this session landed is WRONG, and it cost nothing only by luck

I landed, and reported to the Operator, that `get_copyright_status` is a *"one-call pre-test"* for
body availability, **6/6**. **It is not, and the counter-examples run in both directions.**
Re-verified by the Orchestrator today:

| PMID | `is_open_access` | body served by `get_full_text_article`? |
|---|---|---|
| 36779245 | **`false`** | ✅ **yes, in full** |
| 23583307 | **`false`**, `"All rights reserved"` | ✅ **yes, in full** |
| 23616543 · 17368774 | PMCID present | ⛔ **`full_text: ""`** |
| 24369382 | `false` | ⛔ `full_text: ""` — **and I had recorded this as unacquirable from the pre-test alone, never having attempted it** |

> 🔴 **`is_open_access: false` is a LICENCE field, not a retrievability verdict. A PMCID is not a
> body, and the absence of an open licence is not the absence of a body. The pre-test may ORDER
> acquisition attempts; it must never SKIP them.**

⚠️ **Using it to skip would have cost Scientist G its two best sources** — Oliver 2023 and Semple
2013, both flagged `false`, both served in full. My *"6/6"* was scoring a rule whose failures it had
not yet met. **Recorded as `self`, and the `unacquirable` dispositions of `FT-128`/`FT-129`/`FT-130`
are re-labelled: unacquirable *by attempt*, not by licence.**

---

## 6 · Also recorded, not acted on

- **`G2-C3`** — filter 2's *"removes everything acting on neurogenesis"* is **true for cortical
  projection neurogenesis and false for postnatal SVZ neurogenesis.** The two must be named
  separately.
- **`G2-C4`** — **microcephaly denominators disagree ~4×**: Oliver 10/13 (77%) vs Piard 4/20 (20%),
  mean OFC −1.4 SD, and Piard flags it himself. **Neither tabulates a birth OFC.** Flagged, not
  resolved.
- **`G2-C5`** — `CLAIM 014`'s **title** still says *"across species"* while `DL-MECH-027` records the
  same rat allele at PND5–21 showing **no difference** in neuron number, cortical thickness or layer
  distribution. **Heading-versus-body mismatch. Flagged, not resolved** — outside today's authorized
  scope.
- **Source-internal defect:** Piard defines premature death as *"(i.e., before 3 years)"* then gives
  a range to **8 years 11 months**. Recorded as printed.
- ⛔ **The one thing the delegate could not get, and correctly refused to fake:** the
  `translating time` residual error **in days** — Workman 2013 and Clancy 2007 both return
  `full_text: ""` and Europe PMC REST is `connect_rejected`. It explicitly declined to quote a
  cross-species correlation coefficient as a confidence interval for one species pair. **Right call.**
