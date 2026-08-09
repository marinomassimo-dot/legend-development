# Verbatim locators — PMID 34747138 (Repudi et al., *EMBO Mol Med* 2021)

*Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes* — the source of `CLAIM 004`
(`consolidated baseline`). Captured while the document was open, 2026-08-09.

## Artifact

| Role | Path | SHA-256 |
|---|---|---|
| `article_text` | `files/fulltext/PMID34747138_Repudi2021_PMC.xml` | `7da156e82cb7014f837d8c29374d888cb99ecc3268d1c383af2c3d0832b988bb` |

JATS XML — an accepted text surface for `deepdive_manifest._artifact_text`, so **no derived
`.txt` is needed and none is declared**. Quotes below are verified against the XML itself.

## Text-surface sentinel — PASSED, and structurally inapplicable

| Criterion | Threshold | This document |
|---|---|---|
| comparison characters in a paper with statistics | zero → `SUSPECT` | **12** well-formed `&lt;` entities → pass |
| `P\s*[45]\s*0?\.\d+` | any hit → `SUSPECT` | **0** → pass |
| C0 control characters outside tab/newline | any hit → `SUSPECT` | **0** → pass |

**XML/HTML PMC was chosen over the PDF deliberately, and this is now policy rather than
convenience.** The 2026-08-09 defect is a disagreement between a PDF's *rendered page* and its
*text layer*. Structured XML has no rendered page and no text layer to diverge from it — the
characters are the document. It is the one surface on which that failure cannot arise, so it
is preferred whenever it exists.

The sentinel is run anyway, because "cannot arise" is a structural argument and structural
arguments are exactly the kind of premise this repository has been burned by. Cost: one grep.

---

## L1 — transduction efficiency is 60–70%, not complete

> "The percentage of NeuN and WWOX double‐positive cells was calculated and found to range
> between 60 and 70% (Figs 1E and 2G)."

`surface: body` · Results, *Specific neuronal WWOX expression upon use of AAV9-SynI-WWOX vectors*

Directly relevant to `CLAIM 032` (*haploinsufficiency is not deleterious; the therapeutic
threshold sits well below full restoration*), which is currently `in observation` and rests on
a `BATCH_20260710_A synthesis` with **no primary source**. Here a measured 60–70% neuronal
transduction produces survival, growth, glucose, seizure and myelination rescue. This is a
primary, quantified anchor for a claim that has none.

## L2 — expression persists to nine months

> "Furthermore, WWOX protein expression was lasting as it was detected in 9 months
> post‐injection (Appendix Fig S2A)."

`surface: body` · same section

## L3 — no peripheral expression, tested organ by organ

> "we also tested expression of the transgene in peripheral tissues, including liver, pancreas,
> kidney, testis, and ovary of juvenile and aged mice. As presented in Appendix Fig S2B and C,
> no WWOX expression was detected in Wwox‐null tissues in P17 and 9‐month‐old rescued mice."

`surface: body` · Results

## L4 — 🔴 neuron-only restoration corrects **peripheral** phenotypes

> "Remarkably, WWOX single ICV injection improved motor coordination in rescued mice as
> presented by hindlimb clasping test (Appendix Fig S3). Furthermore, the rescued mice were
> active and both males and females were fertile. Moreover, since Wwox‐null mice were previously
> shown to lack testicular Leydig cells (Aqeilan et al, 2009), we next determined how WWOX
> neuronal restoration affected this phenotype and found intact Leydig cells in P17
> AAV9‐hSynI‐WWOX‐treated mice (Appendix Fig S4A)."

and, on glucose:

> "Wwox‐null and AAV9‐hSynI‐EGFP‐injected mice were hypoglycemic from the second week until they
> succumbed … while AAV9‐hSynI‐mWwox‐ or AAV9‐hSynI‐hWWOX‐injected mice had normal blood glucose
> levels when compared to the wild‐type mice"

`surface: body` · Results

**Why this matters, and it is not small.** Combine L3 and L4: the vector demonstrably does
**not** express in liver, pancreas, kidney, testis or ovary, yet restoring WWOX **in neurons
alone** normalises blood glucose, restores fertility and Leydig cells, and gives cortical bone
comparable to wild-type. The peripheral phenotypes of the Wwox-null mouse are therefore
substantially **downstream of the CNS**, not tissue-autonomous.

