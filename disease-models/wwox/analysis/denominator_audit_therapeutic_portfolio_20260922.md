# Denominator audit of the therapeutic portfolio — one bounded test of a pattern I named

**Date:** 2026-09-22 · **Actor:** Scientist B · **Node:** `DENOMINATOR_AUDIT_OF_THE_THERAPEUTIC_PORTFOLIO`

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and every
> ledger. Nothing promoted, nothing committed. **BLOCK-1 observed: no safety triage, no druggability score.**
>
> 🔴 **Provenance rule, applied throughout.** Most numbers below are **prior-session figure or table
> attestations** recorded in LEGEND's receipt-backed locator manifests. `files/fulltext/` does not exist in this
> checkout, so those pixels cannot be re-opened by me. Every such use is marked `prior-session attestation`. No
> figure-panel claim is made from this environment.
>
> **Nothing here is medical advice.**

---

## 0. Read depth declared up front

| Source | Depth **this session** | Returned body length | Figure access |
|---|---|---|---|
| `therapeutic_strategies_current.md` · TX-001 … TX-007 | 🟢 read in full (headers at lines 40, 58, 64, 73, 80, 87, 94) | local file | n/a |
| `deepdive_manifests/PMID32000863.json` (25 entries) | 🟢 entries surveyed and the seizure/densitometry/supplementary ones read in full | local JSON | none |
| `deepdive_manifests/PMID42397075.json` (30 entries) | 🟢 read in Wave 8; re-used here | local JSON | 🔴 all 22 artefacts unreachable |
| `deepdive_manifests/PMID42422765.json` (29) · `PMID34747138.json` (20) · `PMID36779245.json` (20) | 🟢 relevant entries re-read | local JSON | none |
| `mechanism_intervention_map.md` (N-15 limits at line 757) | 🟢 read | local file | n/a |
| `PMID 34747138` body | re-used from an **in-act fetch in Wave 4**, ≈19 000 characters (approximate) | — | none |
| `PMID 42422765` body | re-used from an **in-act fetch in Wave 3**, **48 780 characters (measured exactly)** | — | none |
| New fetches this session | **none** — the audit is over material already held | 0 bytes | n/a |

⚠️ **DOI route note, because it cost this session three corrections.** `convert_article_ids` this wave returned
DOIs for `39101447` and `32000863` and **the PMID alone for `29808465`**. It is also silent for `42397075`.
**A silent route is a silence, not an absence** — the DOIs in §7 carry a second route each.

---

## 1. The direct answer

**The audit finds four real instances and one clean case — and then the pattern does not survive §3 intact, which
is the honest result and the one I report.** Literally missing denominators occur in **two** strategies
(`TX-001`, `TX-004`); a **detection floor** standing in for a denominator occurs in a third piece of evidence
shared by **two** strategies (`TX-002`, `TX-003`); a missing group size occurs in a fourth (`TX-005`) **where it
is not the binding defect**; `TX-007`'s denominators **are** reported and it fails for a different reason
entirely; and `TX-006` carries its denominator explicitly (*"Limits: N=2, observational, uncontrolled"*) and is
weak for a reason the frame does not describe — **smallness, not unscaledness**.
⇒ **By case: one (c) — a quantity nobody has ever measured; three (b) — present in the source, never extracted,
of which two share a single unreachable paper; one (a) — already in LEGEND and simply not carried into the
tracker; one not applicable; one where the denominator is reported but survivor-conditioned, which the
three-case taxonomy does not have a slot for.**
🔴 **And the counter-test bites.** *"Missing denominator"* is **not** the common factor. It over-fits. What the
instances actually share is narrower and duller: **the load-bearing quantity is reported on a scale that cannot
be placed against the endpoint the strategy needs.** Sometimes the denominator is absent; sometimes the
comparator genotype was never tested; sometimes the two arms are statistically indistinguishable on the scale
that was measured. **Those are three different defects with one symptom, and calling them one defect mis-ranks
at least two of them.** The audit's value is therefore not the frame — it is the four concrete items, listed in
§4.

---

## 2. Tasks 1 and 2 — one row per active strategy

**Method, stated so the rows can be checked.** For each strategy I took the *single* piece of evidence the entry
leans on hardest — not its strongest evidence, but the one whose removal would collapse the entry — and asked
whether the load-bearing quantity is a rate, a fraction or a difference, and whether its denominator is reported.

