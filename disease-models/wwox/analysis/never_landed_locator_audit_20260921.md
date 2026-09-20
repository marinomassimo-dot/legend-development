# Never-landed locator audit — narrow cut

**Date:** 2026-09-21 · Orchestrator, read-only. No canonical file edited.
**Authorised scope:** *"search specifically for other high-value claims where a strong locator
already exists in a receipt/manifest but is absent from the corresponding canonical claim"*, with an
explicit instruction to **abandon the audit if it began expanding toward the fenced-off mass
registry↔ledger reconciliation.**

---

## 0 · The first cut was abandoned, and why — this is a method finding

The obvious instrument is each manifest's `landing` field. Measured across all **81** deep-dive
manifests: **74 of 81 have no claim in `landing`.**

🔴 **That is not a finding; it is a definitional artefact, and reporting it as a finding would have
been the error.** `landing` records where a *reading* was deposited — a dossier, a commit candidate,
a discovery-ledger lead, a queue entry. Landing on a commit candidate **is** the correct pipeline
path; the candidate is what later reaches a claim. A screen that flags 91% of the population is
measuring its own definition.

Per the standing instruction, that cut was **stopped rather than tuned**, because tuning it is the
mass reconciliation. The audit was re-aimed at the *shape* of the two known instances instead.

## 1 · The narrow instrument

Both known instances (`CLAIM 016`'s lithium locator; `CLAIM 039`'s cerebellar locator) have the same
shape: **a locator carrying a neurologically or prognostically load-bearing finding, whose wording
appears nowhere in the canonical text.** So:

- take every locator `proposition` in all 81 manifests;
- keep those matching a high-value term (`cerebell`, `heterozyg`, `+/-`, `EEG`, `burst`, `seizure`,
  `epilep`, `migrat`, `lamina`, `myelin`, `oligodendro`, `GABA`, `chloride`, `excitab`, `Purkinje`,
  `foliation`);
- test whether **any 6-word window** of the proposition occurs in `claim_registry_current.md` or
  `working_model_current.md`.

**Result: 183 propositions carry a high-value term and appear nowhere in canonical text.** Most are
correctly unlanded — method notes, figure attestations, negative checks. The audit's job was to find
the few that are **load-bearing and contradict a claim the model actually relies on**. Four do.

## 2 · The finding: `CLAIM 032`'s tumour caveat is narrower than our own evidence

`CLAIM 032` (VERY HIGH, load-bearing on the gene-therapy dose argument) carries exactly one tumour
qualification:

> *"nei topi eterozigoti è documentato un aumento di tumorigenicità **sotto carcinogeni**."*

**Carcinogen-challenged only.** And its Summary quotes Aldaz asserting haploinsufficiency *"appears
not to be deleterious"* — a sentence whose full form in the source (established earlier in this
batch) continues *"…or **carcinogenic**"*, directly after *"no evidence of **spontaneous** neoplasia
in any tissue examined. This was also the case for … Wwox heterozygous mice."*

🔴 **LEGEND's own manifests contain the contradiction, captured as locators, never landed:**

| PMID | Locator proposition | Snippet, verbatim | Is it in `CLAIM 032`? |
|---|---|---|---|
| **17360458** | *"Adult heterozygotes had more **spontaneous** tumor-bearing animals than wild types."* | *"The number of tumor-bearing animals among Wwox+/− mice was **5-fold higher (P = 0.03)** than in WT mice"* | **NO — and the claim's caveat covers only the challenged case** |
| 17360458 | *"ENU challenge increased lung tumor incidence in heterozygotes."* | *"72% (33/46) of mice developed lung papillary carcinomas, whereas only 36% (15/42) of WT mice did"* | partially — this is the case the caveat covers |
| **17575124** | *"Invasive carcinoma occurred **only** in the heterozygous group in this experiment."* | *"27% (7 of 26) of Wwox+/- mice had invasive SCC in the forestomach … as compared with **none** of the Wwox+/+ mice"* | **NO** |
| **18487609** | *"THE HETEROZYGOTE IS DECLARED PHENOTYPICALLY SILENT … AND TWO THOUSAND WORDS LATER THE SAME PAPER RECORDS A MEASURABLE HETEROZYGOTE PHENOTYPE."* | text: *"Wwox heterozygous (HET) pups were **indistinguishable from wild-type** … at all stages"*; then *"reduced trabecular member connectivity and bone surface area in **both the HET and KO**"*; panel 3B at P15: connectivity density **64 ± 8 (HET) vs 128 ± 10 (WT), −50%**; bone surface **−54%** | **NO** |

**The `17360458` row is the one that matters.** *Spontaneous*, 5-fold, P = 0.03, in a primary — against
a review sentence asserting no spontaneous neoplasia in heterozygotes, which `CLAIM 032` carries and
qualifies only for carcinogen challenge.

**`18487609` is the fourth instance of tonight's recurring pattern**, and the reader who captured it
said so themselves: a heterozygote declared *indistinguishable from wild-type* in the first Results
paragraph, with a **50% deficit** in the panel. It is bone, not brain — it does not speak to
cognition — but it is one more organ in which "heterozygotes are normal" was written next to a
measured heterozygote deficit.

## 3 · The one that does NOT support the thread, preserved as such

`PMID 18674750` carries: *"one copy of the T allele of rs2548861 increases the probability for low
HDL-C by approximately **17%**"* — human, 475 cases and controls, **dominant**.

🔴 **It must not be used.** The reader who captured it defused it in the same manifest, and was
right to: the authors state *"this SNP rs2548861 alone is not a major HDL-C determinant but rather
… a **modifier variant**"*, and *"rs2548861 was **not significantly associated** with HDL-C levels in
this GWAS for lipid traits when an additive model was used."* A dominant effect of a **regulatory
SNP on a lipid trait** is not evidence about **coding haploinsufficiency in neurodevelopment**.
Recorded here so that the next reader who finds this locator does not have to re-derive why it was
left out.

## 4 · What this does and does not establish

**Does:** `CLAIM 032`'s tumour qualification is **narrower than LEGEND's own captured evidence**, and
the gap is specifically the **spontaneous** arm. Three heterozygote phenotypes (two tumour, one bone)
sit in our manifests and in no claim.

**Does not:** none of this is neurological. Tumour incidence and trabecular bone do not measure
cognition or epilepsy, and the endpoint qualifier already proposed for `CLAIM 032` remains the
substantive change. This audit **widens the same crack by one board** — it shows the "not
deleterious" reading was already contradicted inside our own evidence base, in a domain nobody
disputes.

**Method note for the next auditor:** the 183-proposition list is mostly correct silence. The
signal-to-noise was about 4 in 183. A screen like this is worth running **only against a specific
claim under active question** — run generically, it is the mass reconciliation wearing a disguise.
