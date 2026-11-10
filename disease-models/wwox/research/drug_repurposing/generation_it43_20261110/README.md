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