| TX | Load-bearing quantity, as stated | Rate / fraction / difference | Denominator | Surface | What a reader would wrongly conclude from the numerator alone | Case |
|---|---|---|---|---|---|---|
| **TX-001** (line 40) splice-allele correction | The **efficacy endpoint itself** — the fraction of correctly spliced transcript. The only readable measurement in the whole WWOX splice literature is *"The gel-electrophoresis of RT-PCR revealed a band for wild-type and another for mutant-type."* (`PMID 39101447`, a **minigene**, and a **donor** allele — a different class from the acceptor this strategy targets) | **fraction** | 🔴 **NOT REPORTED, AND NEVER MEASURED FOR ANY WWOX ALLELE.** No aberrant:normal ratio exists anywhere; no densitometry; and no WWOX splice allele has ever been assayed with an NMD inhibitor, so the **degraded-vs-stable** fraction is unknown too | `body`, prior-session read (`FTR-20260921-39101447-01`) | *"Two bands, so some normal transcript survives"* — the **relative abundance is unknown**, so the correctly-spliced fraction is unconstrained between ~0 % and ~100 %, and TX-001's efficacy endpoint has **no baseline to improve on** | 🔴 **(c)** |
| **TX-002** (line 58) CRISPRa | *"normal transcript but protein not detected"* for Q230P | **threshold statement** — its denominator is the **limit of detection** | 🔴 **NOT REPORTED.** No LoD, no loading control, no exposure series is held. LEGEND holds the sole source (`PMID 29808465`) at **`abstract_only`**, and it has **no PMCID** | source unreachable | *"No protein, therefore nothing to boost"* — a floor of unknown height cannot support a claim about what lies beneath it | **(b)**, hard |
| **TX-003** (line 64) proteostasis | The same *"protein not detected"*, plus the allelic ranking P47T (normal protein) / G372R (barely detectable) / Q230P (absent) | **ordinal comparison** | 🔴 **NOT COMMENSURABLE.** LEGEND already records that the series mixes **Western blot on fibroblasts** (P47T, Q230P) with **immunofluorescence on organoids** (G372R). The "denominator" here is a **shared scale**, and there isn't one | LEGEND record | *"Abundance ranks the alleles"* — the alleles were measured on different instruments in different tissues | **(b)**, hard — same source |
| **TX-004** (line 73) Wnt/MYC | The A51 arm: SOX2⁺ ≈60 %→≈33 %, SOX2⁺MYC⁺ ≈72→≈50, NEUN⁺ ≈6→≈18, SATB2⁺ ≈0.35→≈0.7 `ns`, CTIP2⁺ ≈0.2→≈0.3 `ns` — **all "percentage of cells"** | **fraction** | 🔴 **NOT REPORTED for the treated arm.** The same paper reports total counts for the **genotype** arm (Fig. 2D: **WT 5649, WWOX-KO 3020, SCAR12 3422, WOREE 5916**) and n's for the **AAV9** arm (WOREE 2560 / WOREE-wwox 2003) | `figure`, **prior-session attestation**, page 12 at 170 ppi re-read at 258 ppi | *"A51 normalised the progenitor pool and produced neurons"* — a fraction shift is fully compatible with a **smaller organoid**. Wave 8 showed NEUN⁺ exceeds pure redistribution by ≈2.2×, so the truth is mixed, **not** that the fraction settles it | **(b)** — the authors demonstrably hold the number and reported its analogue **twice** |
| **TX-005** (line 80) lithium/GSK3β | *"Injection of a potent GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice (Fig. 7d)."* | **difference** (treated vs untreated, per genotype) | 🟡 **animals per genotype per panel not recorded in LEGEND's 25 locators.** ⚠️ The **same paper does report N elsewhere** — Suppl. Fig. 1f gives brain weight for **+/+ N=20, +/− N=21, −/− N=18** — so group sizes exist in that supplement | `figure`, **prior-session attestation**, Fig. 7d at native 1946×1627 | *"Lithium rescues the WWOX genotype"* — 🔴 **but the binding defect is not the denominator.** The panel carries **a `****` bracket in all three genotypes including wild type**. Knowing n would not have changed that | **(b)**, and **secondary** — see §3 |
| **TX-006** (line 87) window protection | `N-15`: cognitive and psychomotor impairment **precedes** the epileptic encephalopathy and **does not improve** when seizures are controlled | **difference** | 🟢 **REPORTED, IN LEGEND'S OWN TEXT**: `mechanism_intervention_map.md` **line 757** — *"Limits: N=2, observational, uncontrolled."* | LEGEND body text | Nothing wrongly — the limit travels with the claim | 🟢 **not applicable** |
| **TX-007** (line 94) AAV9 gene therapy | The **dose threshold**: LD `1.23 × 10¹¹ vg` does not rescue survival; HD `2.63 × 10¹¹ vg` plateaus at ≈80 % to day 300 | **rate** (survival) | 🟢 **REPORTED.** Repudi 2021 gives the arms verbatim — *"total= 18, spontaneously dead= 6 … compared to mice injected with AAV9‐hSynI‐GFP (= 6) or the non‐injected (= 8); < 0.0001, log‐rank Mantel–Cox test"* ⚠️ **the extractor deleted every `n` and the `p`; the numerals are intact and the deletions are stated, not repaired.** Obeid 2026's window series likewise gives P1 n=6, P2 n=6, P3 n=3, P5 n=7 against KO+RI n=6 | `body`, **in-act fetch (Wave 4)**; window n's are a **prior-session attestation** | 🔴 *"The achieved protein level explains the threshold"* — **it does not.** Two doses 2.1-fold apart are **statistically indistinguishable in vector genomes and mRNA across four brain regions, 7 of 8 comparisons `ns`**, while producing opposite survival. And S5 marks **one HD and three LD animals dead**, so later expression comparisons are **survivor-conditioned** | 🔵 **(a)** into the tracker — *and* a case the taxonomy lacks |

