# COMMIT CANDIDATE — CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01

**Source:** batch `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION`, waves 1–3.
Readings: `FTR-20260920-29067327-01`, `FTR-20260920-36498839-01` (both `partial_fulltext_read`,
`figures: unavailable`). Supporting census and metadata-depth work in
`disease-models/wwox/analysis/wwox_heterozygote_phenotype_audit_20260920.md`.
**Ledger:** `fulltext_receipts.py verify` → **OK: 166 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — a qualifier and a premise tag on an existing claim.
**Target:** no working-model bump proposed.
**Status:** `PROPOSED — NOT PROPAGATED`. Awaiting operator.
**Review floor:** R2. 🔴 **`legend-locator-audit` (R4) is NOT triggered but SHOULD be considered by
the operator**: `CLAIM 032` is `clinical relevance: VERY HIGH` and load-bearing on the gene-therapy
dose argument. It is `in observation`, not `consolidated baseline`, so the R4 trigger does not fire
mechanically — that is a fact about the trigger, not about the stakes.

---

## 1 · What is proposed, and what is refused

**Proposed:** add to `CLAIM 032` an **endpoint qualifier** and a `PREMISE_TAG`, recording that its
three supporting sources measured **survival, growth, gross morphology, neoplasia and overtly
observed behaviour** — and **not** cognition, EEG or network excitability.

**Refused, explicitly:** the claim is **NOT** reversed · its `Status: in observation` is **NOT**
changed · the haploinsufficiency finding is **NOT** withdrawn · **no** therapeutic candidate is
created or removed · no working-model edit.

🔴 **This candidate does not say haploinsufficiency is deleterious. It says the claim's own
caveat has now been checked, and the caveat was right.**

---

## 2 · What `CLAIM 032`'s three sources actually measured

`CLAIM 032` already declares: *"la soglia è nota per **sopravvivenza e morfologia**, **non per
cognizione ed epilessia**."* This candidate exists because that sentence turned out to be exactly
and literally true — and stronger than it reads.

| Source | Endpoint actually measured | Age | Cognition / EEG tested? |
|---|---|---|---|
| **Aldaz 2014** (`PMID 24932569`, `PAPER 053`) — a **review**, not primary phenotyping | spontaneous neoplasia + lifespan | lifetime | **No** |
| **Tochigi 2019** (`PMID 31340538`) | western-blot band intensity + immunohistochemistry | PND 5/10/15/21 | **No — and `+/+` and `+/lde` are pooled as "normal" controls** |
| **Human carrier parents** (Abdel-Salam and others) | clinical observation; the quoted sentence is a **tumour** observation | — | **No — no published carrier has a neuropsych battery, EEG or quantitative imaging** |

🔴 **A quotation defect to repair while we are here.** `CLAIM 032` and `PAPER 053` both quote Aldaz
as *"loss of one Wwox allele (i.e. haploinsufficiency) appears **not to be deleterious**"*. The
sentence in the source continues — *"…appears not to be deleterious **or carcinogenic**"* — and its
subject is the preceding clause, *"no evidence of spontaneous neoplasia in any tissue examined"*.
**It is a tumour sentence.** The shortened quote reads as a general statement about organismal
phenotype; the full sentence is about cancer. This is the `D-15` family and it is ours, not a
review's.

**Therefore the third leg of `CLAIM 032` is `nobody looked`, not `looked and found nothing`** — and
those are different evidentiary states that the current wording conflates.

## 3 · What the counter-evidence is, and what it is not

| Source | Lab | Finding | Weight |
|---|---|---|---|
| `PMID 34634460` Breton 2021 | **Carlen (Toronto)** — outside Chang | spontaneous electrographic bursting in **4 of 23 slices from 14 Syn1-Cre het mice** vs **0 of 11 slices from 7 WT**; *"also observed in heterozygote mice … may be reflective of epileptic network activity; however, there are no clear behavioral seizures"* | **strongest independent signal.** ⚠️ conditional (Syn1-Cre), **no statistic reported** for het vs WT, het pooled into "S-CTL" elsewhere in the same paper, Aqeilan is a co-author |
| `PMID 32000863` Cheng 2020 | Hsu/Chang (NCKU) | het Tc-MEP latency **2.13 ± 0.22 ms (n=5) vs WT 1.39 ± 0.13 (n=10), p<0.05** at 3 weeks; amplitude normal; rotarod/gait/clasping normal | concordant, **different instrument** |
| `PMID 29067327` §3.5 + `PMID 36498839` §2.5 | Chang (NCKU) | aged `Wwox+/−` memory decline, cortical aggregates | **single lab, corroboration not replication**; §3.5 has **no n**; aged, not developmental |
| `PMID 27569545` Leppa 2016 | **Geschwind (UCLA)** — outside the field | heterozygous intragenic `WWOX` CNVs, *"lower-penetrance locus"*, ASD multiplex families | 🔴 **DOES NOT SUPPORT THE QUALIFIER.** Primary body behind a licence wall (permanently unobtainable here); abstract carries no number at all; the circulating OR is review-reported and **two reviews by the same author disagree** (9 vs 12, 1,532 vs 3,565). Signal is **bidirectional** — duplications cannot evidence haploinsufficiency. Kept as a recorded negative. |

