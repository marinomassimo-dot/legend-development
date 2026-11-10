"""Reproduces verify_sample.tsv (seed 42: up to six rows per qualification stratum of the run at the time of the first draw). The strata have since changed with the engine fixes of addendum 3, so the file in this folder is the one the independent reader checked."""
import csv, random, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
R = [(i, r) for i, r in enumerate(csv.DictReader(open(HERE.parent / "generation_it41_20261109/search_rows.tsv", encoding="utf-8"), delimiter="\t"), start=2) if r["labelled_form"] != "yes"]
random.seed(42); strata = collections.defaultdict(list)
for i, r in R: strata[(r["qualification"], r["reason"])].append((i, r))
for k, v in sorted(strata.items()): print(k, len(v), [i for i, _ in random.sample(v, min(6, len(v)))])
