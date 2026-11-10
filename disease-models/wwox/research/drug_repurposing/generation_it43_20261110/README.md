# IT43: from qualified knowledge to effective pharmacological generation

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. No predictive validation exists.

## P1: the comparison rows now decide a role (comparison_engine.py, test_comparison_engine.py)

`comparison_engine.py` reads, through Harness's `hypothesis_package`, the explicit fields of every pharmacological_comparison package registered for the investigation (decisive.tsv depth, class and system; new_measurements.tsv blocks_which_comparison_row; comparison.tsv) and writes `compound_decisions_it43.tsv`: evidence tier, derived role, comparison state, premise still needed (measurement ids), the discriminating measurement, public-source work and the question it relaunches. No score, no probability. Rules: only a proposition that names one compound and was read in a primary source gives PRIMARY; a statement naming two compounds never transfers a measure to either (it is a class statement); a limit proposition ("limit of Dnn") removes Dnn from the evidence; potency values from different systems, holding potentials or co-agonist levels are NOT_COMPARABLE; no proposition at all means not stated, never tested and absent.

| | Before (IT42) | After (IT43) |
|---|---|---|
| Tool entry V02 | "ifenprodil; Ro 25-6981" one probe | only ifenprodil is a probe (primary read, D01-D03) |
| Second ifenprodil-site tool | listed as a tool | moved to the unresolved entry V08: abstract values (D05, D06), triheteromer behaviour transferred (D11) |
| Next work for it | none stated | reading its primary source, open question IT43-Q01 (zero spend); no new measurement |
| Reference control | assigned by hand | derived: the design row names it the reference; evidence tier does not apply |
| Gate | none | `test_view_never_exceeds_the_engine`: a probe or requalified entry must be PRIMARY, or cite a source outside the registered packages (NP10679 rests on an abstract-level PMID and search rows: out of the engine's perimeter, said so) |

Contrast cases (synthetic packages, tests): a measure for one molecule does not reach a second named in a shared statement; potency under different holding potentials gives NOT_COMPARABLE and the same conditions give COMPARABLE; an unknown premise leaves the role unresolved and never "weakened".
Consumers changed: `compound_view.tsv` (V02, V08), `open_questions_map.tsv` (IT43-Q01), translations in four languages. Unchanged: INV-05's first experiment (its next_test already named the removable-fraction measurement).
Limits: the engine matches names by whole word and reads the producer's own labels; AMPA perampanel is PRIMARY in the engine but sits inside the unresolved entry V03 (grouped by the AMPA question, not split).

## P2: coverage without losing provenance (dgidb_listing.py, test_dgidb_listing.py)

**Cause of each omission, checked in the held sources before touching anything** (cache read-only):
* DGIdb claims were read by no search path: the catalogue holds them (81 572 claims, export 2024-06-10) on every record, but `action_search.py` reads only ChEMBL mechanism rows and GtoPdb interactions. A path-coverage gap, now closed by a separate listing path (`dgidb_listing.py`), not by changing the IT41/IT42 tables, so their evaluation stays reproducible.
* Ifenprodil and Ro 25-6981 (Q1 positives) are in no table because **the held sources do not carry the datum**, not because of a filter, identity or parser limit: ChEMBL records of ifenprodil (CHEMBL305187 and the tartrate) have no mechanism row; the DGIdb records of ifenprodil list only CYP1A2/CYP2D6/MTOR/DRD1 (DTC, no interaction type) and none names a GRIN gene; the GtoPdb release holds a ligand entry (id 5472) with no interaction row in `interactions.csv`; Ro 25-6981 is in none of the three. Retrieval by symbol could not have reached them; they stay known from primary sources (decisive.tsv D01-D06) and the identity table.

**Listing path.** For the relations S1-S8, every DGIdb claim whose gene is a relation target becomes one row, always UNKNOWN (`listing_only`): DGIdb carries no potency, species or site, and an interaction type ("blocker", "agonist") is recorded as a documented action, never as the relation's direction; radiolabelled forms and empty names are dropped.

Measured against the simple search (ChEMBL mechanisms plus GtoPdb, same relations, names matched after removing salt and stereo prefixes; `dgidb_summary_it43.tsv`):

| Distinct from the simple search | Count over S1-S8 |
|---|---|
| Molecules listed by DGIdb | 353 (relation x molecule) |
| New molecules reached | 105 (101 are DGIdb-only records: identity not reconciled with another source) |
| Of these with a documented action type | 18 |
| Qualification improved | 0 (by rule) |
| New hypotheses generated | 0 (by rule) |

Examples reached as new listings (known compounds; path coverage, not predictive value): a second ifenprodil-site modulator for S1 (eliprodil) and valproic acid for S7. Part of the "new" list is not a candidate: co-agonists and ions (aspartic acid, a divalent ion), compounds listed against a GRIN gene through other claim sources (typical DTC off-target listings). DGIdb's `claim_source` is kept per row; non-commercial claim sources keep their names out of the shareable edition.
Limits: names are matched by a normalised string, so a different salt or code name of a known molecule can still count as "new"; the DGIdb export is old (2024-06) and carries ChEMBL 33 claims.

## P3 to P7, short (details in the files named)
| Piece | Files | Result |
|---|---|---|
| P3 | `third_relation_it43.md` (frame before the search, with an addendum after the earlier INV-07 package was read), `relations_it43.tsv`, `s9/`, `apply_p3.py` | PDK inhibition: three typed molecules, all conditional on an unmeasured premise; the lever is known in WWOX and the compounds known in the repository; what changed is that two compounds the older generator listed as unsigned now have typed per-isoform rows; V13 on the cards |
| P4 | `eval_protocol_it43.md`, `eval_it43.py`, `eval_results.tsv`, `eval_summary_it43.md`, `verify/VERDICTS.md` | source value large, qualification value small on these three questions, generation kept conditional; independent reader: devimistat direction and one species corrected, inorganic ions returned as candidates (open gap) |
| P5 | `../generation_it42_20261110/README.md` (dated update) | IT42 introductory counts reconciled with run 4 |
| P6 | `compound_view.tsv` (column `origin`), `repurposing_view.py`, five-language strings | each card says where the hypothesis came from; the label says why this priority and the evidence |
| P7 | `apply_dream.py` | INV-07 and INV-19 share one isogenic sample series; the reading of each outcome is written in both investigation tables |

## P8 scouting
Taken from the current weekly scouting table of Harness (`governance/candidates/`), no new search and no dependency. Relevant to this iteration: the lookup retrieval-contract idea (entity, identifier, build and version, count before paging, log of every page) matches what the DGIdb listing rows already carry (source, claim source, cache digest); nothing to install. The ions gap noted by the independent reader is the one implementable defect left: a `non_drug_entity` verdict for inorganic ions in `action_search.qualify()`; it changes IT41/IT42 tables, so it is a separate, dated change with its own battery, not folded into this candidate.
