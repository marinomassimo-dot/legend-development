---
record: ADDENDUM to the Scientist-B first-pass on PMID 32000863
id: PILOT_PMID32000863_ADDENDUM_SCIB_v1
addendum_to: PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_SCIB_v1 (committed 2261a15, unmodified)
actor: scientist-b (NOT ACTIVATED — operator-directed analytical pilot; see the edge-adjudication
  record §0 for the authority determination)
date: 2026-08-25
status: NON-CANONICAL. Mutates nothing.
why_an_addendum_and_not_a_revision: §12 forbids rewriting the first-pass before A and C finish.
  Nothing below edits the v1 pilot. Where this session changed my confidence, it is stated here.
---

# Addendum — re-verification, the eight questions in one place, and where my v1 was not independent

> **Nothing here is medical advice.** Lithium has a narrow therapeutic index; nothing below supports
> its use in any patient.

---

## 1 · Re-verification against the artifacts, this session

My v1 pilot read the paper. This session I re-opened it to check whether v1's figure readings survive
contact with the artifact a second time, at native resolution, by a route that does not consult v1.

**All four declared artifact fingerprints match the manifest exactly:**

| Artifact | sha256 | matches manifest |
|---|---|---|
| `PMID32000863_Cheng2020_PMC.xml` | `792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5` | yes |
| `PMID32000863_Cheng2020_supplementary.pdf` | `0acb771cfe3a4c3644b41c10451504047adb715e69727c1889f72774151f8b7f` | yes |
| `…_assets/40478_2020_883_Fig7_HTML.png` | `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542` | yes |
| `…_assets/40478_2020_883_Fig2_HTML.png` | `9e4648590eec98e148f47c52a151d0bb2c93fa20438151743043fe5e7ae47d05` | yes |

Figure 7 re-read at its native 1946×1627 and at 3× on the densitometry row.

**Result: every figure reading in v1 is confirmed. No correction is owed to the v1 pilot.** The
densitometry, the per-panel significance markers, the arm structure and the N values all reproduce.

---

## 2 · The eight §12 questions, answered against verified locators

