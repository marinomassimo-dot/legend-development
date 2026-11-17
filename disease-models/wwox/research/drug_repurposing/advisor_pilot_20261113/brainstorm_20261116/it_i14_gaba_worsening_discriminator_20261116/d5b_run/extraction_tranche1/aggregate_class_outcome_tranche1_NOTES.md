# Notes to aggregate_class_outcome_tranche1.tsv (moved out of the TSV so every row has the same width)

* D5b tranche 1 aggregate (IT, 2026-11-16): class x endpoint x age-at-exposure window x outcome category; counts of children with a stated outcome and of reports; no per-child label, no regimen-plus-person text.
* derived by script from the withheld exposures table, sha256 of that file as published in SEAL.sha256: 74eaac0397188c51b56fa2eeb708c943021ed4e6dc3e7566c7a67dcb95784387
* cells with fewer than 3 children are NOT SCORABLE by the rule (column scorable); the same child can contribute to several cells (several agents); outcome = as stated, polytherapy not attributable
