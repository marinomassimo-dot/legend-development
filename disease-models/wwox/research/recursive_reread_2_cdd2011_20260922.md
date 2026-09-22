# RECURSIVE RE-READ #2 — PMID 22193544 under the insolubility question

**Directive:** recursive re-read, second deliberate test. **Date:** 2026-09-22 · **Actor:** Orchestrator.
**Test:** `OLD PAPER + NEW QUESTION → NEW SCIENCE`.
**Scoring rule, fixed in advance:** recovering a fact already held in this repository scores
`NO NEW INFORMATION`, however useful the fact is.

---

## §1 · Paper, and why it is newly relevant

**PMID 22193544** / PMCID `PMC3354054` / [DOI](https://doi.org/10.1038/cdd.2011.188) — *Cell Death
and Differentiation* 2011. SH-SY5Y under retinoic-acid differentiation, **recombinant proteins**,
endogenous co-IP from **mouse brain extract**, engineered `L404A` / `L311A` point mutants and
`Δ286` / `Δ389` truncations, GST pull-down domain mapping. `complete_fulltext_read`, receipts
`FTR-20260726-22193544-01/02/03`, nine verbatim locators in `deepdive_manifests/PMID22193544.json`.

It qualifies on all four grounds:
1. **Completely read**, eight weeks ago, by a different actor.
2. **The first read had a different purpose** — engagement-partner mapping: which domain binds
   `GSK3β`/Tau, at residue resolution.
3. **It is the only paper in this corpus that made and recovered WWOX protein fragments**, which
   is what makes it newly relevant.
4. It is not a paper this session has been working on.

---

## §2 · OLD QUESTION → NEW QUESTION

**OLD QUESTION (2026-07-26):** *Which WWOX domain and which residues mediate the interaction with
`GSK3β` and Tau, and does an SDR lesion abolish it?*

**NEW QUESTION (today, written before opening the paper):**

> **Can the WWOX SDR domain be expressed and recovered in SOLUBLE form — and what does this
> paper's own handling of its recombinant constructs say about WWOX solubility, the variable on
> which the entire `Q230P` mechanism question now turns, and which 0 of 12 published WWOX
> abundance measurements have ever examined?**

Why the question is new and not merely adjacent: today's abundance census established that **no
published WWOX missense measurement has ever examined an insoluble fraction**, so `H3`
(misfolding/insolubility) is undischarged for `Q230P`. A paper that **built, expressed and
recovered isolated WWOX fragments** must contain, in its Methods, the one class of information
nobody has looked for: an expression system, a solubilisation protocol, and — if a fragment
carrying the SDR was recovered and bound anything — **evidence that the SDR can fold well enough
to be recovered at all.**

Four sub-questions, fixed now:
- **Q-A · Conditions.** What expression system, lysis and solubilisation conditions were used for
  the recombinant proteins? Is any detergent, chaotrope or denaturant named? Is any pellet kept?
- **Q-B · Was an SDR-containing fragment recovered, and did it bind?** A fragment that pulls down a
  partner is at minimum not wholly aggregated. ⚠️ Recovery in a pull-down is **not** proof of a
  native fold, and I commit now to not overreading it.
- **Q-C · Is there an unremarked abundance observation?** Do `L404A`, `L311A`, `Δ286` or `Δ389`
  differ from wild type in expression level or recovery — an SDR-region abundance datum nobody
  has counted?
- **Q-D · Aggregation vocabulary.** Do `insoluble`, `aggregate`, `inclusion body`, `urea`,
  `denatur`, `pellet` appear at all?

---

## §3 · Baseline — enumerated, not guessed

🟢 **`enumerate_baseline_before_scoring` run deliberately for the first time**, after failing twice
today by reconstruction. Every file in the repository bearing the string `22193544` was listed:
**over 100 files**, including `deepdive_manifests/PMID22193544.json`,
`session_evaluations/2026-07-26_PMID22193544.md`, four commit candidates, the claim registry, the
discovery and dismissal ledgers, and today's `wwox_engagement_partner_adjudication_20260922.md` and
`wwox_sdr_function_per_molecule_census_20260921.md`. 🔴 **There is no `fulltext_dossiers/` entry for
this PMID** — the manifest is the whole reading record. Had I guessed filenames I would have
concluded the opposite, as I did this morning on a different PMID.

**Measured in the manifest** (the reading record of the complete read):

| token | count |
|---|---|
| `GST` | 3 — all method-level (*"GST purification and domain mapping"*, *"GST pull-down"*) |
| `express` | 5 | 
| `lysis` | 1 |
| `solub` · `insolub` · `buffer` · `triton` · `np-40` · `nonidet` · `urea` · `denatur` · `pellet` · `aggregat` · `inclusion` · `recombinant` | 🔴 **0 each** |

**So the first read recorded GST pull-down as a *technique* and never as *evidence about WWOX
solubility*.** That is the gap this re-read probes, and it is a real gap rather than a filing one.

Also already held, and therefore **not** scoreable as new: `L404A` abolishes `GSK3β` binding while
`L311A` does not; a **GST-fused SDR fragment did not bind HA-Brca1** (from `PMID 27869163`, a
different paper); region 388–407 is load-bearing in `TX-003` and `proteostasis_rationale.md`; and
this repository's standing correction that *no purified, folded, biophysically characterised WWOX
SDR exists, though heterologous expression has been reported at least twice* (`PMID 21476439`).

---

## §4 · PREDICTIONS, fixed before reading

| # | Prediction | Falsifier |
|---|---|---|
| **P1** | Recombinant proteins are bacterial GST fusions and the Methods name a **mild** lysis buffer with **no** chaotrope and **no** pellet analysis — the same 12/12 pattern as the abundance census | any chaotrope, or any kept pellet |
| **P2** | An **SDR-containing** fragment WAS expressed and recovered, and it bound something | no SDR-containing fragment was made, or none bound |
| **P3** | **No** expression-level or recovery comparison between wild type and the point mutants is reported — they are treated as equivalent without measurement | any such comparison |
| **P4** | `insoluble`, `aggregate`, `inclusion body`, `urea`, `denatur` are **absent** from the body | any occurs |
| **P5** | There is **no** statement anywhere about whether an isolated SDR fragment is folded | any such statement |

**EXPECTED NEW INFORMATION, stated before reading so it can be scored honestly:** I expect a
`NEW DETAIL` — a named lysis buffer and a confirmed SDR-fragment recovery. I expect **not** to find
an abundance comparison (`P3`) and **not** to find aggregation vocabulary (`P4`). If `P3` or `P4`
is refuted, that is `NEW CONNECTION` or better, because it would mean an insolubility datum for an
SDR-domain lesion has been sitting in a completely-read paper in this corpus.

**P1, P3, P4 and P5 are predictions of absence.** In this corpus an absence is assertable only
after a READ, never from a query returning zero — eight distinct failure modes are established.
Any surviving negative carries `PREMISE: METHODS_INVISIBLE` bounded to the served surface.

---

## §5 · Re-read record

**Route:** `mcp__PubMed__get_full_text_article`, `PMC3354054`, 2026-09-22. According to PubMed,
[DOI](https://doi.org/10.1038/cdd.2011.188). Body, Discussion and full Materials and Methods
returned; figure panels not opened.

### §5.1 · Predictions, scored

| # | Outcome | Evidence |
|---|---|---|
| **P1** | 🔴 **REFUTED — and in a direction I did not model** | Not "a mild buffer with no pellet". Three different lysis regimes, and the informative one is **missing**: see `F1`–`F3` |
| **P2** | 🟢 **SUPPORTED** | *"various WWOX functional domains, ww1 (1–60 a.a.), ww2 (40–110 a.a.), ww (1–110 a.a.) and **ADH (110–414 a.a.)**, were expressed as glutathione-transferase (GST) fusions in [E. coli] and **affinity-purified on glutathione beads**"*; *"an intense anti-GSK3β band was bound by the full-length WWOX and **ADH-domain affinity matrix** (lanes 6 and 7), but not by GST alone (lane 2) or the other WWOX domains (lanes 3–5)"* |
| **P3** | 🟢 **SUPPORTED** — no expression-level or recovery comparison between wild type and mutants anywhere | — |
| **P4** | 🟢 **SUPPORTED** — `insoluble`, `aggregate`, `inclusion body`, `urea` do not appear | bounded to the served surface |
| **P5** | 🟡 **PARTIALLY REFUTED** | No statement about the isolated ADH fragment's fold — but an explicit **folding claim for full-length `L404A`** exists, and the authors state *"**As the structure of WWOX is unknown**, the GOR IV Secondary Structure Prediction Method was used"* |

### §5.2 · What is genuinely new

**🔴 F1 — a buffer named `RIPA` is not necessarily RIPA, and today's census classified by name.**

> *"lysed in ice-cold **RIPA buffer** (100 mM HEPES pH 7.4, 150 mM NaCl, 2 mM EDTA, **0.5% Tween 20,
> 0.1% Triton X-100**, 1 mM DTT, 50 µg/ml AEBSF, 10 µg/ml leupeptin, 10 µg/ml aprotinin, 5 mM NaF
> and 1 mM Na₃VO₄)."*

RIPA is defined by **SDS and sodium deoxycholate**. This buffer has **neither**. It is a mild,
non-ionic Tween/Triton buffer **wearing the name of a stringent one** — and Tween 20 at 0.5 % is
gentler still than the Triton it is paired with.

🔴 **Consequence for work done earlier today.** `wwox_missense_abundance_lysis_census_20260922.md`
classifies rows partly by the buffer's **name**, and places at least one row in a stringent class on
that basis. **A name is not a composition.** Every row of that census whose buffer is recorded by
name rather than by recipe must be re-graded to `COMPOSITION UNVERIFIED`, and the census's own
headline — that 0 of 12 rows can separate degradation from insolubility — is **strengthened**, not
weakened: a row that looked stringent may not be. The string `0.5% Tween 20, 0.1% Triton` occurs
**zero** times in this repository.

**🔴 F2 — the GST pull-down Methods contain no lysis step at all.**

> *"For GST pull-down assays, GST or GST–WWOX proteins **expressed in BL21 (DE3) were adsorbed to
> glutathione-agarose beads** (Sigma) for 1 h after three washes with PBS."*

Between *"expressed in BL21 (DE3)"* and *"adsorbed to beads"* there is **no sonication, no
lysozyme, no French press, no lysis buffer and no clarifying spin**. The single step that would say
whether the SDR-containing construct was recovered from the **soluble** fraction or from washed
inclusion bodies is **absent from the Methods**. `PREMISE: METHODS_INVISIBLE` — and it is invisible
on precisely the axis this re-read was built to probe.

**🔴 F3 — the western lysis is direct-to-SDS, and the spin is unspecified.**

> *"Cells were disrupted in **2X sample buffer** (0.1 M Tris-HCl pH 6.8, **4% SDS**, 20% glycerol,
> 2% β-mercaptoethanol), **boiled for 10 min, centrifuged**, placed on ice…"*

