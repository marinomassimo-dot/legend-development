# The Q230P survival paradox — is the "≥1 missense" advantage carried by Q230P, or does Q230P ride along?

**Date:** 2026-09-21 · **Actor:** Scientist B · **Node:** Q230P survival paradox (`CLAIM 030` × `CLAIM 033`)

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and every
> ledger. Nothing promoted, nothing committed.
>
> **Public edition, and de-identification applied deliberately.** Patients are referred to only by the
> pseudonymous numbering their own publications use. **Country, self-identified ethnicity, sex and age are never
> stacked into a single descriptor here**, even where the source publishes all four, because that combination is
> the identifying one. Nationalities already carried elsewhere in this repository are replaced below by family
> indices. No contact details, no institution-plus-age pairings, no living person's identifying information.
>
> **Nothing here is medical advice, and nothing here is prognostic.** A genotype class is not a prognosis for any
> individual, and this file's central finding is precisely that the class does not predict the individual.

---

## 0. Read depth declared up front

| PMID | Identity | Depth **this session** | Returned body length | Figure access |
|---|---|---|---|---|
| **36779245** | Oliver *et al.* 2023, *Epilepsia* — **the source of the survival split** | 🟢 **full body read in-act, including Table 1, Table 3 and the complete genotype-class denominators.** Prior receipt `FTR-20260804-36779245-02` (`complete_fulltext_read`) | non-empty; **≈31 000 characters (approximate; not instrumented)** | none. Figure 4 values re-used from LEGEND manifest entry 18, attributed as prior-session |
| **33916893** | Banne *et al.* 2021, *Cells* — census/review | manifest + receipt `FTR-20260909-33916893-01` (`complete_fulltext_read`, 35 locators) | 0 bytes this session | none. **All Table 1 / Table S1 row values below are prior-session figure/table attestations** |
| **30356099** | Piard *et al.* 2019, *Genet Med* — 20 WOREE cases | manifest (10 locators) + receipt `FTR-20260811-30356099-01` (`partial_fulltext_read`) | 0 bytes | none |
| **40875931** | 2025 registry cohort, *Neurology* — **the replication attempt** | manifest (20 locators) + receipts `FTR-20260726/…-01`, `FTR-20260804-40875931-02`, both `partial_fulltext_read` | 0 bytes | none |
| **39507621** | Teplyshova 2024, *Front Genet* — adult case | receipt `FTR-20260804-39507621-01` (`complete_fulltext_read`) | 0 bytes | none |
| **29808465** | Johannsen 2018, *Neurogenetics* — 🔴 **the only functional study of Q230P** | 🔴 **`FTR-20260810-29808465-01` = `abstract_only`. No PMCID exists.** Not fetchable | n/a | none |
| **42193054** | *Curr Issues Mol Biol* 2026 | receipt `FTR-20260726-42193054-01` (`partial_fulltext_read`); **no manifest** | 0 bytes | none |
| **42721537** | Argentinian founder cohort | 🔴 **NO RECEIPT AT ALL** in the ledger | n/a | none |

🔴 **Three declared gaps that bound everything below.** (i) `CLAIM 030`'s load-bearing statement — *"protein not
detected"* for Q230P — rests on a paper LEGEND holds **at abstract level only**, with no PMC deposit. (ii) The
per-individual outcomes for the 62 literature cases in the survival analysis live in **Supplementary Table S1**,
which is named in the fetched body (`SUPPLEMENTARY MATERIAL S1`, `TABLE S1`) and whose contents are not in it.
(iii) `PMID 42721537` has no receipt and was not read.

---

## 1. The direct answer

