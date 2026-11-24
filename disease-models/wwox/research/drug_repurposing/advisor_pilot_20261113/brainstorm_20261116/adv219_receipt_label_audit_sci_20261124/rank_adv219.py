"""Ranking of flagged records by OPEN-row link (ADV-219, rule of PREREG section 6). Print-only.

Inputs: flags TSV from labelling_flags_adv219.py, two registry catalog JSON dumps
(registry_records.py catalog --json with Identifier and Full title columns), the open
questions map. Score: +3 per OPEN/IN_PROGRESS/CLAIMED row naming the record's identifier or
'PAPER n'; +1 per such row sharing >= 2 rare title tokens; +2 if a flagged section is
data-bearing (results, figures, tables, supplementary). Ties: lower PAPER number first.

Usage: python3 rank_adv219.py flags.tsv catalog_ident.json catalog_title.json open_questions_map.tsv
"""
import collections
import csv
import json
import re
import sys

DATA = {"results", "figures", "tables", "supplementary"}
STOP = set()


def toks(s):
    return set(t for t in re.findall(r"[a-z]{6,}", s.lower()))


def main(flags_p, ci_p, ct_p, map_p):
    ident = {r["id"]: " ".join(r.get("Identifier") or []) for r in json.load(open(ci_p))["rows"]
             if r["source"] == "paper_registry_current"}
    title = {r["id"]: " ".join(r.get("Full title") or []) for r in json.load(open(ct_p))["rows"]
             if r["source"] == "paper_registry_current"}
    freq = collections.Counter()
    for t in title.values():
        freq.update(toks(t))
    common = set(w for w, _ in freq.most_common(60))
    rows = [r for r in csv.DictReader(open(map_p), delimiter="\t")
            if r["status"] in ("OPEN", "IN_PROGRESS", "CLAIMED_THIS_BATCH")]
    rowtxt = {r["qid"]: " ".join([r["question_text_max300"], r["source_ref"], r["status_evidence"]]) for r in rows}
    flagged = collections.defaultdict(list)
    for line in open(flags_p):
        if line.startswith("#") or not line.strip():
            continue
        f = line.rstrip("\n").split("\t")
        if f[1] == "primary":
            flagged[f[0]].append((f[3], f[5]))
    by_key = {}
    for pid, idt in ident.items():
        for k in flagged:
            if k in idt:
                by_key.setdefault(k, []).append(pid)
    out = []
    for k, secs in flagged.items():
        for pid in by_key.get(k, []):
            n = int(re.sub(r"\D", "", pid) or 0) if pid.startswith("PAPER") else 10 ** 6
            pat = re.compile(r"\b" + re.escape(pid.replace("PAPER ", "PAPER ")) + r"\b")
            rare = toks(title.get(pid, "")) - common
            score, hits = 0, []
            for q, t in rowtxt.items():
                direct = (k in t) or bool(pat.search(t))
                share = len(rare & toks(t)) >= 2
                if direct:
                    score += 3
                    hits.append(q + ":id")
                elif share:
                    score += 1
                    hits.append(q + ":tok")
            if any(s in DATA for s, _ in secs):
                score += 2
            out.append((-score, n, pid, k, sorted(set(s for s, _ in secs)), hits[:8], title.get(pid, "")[:90]))
    out.sort()
    print("#rank\tscore\tpaper\tkey\tflagged_sections\tlinked_rows\ttitle")
    for i, (s, n, pid, k, secs, hits, t) in enumerate(out[:40], 1):
        print("%d\t%d\t%s\t%s\t%s\t%s\t%s" % (i, -s, pid, k, ",".join(secs), ",".join(hits), t))


if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2)
    main(*sys.argv[1:5])
