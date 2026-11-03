# eng_main, eng_arm, eng_merged

Engine output of the IT22 incremental runs (`run_v4.py --seeds-dir --only`), kept so the stage tables can be re-derived. Each folder held a relative symlink `actions` ->
`../../generation_it21_p2_20261103/results/actions` (made by `run_v4.py`); symlinks are not allowed on the release surface, so they were removed from the commit. To re-run `make_candidates_v3.py` or `propose` on one of
these folders, recreate it: `ln -s ../../generation_it21_p2_20261103/results/actions <folder>/actions`.