**Neither of the two options the question offers is correct, and the third possibility is the finding: Q230P
spans the entire outcome range inside a single genotype, so there is no consistent survival advantage attached
to it to explain.** In the cohort that generated the statistic, **three of thirteen patients carry Q230P**, and
among them are **both** the oldest living WWOX-DEE patient on record (23 y 11 m, homozygous Q230P) **and** a
deceased patient (died at 8 y 3 m, also **homozygous Q230P**). Two of that cohort's three deaths fall in the
"≥1 missense" class. In the independent census, homozygous Q230P runs from **death at 3 y 3 m** to **alive at 12 y
and 10 y**. And in the one independent replication attempt, the mortality association **does not replicate**
(*p* = 0.432), there are **zero deaths among null/null**, and **the single premature death in the whole cohort is
a Q230P compound heterozygote**. **Q230P is roughly a third of the class the statistic rests on** — approximately
8–11 of the 30 individuals with ≥1 missense variant, with 2–3 unresolvable for overlap — so the class and the
paradox largely *are* the same object; but removing Q230P would remove both the class's longest survivor and some
of its deaths, and **the recomputation cannot be performed from published sources**, because the per-individual
data sit in a supplementary table not present in the retrievable body. ⇒ **`CLAIM 033`'s reservation (1) is
correct and should be strengthened, not softened: the "missense" class is a syntactic class assembled in silico,
its most frequent member has outcomes from death at 3 y 3 m to alive at 23 y 11 m, and the source paper's own
authors write that the hypomorph interpretation requires functional studies that do not exist.** On the
therapeutic question the evidence **does not choose**, and this file does not choose for it — but it narrows the
fork to a single measurement, named in §5.

---

## 2. Task 1 — decomposing the statistic by allele

### 2.1 The statistic, verbatim and in-act (PMID 36779245)

> "We stratified all 75 cases into one of three genetic groups: (1) null/null (= 45), (2) null/missense (= 15), (3) missense/missense (= 15). Using the Kaplan–Meier method to analyze time to death, we found that survival was much poorer for the double null group compared with the patients who had at least one missense pathogenic variant (‐value = .0085, log‐rank test). Probability of survival to the age of 5 years for the double null group was <50%; by comparison, it was >75% for the other two, presumably less severe, genetic groups. By the age of 10 years, the gap in survival probability widened, with the null group at 25% whereas the missense groups remained somewhat steady at >60%."

`surface: body` · Results 3.7, *Genotype–phenotype correlation*. ⚠️ the italic `p` of `p-value` is deleted by the
extractor in both places; the numerals are intact. ⚠️ `n` is likewise deleted before each `= 45 / = 15 / = 15`.

⇒ **The "≥1 missense" class is 30 of 75 individuals.** That is the denominator everything below is measured
against, and it has never been written down in LEGEND.

> "p.Gln230Pro in three of our patients (homozygous in two; compound heterozygous in one) and was reported in six previous families from Iran, Afghanistan, France, and Morocco"

`surface: body` · Results 3.6, *Genetic variants*.

### 2.2 The three Q230P patients in the statistic's own cohort — and they sit at both extremes

**Column-alignment verification, stated before any value is used.** The extracted Table 1 returns **13 patient
numbers but 12 genotype entries**, because Patients 9 and 10 are brothers sharing one entry. The mapping was
verified **three independent ways against the running text** before any row was read: the text states
*"p.Glu17Lys occurred in two of our cohort (Patients 6, 12)"* and entries 6 and 11 are the two `c.49G>A`
entries; *"homozygous p.Arg264Ter in Patient 4"* and entry 4 is `c.790C>T` homozygous; *"three were known to be
from consanguineous families (Patients 5, 8, 13)"* and the consanguinity row reads Yes at positions 5, 8 and 12.
All three reconcile only under the brothers-share-entry-9 mapping. **Positions 1–8 are unaffected by the
collapse**, and all three Q230P rows sit inside 1–8.

