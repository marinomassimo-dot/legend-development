# COMMIT CANDIDATE — the CLAIM 004 / CLAIM 011 dose contradiction, adjudicated at the vector map

**Candidate ID:** CC-20260826-DOSE-ADJUDICATION-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** figure-level adjudication of a named cross-claim contradiction
**Resolves:** §2 of [`CC-20260826-CROSS-CLAIM-CENSUS-01`](CC-20260826-CROSS-CLAIM-CENSUS-01.md),
which flagged this as `NEEDS_SCIENTIFIC_ADJUDICATION` pending one unread figure
**Change class:** 🔴 **MAJOR** — a `consolidated baseline` claim (`CLAIM 004`) and a
`flagged for review` claim (`CLAIM 011`) imply incompatible dose thresholds on the therapeutic
axis, and the discriminant that was expected to reconcile them **does not**
**Target WM:** current at BATCH_COMMIT time
**Batch gate:** intentionally untouched

---

## 0. The finding, and it is the opposite of what I predicted

[`CC-20260826-CROSS-CLAIM-CENSUS-01`](CC-20260826-CROSS-CLAIM-CENSUS-01.md) §2 proposed that the
contradiction would dissolve once Appendix Fig S1A of PMID 34747138 was read, because Obeid 2026
states that WPRE presence inverts the outcome at a fixed vg dose. The prediction was explicit:
if Repudi's vector carried WPRE, the two studies would be reconciled.

🔴 **Appendix Fig S1A, read at 300 dpi from the supplementary PDF, shows all three Repudi vectors
are WPRE-free.** The prediction is falsified, and the contradiction is not softened by the reading
— it is **sharpened**, because the discriminant is now excluded rather than merely unmeasured.

---

## 1. Adjudication recipe — reproducible, image not shipped (rule 5e)

| Item | Value |
|---|---|
| **Source** | `files/fulltext/figures/PMID34747138/EMMM-13-e14599-s001.pdf` (Appendix, 11 pp) |
| **source_pdf_sha256** | `1e5c30a903d96726cffae487e14f2e80593e4a6adf2e8b08efb70a5762f86cd2` |
| **Page** | 2 (Appendix Fig S1) |
| **Crop rect (PDF pt)** | full page `(0.00, 0.00, 510.00, 567.00)` |
| **dpi** | 300 → 2125 × 2363 px |
| **image_sha256** | `e362bdf80c8d850bb32859d20ff39d6264569f1332cb7455fdc649aac61f9c02` |

| Item | Value |
|---|---|
| **Source** | `files/fulltext/figures/PMID34747138/EMMM-13-e14599_article.pdf` |
| **source_pdf_sha256** | `32ee98733a6f45550f6b924b701734e111d171992ecba2535f0c32a5e105b438` |
| **Page / crop** | 4, rect `(400.00, 70.00, 545.00, 205.00)` pt — Figure 2C Kaplan-Meier |
| **dpi** | 600 → 1209 × 1126 px |
| **image_sha256** | `ac41ab21703026d593a30a18ced4dba09a038455df7528844e55956cdb3972fd` |

| Item | Value |
|---|---|
| **Source** | `files/fulltext/figures/PMID42422765/gr3.jpg` (Obeid Figure 3) |
| **source_sha256** | `c63f930cf5c558ae…` (as already declared in `deepdive_manifests/PMID42422765.json`) |
| **Crop box (source px)** | `(436, 0, 726, 297)` of 726 × 708, upscaled ×4.5 → 1305 × 1336 |
| **image_sha256** | `4c6f2fdd31867e96ce450eacdc4222e82ddb85a8e3624e85adbc66ddd586b996` |

⚠️ `gr3.jpg` is the **PMC CDN rendition at 726 px**, not a native-resolution original. It is
adequate for reading axis ticks, curve levels and legend `n`s, and is **not** adequate for
anything finer. Declared rather than glossed.

---

## 2. What the vector maps say

**Appendix Fig S1A** prints three constructs, left-to-right, each between flanking ITRs:

| Vector | Cassette as printed | WPRE |
|---|---|---|
| `AAV-mWwox` | `ITR │ hSynI │ mWwox │ IRES │ GFP │ polyA │ ITR` | **absent** |
| `AAV-hWWOX` | `ITR │ hSynI │ hWWOX │ polyA │ ITR` | **absent** |
| `AAV-GFP` | `ITR │ hSynI │ GFP │ polyA │ ITR` | **absent** |

