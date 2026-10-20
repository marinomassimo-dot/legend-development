# WOREE_RESCUE_REFERENCE — scaffold for the Scientists

> **Non-canonical research scaffold.** Built by Harness Engineering (`plan`) on 2026-10-20 as
> part of `PLAN-REPURPOSING-INTEGRATION-20261020`. It is a **table to be filled**, not a
> reading, not a claim and not a scientific conclusion. It touches none of the four scientific
> current files and no `BATCH_COMMIT` accompanies it. Harness Engineering filled only the cells
> the external roadmap itself attributes to the rescue reference, and marked every one of them
> `TRANSCRIBED_FROM_ROADMAP` · `UNVERIFIED_BY_THIS_RECORD`. **No cell below was read out of the
> primary source by this record.**

## 0 · Why this scaffold exists, and the one thing the roadmap got wrong about it

The external roadmap (`roadmap_v4_r14_20261020.md`, "Riferimento di rescue e obiettivi
funzionali") asks P3 to adopt a `WOREE_RESCUE_REFERENCE` card with five endpoint families, each
annotating figure/table, model, control, age, intervention, direction, duration and limits. The
scout register's 2026-10-10 checkpoint proposes it on the premise that "il lavoro non compare
nella roadmap corrente" and that it is "nuovo per questo radar".

**Measured here on 2026-10-20: the paper is not new to this repository, and it is not unread.**
The rescue reference the roadmap wants built from an abstract is already a read paper with a
registry record, a claim and twelve receipts:

| Fact | Measured value | Command |
|---|---|---|
| Identity | PMID **42422765** = DOI 10.1016/j.omta.2026.201791 = PMCID PMC13343157, *Mol Ther Adv* 2026;34:201791 | `registry_records.py get --pmid 42422765` |
| Receipts | **12**, of which one `complete_fulltext_read` (`FTR-20260814-42422765-06`, 29 locators: 16 figure attestations, 13 body snippets) and eleven `partial_fulltext_read`, the latest `FTR-20261019-42422765-01` | `fulltext_receipts.py status --pmid 42422765` |
| Registry | `PAPER 011` — "Obeid 2026 neuron-specific gene therapy"; `CLAIM 011` — `DATO preclinico (full text reviewed)`, status *flagged for review* | `registry_records.py get --pmid 42422765` |
| Dossiers | `disease-models/wwox/research/fulltext_dossiers/PMID42422765.md`, `…_partial_locators.md` (55 KB), `disease-models/wwox/research/deepdive_manifests/PMID42422765.json` | `ls` |
| Artefacts on disk | `files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml`, `…_r2.xml`, `files/fulltext/PMID42422765_Obeid2026_assets/{mmc1,mmc2}.pdf` | `ls` |

**Consequence for whoever fills this table: fill it from the receipted reading and its
locators, not from the roadmap.** The roadmap's sentences are a secondary summary of an
abstract; this repository holds the full text, the supplement and 29 bound locators. Where the
two differ, the reading wins and the divergence is recorded in § 3.

## 1 · What the scaffold demands per row

Every endpoint family takes **one row per measure**, and a row is complete only when all eight
columns are bound:

| Column | What binds it | What does not bind it |
|---|---|---|
| `figure_or_table` | the panel/table identifier in the primary, plus the locator or receipt event that attests it | the roadmap's prose; a figure number carried in memory |
| `model` | genotype, species, strain, construct and vector configuration as printed | "the mouse model" |
| `control` | the comparator arm actually run, named as the primary names it | "improved" with no stated comparator |
| `age` | age or developmental stage at measurement, as printed | the intervention window reused as the measurement age |
| `intervention` | construct, route, dose **with its unit convention as printed**, and schedule | a dose quoted without the primary's unit ambiguity |
| `direction` | the direction of change at that endpoint, or `UNKNOWN` | a direction inferred from another endpoint in the same paper |
| `duration` | how long the effect was followed, and until when it held | survival of the cohort reported as duration of the effect |
| `limits` | what the measure cannot support: power, cohort size, selection, transfer | a limits sentence copied from the abstract |

Rules the roadmap states and this scaffold keeps: do not call an improvement equivalent to the
control without examining the measure and the power of the comparison; do not assign numeric
weights to the five families from this single study; a partial benefit on one useful endpoint is
admissible; concordance with these endpoints is **not** evidence of efficacy for any candidate.

## 2 · The five endpoint families

Status vocabulary used in the cells below, and nowhere expanded into a new taxonomy:
`TRANSCRIBED_FROM_ROADMAP` (a sentence carried from the external deliverable, unverified here) ·
`NOT_YET_BOUND` (owed: no cell value yet, and its absence is a debt, not a negative result) ·
`UNKNOWN` (looked for and not determinable).

### 2.1 Excitability / EEG

| Column | Value | Status |
|---|---|---|
| `figure_or_table` | NOT_YET_BOUND — the complete read carries 16 figure attestations; bind the panel, do not re-derive it | NOT_YET_BOUND |
| `model` | *Wwox*-null mouse | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `control` | NOT_YET_BOUND | NOT_YET_BOUND |
| `age` | NOT_YET_BOUND | NOT_YET_BOUND |
| `intervention` | neuronal AAV9-hSynI-WWOX | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `direction` | improvement of excitability / epileptiform discharges reported | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `duration` | NOT_YET_BOUND | NOT_YET_BOUND |
| `limits` | the roadmap and the scout register both call the electrophysiology cohorts limited; the size is not stated in either | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |

### 2.2 Myelination

| Column | Value | Status |
|---|---|---|
| `figure_or_table` | NOT_YET_BOUND | NOT_YET_BOUND |
| `model` | *Wwox*-null mouse | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `control` | NOT_YET_BOUND | NOT_YET_BOUND |
| `age` | NOT_YET_BOUND | NOT_YET_BOUND |
| `intervention` | neuronal AAV9-hSynI-WWOX | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `direction` | improvement of myelination reported | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `duration` | NOT_YET_BOUND | NOT_YET_BOUND |
| `limits` | the **oligodendrocyte-targeted construct produced no benefit under the conditions tested**; expression and configuration differ between constructs, so this does **not** show that oligodendrocytes are useless as a pharmacological target | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |

### 2.3 Neuroinflammation / gliosis

| Column | Value | Status |
|---|---|---|
| `figure_or_table` | NOT_YET_BOUND | NOT_YET_BOUND |
| `model` | *Wwox*-null mouse | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `control` | NOT_YET_BOUND | NOT_YET_BOUND |
| `age` | NOT_YET_BOUND | NOT_YET_BOUND |
| `intervention` | neuronal AAV9-hSynI-WWOX | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `direction` | improvement of gliosis / neuroinflammation reported | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `duration` | NOT_YET_BOUND | NOT_YET_BOUND |
| `limits` | a glial effect observed after a **neuronal** rescue does not identify a direct glial target | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |

### 2.4 Growth / metabolism

| Column | Value | Status |
|---|---|---|
| `figure_or_table` | NOT_YET_BOUND | NOT_YET_BOUND |
| `model` | *Wwox*-null mouse | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `control` | NOT_YET_BOUND | NOT_YET_BOUND |
| `age` | NOT_YET_BOUND | NOT_YET_BOUND |
| `intervention` | neuronal AAV9-hSynI-WWOX | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `direction` | improvement of growth and of glycaemia reported | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `duration` | NOT_YET_BOUND | NOT_YET_BOUND |
| `limits` | a systemic readout after a brain-directed intervention needs its own mechanism statement; see § 3 on the dose dependence of this family | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |

### 2.5 Survival / function

| Column | Value | Status |
|---|---|---|
| `figure_or_table` | NOT_YET_BOUND | NOT_YET_BOUND |
| `model` | *Wwox*-null mouse | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `control` | NOT_YET_BOUND | NOT_YET_BOUND |
| `age` | NOT_YET_BOUND | NOT_YET_BOUND |
| `intervention` | neuronal AAV9-hSynI-WWOX, intervention window **P1–P5** per the abstract | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `direction` | improvement of survival and of function reported | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |
| `duration` | NOT_YET_BOUND | NOT_YET_BOUND |
| `limits` | the abstract's window is **P1–P5 and efficacy at later ages is not demonstrated**; the roadmap corrects its own earlier text (scout register, 2026-10-10, said "P0–P5") and corrects the date to publication 18 June 2026 with 10 September as the issue date | TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD |

## 3 · Divergences the filler must resolve before using any of the above

1. **"Dose-dependent" against a threshold.** The roadmap and the scout register both carry the
   primary's own word *dose-dependent*. `CLAIM 011` in this repository is **flagged for review**
   precisely over that word: its flag states that the low-dose arm does not rescue survival and
   that the panel places a threshold between the two doses, so a continuum reading and a
   threshold reading "recommend different trials". A filler who takes the roadmap's phrasing
   imports the flagged reading. Resolve against `CLAIM 011` and its locators, not against this
   scaffold and not against the roadmap.
2. **Dose unit convention.** `CLAIM 011` records that the primary never declares its unit
   convention, leaving the absolute dose uncertain by a factor of exactly two while the HD/LD
   ratio is invariant. Any `intervention` cell that quotes a dose must carry that ambiguity.
3. **Which endpoints the complete read resolved.** `CLAIM 011` states that the three remaining
   domains (ECoG/SWD, myelination, gliosis) are resolved by the complete read "and not all in
   the same direction", with the rewrite tracked as scientifically open. This scaffold therefore
   pre-fills direction cells only as *reported by the roadmap*, and a filler must not promote
   them to the claim's direction without the locators.

## 4 · What this reference is not

- **It is not Q230P evidence.** The model is a *Wwox*-null full knockout. It is neither the
  Q230P missense allele nor a compound heterozygote. `CLAIM 011`'s own genotype caution says the
  design principles (neuron targeting, dose, early window) transfer to trial-readiness logic
  while the expected level of rescue in the reference genotype does not follow from this study.
- **It is not a reusable RNA-seq rescue signature.** The scout register records the primary's
  own data-availability statement as "not relevant": there is no rescue-versus-knockout
  transcriptomic contrast here to invert, to feed to LINCS/iLINCS or to pass to any
  perturbation model. GSE156243 is a knockout-versus-wild-type organoid contrast and is not this
  study's rescue arm; the two must not be merged.
- **It is not an endpoint weighting.** The five families are revisable qualitative references.
  No candidate is required to cover all five, and no numeric weight may be derived from this
  single study.
- **It is not medical advice and names no dose for any person.**

## 5 · How to fill it

1. `python3 framework/scripts/fulltext_receipts.py status --pmid 42422765` — read the receipt
   set and pick the events whose locators cover the family in hand.
2. `python3 framework/scripts/registry_records.py get --pmid 42422765` — read `PAPER 011`,
   `CLAIM 011` and the open flag before writing a direction.
3. Bind each row from `disease-models/wwox/research/fulltext_dossiers/PMID42422765_partial_locators.md`
   and `…/deepdive_manifests/PMID42422765.json`; where a cell needs a panel nobody has opened for
   this question, that is a re-read (read2, read3 …) with its own receipt, not a gap to guess.
4. Replace each `TRANSCRIBED_FROM_ROADMAP` cell with the bound value, or strike it; a transcribed
   cell that survives unbound is reading debt, and it is visible by design.
5. Anything promoted beyond this file goes through the ordinary pipeline. Nothing in this
   scaffold may reach the four scientific current files except through `BATCH_COMMIT`.
