# COMMIT CANDIDATE — CC-20260921-WWOX-ENZYMOLOGY-P306-01

**Source:** a field-wide census run by Scientist A on the node
`MECHANISM_WWOX_SDR_FUNCTION_AND_MISSENSE_RESCUE`
([`wwox_sdr_function_per_molecule_census_20260921.md`](../../analysis/wwox_sdr_function_per_molecule_census_20260921.md)),
**independently re-verified by the Orchestrator** against PubMed metadata and against
`registry_records.py`. **No reading occurred** — the paper is abstract-only from this
environment — and **no receipt is claimed**.
**Ledger:** `fulltext_receipts.py verify` → **OK: 188 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — one corpus record re-tiered and queued, two prose narrowings, one
ledger row. **No claim added, reversed or narrowed. No status changed.**
**Target:** `working_model_version` MINOR bump at batch time. No `BLOCCO 1` change.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.** No canonical claim is touched. What changes is a **reading priority**, a
**therapeutic-strategy obstacle line**, and a **statement of absence** that turns out to be false.

---

## 1 · The finding

> 🔴 **An assay of WWOX catalysis exists. It has existed since 2011. It is in LEGEND's own
> registry, tiered `C`, marked `background only`, and has never been read.**

**PMID 21476439** — Sałuda-Gorgul A, Seta K, Nowakowska M, **Bednarek AK**, *Z Naturforsch C J
Biosci* 2011;66(1–2):73–82, **"WWOX oxidoreductase — substrate and enzymatic characterization."**

Verbatim, from the PubMed metadata abstract (copied in the same act; **no DOI is present in the
record and none is asserted here**):

> *"Due to its potential role in sex-steroid metabolism, using two bacterial expression systems,
> we have cloned WWOX fusion proteins showing oxidoreductase activity in a crude extract, defined
> a course of enzymatic reactions for selected steroid substrates, and **determined related Km
> values**."*

> *"Our results show that **the SDR domain of the WWOX protein has dehydrogenase activity and is
> reactive both in the presence of NAD+ and NADP+ for all examined steroid substrates**."*

> *"On the other hand, with the same substrates and **reduced cofactors (NADH and NADPH) reduction
> activity was not observed**."*

**Its state in LEGEND, verified with `registry_records.py get --pmid 21476439`:**

| Field | Value |
|---|---|
| Record | `CORPUS P306` / `LIT-0306` |
| `Tier (FASE 1)` | **C** |
| `clinical relevance` | **LOW** |
| `Filter decision` | **background only** |
| `Priority` | **low / background** |
| `Date processed` | **triage only** (2026-04-18) |
| `Claim links` | **none — triage only** |
| Receipts | `fulltext_receipts.py status --pmid 21476439` → **`[]`** |

## 2 · Why it matters, stated without inflating it

`sdr_missense_readout_assessment_20260920.md` asked whether any readout of WWOX **SDR function**
exists, answered **`NO`** — *"Not 'not yet', not 'partially'"* — and closed with:

> *"Identifying a physiological substrate is the experiment that would make a genuinely
> complementary second readout possible. It is not in this corpus, and **on the census run here it
> is not anywhere**."*

**That last clause is false, and the correction is owed.** An *in-vitro* activity with Km values
on steroid substrates was published once. ⚠️ **What does NOT change** — and this is the larger
half:

- the activity was measured **in a crude extract**, not on purified enzyme;
- **wild-type protein only** — **no disease allele was tested**;
- **no catalytically-dead triad control** (the `S281A / Y293F / K297A` mutants exist only as
  *"Aldaz laboratory unpublished observations"*);
- **no folded-monomer normalisation**, so it is an activity *report*, not an assay;
- and the substrates are **steroids**, consistent with WWOX's highest expression being testis,
  prostate and ovary — **not** a demonstrated neural substrate.

⇒ **An assay of WWOX *catalysis* exists once. An assay of WWOX *function per molecule* — the thing
`TX-003` is blocked on — still exists nowhere, for any allele.** `PROTEIN AMOUNT` and `PROTEIN
FUNCTION` remain different questions, and only the first has ever been measured on a WOREE allele.

## 2bis · 🔴 The two halves stated as a rule, on Operator note (2026-09-21)

Both halves are already argued above; they are restated here as a standing rule because they are
the two ways this finding will be mis-carried, and they fail in **opposite** directions.

