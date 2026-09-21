# COMMIT CANDIDATE — CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01

**Source:** Scientist B, node `TX007_GENOTYPE_CLASS_CEILING`
([`tx007_genotype_class_ceiling_20260921.md`](../../analysis/tx007_genotype_class_ceiling_20260921.md)),
reading `PMID 42422765` (Obeid 2026) in-act at a **measured 48,780 characters**, against LEGEND's
own strict-verified manifest for `PMID 42397075` (30 locators, figure-attested by a prior session
that had panel access).
**Ledger:** `fulltext_receipts.py verify` → **OK: 188 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — no claim reversed, no status moved, no block redefined. What changes
is the **safety and dose-control description** of the portfolio's north-star strategy, plus one
`CLAIM 011` extension and one method note.
**Target:** `working_model_version` MINOR bump at batch time. **No `BLOCCO 1` change** — see §5.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R3.** `TX-007` is the strategy a treating team is most likely to act on, and
this candidate lowers a `SAFETY` score. It reverses nothing and narrows no claim, so `R4`
(`legend-locator-audit`) is not triggered — but see the provenance caveat in §0, which a reviewer
should treat as the first thing to check.

---

## 0 · Provenance, declared before any number is used

🔴 **Two different kinds of number appear below and they must not be mixed.**

| Kind | Where it comes from | How to treat it |
|---|---|---|
| **Prose values** (regional fold-changes, `ns` counts, author quotations) | Scientist B's in-act fetch of `PMID 42422765`, body measured at 48,780 characters | Verifiable by re-fetch. Ordinary evidence. |
| **Vector-genome doses** (`1.23 × 10¹¹`, `2.63 × 10¹¹` vg) | 🔴 **NOT from the fetch.** They come from `CLAIM 011`'s prior-session raster read of `gr3.jpg` | Figure attestation from a session that had panel access. **This session cannot see panels** and does not claim to. |

**Why the distinction is not pedantry — a new extraction-damage class, and it is a safety one.**
The PMC extractor **deletes superscript exponents from vector-genome doses**. The body returns:

> *"an LD (1.23 × 10vg) and a higher dose (HD, 2.63 × 10vg)"* · *"a dose of 4 × 10vg"*

**`10vg` is `10¹¹ vg` with the exponent silently removed.** Anyone quoting a dose from extracted
PMC text in this literature will print a number wrong by **ten orders of magnitude**, in a document
about administering a virus to an infant. This joins the italic-token deletion already recorded by
`extraction_damage_report.py`. ⇒ proposed as a new row in the damage register, §4(d).

---

## 1 · The finding: `TX-007` has a measured efficacy FLOOR and no measured CEILING

`CLAIM 011` already records the floor, and records it correctly and sharply: Figure 3B places a
**threshold** between `1.23 × 10¹¹` and `2.63 × 10¹¹` vg — the low dose does **not** rescue
survival, the high dose plateaus at ~80 % to 300 days — and it already flags that the paper's own
words *"dose-dependent"*, *"graded improvement"*, *"a clear dose-response relationship"* describe a
continuum the panel refuses.

**What nothing in LEGEND carries is the other side.**

### 1a · The floor is bracketed in vector genomes and **not in biology**

Two doses **2.1-fold apart** produce **opposite survival outcomes** while being **statistically
indistinguishable** on vector genomes and on mRNA across four brain regions — **7 of 8 comparisons
`ns`**. So the minimum effective dose is known as a *number of capsids*, and the biological
quantity it corresponds to is **not measured**.

⚠️ The paper offers an explanation, and it does not survive its own design: *"mice… that failed to
survive exhibited reduced WWOX expression"* is **survivor-versus-non-survivor**, i.e. conditioned
on the outcome it explains. Supplementary S5 marks **one HD and three LD animals dead**.

### 1b · The window is **regional, not scalar** — and the ataxia target organ is the one it misses

WWOX expression at P300, high dose, relative to wild type:

| Region | P300 HD (panel 1) | P300 HD (panel 2) | With WPRE (Fig 2E) |
|---|---|---|---|
| Cortex | **8.2×** | 4.6× | **25.6×** |
| Hippocampus | **10.7×** | 4.7× | **22.3×** |
| Midbrain | 5.6× | 3.1× | 11.6× |
| **Cerebellum** | 🔴 **1.4×** | 🔴 **0.6×** | 6.2× |

🔴 **One systemic dose over-expresses forebrain by roughly 5–11× and leaves the cerebellum at or
below wild type.** The cerebellum is where `SCAR12`'s ataxia lives, where `CLAIM 039` sits, and
where the `P47T` mouse degenerates. **The therapy's own biodistribution under-doses the organ that
carries the ataxic phenotype, at every dose and timepoint reported.**