| Patient | Genotype (verbatim from Table 1) | Class (the paper's own) | Age, status |
|---|---|---|---|
| **1** | `c.689A > C, p.Gln230Pro (mat)/exon 7–8 deletion (pat)` | **Missense/null** | **4 y 7 m**, alive |
| **2** | `c.689A > C, p.Gln230Pro (homozygous)` | **Missense/missense** | 🟢 **23 y 11 m**, alive — *"We report the oldest living patient, aged 23 years 11 months."* |
| **5** | `c.689A > C, p.Gln230Pro (homozygous)` | **Missense/missense** | 🔴 **8 y 3 m (dec.)** |

> "Three patients (Patients 5, 6, 8) died at age 8, 11, and 6 years, respectively."

`surface: body` · Results 3.1.

🔴 **Two of the three deaths in the new cohort carry a missense allele.** Patient 5 is missense/missense (Q230P
homozygous); Patient 6 is missense/null (`c.49G > A, p.Glu17Lys (mat)/intron 4 deletion (pat)`). Only Patient 8
(`Exon 5 deletion (homozygous)`) is null/null. **In the cohort that generated the survival split, the class with
the better survival contributes two of three deaths.**

🔴 **And the same genotype occupies both tails.** Patients 2 and 5 are **both homozygous `c.689A>C p.Gln230Pro`**
— the same two alleles — and one is the oldest living patient on record while the other is dead at 8 y 3 m.

⚠️ **A second observation that attaches a genotype to a fact LEGEND already holds.** The paper states
*"Epilepsy was resistant to antiseizure medications (ASMs) in all patients, except Patient 5."* LEGEND's `N-15`
already records that "the only non-drug-resistant patient died". **That patient is homozygous Q230P.**

### 2.3 The per-genotype table, with distinct families and overlap resolution

⚠️ **The §12 trap is live and is not fully resolvable.** Nationalities are replaced by family indices per the
de-identification note.

| Genotype | Source | Patients | Distinct families | Outcome recorded | Overlap resolved? |
|---|---|---|---|---|---|
| **Q230P homozygous** | 36779245 Patient 2 | 1 | 1 (F-α) | **alive 23 y 11 m**, 21 y follow-up | 🟢 **Yes — novel.** Cannot be the census sisters (alive 12 y/10 y in 2021 ⇒ ~14/12 in 2023) |
| **Q230P homozygous** | 36779245 Patient 5 | 1 | 1 (F-β) | 🔴 **died 8 y 3 m** | 🔴 **NO.** Oliver lists one of the six previous Q230P families in the same country as this patient's reported country. **May be a re-report.** Unresolvable from published data |
| **Q230P / null (exon 7–8 del)** | 36779245 Patient 1 | 1 | 1 (F-γ) | alive 4 y 7 m | 🟡 partial — not matched to any census row, but the census reports no compound-het Q230P in that configuration |
| **Q230P homozygous** | 33916893 Table 1, sibling pair | 2 | 1 (F-δ) | **alive 12 y and 10 y**, both refractory to multiple ASMs | 🟢 Yes — traceable to `29808465` (ref [68]), which is **held at abstract level only** |
| **Q230P homozygous** | 33916893 Table S1 | 1 | 1 (F-ε) | 🔴 **death at 3 y 3 m** (Table 1's column for this row is headed *Death* and survivor rows read *"alive at"*) | 🟢 Yes — distinct family |
| **Q230P homozygous** | 33916893 census | 1 | 1 (F-ζ) | not recorded in LEGEND's locators | 🟡 census-level only |
| **Q230P / c.517-2A>G** (compound het) | 33916893 census | 2 | 1 (F-η) | not recorded in LEGEND's locators | 🟡 census-level only |
| **Q230P compound het ×2** | 33916893 census | 2 | 1 (F-θ) | not recorded | 🟡 census-level only |
| **Q230P / p.Gln72\*** | 40875931 case ID 11 | 1 | 1 (F-ι) | 🔴 **the only premature death in that entire cohort** | 🟢 Yes — registry cohort, distinct |
| **Q230P homozygous** | 40875931 case ID 23 | 1 | 1 (F-κ) | alive; declared **Novel** in the source | 🟢 Yes — declared novel |
| **Q230P, 4 families** | 30356099 | ≥4 | 4 | not decomposed in LEGEND's locators | 🔴 **NO — almost certainly a subset of the census's six families**, since the census is a review aggregating this cohort |

**Counting honestly:**
- **Distinct families established: 8** (F-α, F-γ, F-δ, F-ε, F-ι, F-κ, plus F-ζ and one of F-η/F-θ, which LEGEND's
  census locator enumerates as six families in total for that source).
- **Distinct patients established: ≈11.**
- 🔴 **Unresolvable: 2–3.** F-β may duplicate one of the census's six families; Piard's four families are almost
  certainly a subset of the census's six; and the census's F-ζ/F-η/F-θ outcomes are not recorded at the
  patient level in LEGEND.
- **An unresolvable overlap is a finding.** These cohorts re-report each other: Oliver's 75 cases are 13 new plus
  62 from the literature, and the 2021 census's 56 WOREE cases and Piard's 20 are inside that 62. **They are not
  independent samples and must never be summed.**

### 2.4 🔴 What happens if Q230P is removed — and why it cannot be computed

**Q230P is approximately 8–11 of the 30 individuals in the "≥1 missense" class: between 27 % and 37 %.** Three
convergent measurements support that magnitude and none of them was in LEGEND as a fraction of the class:

- Oliver: **3 of 13** own patients, plus **six previous families**.
- The 2021 census: **8 patients across 6 families**, and Q230P is the **most recurrent single variant of any
  class**, drawn at the lollipop axis maximum (`figure-attestation-from-prior-session`).
- Piard 2019: *"p.(Gln230Pro) was found in four families"* — the most recurrent missense allele in the largest
  primary WOREE cohort.
- The 2021 census tallies the whole WOREE variant set as **45 variants across 56 patient cases (34 loss-of-function
  + 11 missense)** — so **Q230P alone is a large fraction of an 11-variant missense set.**

**The recomputation is not possible from published sources.** The per-individual genotype-and-outcome rows for the
62 literature cases are in `SUPPLEMENTARY MATERIAL S1` / `TABLE S1`, which the retrievable body names and does not
contain. What *can* be said without them, and it is the operative point: **removing Q230P would remove the class's
single longest survivor — a censored observation anchoring the right tail of the Kaplan–Meier curve at 23 y 11 m —
and also remove at least two of the class's deaths (Oliver Patient 5; registry case ID 11).** The direction of the
resulting change is **not predictable**, and anyone who asserts it without the supplementary table is guessing.

### 2.5 🔴 The replication fails, and it fails on Q230P

From LEGEND's manifest for `PMID 40875931` (`figure-attestation-from-prior-session` for the table row):

- Table 2, premature death: **`0 (0.0) 1 (7.7) 0 (0.0) 2 2.44 0.432`** ⇒ **not significant; zero deaths among
  null/null; the single death in the null/missense group.**
- *"Notably, case ID 11 with WWOX variants (p.(Gln72\*); p.(Gln230Pro)) was the only individual who died prematurely, although the cause of death was unknown."*
- *"By contrast, p.(Gln230Pro), which has been previously reported as a 'mutational hotspot' in WWOX, was only present in 2 individuals in our cohort (case ID 11 and ID 23)."*
- Class sizes: *"Over half (n = 25, 56.8%) displayed the N/N variant genotype, 13 (29.5%) the N/M variant genotype, and only 6 (13.6%) the M/M variant genotype"* — **of 44 analysable cases.**
- 🔴 **The paper's Discussion asserts the opposite of its own Table 2**: *"…higher mortality are significantly associated with null/n[ull]"*. LEGEND's manifest already records this as a text-versus-table contradiction.
- Ascertainment, in the authors' own words: *"the patient registry may be biased toward capturing data from living individuals, possibly with milder phenotypes"*.

⇒ **The only independent test of the mortality association reports `p = 0.432`, an inverted direction, and a
Q230P allele in its only death.** This is not in `CLAIM 033`.

### 2.6 The long-survival signal is not confined to missense at all

From the 2021 census (`figure-attestation-from-prior-session`): homozygous **`p.Arg264Ter`** — a nonsense,
null/null genotype — recorded at **8 y 11 m and 5 y 2 m**; homozygous **`p.Trp44Ter`** at **7 y and 20 m**.
🔴 **And the column those endpoints sit in is headed *"Death/ last date of examination"*, so whether a divergence
is in survival or in follow-up length is not resolved by the table at all.** Any survival arithmetic built on
that census inherits that ambiguity.

---

## 3. Task 2 — the four candidate explanations, ranked on evidence

### Rank 1 — **(c) Confounded statistic.** Best supported, by a wide margin.

**Evidence for.** (i) The class is **syntactic, assigned from the DNA lesion type and never from a measured
protein effect** — and in the largest primary cohort *"All missense pathogenic variants but one (P3;
p.[Ser318Leu]) are interpreted based on in silico studies without experimental evidence (no RNA or protein
sequence analyzed)"*, with the same authors adding that *"It is likely that a fraction of predicted missense
variants identified in patients with WWOX-related encephalopathy results in loss of expression due to abnormal
splicing"* — i.e. **some "missense" alleles are probably null**. (ii) The source paper's own severity analysis
finds **no difference at all**: *"our WWOX-DEE patients were as severe as those with two loss-of-function null
alleles"*, and no difference in time to seizure onset (*p* = .65). (iii) Figure 4A's two missense-containing
curves have **95 % bands overlapping across the whole followed range**. (iv) The single replication attempt
returns *p* = 0.432 with the direction inverted and declares its own living-patient ascertainment bias. (v) The
class is 30 of 75 and roughly a third of it is one allele. (vi) 🔴 **The authors themselves decline to assert the
mechanism**: *"suggesting that the functional impact of some missense variants may result in a hypomorphic allele
compared to complete loss-of-function null variants. **Functional studies would be required to support this
hypothesis.**"* — and the abstract says *"at least one **presumed** hypomorphic missense pathogenic variant"*.
**Grammatical mood: the hypomorph reading is offered as a hypothesis in the very sentence that proposes it.**

**Evidence against.** *p* = .0085 on 75 individuals is not nothing, and the 10-year gap (25 % vs >60 %) is wide.
A confound has to be named, and ascertainment is the strongest candidate but is not demonstrated for Oliver's
series. **This explanation is ranked first but is not proven.**

### Rank 2 — **(a) Detection floor.** Plausible, entirely untested, and the assay's sensitivity is unknown here.

LEGEND has already narrowed `CLAIM 030` from *"protein absent"* to *"protein not detected"* with
`PREMISE: DETECTION_FLOOR`. 🔴 **This node can add only that the floor is not merely unmeasured but unreadable
from here**: the single source (`PMID 29808465`) is held **`abstract_only`**, has **no PMCID**, and is not
fetchable. **No quantification, no loading control, no antibody epitope, no exposure series and no limit of
detection is available to this analysis.** LEGEND additionally records that abundance measurements across the
allelic series are **not commensurable** — Western blot on fibroblasts for P47T and Q230P, immunofluorescence on
organoids for G372R — so even the comparison that makes Q230P look extreme is assay-mismatched.

### Rank 3 — **(d) Function without abundance.** This is `CLAIM 030`'s own thesis and it is consistent, not demonstrated.

`CLAIM 030` already states that severity tracks residual **function**, not abundance, on an allelic series in
which P47T has **normal protein and a mild phenotype with abolished binding** while Q230P has **no detectable
protein** and a severe phenotype. The Q230P outcome spread — 3 y 3 m to 23 y 11 m within one genotype — is
**compatible** with an abundance-independent phenotype, but it is equally compatible with modifier effects,
care differences and ascertainment. **No measurement discriminates.**

### Rank 4 — **(b) Tissue specificity.** Not excluded, and **nobody has looked.**

🔴 Checked against LEGEND before asserting: **every abundance measurement for a WWOX missense allele in this
corpus is in fibroblasts or in organoids. No WWOX protein measurement in patient brain, muscle, blood or any
other tissue exists for any missense allele anywhere in LEGEND's holdings.** The hypothesis that Q230P protein is
undetectable in fibroblasts and present in brain is therefore **untested rather than unlikely** — but it is also
the least parsimonious of the four, because it requires a tissue-specific stability difference for which this
gene has no precedent in the corpus.

### 🎯 The single discriminating measurement

> **A quantitative, epitope-mapped Western blot of WWOX in Q230P-carrying patient cells against a calibrated
> recombinant-protein standard curve, run to the assay's stated limit of detection, with the same antibody and
> the same matrix used for P47T and G372R — i.e. make the allelic series commensurable and put a number on the
> floor.**

It discriminates **(a) against (d)** directly: either residual Q230P protein exists below the previous blot's
floor, in which case `TX-003` has a pool to raise and `CLAIM 030`'s abundance/function dissociation needs
re-stating; or the floor is genuinely below any physiologically meaningful level, in which case survival in this
disease is not set by WWOX abundance. It leaves **(c)** untouched — that one needs the supplementary table — and
it is a **necessary precondition** for testing **(b)**, since a tissue comparison is meaningless without a
calibrated assay. It is the cheapest of the four tests and the only one that can be run on material that already
exists.

---

## 4. Task 3 — the therapeutic consequence, and the evidence does not choose

**The fork, stated exactly.**

- **Branch (i) — there is a pool the assay cannot see.** Then `TX-003` (chaperone / proteostatic rescue) becomes
  **more** plausible, not less: there is something to stabilise, and the allele most associated with long survival
  is also the one with the most headroom. `TX-002` (CRISPRa / endogenous boost) is **not** revived by this,
  because `N-05` and `DIS-003` reject it on a different ground — the bottleneck is downstream of transcription —
  and nothing here touches that.
- **Branch (ii) — the floor is real and survival is not abundance-limited.** Then every restoration lever's
  **assumed mechanism** weakens: `TX-003`'s endpoint (soluble, localised, functional WWOX) stops being obviously
  connected to the outcome that matters, and `TX-002` loses its last rationale. 🔴 **Gene addition (`TX-007`) is
  untouched either way**, because it does not restore a residual pool — it supplies protein *de novo*, and its
  efficacy argument rests on the mouse rescue, not on human abundance-outcome correlation.

🔴 **The evidence does not choose, and this file does not choose for it.** The reason is specific and is not
timidity: **the one paper that measured Q230P protein is held at abstract level, has no PMC deposit, and its
detection floor is therefore unknown to this analysis.** Branch (i) and branch (ii) are distinguished by exactly
that number.

**What can be concluded without choosing, and it is not nothing:**

1. 🔴 **`TX-003` must stop citing the survival statistic as support.** If the assumption "missense ⇒ residual
   protein ⇒ milder" fails on Q230P — the allele that is roughly a third of the missense class — then the class
   statistic cannot be evidence that a residual pool exists. **`TX-003`'s rationale has to stand on its own
   molecular evidence, which is currently `T6`.**
2. ✅ **`CLAIM 030`'s thesis survives this node and is strengthened.** Severity — and now survival — do **not**
   track abundance: the allele with no detectable protein spans the full outcome range. That is the claim's own
   prediction.
3. 🔴 **`CLAIM 033` needs a fifth reservation.** Its four existing reservations are correct and one of them
   (reservation 1) already names this contradiction. What it does not carry is that **the association fails to
   replicate**, that **two of three deaths in the generating cohort carry a missense allele**, and that **the
   class's most frequent allele occupies both tails**.
4. ⚠️ **Nothing here is prognostic for any individual**, and the finding cuts against prognostic use: within one
   genotype the recorded outcomes run from death at 3 y 3 m to alive at 23 y 11 m.

---

## 5. What LEGEND already knew · what is new

### 5.1 Already held — confirmed, not re-derived

- `CLAIM 033` reservation (1): the class is **syntactic, not functional**, and LEGEND's own sources falsify it as
  a proxy — Q230P missense with no detectable protein; P47T missense with normal protein and mild phenotype;
  P47R at the same residue with severe phenotype.
- `CLAIM 033` reservation (2): no intermediate phenotype; `null/missense` is not resolved separately.
- `CLAIM 030` addition of 2026-09-09: **Q230P in 8 patients across 6 families**, 4 homozygous and 4 compound
  heterozygous, all in the DEE28/WOREE block and none in SCAR12; **the endpoint within homozygous Q230P spans
  death at 3 y 3 m to alive at 12 y and 10 y**; *"Q230P is severe without being deterministic for early death."*
  🟢 **This node independently confirms and extends that sentence, and LEGEND wrote it first.**
- `CLAIM 030`'s own flag that `PAPER 041` (Johannsen 2018) is *"held here as abstract only and is the
  highest-value acquisition target in this lot."*
- The `PREMISE: DETECTION_FLOOR` narrowing, and the non-commensurability of the allelic-series assays.
- Piard's inconsistent premature-death definitions and its in-silico missense classification.
- `N-15`: the only non-drug-resistant patient died.

### 5.2 New in this node

1. 🔴 **The class denominator, never written down in LEGEND:** *"null/null (= 45), null/missense (= 15),
   missense/missense (= 15)"* — **the "≥1 missense" class is 30 of 75.**
2. 🔴 **Q230P is ≈8–11 of those 30 — roughly a third of the class the statistic rests on.**
3. 🔴 **In the generating cohort, two of the three deaths carry a missense allele**, and only one is null/null.
4. 🔴 **The two homozygous Q230P patients in that cohort are the oldest living patient (23 y 11 m) and a death at
   8 y 3 m** — same two alleles, opposite tails. Column alignment verified three ways before use.
5. 🔴 **The only non-drug-resistant patient in that cohort — a fact LEGEND already held without a genotype — is
   homozygous Q230P**, and died at 8 y 3 m.
6. 🔴 **The replication fails and fails on Q230P:** *p* = 0.432, zero deaths among null/null, and the cohort's
   only premature death is a Q230P compound heterozygote. `CLAIM 033` does not carry this.
7. 🔴 **Long survival is not confined to missense:** homozygous nonsense `p.Arg264Ter` at 8 y 11 m and 5 y 2 m.
8. ✅ **The authors decline the mechanism in their own words:** *"Functional studies would be required to support
   this hypothesis"*, and the abstract says *"presumed hypomorphic"*. The hypomorph reading is a hypothesis in
   the sentence that proposes it.
9. ✅ **Checked and recorded: no WWOX protein measurement in any tissue other than fibroblasts (or organoids)
   exists for any missense allele in LEGEND's holdings.** Explanation (b) is untested, not refuted.
10. 🔴 **The recomputation is blocked at a named artefact** — `SUPPLEMENTARY MATERIAL S1` / `TABLE S1` of
    `PMID 36779245` — which is the single highest-value acquisition for this question.

---

## 6. Corrections, with exact file and line coordinates

**W5-C1 — `CLAIM 033` needs a fifth reservation: the association does not replicate.**
- **File:** `disease-models/wwox/registries/claim_registry_current.md` · `CLAIM 033` begins **line 602**; the
  reservations run from **line 611**; reservation (3) is at **line 614**.
- **Issue:** the claim carries four reservations and none of them is *"an independent cohort tested this and got
  `p = 0.432` with the direction inverted."*
- **Proposed addition after the existing reservations:** `**(5) L'associazione NON è stata replicata.** Nella coorte-registro indipendente (`PMID 40875931`) la morte prematura **non è significativa** (Tabella 2: `0 (0.0) 1 (7.7) 0 (0.0) 2 2.44 0.432`), **zero decessi fra i null/null**, e **l'unico decesso prematuro dell'intera coorte porta Q230P** (`p.(Gln72*)`;`p.(Gln230Pro)`, case ID 11). La Discussion di quel paper afferma il contrario della propria Tabella 2. Gli autori dichiarano inoltre un bias di arruolamento verso individui viventi. ⇒ il claim descrive **un'associazione in una sola coorte, non replicata**.`

**W5-C2 — `CLAIM 033` should carry the class denominator and the Q230P fraction.**
- **File:** same · the `**Summary:**` line at **line 610**
- **Exact current text (fragment):** `In WWOX-DEE i pazienti con genotipo biallelico **null/null** hanno sopravvivenza significativamente peggiore di quelli con **almeno una variante missense** (Kaplan-Meier, log-rank **p = .0085**; 5 anni: <50% vs >75%; 10 anni: ~25% vs >60%).`
- **Proposed replacement:** as above, plus `**Denominatori (verbatim, letti alla fonte 2026-09-21):** null/null n=45 · null/missense n=15 · missense/missense n=15, su 75 casi. **La classe «≥1 missense» è 30 individui**, e **circa 8–11 di essi (≈⅓) portano Q230P** — l'allele che secondo [[claim_registry_current#CLAIM 030]] non dà proteina rilevabile. **Due dei tre decessi della coorte generatrice portano un allele missense.**`

**W5-C3 — `CLAIM 030` should record that Q230P occupies both tails inside the generating cohort.**
- **File:** same · `CLAIM 030` begins **line 551**; the 2026-09-09 addition is at **line 359** (it is appended
  under a different claim block, which is itself worth noting — the addition naming `CLAIM 030` sits at line 359
  while `CLAIM 030`'s own block begins at line 551).
- **Proposed addition:** `**Addition 2026-09-21 (primary, read in-act — `PMID 36779245` Table 1 + Results 3.1/3.6/3.7).** Nella coorte che genera la statistica di sopravvivenza, **tre dei tredici pazienti portano Q230P**: uno `missense/null` vivo a 4 y 7 m, e **due omozigoti Q230P — uno è il paziente vivente più anziano mai riportato (23 y 11 m) e l'altro è deceduto a 8 y 3 m**. Stessi due alleli, code opposte. ⚠️ Il paziente deceduto è anche **l'unico non farmaco-resistente** della coorte (*"resistant … in all patients, except Patient 5"*), il che attacca un genotipo al fatto già registrato in `N-15`. Allineamento di colonna della Table 1 verificato **tre volte** contro il testo corrente prima dell'uso (E17K → Patients 6/12; R264Ter → Patient 4; consanguineità → Patients 5/8/13).`

**W5-C4 — the acquisition target should be named and ranked.**
- **File:** `disease-models/wwox/research/full_text_queue_current.md`
- **Issue:** two artefacts now block this question and neither is queued as such: (i) `PMID 29808465`
  (Johannsen 2018) — **`abstract_only`, no PMCID**, the only functional study of Q230P and the only source of the
  detection floor; (ii) **`SUPPLEMENTARY MATERIAL S1` / `TABLE S1` of `PMID 36779245`** — the per-individual
  genotype-and-outcome rows for the 62 literature cases, without which the survival contrast cannot be
  decomposed. `PMC10952634` is open access, so the supplement is very likely retrievable by a route this session
  did not attempt.
- **Proposed:** create two `FT-` entries, the second flagged as **low-cost / high-yield** — one supplementary
  file closes the central arithmetic of this node.

**W5-C5 — `PMID 42721537` has no receipt and is cited in reasoning.**
- **Issue:** the Argentinian founder cohort is referenced in this repository's reasoning (e.g. in the splice-allele
  census as `FT-110`, five patients on `c.107+1G>A`) but `fulltext_receipts.py status --pmid 42721537` returns
  **no receipt at all**. It was not read for this node and nothing here rests on it.
- **Proposed:** either queue it with a receipt or mark every surface that cites it as census-level.

---

## 7. Source attribution

Retrieved from **PubMed / PubMed Central**. `PMID 36779245` was fetched and read in this session; all values from
`33916893`, `30356099` and `40875931` are **prior-session table/figure attestations from LEGEND's receipt-backed
locator manifests** and are labelled as such.

| PMID | Citation | DOI |
|---|---|---|
| 36779245 | Oliver KL, Trivisano M *et al.* WWOX developmental and epileptic encephalopathy: understanding the epileptology and the mortality risk. *Epilepsia* 2023 | [10.1111/epi.17542](https://doi.org/10.1111/epi.17542) |
| 33916893 | Banne E *et al.* WWOX Gene and Protein — a Critical Review. *Cells* 2021 | [10.3390/cells10040824](https://doi.org/10.3390/cells10040824) |
| 30356099 | Piard J *et al.* The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome. *Genet Med* 2019 | [10.1038/s41436-018-0339-3](https://doi.org/10.1038/s41436-018-0339-3) |
| 40875931 | WWOX-DEE registry cohort. *Neurology* 2025 | [10.1212/WNL.0000000000213883](https://doi.org/10.1212/WNL.0000000000213883) |
| 39507621 | Teplyshova AM *et al.* *Front Genet* 2024 — adult WWOX-DEE case | [10.3389/fgene.2024.1477466](https://doi.org/10.3389/fgene.2024.1477466) |
| 42193054 | *Curr Issues Mol Biol* 2026 | [10.3390/cimb48050449](https://doi.org/10.3390/cimb48050449) |
| 29808465 | Johannsen J *et al.* *Neurogenetics* 2018 — 🔴 **the only functional study of Q230P; held `abstract_only`; no PMCID** | via PubMed (DOI not resolved by the converter in this session) |
| 42721537 | Argentinian founder cohort — 🔴 **no receipt; not read; nothing here rests on it** | not resolved in this session |

---

**End.** Not medical advice, and not prognostic for any individual. Read-only toward every canonical file; nothing
promoted, nothing committed.