### 2.1 The (a)/(b)/(c) tally, stated plainly

| Case | Count | Which |
|---|---|---|
| **(c) never measured by anyone — needs an experiment** | **1** | **TX-001**: the correctly-spliced fraction, for any WWOX allele, with or without NMD block |
| **(b) exists in the source, never extracted — needs a targeted re-read** | **3 strategies, 2 sources** | **TX-002 + TX-003** (one source, `PMID 29808465`, `abstract_only`, **no PMCID** — the hard one) · **TX-004** (A51 denominator) · **TX-005** (seizure-panel n, and it is secondary) |
| **(a) already in LEGEND, not carried into the tracker — propagation only** | **1** | **TX-007**: the 7-of-8-`ns` finding and the survivor conditioning are in `PMID42422765.json` and `CLAIM 011`'s flag; **`therapeutic_strategies_current.md` line 98 carries neither** |
| **not applicable — denominator reported** | **1** | **TX-006** |

🔵 **A fourth case the taxonomy does not have, and it should be named rather than forced into (a).** TX-007's
denominators are reported **and survivor-conditioned** — *"S5A-D label the last four treated animals 'Dead' (one
HD and three LD)"* (prior-session attestation). **A reported denominator that has been selected on the outcome is
not the same object as a missing one**, and the remedies differ: the first needs a sensitivity analysis, the
second needs a number.

---

## 3. The counter-test — attacking my own pattern, with force

**The claim under test (mine, Wave 8):** *"The recurring defect in this corpus is a numerator reported without
its denominator."*

### 3.1 The case where the denominator IS reported, as the node requires

🟢 **TX-007.** Every survival arm carries its n, in two independent papers, from two independent readings (one an
in-act body fetch, one a prior-session attestation). **And the strategy is still not safe to act on.** So a
reported denominator is neither necessary nor sufficient for soundness.

**What does TX-007 share with the others?** Not a missing denominator. What it shares is this: **the quantity that
was measured does not track the endpoint the strategy needs.** Survival was measured; the *biological* threshold
— what protein level separates rescue from death — was not, and cannot be recovered, because the two doses are
indistinguishable on vg and mRNA in 7 of 8 comparisons. **The number is present; the scale is wrong.**

### 3.2 Two more attacks, both of which land

- 🔴 **TX-005's binding defect is not a denominator.** Lithium's panel carries a `****` bracket **in all three
  genotypes, wild type included**. That is a **specificity** failure. Supplying n would not touch it. Ranking
  TX-005 as a denominator instance **mis-describes why it is weak** — and LEGEND already has the correct
  description in `N-02`.
- 🔴 **TX-006 reports its denominator and is weak anyway**, because `N=2` is small and uncontrolled. The frame
  says nothing about smallness, which is the actual limitation. **A frame that is silent about the one case it
  fits cleanly is not doing the work.**

### 3.3 Verdict on the pattern

