# Preregistration, written before any route was run (2026-11-17, HE)
Input text only: IT's R2 prediction ("WNT5A-pathway activity lower in WWOX-knockout organoids; held-data pre-test needs E-MTAB-14792").
Target: gse156243/prediction_wnt_sign_20261025.md (RESULT: seven canonical Wnt genes incl. WNT5A all up in KO, 4 vs 2 libraries).
A route "surfaces" the held answer if the file (or its 7-of-7-up statement) is in the first 20 lines/rows of its output, with no folder or file name given by the searcher.
Routes (N=11) and my probability that each surfaces it:
 1 git grep -n WNT5A (whole repo, first 20 lines)                         0.15
 2 git grep -il WNT5A -- disease-models (file list, scanned whole)         0.60 (the file name contains wnt)
 3 build_evidence_index.py --term WNT5A                                    0.30
 4 repurposing_search.py target WNT5A                                      0.10
 5 supplement_symbol_search.py WNT5A                                       0.05
 6 registry_records.py get --theme wnt (registry route)                    0.10
 7 scripts README (grep Wnt/WNT5A/organoid)                                0.05
 8 CLAUDE.md router -> working_model_current.md (grep WNT5A/Wnt sign)      0.40
 9 research_portfolio.tsv + drug_repurposing README/roadmap grep           0.40
10 discovery ledger grep WNT5A (no query tool exists; check only)          0.20
11 gse156243/README.md (needs the folder name: oracle control, not counted as a route a searcher could pick) 0.70
Expected count of routes 1-10 that surface it: about 2.5 of 10. The route I expect to work best: 2 (a file list), then 8 or 9.
Expected cause of a miss: indexing/representation (results filed by dataset folder, not by gene or need), then tool choice.
