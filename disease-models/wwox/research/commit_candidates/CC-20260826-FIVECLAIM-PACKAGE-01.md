# COMMIT CANDIDATE — the five-claim seizure contradiction: bounded reconciliation package

**Candidate ID:** CC-20260826-FIVECLAIM-PACKAGE-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** finalization. Consolidates
[`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md) into a bounded,
per-claim, review-routable package. **Supersedes** the CLAIM 037 section of
[`CC-20260825-ADVERSARIAL-FALSIFICATION-01`](CC-20260825-ADVERSARIAL-FALSIFICATION-01.md) and
extends [`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md).
**Change class:** 🔴 **MAJOR** · **Locator audit trigger:** ✅ **REQUIRED** — see
[`CC-20260826-LOCATOR-PACKET-01`](CC-20260826-LOCATOR-PACKET-01.md)
**Canonical targets:** `CLAIM 004` · `CLAIM 005` · `CLAIM 011` · `CLAIM 016` · `CLAIM 037` ·
new `CLAIM 040`
**Target WM:** current at BATCH_COMMIT time; rebase required
**Batch gate:** intentionally untouched

---

## 0. The bounded object

**Nine distinct things have been carried in the word "seizure".** They have different evidence,
different animals and different fates. The package repairs the claims **without merging the nine**.

| Axis | State | Best evidence | Animal |
|---|---|---|---|
| `MEASURED_SWD` | ✅ `DATO` | 30× elevation, `p<0.0001`, rescued to `ns` | `Wwox`-null mouse, P14–21 |
| `MEASURED_SPIKE_RATE` | ⚠️ `UNRESOLVED` | complete separation, printed `p=0.2000` at the rank-test floor | same |
| `MEASURED_FIRING` | ✅ `DATO` | ~6× firing rate, rescued to `ns` vs WT | `Wwox`-null mouse, P18–21 |
| `RACINE_SEVERITY` | ✅ `DATO` | pilocarpine + PTZ, 50 % → status epilepticus, SE absent in `+/+` and `+/−` | `Wwox`-null mouse (Hsu allele) |
| `SEIZURE_SUSCEPTIBILITY` | ✅ `DATO` | provoked threshold lowered vs both control genotypes | same |
| `SPONTANEOUS_SEIZURES` | ◐ `DATO`, weak method | *"commonly observed after postnatal day 12"*, opportunistic husbandry + one video | same |
| `EPILEPTOGENESIS` | 🔴 **`UNRESOLVED` — never measured in any WWOX model** | — | — |
| `HUMAN_ABSENCE_SEIZURE_INFERENCE` | ⚠️ `INFERENZA` | SWD is an absence-type signature; WOREE lists six seizure types | mouse → human |
| `GENE_THERAPY_RESCUE` | ✅ `DATO` | genotype → phenotype → rescue-to-`ns`, twice independently | `Wwox`-null mouse |

🔴 **`EPILEPTOGENESIS` is the axis that resolves the whole contradiction.** It denotes the
*process* by which a brain acquires an enduring predisposition to spontaneous recurrent seizures.
Measuring it requires observing the transition — a latent period, a documented conversion, or a
manipulation that shifts it. **No WWOX study has done this.** Cheng 2020 uses the word twice, both
times for *provoked seizure susceptibility at a time point*; Obeid 2026 does not use it at all
(**zero occurrences**). The prohibition in `CLAIM 005` and the data in `CLAIM 004/011/016` have
been talking past each other because of one word.

---

## 1. Per-claim repair

### `CLAIM 004` — *AAV9-WWOX neuron-targeted rescue shows multi-domain in vivo improvement* · `consolidated baseline`

- **CURRENT_TEXT:** *"…recupera sopravvivenza/letalità postnatale, crescita, ipoglicemia, **crisi**,
  atassia, mielinizzazione…"*
- **WHAT_IS_FALSE:** nothing.
- **WHAT_IS_TOO_BROAD:** *"crisi"* unqualified. The rescued electrophysiological endpoint in its
  source is **cell-attached firing rate**, not a scored seizure. Spontaneous behavioural seizures
  in this animal were never scored by a protocol.
- **WHAT_IS_NOMENCLATURE:** *"recupera … letalità"*. Verified at the panel: the curve reaches
  **0 % by ~330 d** after holding ≈93 % to ~270 d. That is a **large extension, not survival**.
