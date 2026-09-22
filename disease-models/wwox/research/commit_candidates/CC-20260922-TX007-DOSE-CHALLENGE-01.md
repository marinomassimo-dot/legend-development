# COMMIT CANDIDATE — CC-20260922-TX007-DOSE-CHALLENGE-01

**Source:** Scientist J, `TX-007` dose challenge
([`tx007_dose_challenge_20260922.md`](../../analysis/tx007_dose_challenge_20260922.md)).
**Four load-bearing claims re-verified by the Orchestrator**; two more are carried at the
delegate's read depth and labelled as such.
**Change class:** 🔴 **MODERATE.** It removes two false corroborations from the entry that carries
the portfolio's **strongest** therapeutic arm at belief `alto`, and corrects a citation that is
wrong in three mutually inconsistent ways.
**Target:** `discovery_ledger_current.md` `DL-MOL-005` · three analysis files and two candidates
carrying the wrong journal name · `tx007_genotype_class_ceiling_20260921.md`.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R3** — it lowers the evidential standing of the gene-replacement axis.
**Proposes:** `D-33` — *"a within-study control is not a replication, and a predecessor from the
same laboratory is not independent corroboration."*
**BLOCK-1:** no molecule, no dose or route recommendation, no safety claim. Doses appear only as
what a paper used. *"No overt toxicity observed"* is not *"safety established."*

---

## 1 · 🔴 Zero independent replication. Verified.

**Reproduced by the Orchestrator, exactly:**

```
WWOX AND (AAV9 OR AAV OR adeno-associated)   →   total_count: 3
query_translation: ("wwox protein human"[Supplementary Concept] OR
                    "wwox protein human"[All Fields] OR "wwox"[All Fields])
                   AND ("AAV9"[All Fields] OR "AAV"[All Fields] OR "adeno-associated"[All Fields])
```

**Fully expanded** — the `wwox protein human` Supplementary Concept fired, so **the zero-trap is
ruled out and the `3` is a measurement.** The three records are `42422765` (primary), `34747138`
(primary) and `42128308` — **a review by the same authors.**

**And they are one laboratory.** Verified from the 2026 metadata retrieved this session: **Aqeilan
RI is senior author**, **Repudi S** is third author of 2026 and **first author of 2021**, same
institution (Lautenberg Center, Hebrew University–Hadassah). Positive control, identical query form:
`SCN1A AND (AAV9 OR AAV OR adeno-associated)` → **25**.

🔵 **Stronger than "a small field":** `Aldaz CM[Author] AND Wwox AND (mouse OR mice)` → **18**. An
independent laboratory has held WWOX mouse models for ~20 years and **its intersection with the AAV
set is empty.** The capability exists elsewhere and has not been used.

⚠️ **And the delegate bounded its own negative, live.** `WWOX AND (… OR intracerebroventricular)`
returns **10 records and neither primary is among them**, although both delivered by ICV and both use
the word in their bodies. **The two papers that did the thing are invisible to a query for the
thing.** So the `3` is a floor on the *findable* literature, not a proof of absence — **a fourth
demonstration, after the punctuation trap, the bare-number `[UID]` trap and `[All Fields]` not
indexing Methods, that a query count needs its bound stated.**

---

## 2 · 🔴 `DL-MOL-005` asserts two corroborations that do not exist

`discovery_ledger_current.md:112`, verbatim:

> **Evidenza: supporta** = rescue multi-dominio, dose-dip., durevole a P300, **replicato
> mWwox≈hWWOX**, neuron-specific senza espressione epatica (S6); **proof-of-concept 2021
> indipendente**; convergenza con rescue ectopico organoidi (MECH-007)

**Both emphasised items are false as corroboration, and this entry holds belief `alto` on a stated
basis of *"convergenza multi-livello."***