**Obeid 2026 Figure 2A** prints two constructs: `AAV9 │ ITR │ Synapsin → WWOX │ ITR` and the same
with a yellow `WPRE` box appended after `WWOX`.

⇒ **Repudi's `AAV-hWWOX` and Obeid's WPRE-free `AAV9-hSynI-hWWOX` are the same architecture.**

---

## 3. The comparability audit — every discriminant I could name, checked

| Axis | Repudi 2021 (PMID 34747138) | Obeid 2026 (PMID 42422765) | Match |
|---|---|---|---|
| Laboratory | Aqeilan | Aqeilan | ✅ same |
| Serotype | AAV9 | AAV9 | ✅ |
| Promoter | hSynI | hSynI | ✅ |
| Transgene | hWWOX | hWWOX | ✅ |
| **WPRE** | **absent** (Appendix Fig S1A, pixels) | **absent** in the failing arm | ✅ |
| Route / age | ICV, P0–P1 | ICV, P0–P1 | ✅ |
| **Titration** | *"Viral titer was measured by qRT–PCR using bGH primers"* | *"Viral titers were determined by RT-qPCR using bGH primers"* | ✅ **same method, same primers** |
| **Background** | FVB | *"Mice were kept on an FVB (Friend leukemia Virus B) background"* | ✅ |
| Vector source | Vector Biolabs / HUJI Vector Core | Fujifilm / Vector Biolabs / BIB; HUJI ELSC Core | ◐ overlapping |
| Injection | **free-hand**, ~1 µL/hemisphere | **stereotactic** (Kopf frame, Micro-4 pump, 1–1.5 µL/min), 2.0 µL/hemisphere | ❌ **differs** |
| Dose | `2 × 10¹⁰` GC/hemisphere → **4 × 10¹⁰ total** (Methods); Fig 2A legend prints `AAV-hWWOX (2 × 10¹⁰)` | LD **1.23 × 10¹¹**, HD **2.63 × 10¹¹**; separate arm at **4 × 10¹⁰** and **8 × 10¹⁰** | ❌ |

⚠️ **Repudi's own dose is internally ambiguous.** Methods say per-hemisphere and *"the other
hemisphere was injected in the same way"*; the Figure 2A legend prints a bare `(2 × 10¹⁰)`. The
consistent reading is **4 × 10¹⁰ total**, but the paper does not say so in the legend, and the
alternative reading (2 × 10¹⁰ total) makes the contradiction **worse**, not better. Both readings
are recorded; neither is chosen silently.

---

## 4. The survival curves, read at pixel level

**Repudi Fig 2C** (600 dpi crop, recipe §1) — `KO+AAV-hWWOX (n = 16)`, green:
holds ≈93 % from ~90 d through ~270 d, then steps ≈78 % (~295 d) → ≈62 % (~318 d) → ≈15 %
(~322 d) → **0 % by ~330 d**. WT (n = 6) flat at 100 %. KO (n = 8) to 0 % by ~28 d.
`p < 0.0001`, log-rank.

**Obeid Fig 3B** (×4.5 crop, recipe §1):
- `WT+RI n=20` — 100 % → ≈90 % (~50 d) → ≈72 %, flat to 300 d. **Wild type itself is not 100 %.**
- `KO+RI n=10` — 0 % by ~18 d.
- **`KO+WWOX (LD) n=20` (1.23 × 10¹¹) — declines from ~20 d, reaches 0 % by ~80 d.**
- `KO+WWOX (HD) n=30` (2.63 × 10¹¹) — ≈78 % at ~85 d, flat to 300 d.

### The comparison, on a common endpoint

| Study | Dose (WPRE-free hSynI-hWWOX) | Survival ≈270–300 d |
|---|---|---|
| **Repudi 2021** | **2–4 × 10¹⁰** | **≈93 % at 270 d** |
| Obeid 2026 LD | 1.23 × 10¹¹ (**3–6× higher**) | **0 % — all dead by ~80 d** |
| Obeid 2026 HD | 2.63 × 10¹¹ | ≈78 % at 300 d |

🔴 **Repudi's three-to-sixfold LOWER dose of the same vector architecture, in the same strain,
titrated by the same method in the same laboratory, outperforms Obeid's LD by the entire width of
the experiment and is comparable to Obeid's HD.**