- **WHAT_IS_MEASURED:** ~6× firing-rate elevation in KO, no significant difference between rescued
  and WT (Fig 3A–B); survival extension `p<0.0001`.
- **MINIMUM_REPAIR:** replace *"crisi"* with *"ipereccitabilità neuronale misurata come frequenza
  di scarica in cell-attached"*; qualify *"letalità"* as *"estensione della sopravvivenza"* with
  the curve, not the word.
- **SOURCE:** `PAPER 005` — PMID 34747138 · **LOCATOR:** L-004-a, L-004-b
- **CHANGE_CLASS:** **MODERATE** (qualification of a baseline, no reversal)

### `CLAIM 005` — *Reduced GABAergic interneurons and glial activation in WWOX-KO* · `consolidated baseline`

- **CURRENT_TEXT:** *"**No canonical statement may describe a Wwox-null mouse as showing
  epileptogenesis.** Whether the mouse lacks the phenotype or dies before expressing it is open
  and testable…"*
- **WHAT_IS_FALSE:** the second sentence. **It is not open.** Cheng 2020 observes spontaneous
  seizures from P12 — inside the null's lifespan — and Obeid 2026 records SWDs at P14–21.
- **WHAT_IS_TOO_BROAD:** the prohibition. It bans a **class of fact about an animal**, and three
  claims in its own registry state that fact.
- **WHAT_IS_NOMENCLATURE:** 🔴 **the whole collision.** Read strictly, "epileptogenesis" is a
  process nobody has measured, so the prohibition is *accidentally correct and wrongly scoped*.
- **WHAT_IS_MEASURED:** PV⁺/NPY⁺ counts and IBA1/GFAP area fractions at two weeks. **Unchanged and
  untouched by this repair.**
- **MINIMUM_REPAIR:** retarget, do not delete →
  *"No canonical statement may assert EPILEPTOGENESIS — the process of acquiring an enduring
  predisposition to spontaneous recurrent seizures — in any WWOX model, because no study has
  measured that process. Measured seizure and epileptiform phenotypes ARE recordable and are
  recorded: see CLAIM 004, CLAIM 011, CLAIM 016, CLAIM 037. PMID 19936220 remains free of any
  seizure measurement; that is a statement about that paper, not about the animal."*
  **Delete** the "dies before convulsing" sentence.
- **SOURCE:** `PAPER 006` — PMID 30290271; falsifiers `PAPER 019`, `PAPER 011`
- **LOCATOR:** L-005-a, L-016-a, L-011-a
- **CHANGE_CLASS:** 🔴 **MAJOR** — rewrites a canonical prohibition inside a baseline claim

### `CLAIM 011` — *AAV9-hSynI-hWWOX: dose-dependent durable rescue … inclusi ECoG/SWD* · `flagged for review`

- **CURRENT_TEXT:** *"…gliosi, ipereccitabilità / SWD su ECoG (spike-wave discharges — surrogato
  elettrofisiologico delle crisi)"*; flag defers ECoG to a fuller reading.