Two consequences, opposite in sign:
- 🟢 **Favourable.** 4 % SDS plus 10 minutes at 100 °C is a *maximally* denaturing whole-cell
  extraction. There is no mild step, so there is no soluble/insoluble split — a band seen or not
  seen on **this** paper's blots is far less likely to be a solubility artefact than the mild-buffer
  rows of today's census.
- 🔴 **Unfavourable.** *"centrifuged"* carries **no g-force, no duration, and no statement of which
  fraction was loaded.** Even a fully denaturing lysate can lose material to a pellet if the spin is
  hard enough. The step is named and unquantified — the same defect class as the census's 0/12.

**🟡 F4 — what the ADH construct does and does not license.** The `ADH (110–414)` construct — which
**contains residue 230** — was expressed in *E. coli*, affinity-purified, and retained a **specific**
interaction while three other fragments and GST alone did not. That is a real internal specificity
control and it is a **third** heterologous WWOX expression, the only one with purification plus a
functional readout on the purified material.

🔴 **But the binding determinant is `L404`, inside region 388–407, and `Δ389` abolishes binding.**
That is a **linear motif near the construct's C-terminus**, and a linear motif can be presented by a
poorly folded or GST-solubilised polypeptide. **So this does NOT show that the SDR core — where
`Q230` sits — is folded.** It shows the construct can be made and recovered, and that one terminal
motif is presented. Drawing that boundary is the contribution; crossing it would repeat exactly the
overreach this repository corrected earlier in the session.

