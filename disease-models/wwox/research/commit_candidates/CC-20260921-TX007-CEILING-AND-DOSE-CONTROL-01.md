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

---

## WAVE-2 READINESS (2026-09-27)

**Actor:** `scientist`, wave-2 package "dose". **context_policy declared:** `QUESTION_DRIVEN`.
**Surface read first-hand:** `files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml` (PMC JATS, sha256
`7bea83346b708e541d2c432e5da4029f69673e1abc3c6fe70926ad0e3ec2eef2`, efetch `db=pmc id=13343157`), re-acquired because `evidence_presence.py` reports **0 of 18**
declared artifacts present here. Receipt prepared, **not recorded**:
`scratchpad/receipts_pending/dose_42422765_1.json` (`FTR-20260927-42422765-07`).

### Verdict: **READY_MAJOR** — the candidate declares MINOR, and it is re-classified **MAJOR** here because it moves a `SAFETY` score on the portfolio's north-star strategy. **Not applied.**

**Re-classification, stated plainly.** §3(a) changes `SAFETY 1–2` → `SAFETY 1` on `TX-007` — the strategy a
treating team is most likely to act on. A score move on that record is not a MINOR annotation whatever its
content, and this wave's standing instruction is explicit: a `therapeutic_strategies_current.md` change that
moves a `SCORE` or `SAFETY` text is **not applied outside a batch** and is marked `READY_MAJOR`. The
candidate's own reasoning for MINOR (*"nothing is reversed"*) is correct about the science and does not
govern the class.

**What was done — the owed work, performed.**
1. 🔴 **The two author quotations are no longer unreceipted.** §0 declared them as coming from an in-act
   fetch with no persisted locator; both are now **verbatim locators in
   `deepdive_manifests/PMID42422765.json` (entries 29 and 30), machine-verified** against the re-acquired
   JATS surface by `deepdive_manifest.py --verify-artifacts`. §0's provenance caveat is discharged **for
   these two sentences** and for nothing else.
2. ✅ **Every regional fold-change in §1b traces to a recorded figure attestation, and the panel-set
   confusion the triage flagged does not apply.**
   - `8.2 / 10.7 / 5.6 / 1.4` → manifest **entry 28**, *"S5J at P300 prints WT 1, KO 0.2, cortex 8.2,
     hippocampus 10.7, midbrain 5.6 and cerebellum 1.4"*.
   - `4.6 / 4.7 / 3.1 / 0.6` → manifest **entry 19**, *"S6D at P300: WT 1, KO 0.1, cortex 4.6, hippocampus
     4.7, midbrain 3.1, cerebellum 0.6"*.
   - `25.6 / 22.3 / 11.6 / 6.2` → manifest **entry 15**, Figure 2E, `WWOX+WPRE` at 4E10.
   ⚠️ The neighbouring `S6E` values *1 / 0.9 / 0.3 / 0.6* are **four wild-type lanes** and are **not** the
   cerebellar 0.6 used here; the coincidence of the trailing `0.6` is exactly the confusion this check
   existed to foreclose. **No column of §1b's table is unattested.**
3. ✅ **`extraction_damage_report.py` row (d) is confirmed and widened.** The PMC **text** route deletes the
   exponent (`1.23 × 10vg`); the **JATS XML** route does not delete it but **flattens** it (`10<sup>11</sup>`
   → `1011`). Two routes, two distinct silent dose corruptions. The proposed row should therefore be written
   as **`VECTOR_GENOME_EXPONENT_LOST`** with **two** named mechanisms — `DELETED` (text/HTML) and
   `FLATTENED` (XML superscript) — rather than one.
4. 🔴 **Numbering adjudicated: the proposed `D-21` is wrong today.** The `🩸 DEFAULTS THAT BIT US` table ends
   at **`D-16`** (verified in `dismissal_ledger_current.md`), and `D-17` is operator-DEFERRED and reserved.
   `D-18`/`D-19`/`D-20` are only *proposed* by sibling candidates and are not in the ledger. ⇒ the batch
   writes §3(e) at **the next free number at batch time, skipping the reserved `D-17`** — it must not
   hard-code `D-21` and create a gap that later reads as three lost lessons.
5. **Applied outside batch (non-canonical, MINOR, recorded as such):** `analysis/tx007_genotype_class_ceiling_20260921.md`
   now carries a dated, append-only correction block relabelling *"the configuration of the 2021
   proof-of-concept"* as an **inference** from Obeid 2026's framing (the 2021 paper never mentions WPRE; its
   Appendix vector map is WPRE-free), plus the receipt and attestation trail of items 1–2 above. And
   `analysis/mechanism_intervention_map.md` `R-01`: the `INTERVENTION` row no longer states *"WPRE element"*
   for the therapeutic configuration, and `KNOWN_MAJOR_SAFETY_CONSTRAINTS` now labels the DRG item
   **TRANSFERRED (T4/T5)** with its review source named.

