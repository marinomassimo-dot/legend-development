# Retrieval-miss probe: why a held Wnt answer was not found from the text of a prediction (ADV-023, HE, 2026-11-17)

Not medical advice. Mechanism and retrieval level only. Probe at the level of file lists and the first lines each route prints; no source was re-read for science.

## The case
IT's selection note (`it_rp008_lens_selection_20261117/`) states prediction R2 ("WNT5A-pathway activity lower in knockout organoids; the held-data pre-test needs E-MTAB-14792"). SCI's gate note did not cite the held answer either. The held answer is
`gse156243/prediction_wnt_sign_20261025.md`, RESULT section: the seven canonical Wnt genes including WNT5A are all up in the knockout (4 against 2 libraries), with the maturation limit. The paper's own figure-level reading is in `deepdive_manifests/PMID34268881.json` (Figure 4D; the rescue brings WNT5A back toward or below wild type).

## Preregistration
[`PREREG_written_before_any_route.md`](PREREG_written_before_any_route.md), written before any route was run (sha256 prefix 91805195546ef146 at writing): ten routes a searcher could pick without naming the dataset folder, about 2.5 expected to surface the file in the first 20 lines or rows, best expected a file list (route 2), then the working model or the portfolio (8, 9); expected cause: indexing and representation (results filed by dataset folder), then tool choice.
A route counts as surfacing the held answer when the file, or a line that names it, is in the first 20 lines or rows of the output.

## Before (main d5e9061fa, 2026-11-17 18:30Z)
| # | Route and exact query | First thing it returns | File in the first 20? |
|---|---|---|---|
| 1 | `git grep -n WNT5A` | 74 lines, opened by `pathograph_export.jsonl`, corpus seed, receipts, a commit candidate | **no**: its 3 lines are hits 31 to 33 of 74 |
| 2 | `git grep -il WNT5A -- disease-models` | 58 file names, alphabetical | **no**: rank 24 of 58 (a reader who scans all 58 sees `prediction_wnt_sign`) |
| 3 | `build_evidence_index.py --term WNT5A` | 14 manifest records, the first two from PMID 22574198 | **file no; datum yes**: PMID 34268881 Figure 4D records are ranks 3 to 5 (rescue brings WNT5A back toward or below wild type), but this is the paper's figure, not the 10-25 test, and it is truncated to a proposition |
| 4 | `repurposing_search.py target WNT5A` | "0 ChEMBL human mechanism rows" | no |
| 5 | `supplement_symbol_search.py WNT5A` | "0 file(s) with a match" (a statement about supplements on disk) | no |
| 6 | `registry_records.py get --theme wnt` | surface preambles of two registries, no record naming the file | no |
| 7 | `framework/scripts/README.md`, grep Wnt/organoid | 1 hit, unrelated (the join row) | no |
| 8 | `CLAUDE.md`, then `working_model_current.md`, grep Wnt | router: 0; working model: 2 lines, both HIF1A "Wnt-adjacent" | no |
| 9 | `research_portfolio.tsv`, `drug_repurposing/README.md`, `roadmap_current.md`, grep Wnt | README: 4 Wnt hits (D02 tankyrase), none the organoid sign; the file is named by none | no |
| 10 | `discovery_ledger_current.md`, grep WNT5A | one line, "Evidence boundary" dated 2026-10-03: direction not fixed by neural data (it predates the 10-25 result; I saw no later line on that entry in this grep) | no (and the line it returns is the earlier state) |
| 11 | `gse156243/README.md` (oracle: needs the folder name; not counted) | line 18 says the raised canonical Wnt readout was already in manifest entry 31 | does not name the file |

Before: **0 of 10** routes put the file in the first 20; 1 of 10 (route 3) puts the underlying paper-level datum there. Prediction was about 2.5 of 10 (routes 2, 8, 9 were my best guesses); I was wrong on 2 (rank 24, alphabetical order), 8 and 9 (neither names it).

