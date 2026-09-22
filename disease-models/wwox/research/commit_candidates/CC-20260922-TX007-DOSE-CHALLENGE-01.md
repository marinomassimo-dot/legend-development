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
them.** The DOI is correct everywhere — so the drift is purely in the human-readable name, expanded
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
