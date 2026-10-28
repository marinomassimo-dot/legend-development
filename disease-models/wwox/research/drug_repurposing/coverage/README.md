# Coverage matrix and research priorities

Non-canonical research material (iteration 3). Generated; do not edit the JSON files by hand. Nothing
here is a ranking of treatments, a probability of benefit or cure, or medical advice.
Revision 4 (iteration 4, 2026-10-28) changes three semantics, described where they apply below: wild-type evidence is no longer reported as an observation in the disease model; consistent and opposed actions on one need are shown together; a source problem no longer changes every disposition. Revision 3 (2026-10-28) applied the independent audit of revision 1 and its re-verification
(`../locator_audits/2026-10-28_it3_coverage_independent_verification.md`, `…_reverification.md`).

**Plain statement (also in `coverage_summary.json` key `plain_statement`):** none of the interventions in this matrix is a catalogued
repurposing candidate with a controlled recovery in a WWOX system. The only experimental L4 cells are an AAV9 gene therapy (high dose,
n 5 for spike-wave discharges; for growth, **body weight only**, blood glucose unchanged); the other L4 cell is an uncontrolled case-level
clinical report (vigabatrin); the ketogenic-diet record is retrospective, has no denominator and is not counted as L4. Ethosuximide, lithium and a tool compound (d-APV) have single WWOX-system readouts without
recovery status; A51 has one readout with reading depth UNKNOWN (state `observed_depth_unknown`).

## One command

