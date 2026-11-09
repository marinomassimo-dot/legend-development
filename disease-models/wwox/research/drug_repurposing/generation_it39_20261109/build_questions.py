"""IT39 P5/P9: question dossiers assembled from the investigations table and the comparator table, no new reading.
Usage: python3 build_questions.py [--write]   (default prints; --write refreshes questions_it39.md). `--help` prints this text."""
import csv
import sys
from pathlib import Path

if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

DR = Path(__file__).resolve().parent.parent
IDS = ["INV-17", "INV-18", "INV-05", "INV-03"]
CUT = 700


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def build():
    inv = {r["inv_id"]: r for r in rd(DR / "ranking_it8_p9_20261029/investigations_it20.tsv")}
    comp = rd(DR / "comparators_it39_20261109/output/comparators.tsv")
    out = ["# Question dossiers (IT39): observed, inferred, the premise that decides, the test, the comparators", "",
           "Assembled mechanically from `investigations_it20.tsv` and `comparators_it39_20261109/output/comparators.tsv`; no new reading, no compound promoted, an order of research questions and not of treatments. Regenerate: `python3 build_questions.py --write`.", ""]
    for i in IDS:
        r = inv[i]
        out += [f"## {i}: {r['question']}", "",
                f"* direction state: {r['direction_state']}; status: {r['status']}; origin class: {r['origin_class']}",
                f"* observed and available: {r['evidence_available'][:CUT]}",
                f"* decisive uncertainty (the premise that decides): {r['decisive_uncertainty'][:CUT]}",
                f"* next test: {r['next_test'][:CUT]}"]
        rows = [c for c in comp if c["inv_id"] == i]
        for role in ("functional_outcome", "mechanism_separating"):
            names = sorted({c["comparator"] for c in rows if c["role"] == role})
            out.append(f"* comparators, {role.replace('_', ' ')}: " + ("; ".join(names) if names else "none in the files"))
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    text = build()
    if "--write" in sys.argv:
        (Path(__file__).resolve().parent / "questions_it39.md").write_text(text, encoding="utf-8")
    else:
        print(text)