**The pattern across the independent sources is the finding: normal behaviour, abnormal
instrument.** Every endpoint `CLAIM 032` rests on is of the class these studies show is insensitive
to the heterozygote.

**And a structural reason the phenotype could not have been seen:** the field **pools heterozygotes
into control groups**. Tochigi pools `+/+` with `+/lde` as "normal"; Breton pools het into "S-CTL";
our own [[paper_registry_current#PAPER 058]] reports spontaneous seizures as `0/14 controls`, with
the control genotypes **undifferentiated**. The Aqeilan colony is bred het × het, so ~15 CNS papers
had het littermates available, and the only het data ever published from it are fertility rate and
litter size.

## 4 · Proposed text (verbatim, for the operator to accept, edit or refuse)

Add to `CLAIM 032`:

> **🔴 Endpoint qualifier (2026-09-20, `SCIENTIST_CHANG_NS…` waves 1–3).** The three sources of this
> claim measure **survival, growth, gross morphology, spontaneous neoplasia and overtly observed
> behaviour**. None measures cognition, EEG or network excitability, and Tochigi 2019 **pools
> `+/+` with `+/lde` as "normal"**. The Aldaz sentence quoted above is, in its source, a **tumour**
> sentence (*"…not to be deleterious **or carcinogenic**"*, following *"no evidence of spontaneous
> neoplasia"*). `PREMISE: NOBODY_LOOKED` — this leg is untested, not tested-negative.
> **Counter-directional evidence, flagged not propagated:** subclinical instrument-level findings in
> heterozygotes from **three laboratories** (Breton 2021 network bursting, Carlen/Toronto; Cheng
> 2020 Tc-MEP latency, NCKU; Chang 2017/2022 aged memory, NCKU), against normal behaviour in the
> same animals. `REVIVAL_TRIGGER`: an aged germline `Wwox+/−` behavioural battery by a laboratory
> outside NCKU, seizure provocation on the `+/lde` rat heterozygote, or EEG/neuropsych on already
> identified WWOX-DEE carrier parents.
> **What does NOT change:** haploinsufficiency remains compatible with normal survival, growth and
> gross morphology, and every published human carrier parent remains clinically well. **What does
> change:** the corollary *"partial restoration may suffice"* may no longer be stated **without
> naming the endpoint it is sufficient for.**

## 5 · Declared limits of this candidate

- Both Chang readings are `partial_fulltext_read` with `figures: unavailable`. **No panel was
  inspected**, so per `D-14` the het findings are carried as **flag, not reversion**. `FT-104`
  records the residual debt.
- Breton 2021 was reached at **abstract/metadata depth**; its quote is verbatim from its deposit and its
  **missing statistic** is stated rather than filled in.
- 🔴 **The Leppa limit declared above was right, and is now hardened (2026-09-20, wave 5).** The primary body
  is **unobtainable in this environment and permanently so**: PMC5011063 is *in* PMC but **not in the open-access
  subset** — `get_copyright_status` returns *All rights reserved*, `is_open_access: false`. The route will always
  return empty; `FT-103` is re-queued as **acquisition-blocked (licence wall)**, not merely unread.
  **The primary abstract's entire WWOX content is one clause** — *"another lower-penetrance locus involving
  inherited deletions and duplications of WWOX"* — with **no count, no denominator, no percentage, no p-value
  and no odds ratio**. The paper's only stated denominator is **1,532 AGRE families**.
  🔴 **And the second-hand numbers are now actively suspect, not merely unverified.** The same senior author
  reports the same result twice, incompatibly: **Aldaz & Hussain 2019** gives *"9 affected children, with very
  high odds ratio"* against 1,532 families and **no numeric OR**; **Aldaz & Hussain 2020** gives 12/3565 vs
  1/2633, p=0.01, **OR = 8.8**. They disagree on count (9 vs 12), unit (children vs families), denominator
  (1,532 vs 3,565) and on whether a numeric OR exists at all. At most one is a faithful transcription, and
  `OR = 8.8` may have been **computed or imported by the reviewing author** rather than quoted. This is `D-15`
  caught in the act, and it is why the candidate never leaned on the figure.
  ⚠️ **A logical cap that survives the numbers entirely: the signal is BIDIRECTIONAL.** Duplications sit in the
  same finding as deletions, and **a duplication cannot evidence haploinsufficiency**. This is a dosage-
  *disturbance* / locus-*fragility* signal, not a half-dose signal — WWOX spans FRA16D, the second-most-common
  fragile site, and DGV puts large germline WWOX CNVs at ~0.10% of 27,263 individuals, the same order as the
  case rate being claimed. **Leppa 2016 therefore does not support the endpoint qualifier and is not used for
  it.** It is recorded because it was the best human candidate and it did not survive examination.
- Tochigi 2019 (`PMID 31340538`) and Mallaret (`PMID 24369382`) could not be re-read in this
  environment (no PMCID / empty PMC body). The Tochigi pooling statement is the delegate's reading.
- **This candidate changes a `VERY HIGH` clinical-relevance claim that carries the dose argument.
  It is the one item in this batch that most deserves the operator's own eyes.**