```bash
python3 -B framework/scripts/repurposing_coverage.py run      # about 6 s, offline, deterministic
python3 -B framework/scripts/repurposing_coverage.py check    # exit 1 if the files differ from a fresh regeneration
python3 -B framework/scripts/test_repurposing_coverage.py     # 47 offline tests: a synthetic fixture plus negative tests on the real files
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
| `assertion_pertinence.tsv` | for each card assertion: the need whose endpoint it measures, its subject, evidence kind, sign, whether it counts for L3/L4 and the `comparator` the sign is measured against (72 rows covering all 71 data assertions of the intervention cards). Evidence kinds that matter for wild type: `readout_in_wwox_system` (result in the WWOX model), `genotype_comparison_vs_wild_type` (the treated WWOX-deficient arm compared with wild type only, no untreated disease arm), `effect_in_wild_type_arm` (the drug's effect in a wild-type or heterozygous arm of the same experiment), `control_arm_same_experiment` (reference or control without an effect of its own) An assertion judged uninformative, out of scope, a control arm of the same experiment or unquantified is listed with `counts_L3=no` so it stays visible under `listed_not_counted`; any assertion left unlisted shows in the per-cell `unassessed_assertions_on_card` |

## What counts as a link (headline) and what does not

* **Headline link**: a catalogue row on an `intervention_target` or `disease_gene_product` of a need. ChEMBL by the human
  GENE_SYMBOL of the target component (PDK1 is not PDPK1; non-human rows are set aside), DGIdb by HGNC id.
* `pathway_member` targets are counted **apart** (`records_incl_pathway_members`); `effector_constraint` (MAPT) and
  `readout_marker` targets are **never** links; identity-guard targets are listed beside.
* Excluded and listed (`excluded_from_counts` on the association; counts under `catalogue_coverage.excluded_rows`):
  * **source artefact**: 77 DGIdb Guide-to-Pharmacology records carry ABAT only from a gene list that also holds ABCA1-3
    (adenosine-receptor ligands: caffeine, theophylline, istradefylline ...). Two rules, both in `source_artefacts.tsv`:
    the verified explicit row (`require_second_source` for ABAT and ABCA1-3) and a **generic detector** for alphabetical-prefix
    gene-list expansions in Guide-to-Pharmacology (a record holding 3 or more symbols from the first 8 percent of the DGIdb symbol list:
    A12M3, A1BG, AAMP, ABAT ...; a row on such a symbol with no second source does not count). The detector flags 2,229 rows catalogue-wide;
    of the need genes it touches only ABAT (55 of the 77 records; the other 22 are ABAT-only records that the run test cannot see and the
    explicit row covers), so the headline counts are identical to the explicit-rule outcome. Genuine ABAT records (vigabatrin, valproate,
    tiagabine ...) have a second source;
  * **alias risk**: DGIdb `PDK1` rows on records that also carry `PDPK1` and no ChEMBL PDK1 mechanism (Osu-03012/AR-12,
    celecoxib) are listed as unresolved alias-risk rows;
  * **placeholder**: the DGIdb drug literally named `NULL`.
  * Every excluded association carries an explicit `excluded_reason` (`source_artefact`, `alias_risk`, `placeholder`).
* Per-need counts are given by target kind and the unions are given both ways (headline only; headline plus pathway members).

## Four levels, never summed, never a score

1. **L1 documented link** (headline definition above); states `documented`, `pathway_member_only`, `none_found`,
   `source_incomplete`, `not_evaluable`.
2. **L2 mechanistic coherence**: direction-consistent action, only for needs with direction up, down or restore and an
   explicit role row. For `uncertain` needs L2 is `not_evaluable` and the list is an **exploration list**. The role row's
   qualifier travels with the label: the seizure-need cells are "symptom-level inference, not mechanism-linked to WWOX";
   GRIN rows rest on "ONE full competitive block (d-APV)"; T-type rows on "ONE ethosuximide experiment".
3. **L3 observed effect**: an assertion on this compound whose endpoint is listed as pertinent to this need, a readout in a WWOX
   system or a WWOX clinical case report, **with its sign** (benefit, partial, mixed, null, harm, normalised or not normalised against
   wild type when no knockout arm exists; never pooled). What the comparison is decides the meaning: only a **result in the WWOX model**
   (treated against the untreated disease arm, or a dose arm) or a WWOX case report makes a cell `observed_wwox_system` / `observed_case_level_only`.
   A **direct genotype comparison with wild type only** gives `observed_vs_wild_type_only`; a **pharmacological effect in a wild-type or carrier arm** gives
   `effect_in_wild_type_only`; neither is an effect in the disease model, a rescue or an L4 recovery. When a cell also has a result in the model, the
   wild-type rows sit beside it in their own sign fields (`signs_direct_genotype_comparison_vs_wild_type_only`, `signs_effect_in_wild_type_or_carrier_arms`)
   and are never mixed into `signs_wwox_system_readouts`. Every observation is kept in `observations` with subject row, meaning, comparator, endpoint,
   stage or time, genotype, conditions (flags), sign, reading depth and character (experimental, or uncontrolled clinical report). **An assertion whose reading depth is UNKNOWN never reaches
   `observed_wwox_system`** (state `observed_depth_unknown`). Control arms of the same experiment (wild type, heterozygote), uninformative
   case reports (n=1 on seven drugs) and out-of-scope endpoints are not observations and are listed apart. Each cell carries
   `unassessed_assertions_on_card` so it cannot read observed while a null of the same experiment is unlisted. Other-disease
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
`consistent_mechanism_candidate`, `exploration_candidate`, `opposite_mechanism`, `mixed_consistent_and_opposed_actions` (the same family has both a consistent and an opposed action on one need: both are listed with target, action, source and record, L2 reads `mixed_consistent_and_opposed`, and no sign is summed or netted), `no_catalogue_link_found` (renamed from
`not_relevant`: a statement about the catalogue, not about relevance), `insufficient_data`, `source_queried_without_result`,
`incomplete_or_failed_query`. Source states are a vocabulary of their own (`OK`, `STALE_EXPORT`, `STALE_AFTER_FAILED_REFRESH`,
`PARTIAL`, `FAILED`, `INCOMPLETE`, `NOT_FETCHED`). A hard problem of a source no longer turns every disposition
into `incomplete_or_failed_query`. Three things are kept apart: **positive evidence** (a documented link, a consistent or opposed action, an observation) stays
what it is when a working source supports it; the **search as a whole** is flagged incomplete on every priority record (`search_incompleteness`) and in
`search_completeness` of the summary; only an **absence conclusion that depends on the missing source** (no link found, no target row) becomes
`incomplete_or_failed_query`. A source's role decides which: ChEMBL and DGIdb (mechanism) and UniChem (identity) can undermine an absence;
openFDA NDC, DSLD and the drug matrix (accessibility or status) only caveat the access categories and never erase a mechanism. A positive link whose own source is
flagged keeps its disposition and carries a caveat. The stale DGIdb export (2024-06-10) adds a caveat to every absence-type result. No combination or
synergy is inferred.

## Access caveat

DSLD is `PARTIAL` (981 of 4,697 bulk-list names probed, name-only matching): every family row and every priority record carries an
`access_caveat`, and the summary lists it under `access_caveats`. For supplements `unknown/unverified` is not a negative.

## Limits

Catalogue links are source statements (no potency). DGIdb is a stale export and its rows are **not cleared for public release**.
`target_roles.tsv`, `source_artefacts.tsv` and `assertion_pertinence.tsv` are curated by hand and reviewable; every pair or
assertion they do not list is unresolved or uncounted. Cards added after the pertinence table was written (for example the
apinocaltamide card) have unlisted assertions until someone judges them. Seizure-need cells are symptom-level inferences.
Name-prefix siblings (lithium salts) are a hint only.

## Target identity (iteration 4, 2026-10-28): the cause behind the "short-name collisions"

The collisions listed in the previous audit (GRIN1/STING ligands, ATF4/nicotinic, CTNNB1/p38, EIF4EBP1/CDK, EIF2S1, GRIA1, GRIA2, GRIA4, GSK3B, ABAT/adenosine, zolbetuximab, GRP94 inhibitor 54, semapimod) were not name collisions. In the DGIdb 2024.1 Guide-to-Pharmacology rows, `gene_claim_name` is `NCBIGENE:<n>` where `<n>` is the **GtoPdb target id** (STING1 = 2902, ADORA1 = 18, CHRNA7 = 468, MAPK14 = 1499, CDK6 = 1978, BCAT2 = 2893, CLDN18 = 2903, HSP90B1 = 2904), an internal number, not an NCBI Gene id; DGIdb resolved the number to the gene that owns it as an Entrez id (GRIN1 = 2902, ABAT = 18, ATF4 = 468, CTNNB1 = 1499, EIF4EBP1 = 1978, GRIA4 = 2893, GRIN2A = 2903, GRIN2B = 2904) or, for part of the rows, by symbol. Measured against the GtoPdb 2026.3.1 download (public, no registration; ODbL database, CC BY-SA 4.0 contents): of 16,070 rows, 1,976 name a gene of the GtoPdb target (confirmed), 14,064 name another gene (corrected), 30 pair (ligand, target id) values are not in the release (unverified). The ligand id (IUPHAR.LIGAND) and the target id survive in the claim, so the catalogue now verifies each row through them (`catalog_build.py`, `identity_gtopdb`), replaces the served gene by the GtoPdb target's gene(s) (complex targets expand to their subunit genes, `target_level: complex`), keeps the served gene as `dgidb_served_gene`, and records GtoPdb's target name/class, species, stated selectivity and the number of same-family targets listed for the ligand. A row that cannot be verified stays visible as an `unconfirmed_identity` row and is the only thing excluded from counts. The ten symbol rules and the alphabetical-run detector of `source_artefacts.tsv` were removed (the file keeps only the PDK1/PDPK1 alias row); the guard test no longer holds a hand-listed gene set.

Consequences, in numbers (rows examined 2026-10-28, headline = records with a counted link): records 1,008 -> 1,218, families 979 -> 1,189; excluded `source_artefact` 232 -> 0 (every one of those rows was re-identified: they are real ligands of other targets); consistent cells 102 -> 103, opposed 13 -> 13. The rise is recovery of real GtoPdb interactions that DGIdb had attached to wrong genes (GRIA4 counted 28 -> 48, GSK3B 50 -> 81, GRIN1 57 -> 73), not new evidence. Positive controls kept: D-AP5, NVP-AAM077, ketamine, dizocilpine on GRIN2A/GRIN2B; vigabatrin on ABAT (ChEMBL INHIBITOR plus GtoPdb "irreversible inhibition"). Removed from GRIN2A/2B: zolbetuximab (CLDN18) and semapimod (HSP90B1). GRIA4's three records (BAY-069 and two numbered compounds) are confirmed errors (BCAT2 inhibitors); genuine GRIA4 ligands lost under other genes were recovered.

Evidence scope (new row fields): `target_scope` (`single_protein`, `single_protein_among_siblings`, `complex_or_group`, `unspecified`) and `subunit_selectivity` (`stated_for_this_target` only for a single protein with no same-family sibling for that ligand; otherwise `not_established`). D-AP5 is listed by GtoPdb on all four GluN2 subunits, memantine/ketamine by ChEMBL on the NMDA receptor complex group: they are NMDAR-level / GluN2-class links; the label `consistent` rests on the role row's class-level coupling and is never read as GluN2A or GluN2B selectivity. Row fields `relation_kind` (what kind of statement the claim source makes: curated mechanism/pharmacology, target-database or target-review listing, bioactivity compilation, pharmacogenomic association, cancer knowledge-base association; basis: DGIdb source full names) and `action_stated` separate a documented action from a listing; `headline_records_by_strongest_relation` in the summary reports 618 / 12 / 588 records (curated action / other-source action / link without stated action). `curated_mechanism_elsewhere` flags an unstated listing on a record whose curated mechanism names other targets (tiagabine on ABAT, curated target GAT-1): a flag, not an exclusion.

ABAT, second-source rows (DGIdb claim sources, none states an action): vigabatrin is documented (ChEMBL INHIBITOR, GtoPdb irreversible inhibition); CPP-115 is documented by GtoPdb (inhibitor, recovered); valproate is a pharmacogenomic association (PharmGKB) plus bioactivity (DTC) plus target-review listings, action unstated; tiagabine is a target-review listing contradicted by its curated mechanism (flagged); alanine, pyruvate, pyridoxal phosphate, 4-hydroxybenzaldehyde are Therapeutic Target Database listings with no action (substrate/cofactor-like or unclear). None of the unstated rows is read as inhibition.

Other anomaly found by query, independent of the listed genes: DGIdb resolves the claim symbol MCL1 (DTC, NCI, ChEMBL, CIViC; 77 rows including TTD's "MCL-1" target name) to `ADAMTSL4-AS1`, an antisense locus, PDE10A to LINC00473 and BACH1 to GRIK1-AS2. A generic flag (`claim_symbol_anomaly`) marks a symbol claim resolved to an antisense/lncRNA locus as `unverified`; no MCL1 row exists in the export under its own gene, so the true links are not recoverable offline (an HGNC lookup would be needed).

Still open: (1) the other claim sources (TTD target names, TEND/TdgClinicalTrial UniProt-derived genes, symbol claims of DTC/PharmGKB/NCI) have no stable-id check available offline, only the heuristic above and the PDK1/PDPK1 alias row; (2) GtoPdb 2026.3.1 is newer than DGIdb's 2024.1 claims, so a pair absent from it is unverified, not wrong; (3) subunit selectivity (GluN2A vs GluN2B) could be read from GtoPdb affinity values, which the catalogue deliberately does not copy; (4) the ChEMBL side was checked by the target types it already carries (group and complex targets give class-level links), not re-resolved through the ChEMBL target REST.

## Residual limits recorded before iteration 4 (items 2 and 3 are closed by the section above)

Closed since the final check: the per-need drop counts exist (`excluded_records_by_reason` per need) and a live-data test now fails when a source-artefact symbol overlaps a need target without a reviewed decision (`test_artefact_symbols_that_are_need_targets_...`).
The audit of `target_roles.tsv` and `source_artefacts.tsv` found nine more short-name collisions in the Guide-to-Pharmacology rows (GRIN1 STING ligands, ATF4 nicotinic ligands, CTNNB1 p38 inhibitors, EIF4EBP1 CDK inhibitors, EIF2S1, GRIA1, GRIA2, GRIA4, GSK3B); they are now `require_second_source` rows, and the headline moved from 1,026 to 1,008 records (979 families), consistent cells from 125 to 102.
Closed in iteration 4: (1) cells whose only comparison was against wild type no longer carry the name `observed_wwox_system` (see L3). Still open: (2) GRIN2A/GRIN2B keep a few Guide-to-Pharmacology-only rows that look like collisions (zolbetuximab, GRP94 inhibitor 54, semapimod) but sit beside many genuine NMDA-receptor ligands, so a symbol-level rule would drop real ones; (3) the GRIA4 rows were treated as collisions without being checked at source; (4) the collision hunt covered need genes only, and a gene added to a future need must be checked the same way (list its Guide-to-Pharmacology-only rows). GRIN2A/GRIN2B were kept at coupling `same` at class level on purpose (d-APV acts at the glutamate site, which sits on the GluN2 subunits); which GluN2 subunit is involved is not resolved. See `locator_audits/2026-10-28_it3_roles_artefacts_independent_audit.md`.