## Which kind of miss
- **Indexing and representation gap, mostly.** The held test is filed by dataset folder (`gse156243/`). The surfaces a searcher starts from are filed by paper (evidence index, manifests), by need (`needs_human_neural_systems.tsv` names GSE156243 for WNT-BETA-CATENIN but no router points to it) or by record (registries); none is keyed by gene. Who cites the file: the cards `M01*`, the therapeutic-hypotheses ledger and the generation-arm prediction ledger; not the discovery ledger, the working model, the claim registry nor any README.
- **Tool choice, in part.** The two routes that work (a plain `git grep -n WNT5A` read to the end, and the evidence index) are generic and found the datum; the structured tools for need and compound return nothing for a gene that is not a drug target.
- **Reader's choice: not determined.** I did not read what IT or SCI ran. IT's own note says "I did not confirm a held copy" of E-MTAB-14792, a different dataset, and a pre-test on radial-glia cell types is not the bulk test already held; the note proposes the pre-test without checking the bulk result for the same gene.
- A second, unfixed finding: route 10 returns a dated 2026-10-03 statement that the neural direction is unfixed, with no pointer to the 10-25 result. A reader who stops there gets the older state.

## The one fix (reversible: delete one paragraph)
One paragraph in `drug_repurposing/README.md`, before "The rest of the capability, and where it lives": held results are filed by dataset folder; the organoid Wnt sign result and its location; the per-need list of held human-neural readings. It uses the gene symbols as text so that a symbol search reaches it.

## After (same ten routes, same queries, working tree with the paragraph)
| # | Result |
|---|---|
| 1 | README paragraph is hit 12 of 75, and it names the file: **yes** |
| 2 | README is rank 9 of 59: **yes** |
| 9 | README names the file: **yes** |
| 3 to 8, 10 | unchanged, no |

After: **3 of 10** (before 0 of 10). The three that moved are text searches; the structured tools (4 to 6) and the ledger and working-model routes (8, 10) are unchanged, so the gap is closed for a searcher who greps the research folder and still open for one who uses only those tools. One paragraph also does not generalise: the next held gene result filed under a dataset folder is as hidden as this one was.

## What would close it for the general case (not done)
A derived gene-to-held-result index regenerated from `prediction_*.md` RESULT sections, or a line in the working-model row for the organoid evidence; each is more than a pointer and is left to the Advisor's choice of priority.

## Update 2026-11-17, second re-run: the derived index route (ADV decision; preregistration addendum written before the run)
Built: `framework/scripts/held_results_index.py` (build, check, lookup), its test `framework/scripts/test_held_results_index.py`, the derived copy `gse156243/HELD_RESULTS_BY_GENE_derived.md` (marked derived at its head; 136 rows; rebuilt by one command, `check` fails on drift), one routing row in `framework/scripts/README.md` section 1 and one recipe row in section 13. No source file edited. The test rebuilds the index and checks that WNT5A points to `prediction_wnt_sign_20261025.md` RESULT, line 49 ("7 of 7 up"), accession GSE156243.

Re-run on the working tree after merging main (same queries as the first run; routes 12 and 13 added):
| # | Route | In the first 20? | What made it move |
|---|---|---|---|
| 1 | `git grep -n WNT5A` (146 lines now) | yes: 5 of the first 20 name the file | IT's dated updates (a51 node, hit 1; discovery ledger, hit 13) and the README paragraph (hit 14), landed meanwhile |
| 2 | `git grep -il WNT5A -- disease-models` | yes (README rank 10; note rank 40, derived index rank 30) | README paragraph |
| 3 | evidence index `--term WNT5A` | no for the file; the paper-level datum is still there | unchanged |
| 4, 5, 6, 8 | need/compound search, supplement search, registry theme, working model | no | unchanged |
| 7 | scripts README grep Wnt/organoid | yes (the new section 13 row names the file) | new recipe row |
| 9 | README, portfolio, roadmap | yes | README paragraph |
| 10 | discovery ledger grep WNT5A | yes (IT's dated update, line 103, names the file) | IT, not this work |
| 12 | `held_results_index.py lookup WNT5A` | yes (the Wnt sign note, line 49, first row after the reanalysis) | the index |
| 13 | scripts README grep "held result" | yes (routing row and recipe row) | the index rows |
Result: **7 of 12** routes (the ten original: 5; the two new: 2). Preregistered: 4 of 11, and route 13 deciding findability. Differences from the prediction: route 10 (not predicted; IT's update, made at ADV's request after the first report) and route 7 (not predicted; the recipe row names the file, which is the router naming it rather than the tool finding it).
What this does and does not show: the index route works when the searcher knows the tool or greps the router for "held result" (route 13 found it); the structured need and compound tools and the working model are still silent on the gene. The count mixes three interventions (README paragraph, IT's ledger and node updates, the index and its rows), made at different times; the per-route "what made it move" column is the attribution, not a controlled comparison. The index covers one folder and RESULT sections of notes that declare a gene set; a gene that none of them declares returns "not indexed", a statement about the folder.
