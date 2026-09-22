# OPERATOR DECISION PACKET — the six gated commit candidates

**Date:** 2026-09-22 · **Prepared by:** Orchestrator · **Status:** 🔴 **NONE PROPAGATED.** Every
candidate below is `PROPOSED — NOT PROPAGATED` and stays that way until the Operator authorises it.
**BLOCK-1:** no molecule, no dose, no route is introduced by any of the six. Nothing here is medical
advice.

**Why this file exists.** These six have been reported as an opaque count for most of the session.
A count is not a decision object. Each row below carries what the canonical file says **now**, what
it would say **after**, what supports the change, what else moves, and what it costs to undo.

**Read this first — the honest summary.** Five of the six **remove or bound an overstatement**; not
one of them adds a new positive finding. **Four are pure epistemic hygiene** and cost the model
nothing but precision. **One cuts against a named therapeutic strategy** and is the only one with a
real decision in it. **One is a single missing tag** that I would accept today on the strength that
its absence already produced a documented error in this session — mine.

---

## §1 · The six, at a glance

| ID | Class | Severity | Direction | Reversibility | Recommendation |
|---|---|---|---|---|---|
| **`CC-…CLAIM011-DOSE-ENDPOINTS-01`** | precision on a canonical numeric endpoint | 🟡 **MEDIUM** | bounds an absolute; **ratio untouched** | trivial (text-only) | 🟢 **ACCEPT** |
| **`CC-…SDR-HOMODIMER-PREMISE-01`** | TAG an uncited assertion | 🔴 **HIGH** | adds a label, deletes nothing | trivial | 🟢 **ACCEPT** |
| **`CC-…VERMIS-HYPOPLASIA-FREQUENCY-01`** | QUALIFY a frequency word | 🟡 **MEDIUM** | bounds *"most cases"* | trivial | 🟢 **ACCEPT** |
| **`CC-…CLAIM025-SIGN-INVARIANCE-01`** | QUALIFY a directionality | 🟡 **MEDIUM** | bounds the **sign**, keeps the ratio architecture | trivial | 🟢 **ACCEPT WITH NARROWING** |
| **`CC-…NMD-PREMISE-WITHDRAWAL-01`** | WITHDRAW an unsourced premise | 🔴 **HIGH** | **re-opens** a closed therapeutic axis | moderate — a closed axis becomes open | 🟡 **ACCEPT WITH NARROWING** |
| **`CC-…TX001-CEILING-REASSESSMENT-01`** | reassess a strategy's expected value | 🔴 **HIGH** | **cuts against `TX-001`** | moderate | 🟠 **DEFER — pending the dependency below** |

---

## §2 · One at a time

### 1 · `CC-20260922-CLAIM011-DOSE-ENDPOINTS-01`

- **SEVERITY** 🟡 MEDIUM. It corrects how a number may be **used**, not whether it is right.
- **CURRENT CANONICAL TEXT** — `claim_registry_current.md`, `CLAIM 011` flag body: *"**LD = 1.23 ×
  10¹¹ vg**, **HD = 2.63 × 10¹¹ vg**"*, stated as bare absolutes; and a `REVIVAL_TRIGGER` telling an
  experimenter to place *"un braccio a dose intermedia fra 1.23 e 2.63 × 10¹¹ vg"*.
- **PROPOSED CHANGE** — keep both numbers, add *"come stampati"*, and record that the primary never
  states the unit convention: bare `vg` on all three surfaces, `hemisphere` never adjacent to a
  dose, **no dose in the Methods at all**, bilateral ICV, 2.0 µL, one injection per hemisphere. So
  the **absolute** dose is uncertain by a factor of 2 — `LD ∈ [1.23, 2.46] × 10¹¹`,
  `HD ∈ [2.63, 5.26] × 10¹¹`. Rewrite the `REVIVAL_TRIGGER` to specify the intermediate arm **as a
  fraction of the primary's HD, never in absolute vg**, and add a second, cheaper trigger: an
  explicit statement of the convention closes the ambiguity with **no experiment**.