> ✅ **HALF ONE — treat the 2011 Km / cofactor / substrate evidence as a REAL HISTORICAL
> BIOCHEMICAL RESULT until a primary reading determines otherwise.** It is a peer-reviewed primary
> reporting cloned fusion proteins, a defined steroid-substrate panel, cofactor dependence and Km
> values. **It is abstract-only from here, which is a statement about this environment, not about
> the paper.** It must not be discounted, hedged into vagueness, or described as "claimed" —
> `PREMISE: UNREAD_PRIMARY` is the correct tag, and it means *owed a reading*, **not** *doubted*.

> 🔴 **HALF TWO — do NOT infer that it provides a validated functional assay for disease alleles.**
> Crude extract, **wild-type protein only**, **no disease allele of any kind**, no
> catalytically-dead triad control, no folded-monomer normalisation, and **no physiological
> substrate assigned**. An activity **report** is not an **assay**. Nothing about `Q230P`,
> `P47T`, `G372R` or any other variant follows from it.

**Why both are needed together.** Half one alone invites *"WWOX catalysis is characterised"*, which
would make `TX-003` look unblocked when it is not. Half two alone invites *"there is no WWOX
enzymology"*, which is the sentence this candidate exists to withdraw. 🔵 **The honest position is
the narrow one: an assay of WWOX CATALYSIS exists once, and an assay of FUNCTION PER MOLECULE
exists nowhere, for any allele.**

⚠️ **And one live contradiction sits across the substrate question** and must travel with any use of
this result: a 2015 **review** proposes the catalytic domain is a **retinal** oxidoreductase acting
**reversibly** on all-trans-retinal, while the 2011 primary observed **oxidation only** — *"with the
same substrates and reduced cofactors (NADH and NADPH) reduction activity was not observed."*
**They disagree on reversibility, which is the one property an assay design must choose, and no
experiment has ever been run that could tell them apart.**

## 3 · How it was missed, and the root cause that is now fixed

`unread_gold.py` exists precisely to catch this (failure mode `FM-011`). It missed this paper on
**both** of its paths, for **three** independent reasons, all measured today:

1. 🔴 **Its selector regexes matched the wrong field spelling.** `tier` looked for
   `**Tier (PHASE 1):**` — the registry writes `**Tier (FASE 1):**`, **187 records, zero in
   English**. `relevance` looked for `**Relevance:**` — the registry writes
   `**clinical relevance:**`, **254 records, zero of the short form**. Both matched **nothing**,
   so the default filter could never fire and printed *"No unread Tier-A / Relevance-HIGH
   CORPUS"* — **a parse failure wearing the costume of an all-clear**. This is the repository's
   own §3 rule turned on its own instrument: *a zero from a parser is not evidence of absence
   until the parser is shown to be reading the document.*
2. 🔴 **Even parsing correctly, the default filter is structurally blind here.** Of 164 unread
   corpus placeholders, **155 are `C` / `LOW`** and **none is `A` / `HIGH`**. The FASE-1 triage
   gave the whole 221–400 window the same label, so the tier field carries no discriminating
   information and a tier-gated tool cannot find gold in it **even when it works**. It can only
   find gold that triage already called gold — which is the one case that needs no tool.
3. 🔴 **The mechanism lens had no vocabulary for catalysis.** `MECHANISM_RE` hunted allele,
   protein fate, proteostasis and interaction terms — the *proteostasis* half of the missense
   question (**is the protein there?**) — and had no term at all for the other half (**does the
   protein work?**): no `enzym`, `substrate`, `catalytic`, `oxidoreduct`, `dehydrogenas`, `Km`,
   `cofactor`, `NAD`. Its one "function" group was `binding|interact|partner|rescue`, i.e. exactly
   the interaction proxies the SDR-readout assessment had **rejected** as not being measures of
   SDR function. **The lens encoded the same blind spot the science had.**

**Repaired at T0, with regressions** (`framework/scripts/test_unread_gold.py`, 12 tests, **mutation-tested:
4 fail when the fixes are reverted**): both field spellings accepted, a catalysis clause added,
and the tool now **cross-checks the receipt ledger**. Effects, measured:

- `P306` and five other records now surface on the mechanism lens (79 → 85);
- **19 of 164 placeholders were found to be advertised as "never deep-dived" while carrying
  complete- or partial-read receipts** — stale rows that would each have dispatched duplicate
  work, the `FT-102` failure waiting to happen 19 more times. They are **annotated, not hidden**:
  a stale registry row is a finding.

## 4 · What is proposed

**(a) `CORPUS P306` → full-text queue at HIGH, and acquisition packet.** It is **not** promoted to
a `PAPER` record: no reading stands behind it and it must not acquire the appearance of one.

