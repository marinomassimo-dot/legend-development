"""ADV-264 extension (declared post hoc): bytes held for the studies whose best receipt is complete, and the one-study
difference between the two counts. Usage: python3 extension_complete_bytes_adv264.py <repo root> <root checkout> <out folder>"""
import sys
if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import collections, csv, hashlib, importlib.util, json, os, re
repo, held_root, out = sys.argv[1:4]
A = os.path.join(repo, "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv219_receipt_label_audit_sci_20261124/labelling_flags_adv219.py")
spec = importlib.util.spec_from_file_location("a219", A); a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
L = os.path.join(repo, "disease-models/wwox/registries/fulltext_read_receipts.jsonl")
latest, events = a.load_ledger(L)
idx = a.index_files([os.path.join(held_root, "files/fulltext"), os.path.join(held_root, "files/deepening_downloads")])
# difference between the two hits
tok = collections.defaultdict(list)
for line in open(L):
    if '"contemporaneous_receipt"' not in line: continue
    d = json.loads(line); m = re.match(r"FTR-\d{8}-(.+)-[0-9A-Za-z]+$", d["event_id"])
    tok[m.group(1)].append((d["event_at"], d["event_id"], d.get("evidence_depth"), (d.get("study_id") or {})))
p1 = {k for k, e in latest.items() if e.get("evidence_depth") == "partial_fulltext_read"}
p2 = {k for k, v in tok.items() if max(v)[2] == "partial_fulltext_read"}
print("only in first hit (key rule pmid/doi):", sorted(p1 - p2)[:5], "only in second hit (event-id token):", sorted(p2 - p1)[:5])
for k in sorted(p1 ^ p2)[:3]:
    print(k, [ (e[1], e[2], e[3]) for e in sorted(tok.get(k, []))][-3:])
# complete best-state, bytes
comp = [k for k, evs in events.items() if any(e.get("evidence_depth") == "complete_fulltext_read" for e in evs)]
fp = collections.defaultdict(set)
for k in comp:
    for e in events[k]:
        if e.get("source_fingerprint"): fp[e["source_fingerprint"]].add(k)
digest_hit = {}
for sub in ("files/fulltext", "files/deepening_downloads", "files/supplement", "files/operator_inputs"):
    for dp, _, fns in os.walk(os.path.join(held_root, sub)):
        for fn in fns:
            p = os.path.join(dp, fn)
            try:
                if os.path.islink(p) or not os.path.getsize(p): continue
                h = hashlib.sha256(open(p, "rb").read()).hexdigest()
                if h in fp:
                    for k in fp[h]: digest_hit.setdefault(k, p)
            except OSError: pass
rows = []
for k in sorted(comp):
    name = bool(a.match_files(k, latest[k], idx))
    rows.append((k, "name" if name else "", "digest" if k in digest_hit else "", len(events[k])))
cnt = collections.Counter(("bytes" if (r[1] or r[2]) else "none") for r in rows)
print("best-state complete studies", len(comp), dict(cnt), "by name", sum(1 for r in rows if r[1]), "by digest only", sum(1 for r in rows if r[2] and not r[1]))
with open(os.path.join(out, "complete_best_state_bytes_adv264.tsv"), "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n"); w.writerow("study_key bytes_by_name bytes_by_digest n_receipts".split())
    w.writerows([[x if x != "" else "-" for x in r] for r in rows])