- **PRIMARY SUPPORT** — `PMID 42422765` read on all dose-bearing surfaces; `analysis/tx007_dose_unit_forensics_20260922.md`.
- **WHY NEEDED** — an experimenter following the current trigger could choose an absolute dose that
  is **2× off target**. That is an actionable instruction in a canonical file, and it is wrong.
- **🟢 WHAT DOES NOT MOVE, and it is the larger half** — the unit cancels in the ratio:
  `HD/LD = 2.63/1.23 = 2.1382` under **every** permitted reading. Nothing the flag argues depends on
  the ambiguity. *(I record that my own earlier hypothesis — that the unit ambiguity might explain
  the non-monotonicity — was a category error, withdrawn, and independently confirmed as such.)*
- **DEPENDENT SURFACES** — `full_text_queue_current.md` FT entries citing the dose; the dose
  adjudication candidates from 2026-08-26; `therapeutic_routing_and_endpoint_hardening.md`.
- **THERAPEUTIC CONSEQUENCE** — changes **how a dose-finding arm is specified**, not whether one is
  warranted.
- **REVERSIBILITY** — trivial. Text-only; no claim status changes.
- **🟢 RECOMMENDATION: ACCEPT.**

### 2 · `CC-20260922-SDR-HOMODIMER-PREMISE-01`

- **SEVERITY** 🔴 HIGH — not for its size, but because its absence has already caused harm in this
  session.
- **CURRENT CANONICAL TEXT** — `discovery_ledger_current.md:852`, inside a *limitations* bullet:
  *"relSASA e SSE sono calcolati su un **monomero**, ma WWOX **omodimerizza via SDR** e l'interfaccia
  non è modellata"*.
- **PROPOSED CHANGE** — **TAG only.** Mark *"WWOX omodimerizza via SDR"* `PREMISE: UNVERIFIED`.
  Nothing deleted, reversed or re-scored.
- **PRIMARY SUPPORT** — the clause carries **no source, no PMID, no wikilink and no epistemic tag**.
  A census found no primary establishing it.
- **WHY NEEDED — and this is a confession, not an argument.** I read that clause as established,
  wrote it into a structural brief as fact, built an *"interface ⇒ aggregation ⇒ boosting WWOX is
  dangerous"* chain on it, and reported it to the Operator as **the single structural fact that
  would flip the therapeutic sign.** An uncited premise sitting inside a caveat is in the least
  visible place in a document, because a reader checking a limitation is checking the *limitation*,
  not the claim inside it. **The tag is what stops the next actor doing what I did.**
- **DEPENDENT SURFACES** — every downstream file repeating the clause; the `Q230P` structural node;
  `TX-003` proteostasis reasoning.
- **THERAPEUTIC CONSEQUENCE** — none directly. It **prevents** an unsupported one.
- **REVERSIBILITY** — trivial. If a primary surfaces, the tag is removed and a citation replaces it.
- **🟢 RECOMMENDATION: ACCEPT.** This is the cheapest and highest-value of the six.

### 3 · `CC-20260922-VERMIS-HYPOPLASIA-FREQUENCY-01`

- **SEVERITY** 🟡 MEDIUM.
- **CURRENT CANONICAL TEXT** — `discovery_ledger_current.md` L554: *"cerebellar vermis hypoplasia …
  **have been described in most cases**."*
