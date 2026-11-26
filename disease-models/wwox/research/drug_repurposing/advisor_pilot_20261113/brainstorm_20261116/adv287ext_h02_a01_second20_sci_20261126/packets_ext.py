"""ADV-287 extension: write one packet per set (card id, verbatim sentence, record source, locator, target, endpoint,
context). No reading, class or comment. Both readers get the same packet. Run: python3 -P -E packets_ext.py [set ...]"""
import csv, glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.normpath(os.path.join(HERE, "../../../cards"))
rows = list(csv.DictReader(open(os.path.join(HERE, "sample_final.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE))
packets = {os.path.basename(f).split(".")[0]: json.load(open(f)) for f in glob.glob(os.path.join(CARDS, "*.packet.json"))}
def records(o, path, parent, ppath):
    if isinstance(o, dict):
        for k, v in o.items(): yield from records(v, path + "/" + k, o, path)
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from records(v, f"{path}[{i}]", parent, ppath)
    elif isinstance(o, str): yield o, path, parent
for s in (sys.argv[1:] or ["H02", "A01", "R"]):
    sel = [r for r in rows if r["n"].split("-")[0] == s]
    out = [f"# Packet {s}: card sentences to check ({len(sel)}). Card files: disease-models/wwox/research/drug_repurposing/cards/<card>.packet.json", ""]
    gone = []
    for r in sel:
        hits = [(p, rec) for t, p, rec in records(packets[r["card"]], "", None, "") if r["sentence"] in t]
        if not hits: gone.append(r["n"]); continue
        out.append(f"## {r['n']} (card {r['card']})")
        out.append(f"SENTENCE: {r['sentence']}")
        for p, rec in hits[:2]:
            out.append(f"printed at: {p}")
            if isinstance(rec, dict):
                for k in ("id", "target_id", "source", "locator", "endpoint", "direction", "context", "reading_depth"):
                    if rec.get(k): out.append(f"  record {k}: {json.dumps(rec[k], ensure_ascii=False)[:500]}")
        out.append("")
    open(os.path.join(HERE, f"PACKET_{s}.md"), "w").write("\n".join(out) + "\n")
    print(s, "written", len(sel) - len(gone), "gone", gone)