And the design choice that produced it is recorded: **`WPRE` was removed**, and `DL-MECH-009`
already holds that `WPRE` was **the element that most boosted cerebellum (16.7×)**. The authors'
own account of the trade-off, quoted:

> *"Although no overt toxicity was observed in prior studies, we removed WPRE as a proactive
> risk-mitigation step."*

⚠️ **That is a non-observation, not a safety result** — and the sentence is worth reading twice,
because it is the shape this repository has been burned by: an absence of looking narrated as an
absence of harm. The consequence is stated by the authors too:

> *"this reduction in expression necessitates the use of higher vector doses."*

⇒ **the safety margin is bought with more capsid**, which is itself the dose-limiting toxicity axis
for AAV9 in the CNS.

### 1b-bis · 🔴 THE CEREBELLAR SIGNAL IS A SEPARATE FINDING FROM THE DOSE FINDING — Operator note, 2026-09-21

Added because the two get collapsed the moment they are written in one paragraph, and they have
**different evidence, different consequences and different remedies.**

| | **The dose finding** | **The regional finding** |
|---|---|---|
| **What it says** | the minimum effective dose is bracketed **in vg and not in biology**, and no maximum is measured at all | one systemic dose produces **5–11× wild type in forebrain and 1.4×/0.6× in cerebellum** |
| **Evidence** | 7-of-8 `ns` regional comparisons across two doses with opposite survival outcomes | per-region expression at P300, and the `WPRE` design record (`DL-MECH-009`, cerebellum 16.7×) |
| **Whom it affects** | **everyone** — it is a property of the therapy at any dose | **most sharply the ataxic phenotype**, i.e. `SCAR12` and the cerebellar limb of `CLAIM 039` |
| **What would fix it** | a dose–expression–toxicity study reporting achieved protein per region with tumour surveillance | **not more dose** — see below |
| **Direction** | uncertainty, in both directions | 🔴 **a shortfall, in one direction, in one organ** |

🔴 **The reason they must not be merged: raising the dose does not fix the regional gap, and the
regional gap is not evidence about the ceiling.** If the cerebellum sits at 0.6–1.4× while the
forebrain sits at 8–25×, then a dose increase sufficient to bring the cerebellum to wild type would
push the forebrain **further into the range nobody has measured a ceiling for**. The two findings
**constrain each other from opposite sides**, and a sentence that says only *"expression is
dose-dependent and broadly distributed"* loses both at once.

⚠️ **What the regional finding is NOT.** It is **not** a claim that the therapy fails, **not** a
claim that ataxia will not respond, and **not** a comparison anyone has tested against outcome. It
is a **biodistribution observation**: the organ carrying the ataxic phenotype is the organ the
vector reaches least, at every dose and timepoint reported. **No efficacy endpoint was measured in
cerebellum**, so whether 1.4× is sufficient there is unknown — which is the point, and is why it
needs its own line rather than a clause inside a dose sentence.

🔵 **And it is a design question with a known lever, which the dose finding does not have:** route
and capsid, not titre. `WPRE` — removed for safety — was the element that most boosted cerebellum.
That trade is recorded in `DL-MECH-009` and is the concrete thing a programme could revisit.

### 1c · Nobody has asked whether too much WWOX harms a neuron

A bounded census — `(WWOX OR WOX1) AND (ectopic OR overexpression OR transfection) AND apoptosis
AND (neuronal terms)` — returns **`total_count: 2`**: one review LEGEND already holds, and
`PMID 22534828` (Chang/NCKU; COS, cancer and neuroblastoma lines; **abstract only**; independence
caution applies). **No published experiment asks the question.**

In the 2026 dose-ranging body: `overexpress` = 0, `supraphysio` = 0, `apopto` = 0, `threshold` = 0,
and **no tumour surveillance of any kind** (`tumor` appears three times, all in the Introduction).

🔴 **This matters more for WWOX than for a typical gene-addition target**, and LEGEND already knows
why: `CLAIM 028` records that *"more WWOX = better" is not a safe default*; `N-05` states the
principle *"neither too little nor too much WWOX"*; WWOX induction is pro-apoptotic in several
published systems; and WWOX is a **tumour suppressor** being delivered at 8–25× wild type into a
developing brain for life, by a vector with **`REVERS 0`**. **LEGEND holds the principle and not one
datum.**

---

## 2 · The genotype-class question, answered — and the answer is a refusal

**Asked:** should `TX-007`'s progenitor caveat be qualified as graded by genotype class?
**Answer: NO. Leave it general.** The evidence forbids the qualification, in two independent ways.

