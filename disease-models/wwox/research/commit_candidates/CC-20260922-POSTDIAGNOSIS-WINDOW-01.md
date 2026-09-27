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

---

## BATCH DISPOSITION — `BATCH_20260927_001` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** PROPAGATED IN PART

**§1 only.** `discovery_ledger_current.md` `DL-MECH-011`: an append-only rectification restates the filter as "efficacy demonstrated P0–P5; upper bound unknown and unmeasurable in this model, which dies at 3–4 weeks" and stops it being used to remove candidates until an upper bound exists, with the primary's own sentence quoted verbatim from `fulltext_dossiers/PMID42422765_partial_locators.md` (verified present) and `D-31` named. 

**Still owed, so this candidate stays open:** §2 (Semple 2013, no receipt), §3 (cohort ages, partial receipts) and §4 (Sanai 2011, no receipt) are not locator-backed and were deliberately kept out of the ledger text; the `CLAIM 014` title-versus-body mismatch is flagged by the candidate and is not a canonical edit this batch makes. Flagged for Mirror ex-post review under §21e: it reverses the direction of a conclusion an earlier session reported.

## CORRECTION TO THE BATCH DISPOSITION — Mirror ex-post finding F5 (2026-09-27, ACTOR_ID `scientist`), append-only

The block above says "§1 only" and lists §2–§4 as owed, but §1 itself has **two** targets: `DL-MECH-011` **and** `superior_node_search_20260922.md` §4 — the surface that *uses* filter 2 to remove candidates. Only the ledger half was written, so the correction did not reach the pruning surface. Repaired now: filter 2 in `analysis/superior_node_search_20260922.md` (the filter-list item under §4, anchor *"It must have a window that is still open after diagnosis"*) is restated as *"efficacy demonstrated P0–P5; upper bound unknown and unmeasurable in this model, which dies at 3–4 weeks — not to be used to remove candidates until an upper bound exists"*, with the primary's verbatim sentence, `D-31`, and a pointer to the `DL-MECH-011` rectification. No canonical file touched; `superior_node_search_20260922.md` is analysis layer.

**Named residue, not repaired:** the file is a **dated session artefact**, and the ranking it reached (NODE 1 first, four arms pruned) was computed under the old wording. The restatement marks the filter; it does **not** re-derive the pruning or re-rank the portfolio, and the text says so. Re-running that search under the restated filter — in particular re-examining the candidates removed for acting on neurogenesis or corticogenesis — remains owed by this candidate, alongside §2 (Semple 2013, no receipt), §3 (cohort ages, partial receipts) and §4 (Sanai 2011, no receipt). This candidate stays open.

Source: `session_evaluations/2026-09-27_BATCH_20260927_001_mirror_review.md` F5.

## WAVE-2 READINESS (2026-09-27)

**Actor:** ACTOR_ID `scientist`, wave-2 package `development`, branch `task/wave2-development`.
**`context_policy`: `QUESTION_DRIVEN`** for all four sources, declared before any was opened; this session held this candidate and its `BATCH_20260927_001` disposition, so `SOURCE_FIRST` was not available and is not claimed. Questions, narrowly: *does any sourced index map mouse P1–P5 to a human age, and with what spread; does either large cohort report an age at molecular diagnosis; and is the human postnatal periventricular compartment measurably open at the presentation age?*

**Verdict: `CLOSE` — closing status `PROPAGATED`**, with two named residues that are **new work, not this candidate's residue**, and no operation left for the batch.

### 1 · Evidence for the closing status

- **§1 landed** in `BATCH_20260927_001` (`DL-MECH-011` rectification) and its Mirror finding **F5** was repaired the same day on `analysis/superior_node_search_20260922.md` §4. Both are verified present on this head.
- **§2, §3 and §4 — the three sections the disposition listed as *"not locator-backed and deliberately kept out of the ledger text"* — are now locator-backed and written into `DL-MECH-011`**, append-only, as two bullets (see §2 below). That is the whole of what this candidate was still open for.