---

## 5. `VG_DOSE_ALONE_IS_NOT_TRANSFERABLE` — **SUPPORTED**, with the discriminant in hand

The operator's condition was: do not promote without the vector discriminant. It is now read, and
it **excludes** vector configuration as the explanation. The hypothesis survives on stronger
ground than the route originally proposed:

1. **Within Obeid 2026**, WPRE presence inverts survival at a fixed 4 × 10¹⁰ vg — vector
   configuration beats dose.
2. **Between Repudi and Obeid**, vector configuration is *matched* and dose is *inverted relative
   to outcome* — so dose does not determine outcome even at fixed configuration.

⇒ **A vg number is not a transferable quantity across studies.** Any inference of the form
*"a clinical WWOX dose must exceed ~10¹¹ vg"* reads a study-specific constant as a biological one.

**What is NOT concluded.** Not that either paper is wrong; not that Repudi's rescue is
unreliable; and **not** that the residual is explained. The unmatched axes are **injection
technique** (free-hand vs stereotactic), **volume** (1 vs 2 µL/hemisphere), and **vector lot/prep
year**. `PREMISE_TAG: INFERENZA` on any claim that delivery efficiency is the residual cause —
it is the leading candidate and **has not been measured**.

🔴 **The measurement that would settle it exists in Obeid 2026 and was never used for this.**
Obeid quantifies **vector genome copies in brain tissue at P30 by qPCR** (Figures 5A–5D). If
Repudi's brains were assayed the same way, the two studies could be compared on **delivered
genomes per brain** instead of on injected vg — the quantity that actually transfers. That is a
tissue-qPCR run on banked material, not a new animal study.

---

## 6. A second finding: Obeid 2026 contains an apparent internal dose inversion, and it is a follow-up artifact

Obeid reports that the WPRE-free vector at **8 × 10¹⁰ vg** produced *"improved outcomes, including
rescue of lethality"* (Fig 2B), while the same WPRE-free vector at **1.23 × 10¹¹ vg** — 1.5×
higher — produced only a *"modest"* extension ending in total mortality by ~80 d (Fig 3B).

🔴 **Read at pixels, Figure 2B's x-axis ends at 50 days.** The `8 × 10¹⁰` arm (n = 5, magenta)
is flat at 100 % to ~31 d; the `4 × 10¹⁰` arm (n = 3, yellow) falls to ≈33 % by ~20 d with one
animal censored at ~25 d; untreated KO reaches 0 % at ~19 d.

⇒ *"Rescue of lethality"* in Figure 2 means **"alive at about 31 days"**. In Figure 3, followed to
300 days, the same word means **"alive at 300 days"**. **`NOMENCLATURE_CONFLICT`, not a true
contradiction** — one word, two follow-up windows, inside one paper. Recorded because a reader
comparing the two figures without the axes will infer a dose inversion that the data do not show.

---

## 7. A third finding: Repudi Fig 2C's legend and its panel disagree

The legend states *"total n = 16, alive n = 6, spontaneously dead n = 6, 4 mice (shown in yellow)
were taken out for analysis"*. **The plotted green curve reaches 0 %.** A Kaplan-Meier with 6
animals alive cannot terminate at zero; censored animals hold the curve above it.

`EPISTEMIC_STATUS`: **`UNRESOLVED`.** Most likely the "alive" count was current at manuscript
writing while the curve was drawn later, or the censored animals were plotted as events. **Either
way the survival fraction at ~330 days cannot be taken from this panel at face value**, and the
`≈93 % at 270 d` figure used in §4 — which is read before any of the ambiguous terminal steps —
is the part that is safe to use.

---

## 8. Proposed canonical effect

- **`CLAIM 004` (MAJOR annotation).** Record the dose **with its vector configuration and its
  comparator**: `AAV9-hSynI-hWWOX`, **WPRE-free** (Appendix Fig S1A), `2 × 10¹⁰` GC/hemisphere
  (≈`4 × 10¹⁰` total), survival ≈93 % at 270 d then declining, `p < 0.0001` vs untreated. **Never
  the dose alone.**