🔴 **The pattern does not survive intact, and I report that rather than restating it.** Of seven strategies:
**two** have a literally missing denominator (`TX-001`, `TX-004`); **one more** has a missing *scale* that I had
to stretch the word "denominator" to cover (`TX-003`'s non-commensurable assays) and **one** a missing *floor*
(`TX-002`'s limit of detection); **one** has a missing group size that is not its binding defect (`TX-005`);
**two** do not fit at all (`TX-006`, `TX-007`). **Four of seven require the word to be stretched, and in two of
those the stretch changes the diagnosis.**

✅ **What survives, narrower and less quotable:** the instances share a *symptom* — **a load-bearing number that
cannot be placed on the same scale as the endpoint it is cited for** — and **three distinct causes**: an absent
denominator, an untested comparator, and a measurement that does not resolve the arms it is meant to separate.
**"Missing denominator" names one cause and was being used to name all three.** That is exactly the error this
node was convened to check for, one level up, and it was mine.

⚠️ **And the frame's real weakness, stated against myself:** almost any quantitative claim can be re-described as
a ratio with an implicit denominator. The four Wave-8 instances were selected **after** the frame was in mind.
**A pattern found that way needs an out-of-sample test**, and the only two out-of-sample cases available here —
TX-006 and TX-007 — are the two it fails on.

---

## 4. Task 4 — what follows, in one paragraph

**Three targeted re-reads, one propagation fix, and one real experiment — and nothing structural.** The real gap
is **TX-001's efficacy endpoint**: no aberrant:normal transcript ratio exists for any WWOX splice allele, with or
without an NMD block, and only an experiment can produce one — LEGEND already holds it as `E-4`/`DL-BIO-003` with
a traceable route (a group that possesses WOREE fibroblasts and runs WWOX RT-PCR), so **it needs no new
mechanism, only priority**. The three re-reads are: **`PMID 29808465`'s detection floor** (serving TX-002 and
TX-003; the hard one — `abstract_only`, no PMCID, already on record as the highest-value acquisition target),
**the A51 denominator** in `PMID 42397075` (one number: total cells per organoid, treated versus vehicle), and
**the seizure-panel group sizes** in `PMID 32000863` (cheap, and secondary — TX-005's binding defect is
specificity, not n). The propagation fix is **TX-007**: the 7-of-8-`ns` finding and the survivor conditioning are
already in LEGEND and simply do not appear in the tracker. 🔴 **No gate, no registry, no mandatory field and no
audit programme is proposed, and none is warranted — the audit's own counter-test showed the frame that would
justify one does not hold.**

---

## 5. What LEGEND already knew · what is new

### 5.1 Already held

- `TX-001`'s missing baseline, the zero NMD-inhibitor result, and *"nessun rapporto aberrante:normale esiste da
  nessuna parte"*; `DL-BIO-003` and the traceable Genova route.
- `CLAIM 030`'s `PREMISE: DETECTION_FLOOR` and the non-commensurable allelic-series assays; `PAPER 041` flagged
  as *"the highest-value acquisition target in this lot."*
- `N-02` (lithium significant in all three genotypes) and `N-15` with its *"Limits: N=2"*.
- `CLAIM 011`'s threshold flag; `PMID42422765.json` entries 12 and 28 (the 7-of-8 `ns`; the dead-animal labels).
- Wave 8: the A51 percentages without a denominator, and the 1.37× redistribution arithmetic.

### 5.2 New in this node

1. ✅ **The audit itself, one row per active strategy**, with the load-bearing quantity named and its denominator
   located or declared absent — **this did not exist in any form**.
2. 🔴 **The pattern I named in Wave 8 does not survive its own test.** Two of seven fit cleanly; two more require
   stretching the word; two do not fit at all — and in `TX-005` the stretch **mis-ranks the defect**.
3. ✅ **A better and duller common factor**: a load-bearing number that cannot be placed on the endpoint's scale,
   arising from **three distinct causes**, of which an absent denominator is one.
4. 🔵 **A fourth case the (a)/(b)/(c) taxonomy lacks**: a denominator that is **reported and
   survivor-conditioned** (TX-007), which needs a sensitivity analysis rather than a number.
5. ✅ **The proportions, which the node asked for**: **1 (c) · 3 (b), two of them sharing one unreachable source ·
   1 (a) · 1 not applicable · 1 outside the taxonomy.**
6. ⚠️ **A methodological admission**: the four Wave-8 instances were selected after the frame was in mind, and
   the only two out-of-sample cases are the two it fails on.

---

## 6. Corrections, with exact file and line coordinates

**W9-C1 — `TX-007`'s scoring line still carries none of what LEGEND knows about its threshold.** *(This is the
one (a) case; it extends `W3-C1` rather than replacing it.)*
- **File:** `disease-models/wwox/therapeutics/therapeutic_strategies_current.md` · **line 98**
- **Issue:** the line records `EVID 2` and `REVERS 0` and says nothing about the fact that **the survival
  threshold has no measured expression difference behind it** (7 of 8 vg/mRNA comparisons `ns` across four brain
  regions) or that the expression comparisons are **survivor-conditioned** (one HD and three LD animals marked
  dead). Both are already in `PMID42422765.json` (entries 12, 28) and in `CLAIM 011`'s flag.