| # | Question | Answer | Verified locator |
|---|---|---|---|
| 1 | Does lithium suppression of PTZ-provoked seizures occur only in Wwox-null animals or also in control genotypes? | **Also in both control genotypes.** All three panels of Fig. 7d carry `****`: `+/+` PTZ N=12 vs LiCl N=8; `+/−` N=12 vs N=12; `−/−` N=6 vs N=7 | Fig. 7d, image at native resolution. The Results text names only `−/−`; the caption names only `−/−` |
| 2 | Does the experiment demonstrate a WWOX-specific rescue? | **No.** A suppression significant in wild-type cannot separate *"corrects the WWOX lesion"* from *"raises seizure threshold in any mouse"* | as above |
| 3 | Does it demonstrate that GSK-3β is the molecular target responsible for lithium's effect? | **No.** No selective inhibitor, no `Gsk3b` epistasis, no target-engagement measurement after LiCl. The paper's own Discussion supplies competing routes it does not exclude: *"rescue Wnt-dependent cerebellar midline fusion and neurogenesis deficits early in development [38]"*, *"induce β-catenin-mediated myelin gene expression in mouse Schwann cells and enhance remyelination [47]"* — both lesions this mouse has. Its cited support for the anti-PTZ effect, ref. 10, is *"Bahremand A … Additive anticonvulsant effects of agmatine and lithium chloride on pentylenetetrazole-induced clonic seizure in mice: **involvement of α2-adrenoceptor**"* — ordinary mice, different receptor system | Discussion, final substantive paragraph; reference list entries 10, 38, 47 |
| 4 | What does Fig. 7c establish about total GSK-3β, Ser9 phosphorylation, genotype pattern, statistical support? | **Total GSK-3β: essentially flat** — 2.2·2.4·2.4 (cerebellum), 2.3·2.4·2.6 (hippocampus), 2.2·2.4·2.6 (cortex) across `+/+`·`+/−`·`−/−`. **pSer9: falls sharply in `−/−`** — 2.7·3.1·**1.3**, 3.6·3.5·**2.0**, 3.9·3.8·**2.5** (−52%, −44%, −36%). **Genotype pattern: no dosage gradient** — the heterozygote sits at or above wild-type on the phospho blot in every region. **Statistical support: none.** One lane per genotype per region, no error bars, no test; the caption offers only *"The representative results of four independent experiments are shown"* | Fig. 7c, native pixels, densitometry row re-read at 3× |
| 5 | Does ethosuximide show a genotype-restricted pattern distinct from lithium? | **Yes, and it is the inversion of the paper's argument.** Fig. 7b marks PTZ vs PTZ+ETS **`n.s.` in `+/+` and `+/−`** and **`***` in `−/−`**. The comparator has the specificity; the drug the paper favours does not. The text states this for ethosuximide — *"although ethosuximide pretreatment had no effects on the behavior changes in Wwox+/+ and Wwox+/− mice"* — and **never states the converse for lithium** | Fig. 7b panels + Results, verbatim |
| 6 | What causal edge does the paper license between Wwox loss, GSK-3β state and seizure phenotype? | **Wwox loss → reduced GSK-3β Ser9 phosphorylation** at P20 in three regions: an **observation**, in one representative blot, untested. **GSK-3β state → seizure**: not licensed. The pharmacology is non-selective and non-specific to genotype; abundance and activity are dissociable and only phosphorylation moved. The strongest licensed proposition about lithium is: *systemic lithium pretreatment raises the threshold for PTZ-provoked seizure in this paradigm, irrespective of Wwox genotype* | §5, E-016-035 in the edge record |
| 7 | Which propositions belong in the mechanism graph, the pharmacological observation layer, the hypothesis layer? | **Mechanism graph:** none from this paper alone. The residue-level WWOX ⊣ GSK3β mechanism belongs to PAPER 056 and is *cited* here, not measured — ref. 65 is Wang 2012. **Pharmacological observation layer:** the PTZ paradigm results, including the wild-type panels, with their arm structure and N. **Hypothesis layer:** *"GSK-3β mediates the Wwox-null seizure hypersusceptibility"*, which is the paper's title claim and its least-supported one | — |
| 8 | Are there figure/text discrepancies material to the graph? | **Three.** (a) The caption and Results name only `−/−` for a panel whose other two genotypes are marked as significantly. Incomplete, not false — but it is the incompleteness the downstream reading inherited. (b) Panel d carries `****`, a marker the caption never defines — it defines only `n.s.` and `*** P < 0.001`. (c) **The canonical claim cites the wrong panel**: `claim_registry_current.md:300` attributes the lithium result to `Fig. 7b`, which is the ethosuximide panel | §8 of the edge record |

**Design asymmetry, recorded because it decides how much (1) and (5) can carry.** Panel b has three
arms including a saline Control (N=4/5/4); **panel d has two arms and no Control**, and no LiCl-alone
arm. And the wild-type lithium effect reached `****` at N=12 vs 8, while the wild-type ethosuximide
comparison returned `n.s.` at N=20 vs 16 — the ETS null result is **not** attributable to a smaller
cohort.

🔴 **The statistical objection cuts both ways, and I record it against my own preferred reading.**
There is **no genotype × treatment interaction test anywhere in the paper**. Every marker is a
within-genotype pairwise comparison. So "significant in `−/−`, `n.s.` in `+/+`" does not by itself
establish that ethosuximide's effect *differs* between genotypes, any more than three separate
`****` establish that lithium's does not. Answer 5 is a statement about *the pattern of tests the
paper reports*, not about a demonstrated interaction — and the same discipline that forbids the
paper's genotype-specific reading of lithium forbids a strong genotype-specific reading of
ethosuximide.

---

## 3 · Where my v1 was not independent, stated plainly

My v1 frontmatter declares independence from Scientist A and from the Plan crosswalk. That much held.
It does **not** declare, because I had not found it, that **the repository already contained the
answer**.

`disease-models/wwox/analysis/locator_contract_live_test.md:375–395`, tracked, dated 2026-08-04:

> *"**Figure 7d has three panels — +/+, +/− and −/− — and lithium suppresses seizures in all
> three.**"*
> *"Ethosuximide, the comparator the paper says lithium beats, **is** genotype-specific: Figure 7b
> marks it non-significant in +/+ and +/− and significant only in −/−."*
> *"**'Elevated' is the wrong word.** Figure 7c prints its densitometry: **total GSK3β is flat** …
> GSK3β is **dis-inhibited, not more abundant.**"*

