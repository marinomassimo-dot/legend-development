# Does the underlying arithmetic support the prognostic association? — an independent reconstruction

**Date:** 2026-09-21 · **Actor:** Orchestrator, on Operator instruction · **Source:** `PMID 36779245`
(Oliver, Trivisano, … Scheffer, *Epilepsia* 2023), read **in-act** from `PMC10952634`,
DOI [10.1111/epi.17542](https://doi.org/10.1111/epi.17542) — **both identifiers verified by
`convert_article_ids`, by copy.**
**Status:** non-canonical analysis file. **No canonical file edited.** Not medical advice, and
nothing here is a prognosis for any person.

---

## 0 · What was retrievable, and what was not

| Item | Status |
|---|---|
| Full body text | 🟢 **read in-act**, in full |
| **Table 1** — the 13-patient cohort, genotype by patient | 🟢 **retrieved complete** |
| **Table 2** — epilepsy/EEG/MRI by patient | 🟢 retrieved complete |
| **Table 3** — cohort vs literature summary | 🟢 retrieved complete |
| 🔴 **`SUPPLEMENTARY MATERIAL S1` / `TABLE S1`** — the per-individual rows for the **62 literature cases** | 🔴 **NOT RETRIEVABLE.** The deposit ends with the two file names and **no content** |
| Figures (incl. Figure 4A, the Kaplan–Meier) | ❌ not inspectable in this environment |

**Routes attempted and their results**, so nobody repeats them: `curl` to `pmc.ncbi.nlm.nih.gov`
and `www.ncbi.nlm.nih.gov` → **`CONNECT tunnel failed, 403`** (proxy egress); `WebFetch` on the PMC
article → **`EGRESS_BLOCKED`**; PubMed MCP `get_full_text_article` → **body yes, supplementary
no**. ⇒ **`TABLE S1` is acquisition work, and `FT-122` stands.**

> 🔵 **This is the one place the answer genuinely turns on a file nobody here can open** — and it is
> an **open-access** paper. That is worth saying plainly: the obstacle is not a paywall, it is a
> supplementary-file route this environment does not have.

---

## 1 · Table 1 reconstructed, and its alignment verified before use

⚠️ **The extraction returns Table 1 as parallel row-lists, not as rows** — 13 ages, **11** variant
entries, **12** genotype-class entries. Alignment therefore had to be **established, not assumed**.
🔴 **And Table 1 carries a published correction**: *"[Correction added on 24 March 2023, after first
online publication: The entries in column 9 of Table 1 for the 'WWOX' and 'Genetic combination'
rows of the 'Genetics' section have been updated.]"* — precisely the §12 hazard.

**Three independent anchors in the running text fix the mapping, and all three agree** (brothers
**Patients 9 and 10 share one genetics entry**, which reconciles 11/12/13):

| Anchor, verbatim from the body | Reconciles |
|---|---|
| *"p.Gln230Pro in three of our patients (homozygous in two; compound heterozygous in one)"* | exactly three `Q230P` entries: one compound het + two homozygous |
| *"Three patients (Patients 5, 6, 8) died"* … *"died at age 8, 11, and 6 years, respectively"* | ages column reads `8 y 3 m (dec.)`, `11 y 7 m (dec.)`, `6 y (dec.)` at positions 5, 6, 8 |
| *"We report the oldest living patient, aged 23 years 11 months"* | position 2 reads `23 y 11 m, M` |

✅ **Alignment confirmed on three anchors. The `Q230P` rows below are safe to use.**

### 🔴 The three `Q230P` patients, from Table 1

| Patient | Genotype (verbatim) | Class | Age / outcome |
|---|---|---|---|
| **1** | `c.689A > C, p.Gln230Pro (mat)/exon 7–8 deletion (pat)` | Missense/null | 4 y 7 m, **alive** |
| **2** | `c.689A > C, p.Gln230Pro (homozygous)` | Missense/missense | 🟢 **23 y 11 m, alive — the oldest patient on record** |
| **5** | `c.689A > C, p.Gln230Pro (homozygous)` | Missense/missense | 🔴 **8 y 3 m, DECEASED** |

> **Two patients, the same two alleles, the same cohort, opposite tails.** Independently
> reconstructed here from Table 1, not taken from the delegate.

**And the deaths are not concentrated in the null class.** Of the three deceased — Patients 5, 6, 8
— Patient 5 is `missense/missense` and Patient 6 is `missense/null` (`p.Glu17Lys` / intron 4
deletion). **Only Patient 8 (`exon 5 deletion` homozygous) is null/null.** ⇒ **in the cohort that
generated the statistic, two of three deaths carry a missense allele.**

---

## 2 · The four things the Operator asked to be distinguished

### (a) Descriptive imbalance — ✅ **REAL, and not in dispute**
Stratification, verbatim: *"We stratified all 75 cases into one of three genetic groups:
(1) null/null (= 45), (2) null/missense (= 15), (3) missense/missense (= 15)."*
Reported outcome: 5-year survival **<50 %** for null/null versus **>75 %** for the other two; by
10 years **25 %** versus **>60 %**. **Nothing here disputes that the assembled data look like
that.**