- **`CLAIM 011` (MODERATE annotation, flag not lifted).** Its threshold *"between 1.23 and
  2.63 × 10¹¹ vg"* is a threshold **for this study's vector, prep and delivery**, and is
  contradicted at 3–6× lower dose by `PAPER 005`/`PAPER 063`'s own predecessor. The `REVIVAL_TRIGGER`
  already on the claim — an intermediate-dose arm — is **necessary but not sufficient**; it must
  also report delivered genome copies per brain.
- **New dismissal-ledger entry.** *"A vg dose measured in one WWOX gene-therapy study transfers to
  another"* → ❌ **REJECTED**. `REVIVAL_TRIGGER`: two studies reporting **delivered vector genome
  copies per brain region** by the same assay, agreeing on outcome at matched delivered dose.
- **No change to the direction of `CLAIM 004`'s rescue finding**, which is not in question.

---

## 9. Review required

🔴 **Operator authorization.** MAJOR: it qualifies a `consolidated baseline` claim's headline
quantity and contradicts a threshold currently used to reason about trial dosing. It also
**retracts a prediction this session published** in the census candidate, which is recorded here
rather than quietly amended.

---

## WAVE-2 READINESS (2026-09-27)

**Actor:** `scientist`, wave-2 package "dose", under the operator standing authorisation of 2026-09-27.
**context_policy declared:** `QUESTION_DRIVEN` — this session held LEGEND's records (candidate text, claim
registry, manifests) before opening any source, so `SOURCE_FIRST` was not available to it and is not
claimed. What it admitted is named where it is used.
**Evidence base re-derived first, because it changes what any verdict here can mean:**
🔴 `evidence_presence.py --pmid 42422765 --pmid 34747138` → **0 of 28 declared artifacts present in this
checkout** (`VERDICT: NO LOCAL EVIDENCE`). Every figure value in this candidate therefore rests on the
recorded attestation of the session that had panel access, not on a fresh panel read. One structured
surface was re-acquired to repair what could be repaired from text:
`files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml`, sha256
`7bea83346b708e541d2c432e5da4029f69673e1abc3c6fe70926ad0e3ec2eef2`, efetch `db=pmc id=13343157`,
recorded in `research/retrieval_manifest.jsonl` and declared in
`deepdive_manifests/PMID42422765.json` with its `acquisition_recipe`. Receipt prepared and **not**
recorded (the ledger is a hash chain and sibling packages run in parallel):
`scratchpad/receipts_pending/dose_42422765_1.json` (`FTR-20260927-42422765-07`,
`partial_fulltext_read`, prior `FTR-20260814-42422765-06`, `reread_reason:
new_question_outside_prior_coverage`).

### Verdict: **READY_MAJOR** (change class MAJOR, unchanged from §9 — operator authorisation still required)

**What was done.**
1. **Disposition contradiction adjudicated.** Nothing of this candidate is propagated: `CLAIM 004`
   carries its 2026-08-10 comparator boundary but **no dose basis and no vector configuration**; `CLAIM 011`
   carries the LD/HD threshold with **no vector-configuration boundary**; and `registry_records.py get
   --id "dismissal_ledger_current"` reaches **no** entry for a transferable vg dose. Verified at commit
   `db7fbeb`, claim-registry digest `fbaef2510878`.
2. **Family head confirmed.** `CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01` is closed as **SUPERSEDED** by
   `CC-20260826-DOSE-DECISION-TABLE-01` in this wave (see that file), so this candidate now has **one**
   dependent, not two, and the batch propagates two wordings rather than three.
3. **Two of this candidate's load-bearing sentences were promoted from prose to receipted locators** in
   `deepdive_manifests/PMID42422765.json` (entries 29–30, machine-verified): the WPRE-removal rationale and
   the *"higher vector doses"* consequence. They are quoted in §5 of this file's sibling candidates and had
   no persisted locator anywhere.
4. **Not re-verified and not claimable as re-verified:** Appendix Fig S1A at 300 dpi, Repudi Fig 2C, Obeid
   Fig 3B. The bytes are absent (see above). The §1 adjudication recipe remains reproducible from a
   reader's own copy, which is what rule 5e asks of it.

### Exact operation list for `batch_commit.py propagate`

**File `disease-models/wwox/registries/claim_registry_current.md` · record `CLAIM 004` · op
`replace-within`**

- *old text (verbatim from the current file, the final sentence of the Summary field):*
  `espressione durevole ≥9 mesi.`
