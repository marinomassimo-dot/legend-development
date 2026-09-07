# COMMIT CANDIDATE — FIVECLAIM final hardening: the delta set is not closed under the proposition it repairs

**Candidate ID:** CC-20260826-FIVECLAIM-HARDENING-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** final hardening of [`CC-20260826-FIVECLAIM-PACKAGE-01`](CC-20260826-FIVECLAIM-PACKAGE-01.md)
for independent Mirror review. **Does not supersede it** — it supplies the review fields the package
does not carry, and adds three deltas the package's target list omits.
**Change class:** 🔴 **MAJOR** (inherits the package's Δ1/Δ2/Δ3, and extends the target set)
**Locator audit trigger:** ✅ **REQUIRED** — [`CC-20260826-LOCATOR-PACKET-01`](CC-20260826-LOCATOR-PACKET-01.md)
groups A and B cover every new delta below; **no new locator is needed**
**Canonical targets:** the package's six · **plus** `working_model_current.md` claim mirror ·
`meta_gaba_paradox_current.md` · `discovery_ledger_current.md` `DL-MECH-075` ·
`dismissal_ledger_current.md` `DIS-011`
**Base head:** `ccddc28939234ad4fe29c417935a0dbe11de86d0` (branch `lettore`)
**Batch gate:** intentionally untouched

---

## 0. 🔴 The finding that makes this candidate necessary

The package repairs the **claim registry**. The falsified proposition — *"seizures are absent in
`Wwox`-null mice"* — lives on **seven** canonical surfaces. The package targets **two of them, and
one of those only partially.**

Enumerated by literal string sweep over the canonical tree, excluding
`research/commit_candidates/` (which is where the repair documents live and would otherwise
match themselves):

```bash
/usr/bin/grep -rn -Ei "non hanno epilessia|show no epilepsy|explicitly absent" \
  disease-models/wwox/registries/ disease-models/wwox/meta/ disease-models/wwox/analysis/ \
  disease-models/wwox/therapeutics/ disease-models/wwox/biomarker_endpoint/ \
  disease-models/wwox/disease_model.md disease-models/wwox/mission.md \
  disease-models/wwox/research/discovery_ledger_current.md \
  disease-models/wwox/research/dismissal_ledger_current.md \
  disease-models/wwox/research/research_lines_current.md \
  disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md
```

⚠️ **`grep` on this machine is `ugrep`**, which honours ignore-files. `/usr/bin/grep` is used
explicitly above so the population is the one named on the command line, not a filtered subset.
Both implementations were run and returned the same set here.

| # | Surface | Locus | The proposition, as written | Form | In the package? |
|---|---|---|---|---|---|
| 1 | `claim_registry_current.md` | `CLAIM 037` **Title** (line 663) | *"and it is **explicitly absent** in Wwox-null mice"* | 🔴 `ABSENT` | ✅ Δ1 |
| 2 | `claim_registry_current.md` | `CLAIM 037` **Evidence boundary** (line 672) | *"I topi Wwox-null non hanno epilessia **riportata**"* + *"potrebbero morire prima di convulsionare"* | `NOT_REPORTED` (correctly hedged) + die-first | ✅ Δ2 |
| 3 | `claim_registry_current.md` | `CLAIM 005` **Evidence boundary** (line 114) | *"PMID 19500159 states … that Wwox-null mice **show no epilepsy**"* | 🔴 `ABSENT` | ❌ **NO** — Δ3 begins at the *next* sentence |
| 4 | `working_model_current.md` | claim mirror, row 037 (line 185) | *"and is **explicitly absent** in Wwox-null mice"* | 🔴 `ABSENT` | ❌ **NO** — the package declares no working-model target |
| 5 | `meta_gaba_paradox_current.md` | provenance directive (lines 19–20) | *"they are **explicitly ABSENT** in Wwox-null mice"* … *"Wwox-null **mice show no epilepsy**"* | 🔴 `ABSENT` ×2, **inside a reader-facing instruction** | ❌ routed **elsewhere** — [`CC-20260826-PROVENANCE-01`](CC-20260826-PROVENANCE-01.md) §E, as **MINOR** |
| 6 | `discovery_ledger_current.md` | `DL-MECH-075` headline (line 1973) | *"Il terminale dichiara che i topi Wwox-null **NON hanno epilessia**"* | 🔴 `ABSENT` in the headline; the body quotes the source correctly | ❌ **NO** — named in **zero** candidates |
| 7 | `dismissal_ledger_current.md` | `DIS-011` verdict (line 200) | *"rigettata, e non per assenza di prova ma per **prova contraria**"* | 🔴 survey silence promoted to **contrary evidence** | ❌ **NO** — named in **zero** candidates |

**Measured, not asserted:**

```bash
/usr/bin/grep -rln "DIS-011"      disease-models/wwox/research/commit_candidates/   # → no match
/usr/bin/grep -rln "DL-MECH-075"  disease-models/wwox/research/commit_candidates/   # → no match
```

🔴 **Consequence for routing.** Surfaces 1–3 are MAJOR and need Operator authorization. Surface 5
is routed as MINOR in a different candidate. Surfaces 4, 6 and 7 are routed nowhere. **Any partial
approval leaves the corpus internally contradictory:** approve only the MAJOR package and the
reader-facing meta directive still instructs readers to treat murine seizure evidence as
rat-derived; approve only the MINOR bundle and the claim keeps the clause the meta just dropped.

⇒ **The seven surfaces are one delta and must be routed as one atomic unit**, at the highest class
any member carries (🔴 MAJOR).

---

## 1. 🔴 `DIS-011`'s revival trigger has already fired, and nobody pulled it

This is the single most consequential item in this candidate, and it is mechanical rather than
interpretive.

`dismissal_ledger_current.md` `DIS-011` — *«Il modello murino Wwox-null mostra epilettogenesi»* →
❌ **RIGETTATA** — declares:

> **`REVIVAL_TRIGGER`:** (a) qualunque **EEG o osservazione di crisi in un topo Wwox-null**;
> (b) un modello condizionale che sopravviva oltre le 3 settimane e poi convulsioni;
> (c) stimolazione audiogena applicata al topo con lo stesso protocollo del ratto.

**Trigger (a) has fired twice, and both firings are inside the read corpus:**

| Firing | Source | What it is | Read status |
|---|---|---|---|
| **seizure observation** | Cheng 2020, PMID 32000863 — *"In our generated Wwox−/− mice, spontaneous epileptic seizures were commonly observed after postnatal day 12"* | the observation half of trigger (a) | `complete_fulltext_read`, locator `L-016-a` |
| **EEG** | Obeid 2026, PMID 42422765 — continuous 24/7 ECoG, P14→P21, SWD/animal, blinded reader | the EEG half of trigger (a) | `complete_fulltext_read`, locator `L-011-a` |

⇒ **`DIS-011` must be REVIVED, not annotated.** A dismissal whose declared revival trigger has
fired and which still reads `RIGETTATA` is a **silent false negative of the exact species the
ledger's own preamble warns about** — and it has been standing while three claims in the same
registry recorded the triggering fact.

⚠️ **What revival does and does not do.** Reviving `DIS-011` does **not** license asserting
epileptogenesis. The proposition `DIS-011` rejected is *«il modello murino Wwox-null mostra
epilettogenesi»*, and after the package's Δ3 that proposition remains prohibited — because
`EPILEPTOGENESIS` as a **process** is unmeasured in every WWOX model. What revival changes is the
**ground**: the dismissal currently rests on *"prova contraria"*, and there is no contrary
evidence — there is a 2009 literature survey over four papers, **none of which recorded EEG**,
plus two later studies that measured the phenotype and found it. The verdict must be restated as
`NOT_MEASURED_AS_A_PROCESS`, never as `ABSENT`.

---

## 2. Per-delta review fields — the package's six, hardened

Every `CURRENT_TEXT` below was read back out of `claim_registry_current.md` at
`ccddc28939234ad4fe29c417935a0dbe11de86d0` immediately before writing, by `sed -n` over the line
range, **not transcribed from the package**. Where the package quoted with ellipsis, the ellipsis
is expanded here — a Mirror reviewer diffing an elided string against the file gets a false
mismatch.

**Baseline-effect legend:** `NARROWED` = the claim asserts strictly less · `REVERSED` = a
truth-value flips · `REWORDED` = same proposition, different words · `RETARGETED` = the
proposition is replaced by a different one that preserves the guard.

---

### Δ1 · `CLAIM 037` **Title** · line 663

- **CURRENT_TEXT** *(literal, whole line after `**Title:** `)*:
  > The seizure phenotype of the Wwox literature is a rat `lde/lde` phenotype, electrographically documented, and it is explicitly absent in Wwox-null mice
- **PROPOSED_REPLACEMENT** *(literal)*:
  > Seizure-related phenotypes in WWOX rodent models are documented in the rat `lde/lde`, in the `Wwox`-null mouse (behaviourally since 2020, electrographically since 2026) and in the `P47T` knock-in mouse (video-EEG, adult); the audiogenic kindling phenotype remains rat-specific
- **EVIDENCE_CLASS:** `DATO` on all four datasets; the deleted clause was `INFERENZA` presented as `DATO`
- **LOCATOR:** `L-037-a`, `L-037-b`, `L-037-c` (the negative) · `L-016-a`, `L-005-a`, `L-011-a`, `L-007-a` (the falsifiers)
- **DO_NOT_INFER:** that the mouse and rat phenotypes are the same phenotype; that "documented"
  implies equal method quality across the four datasets (one is husbandry observation, one is
  four-channel video-EEG); that the `P47T` finding transfers to the null or vice versa.
- **WHY_MINIMUM:** one clause deleted, one added. The rat attribution is **retained and narrowed**
  to the phenotype it is true of, rather than removed.
- **AFFECTED_DOWNSTREAM:** `CLAIM 005` (cites 037 for the rat-phenotype framing) · `CLAIM 038`
  (rat-scoped hypercatabolism) · `CLAIM 039` (cross-linked) · `working_model_current.md:185` mirror
  · `meta_gaba_paradox_current.md:19` directive
- **BASELINE_EFFECT:** 🔴 **REVERSED** on the deleted clause; **NARROWED** on the rat attribution

---

### Δ2 · `CLAIM 037` **Evidence boundary** · line 672

- **CURRENT_TEXT** *(literal, opening through the clause that must go — the package elided this;
  it is expanded here)*:
  > 🔴 **I topi Wwox-null non hanno epilessia riportata** — affermato tre volte in PMID 19500159 e formalizzato in Table 2, dove la riga `Epilepsy` è compilata solo per `lde/lde`. Gli autori lasciano aperta la spiegazione (i topi potrebbero morire prima di convulsionare) e la sopravvivenza la rende testabile: 2–3 settimane nel topo contro **3–12 settimane** nel ratto, con esordio più precoce delle crisi al giorno 16.
- **PROPOSED_REPLACEMENT** *(literal)*:
  > 🔴 `NOT_REPORTED ≠ ABSENT`. PMID 19500159 writes *"neither epileptic seizures nor abnormal behavior **has been reported** in Wwox KO (knockout) mice"* and *"the reason for **no detection** of spontaneous epilepsy in the KO mice is unknown"*, and its Table 2 `Epilepsy` row is empty for **both** mouse columns under footnotes naming Aqeilan et al. 2007/2008/2009 and Ludes-Meyers et al. 2007 — **four papers, none of which recorded EEG.** The negative is a survey artefact of its sources, not a measurement, and the source says so. The die-first explanation is **withdrawn as an explanation**: Cheng 2020 observes spontaneous seizures from P12, inside the null's lifespan. It is retained as the source's own modal — the paper offers it with *"may"*, as one of three candidate reasons.
- **EVIDENCE_CLASS:** `DATO` (as a report of what PMID 19500159 says) — **downgraded from** an
  implied `DATO` about the animal
- **LOCATOR:** `L-037-a` (the *"has been reported"* sentence, p. 2) · `L-037-b` (Table 2, p. 9,
  recipe: `source_pdf_sha256 e1a0a87d…`, page 9, rect `(40,60,560,470)` pt, 400 dpi,
  `image_sha256 290cfc8b…`) · `L-037-c` (the *"no detection"* sentence, pp. 9–10)
- **DO_NOT_INFER:** that `Wwox` KO mice do or do not have seizures — `L-037-a`'s `DO_NOT_INFER`
  says this explicitly; that an empty Table 2 cell implies absence **or** presence; that the
  die-first explanation is correct or incorrect — it is withdrawn as *load-bearing*, not refuted.
- **WHY_MINIMUM:** 🔴 **the hedge is restored, not invented.** The source was already careful and
  the registry hardened it. Only the hardened words change.
- **AFFECTED_DOWNSTREAM:** `CLAIM 005` boundary (same chain) · `DL-MECH-075` (whose headline drops
  the same hedge) · `DIS-011` (whose verdict rests on this text)
- **BASELINE_EFFECT:** **NARROWED** — the claim now asserts strictly less about the animal and
  exactly as much about the paper

---

### Δ3 · `CLAIM 005` **Evidence boundary** · line 114, closing two sentences

- **CURRENT_TEXT** *(literal)*:
  > **No canonical statement may describe a Wwox-null mouse as showing epileptogenesis.** Whether the mouse lacks the phenotype or dies before expressing it is open and testable: the earliest rat seizure onset (day 16) already exceeds the entire lifespan of the mouse null.
- **PROPOSED_REPLACEMENT** *(literal)*:
  > **No canonical statement may assert `EPILEPTOGENESIS` — the process of acquiring an enduring predisposition to spontaneous recurrent seizures — in any WWOX model, because no study has measured that process.** Measured seizure and epileptiform phenotypes **are** recordable and are recorded: see `CLAIM 004`, `CLAIM 011`, `CLAIM 016`, `CLAIM 037`, `CLAIM 040`. PMID 19936220 remains free of any seizure measurement; that is a statement about that paper, not about the animal.
- **EVIDENCE_CLASS:** prohibition — not a datum. Its **ground** moves from `DATO` (asserted absence)
  to `NOT_MEASURED` (a declared gap).
- **LOCATOR:** `L-037-a/b/c` (why the old ground fails) · `L-016-a`, `L-016-b`, `L-011-a` (why the
  ban on measured fact fails)
- **DO_NOT_INFER:** that the retargeted prohibition licenses any seizure claim it does not name;
  that `EPILEPTOGENESIS` is *absent* — the prohibition forbids the assertion **in both
  directions**; that PMID 19936220's silence is evidence about the animal.
- **WHY_MINIMUM:** the prohibition is **retargeted from an entity to a process**, preserving the
  guard it was built for while removing the ban on measured fact. Deleting it outright would
  discard the guard.
- **AFFECTED_DOWNSTREAM:** `CLAIM 004`, `CLAIM 011`, `CLAIM 016`, `CLAIM 037`, new `CLAIM 040` —
  all five currently violate the prohibition as written · `CLAIM 015` (whose *shape* Δ3 adopts) ·
  `DIS-011`
- **BASELINE_EFFECT:** 🔴 **RETARGETED** — neither a narrowing nor a reversal. The old proposition
  is withdrawn and a different one installed.

---

### Δ4 · `CLAIM 011` **Summary**

- **CURRENT_TEXT** *(literal fragment)*:
  > ipereccitabilità / SWD su ECoG (spike-wave discharges — surrogato elettrofisiologico delle crisi)
- **PROPOSED_REPLACEMENT** *(literal fragment)*:
  > ipereccitabilità / SWD su ECoG (spike-wave discharges — **correlato elettrografico di tipo assenza**; non un surrogato dei tipi convulsivi tonico, clonico, tonico-clonico, mioclonico o degli spasmi che compongono lo spettro WOREE)
- **EVIDENCE_CLASS:** `DATO` on the SWD measurement; the replaced phrase was `INFERENZA`
- **LOCATOR:** `L-011-a` (SWD/animal panel), `L-011-b` (Methods, ECoG acquisition), `L-011-c`
  (Fig 7E raster)
- **DO_NOT_INFER:** that SWD suppression predicts convulsive-seizure benefit; that a single-channel
  montage resolves bilateral synchrony; that the untested interictal-spike endpoint of the same
  figure is `ns`.
- **WHY_MINIMUM:** three words replaced. Measurement, statistics and the dose flag are untouched.
- **AFFECTED_DOWNSTREAM:** new `CLAIM 040` (inherits the absence-type boundary) · `CLAIM 031`
  (seizure control ≠ developmental rescue) · `therapy_levers.md` gene-therapy rationale
- **BASELINE_EFFECT:** **NARROWED**

---

### Δ5 · `CLAIM 004` **Summary**

- **CURRENT_TEXT** *(literal fragment)*:
  > singola ICV neonatale (P0) di AAV9-hSynI-WWOX (murino o umano, equivalenti) recupera sopravvivenza/letalità postnatale, crescita, ipoglicemia, crisi, atassia, mielinizzazione
- **PROPOSED_REPLACEMENT** *(literal fragment)*:
  > singola ICV neonatale (P0) di AAV9-hSynI-WWOX (murino o umano, equivalenti) **estende la sopravvivenza** (≈93 % a 270 giorni, poi in discesa; `p < 0.0001` contro il null non trattato — **non** sopravvivenza pari al WT), crescita, ipoglicemia, **ipereccitabilità neuronale misurata come frequenza di scarica in cell-attached**, atassia, mielinizzazione
- **EVIDENCE_CLASS:** `DATO`; the two replaced words were nomenclature over-reach, not data
- **LOCATOR:** `L-004-a` (Fig 3A–B firing rate), `L-004-b` (Fig 2C survival curve)
- **DO_NOT_INFER:** that firing-rate rescue is seizure rescue; that survival extension is survival;
  that the P0 window transfers to a post-natal human dosing schedule — the source calls
  post-natal dosing explicitly future work.
- ⚠️ **DO_NOT_INFER, added here:** Fig 2C's legend declares *"total n = 16, alive n = 6,
  spontaneously dead n = 6, 4 mice … taken out for analysis"* while the plotted curve reaches 0 %.
  **The terminal fraction cannot be taken at face value**; ≈93 %-at-270 d is a curve reading, not a
  reconciled survivorship.
- **WHY_MINIMUM:** two words qualified. No domain is removed.
- **AFFECTED_DOWNSTREAM:** `CLAIM 003` (cause vs rescue on a shared source) · `CLAIM 011` (dose
  adjudication) · `CLAIM 032` (partial-restoration threshold) · `TX-007`
- **BASELINE_EFFECT:** **NARROWED**

---

### Δ6 · `CLAIM 016` — addition only

- **CURRENT_TEXT:** unchanged; nothing is removed.
- **PROPOSED_REPLACEMENT:** append a cross-reference to `CLAIM 037` / `CLAIM 040`; record that
  Cheng 2020 is the **only** primary source for spontaneous behavioural seizures in a `Wwox`-null
  mouse, and that its observation is **a floor, not a rate** (routine handling plus one movie, no
  scored protocol, no denominator); record that its word *"epileptogenesis"* is the source's and
  is **not licensed** by what it measured.
- **EVIDENCE_CLASS:** `DATO` (provoked susceptibility, Racine) + `NOT_MEASURED` (rate)
- **LOCATOR:** `L-016-a`, `L-016-b`
- **DO_NOT_INFER:** a penetrance figure from *"commonly observed"*; that the lithium arm is
  genotype-specific — the existing boundary already forbids this and is untouched.
- **WHY_MINIMUM:** addition only.
- **AFFECTED_DOWNSTREAM:** `CLAIM 035` (residue-level mechanism) · `TX-005` · `DIS-009`
- **BASELINE_EFFECT:** **REWORDED** (strictly, extended — no existing proposition changes)

---

### Δ7 · new `CLAIM 040`

- **CURRENT_TEXT:** none — the claim does not exist.
- **PROPOSED_REPLACEMENT** *(literal)*:
  > Neuronal restoration of WWOX suppresses spike-wave discharges in the `Wwox`-null mouse to a level statistically indistinguishable from wild type.
- **EVIDENCE_CLASS:** `DATO` · P1/P7 · T2 · `in observation` · `PAPER 011`, Figure 7E
- **LOCATOR:** `L-011-a/b/c`
- **DO_NOT_INFER:** that SWD suppression is convulsive-seizure suppression; that `ns` vs WT on one
  endpoint is normalisation; that the untested interictal-spike endpoint agrees; that a
  developmental benefit follows — `CLAIM 031` is cross-linked **precisely** to block that step.
- **WHY_MINIMUM:** the triad exists only as a sub-clause of a claim flagged for an unrelated
  reason. Promoting it changes no other text.
- **AFFECTED_DOWNSTREAM:** `CLAIM 011` (loses the sub-clause's weight) · `CLAIM 022` (must not be
  re-centred on postnatal seizures) · `CLAIM 031`
- **BASELINE_EFFECT:** **addition**

---

## 3. Three deltas the package omits — full review fields

### Δ8 · `working_model_current.md:185` — the claim mirror · 🔴 MAJOR

- **CURRENT_TEXT** *(literal, table cell)*:
  > The seizure phenotype of the Wwox literature is a rat `lde/lde` phenotype, EEG-documented, and is explicitly absent in Wwox-null mice
- **PROPOSED_REPLACEMENT:** the Δ1 replacement string, abbreviated to mirror length; the mirror
  must not assert what the claim no longer asserts.
- **EVIDENCE_CLASS / LOCATOR / DO_NOT_INFER:** identical to Δ1 — this is the same proposition.
- **WHY_MINIMUM:** a mirror carries no independent evidence. Leaving it is not conservatism, it is
  a second copy of a deleted falsehood. 🔴 The principle is already established in this candidate
  set: [`CC-20260826-CLAIM006-01`](CC-20260826-CLAIM006-01.md) §3 routes the `CLAIM 006` mirror on
  exactly this ground — *"mirrors must not drift from the claim"*. FIVECLAIM does not apply it.
- **AFFECTED_DOWNSTREAM:** every reader who consults the working model instead of the registry.
- **BASELINE_EFFECT:** 🔴 **REVERSED**

### Δ9 · `meta_gaba_paradox_current.md:19–20` — the provenance directive · 🔴 MAJOR *(currently routed MINOR)*

- **CURRENT_TEXT** *(literal, opening of the blockquote)*:
  > 🔴 **Provenance correction — `BATCH_20260806_002`. Seizures are a RAT phenotype in this literature, and they are explicitly ABSENT in Wwox-null mice.**
  > Wherever this file uses seizure activity or epileptogenesis as context for the **murine** hippocampal marker phenotype above, that context is **rat-derived and species-discordant**, not a property of the mouse model.
- **PROPOSED_REPLACEMENT:** replace the two asserted-absence sentences with the Δ2 formulation, and
  **keep the part that is correct and valuable** — that the chain which imported the seizure
  premise into the mouse literature was a **citation chain, not a measurement**. The directive's
  second sentence must be withdrawn outright: murine seizure context is **not** rat-derived, and an
  instruction to treat it as such actively suppresses four correct datasets.
- **EVIDENCE_CLASS:** directive; ground moves from `DATO` to `NOT_MEASURED`
- **LOCATOR:** `L-037-a/b/c`, `L-016-a`, `L-011-a`
- **DO_NOT_INFER:** that the metabolic-decompensation caveat in the same blockquote is affected —
  it is independent and stands.
- **WHY_MINIMUM:** two sentences. The remainder of the blockquote is sound.
- 🔴 **ROUTING DEFECT:** this surface is currently routed in
  [`CC-20260826-PROVENANCE-01`](CC-20260826-PROVENANCE-01.md) §E, which the review index classes
  as **MINOR per item**, and whose justification points at
  [`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md) — a document FIVECLAIM **supersedes**.
  The same falsified proposition is therefore routed at two authorization levels, via a chain whose
  head is superseded.
- **AFFECTED_DOWNSTREAM:** `CLAIM 002`, `CLAIM 005` — the meta's whole purpose is to frame the
  GABA/glia reading.
- **BASELINE_EFFECT:** 🔴 **REVERSED**

### Δ10 · `discovery_ledger_current.md:1973` — `DL-MECH-075` headline · MODERATE

- **CURRENT_TEXT** *(literal, heading)*:
  > ### DL-MECH-075 — La catena non finisce in assenza di prova: finisce in una prova contraria. Il terminale dichiara che i topi Wwox-null NON hanno epilessia
- **PROPOSED_REPLACEMENT** *(literal)*:
  > ### DL-MECH-075 — La catena non finisce in una misura: finisce in un censimento della letteratura. Il terminale dichiara che nei topi Wwox-null l'epilessia non è stata *riportata*, e che la sua mancata rilevazione è inspiegata
- **EVIDENCE_CLASS:** `DATO` as a report of the literature — **which the entry's own body already
  states correctly**, quoting *"has been reported"* and *"no detection"* verbatim. Only the
  headline overstates.
- **LOCATOR:** `L-037-a`, `L-037-c`
- **DO_NOT_INFER:** that the entry's chain-tracing conclusion is wrong. It is right: PMID 30290271
  → PMID 19936220 → PMID 19500159 is a citation chain with no measurement at either hop. **That
  finding survives intact.**
- **WHY_MINIMUM:** the headline only. The body needs no edit — it already carries the hedge.
- **AFFECTED_DOWNSTREAM:** `DL-MECH-072`, `DL-MECH-073`, `CLAIM 005`, `DIS-011`
- **BASELINE_EFFECT:** **NARROWED**

### Δ11 · `dismissal_ledger_current.md` `DIS-011` — 🔴 **REVIVE** · MAJOR

- **CURRENT_TEXT** *(literal, verdict line)*:
  > - **Verdetto:** **rigettata, e non per assenza di prova ma per prova contraria.** PMID 19936220 non contiene EEG, osservazione di crisi, test comportamentale o istologia cerebrale; l'unica misura cerebrale del paper è il peso dell'organo. Il termine entra una sola volta, come citazione in Discussione del ratto `lde`. E il terminale, PMID 19500159, dichiara in tre punti — e in una Table 2 la cui riga `Epilepsy` è **vuota per entrambi i modelli murini** — che i topi Wwox-null **non hanno epilessia riportata**.
- **PROPOSED_REPLACEMENT** *(literal)*:
  > - **Verdetto:** **rigettata come misura, non come fatto — e REVIVED 2026-08-26 perché il suo `REVIVAL_TRIGGER` (a) si è attivato.** PMID 19936220 non contiene EEG, osservazione di crisi, test comportamentale o istologia cerebrale; l'unica misura cerebrale del paper è il peso dell'organo, e il termine entra una sola volta come citazione in Discussione del ratto `lde`. Il terminale, PMID 19500159, non afferma un'assenza: scrive *"has been **reported**"* e *"no **detection**"*, e la sua Table 2 ha la riga `Epilepsy` vuota per entrambe le colonne murine sotto note che citano quattro paper, **nessuno dei quali ha registrato EEG**. ⇒ `NOT_REPORTED ≠ ABSENT`, e `NO_DETECTION ≠ NO_PHENOTYPE`. **Il trigger (a) — «qualunque EEG o osservazione di crisi in un topo Wwox-null» — è stato soddisfatto due volte**: Cheng 2020 (crisi spontanee osservate da P12) e Obeid 2026 (ECoG continuo P14–P21). Ciò che resta rigettato è l'affermazione di **EPILETTOGENESI come processo**, mai misurata in nessun modello WWOX — vedi la proibizione ritargettata in `CLAIM 005`.
- **EVIDENCE_CLASS:** dismissal verdict; ground moves from `DATO` (contrary evidence) to
  `NOT_MEASURED` (no process measurement) — **the dismissal survives, its ground does not**
- **LOCATOR:** `L-037-a/c` (the source's hedges) · `L-016-a` and `L-011-a` (the two firings)
- **DO_NOT_INFER:** that revival licenses asserting epileptogenesis; that `DIS-011`'s companion
  finding — the two-hop unverified citation chain — is weakened. It is not.
- **WHY_MINIMUM:** the verdict word and its ground. The chain analysis, the *"perché è sopravvissuta
  così a lungo"* paragraph and the re-audit hook are untouched, except that the *"Cosa NON viene
  rigettato"* paragraph's survival argument (*"2–3 settimane nel topo contro 3–12 nel ratto"*)
  must be marked **withdrawn**, on the same ground as Δ2.
- **AFFECTED_DOWNSTREAM:** `CLAIM 005` (which cites the same chain) · `DL-MECH-075` · the
  re-audit hook *"rigetto di fenotipo per specie"* — which should now be pulled for every
  species-scoped negative in the ledger
- **BASELINE_EFFECT:** 🔴 **REVERSED** (of the ground), **preserved** (of the verdict)

---

## 4. 🔴 Special-invariant audit — `NOT_REPORTED ≠ ABSENT`, `NO_DETECTION ≠ NO_PHENOTYPE`

Checked mechanically, in both directions, over the BEFORE and AFTER of all eleven deltas.

| Check | BEFORE state | AFTER state |
|---|---|---|
| Does any surface assert `ABSENT` where the source says `NOT_REPORTED`? | 🔴 **YES — five surfaces**: 037 Title, `CLAIM 005`:114, `working_model`:185, `meta_gaba_paradox`:19–20, `DL-MECH-075` headline | ✅ **none** |
| Does any surface assert `NO_PHENOTYPE` where the source says `NO_DETECTION`? | 🔴 **YES — `DIS-011`**, via *"prova contraria"* | ✅ **none** — restated as `NOT_MEASURED` |
| Does the repair over-correct — asserting `PRESENT` where only `REPORTED` is warranted? | n/a | ✅ **no.** Δ1 says *"documented"* and names the method tier of each dataset; Δ6 marks Cheng 2020 a **floor, not a rate** |
| Does the repair assert a **process** anywhere? | 🔴 the ban did, by implication | ✅ **no** — Δ3 forbids it in both directions |
| Is any `UNRESOLVED` axis silently promoted? | — | ✅ **no.** `MEASURED_SPIKE_RATE` stays `UNRESOLVED`; `EPILEPTOGENESIS` stays `UNRESOLVED`; `E_GABA` stays unmeasured |

🔴 **The invariant's own failure mode, named.** Every one of the five `ABSENT` upgrades was
produced by the same operation: a **hedged predicate about the literature** (*"has been
reported"*, *"no detection"*) was rewritten as an **unhedged predicate about the animal**. The
transformation is invisible per-surface — each rewrite looks like tightening prose. It is only
visible across surfaces, which is why the closure check in §0 is the load-bearing part of this
candidate and not the per-delta table.

---

## 5. Artefact-resolution note for the Mirror reviewer

⚠️ `files/` is **gitignored** and therefore **per-working-directory**. Verified:

```bash
git ls-files files/ | wc -l          # → 0
```

The locator packet's `ARTIFACT` paths (`files/fulltext/PMID19500159_Suzuki2009.pdf` and the rest)
**do not resolve inside this worktree**; they resolve in the main checkout. The durable identifier
is the **sha256**, not the path — and it verifies:

```
e1a0a87dc7faac002c20f060293aa7f6962f8ba61105bf6237e72bc4a0dd5c56
  <REPO_ROOT>/files/fulltext/PMID19500159_Suzuki2009.pdf   ✅ matches declared
```

**Reviewer instruction:** resolve every `ARTIFACT` path against the checkout that holds
`files/fulltext`, confirm by sha256, and treat a path miss as a location failure — never as a
missing artefact.

---

## 6. What this candidate refuses to do

- **Does not supersede** `CC-20260826-FIVECLAIM-PACKAGE-01`. Its six deltas stand as written; this
  document supplies review fields and adds four surfaces.
- **Does not merge the nine seizure axes.** Every delta names its axis.
- **Does not lift `CLAIM 011`'s dose flag**, or change `CLAIM 016`'s status.
- **Does not assert that `Wwox`-null mice have epileptogenesis.** Δ3 forbids it; Δ11 keeps the
  dismissal.
- **Does not create a new schema.** `BASELINE_EFFECT` and `DO_NOT_INFER` are prose fields, used
  here and not proposed as registry fields.
- **Does not retrofit** the pre-2026-08-25 candidates.

---

## 7. Review required

🔴 **Operator authorization**, MAJOR on six counts: Δ1, Δ2, Δ3, Δ8, Δ9, Δ11.
🔴 **Route all eleven deltas as one unit.** Partial approval produces a corpus that contradicts
itself on the surface the other half repairs — §0.
🔴 **Locator audit REQUIRED before the MAJOR edits.** No new locator is needed: packet groups A and
B already cover every string above.