| asserted | what it actually is |
|---|---|
| *"proof-of-concept 2021 **indipendente**"* | 🔴 **the same laboratory** — same senior author, first author of 2021 is a co-author of 2026, same institution. **Not independent.** |
| *"**replicato** mWwox≈hWWOX"* | 🔴 a **within-study transgene control** (murine versus human coding sequence in one experiment), not a replication of a finding by anyone |

**Proposed:** strike *"indipendente"*, re-label the 2021 study **"proof-of-concept precedente dallo
stesso laboratorio"**, re-label the transgene comparison **"controllo intra-studio, non una
replicazione"**, and add: **"nessun laboratorio indipendente ha replicato alcuna parte della
sostituzione genica di WWOX (censimento 2026-09-22: 3 record, un solo laboratorio)."** `D-33`.

🔵 **The datum is not demoted; the corroboration is.** The multi-domain rescue, the durability to
P300 and the absence of hepatic expression all stand as measured. What changes is that they rest on
**one laboratory and, for the dose axis, one experiment** — because `34747138` administers a
**single** dose, so every dose–response statement rests on `42422765` alone, and inside it on two
figures.

---

## 3 · 🔴 The journal is cited three ways, none of them right

According to PubMed, PMID 42422765 is ***Molecular therapy. Advances*** (`Mol Ther Adv`), **34(3):201791**, [DOI](https://doi.org/10.1016/j.omta.2026.201791), `PMC13343157`. In this repository:

| cited as | where | count |
|---|---|---:|
| ⛔ *"Mol Ther Oncol"* | `downstream_wwox_independent_rescue_census`, `tx007_genotype_class_ceiling`, `earliest_lesion_developmental_timeline` | **7** |
| ⛔ *"Mol Ther Methods Clin Dev"* | `PMID42422765_partial_locators`, `CC-20260826-SEIZURE-RECONCILIATION-01`, `CC-20260826-LOCATOR-PACKET-01` | **3** |
| ⛔ *"OMTA (Mol Ther Methods Clin Dev)"* | `discovery_ledger_current` | 1 |
| ✅ *"Mol Ther Adv"* | `discovery_ledger_current:714` | 1 |

**Three wrong variants, mutually inconsistent, and the correct name sits in the same file as one of
them.** ⚠️ **Repaired 2026-09-22 — and the census undercounted.** The delegate named 11 occurrences in
7 files; a repository-wide sweep found **14 in 10** — the three extra being
`CC-20260826-CLAIM037-01.md` (a superseded candidate),
`denominator_audit_therapeutic_portfolio_20260922.md` and
`postdiagnosis_window_evidence_20260922.md`. **All 14 corrected.** ⚠️ **My own first count of this
was 13 in 9** — the third file surfaced only on re-running the sweep after the first repair pass,
which is the argument for re-running a sweep rather than trusting its first result. The occurrences in the
table above are deliberately left as written: they are the record of the defect, and repairing them
would erase it. The DOI is correct everywhere — so the drift is purely in the human-readable name, expanded
from `omta` by recall, three separate times. ⚠️ **On the very paper whose own near-miss record is
about a DOI reconstructed from memory of the journal.** Same failure class, same paper, still live.

**Proposed:** one pass over the eleven occurrences. Trivial to fix, and left alone it is the kind of
citation a reader cannot resolve.

---

## 4 · Carried at the delegate's read depth — flagged, not promoted

These two are the report's sharpest scientific findings and I **could not verify them from local
artefacts** (the relevant strings are not in the local manifests; `files/` is absent and the raw
JATS/PDF surface is `403 at CONNECT`). They are recorded as **delegate-read, pending confirmation.**

**(a) 🔴 The 2021 proof-of-concept censored two thirds of its main arm, and it is in the legend.**

| 2021 arm | total | spontaneously dead | removed by investigators | mortality among non-removed |
|---|---:|---:|---:|---:|
| AAV9-hSynI-**mWwox** | 18 | 6 | **12 (67%)** | **6/6 = 100%** |
| AAV9-**hWWOX** | 16 | 6 | 4 | 6/12 = 50% |

Animals removed for ephys/EM/histology are removed **at scheduled times and in usable condition** —
non-random by construction, **in the direction that flatters survival**, with no sensitivity
analysis. **And the two arms disagree on mortality, 100% versus 50%, while the paper concludes
*"No difference was noted when using the murine or human WWOX vectors."*** ⚠️ If confirmed, this
strengthens the `denominator_audit`'s out-of-sample case, which quotes that same legend and **did
not read the censoring inside it**.

**(b) 🔴 The non-monotonicity is text-versus-text, not a panel-reading doubt.** Two running-text
sentences, same paper, same WPRE-lacking vector: *"Increasing the dose … to 8 × 10¹⁰ vg was
associated with improved outcomes, including rescue of lethality"* — and — *"LD-treated mice did not
survive to P90"*, where LD = **1.23 × 10¹¹ vg**, ≈1.5× **higher**. The repository currently resolves
this by granting the presumption to the text over a doubted panel; **if both sides are text, that
resolution does not work.**

🔵 **And the cheapest explanation is a unit, not a biology:** the 2026 doses are bare `vg` — no
`/hemisphere`, no `total` — while the Methods deliver **2.0 µL/hemisphere bilaterally** and the 2021
paper states **`GC/hemisphere`**. Per-hemisphere-versus-total is **2×**; the LD→HD step is **2.1×**.
**The unit ambiguity is the size of the effect it is being used to measure.**

---

## 5 · Threshold versus continuum — the repository is closer to right and still one word too confident

One ordered pair of doses, corroborated across three concordant endpoints (survival; glucose P20;
GFAP S7H) with **no expression correlate** (7 of 8 regions `ns`).

> **Not a dose–response curve; also not a clean threshold — a threshold is a claim about a function,
> and two points do not define one.**

The repository's *"threshold, not a continuum"* beats the paper's *"clear dose-response
relationship"*, and the paper's strongest sentence overreaches both: *"providing **strong mechanistic
evidence** of on-target activity"* — asserted on the **one layer that failed to separate the arms.**

⚠️ **Two measurement facts worth keeping:** both papers titrate **by qPCR only**, with no orthogonal
method and **no titration-uncertainty statement**; and the Methods name **four vector sources** and
**assign no arm to any of them**, so a preparation/lot contribution to LD-versus-HD cannot be
excluded. **Recorded as *cannot verify*, not as allegation.**

---

## 6 · The regional signal, kept separate — and a five-year absence

🔴 **`cerebell` occurs 7× in the 2026 body and every one is expression, distribution or blot. There
is no cerebellar functional endpoint of any kind — in either primary, across five years.**

⚠️ **And do not merge the transduction fractions:** 2026 reports ~40%→55–60% of NeuN⁺, 2021 reports
60–70% — the later, higher-dose study reports a *lower* fraction, but the numbers are **not
comparable** (±WPRE; the 2026 text says WPRE signal *"preclud[ed] quantification"*). **"Higher dose"
and "more neurons reached" are not the same quantity here.**

🔵 **This composes with a finding from the same day:** the human developmental array shows the
**cerebellar cortex** is the one region with *"a more significant increase in early postnatal life"*
— and it is the region with the **weakest vector coverage and no functional endpoint.** Two reasons
to keep that axis separate, now pointing in opposite directions.

🔴 **And the portfolio's strongest "no level control" evidence has no recorded dose.** The
0.4×–7× protein spread and the ~11× SATB2 overshoot come from `42397075`, whose entire LEGEND record
(dossier + manifest) contains **no `vg`, `MOI`, `titer` or `dose`** — only `125 nM` of A51. So the
17-fold spread **cannot be attributed to dose or to line.** A retrieval debt, not a finding about
the paper.

---

## 7 · The delegate's own discipline, recorded because it is the standard

- ⚪ **It raised a suspicion and killed it.** Having found that `34268881`'s *"W-AAV"* is named for
  the **AAVS1** safe-harbour locus and not an AAV vector (*"targeting the safe harbor locus
  **AAVS1** … under **UBP** promoter"*, with the rescue done by **lentivirus**), it checked whether
  LEGEND's `AAV9` attribution for `42397075` was the same confusion. **It is not** — the dossier
  quotes *"neuron-targeted AAV9-hSynI-WWOX restoration"* verbatim. **The repository was right and
  the delegate said so.**
- ⚪ **It recorded a summariser's gloss as a defect:** a web search whose nine links were all the
  same two papers nonetheless concluded *"publications from multiple laboratories … an active area of
  research"* — **false, and generated from one laboratory.** The cheapest available demonstration
  that a generated summary is not a census.
- ⚪ **It declined to claim an `FT-` entry it did not need**, having checked every PMID against queue
  and registry first, and deliberately did **not** name two search-only PMIDs as premises.
- 🔵 **It extended the extraction-damage class three ways:** **zero `n =` tokens and zero P-values
  survive**; **the extracted body contains no figure captions at all** (so caption statistics quoted
  earlier came from a local HTML surface **absent from this worktree** — two surfaces of one paper
  differing by ~39,000 characters and by the entire statistical apparatus); and **chemical
  subscripts go too** (`CO₂`→`CO`, `H₂O₂`→`HO`). **The class is every super/subscript numeral, not
  just vector exponents.**
- 🔵 **One exponent form survives extraction: E-notation.** *"all vectors were tested at the same
  titer (4E10)"* came through intact. **Worth knowing for every future dose read.**

---

## 8 · The experiment, and why it is not the one already queued

A **single-lot, unit-declared, four-arm ICV dose series** at one fixed WPRE configuration spanning
4 × 10¹⁰ → 2.63 × 10¹¹ — **including the 8 × 10¹⁰ / 1.23 × 10¹¹ pair the literature currently
contradicts itself on** — with: **two orthogonal titration methods and a stated CV**; **dose reported
both per hemisphere and as total, with the volume, in one sentence**; **one pre-declared survival
horizon in every arm**; **all tissue removals pre-scheduled, with Kaplan–Meier reported twice, with
and without censoring**; **ECoG P14–P21 and glucose P10/P20 as primary** — the endpoints survival
cannot manufacture; and **achieved protein per region per animal**, so expression can be *regressed*
on dose instead of compared as group means, which is what produced 7-of-8 `ns`.

🔵 **And at least once by a laboratory that is not the originating one.** An independent replication
of the last two items at two doses would be worth more than a third dose arm from the same group.

🔴 **This is not `CLAIM 011`'s queued intermediate-dose arm.** That instinct is right, but **a third
point on a ruler with an unstated unit, unreported titration error and a non-monotone prose axis is a
third point on an uncalibrated ruler.**

⚠️ **One route fact that survives everything above:** the two papers' doses are **not on a common
scale even if the exponents and units were settled** — 2021 injected **~1 µL/hemisphere free-hand**,
2026 **2.0 µL/hemisphere stereotaxically**. Volume and technique both change CSF distribution, and
settling the exponents would not fix it.

---

## 9 · 🔴 APPEND-ONLY CORRECTION — §4a's arithmetic is right and its interpretation overreached

Scientist M retrieved `PMC8649866` and verified §4a number by number. **The Orchestrator then
retrieved the same body independently and confirms every item below.** According to PubMed, Repudi
*et al.* 2021, *EMBO Mol Med* ([DOI](https://doi.org/10.15252/emmm.202114599)).

### 9a · The legends, verbatim — every number in §4a is CORRECT

> **Fig 1C:** *"Kaplan–Meier survival graph indicates prolonged life span of knockout mice injected
> with AAV9‐hSynI‐mWwox [**total= 18, spontaneously dead= 6**, mice taken out for
> electrophysiology/electron microscopy/analysis, **are shown in yellow,= 12**] compared to mice
> injected with AAV9‐hSynI‐GFP (= 6) or the non‐injected (= 8); **< 0.0001, log‐rank Mantel–Cox
> test**."*

> **Fig 2C:** *"…AAV9‐hWWOX [**total= 16, alive= 6, spontaneously dead= 6, 4 mice (shown in yellow)
> were taken out for analysis**) compared to the non‐injected (= 8)] (**< 0.0001, log‐rank
> Mantel–Cox test**)."*

18 / 6 / 12 and 16 / 6 / 6 / 4 — **all verified.** (The extractor deletes every `n` token, so
`total= 18` is `total n = 18`; the numerals are intact and the deletion is stated, not repaired.)
The equivalence sentence is verbatim too: *"No difference was noted when using the murine or human
WWOX vectors"*, and in the Discussion *"our analyses did not reveal any difference between mWwox and
hWWOX vectors."*

### 9b · 🔴 But §4a's interpretation is wrong in three ways, and the first is the important one

**1. It IS a Kaplan–Meier, and the censoring IS marked.** Both arms are KM curves with a log-rank
Mantel–Cox test at `p < 0.0001`, and both legends state the removed animals are ***"shown in
yellow"*** on the curve. **Kaplan–Meier is the standard handling of animals withdrawn before the
event** — they are censored at withdrawal and displayed. **§4a's framing that the survival analysis
is "conditioned on a non-random removal" is withdrawn.** It is not a naive proportion among the
non-removed; it is a time-to-event estimate that censors and marks them.

**2. *"Removed at scheduled times"* is not in the paper.** Fig 1C says only *"taken out for
electrophysiology/electron microscopy/analysis"*; Fig 2C says only *"taken out for analysis"*.
**No age, no schedule and no criterion is stated for any removal.** That was the delegate's
inference and is withdrawn as a quotation.

**3. The direction of bias is undetermined, and for much of the cohort it points the other way.**
The adult experiments that consumed those animals are at **6 months** (adult cell-attached
recordings; corpus-callosum EM) and **8–9 months** (aged open field) — verified verbatim in the
figure legends. **Late censoring does not inflate a survival curve the way early censoring does.**
§4a's *"in the direction that flatters survival"* is withdrawn as unestablished.

### 9c · 🎯 What survives is a better finding than the one it replaces

**What remains true, and is the real defect:** the paper **never states that censoring is
non-informative**, never gives the age or selection criterion for a single removal, and runs **no
sensitivity analysis** — the Statistical analysis section names only *"The two‐tailed unpaired
Student's‐test or two‐way ANOVA with Bonferroni for post hoc comparisons."* **Kaplan–Meier is
unbiased only if withdrawal is independent of prognosis, and that assumption is neither stated nor
tested.** The Discussion's limitations concern oligodendrocyte function, tumour surveillance in
*"the limited number of adult"* mice *"(age 8–11 months)"* and the P0 treatment age — **not the
survival cohort.**

🔴 **And the sharper point, which replaces the 100%-vs-50% contrast entirely:**

> **Nobody compared the two vectors, in either direction.** The paper asserts *"No difference was
> noted…"* **while running no statistical comparison between the two arms** — each arm is tested
> only against its own untreated controls. *An untested equivalence is not equivalence.* **But
> §4a's counter-evidence is not a valid time-to-event comparison either:** *"mortality among
> non-removed"* is a statistic with **no time axis**, neither legend reports a death time, and the
> cheapest explanation of 100% versus 50% is **follow-up duration** — the hWWOX arm still had
> `alive= 6` at write-up while the mWwox arm was carried to 6–9 months. A cohort followed longer
> accrues more deaths.

**Both the paper's claim and the candidate's counter-claim are unsupported. That is the finding.**

### 9d · Two further items verified in the same read

- ✅ **The 2021 paper never mentions WPRE.** Its vectors are `AAV9‐hSynI‐mWwox‐IRES‐EGFP`,
  `AAV9‐hSynI‐hWWOX` and `AAV9‐hSynI‐EGFP`. So the repository's *"the configuration of the 2021
  proof-of-concept"* **is an inference from the 2026 paper's framing, not a 2021 statement** —
  confirmed, and it should be labelled as such.
- ✅ **The dose and its unit, verbatim:** *"Approximately 1 µl (2 × 10GC/hemisphere)"* — exponent
  deleted by the extractor, **and explicitly per hemisphere, free-hand.** This confirms §4b's unit
  point from the other side: the 2021 paper states its unit and the 2026 paper does not.
- 🔵 **And a contrast worth recording:** 2021 declares *"The authors declare that they have no
  conflict of interest."* The 2026 paper carries three Mahzi Therapeutics co-authors. **Not a defect
  in either paper — a fact about how the axis's evidence base changed between them.**

**§4a is therefore replaced by §9. The arithmetic stands; the interpretation does not.**

---

## 10 · 🔴 APPEND-ONLY — the 2.1× step is ROBUST, and *"the ambiguity is the size of the effect"* is a CATEGORY ERROR

Scientist O ran the forensic audit the Operator ordered. **Verified by the Orchestrator.**

### 10a · The unit ambiguity is a common-mode multiplier and cancels out of the ratio

LD and HD are stated **in one sentence, one token form, one figure, one experiment**, and the Methods
deliver **the same 2.0 µL/hemisphere bilaterally to every arm**. Let *u* convert written `vg` to total
vg (*u* = 2 if per-hemisphere, *u* = 1 if total). **The same *u* applies to both arms:**

```
HD/LD = (u · 2.63×10¹¹) / (u · 1.23×10¹¹) = 2.63/1.23 = 2.1382      ← u cancels
```

**Recomputed by the Orchestrator under every permitted reading:**

| reading | LD total | HD total | **HD/LD** |
|---|---|---|---|
| per hemisphere | 2.46×10¹¹ | 5.26×10¹¹ | **2.1382** |
| total per animal | 1.23×10¹¹ | 2.63×10¹¹ | **2.1382** |
| per injection (≡ per hemisphere) | 2.46×10¹¹ | 5.26×10¹¹ | **2.1382** |

The four-point span `4×10¹⁰ → HD` is **6.575× under both readings**. **Every ratio in the paper is
invariant. Only the absolute level moves, and by exactly 2×.**

> 🔴 **§4b's *"the unit ambiguity is the size of the effect it is being used to measure"* — which I
> wrote and also reported to the Operator — is a category error. A common-mode multiplier cannot
> corrupt the ratio it cancels from.** The defect is real and is confined to the **absolute** axis:
> LD ∈ [1.23, 2.46]×10¹¹ vg, HD ∈ [2.63, 5.26]×10¹¹ vg. **Withdrawn.**

### 10b · Classification: **`AMBIGUOUS BUT BOUNDED`**

**Not `UNAMBIGUOUS`** — the dose is written as bare `vg` on all three surfaces. **Not `INTERNALLY
INCONSISTENT`** — that was *tested*, not assumed: one Methods, one protocol, one volume, one token
form. 🔵 **The paper is consistently silent, not inconsistently specified — which is exactly why the
ratio is recoverable and the absolute dose is not.** The bound on the ratio is **degenerate**: a
single value.

### 10c · 🆕 The structural mechanism by which the unit was lost

🔴 **`PMID 42422765` states no dose in its Methods at all.** All seven `vg` tokens sit in
Results/Discussion; the Methods carry volume, rate, coordinates, needle, titration and four vendors —
**and no dose.** `hemisphere` occurs twice, both in Methods, **never adjoining a dose**; `GC`,
`per animal` and `total dose` occur **zero** times. **The dose and its unit live in different
sections, which is how the qualifier went missing.**

🔴 **And `LD` denotes two different doses about 1,000 characters apart** — *"lower dose (LD)
containing WPRE"* = 4×10¹⁰ **+WPRE**, versus *"an LD (1.23 × 10 vg)"* = 1.23×10¹¹ **−WPRE**. **3.1×
apart, opposite WPRE configuration, same two letters.** A reader who carries `LD` across those
thousand characters is comparing two different experiments.

### 10d · The non-monotonicity SURVIVES — and the unit work sharpens rather than dissolves it

The cheapest escape — a per-figure unit switch — is **positively excluded**, not merely unavailable.
The paper's own bridge sentence, ⚠️ **already held in this repository** at
`CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01.md:90` (the quotation is not new; **the use made of it
is**):

> *"However, this reduction in expression **necessitates the use of higher vector doses** to achieve
> comparable therapeutic outcomes."*

**That is a cross-figure magnitude comparison, and it requires one scale.** Under a single
convention, `LD / 8×10¹⁰ = 1.5375` — **a 1.54× higher dose fails where a lower one rescued.**
Contradiction intact.

🔴 **But `D-36` and its own logic still forbid inferring biological non-monotonicity.** Three
cheaper-than-biology explanations remain, and the leading one is new:
**(b) follow-up-horizon mismatch** — Fig 2 runs ~50 d against Fig 3's 300 d, and untreated KO die at
~15–20 d, so **at 50 days an LD animal that dies by ~90 d also reads as "rescued."** The served text
states **no Fig 2 horizon.**
**(c)** an erroneous sentence; **(e) 🆕** the `8 × 10` exponent is only **🟡 MEDIUM** — **if it is
8×10¹¹, the tension vanishes entirely.**

### 10e · Corrections to §4b and §9's provenance, and one upgrade

- 🔴 **§4b's *"text-versus-text"* framing is too strong.** The *sentences* are running text, but
  **both exponents are figure-derived** — the served body reads `10vg` on both sides. So it is
  text-versus-text on the claims and **figure-versus-figure on the numbers**, and a prior wave rated
  the `8×10¹⁰` exponent **🔴 LOW** while building on it a conflict it declared figure-independent.
- 🟢 **Upgrade:** the **2021** dose exponent is **🟢 HIGH, not 🟡** — `PMID34747138_locators.md`
  carries it from a **local JATS XML** (`surface: body`): *"Approximately 1 μl (2 × 10¹⁰
  GC/hemisphere)."* **The repository already held the primary rendering a prior wave said it lacked.**
- 🔴 **Downgrade:** the third LD/HD exponent surface (a web-search snippet) **fails on re-test** —
  it now returns *"a low dose (LD, 1.23 × 10 vg)"*, exponent deleted. The doses remain 🟢 HIGH on two
  primary-artefact renderings, **but the margin is one surface, not two.**

### 10f · The cross-paper convergence test — exactly symmetric, and it adjudicates nothing

| | 2021 (fully specified) | 2026 under per-hemi | 2026 under total |
|---|---|---|---|
| total/animal | 4.00×10¹⁰ GC | 8.00×10¹⁰ (**2×**) | 4.00×10¹⁰ (🎯 **1×**) |
| concentration | 2.00×10¹⁰ GC/µL | 2.00×10¹⁰ (🎯 **1×**) | 1.00×10¹⁰ (**0.5×**) |

**Each reading reproduces the 2021 experiment exactly on one derivable quantity and misses by exactly
2× on the other.** Reported as a **negative result** — it cannot adjudicate, and saying so is the
finding.

🔵 **And the delegate tested for `INTERNALLY INCONSISTENT`, the most damaging verdict available to
it, and reported that it does not hold.** That is the standard.

**§4b is therefore replaced by §10. The unit defect is real, bounded at exactly 2×, and confined to
the absolute axis — the 2.1× step itself is robust.**