- **WHAT_IS_FALSE:** nothing.
- **WHAT_IS_TOO_BROAD:** *"surrogato elettrofisiologico delle crisi"*. **SWD is an absence-type
  signature**; it is not a surrogate for the tonic, clonic, tonic-clonic, myoclonic or spasm
  components of WOREE. And *"dose-dependent"* is separately contradicted — see
  [`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md).
- **WHAT_IS_NOMENCLATURE:** "dose-dependent" describes a continuum where the panel shows a
  threshold — already flagged; unchanged here.
- **WHAT_IS_MEASURED:** SWD/animal, `****` WT-vs-KO and `****` KO-vs-HD, `ns` WT-vs-HD, n=5/group,
  continuous 24/7 ECoG P14→P21, blinded reader. Spike rate **not tested** (see below).
- **MINIMUM_REPAIR:** record that the ECoG domain **is** now adjudicated at panel level; narrow
  *"surrogato delle crisi"* to *"correlato elettrografico di tipo assenza"*. **Flag stays** — it
  concerns the dose axis.
- **SOURCE:** `PAPER 011` — PMID 42422765 · **LOCATOR:** L-011-a, L-011-b, L-011-c
- **CHANGE_CLASS:** **MODERATE**

### `CLAIM 016` — *GSK3β hyperactivation may contribute to seizure susceptibility* · `in observation`

- **CURRENT_TEXT:** *"In Wwox-null mice, GSK3β is elevated …, and lithium significantly suppresses
  PTZ-induced seizure susceptibility."*
- **WHAT_IS_FALSE:** nothing. Its lithium boundary is already correct and hard-won.
- **WHAT_IS_TOO_BROAD:** nothing new.
- **WHAT_IS_NOMENCLATURE:** its source calls the phenotype *"enhanced epileptogenesis"*. That word
  is **not licensed** — what was measured is provoked susceptibility at a time point.
- **WHAT_IS_MEASURED:** Racine severity after pilocarpine and PTZ; 50 % of KO reaching status
  epilepticus, **SE absent in `+/+` and `+/−`**; spontaneous seizures *"commonly observed after
  postnatal day 12"* by husbandry observation + one video.
- **MINIMUM_REPAIR:** add a cross-reference to `CLAIM 037`/`CLAIM 040`; record that Cheng 2020 is
  the **only** primary source for spontaneous behavioural seizures in a `Wwox`-null mouse and that
  its observation is **a floor, not a rate**; record that its "epileptogenesis" is the source's
  word, not a measurement.
- **SOURCE:** `PAPER 019` — PMID 32000863 · **LOCATOR:** L-016-a, L-016-b
- **CHANGE_CLASS:** **MINOR**

### `CLAIM 037` — *…and it is explicitly absent in Wwox-null mice* · `in observation`

- **CURRENT_TEXT (Title):** *"The seizure phenotype of the Wwox literature is a rat `lde/lde`
  phenotype, electrographically documented, and it is explicitly absent in Wwox-null mice"*
- **WHAT_IS_FALSE:** 🔴 **the final clause.** Falsified by four independent datasets, the earliest
  from **2020**: Cheng 2020 (spontaneous + provoked, behavioural), Repudi 2021 (cell-attached),
  Obeid 2026 (continuous ECoG), and — in a *different* mouse genotype — Hussain 2023 (video-EEG).
  Also false: *"i topi potrebbero morire prima di convulsionare"*.
- **WHAT_IS_TOO_BROAD:** *"the seizure phenotype … is a rat phenotype"*. True only of the
  **audiogenic/kindling** phenotype.
- **WHAT_IS_NOMENCLATURE:** *"non hanno epilessia riportata"* — accurate as of a **2009 literature
  survey over four papers none of which recorded EEG**. `NOT_REPORTED ≠ ABSENT`.
- **WHAT_IS_MEASURED:** the entire rat `lde/lde` dataset — 95 % audiogenic (female-only), 34 %
  spontaneous floor, interictal spikes, CA1/amygdala vacuolisation. **Untouched.**
- **MINIMUM_REPAIR:** Title → *"Seizure-related phenotypes in WWOX rodent models are documented in
  the rat lde/lde, in the Wwox-null mouse (behaviourally since 2020, electrographically since
  2026) and in the P47T knock-in mouse (video-EEG, adult); the audiogenic kindling phenotype
  remains rat-specific."* Delete the false clause and the "dies first" sentence; add the
  `NOT_REPORTED ≠ ABSENT` record; retarget transferability (T2 electrographic mouse null, T2
  behavioural conditionals, **T3 audiogenic rat only**).
- **SOURCE:** `PAPER 058`, `PAPER 059`; falsifiers `PAPER 019`, `PAPER 005`, `PAPER 011`, `PAPER 007`
- **LOCATOR:** L-037-a, L-016-a, L-005-a, L-011-a, L-007-a
- **CHANGE_CLASS:** 🔴 **MAJOR** — a `DATO` claim's headline deleted as false

### `CLAIM 040` — **new**

- **Proposed text:** *"Neuronal restoration of WWOX suppresses spike-wave discharges in the
  `Wwox`-null mouse to a level statistically indistinguishable from wild type."*
- `DATO` · P1/P7 · T2 · `in observation` · Source `PAPER 011`, Figure 7E
- **Evidence boundary:** n=5/group; **single-channel** montage — bilateral synchrony not
  resolvable, unlike `PAPER 007`'s four-channel design; **no post-surgical recovery interval**;
  P14–P21 only; the interictal-spike endpoint of the same figure is **not tested**; SWD is an
  absence-type signature and does not represent WOREE's convulsive types.
- **Rationale:** the only genotype→phenotype→rescue triad on a seizure-adjacent endpoint in the
  corpus, currently a sub-clause of a claim flagged for an unrelated reason.
- **CHANGE_CLASS:** **MINOR (addition)**

---

## 2. 🔴 Guardrail check — does the repair create a new contradiction?

Run against every prohibition and boundary the registry holds. **The screen that found this
contradiction was re-run against the proposed text.**

| Guardrail | Interaction | Verdict |
|---|---|---|
| **`CLAIM 015`** — *"'developmentally pre-wired' must not be read as 'prenatally demonstrated'"* | The repair adds **postnatal** electrographic and behavioural findings (P12–P21, adult). It makes **no prenatal claim** and does not license reading any of it as prenatal. `CLAIM 015`'s Summary already includes *"early network hyperexcitability"* among its convergent strands — the repair **supplies the measurement** that phrase was resting on, and narrows it to postnatal. | ✅ **compatible, and strengthens 015's boundary** |
| **`CLAIM 015`'s form** | 015 constrains an *inference from a phrase*; the repaired `CLAIM 005` now does the same (constrains asserting a *process*) instead of banning a *class of fact*. | ✅ **the repair adopts 015's shape** |
| **`CLAIM 038`** — BUN/creatinine, one explanation being hypercatabolism from *"crisi ripetute"* | Rat-scoped. The repair does not extend repeated convulsions to the mouse null; mouse evidence is SWD, provoked seizures and unquantified spontaneous events. | ✅ no new conflict |
| **`CLAIM 031`** — *"seizure control does not rescue development"* | Human, anti-seizure **drugs**. `CLAIM 040` is murine **gene therapy** on an electrographic endpoint. Distinct proposition; the repair explicitly does **not** claim developmental rescue. | ✅ no conflict |
| **`CLAIM 022`** — *"should not be modeled as purely postnatal seizure-driven deterioration"* | ⚠️ **Closest call.** The repair adds postnatal seizure evidence and could be misread as re-centring the model on postnatal seizures. **Mitigation written into the repair:** `CLAIM 040`'s boundary states the rescue is on an *electrographic* endpoint only, and `CLAIM 031` is cross-linked so seizure control is never counted as developmental protection. | ✅ compatible **with the mitigation**; ❌ without it |
| **`CLAIM 032`** — haploinsufficiency not deleterious | The repair adds no `Wwox^+/−` electrophysiology, because **none exists**. It records the gap. | ✅ no conflict |
| **`CLAIM 016`'s lithium boundary** | Untouched and re-cross-referenced. | ✅ preserved |

🔴 **One guardrail the repair must ADD, or it creates the next contradiction:** a statement that
**`EPILEPTOGENESIS` remains unmeasured in every WWOX model**, placed in the repaired `CLAIM 005`.
Without it, the deletion of the old prohibition leaves the process claim unguarded, and the
retargeted prohibition is the only thing standing between the corpus and the exact import the
original sentence existed to prevent.

---

## 3. Minimum canonical delta — six edits, **not applied**

| # | Target | Edit | Class |
|---|---|---|---|
| Δ1 | `CLAIM 037` Title | delete *"and it is explicitly absent in Wwox-null mice"*; replace per §1 | 🔴 MAJOR |
| Δ2 | `CLAIM 037` Evidence boundary | `NOT_REPORTED ≠ ABSENT` record; delete *"dies before convulsing"*; retarget transferability | 🔴 MAJOR |
| Δ3 | `CLAIM 005` Evidence boundary | **retarget** the prohibition to the process; delete the "open question"; add the unmeasured-epileptogenesis guardrail | 🔴 MAJOR |
| Δ4 | `CLAIM 011` | narrow *"surrogato delle crisi"* → absence-type electrographic correlate; record ECoG panel adjudication; **flag stays** | MODERATE |
| Δ5 | `CLAIM 004` | qualify *"crisi"* → cell-attached firing rate; qualify *"letalità"* → survival extension | MODERATE |
| Δ6 | `CLAIM 016` | cross-reference; record Cheng 2020 as sole primary and its floor-not-rate status | MINOR |
| Δ7 | new `CLAIM 040` | add per §1 | MINOR |

**Unchanged and explicitly listed:** the entire rat dataset in `CLAIM 037`; `CLAIM 005`'s PV/NPY
and glial measurements; `CLAIM 016`'s lithium non-specificity boundary; `CLAIM 011`'s dose flag;
`CLAIM 004`'s comparator boundary.

---

## 3b. The delta as literal strings — re-derived 2026-08-26, verified against the registry

Every `BEFORE` below was read back out of `claim_registry_current.md` at re-derivation time, not
transcribed from an earlier draft.

### Δ1 · `CLAIM 037` Title · 🔴 MAJOR · `L-037-a/b/c`, `L-016-a`, `L-011-a`, `L-007-a`

**BEFORE**
> The seizure phenotype of the Wwox literature is a rat `lde/lde` phenotype, electrographically
> documented, **and it is explicitly absent in Wwox-null mice**

**AFTER**
> Seizure-related phenotypes in WWOX rodent models are documented in the rat `lde/lde`, in the
> `Wwox`-null mouse (behaviourally since 2020, electrographically since 2026) and in the `P47T`
> knock-in mouse (video-EEG, adult); the audiogenic kindling phenotype remains rat-specific

**WHY_MINIMUM** — one clause is deleted and one is added. The rat attribution, which is true of
the **audiogenic/kindling** phenotype, is retained and narrowed rather than removed.

### Δ2 · `CLAIM 037` Evidence boundary · 🔴 MAJOR · `L-037-a/b/c`

**BEFORE** *(opening, and the clause that must go)*
> 🔴 **I topi Wwox-null non hanno epilessia riportata** — affermato tre volte in PMID 19500159 e
> formalizzato in Table 2 … Gli autori lasciano aperta la spiegazione (**i topi potrebbero morire
> prima di convulsionare**) …

**AFTER**
> 🔴 `NOT_REPORTED ≠ ABSENT`. PMID 19500159 writes *"has been **reported**"* and *"no
> **detection**"*, and its Table 2 `Epilepsy` row is empty for **both** mouse columns under
> footnotes naming Aqeilan 2007/2008/2009 and Ludes-Meyers 2007 — **four papers, none of which
> recorded EEG.** The negative is a survey artefact of its sources, not a measurement, and the
> source says so. The die-first explanation is **withdrawn**: Cheng 2020 observes spontaneous
> seizures from P12, inside the null's lifespan.

**WHY_MINIMUM** — 🔴 **the hedge is restored, not invented.** The source was already careful; the
registry hardened it. Only the hardened words change.

### Δ3 · `CLAIM 005` Evidence boundary · 🔴 MAJOR · `L-037-a/b/c`, `L-016-a/b`, `L-011-a`

**BEFORE**
> **No canonical statement may describe a Wwox-null mouse as showing epileptogenesis.** Whether
> the mouse lacks the phenotype or dies before expressing it is open and testable: the earliest
> rat seizure onset (day 16) already exceeds the entire lifespan of the mouse null.

**AFTER**
> **No canonical statement may assert `EPILEPTOGENESIS` — the process of acquiring an enduring
> predisposition to spontaneous recurrent seizures — in any WWOX model, because no study has
> measured that process.** Measured seizure and epileptiform phenotypes **are** recordable and are
> recorded: see `CLAIM 004`, `CLAIM 011`, `CLAIM 016`, `CLAIM 037`, `CLAIM 040`. PMID 19936220
> remains free of any seizure measurement; that is a statement about that paper, not about the
> animal.

**WHY_MINIMUM** — the prohibition is **retargeted from an entity to a process**, which preserves
the guard it was built for and removes the ban on measured fact. Deleting it outright would
discard the guard.

### Δ4 · `CLAIM 011` Summary · MODERATE · `L-011-a/b/c`

**BEFORE**
> … ipereccitabilità / SWD su ECoG (spike-wave discharges — **surrogato elettrofisiologico delle
> crisi**).

**AFTER**
> … ipereccitabilità / SWD su ECoG (spike-wave discharges — **correlato elettrografico di tipo
> assenza**; non un surrogato dei tipi convulsivi tonico, clonico, tonico-clonico, mioclonico o
> degli spasmi che compongono lo spettro WOREE).

**WHY_MINIMUM** — three words replaced. The measurement, the statistics and the dose flag are
untouched.

### Δ5 · `CLAIM 004` Summary · MODERATE · `L-004-a/b`

**BEFORE**
> … singola ICV neonatale (P0) di AAV9-hSynI-WWOX (murino o umano, equivalenti) **recupera
> sopravvivenza/letalità postnatale**, crescita, ipoglicemia, **crisi**, atassia, mielinizzazione …

**AFTER**
> … singola ICV neonatale (P0) di AAV9-hSynI-WWOX **estende la sopravvivenza** (≈93 % a 270 giorni,
> poi in discesa; `p < 0.0001` contro il null non trattato — **non** sopravvivenza pari al WT),
> crescita, ipoglicemia, **ipereccitabilità neuronale misurata come frequenza di scarica in
> cell-attached**, atassia, mielinizzazione …

**WHY_MINIMUM** — two words are qualified. *"crisi"* is replaced by **what was actually measured**;
*"recupera letalità"* by **what the curve shows**. No domain is removed.

### Δ6 · `CLAIM 016` · MINOR · `L-016-a/b`

**AFTER (addition only)** — cross-reference `CLAIM 037` / `CLAIM 040`; record that Cheng 2020 is
the **only** primary source for spontaneous behavioural seizures in a `Wwox`-null mouse and that
its observation is **a floor, not a rate** (husbandry observation + one video, no denominator);
record that its word *"epileptogenesis"* is the source's and is **not licensed** by what it
measured. **Nothing is removed.**

### Δ7 · new `CLAIM 040` · MINOR · `L-011-a/b/c`

As §1. Status `in observation`.

---

## 3c. 🔴 Re-checked: does the AFTER state keep the six things separable?

| Axis | Where it lives after the delta | Distinct? |
|---|---|---|
| `epileptogenesis` terminology | Δ3 — named as a **process** and declared unmeasured everywhere | ✅ |
| spontaneous seizures | Δ6 — Cheng 2020, floor-not-rate, method named | ✅ |
| SWD | Δ4 + Δ7 — absence-type electrographic correlate, explicitly **not** a convulsive surrogate | ✅ |
| seizure susceptibility | Δ6 — provoked, Racine, SE absent in `+/+` and `+/−` | ✅ |
| EEG abnormality | Δ1 + Δ7 — interictal spike rate kept separate from SWD, and marked `UNRESOLVED` | ✅ |
| gene-therapy rescue | Δ5 + Δ7 — firing rate (`CLAIM 004`) and SWD (`CLAIM 040`) named separately | ✅ |

**No headline in the AFTER state upgrades `NOT_REPORTED` to `ABSENT`.** Δ1 removes the only one
that did; Δ2 replaces it with the source's own hedge; Δ3 forbids the process claim in both
directions.

### Interaction re-check

| Guardrail | After the delta |
|---|---|
| `CLAIM 015` | ✅ Δ3 **adopts 015's shape** — constrains an assertion, not a class of fact about an animal |
| `CLAIM 022` | ⚠️ **compatible only with the mitigation.** Δ7's boundary must state the endpoint is electrographic, and Δ7 must cross-link `CLAIM 031`. Without both, the delta could be read as re-centring the model on postnatal seizures |
| `CLAIM 031` | ✅ different species and intervention; Δ7 cross-links it so seizure control is never counted as developmental protection |
| `CLAIM 032` | ✅ untouched. Δ6 records that SE was **absent in `+/−`**, which is the only `Wwox^+/−` seizure datum that exists and is **consistent** with 032 |
| `CLAIM 038` | ✅ rat-scoped; the delta extends no convulsion claim to the mouse null |
| `CLAIM 040` | ✅ new; its boundary carries the single-channel, no-recovery-interval and absence-type limits |

---

## 4. What the package refuses to do

- **Does not merge the nine axes.** Each repair names which axis it touches.
- **Does not generalise SWD** to convulsive seizure types.
- **Does not claim epileptogenesis** anywhere — that is the point of Δ3.
- **Does not transfer the `P47T` phenotype to the null**, or the null's to `P47T`.
- **Does not lift `CLAIM 011`'s flag.**
- **Does not upgrade `CLAIM 016` past `in observation`.**

---

## 5. Review required

🔴 **Operator authorization**, MAJOR on three counts (Δ1, Δ2, Δ3).
🔴 **Locator audit REQUIRED before the MAJOR edits** —
[`CC-20260826-LOCATOR-PACKET-01`](CC-20260826-LOCATOR-PACKET-01.md) is built for a reviewer who
must not inherit this candidate's conclusions.