- **Proposed:** append to the `EVID` parenthesis — `⚠️ **e la soglia di sopravvivenza non ha dietro di sé alcuna differenza di espressione misurata**: due dosi distanti 2,1× sono statisticamente indistinguibili in genomi virali e mRNA in quattro regioni cerebrali (**7 confronti su 8 `ns`**) pur producendo esiti di sopravvivenza opposti; e i confronti di espressione successivi sono **condizionati ai sopravvissuti** (S5 marca un animale HD e tre LD come deceduti). Fonti già in LEGEND: `PMID42422765.json` voci 12 e 28, flag di [[claim_registry_current#CLAIM 011]].`

**W9-C2 — `TX-001`'s entry should say that its efficacy endpoint is case (c), not case (b).**
- **File:** same · **line 40** block, the `**Mandatory gate:**` bullet
- **Issue:** the gate correctly demands junction-specific RT-PCR before any modality choice. What it does not say
  is that **the quantity it demands has never been produced for any WWOX allele by anyone** — so this is not a
  literature-retrieval task but an experiment, and it is the **only one** of the seven strategies for which that
  is true.
- **Proposed:** add one clause — `**È un esperimento, non un recupero bibliografico:** il rapporto aberrante:normale non esiste per **nessun** allele WWOX, con o senza blocco dell'NMD. Unico caso del portafoglio in cui la quantità portante non è mai stata misurata da nessuno (audit denominatori 2026-09-22).`

**W9-C3 — record that the Wave-8 pattern was tested and narrowed.**
- **File:** `disease-models/wwox/research/discovery_ledger_current.md` · as a `FM-` (failure-mode) entry, since
  the finding is about **my own inference**, not about the biology
- **Proposed content:** *"«Denominatore mancante» è stato proposto come difetto ricorrente del portafoglio su
  quattro istanze e **non regge al test fuori campione**: due strategie su sette lo presentano letteralmente,
  due richiedono di allargare il termine, due non lo presentano affatto — e in `TX-005` allargarlo **sbaglia la
  diagnosi** (il difetto vincolante è la specificità, non la n). Le quattro istanze erano state selezionate
  **dopo** che la cornice era in mente. ⇒ quasi ogni affermazione quantitativa può essere ridescritta come un
  rapporto con un denominatore implicito; una cornice trovata così richiede un test fuori campione prima di
  essere usata."*
- ⚠️ **Placement is the ledger owner's call**; I am not proposing an ID.

---

## 7. Source attribution

Retrieved from **PubMed / PubMed Central**. **No new fetch was made in this wave** — the audit is over material
LEGEND already holds. DOIs carry two routes each; ⚠️ `convert_article_ids` is **silent** for `29808465` and
`42397075`, which is a route's silence and not an absence.

| PMID | Citation | DOI | Routes |
|---|---|---|---|
| 39101447 | *Mol Genet Genomic Med* 2024 — WWOX-DEE, the minigene splice measurement behind TX-001 | [10.1002/mgg3.2500](https://doi.org/10.1002/mgg3.2500) | converter ✅ (`PMC11298992`) + metadata ✅ |
| 29808465 | Johannsen J *et al.* *Neurogenetics* 2018 — the sole Q230P protein measurement | 🔴 **no DOI from the converter; no PMCID; held `abstract_only`** | converter ⛔ silent · metadata ⛔ |
| 42397075 | Steinberg DJ *et al.* *Brain* 2026 — the A51 arm | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) | converter ⛔ silent · manifest `doi` field ✅ + metadata ✅ (earlier wave) |
| 32000863 | Cheng Y-Y *et al.* *Acta Neuropathol Commun* 2020 — lithium/ethosuximide PTZ panels | [10.1186/s40478-020-0883-3](https://doi.org/10.1186/s40478-020-0883-3) | converter ✅ (`PMC6990504`) + in-act body ✅ |
| 34747138 | Repudi S *et al.* *EMBO Mol Med* 2021 — the Kaplan–Meier arms | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) | converter ✅ + in-act body ✅ |
| 42422765 | Obeid M *et al.* *Mol Ther Oncol* 2026 — the dose threshold and S5 | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) | converter ✅ + in-act body ✅ |
| 36779245 | Oliver KL *et al.* *Epilepsia* 2023 — cohort denominators, cited for contrast | [10.1111/epi.17542](https://doi.org/10.1111/epi.17542) | converter ✅ + in-act body ✅ |

---

**End.** Not medical advice. No gate, registry, mandatory field or audit programme is proposed. Read-only toward
every canonical file; nothing promoted, nothing committed.
