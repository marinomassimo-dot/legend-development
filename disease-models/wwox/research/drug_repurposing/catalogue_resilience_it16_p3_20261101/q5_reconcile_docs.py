#!/usr/bin/env python3
"""Measure what searching the markdown reports under disease-models/wwox/research/ would change in the 34 `reconciliation` values of deepening_queue.tsv.
Uses the tokens and the whole-word pattern of ranking_it8.prior_assessments (imported, not copied). Documents that discuss the queue itself (they contain
'deepening_queue' or 'deepening queue') are excluded: they read the queue and would count it as a mention of itself. Read-only: writes only --out.
`--help` touches neither the network nor any file."""
import argparse, csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DR = os.path.abspath(os.path.join(HERE, ".."))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--research", default=os.path.abspath(os.path.join(DR, "..")))
    ap.add_argument("--queue", default=os.path.join(DR, "ranking_it8_p9_20261029", "deepening_queue.tsv"))
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    sys.path.insert(0, os.path.join(DR, "ranking_it8_p9_20261029")); sys.path.insert(0, DR)
    import ranking_it8 as R
    texts, skipped = {}, 0
    for root, _, fs in os.walk(a.research):
        if os.path.basename(root) == "ranking_it8_p9_20261029" or "/.git" in root:
            continue
        for f in fs:
            if f.endswith(".md"):
                t = open(os.path.join(root, f), encoding="utf-8", errors="ignore").read().lower()
                if "deepening_queue" in t or "deepening queue" in t:
                    skipped += 1
                    continue
                texts[os.path.relpath(os.path.join(root, f), a.research)] = t
    rows = []
    for r in csv.DictReader(open(a.queue, encoding="utf-8"), delimiter="\t"):
        names = [n.strip() for n in r["names"].split(";")]
        toks = R._name_tokens(r["display_group"], names)
        pats = [re.compile(r"(?<![a-z0-9])" + re.escape(t).replace(r"\ ", r"[\s-]?") + r"(?![a-z0-9])") for t in toks]
        hits = sorted(k for k, t in texts.items() if any(p.search(t) for p in pats))
        cur = r["reconciliation"]
        new = cur if cur != "NO_CARD_OR_RECORD_FOUND" or not hits else "MENTIONED_ONLY"
        short = sorted(t for t in {R.display_group_key(r["display_group"])} | {R.display_group_key(n) for n in names} if t and len(t) < 6)
        rows.append([r["display_group"], cur, new, "CHANGES" if new != cur else "same", len(hits), "; ".join(hits[:5]), ";".join(short)])
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["display_group", "reconciliation_now", "reconciliation_if_reports_searched", "change", "n_report_documents", "first_documents", "names_shorter_than_6_chars"])
        w.writerows(rows)
    ch = [x for x in rows if x[3] == "CHANGES"]
    print(len(texts), "documents searched;", skipped, "excluded as queue-reading;", len(ch), "of", len(rows), "values change")


if __name__ == "__main__":
    main()
