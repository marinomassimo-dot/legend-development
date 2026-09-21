# COMMIT CANDIDATE — CC-20260921-CLAIM033-REPLICATION-01

**Source:** Scientist B, node `Q230P_SURVIVAL_PARADOX`
([`q230p_survival_paradox_20260921.md`](../../analysis/q230p_survival_paradox_20260921.md)),
reading **`PMID 36779245`** in-act — `PMC10952634`, body ≈ 31,000 characters, **including Table 1
and the genotype-class denominators**, with column alignment verified three independent ways
against running text before use.
**Ledger:** `fulltext_receipts.py verify` → **OK: 188 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — one reservation added to one claim, denominators added to another,
two queue entries. **No claim is reversed and no status moves.** `CLAIM 033` already carries four
reservations and already tags `missense = ipomorfo` as `IPOTESI`; this adds the fifth and the
sharpest.
**Target:** `working_model_version` MINOR bump at batch time. No `BLOCCO 1` change.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R3.** `CLAIM 033` is the most directly **prognostic** statement in the model and
the one a family is most likely to be told. It is not reversed here — it is bounded.

---

## 1 · The finding: Q230P spans the whole outcome range inside one genotype

The node asked whether the survival advantage of the "≥1 missense" class is carried by `Q230P` or
whether `Q230P` rides along. **The answer is neither**, and it is better than either.

From the cohort that generated the statistic (`PMID 36779245`), Table 1:

| Patient | Genotype | Class | Outcome |
|---|---|---|---|
| 1 | `Q230P` / exon 7–8 deletion | missense/null | alive, 4 y 7 m |
| 2 | **`Q230P` homozygous** | missense/missense | 🟢 **alive, 23 y 11 m — the oldest patient on record** |
| 5 | **`Q230P` homozygous** | missense/missense | 🔴 **died, 8 y 3 m** |

🔴 **The same two alleles, in the same cohort, occupy opposite tails.** There is no consistent
survival advantage attached to `Q230P` for a mechanism to explain — **which dissolves the paradox
rather than solving it.**

And the class itself carries the deaths: *"Three patients (Patients 5, 6, 8) died"* — **two of the
three carry a missense allele**; only Patient 8 (`exon 5 del` homozygous) is null/null.

> ⚠️ **One attachment that must travel with its uncertainty.** *"Epilepsy was resistant to ASMs in
> all patients, except Patient 5."* The single non-drug-resistant patient in the cohort — a fact
> LEGEND already held under `N-15` **without a genotype attached** — is **homozygous `Q230P`, dead
> at 8 y 3 m**. `n = 1`. **It is not a treatment-response signal and must not become one.**

## 2 · The denominators, which LEGEND did not have

> *"We stratified all 75 cases into one of three genetic groups: (1) null/null (= 45),
> (2) null/missense (= 15), (3) missense/missense (= 15)."*