1. 🔴 **No isogenic comparison across genotype classes exists.** The isogenic axis is real but runs
   only WT-versus-KO on one background (`JH-iPS11` vs `JH WKO-1C/2C`, `KO-A2`, `KO-1B`). **Every
   patient line is a different donor on a different background** — WOREE `WSM S` (`c.517-2A>G`
   hom), `LM-iPS` (`c.864G>A` / ~93 kb deletion), `WCH S` (compound het); SCAR12 `WPM S` / `WPM D`
   (`c.1114G>C` hom). **Genotype and donor background are perfectly confounded.**
2. 🔴 **Within-genotype, within-background variance is itself significant.** Two **isogenic**
   knockout clones differ on the progenitor readout — `SOX2⁺MYC⁺/SOX2⁺` ≈ 43 % (`KO-A2`) versus
   ≈ 54 % (`KO-1B`) — with a **significance bracket drawn between the two knockout clones**. Clone
   variance is measurable, significant, and unpartitioned. **A between-line difference not shown to
   exceed it cannot be called a genotype effect.**

**And the "patient lines are near-normal" reading, which this repository has been carrying, needs
narrowing rather than promoting:**

- the **lesion is shared**: MYC activation in radial glia is present in the KO **and** both patient
  lines at comparable magnitude (pseudobulk log2FC ≈ 1.8 / 1.65 / 1.6). The prior session's own
  self-correction (manifest entry 25, *"QUALIFIES MY OWN CLAIM, WHICH WAS TOO FLAT"*) was right,
  and manifest entries 2 and 25 are **not in conflict** — they measure different layers;
- on mitotic progenitors **WOREE carries a `*`** (≈ 6 % vs WT ≈ 3 %) — the patient class is **not**
  normal on that axis;
- **SCAR12 has no bracket at all**, and *untested is not normal*;
- both patient **whiskers reach ≈ 41 % and ≈ 44 %** against a WT median of ≈ 3 % — near-normal
  medians inside wildly dispersed, unpowered distributions;
- the **cell-cycle phase distribution — the paper's own mechanistic bridge — is plotted with no
  error bars and no significance markers even in the knockout**, and has **never been measured in a
  patient line at all**.

> ✅ **The honest statement:** the progenitor **lesion** appears shared across genotype classes; its
> **consequence** appears graded; and the gradation **cannot be attributed to genotype** with the
> data as published. `TX-007`'s caveat stays general. **This is a refusal to take a favourable
> reading, not a finding of harm.**

---

## 3 · What is proposed

**(a) `TX-007` scoring line** — `SAFETY 1–2` → **`SAFETY 1`**, with the reason named:

> **SAFETY 1** — AAV9 CNS in `n = 1` human, immunogenicity/dose/long-term unknown, **and now
> also: no measured upper bound on expression.** Achieved WWOX runs **8–25× wild type in forebrain
> at P300** while the **cerebellum never reaches wild type at any dose or timepoint**; restored
> protein across rescued human lines spans **0.4×–7×**; `SATB2` overshoots to **~11×**. **No
> published experiment asks whether excess WWOX harms a neuron** (`total_count: 2`, one review +
> one abstract-only), and the 2026 dose-ranging study performs **no tumour surveillance**. With
> `REVERS 0`, an unmeasured ceiling is not a gap in knowledge — it is an unbounded, irreversible
> exposure.

**(a-bis) `TX-007` — carry the regional finding as its OWN line, not inside the dose sentence:**

> ⚠️ **Biodistribution (separate from dose).** At P300 the achieved WWOX runs **5–11× wild type in
> forebrain and 1.4× / 0.6× in cerebellum** — **the organ carrying the ataxic phenotype is the one
> the vector reaches least, at every dose and timepoint reported.** **No efficacy endpoint was
> measured in cerebellum**, so whether that level suffices there is unknown. 🔴 **Raising the dose
> is not the remedy**: bringing cerebellum to wild type would push forebrain further into the range
> with no measured ceiling (§1c). The lever is **route and capsid, not titre** — and `WPRE`,
> removed for safety, was the element that most boosted cerebellum (`DL-MECH-009`, 16.7×).

**(b) `TX-007` window/age caveat** — append the genotype-class status of §2, **leaving the caveat
general**, and stating explicitly that the favourable reading was available and was refused for
cause.

**(c) `CLAIM 011`** — extend the existing threshold flag, which resolves the floor and is silent on
the ceiling:

> **Extension, 2026-09-21.** The same dose study that fixes the **floor** leaves the **ceiling**
> unmeasured. The two doses are `ns` on vector genomes and mRNA in **7 of 8** regional comparisons
> while differing in survival outcome, so the minimum effective dose is bracketed **in vg, not in
> biology**; the survivor-versus-non-survivor expression explanation is conditioned on its own
> outcome. Expression at P300 is **regional, not scalar** — forebrain 5–11× wild type, **cerebellum
> 1.4× and 0.6×** — and `WPRE`, removed as *"a proactive risk-mitigation step"* against *"no overt
> toxicity… observed"*, was the element that most boosted cerebellum (`DL-MECH-009`, 16.7×). The
> authors state the consequence: *"this reduction in expression necessitates the use of higher
> vector doses."* `PREMISE: NOBODY_LOOKED` on the upper bound.