**Not done, and the reason is a fact about this checkout, not a choice.** The panels themselves — S5J, S6D,
Figure 2E — were **not** re-read: none of the 18 fingerprinted artifacts exists here. What would unblock it:
re-acquire `mmc1.pdf` and `gr1–gr7.jpg`, re-render at the declared dpi, and re-read the three panels; only
then can a blind locator audit cover the figure triples.

### Exact operation list for `batch_commit.py propagate` (and for the two non-batch surfaces)

1. **`disease-models/wwox/therapeutics/therapeutic_strategies_current.md` · record `TX-007` ·
   op `replace-within`** — *old text (verbatim):* `SAFETY 1–2 (AAV9 CNS: n=1, immunogenicity/dose/long-term unknown)` ·
   *new text:* `SAFETY 1 (AAV9 CNS: n=1, immunogenicity/dose/long-term unknown, **and no measured upper bound on expression** — see the ceiling note below)`. 🔴 **MAJOR: a score move; operator/Mirror R3 before it is written.**
2. **same file · record `TX-007` · op `insert-after`** the `Scoring:` line — §3(a)'s `SAFETY 1` rationale block
   **and, as its own separate bullet**, §3(a-bis)'s biodistribution note. 🔴 The two must not be merged into one
   sentence: §1b-bis is the candidate's own finding about why they constrain each other from opposite sides.
3. **same file · record `TX-007` · op `replace-within`** the window/age caveat — append §3(b): the
   genotype-class qualification was **available and refused for cause** (§2), and the caveat stays general.
4. **`.../claim_registry_current.md` · record `CLAIM 011` · op `replace-within`** — *old text (verbatim):*
   `🔴 **BATCH_20260815_001 boundary:**` · *new text:* §3(c)'s `Extension, 2026-09-21` block followed by that
   same string, so the extension lands before the existing boundary and the boundary is untouched.
   ⚠️ Merge with the other three `CLAIM 011` rewrites in one atomic op list.
5. **`framework/scripts/extraction_damage_report.py` damage register** — one row, per item 3 above, with the
   two mechanisms named. Harness, not science; **left for the harness owner** because sibling packages are
   editing `framework/` in parallel.
6. **`.../research/dismissal_ledger_current.md` · op `append`** — §3(e)'s `DEFAULTS THAT BIT US` row at the
   next free number, skipping the reserved `D-17`.

### LOCATOR TRIPLES FOR BLIND AUDIT

| proposition | verbatim quote | anchor |
|---|---|---|
| WPRE was removed as a precaution in the absence of an observed harm — a non-observation, not a safety result. | "Although no overt toxicity was observed in prior studies, we removed WPRE as a proactive risk-mitigation step to improve the predictability and control of neuronal WWOX expression for potential clinical translation." | `PMID42422765_Obeid2026_PMC_2026-09-27.xml`, Discussion (manifest entry 29) |
| The authors state the price of that removal: the safety margin is bought with more capsid. | "However, this reduction in expression necessitates the use of higher vector doses to achieve comparable therapeutic outcomes." | same artifact, Results, WPRE section, final sentence (manifest entry 30) |
| The minimum effective dose is known as a number of capsids and not as a biological quantity. | *(figure attestation)* Figure 5, twelve panels at P30: two doses with opposite survival outcomes, 7 of 8 regional GC/mRNA comparisons `ns` | `deepdive_manifests/PMID42422765.json` entry 12 — **bytes absent from this checkout; figure triple not auditable until re-acquired** |
| Achieved expression at P300 is regional, not scalar, and the cerebellum is the region the vector reaches least. | *(figure attestation)* S5J at P300: WT 1, KO 0.2, cortex 8.2, hippocampus 10.7, midbrain 5.6, cerebellum 1.4; S6D at P300: cortex 4.6, hippocampus 4.7, midbrain 3.1, cerebellum 0.6 | manifest entries 28 and 19 — **bytes absent; attestation carried forward** |
| The expression explanation the paper offers for the survival threshold is conditioned on the outcome it explains. | *(figure attestation)* S5A–D label the last four treated animals "Dead" — one HD and three LD — so the P90 dose comparison is made among survivors | manifest entry 28 — **bytes absent** |

**Pending:** operator/Mirror R3 on the `SAFETY` move; re-acquisition of the figure bytes before the figure
triples can be audited blind; the harness row (5).