Plus the premise tag on *"lithium is a GSK3β inhibitor"*, the alternative mechanisms from the
Discussion, and a `REVIVAL_TRIGGER` naming a selective inhibitor or `Gsk3b` epistasis. And CLAIM 016's
own `Evidence boundary`, propagated 2026-08-10 by `BATCH_20260810_005`, carries the same conclusion
in the canonical registry.

**Consequences, stated in order of who they bind.**

1. **Mine.** My v1 pilot does not cite `locator_contract_live_test.md`. That is a provenance gap in
   v1 and it is mine. A first-pass that re-derives a recorded finding should say the finding was
   recorded; mine presents it as a bottom line.
2. **The exercise's.** No Scientist reading PMID 32000863 *through this repository* can be
   independent of the repository's conclusion about it. §12 therefore measures whether three actors
   can re-derive a recorded answer from the primary artifact — a real and worthwhile thing to
   measure, and **not the thing the prompt says it measures**. Any Mirror audit of independence
   should test against the tracked tree, not only against actor-to-actor contact.
3. **Nobody's, yet.** The finding being pre-recorded does not make it right, and re-derivation from
   the artifact is how it stops being taken on trust. It survived mine.

---

## 4 · What this session adds that the pre-existing analysis does not have

Stated as a delta so a reviewer need not diff two long documents.

1. **The canonical claim cites the wrong panel.** `locator_contract_live_test.md` has `7d` for
   lithium and `7b` for ethosuximide, both correct. `claim_registry_current.md:300` attributes the
   lithium result to `Fig. 7b`. Nobody reconciled them, and the wrong one is the canonical one. It is
   also the **only figure-panel citation of any kind in the entire claim registry**.
   ⚠️ **Not a `7b → 7d` swap:** the parenthetical is compound and its second clause is genuinely
   about `7b`. A blind substitution breaks the half that is right.
2. **The propagation of the unsupported wording is countable.** *(Phase II correction: "unsupported",
   not "disproven" — the abundance direction really is upward by 9–18% on unstatisticized lanes.
   Both peers objected to my stronger word and both are right.)* At HEAD `8612baa`, over 581 tracked
   files excluding `reviews/scientist-b/`, **14** assert *"GSK3β is elevated"*; **1** of the 14 also
   states the correction. Among the fourteen: the canonical registry; `dismech_export_spec.md` where
   it is `016-a` typed `DATO`; four blind-review sheets that put it before reviewers as a reference
   proposition; and `therapy_levers.md` A2. Meanwhile `working_model_current.md:164` — the mirror of
   CLAIM 016 — is **already corrected**. Mirror and claim disagree.
3. **The readout mismatch nobody had joined up.** CLAIM 035's own `Clinical meaning` warns that
   *"qualunque studio WWOX-DEE che usi pS9 come readout di attività GSK3β produrrà un falso
   negativo"*. CLAIM 016's principal molecular evidence **is** a pS9 western in a WWOX-deficient
   setting. The warning was written, exported as assertion `035-f`, blinded and reviewed — and never
   turned around and pointed at the claim beside it in the same document.
4. **A wrong-reason success for Mirror.** `therapy_levers.md` A2 calls the lithium lever
   *"genotype-agnostic"* — the right word — reached by reasoning *"acts downstream of WWOX loss"*
   rather than from the wild-type panel, and delivered alongside *"abolishes seizures"* (the panel
   shows suppression, not abolition) and a mechanism attribution the experiment does not establish.

---

## 5 · What did not change

- The v1 pilot's bottom line stands, re-verified at the artifact: **the lithium experiment does not
  demonstrate a WWOX-specific rescue and does not identify GSK-3β as the molecule through which
  lithium acts.**
- The **abundance datum** stands as an observation of *phosphorylation*, not of abundance.
- The **residue-level mechanism of PAPER 056** stands, and is untouched by any of this.
- CLAIM 016's status stays `in observation`. Nothing here argues for promotion or reversal.
- **No canonical mutation. §16 observed in full.**
