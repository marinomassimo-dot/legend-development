"""ADV-287 extension: apply the sentence-only screen (frozen in PREREG) to list_ext.tsv and write sample_final.tsv.
Run: python3 -P -E screen_ext.py"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {"H02-01": "label (age band)", "H02-18": "design label (culture and exposure days)", "H02-19": "design label (ages, days of exposure)",
       "H02-20": "the word ratio without a value", "H02-22": "no quantity", "A01-01": "proposed experiment", "A01-12": "the word ratio without a value",
       "R-18": "the word ratio without a value", "R-20": "identical text already drawn (R-19)", "R-21": "design description, no value",
       "R-22": "versus without a value", "R-23": "the word range without a value", "R-26": "label (age)", "R-27": "the word ratio without a value",
       "R-28": "proposed result", "R-30": "identical text already drawn (R-19)", "R-31": "the word range without a value",
       "R-32": "identical text already drawn (R-19)", "R-36": "the word range without a value", "R-38": "identical text already drawn (R-19)"}
rows = list(csv.DictReader(open(os.path.join(HERE, "list_ext.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE))
take = [r for r in rows if r["role"] == "full_pass" and r["n"] not in OUT]
for k in ("route1", "route2_only"):
    need = sum(r["role"] == f"sample_{k}" for r in rows)
    pool = [r for r in rows if r["role"] in (f"sample_{k}", f"reserve_{k}") and r["n"] not in OUT]
    take += pool[:need]
cols = list(rows[0].keys())
with open(os.path.join(HERE, "sample_final.tsv"), "w") as o:
    o.write("\t".join(cols) + "\n")
    for r in take: o.write("\t".join(r[c] for c in cols) + "\n")
with open(os.path.join(HERE, "screened_out.tsv"), "w") as o:
    o.write("n\tcard\treason\tsentence\n")
    for r in rows:
        if r["n"] in OUT: o.write("\t".join([r["n"], r["card"], OUT[r["n"]], r["sentence"]]) + "\n")
import collections
c = collections.Counter(r["n"].split("-")[0] for r in take)
print(dict(c), "families in random 20:", len({r["card"].split("_")[0] for r in take if r["n"].startswith("R-")}), [r["n"] for r in take if r["n"].startswith("R-")])