⇒ the "≥1 missense" class is **30 of 75**. `Q230P` is **≈ 8–11 of those 30 (27–37 %)**, from three
convergent measures (3 of Oliver's 13 plus *"six previous families"*; the 2021 census's 8 patients
across 6 families, `Q230P` the **most recurrent variant of any class**; Piard's *"found in four
families"* against a whole-WOREE missense set of only **11 variants**).

🔴 **The recomputation cannot be completed and is not attempted.** The per-individual rows for the
62 literature cases live in `SUPPLEMENTARY MATERIAL S1` / `TABLE S1`, **named in the body and not
in it**. What is certain is that removing `Q230P` removes **both** the class's longest survivor —
a censored observation anchoring the right tail — **and at least two of its deaths**. **The
direction is unpredictable, and anyone asserting it without that table is guessing.**

## 3 · 🔴 The association does not replicate, and it fails on `Q230P`

`PMID 40875931` (registry cohort), Table 2: **`0 (0.0) 1 (7.7) 0 (0.0) 2 2.44 0.432`** — **not
significant, and zero deaths among null/null.** Its single death:

> *"case ID 11 with WWOX variants (p.(Gln72\*); p.(Gln230Pro)) was the only individual who died
> prematurely."*

⚠️ **That paper's Discussion asserts the opposite of its own Table 2**, and its authors declare
living-patient ascertainment bias. **`CLAIM 033` carries none of this.** Also recorded: long
survival is **not** confined to missense — homozygous nonsense `p.Arg264Ter` at **8 y 11 m** and
**5 y 2 m**.

## 4 · §12 overlap, resolved as far as published data allows

**8 distinct families and ≈ 11 distinct patients** established; **2–3 unresolvable**. Oliver's
Patient 2 is provably novel (census sisters alive at 12 y / 10 y in 2021 ⇒ ~14 / 12 by 2023).
Patient 5's family **may duplicate** one of the six previously reported `Q230P` families —
**unresolvable from published data, and stated as such rather than assumed either way.** Piard's
four families are almost certainly a subset of the census's six.

🔴 **These cohorts re-report each other** — Oliver's 75 = 13 new + 62 from the literature, which
contains the census's 56 and Piard's 20 — **and must never be summed.**

## 4bis · 🔴 PRIMARY-SOURCE VERIFICATION, added on Operator instruction

The body of `PMID 36779245` was subsequently read **in-act by the Orchestrator** from `PMC10952634`
and **Table 1 reconstructed independently of the delegate** —
[`oliver2023_table1_independent_reconstruction_20260921.md`](../../analysis/oliver2023_table1_independent_reconstruction_20260921.md).

**Everything in §1–§4 above is confirmed at source**, and the alignment was **established rather
than assumed**: the extraction returns Table 1 as parallel row-lists (13 ages, 11 variant entries,
12 class entries), and 🔴 **Table 1 carries a published correction to column 9** — so three
independent anchors in the running text were used to fix the mapping, and all three agree. The
`Q230P` rows are safe.

**Two things the verification ADDS, and both belong in the fifth reservation:**

1. 🔴 **The deaths are not concentrated in the null class — verified per patient.** Of the three
   deceased, **Patient 5 is `missense/missense`** and **Patient 6 is `missense/null`**
   (`p.Glu17Lys` / intron 4 deletion); **only Patient 8 is `null/null`.**
2. 🔴 **The pooled sample combines two strata that differ in ascertainment AND in genotype
   composition**, from the paper's own Table 3 — **mortality 23 % (this cohort) vs 38 %
   (literature)** with **mean age 8 y 2 m vs 3 y 4 m**, and class mix **50/33/17 vs 60/15.5/24.5**.
   The authors note the age–mortality inversion themselves — *"despite our patient group being
   notably older … the mortality was lower"* — **without treating it as a bias term**, and both
   strata enter one Kaplan–Meier.
3. 🔴 **Censoring is age-at-publication, not follow-up.** Figure 4A's dashes are *"the most recent
   age known to be living of each individual (censored observations)"*. In a literature-assembled
   cohort an early-fatal case is reported **because** it died, while a living case is reported at
   whatever age someone wrote it up. **That is informative censoring and the analysis does not
   address it.** ⚠️ The median literature age is **2 y 6 m**, so the *">60 % beyond 10 years"* tail
   rests on few individuals inside groups of **15**, with **no numbers-at-risk reported**.

**Two further limbs are therefore added to the proposed fifth reservation:** the **ascertainment
asymmetry** (2) and the **censoring definition** (3).

> ✅ **And what the verification did NOT overturn, stated because it would have been easy to
> overstate:** the descriptive imbalance is real, the log-rank result is as reported, and null/null
> remains the worse class on the assembled data. **`CLAIM 033` is bounded, not reversed.** What
> fails is its transfer to an individual — which is what `D-24` records.

🔴 **`TABLE S1` remains unretrieved and is now known to be unreachable from here**: `curl` to both
PMC hosts returns `CONNECT tunnel failed, 403`; `WebFetch` returns `EGRESS_BLOCKED`; the MCP returns
the body **and the two supplementary file names with no content**. **The recomputation stays
blocked and no direction is asserted** — `FT-122` stands, and it is an **open-access** file, so the
obstacle is a route, not a paywall.

## 4ter · 🔵 CREDIT: LEGEND held the both-tails datum already, under a different claim

Recorded because this session nearly reported it as a discovery.

`CLAIM 019` — not `CLAIM 033`, and not the claim this node was examining — already carries, in its
own body:

> *"nella coorte Oliver 2023 un paziente **Q230P omozigote** è il **più anziano dello studio
> (23 anni e 11 mesi, vivo)**; un altro Q230P omozigote è **morto a 8 anni**; il paziente con
> **Q230P + delezione** … è **vivo a 4 anni e 7 mesi**. La variabilità individuale è ampia."*

**All three `Q230P` patients, with their outcomes, and the conclusion drawn.** LEGEND wrote it
first, and this is the second time in one session that a finding presented as new turned out to be
held — the first was `CLAIM 030`'s 2026-09-09 note that *Q230P is severe without being deterministic
for early death*.

**What this node genuinely adds**, kept honest by the above: verification from **Table 1 at source**
with the alignment established against three anchors; the **denominators** (45 / 15 / 15 of 75);
the **replication failure** in the registry cohort; the **ascertainment asymmetry** between the two
pooled strata; and the **censoring definition**. The *datum* was held; the *arithmetic around it*
was not.

🔴 **And it is a sixth instance of this session's structural pattern, in a new form.** The others
were *existence without a record*; this is **existence in the wrong place** — a finding filed under
`CLAIM 019` that the `CLAIM 033` analysis needed, with nothing connecting them. `CLAIM 033`'s
`Wikilinks` do not reach `CLAIM 019`. ⇒ **added to the proposal: cross-link the two claims**, so the
next reader of the prognostic claim meets the allele that spans both its tails.

## 5 · What is proposed

**(a0) `CLAIM 033` ↔ `CLAIM 019` — add the missing cross-link** (see §4ter): the claim that
stratifies survival by allele class must reach the claim recording that its flagship missense allele
spans both tails.

**(a) `CLAIM 033` — add a fifth reservation: *the association does not replicate*.** Naming the
registry cohort's non-significant result, its zero null/null deaths, its single death carrying
`Q230P`, its Discussion contradicting its own Table 2, and its declared ascertainment bias.

**(b) `CLAIM 033` Summary — add the denominators** (45 / 15 / 15 of 75) and the `Q230P` fraction of
the missense class (≈ 27–37 %), with the note that the recomputation is blocked on `TABLE S1`.

**(c) `CLAIM 030` — record the both-tails finding.** Two homozygous `Q230P` patients in one cohort
at 23 y 11 m alive and 8 y 3 m dead. ✅ **This strengthens `CLAIM 030` rather than challenging
it**: its thesis is that severity tracks residual **function**, not abundance, and a genotype
spanning both tails is exactly what a non-abundance-determined phenotype looks like.

**(d) Two acquisitions** → `FT-122`: **`TABLE S1` of `PMID 36779245`** (🎯 `PMC10952634` is open
access — **one supplementary file closes the central arithmetic of this node; lowest cost, highest
yield item in the queue**) and **`PMID 29808465`** (abstract-only, no PMCID — the Q230P detection
floor).

**(e) `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`** — one row:

> **D-24** · *"a genotype class with better average survival means its members do better"* ·
> **Why it is FALSE here:** the most recurrent missense allele in WOREE occupies **both tails of the
> same cohort** — homozygous `Q230P` at 23 y 11 m alive and at 8 y 3 m dead — and **two of the
> generating cohort's three deaths carry a missense allele**. The class statistic is a population
> average over a class whose members are **classified syntactically, from the lesion in the DNA,
> never from a measured effect on protein**; the source itself says *"All missense pathogenic
> variants but one… without experimental evidence"* and *"Functional studies would be required to
> support this hypothesis"*. **A class average is not a prognosis for a member of the class.**
> **Detection rule:** before a genotype-class statistic is used about an individual allele, ask what
> that allele's own outcomes look like *inside* the class.

⚠️ **Numbering:** `D-17` is **reserved** (proposed 2026-09-21, **DEFERRED by the operator**, not in
the ledger). This session's other candidates propose `D-18`–`D-23`. **Do not renumber into `D-17`.**

## 6 · Therapeutic consequence — and the evidence was not made to choose

🔴 **`TX-003` must stop citing the survival statistic as support.** If *"missense ⇒ residual
protein"* fails on a third of the class, the class statistic is **not evidence that a residual pool
exists**, and `TX-003` falls back on its own molecular case — which is where it should always have
stood.

✅ **`CLAIM 030`'s thesis survives and is strengthened** (§5c).

✅ **`TX-007` is untouched.** Gene addition supplies protein *de novo* and never depended on a
residual pool. **This is the second time today that a finding which lowers confidence elsewhere
leaves gene addition exactly where it was.**

**The fork that is NOT resolved, and deliberately:** whether `Q230P` has a pool below the Western
blot floor (`TX-003` more plausible) or whether survival here is not abundance-determined at all
(every restoration lever's assumed mechanism weakens, gene addition excepted). **The one paper that
measured `Q230P` protein is abstract-only from here.** The discriminating measurement is named in
§7 and the candidate does not pick a side.

## 7 · The discriminating measurement

A **quantitative, epitope-mapped WWOX Western blot in `Q230P` cells against a calibrated
recombinant standard curve run to the stated limit of detection**, with the **same antibody and
matrix** as `P47T` and `G372R`. It makes the allelic series commensurable — `CLAIM 030` already
records that it is not — and **puts a number on the floor** `CLAIM 030`'s `PREMISE: DETECTION_FLOOR`
currently leaves open. Separates (a) from (d), is a precondition for (b), cheapest of the four, and
runs on material that already exists.

## 8 · What is explicitly REFUSED

- ❌ **`CLAIM 033` is not reversed or withdrawn.** It is bounded by a fifth reservation. Its
  `p = .0085` stands as what it is: a population statistic over a syntactic classification.
- ❌ **No recomputation of the survival contrast** without `TABLE S1`. Both directions are arguable
  and neither is evidenced.
- ❌ **No prognostic statement about any allele or any person.** The finding is the opposite: a
  class average does not transfer to a member.
- ❌ **No treatment-response inference** from Patient 5's ASM responsiveness. `n = 1`.
- ❌ **No new gate** (§26). One ledger row with a detection rule.

> 🔵 **Credit where it is due, and it is not this session's.** `CLAIM 030`'s 2026-09-09 addition
> already wrote that *Q230P is severe without being deterministic for early death*, and already
> flagged Johannsen as the highest-value acquisition. **LEGEND wrote it first.** This node confirms
> and quantifies that sentence from the primary. ⚠️ Scientist B flagged that addition as possibly
> filed under the wrong claim block; **checked — it is not.** It sits inside `CLAIM 019` (the Q230P
> functional-endpoint claim), which is where a Q230P genotype-distribution addition belongs, and it
> cross-links `CLAIM 030` from its `Wikilinks` line.

## 9 · Growth delta

`claims +0 · papers +0 · corpus +0`.

---

*Sources retrieved from **PubMed / PubMed Central**.
DOIs — [36779245](https://doi.org/10.1111/epi.17542) · PMCID `PMC10952634` — **both verified by
`convert_article_ids` at drafting time, by copy, in the same act.** `PMID 40875931` and
`PMID 29808465` return **the PMID alone — no DOI, no PMCID** (verified), which independently
confirms `29808465` as unobtainable by any automated route here. *This session reconstructed two
DOIs from memory earlier and caught both; nothing here is carried without a copy.*
Not medical advice, and nothing in this candidate is a prognosis.*