### 2 · What was done — the missing work itself

1. 🔴 **§2 now has its source and its bound, and the bound is disqualifying for a number: Semple 2013 was read** (`PMID 23583307`, **no prior receipt in this ledger**; new manifest `deepdive_manifests/PMID23583307.json`, schema v2, deep-dive sections **waived by name**, PASS with 5 declared gaps, **5 locators**). The white-matter index reads *"at pnd 1–3 corresponds to 23–32 weeks gestation in human infants, while pnd 7 is analogous to 32–36 weeks"* — nine weeks wide before any species question — and the enzyme indices put human term at rat **7.4 days** on one marker and *"pnd 20.4"* on another, **in the same paragraph**, which draws the conclusion itself: *"equating ages based upon a single milestone or event may lead to misinterpretation"*. Every index is rat or unqualified rodent, and *"Neural tube formation occurs approximately mid-gestation in rodents, on gestational day (gd) 10.5–11 and 9–9.5 in rats and mice, respectively"*. **So no equivalence number enters the ledger; the direction does** — every index places rodent P1–P5 at or before human term, none after.
2. 🔴 **§3's central negative is verified at both cohorts, with its denominator stated: no age at molecular diagnosis is reported.** Piard 2019 gives presentation age — *"was 1.6 months ranging from day 1 to 7 months"* — and names the molecular diagnosis once, without an age, in a sentence about RNA sampling (`PMID30356099.json` **entries 10–11**). Oliver 2023 gives *"Seizures began at a median of 5"* weeks (range 1 day–10 months, mean 9 weeks; literature arm 8.6 weeks) and no diagnosis age (`PMID36779245.json` **entry 27**). ⚠️ **Both negatives are bounded to the served body**: the supplementary tables are not on disk, so this is *"the article does not print it"*, never *"the datum does not exist"*.
3. ✅ **§3's observation-floor half is persisted too**: *"Development was abnormal from birth in 11 of 13 patients, with 9 of 13 patients not meeting any developmental milestones at seizure onset"* and the authors' own caveat *"With EIDEE, it is often difficult to ascertain whether early development is normal prior to seizure onset"* (`PMID36779245.json` **entries 28–29**). Seizure onset is a presentation floor; it is not the start of disease.
4. 🎯 **§4's intersection is verified in human tissue: Sanai 2011 was read** (`PMID 21964341`, **no prior receipt**; new manifest `deepdive_manifests/PMID21964341.json`, 6 locators, PASS with 5 declared gaps) — the DCX⁺ 25-fold decline across the first six months, the depletion *"between 6 to 18 months of age"*, trace levels after 18 months, the uninterrupted RMS at 1 day, 1 week, 1, 3 and 6 months, the MMS present at 4–6 months and absent at 8–18 months, and *"We analyzed serial sections of mouse brains at P4, P8, P16 and P20 and did not detect a MMS"* — **a human compartment no mouse window models**. 🔴 **And the candidate's *"10 neurosurgical resections + 50 autopsied brains"* is NOT in the served body or abstract and is NOT carried**; the body states per-experiment denominators instead (n = 6 autopsies, n = 23 specimens, n = 16 for the decline series). ⚠️ **The bound that travels with all of it: there is no WWOX measurement in this paper at any age. The tissue is open; the gene is unmeasured.**
5. 🔵 **§5's `G2-C6` correction needs nothing from this package and is left alone** — it is already the rule this repository applies (a licence field may order acquisition attempts, never skip them), and this session's own five re-acquisitions were all performed rather than pre-tested away.

### 3 · Applied outside batch (non-canonical, `MINOR`)

`research/discovery_ledger_current.md` `DL-MECH-011` — **two append-only rectification bullets**, one for §2 (the translation carries a direction, not a number) and one for §3/§4 (what is measured of the human side, with the two bounded negatives and the open compartment, each with its locator entries). The earlier `BATCH_20260927_001` bullet is untouched; nothing above it is rewritten. **No canonical file touched.**

