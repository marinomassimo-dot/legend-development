# DREAM-3 pilot — pre-registration (written before the first delegate ran)

Date: 2026-11-08. Actor: `plan` (Harness Engineering). Scope: one small case, run twice on the same
repository, once before and once after the Dream pass writes its result into the shared homes.
Not a claim about WWOX biology; every statement about the biology below is exploratory.

## The case (new work, outcome unknown to the delegate)

Question given to a fresh delegate, identical in both runs:

> In this repository, what is known and what is open about the insulin-like growth factor (IGF)
> axis in WWOX-deficient animal models, and which single new measurement would be most informative?
> Use only files in the repository plus PubMed; propose, do not conclude.

What the repository already holds (checked by the author before the run, listed here so the
grading is not made afterwards):

| Item | Where | Status |
|---|---|---|
| `lde/lde` dwarfism, GH not significantly lower, IGF-1 axis never measured, "`WWOX AND "growth hormone"` returns 0 records" | `dismissal_ledger_current.md`, entry on the GH premise, revival trigger (c) | consumed as a dismissal; the "0" is dated and now **stale** (PubMed returns 4 records for WWOX with GH/IGF-1, none a measurement) |
| Wwox-null mouse: hypoglycaemia and growth failure rescued by neuronal AAV; IGF-1 not stated | `fulltext_dossiers/PMID34747138.md` | one datum, tissue of origin ambiguous |
| `lde/lde` uremic without hypoglycaemia; hypoglycaemia is one limb of a multi-system derangement | `analysis/DISCOVERY_TRACE_metabolic_gating_20260922.md` | consumed |
| Hypertension GWAS title "IGF1, SLC4A4, WWOX, SFMBT1" | `fulltext_dossiers/PMID22479346.md` | **misleading control**: a list of loci, not a link |
| Infant brain GWAS: IGFBP7 (grey matter) and WWOX (white matter), separate loci | `analysis/human_prenatal_infant_wave1_20260921.md` | **misleading control**: same sentence, different SNPs |
| IGF-1 and microglia in a myelination model (clemastine, Pdk1) | `drug_repurposing/myelin_inv06_20261107/verify/audit_m.md` row E39 | another session's package; context, not WWOX |

## What could change (stated before the run)

Without a Dream result in the shared homes, a fresh searcher is expected to find the GH dismissal
and probably the Wwox glucose paper, may repeat the PubMed search for GH, may treat the two
GWAS lists as support for a WWOX–IGF link, and will propose "measure serum IGF-1" without
saying what each outcome would separate. With the result in place the expected differences are
(each scored yes/no from the delegate's report and its transcript):

1. **Duplicate search avoided**: does not re-run the GH/IGF PubMed search the dismissal already covers, or runs it only to date-check the stale "0".
2. **Qualifiers kept**: the two GWAS lists are reported as co-occurrence without a WWOX–IGF link; the `lde` GH result is reported as "not significantly lower" with the small sample, not as "normal".
3. **Measurement discriminates**: the proposal names at least three rival explanations (endocrine deficit; consequence of seizures, feeding or uremia; cell-autonomous skeletal or muscle effect) and says which outcome of the proposed measurement would favour each.
4. **Stale item handled**: states that the "0 records" count is out of date and that the new records are not measurements.
5. **No effect is a valid result**: if both runs reach the same proposal at similar cost, the Dream result changed nothing and the verdict is SIMPLIFY or DISCARD for this movement.

## Controls and limits declared in advance

* Same model and effort for both runs (`legend-delegate`, Sonnet, medium, read back afterwards), one delegate at a time, no escalation.
* The delegate inherits the private memory index; a "repository only" instruction is not isolation. The transcript of each run is inspected for what entered its context. The limit is reported, not removed: no other session's memory is edited.
* n = 1 per arm. Differences are descriptive; a single pair cannot show reliability.
* A saved lead or a written note does not show that anything used it. The only consumer judged is the fresh searcher.
* Cost: tokens from the delegate transcripts (born, peak, output, cache read), apart from estimates; no conversion to a share of a plan.