> **`FT-112` / packet item `A11` — `PMID 21476439`.** Re-tier `CORPUS P306` from `C` / `LOW` to
> **`Tier: A` / `clinical relevance: HIGH`**, `Filter decision: **deep-dive — full text required**`,
> with the re-tier reason recorded in `Note`. **Acquisition status:** `convert_article_ids` returns
> the PMID alone — **no PMCID**; the metadata record carries **no DOI**; *Z Naturforsch C*
> (De Gruyter), 2011. **Not retrievable by any automated route in this environment.**
> **What to ask a human for, precisely:** the **Km table** and the **substrate list with cofactor
> conditions**, plus the Methods paragraph describing the expression construct and whether any
> purification step preceded the activity measurement.

**(b) Narrow `sdr_missense_readout_assessment_20260920.md` § 6.** Append a dated correction (do not
rewrite — the file is append-only in practice and its reasoning is sound):

> 🔴 **Correction, 2026-09-21.** *"on the census run here it is not anywhere"* is too strong and is
> withdrawn. **`PMID 21476439` (2011) measured WWOX dehydrogenase activity on steroid substrates
> with NAD⁺ and NADP⁺ and reported Km values** — in a crude extract, on wild-type protein, with no
> disease allele and no catalytically-dead control. The narrowed statement that survives: **no
> *physiological* substrate is assigned, and no function-per-molecule assay exists for any allele.**
> The paper was in this repository as `CORPUS P306`, `background only`, throughout.

**(c) `TX-003` — narrow the obstacle line.** Current text: *"WWOX is an oxidoreductase with
undefined physiological substrate/activity"*. Proposed:

> WWOX's SDR domain has **measured in-vitro dehydrogenase activity** on steroid substrates with
> both NAD⁺ and NADP⁺, and published Km values (`PMID 21476439`, 2011) — **oxidation only; no
> reduction activity was observed with NADH/NADPH**. ⚠️ **This is not yet an assay**: crude
> extract, wild-type only, no disease allele, no catalytic-triad control, no folded-monomer
> normalisation, and no **physiological** substrate assigned. **`TX-003`'s blocker is therefore
> narrower than "no activity is known" and sharper than it was: the activity exists on paper and
> has never been pointed at an allele.** `PREMISE: UNREAD_PRIMARY` — abstract-only, acquisition
> item `A11`.

**(d) `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`** — one row:

> **D-19** · *"the tool that finds unread gold reported none, so there is none"* · **Why it is
> FALSE here:** `unread_gold.py` printed *"No unread Tier-A / Relevance-HIGH CORPUS"* while its two
> selector regexes matched **zero** records in the live registry — it was not reporting a clean
> registry, it was reporting that it could not read one. **The repository's own rule, applied to
> its own instrument: a zero from a parser is not evidence of absence until the parser is shown to
> be reading the document.** And a second, subtler half: even once parsing, a **tier-gated** filter
> over a corpus where 155 of 164 unread records share one tier can only surface what triage already
> ranked — it cannot correct triage, which is the only job it has.
> **Detection rule:** before trusting any selector-based tool's empty result, check that its
> selectors match **more than zero** records in the live document.

⚠️ **Numbering:** `D-17` was proposed on 2026-09-21 and **DEFERRED by the operator**; it is **reserved, not free**, and is not in the ledger. This session's candidates propose `D-18`–`D-23`, one each. **Do not renumber into `D-17`.**

## 5 · What is explicitly REFUSED

- ❌ **No claim is created.** An abstract is not a reading. Nothing about WWOX enzymology enters
  the claim registry from this candidate.
- ❌ **No promotion to `PAPER`.** `CORPUS P306` becomes a **queued** record, not an integrated one.
- ❌ **No neurosteroid bridge.** The substrates are steroids and the brain has neurosteroids; that
  is a *resemblance*, not evidence, and it is named here only to be refused until someone measures
  a neural substrate.
- ❌ **No new gate, auditor or registry** (§26). The repair is to an **existing, already-routed
  tool**, with regressions — and one ledger row carrying a detection rule.
- ❌ **`TX-003`'s score does not move.** A wild-type in-vitro activity with no allele arm changes
  the *description of the blocker*, not the *probability of the strategy*.

## 6 · Growth delta

`claims +0 · papers +0 · corpus +0`. `CORPUS P306` is **re-tiered and queued**, not added.

---

*Sources retrieved from **PubMed / PubMed Central**. `PMID 21476439` carries no DOI in its PubMed
record; none is invented here. Other DOIs — [24932569](https://doi.org/10.1016/j.bbcan.2014.06.001) ·
[38161429](https://doi.org/10.3390/ijms25010316).
Not medical advice.*