**(d) `extraction_damage_report.py` damage register** — new row:
**`VECTOR_GENOME_EXPONENT_DELETED`.** The PMC extractor removes superscript exponents from dose
strings, rendering `1.23 × 10¹¹ vg` as `1.23 × 10vg`. **Ten orders of magnitude, in a dose.** No
dose may be quoted from extracted PMC text in this corpus without the figure or PDF behind it.

**(e) `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`** — one row:

> **D-21** · *"a gene-addition therapy's risk is the delivery, so more expression is at worst
> wasted"* · **Why it is FALSE here:** the target is a **tumour suppressor whose induction is
> pro-apoptotic**, delivered for life by a vector with `REVERS 0`, reaching **8–25× wild type** in
> forebrain — and the literature contains **no experiment asking whether excess WWOX harms a
> neuron**, and the dose-ranging study contains **no tumour surveillance**. LEGEND already held the
> principle (`CLAIM 028`, `N-05`, `FM-013`: *neither too little nor too much*) and **not one
> datum**, and the portfolio's `SAFETY` score carried the delivery risk only.
> **Detection rule:** for any restoration lever, ask for the **ceiling** in the same breath as the
> floor. A measured minimum effective dose with no measured maximum tolerated expression is half a
> dose-response, and the missing half is the irreversible one.

⚠️ **Numbering note:** `D-17` was **proposed and DEFERRED by the operator** on 2026-09-21 and is
**not** in the ledger. `D-18`, `D-19`, `D-20` are proposed by this session's other candidates.
`D-17` is **reserved, not free** — do not renumber into it.

---

## 4 · The resolving experiments, named

**For the genotype-class question — an isogenic allelic series on one background.** `JH-iPS11`: WT,
CRISPR null, plus **knock-ins of `c.517-2A>G` and `c.1114G>C`**; **≥3 clones per genotype, ≥3
independent differentiations**; scored on all four layers separately (RG fraction · proliferation
index · RG transcriptome · cell-cycle distribution). It is the only design that separates genotype
from donor background **and** partitions the clone variance that is already significant between two
isogenic knockout clones.

**For the ceiling — and this is the one a first-in-human programme needs.** A dose–expression–
toxicity study that reports, per region, **achieved WWOX protein relative to wild type**, with
**tumour surveillance** and an explicit **maximum tolerated expression**, in animals followed past
the 8–11 months the 2021 work qualified three times. Until it exists, the upper bound of `TX-007`
is an assumption.

## 5 · What is explicitly REFUSED

- ❌ **No `BLOCCO 1` change, and no clinical recommendation of any kind.** Nothing here tells anyone
  to do or not do anything. `TX-007` remains the portfolio's highest-scoring causal strategy and the
  only multi-pathway one demonstrated preclinically. **Lowering a `SAFETY` sub-score is not opposing
  the therapy; it is refusing to score an unmeasured quantity as if it were measured.**
- ❌ **No claim that WWOX overexpression is harmful.** The finding is that **nobody has asked**.
  `PREMISE: NOBODY_LOOKED`, not `PREMISE: HARM`.
- ❌ **No genotype-class qualification of the progenitor caveat** — refused for cause, §2.
- ❌ **No new gate or auditor** (§26). Two ledger rows and one damage-register row, all existing
  mechanism.
- ❌ **No figure panel is claimed as inspected by this session.** See §0.

## 6 · Growth delta

`claims +0 · papers +0 · corpus +0`. `CLAIM 011` is extended, not added.

---

*Sources retrieved from **PubMed / PubMed Central**.
DOIs — [42422765](https://doi.org/10.1016/j.omta.2026.201791) (PMCID `PMC13343157`) ·
[42397075](https://doi.org/10.1093/brain/awag239) ·
[34747138](https://doi.org/10.15252/emmm.202114599) (PMCID `PMC8649866`).
All three verified by `convert_article_ids` at drafting time, by copy, in the same act.

> 🔵 **A near-miss recorded because it is the rule working, not because it is interesting.** The
> first draft of this line carried `10.1016/j.ymthe.2026.01.014` for `PMID 42422765` — a DOI
> **reconstructed from memory of the journal**, never copied from anything. The true DOI is
> `10.1016/j.omta.2026.201791`. It was caught only because it had been flagged as unverified
> instead of being allowed to look finished. **An identifier assembled from recall is plausible by
> construction, which is exactly what makes it dangerous** — this is the third instance in three
> days of the same failure class in this repository, and the first caught before it was written
> into a durable record rather than after.

Not medical advice.*