### 4 · No operation list, and why

This candidate leaves the batch nothing: §1 is propagated, §2–§4 are applied outside batch on a research-layer file, and the two remaining items are **not propagatable as written**:

- ⏳ **Re-running the pruning of `superior_node_search_20260922.md` under the restated filter** — named by the Mirror F5 correction as owed. It is a **new search task with its own budget**, not an edit: the ranking was computed under the old wording and re-deriving it means re-examining the candidates removed for acting on neurogenesis or corticogenesis. Recorded, not attempted here.
- ⏳ **`CLAIM 014`'s title-versus-body mismatch (`G2-C5`)** — canonical, and this candidate flags it deliberately without proposing an edit. It needs its own candidate and its own review floor, because the title says *"across species"* while `DL-MECH-027` records the same rat allele showing no difference in neuron number, cortical thickness or layer distribution.

### 5 · Receipts and pending

Four pending receipt JSONs, **`fulltext_receipts.py record` deliberately NOT run** (hash chain, parallel packages): `receipts_pending/development_23583307_1.json` (`FTR-20260927-23583307-01`, `first_read`), `development_21964341_1.json` (`FTR-20260927-21964341-01`, `first_read`), `development_30356099_1.json` (`FTR-20260927-30356099-03`) and `development_36779245_1.json` (`FTR-20260927-36779245-05`) — all `partial_fulltext_read`.

🔴 **Evidence locality, and one case where no free route reproduces a declared digest.** `PMID30356099_Piard2019_EPMC.xml` was absent and was re-acquired from Europe PMC, reproducing `885c00f9…` exactly. `PMID36779245_Oliver2023_PMC.xml` — the artefact behind twenty persisted Oliver locators — is absent and **no free route reproduces its digest today**: efetch gives `780f42de…`, Europe PMC `fullTextXML` `60b5a77b…`, PMC OAI `c1e3310c…`. The efetch serialisation was therefore declared as a **second** `article_text` artefact with its recipe and the three new locators bound to it; the twenty earlier locators were left pointing where they always pointed. **Nothing was re-bound and no digest overwritten** — which is the rule, and it is why this candidate's Oliver evidence now stands on a surface a fresh checkout can fetch.

**DEFAULTS_TAKEN.** (1) *Two of the four sources had no receipt at all* → read them partially, under a declared question, and wrote manifests with the deep-dive sections waived **by name** rather than filled; safe because the waiver states what was not done and the locators verify against a fingerprinted artefact. (2) *A figure in §4 could not be located in the source* → dropped it and recorded the per-experiment denominators the body does print, rather than carrying an unverifiable total. (3) *The declared Oliver artefact is unreproducible* → declared a new artefact beside it instead of re-pointing the old locators to a surface they were never taken from. (4) *The re-ranking §1 owes is a task, not an edit* → recorded as a new task with one line, not silently carried inside this candidate. **STOP_LOG: empty.**

## BATCH DISPOSITION — `BATCH_20260927_003` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** **PROPAGATED** — `BATCH_20260927_003` (MINOR, MANUAL, `WM_v6.0` → `WM_v6.1`).

Closed as **PROPAGATED**: §1 landed in `BATCH_20260927_001` and its Mirror finding F5 was repaired the same day; §2–§4 are now locator-backed and written into `DL-MECH-011` as two append-only bullets, with two first-read manifests created (`PMID 23583307`, `PMID 21964341`). The candidate's *"10 resections + 50 autopsied brains"* figure is **not** carried — it is not in the served body — and the nine-week-wide translation index yields a **direction, not a number**. The two residues named in its §4 are new tasks, not this candidate's residue: the re-ranking of `superior_node_search_20260922.md` under the restated filter, and `CLAIM 014`'s title-versus-body mismatch, which needs its own candidate and review floor.

**Mirror ex-post review due** under §21e — see the batch report at `session_evaluations/2026-09-27_BATCH_20260927_003.md`.