This bears directly on `CLAIM 036` — *"a systemic Wwox-null mouse at P18 is metabolically
decompensated, so any brain phenotype in that window carries a quantified systemic
confounder"* (from `PAPER 057`, Ludes-Meyers 2009). It does not refute that claim: the
decompensation is measured and real. It **qualifies its causal direction**. If correcting only
neurons normalises glucose, then the metabolic crisis is not an independent confounder sitting
beside the brain phenotype — it is, at least in part, a consequence of it. A confounder that is
downstream of the exposure is a mediator, not a confounder, and the two license opposite
reasoning. `CLAIM 036` should carry this qualification.

## L5 — the treated-versus-WT comparison IS reported here

> "No significant difference in average firing rate was observed between the KO+AAV9‐mWwox or
> KO+AAV9‐hWWOX and the WT pups (Fig 3B)."

`surface: body` · Results

Worth recording as a contrast with PMID 42397075 (2026), where "similar to WT" is asserted for
the organoid rescue while Fig. 6A(ii) shows **no WT-versus-treated bracket at all**. The same
group states the comparison explicitly when it has made it. That strengthens, rather than
weakens, the 2026 reading: the omission there is informative.

## L6 — murine and human transgene are interchangeable in this model

> "No difference was noted when using the murine or human WWOX vectors."

`surface: body` · Results

## L7 — declared limit: no adult KO comparator exists

> "Since KO mice died within less than 4 weeks, we could not perform in vivo recordings in adult
> KO mice. We therefore performed cell attached in vivo recordings only in adult WT and
> KO+AAV9‐mWwox mice (Fig 3C)."

`surface: body` · Results

Honest and explicit. The adult-timepoint claim is therefore WT-versus-rescued only, with no
untreated arm — by necessity, not by omission.

## L8 — myelination rescue runs through OPC differentiation

> "AAV9‐mediated WWOX expression in neurons increased the differentiation of OPCs to matured
> oligodendrocytes as assessed by immunostaining with CC1 … and anti‐PDGFRα … Quantification of
> CC1 and OPCs in the corpus callosum showed significantly increased number of matured
> oligodendrocytes in rescued mice compared to the KO mice injected with control virus at P17"

`surface: body` · Results

This is the therapeutic mirror of `CLAIM 003` (non-cell-autonomous hypomyelination, PMID
33914858): the same axis, corrected.

## L9 — sample sizes are uniformly small

Throughout: `n = 3` per genotype for immunofluorescence quantification, GFAP/Iba1 counts,
myelination and OPC counts; `n = 4` per group for body weight; electrophysiology averages 30–60
neurons drawn from `n = 3` animals. Survival curves are the largest cohorts (n = 18 and n = 16
treated). Not a defect — but the effect sizes are large and the animal-level n is 3, so the
claim class is *demonstrated in a small cohort*, not *precisely estimated*.

---

## Coverage — reading state

| Section | State |
|---|---|
| abstract, "The paper explained" | read |
| introduction | read |
| results | read |
| figures | **captions_only** — figure captions read in full; the images themselves not opened |
| tables | not_present |
| discussion | **not_read** |
| methods | **not_read** (present in the XML, section list mapped) |
| supplementary (Appendix Figs S1–S6) | **not_read** — heavily load-bearing: L2, L3, L4 all cite Appendix figures |
| references | not enumerated |

**Evidence depth: `partial_fulltext_read`.** Not complete, and no receipt claiming completeness
may be issued. Reading debt for PMID 34747138 stays open.

**Note on where the evidence sits.** L3 and L4 — the strongest finding in this reading — rest on
`Appendix Fig S2B–C`, `S3` and `S4A`, none of which has been opened. The running text states
their result. That is exactly the configuration in which this repository has twice been burned
(Wang 2012's caption, the 42397075 Fig. 6 brackets), so the finding is recorded as
`PREMISE: INFERENZA` pending inspection of those panels, not as `DATO`.
