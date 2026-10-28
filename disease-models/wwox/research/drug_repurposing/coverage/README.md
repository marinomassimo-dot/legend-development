# Coverage matrix and research priorities

Non-canonical research material (iteration 3). Generated; do not edit the JSON files by hand. Nothing
here is a ranking of treatments, a probability of benefit or cure, or medical advice.
Revision 2 (2026-10-28) applies the independent audit of revision 1
(`../locator_audits/2026-10-28_it3_coverage_independent_verification.md`).

## One command

```bash
python3 -B framework/scripts/repurposing_coverage.py run      # about 6 s, offline, deterministic
python3 -B framework/scripts/repurposing_coverage.py check    # exit 1 if the files differ from a fresh regeneration
python3 -B framework/scripts/test_repurposing_coverage.py     # 26 offline regressions on a synthetic fixture
python3 -B framework/scripts/repurposing_search.py need NEED-T-TYPE-CALCIUM
python3 -B framework/scripts/repurposing_search.py compound memantine      # works for a compound with no card
```

Inputs are read at run time and never copied: `../needs/needs.json`, `../catalog/` (via
`framework/scripts/compound_catalog.py`), `../cards*/`, `../join/measure_next.json`, and three curated, reviewable
inputs in this directory. The `generated_from` block of `coverage_matrix.json` holds a digest of each input.
After `needs.json` or a card changes: regenerate, then regenerate the view (`repurposing_view.py run`).

| File | What it is |
|---|---|
| `coverage_summary.json` | the stable JSON the view reads (revision-1 key names are kept as aliases carrying the new definitions) |
| `coverage_matrix.json` | sparse rows x needs; every non-empty cell carries four separate levels |
| `priorities.json` | one record per prioritised (row, need) pair: disposition, reason, levels, eight criteria, next deepening |
| `associations.jsonl.gz` | every need -> target -> catalogue-record row with link source, raw action, consistency, `excluded_from_counts` and limits |
| `target_roles.tsv` | coupling between a target's activity and a direction-evaluable need's quantity, each with a certainty `qualifier`; GRIA1-4 are `unresolved` (the need says only "possibly AMPAR"; no datum) |
| `source_artefacts.tsv` | rules that keep known upstream artefacts out of the counts (below) |
| `assertion_pertinence.tsv` | for each card assertion: the need whose endpoint it measures, its subject, evidence kind, sign, and whether it counts for L3/L4 (52 rows). Unlisted assertions are not counted and are reported as `assertions_not_assessed_for_pertinence_not_counted` |

## What counts as a link (headline) and what does not

* **Headline link**: a catalogue row on an `intervention_target` or `disease_gene_product` of a need. ChEMBL by the human
  GENE_SYMBOL of the target component (PDK1 is not PDPK1; non-human rows are set aside), DGIdb by HGNC id.
* `pathway_member` targets are counted **apart** (`records_incl_pathway_members`); `effector_constraint` (MAPT) and
  `readout_marker` targets are **never** links; identity-guard targets are listed beside.
* Excluded and listed (`excluded_from_counts` on the association; counts under `catalogue_coverage.excluded_rows`):
  * **source artefact**: 77 DGIdb Guide-to-Pharmacology records carry ABAT only from a gene list that also holds ABCA1-3
    (adenosine-receptor ligands: caffeine, theophylline, istradefylline ...). Rule `require_second_source`: the lone
    Guide-to-Pharmacology row does not count; genuine ABAT records (vigabatrin, valproate, tiagabine ...) have a second source;
  * **alias risk**: DGIdb `PDK1` rows on records that also carry `PDPK1` and no ChEMBL PDK1 mechanism (Osu-03012/AR-12,
    celecoxib) are listed as unresolved alias-risk rows;
  * **placeholder**: the DGIdb drug literally named `NULL`.
* Per-need counts are given by target kind and the unions are given both ways (headline only; headline plus pathway members).

## Four levels, never summed, never a score