- **PROPOSED CHANGE** — bound the frequency word. The imaging finding is **not** denied; *"most
  cases"* is qualified against a collation whose explicit subject is the radiological spectrum
  (`PMID 38161429`, Battaglia 2023, *Front Pediatr*, [DOI](https://doi.org/10.3389/fped.2023.1301166)).
  🔴 **The receipt is NOT touched** — receipts are append-only and the reading is not in question.
- **PRIMARY SUPPORT** — Riva (`PMID 35573960`, receipt `FTR-20260921-35573960-01`) versus Battaglia
  2023.
- **WHY NEEDED** — a frequency word in a canonical file is read as a prevalence estimate. This one
  was never a prevalence estimate.
- **DEPENDENT SURFACES** — `CLAIM 039`; the cerebellar thread, which this session has expanded
  considerably.
- **THERAPEUTIC CONSEQUENCE** — none. It affects what may be said about **how often**.
- **REVERSIBILITY** — trivial.
- **🟢 RECOMMENDATION: ACCEPT.**

### 4 · `CC-20260922-CLAIM025-SIGN-INVARIANCE-01`

- **SEVERITY** 🟡 MEDIUM.
- **CURRENT CANONICAL TEXT** — `CLAIM 025` carries *"the responding gene set is context-dependent"*
  — a boundary on the **gene set**, not on the **sign** — and `Genotype/model relevance` asserts
  *"cross-context support da dati translazionali multipli"*.
- **PROPOSED CHANGE** — restrict `cross-context support` to the **ratio architecture**, and add an
  evidence boundary recording that the **sign inverts between lineages**: in leucocytes the low
  ratio is the maladaptive state; in `PMID 42589397` a low ratio associates with **worse** DFS in
  BRCA basal-like and HER2-enriched and **better** in Luminal A, Luminal B and OV. Conclusion:
  **`CLAIM 025` describes a *state*, not a *severity*.**
- **PRIMARY SUPPORT** — `PMID 42589397` / `PMC13467099` (`FT-144`).
- **🟢 WHAT MUST NOT BE LOST IN QUALIFYING IT** — the same source **strengthens** the ratio
  architecture: in the combined BRCA model *"the individual genes lost significance"* while the
  ratio did not.
- **🔴 NARROWING I ATTACH AS A CONDITION OF ACCEPTANCE** — the supporting source is
  **same-group, same-dataset, tumour-only, with no perturbation**. It therefore must **not** raise
  the corroboration weight of `CLAIM 025`, and must **not** license any transfer to a non-tumour CNS
  claim. The candidate already says this; I am making it a condition rather than a remark.
- **DEPENDENT SURFACES** — any inference of the form *"lower ratio = worse"*; biomarker-endpoint
  reasoning.
- **THERAPEUTIC CONSEQUENCE** — 🔴 **real.** A biomarker whose sign is not invariant cannot be used
  as a severity read-out, which is how a context-free *"lower = worse"* would have been used.
- **REVERSIBILITY** — trivial in text; the **interpretive** change is the point and is meant to stick.
- **🟢 RECOMMENDATION: ACCEPT WITH NARROWING** (the tumour-only / no-perturbation bound made binding).

### 5 · `CC-20260922-NMD-PREMISE-WITHDRAWAL-01`

- **SEVERITY** 🔴 HIGH — it **re-opens** a therapeutic axis the model had closed.
- **CURRENT CANONICAL TEXT** — `therapeutic_hypotheses_ledger_current.md:216`: *"L'allele di sito
  accettore del genotipo di riferimento (c.1057-2A>G) produce trascritto aberrante **destinato a
  NMD**: up-regolarlo spinge solo più trascritto verso la degradazione, senza proteina utile."*
- **PROPOSED CHANGE** — withdraw Premise A. Line 216 carries **no citation, no locator and no
  epistemic tag** on the NMD clause; its only upstream node, `DL-BIO-002`, states a **disjunction**
  (*"frameshift/PTC → NMD **or** truncated_protein"*), tagged `IPOTESI`, explicitly *"Resta
  in-silico; DATO = RT-PCR wet."* **Line 216 collapsed a hedged disjunction into a categorical
  assertion and dropped the tag, the hedge and the source.**
- **🔴 AND THE STRUCTURAL HALF, which is stronger than the bibliographic one** — exon 9 is the
  **terminal** exon, so no producible transcript from this allele is an EJC-dependent NMD substrate.
  The premise was not merely uncited; it was **architecturally wrong**. *(`DL-MECH-045` reached a
  compatible conclusion for a different reason — right answer, wrong route — and that is recorded.)*
- **WHY NEEDED** — a premise with no source is currently closing a live therapeutic axis
  (non-allele-specific WWOX upregulation). Closing an axis is a decision; this one was never made.
- **DEPENDENT SURFACES** — `DL-BIO-002`; `TX-001`; `HYP-20260709-02`; the query-hygiene rule set.
- **THERAPEUTIC CONSEQUENCE** — 🔴 **the largest in the packet.** Non-allele-specific upregulation
  moves from *closed* to *open and untested*.
- **🔴 NARROWING I ATTACH** — **open is not favourable.** Today's work establishes that the *sign* of
  a non-allele-specific boost is **branch-dependent**: it yields functional protein under impaired
  translation, more aggregate under insolubility, and is actively dangerous under a toxic
  gain-of-function branch that nobody can exclude **because nobody has ever looked in the pellet**.
  The withdrawal must land with that attached, or it will read as an endorsement.
- **REVERSIBILITY** — moderate. Re-closing later requires positive evidence, which is the correct
  asymmetry.
- **🟡 RECOMMENDATION: ACCEPT WITH NARROWING** — withdraw the premise, and land the
  *"open ≠ favourable"* bound in the same edit, not a later one.

### 6 · `CC-20260922-TX001-CEILING-REASSESSMENT-01`

- **SEVERITY** 🔴 HIGH — it **cuts against** a named strategy.
- **CURRENT CANONICAL TEXT** — `therapeutic_strategies_current.md`, `TX-001` Mechanism: *"Exon
  skipping, cryptic acceptors, intron retention or multiple isoforms could emerge."*
- **PROPOSED CHANGE** — record that **exon skipping cannot occur at this allele**: the lesion
  destroys the acceptor of **exon 9**, which is **terminal**; there is no exon 10 to splice to.
  **Four of four published WWOX splice-allele measurements report the one outcome that is
  structurally impossible here**, so the field's prior is not weak evidence — it is **inapplicable**,
  and `TX-001` currently inherits it as if informative. Plus a **conditional** ceiling finding, and
  four design constraints each of which would otherwise force a **false negative**.
- **PRIMARY SUPPORT** — exon architecture (unconditional); the splice-outcome census; Scientist P's
  derivation; the convergent confirmation in §8.
- **WHY NEEDED** — a strategy is currently scored against a prior that cannot apply to it.
- **DEPENDENT SURFACES** — `TX-001`; `tx001_experiment_decision_packet_20260921.md`; the splice
  census; `CC-20260922-SPLICE-ARM-01` and `CC-20260922-EXON7-NATURAL-EXPERIMENT-01`.
- **THERAPEUTIC CONSEQUENCE** — 🔴 real and **bimodal, not negative**: the reassessment narrows what
  `TX-001` can be expected to do while naming the conditions under which it still could.
- **REVERSIBILITY** — moderate. Lowering a strategy's expected value in canon is read by downstream
  actors as a decision.
- **🟠 RECOMMENDATION: DEFER** — and the reason is a dependency, not a doubt. **This candidate
  declares `Depends on: CC-20260922-NMD-PREMISE-WITHDRAWAL-01`.** Its unconditional half (terminal
  exon ⇒ skipping impossible) is, in my judgement, **correct and independently checkable**; I would
  accept that half today. Its **conditional** half inherits the NMD reasoning. Landing #6 before #5
  would put a dependent reassessment into canon ahead of the premise withdrawal it rests on.
  🟢 **If the Operator accepts #5, I recommend accepting #6's unconditional half immediately and
  re-presenting the conditional half as its own candidate.**

---

## §3 · What I am NOT asking for

- No propagation. `BATCH_COMMIT` is not run by this file, and no `*_current.md` is touched by it.
- No new claim. **Not one of the six adds a positive finding** — five remove or bound an
  overstatement and one adds a label.
- No molecule, dose, route or clinical recommendation.
- No re-opening of the withdrawn claim that late scheduled removals necessarily biased the TX-007
  survival comparison. That is not in this packet and is not revived by anything in it.

## §4 · Order of operations, if the Operator accepts

1. **#2 `SDR-HOMODIMER-PREMISE`** — one tag, no dependencies, and it is the one already shown to
   cause harm while untagged.
2. **#1, #3, #4** in any order — independent, text-only, each with its narrowing attached.
3. **#5 `NMD-PREMISE-WITHDRAWAL`** with the *"open ≠ favourable"* bound in the same edit.
4. **#6 unconditional half** only after #5; conditional half re-presented separately.

Gate state at the time of writing: `legend_lint` **PASS**, growth anchors **PASS**
(`unread_premises = 0`), receipt chain **201, tail-anchored**, publication gate **PASS / 0 blocks**.
