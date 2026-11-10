# IT42 P1 — which decision reads the results (three cases, relation to public page)

Non-canonical working note. Not medical advice. Every link below is asserted by `test_trace_it42.py` (a link that disappears fails the test); no new engine was written.

## What was verified first (not asked of the operator)

IT41's reader call is real: `consume_reader.py` calls `hypothesis_package.comparison_for` (8 rows for INV-05) and joins the Harness identity table (the label conflict of GYKI 52466 travels with the name). The open question was who *uses* those outputs.

## What was only exported, and what now reads it

| Output | State before IT42 | Consumer now |
|---|---|---|
| `compound_identity_join.tsv` | read by nothing | `repurposing_view.compound_identity_states` turns it into a class label per item (conflict / unverified / partial / checked) shown on each entry of the public list in both editions, no name attached |
| `qualification`, `reason`, `unknown_fields` of `search_rows.tsv` | did not exist | a consistency gate in `test_trace_it42.py`: an entry cannot be shown as emerged, known requalified or probe if the engine EXCLUDES every row of its molecules, and the DQP-1105 entry must stay UNKNOWN; the entry kinds themselves are hand-assigned from these verdicts |
| `comparison_rows_it41.tsv` | read by nothing | still an export for the human reader of INV-05 and for the next brief (`next_batch_it42_20261110/BRIEF.md` cites its rows); **no automatic decision reads it** |
| `eval_results.tsv` | new | read by the report only |

## Case 1 — favourable and conditional: GluN2B-directed comparison

relation S1 (`relations_it41.tsv`) → `action_search.py` rows (59 non-labelled rows over ChEMBL mechanisms and GtoPdb) → qualification: 5 CANDIDATE with every check passed, 3 CANDIDATE with the receptor site missing (`unknown_fields: receptor_site`), 1 UNKNOWN, 50 EXCLUDED with a reason → comparison and selection in `comparisons_it41.md` (minimum interpretable experiment: one ifenprodil-site modulator up to its measured removable share) → investigation INV-05 (`next_test`, with per-molecule maxima, and `feasibility` carrying decision, in-silico work, new measure, reopen condition and priority) → entries V02, V05, V06, V07 of the public list. **Decision that reads it:** the choice of the minimum experiment and of which molecules may serve as second modulator; it is a human decision recorded in INV-05, and the page shows what moves it up or down.

## Case 2 — ambiguous identity: GYKI 52466 / GYKI 53655

relation S8 (AMPA/kainate antagonism, added for this trace) → rows from ChEMBL and GtoPdb → the GtoPdb label GYKI53784 matches the identity table through `record_name` and is **UNKNOWN: label_conflict** on GRIA1–4, while GYKI53655 stays CANDIDATE (a distinct structure is not dragged down) → comparator row of INV-05 for GYKI 53655 now states the Harness declaration (CHEMBL267450, different structure from GYKI 52466) → probes table and BH1 (IT41) → entry V03 shows "identity: label conflict" → public page. **Decision that reads it:** which tool the AMPA arm may name (the tissue data are for GYKI 53655) and that kinetic values of one are not carried to the other.

## Case 3 — must remain unknown

* DQP-1105 (S1): the assay text names GluN2C → UNKNOWN, entry V09 kind "weakened", never a GluN2B datum.
* KCC2 enhancement (S6): the table holds only inhibitors of SLC12A5; all are EXCLUDED for direction; no enhancer row exists, which is not an absent action (`cases.md` Case 4, README of IT41).
* BNIP3 direction (stage S18): three proposals carry INV-19, an abstention with a discriminating question, and the status does not change.
**Decision that reads it:** no compound is nominated; the entries say what would move them.
