#!/usr/bin/env python3
"""Lane A2 package 2 (ADV-034): mine the Disease Mechanisms KB (kb.zip of a public release) for NMDA-receptor antagonists and scan every entry's pathophysiology graph for parentless nodes.
Usage: mine.py KB_ZIP OUT_DIR. Needs PyYAML. Reads the zip with zipfile only (nothing is extracted)."""
import sys, re, zipfile, json, csv, collections, statistics
import yaml
if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); sys.exit(0 if len(sys.argv) == 3 else 2)
zpath, out = sys.argv[1], sys.argv[2]
TERMS = {
 "ketamine": r"\b(?:es)?ketamine\b", "memantine": r"\bmemantine\b", "dextromethorphan": r"\bdextromethorphan\b|\bdextrorphan\b",
 "magnesium": r"\bmagnesium\b|\bMgSO4\b", "amantadine": r"\bamantadine\b", "felbamate": r"\bfelbamate\b",
 "NMDAR antagonist (class)": r"NMDA[R]?\s*(?:receptor\s*)?(?:antagonist|blocker|inhibitor)|NMDAR\s*(?:antagonist|blocker)", "nitrous oxide": r"\bnitrous oxide\b",
}
CT = {k: re.compile(v, re.I) for k, v in TERMS.items()}
EPI = re.compile(r"epilep|seizure|encephalopath|spasm|convuls", re.I)
z = zipfile.ZipFile(zpath)
files = sorted(n for n in z.namelist() if n.startswith("kb/disorders/") and n.endswith(".yaml"))
hits, orphan_rows, parse_fail = [], [], []
def walk(o, path, ctx, found):
    if isinstance(o, dict):
        txt = " ".join(str(o.get(k, "")) for k in ("name", "snippet", "explanation", "description", "preferred_term") if isinstance(o.get(k, ""), (str, int, float)))
        if "snippet" in o or "explanation" in o or ("name" in o and path.startswith("treatments")):
            for term, rx in CT.items():
                if rx.search(txt):
                    found.append({"term": term, "section": path.split("/")[0], "kind": "evidence_item" if ("snippet" in o or "explanation" in o) else "treatment_entry",
                                  "grade": o.get("evidence_source", "") or ctx.get("grade", ""), "pmid": re.sub(r"\D", "", str(o.get("reference", ""))) or ctx.get("pmid", ""),
                                  "supports": o.get("supports", ""), "text": re.sub(r"\s+", " ", str(o.get("snippet") or o.get("name") or o.get("explanation") or ""))[:160]})
        for k, v in o.items():
            c2 = dict(ctx)
            if k == "evidence_source": c2["grade"] = v
            walk(v, f"{path}/{k}" if path else k, c2, found)
    elif isinstance(o, list):
        for v in o: walk(v, path, ctx, found)
for n in files:
    try:
        d = yaml.safe_load(z.read(n).decode("utf-8", "ignore"))
    except Exception as e:
        parse_fail.append(n); continue
    if not isinstance(d, dict): parse_fail.append(n); continue
    name = d.get("name", n); desc = str(d.get("description", ""))
    parents = d.get("parents") or []
    epi = bool(EPI.search(name + " " + desc + " " + " ".join(map(str, parents))))
    found = []
    walk(d, "", {}, found)
    for f in found:
        hits.append({"entry": name, "file": n.split("/")[-1], "epilepsy_related": epi, **f})
    # graph scan
    pp = d.get("pathophysiology") or []
    names = [p.get("name") for p in pp if isinstance(p, dict) and p.get("name")]
    if names:
        edges = [(p["name"], x.get("target") if isinstance(x, dict) else x) for p in pp if isinstance(p, dict) and p.get("name") for x in (p.get("downstream") or [])]
        inc = collections.Counter(b for a, b in edges if b in names)
        parentless = [x for x in names if inc[x] == 0]
        adj = collections.defaultdict(list)
        for a, b in edges:
            if b in names: adj[a].append(b)
        seen, st = {names[0]}, [names[0]]
        while st:
            x = st.pop()
            for y in adj[x]:
                if y not in seen: seen.add(y); st.append(y)
        orphan_rows.append({"entry": name, "nodes": len(names), "edges": len(edges), "parentless_beyond_first": len([x for x in parentless if x != names[0]]), "reachable_from_first": len(seen), "epilepsy_related": epi})
    else:
        orphan_rows.append({"entry": name, "nodes": 0, "edges": 0, "parentless_beyond_first": 0, "reachable_from_first": 0, "epilepsy_related": epi})
import os
os.makedirs(out, exist_ok=True)
with open(f"{out}/nmdar_antagonist_items.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["entry", "epilepsy_related", "term", "section", "kind", "grade", "pmid", "supports", "text"])
    for h in sorted(hits, key=lambda h: (h["term"], h["entry"])):
        w.writerow([h["entry"], h["epilepsy_related"], h["term"], h["section"], h["kind"], h["grade"], h["pmid"], h["supports"], h["text"]])
with open(f"{out}/graph_scan.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["entry", "nodes", "edges", "parentless_beyond_first", "reachable_from_first", "epilepsy_related"])
    for r in orphan_rows: w.writerow([r["entry"], r["nodes"], r["edges"], r["parentless_beyond_first"], r["reachable_from_first"], r["epilepsy_related"]])
summary = {"disorder_files": len(files), "parse_failures": parse_fail}
summary["hits"] = len(hits); summary["entries_with_hits"] = len({h["file"] for h in hits})
by = collections.defaultdict(lambda: {"items": 0, "entries": set(), "epilepsy_entries": set(), "grades": collections.Counter()})
for h in hits:
    b = by[h["term"]]; b["items"] += 1; b["entries"].add(h["file"]); b["grades"][h["grade"] or "none"] += 1
    if h["epilepsy_related"]: b["epilepsy_entries"].add(h["file"])
summary["by_term"] = {k: {"items": v["items"], "entries": len(v["entries"]), "epilepsy_entries": len(v["epilepsy_entries"]), "grades": dict(v["grades"])} for k, v in by.items()}
g = [r for r in orphan_rows if r["nodes"]]
summary["graph"] = {"entries_with_pathophysiology": len(g), "entries_without": len(orphan_rows) - len(g),
    "entries_with_parentless_beyond_first": sum(1 for r in g if r["parentless_beyond_first"]), "median_nodes": statistics.median(r["nodes"] for r in g),
    "entries_not_all_reachable_from_first": sum(1 for r in g if r["reachable_from_first"] < r["nodes"]),
    "share_nodes_reachable_median": round(statistics.median(r["reachable_from_first"] / r["nodes"] for r in g), 3)}
json.dump(summary, open(f"{out}/summary.json", "w"), indent=1)
print(json.dumps(summary, indent=1))
