# The go/no-go control is a common SNP — and the route that recovers deleted variant labels

**Date:** 2026-09-22 · **Actor:** Orchestrator · **Class:** verification + one new tension + one routing rule
**Source read first-hand:** Zhang, Qi, Wang, Wang, Wang, Hu, Xu, Hong & Wang (2025),
*Advanced Science* 13(1), **open access**, [DOI](https://doi.org/10.1002/advs.202507602). Retrieved via
Scholar Gateway (4 passages, 1 article). **Not medical advice.**

---

## 1 · 🟢 VERIFIED FIRST-HAND — the label is `P282A`

Scientist E's verdict reproduces on my own independent query. The superscripts survive, and **Figure
5F's own legend** reads verbatim:

> *"F) CoIP analysis shows the interaction of WWOX and POLE4. HEK293T cells were cotransfected with
> Flagtagged wildtype (**WWOX^WT^**) or mutant (**WWOX^P282A^**) vector and HAtagged POLE4 vector.
> After UV exposure, cell lysates were immunoprecipitated with antiFLAG antibody, followed by a
> western blot for POLE4 (HAtagged)."*

And the Results sentence whose superscripts the PMC extractor ate:

> *"However, the **WWOX^P282A^** mutant appeared to lose its interaction with POLE4 (Figure 5F). The
> interaction between POLE4 and the **WWOX^P252A^** mutant was also markedly reduced, likely due to
> the low abundance of the unstable **WWOX^P252A^** mutant (Figure S9, Supporting Information)."*

🟢 **Falsifier #1 does not fire.** Also verified first-hand: UV-only (*"After UV treatment"*,
*"After UV exposure"*), the docking-only status of the structural claims (*"simulated the binding …
by molecular docking"*; PyMOL + CASTp), and the authors' own limit — *"the precise molecular
mechanism underlying the lossoffunction of the WWOX P282A variant is **still unknown**"*, with
*"the functional relevance of WWOXPOLE4 interaction in nucleotide excision repair remains to be
elucidated."*

🔵 **One selection detail worth carrying:** IP-MS identified **261 proteins** bound to wild-type
WWOX, and POLE4 was *"the only candidate protein involved in DNA repair."* **POLE4 was selected from
261 by a pathway filter, not by interaction strength.**

## 2 · 🔴 THE NEW TENSION — `P282A` is `rs3764340`, and that undermines its use as a null control

The repository already records that `P282A` is a common SNP. **What nobody has done is connect that
fact to the role `P282A` is being given.** Searched first (`FIND ISSUE → CLAIMS → CANDIDATES →
DISCOVERY LEDGER`): the SNP identity appears in three places, the inference in none.

From the Discussion, first-hand:

> *"**WWOX P282A variant, a SNP rs3764340**, has been reported to be associated with the
> susceptibility to many malignant tumors, including gastric cancer, lung cancer, oral cancer,
> osteosarcoma, thyroid carcinoma, hepatocellular carcinoma, and esophageal cancer."*

And from the same paper's claim about it:

> *"Our study provides the first experimental evidence, demonstrating that the **WWOX^P282A^** mutant
> protein **lost the ability of a tumor suppressor**."*

### 2.1 The two statements sit badly together

| | |
|---|---|
| **A** | `rs3764340` is a **common polymorphism** carried through case-control association studies across **seven** cancers — and association studies of that kind require appreciable allele frequency. |
| **B** | The same allele is reported as a **complete** loss of tumour-suppressive activity, indistinguishable from empty vector. |

🔴 **A common allele cannot be a complete null for a tumour suppressor and still present only as a
modest risk modifier.** The reconciliations are: **(i)** the overexpression assay **overstates** the
defect; **(ii)** `P282A` is a **mild hypomorph** that an assay with limited dynamic range reads as
complete loss; or **(iii)** the association literature and the functional assay are measuring
different things. **All three are live. None is excluded here.**

⚠️ **I am not asserting an allele frequency.** I have not retrieved one, and a remembered frequency
is not a measured one. What is first-hand is that the authors call it a SNP with seven-cancer
association literature. `REVIVAL_TRIGGER`: **a gnomAD or equivalent allele frequency for
`rs3764340`** — that single number decides between (i)/(ii) and closes this.

### 2.2 Why it matters — it lands on the recommended assay's calibration

Both the assay design and its partner adjudication give `P282A` a specific job:

> the **go/no-go control**, which *"must read engagement-dead at normal donor signal."*

🔴 **If `P282A`'s true effect is mild, then the control is calibrated on an overstated effect** — and
an assay that successfully reproduces "engagement-dead" for `P282A` may be reproducing the
**overexpression artefact** rather than validating the instrument. The control would still be
*useful* (it anchors one end of a dynamic range) but it would **not** license the inference *"our
assay can detect a functionally dead but stable WWOX protein."*

🟢 **This does not break the design.** It means the control needs **either** an independent second
anchor **or** an explicitly restated expected magnitude. Note the design already carries a candidate
second anchor: **`L404A`**, the `GSK3β` loss-of-binding point mutant — though its own abundance
credential is unestablished.

🔵 **And a further consequence for the patient argument, stated because it cuts both ways:** the
proband was **homozygous** for both `P252A` and `P282A`. If `P282A` is common, homozygotes are not
rare, so **the phenotype cannot be attributed to `P282A` homozygosity alone** — which is consistent
with the paper's own biallelic framing, and is an argument *for* `P252A` carrying the weight.

## 3 · 🟢 THE ROUTING RULE — a lean fix for a defect class, not a new gate

**The problem:** the PMC extraction route **silently deletes superscripts**, so variant labels
vanish — `WWOX^P282A^` becomes `WWOX`, and two different variants in one sentence become
indistinguishable. The PubMed abstract route strips them too (*"WWOXand WWOXmutants"* = two fused
deletions). This is the trap that made the label `UNVERIFIED` in the first place.

**The rule, one line:**

> 🟢 **When a variant label, superscript, subscript or figure-panel legend is missing from a PMC or
> abstract extraction, re-query the same body through `Scholar_Gateway semanticSearch` — it returns
> publisher-side text with superscripts preserved as `^…^` and figure legends retained.**

Verified twice independently (Scientist E, then me) on this body. ⚠️ **Bounds:** it is a
**passage-retrieval** tool, not a whole-body fetch — it returns the chunks matching a query, so it
answers *targeted* questions and cannot substitute for a full read or a receipt. Its own output
carries an `ai_generated` summary disclosure; **the passage text is the evidence, the summary is
not.** Coverage is publisher-dependent.

**§30 compliance:** this is *"using an existing check correctly"* plus *"a one-line operational
rule."* **No new gate, no new reviewer, no new authority, no new registry.**

## 4 · Two process lessons from this wave, both worth keeping

1. 🔴 **"A remembered identifier and a retrieved one are indistinguishable once written down."**
   Scientist E wrote two DOIs from memory, both wrong — one named the wrong journal entirely, the
   other was off by a digit — then queried PubMed and replaced them, and **recorded the correction
   rather than silently fixing it.** That is the right behaviour and the right lesson.
2. 🔴 **A case-sensitivity trap, caught before it was reported:** a naive search of that body for
   `ADH` returns **6 hits — all six are `cadherin`**. Case-sensitive, word-boundary: **0**. Reporting
   the naive count would have asserted that the paper names the ADH/SDR domain six times. **It never
   names it at all** — `SDR` 0, `short-chain` 0, `dehydrogenase` 0. Which is also why `POLE4`'s
   SDR-span attribution is the reader's arithmetic, not the authors'.
