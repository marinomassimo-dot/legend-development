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

*(empty at pre-registration)*

---

## §6 · Classification

*(empty at pre-registration)*