1. **L1 documented link** (headline definition above); states `documented`, `pathway_member_only`, `none_found`,
   `source_incomplete`, `not_evaluable`.
2. **L2 mechanistic coherence**: direction-consistent action, only for needs with direction up, down or restore and an
   explicit role row. For `uncertain` needs L2 is `not_evaluable` and the list is an **exploration list**. The role row's
   qualifier travels with the label: the seizure-need cells are "symptom-level inference, not mechanism-linked to WWOX";
   GRIN rows rest on "ONE full competitive block (d-APV)"; T-type rows on "ONE ethosuximide experiment".
3. **L3 observed effect**: an assertion on this compound whose endpoint is listed as pertinent to this need, a readout in a WWOX
   system or a WWOX clinical case report, **with its sign** (benefit, partial, mixed, null, harm; never pooled). Other-disease
   precedents (`precedent_other_disease_only`), enzyme or cell-free assays (`target_engagement_only`) and safety signals
   (`safety_signal_only`) are separate states. A tool compound (d-APV) or a genetic precedent (Ldh RNAi) is its own row and is
   never attached to a named drug; a mention of a compound id in card text attaches nothing.
4. **L4 observed recovery in a WWOX system**: an L3 assertion with bridge comparison `OPPOSES_DISEASE_CHANGE`, reading depth known,
   endpoint pertinent, one dose arm at a time (low-dose arms are `mixed` and never recovery); `observed_experimental` and
   `observed_case_level` (uncontrolled clinical report) are kept apart. It is a technical comparison, not efficacy.

Scope stays visible: `wwox_experimental`, `wwox_clinical_report`, other-disease precedent. The needs' own observations fill no
compound cell.

## Units and anti-inflation rules

* A **family** is a ChEMBL record group joined by parent link or identical InChIKey connectivity block; every source-only
  record is its own family and is **not merged on name**. Name twins are flagged and a collapsed count is given as a sensitivity
  figure only. Coverage counts families; record counts are labelled records.
* A (family, need) cell counts once however many targets or records produce it. Needs share targets, so per-need counts must not
  be added; use the unions. Dispositions are reported as cells **and** as distinct families/rows.
* Percentages carry numerator, denominator and what is counted; where no sensible denominator exists, counts and gaps are shown.
* Non-molecule modalities, class-level cards without a declared catalogue identity and tool/genetic subjects are rows `INT:<card>`
  (or `INT:<card>:tool`) of their own; their L1/L2 are `not_evaluable`, not zero.

## Priorities and how they can end

No score, no ordering by evidence volume (order is need id then row id). Each record lists a disposition, a reason, the levels, the
role qualifiers, and eight criteria (WWOX relevance, direction/mechanism, evidence quality and independence, counter-evidence,
potency and assay context, transferability, pharmacology/safety information present, discriminating experiment). Dispositions:
`consistent_mechanism_candidate`, `exploration_candidate`, `opposite_mechanism`, `no_catalogue_link_found` (renamed from
`not_relevant`: a statement about the catalogue, not about relevance), `insufficient_data`, `source_queried_without_result`,
`incomplete_or_failed_query`. Source states are a vocabulary of their own (`OK`, `STALE_EXPORT`, `STALE_AFTER_FAILED_REFRESH`,
`PARTIAL`, `FAILED`, `INCOMPLETE`, `NOT_FETCHED`): a hard problem of any source makes every disposition
`incomplete_or_failed_query`; the stale DGIdb export (2024-06-10) adds a caveat to every absence-type result. No combination or
synergy is inferred.

## Limits

Catalogue links are source statements (no potency). DGIdb is a stale export and its rows are **not cleared for public release**.
`target_roles.tsv`, `source_artefacts.tsv` and `assertion_pertinence.tsv` are curated by hand and reviewable; every pair or
assertion they do not list is unresolved or uncounted. Cards added after the pertinence table was written (for example the
apinocaltamide card) have unlisted assertions until someone judges them. Seizure-need cells are symptom-level inferences.
Name-prefix siblings (lithium salts) are a hint only.
