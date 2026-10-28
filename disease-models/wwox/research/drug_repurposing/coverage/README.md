# Coverage matrix and research priorities

Non-canonical research material (iteration 3, phase B). Generated; do not edit the JSON files by
hand. Nothing here is a ranking of treatments, a probability of benefit, or medical advice.

## One command

```bash
python3 -B framework/scripts/repurposing_coverage.py run      # about 6 s, offline, deterministic
python3 -B framework/scripts/repurposing_coverage.py check    # exit 1 if the files differ from a fresh regeneration
python3 -B framework/scripts/test_repurposing_coverage.py     # 17 offline regressions on a synthetic fixture
python3 -B framework/scripts/repurposing_search.py need NEED-T-TYPE-CALCIUM
python3 -B framework/scripts/repurposing_search.py compound memantine      # works for a compound with no card
```

Inputs are read at run time and never copied: `../needs/needs.json` (22 needs; edit and regenerate),
`../catalog/` (via `framework/scripts/compound_catalog.py`), `../cards*/`, `../join/measure_next.json`,
and `target_roles.tsv` (below). The `generated_from` block of `coverage_matrix.json` holds a digest of
each input.

| File | What it is |
|---|---|
| `coverage_summary.json` | the stable JSON the view reads: units, source states, per-need counts, matrix level counts, observations, disposition counts, limits |
| `coverage_matrix.json` | sparse rows x needs; every non-empty cell carries four separate levels |
| `priorities.json` | one record per prioritised (row, need) pair: disposition, reason, the eight criteria, next deepening |
| `associations.jsonl.gz` | every need -> target -> catalogue-record association with link source, raw action, consistency and limits |
| `target_roles.tsv` | explicit coupling between a target's activity and a direction-evaluable need's quantity (17 rows); an absent row means `direction_unresolved`, never a guess |

## Four levels, never summed, never a score

1. **L1 documented link**: the catalogue links a compound family to a link-type target of the need
   (ChEMBL mechanism by human gene symbol of the target component, DGIdb by HGNC id). Readout-marker
   and identity-guard targets are not links; an identity-guard hit is listed beside, and non-human
   ChEMBL rows are set aside.
2. **L2 mechanistic coherence**: the stated action on an intervention target is direction-consistent,
   only for needs whose direction is up, down or restore and only with an explicit role row.
   **For the 12 needs whose direction is `uncertain`, L2 is `not_evaluable` and the list is an
   exploration list** (labelled in every association, cell and priority).
3. **L3 observed effect**: a card assertion that is data (not inference) reports a readout change. The card
   must be cited by the need; endpoint-level pertinence is not checked.
4. **L4 observed recovery in a WWOX system**: a WWOX-system assertion whose bridge comparison is
   `OPPOSES_DISEASE_CHANGE`. This is the module's technical comparison, not efficacy or safety.

Scope stays visible on every observation: `wwox_experimental`, `wwox_clinical_report`,
`other_disease_precedent`, `unverified_hypothesis`. The needs' own WWOX observations (other contexts,
computational results) are not interventions and fill no compound cell.

## Units and anti-inflation rules

* A **family** is a ChEMBL record group joined by parent link or identical InChIKey connectivity block; every
  source-only record (DGIdb, MATRIX, openFDA) is its own family and is **not merged on name**. A name twin is
  flagged (`n_possible_duplicates`), and the summary gives the count if twins were collapsed as a sensitivity
  figure only. Coverage counts families, and says so; record counts are labelled records.
* A (family, need) cell counts once however many targets, pathways or salt records produce it. Needs share
  targets (CACNA1G, ABAT, GRIN1), so per-need counts must not be added; the union and the distribution by
  number of needs touched are in the summary.
* Percentages carry numerator, denominator and what is counted. Where no sensible denominator exists (there is
  no list of "all compounds that should be tested") the summary gives counts and gaps only.
* Non-molecule modalities (gene replacement, editing, ASO, diet) and class-level or unmatched cards are rows
  `INT:<card>` of their own, never counted as molecules; their L1/L2 are `not_evaluable`, not zero.

## Priorities, and how they can end

`priorities.json` has no score and no ordering by evidence volume (order is need id then row id). Each record
lists a **disposition**, a reason, the levels, and eight criteria with their values: WWOX relevance,
direction/mechanism, evidence quality and independence, counter-evidence, potency and assay context (always
`NOT_CARRIED`: the catalogue holds none), transferability (species and scope of the evidence, a stated
distance, not a score), pharmacology/safety information present (safety is `NOT_ASSESSED`), and whether a
discriminating experiment is named. Dispositions, each distinct: `consistent_mechanism_candidate`,
`exploration_candidate`, `opposite_mechanism`, `not_relevant`, `insufficient_data`,
`source_queried_without_result`, `incomplete_or_failed_query` (a catalogue source not in state OK; not a
negative). No combination or synergy is inferred; complementarity, redundancy and opposing actions for a set are
read from the per-target action fields of `associations.jsonl.gz` and the matrix, not computed as a joint score.
A pair enters `priorities.json` if it is card-attached, direction-coherent, or its family is approved or has
US access evidence; the rest stay in the matrix (counted under `pairs_not_prioritised`).

## Limits

Catalogue links are source statements (no potency). DGIdb is the 2024-06-10 export and its rows are **not
cleared for public release**. `target_roles.tsv` covers 17 target-need pairs; every other pair is unresolved.
Card pertinence is card-level. Class-level cards attach to their declared or mentioned catalogue members, and the
attachment (`identity`, `named_member`, `mentioned_in_text`) is recorded in each row. Name-prefix siblings (for
example lithium salts) are listed as a hint only. A failed or stale catalogue source turns every disposition
into `incomplete_or_failed_query`.
