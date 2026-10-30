#!/usr/bin/env python3
"""Post-hoc (not pre-declared): which compound sources and plates the 300 most-opposed compounds of trial 1 come from. Usage: trial1_source_check.py PROFILES.parquet results/jump_wwox_ko_most_opposed_top300.tsv"""
import sys
if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import pandas as pd, pyarrow.parquet as pq
t = pq.read_table(sys.argv[1], columns=["Metadata_Source", "Metadata_Plate", "Metadata_JCP2022"]).to_pandas()
top = pd.read_csv(sys.argv[2], sep="\t"); sub = t[t.Metadata_JCP2022.isin(top.jcp)]
print(sub.Metadata_Source.value_counts()); print(t[t.Metadata_JCP2022.str.startswith("JCP2022_0")].Metadata_Source.value_counts(normalize=True).round(3).head(8))
print(sub.Metadata_Plate.value_counts().head(5)); print(t[t.Metadata_JCP2022.str.startswith("JCP2022_8")].Metadata_Source.value_counts())