- *new text:*
  `espressione durevole ≥9 mesi. 🔴 **Dose e configurazione, insieme e mai la dose sola (2026-09-27, `CC-20260826-DOSE-ADJUDICATION-01`):** il vettore è `AAV9-hSynI-hWWOX` **privo di WPRE** (Appendix Fig S1A, letta a 300 dpi; il paper 2021 non menziona WPRE) e la dose è **2 × 10¹⁰ GC/emisfero, entrambi gli emisferi, totale ≈4 × 10¹⁰ GC** — base dichiarata due volte (Results e Methods), mentre la legenda di Fig 2A stampa il solo `(2 × 10¹⁰)`. Citare la dose senza configurazione e senza base è ciò che rende la quantità non trasferibile.`

**File `disease-models/wwox/registries/claim_registry_current.md` · record `CLAIM 011` · op
`replace-within`**

- *old text (verbatim, inside the 🔴 flag):*
  `` `REVIVAL_TRIGGER`: un braccio a dose intermedia fra 1.23 e 2.63 × 10¹¹ vg localizzerebbe la soglia — l'esperimento più informativo che questo paper implica. ``
- *new text:* the text proposed by `CC-20260922-CLAIM011-DOSE-ENDPOINTS-01` Δ2 **plus** this candidate's
  boundary, appended as one sentence:
  `⚠️ **Confine di configurazione (2026-09-27):** la soglia è una soglia **per questo vettore, questo lotto e questa consegna** — il predecessore dello stesso laboratorio, con la stessa architettura WPRE-free, ottiene ≈93 % di sopravvivenza a 270 giorni a una dose **3–6× più bassa** (Repudi 2021, ≈4 × 10¹⁰ GC totali), quindi il numero non è una costante biologica. Il `REVIVAL_TRIGGER` deve riportare anche le **copie di genoma consegnate per regione**, non solo la dose iniettata.`

**File `disease-models/wwox/research/dismissal_ledger_current.md` · op `append`** (non-canonical,
append-only; the batch appends it so that the three dose candidates produce **one** entry)

- *new record id:* **`DIS-021`** — the next free id, verified by `registry_records.py catalog --source dismissal_ledger_current` (20 records, `DIS-001`…`DIS-020`, none on dose transferability). *Record:* `"A vg dose measured in one WWOX gene-therapy study transfers to another"` → ❌ **REJECTED**,
  on the three independent grounds the decision table states (within-study non-linearity; the ≈44× WPRE
  dose-equivalence; the two papers not reporting the same physical quantity).
  `REVIVAL_TRIGGER`: two studies reporting **regional WWOX protein relative to WT** at a matched, stated
  age, agreeing on outcome at matched protein.

### LOCATOR TRIPLES FOR BLIND AUDIT

| proposition | verbatim quote | anchor |
|---|---|---|
| The 2026 paper's own words say that removing WPRE was a precaution taken in the absence of an observation, not a safety result. | "Although no overt toxicity was observed in prior studies, we removed WPRE as a proactive risk-mitigation step to improve the predictability and control of neuronal WWOX expression for potential clinical translation." | `PMID42422765_Obeid2026_PMC_2026-09-27.xml`, Discussion, paragraph on control of transgene expression (manifest entry 29) |
| The same paper states that the lower expression has to be bought back with more capsid — which is what makes a vg number a property of the construct rather than of the biology. | "However, this reduction in expression necessitates the use of higher vector doses to achieve comparable therapeutic outcomes." | same artifact, Results, "Removal of WPRE enables controlled WWOX expression while maintaining therapeutic efficacy at higher vector doses", final sentence (manifest entry 30) |
| The 2026 doses are printed as bare `vg` with no unit convention anywhere in the running text. | "For translational relevance, we evaluated two clinically applicable doses: an LD (1.23 × 1011 vg) and a higher dose (HD, 2.63 × 1011 vg) (Figure 3A)." | same artifact, Results, dose-response section, first paragraph (manifest entry 31) |
| The Methods state no dose at all — the only vector quantity in them is how the titre was assayed. | "Viral titers were determined by RT-qPCR using bGH primers." | same artifact, Materials and methods, "Plasmid vectors", final sentence (manifest entry 33) |
| The injection is bilateral, one injection per hemisphere, which bounds the unit ambiguity at exactly 2×. | "A Micro-4 nano-pump controller was used to ensure a steady injection rate of 1–1.5 μL/min, delivering 2.0 μL/hemisphere through a Hamilton syringe with a 32G needle (World Precision Instruments)." | same artifact, Materials and methods, "ICV injection of AAV particles into P0-P5 Wwox-null mice" (manifest entry 32) |
| Repudi's total dose is per-hemisphere twice over, so the comparator for the 2026 study is ≈4 × 10¹⁰ GC total. | "Approximately 1 µl (2 × 10¹⁰ GC/hemisphere) virus was dispensed … The other hemisphere was injected in the same way." | `PMID34747138_locators.md` / `deepdive_manifests/PMID34747138.json`, Methods, local JATS XML surface — **artifact bytes absent from this checkout, attestation carried forward, re-acquisition owed** |