### (b) Statistical association — ✅ **as reported**, ⚠️ **on a pooled sample**
*"survival was much poorer for the double null group compared with the patients who had at least
one missense pathogenic variant (‐value = .0085, log‐rank test)"*. Kaplan–Meier, R Survival,
R 4.0.2. 🔴 **Not reproducible here**: the 62 literature rows are in `TABLE S1`. **No
recomputation is attempted and none is implied.**

### (c) Survival inference — 🔴 **this is where it does not carry to an individual**
1. **The classification is syntactic, and the authors say so twice.** *"presumed hypomorphic"*
   (abstract) and *"Functional studies would be required to support this hypothesis"* (Discussion).
   Variants were *"coded as either null … or missense"* from the lesion in the DNA, never from a
   measured protein effect. **The grammatical mood of the mechanism is hypothesis, in the sentence
   that proposes it.**
2. 🔴 **The flagship missense allele spans the whole range.** `Q230P` is the most recurrent
   missense variant in the disease and occupies both tails of this very cohort (§1). **A class
   average is not a prognosis for a member of the class.**
3. **The authors themselves find no dose gradient inside the missense side:** *"We found no
   difference between individuals with one or two missense variants and therefore no evidence to
   support an 'intermediate' phenotype"* — which is what a clean hypomorph model would predict and
   does not show.
4. **No severity difference accompanies the survival difference.** Time to seizure onset:
   *"no difference between the three genetic groups (‐value = .65)"*, and the cohort is uniformly
   profound — *"Profound"* intellectual disability in **13 of 13**, none ambulant.

### (d) Ascertainment and censoring — 🔴 **uncontrolled, and the direction is knowable**
1. 🔴 **The two pooled strata differ in both ascertainment and composition**, from Table 3:

   | | this cohort (n = 13) | literature (n = 62) |
   |---|---|---|
   | Mean age last known | **8 y 2 m** | 3 y 4 m |
   | **Deceased** | **23 %** | **38 %** |
   | null/null · null/missense · missense/missense | 50 % · 33 % · 17 % | 60 % · 15.5 % · 24.5 % |

   **An older cohort with lower mortality is the signature of a living-patient recruitment**, and
   the authors note the age gap themselves — *"despite our patient group being notably older …
   the mortality was lower"* — **without treating it as a bias term.** The two strata are pooled
   into one Kaplan–Meier.
2. 🔴 **Censoring in a literature-assembled cohort is informative.** Figure 4A's dashes are
   *"the most recent age known to be living of each individual (censored observations)"* — i.e.
   **the age at which somebody published**, not a follow-up time. Early-fatal cases are reported
   *because* they died; living cases are reported at whatever age a report happened. **That is not
   non-informative censoring, and the analysis does not address it.**
3. **The long tail rests on very few at risk.** Median age of the literature cases is **2 y 6 m**,
   so the *"steady at >60 %"* beyond 10 years is carried by a small number of individuals inside
   groups of **15**. **No numbers-at-risk are reported.**

---

## 3 · The answer

> **The descriptive imbalance is real and the statistical association is as reported. The
> underlying arithmetic does NOT support using it as an individual-level prognostic statement** —
> because the exposure variable is a syntactic proxy the authors decline to validate, its most
> recurrent missense allele occupies both tails of the same cohort, the pooled sample combines two
> strata that differ in ascertainment *and* in genotype composition, and censoring is
> age-at-publication rather than follow-up.

**What this does NOT do:** it does not reverse `CLAIM 033`, does not dispute that null/null is the
worse class on the assembled data, and does not assert the association would vanish if `Q230P` were
removed — **that computation needs `TABLE S1` and both directions remain arguable**, since removing
`Q230P` removes the class's longest survivor *and* two of its deaths.

**Therapeutic consequence, already landed in `CC-20260921-CLAIM033-REPLICATION-01`:** `TX-003` must
stop citing this statistic as evidence that a residual protein pool exists. §2(c) is why.

---

## 4 · What is proposed

**No new candidate.** `CC-20260921-CLAIM033-REPLICATION-01` already proposes the fifth reservation,
the denominators and the `Q230P` fraction; this file **supplies its primary-source verification**
and is referenced from it. Two amendments are proposed to that existing candidate:

1. **Add the ascertainment asymmetry as a named limb of the fifth reservation** — 23 % vs 38 %
   mortality across strata pooled into one curve, with 8 y 2 m vs 3 y 4 m mean age (§2d.1).
2. **Add the censoring point** — Figure 4A's censored observations are ages at publication, not
   follow-up times (§2d.2).

⚠️ **Per the Operator's boundary, no prognostic claim change is propagated from this file.** It
goes to the normal canonical review with the candidate.

---

*Retrieved from **PubMed / PubMed Central**. `PMID 36779245` · DOI
[10.1111/epi.17542](https://doi.org/10.1111/epi.17542) · `PMC10952634`, verified by copy.
**Body read in-act; `TABLE S1` not retrieved and no claim rests on its contents.** No receipt is
claimed: no locator manifest was built and no figure was inspected. Not medical advice.*