### §5.3 · Scored zero — already held, and I nearly claimed one of them

- **The c-Jun folding control for `L404A`** (*"C-jun was immunoprecipitated by either WT or mutant
  WWOX–GFP, indicating that WWOX L404A is folded correctly"*). 🔴 **Already held, in three places** —
  `full_text_queue_current.md:501` (which also records that a **single-partner** control is weak),
  the manifest, and the registry note for PAPER 053's neighbour. **`NO NEW INFORMATION`.** I had it
  marked as the headline find of this re-read until I checked.
- **The `ADH (110–414)` construct boundaries** — already verbatim in
  `CC-20260922-EXON7-NATURAL-EXPERIMENT-01` and `CC-20260922-SPLICE-ARM-01`. **`NO NEW INFORMATION`.**
- **`GOR IV` threaded onto `1O9U`, and its reduced independence** — already in the discovery ledger
  twice and in the manifest. **`NO NEW INFORMATION`.**
- The Supplementary Figure A defect, the irreproducible kinase-assay conditions, the millimolar
  `WWOXtide` — all already held. **`NO NEW INFORMATION`.**

### §5.4 · 🔴 The method defect, and it is the second-order version of this morning's

This morning I failed by building a baseline from **guessed filenames**. Today I fixed that: §3
enumerated **every** file bearing the identifier, by listing. **And I then measured only one of
them — the manifest — and wrote the baseline from it.**

> **Enumeration without reading is not a baseline.** The manifest held 9 locators and zero
> solubility tokens, so it looked like a clean gap. The **registry note and the queue entry** held
> the c-Jun control, its weakness, the construct boundaries and the `GOR IV` provenance — four facts
> that would have been scored as discoveries.

The enumeration is what saved it, but only because I re-grepped **after** the re-read, not because
the baseline was right. `enumerate_baseline_before_scoring` has now been **observed to fail three
times in one day, in three different forms**, and has still never been executed correctly
end-to-end. Its correct form has two steps, not one: **list every file bearing the identifier, then
grep the target concepts across all of them** — not across the one that looks canonical.

---

## §6 · Classification

### Verdict: **`NEW CONNECTION`**

Earned by **F1 alone**: a buffer's *name* is not its *composition*, and a census written six hours
earlier classifies partly by name. That changes how an existing result must be read, which is the
definition of a connection rather than a detail. `F2` and `F3` are `NEW DETAIL` — real, unrecorded,
and both on the axis the question targeted, but neither changes a conclusion on its own.

**Not `EXPERIMENT-CHANGING INSIGHT`, and the reason is the pre-committed rule.** The thing I
expected to be experiment-changing — a published, in-gene, orthogonal-partner folding control for
an SDR point mutant, which is exactly the "ruler" that `q230p_direct_discriminator_20260922.md`
designs from scratch — **is already in this repository, together with the objection that one
partner is not enough.** Grading it as a discovery would have been rediscovery dressed as insight.

### What the test says about the method

Re-read #1 returned `NEW CONNECTION` on a question of *what was measured*. Re-read #2 returned
`NEW CONNECTION` on a question of *how it was measured*, and its yield came entirely from **Methods
prose that no prior reading had a reason to parse** — buffer recipes, a missing lysis step, an
unquantified spin. Both re-reads found their value in the same place: **the part of the paper that
the first reader's question made irrelevant.**

🔴 **And the honest counterweight:** three of this re-read's five candidate findings were already
held, and I had to re-grep to discover that. **Two deliberate re-reads is not enough evidence to
call this primitive reliable** — what it has demonstrated twice is that it *returns something*, not
that the something is worth the fetch. The cost is one full-text retrieval plus a proper baseline;
the yield so far is one connection each time.

`REVIVAL_TRIGGER` for this file: any WWOX construct expressed with a **stated** bacterial lysis
protocol; any WWOX western with a **stated** g-force and fraction; any orthogonal-partner folding
control run with **more than one** partner.