**What is still pending:** operator authorisation (§9); a blind locator audit of the figure triples
(Appendix Fig S1A, Repudi Fig 2C, Obeid Fig 3B) is **not runnable** until the bytes are re-acquired — that
is the one gate this wave could not discharge, and it bears only on the figure triples, not on the six
text triples above.

### Addendum — a cross-file contradiction this candidate already resolves, recorded so the resolution is findable

Two analysis files still say the question is open: `analysis/model_horizon_and_p47t_platform_20260922.md`
lines 174–179 — *"The one surface that could still carry a WPRE is `Appendix Fig 1`, the vector schematic —
which is referenced in the Results and was NOT served… The unread 2021 Appendix vector map remains the only
way to close it"* — and `analysis/tx007_dose_challenge_20260922.md` line 505, which names the same unread
Appendix. 🔴 **It is not unread.** §1–§2 of this candidate read it on 2026-08-26 at 300 dpi from
`EMMM-13-e14599-s001.pdf` page 2 (`source_pdf_sha256 1e5c30a9…f86cd2`, `image_sha256 e362bdf8…c61f9c02`) and
found **all three constructs WPRE-free**. ⇒ the 2021 vector question is **closed**, and the repository's
phrase *"the configuration of the 2021 proof-of-concept"* is an inference that the Appendix **contradicts**
rather than merely fails to support. This wave relabelled the live site
(`analysis/tx007_genotype_class_ceiling_20260921.md`, dated correction block) and left the two files above
untouched, because they are not this package's targets — a one-line pointer in each is the cheapest possible
follow-up and is named here so it is not rediscovered a third time.
⚠️ Stated with its own limit: the 300-dpi render is **not present in this checkout** (`files/` holds none of
the 10 artifacts of PMID 34747138), so this is the recorded attestation of the reading session, replayable
from a reader's own copy by the §1 recipe and not re-verified today.

## BATCH DISPOSITION — `BATCH_20260927_004` (2026-09-27, ACTOR_ID `scientist`), append-only

**Verdict: `PROPAGATED`.** `CLAIM 004`'s dose-and-configuration boundary applied record-scoped, and `DIS-021` appended once for the whole dose family (this candidate and `CC-20260826-DOSE-DECISION-TABLE-01` proposed the same entry; one was written). Blind audit `research/locator_audits/2026-09-27_wave2_audit_A.md`: **6 of 6 SUPPORTED**, 0 OVERSHOOT, 0 UNDERSHOOT. Two things the audit changed in the wording. 🔴 **First, a readiness claim of this candidate was FALSE and is corrected in the propagated text:** triple 6's anchor declared the Repudi artefact *«bytes absent from this checkout, attestation carried forward, re-acquisition owed»*. The bytes are present at `files/fulltext/PMID34747138_Repudi2021_PMC.xml`, sha256 `7da156e8…`, and **both** Methods sentences were re-verified verbatim by this batch. No re-acquisition is owed, and the record now says so. ⚠️ **Second**, the audit's note that the ≈4 × 10¹⁰ GC total is **arithmetic over two sourced sentences and not an assertion of the source** is written into the claim. The Appendix Fig S1A WPRE-free reading stays a **declared 300-dpi figure attestation**: the render exists in no checkout reachable here, so the audit could not adjudicate it and it is labelled as the reading session's attestation rather than promoted to a verified quotation.

**Operator authorisation, verbatim (2026-09-27, given in writing after being shown the MAJOR proposals):** *«procedi tu, ti autorizzo su tutto»*. **Mirror ex-post review due** under §21e — see `session_evaluations/2026-09-27_BATCH_20260927_004.md`.
