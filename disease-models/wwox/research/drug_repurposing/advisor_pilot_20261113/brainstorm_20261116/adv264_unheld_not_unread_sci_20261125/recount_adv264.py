"""ADV-264: recount the 'no held artefact' studies of ADV-219 by earlier receipt and by digest.

Print and write-to-folder only; no network. Usage:
  python3 recount_adv264.py <repo root> <held root, the root checkout> <out folder>
First hit: the ADV-219 code path (parsed JSON, key = PMID else DOI else event id).
Second hit: raw ledger lines, key = the event-id study token, counted without ADV-219's functions.
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import collections, csv, hashlib, importlib.util, json, os, random, re

repo, held_root, out = sys.argv[1:4]
A219 = os.path.join(repo, "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/"
                          "brainstorm_20261116/adv219_receipt_label_audit_sci_20261124/labelling_flags_adv219.py")
spec = importlib.util.spec_from_file_location("a219", A219)
a219 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a219)

LEDGER = os.path.join(repo, "disease-models/wwox/registries/fulltext_read_receipts.jsonl")
latest, events = a219.load_ledger(LEDGER)
held_dirs = [os.path.join(held_root, "files/fulltext"), os.path.join(held_root, "files/deepening_downloads")]
idx = a219.index_files(held_dirs)

RANK = ["complete_fulltext_read", "partial_fulltext_read", "queried_not_full_read", "abstract_only",
        "retrieved_not_read"]


def best_depth(evs):
    ds = [e.get("evidence_depth") for e in evs if e.get("evidence_depth") in RANK]
    return min(ds, key=RANK.index) if ds else "other"


# ---- first hit
pop, stats = {}, collections.Counter()
for key, ev in latest.items():
    if ev.get("evidence_depth") != "partial_fulltext_read":
        continue
    stats["primary"] += 1
    files = a219.match_files(key, ev, idx)
    if files:
        stats["held"] += 1
    else:
        stats["not_held"] += 1
        pop[key] = ev
best = collections.Counter(best_depth(evs) for evs in events.values())
latest_c = collections.Counter(ev.get("evidence_depth") for ev in latest.values())

# ---- digest index (misplaced or renamed copies), root checkout folders that hold documents
targets = collections.defaultdict(set)
for key in pop:
    for e in events[key]:
        f = e.get("source_fingerprint")
        if f:
            targets[f].add(key)
found = {}
scanned = 0
for sub in ("files/fulltext", "files/deepening_downloads", "files/supplement", "files/figures", "files/operator_inputs"):
    root = os.path.join(held_root, sub)
    for dp, _, fns in os.walk(root):
        for fn in fns:
            p = os.path.join(dp, fn)
            try:
                if os.path.islink(p) or os.path.getsize(p) == 0:
                    continue
                h = hashlib.sha256()
                with open(p, "rb") as fh:
                    for chunk in iter(lambda: fh.read(1 << 20), b""):
                        h.update(chunk)
                scanned += 1
                d = h.hexdigest()
                if d in targets:
                    found.setdefault(d, []).append(os.path.relpath(p, held_root))
            except OSError:
                pass

# ---- classes
rows = []
for key, ev in sorted(pop.items()):
    evs = events[key]
    complete = any(e.get("evidence_depth") == "complete_fulltext_read" for e in evs)
    cov = {}
    for sec in ("methods", "results"):
        cov[sec] = a219.best_state(evs, sec)
    if complete:
        k = "K1"
    elif cov["methods"] == "read" and cov["results"] == "read":
        k = "K2"
    else:
        k = "K3"
    digs = {e.get("source_fingerprint") for e in evs if e.get("source_fingerprint")}
    hit = sorted({p for d in digs for p in found.get(d, [])})
    manifest = ""
    if re.fullmatch(r"\d{5,9}", key):
        mp = os.path.join(repo, "disease-models/wwox/research/deepdive_manifests/PMID%s.json" % key)
        if os.path.exists(mp):
            try:
                m = json.load(open(mp))
                manifest = "declared_%d" % len(m.get("source_artifacts") or [])
            except Exception:
                manifest = "unreadable"
    kind = "pmid" if re.fullmatch(r"\d{5,9}", key) else "preprint" if key.startswith("PPR") else "doi" if "/" in key else "other"
    rows.append((key, kind, k, best_depth(evs), len(evs), "%s/%s" % (cov["methods"], cov["results"]),
                 "B1" if hit else "", ";".join(hit)[:200], manifest, ev["event_id"]))

os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "population_adv264.tsv"), "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("study_key kind class best_depth n_receipts methods_results_best bytes_by_digest found_at manifest latest_event".split())
    w.writerows([[x if x != "" else "-" for x in r] for r in rows])

kc = collections.Counter(r[2] for r in rows)
bc = collections.Counter(r[6] or "none" for r in rows)
print("first hit: primary %d held %d not_held %d" % (stats["primary"], stats["held"], stats["not_held"]))
print("classes", dict(kc), "bytes by digest", dict(bc), "files hashed", scanned)
print("best-state depth, all ledger studies", dict(best), "total", sum(best.values()))
print("latest-receipt depth, all ledger studies", dict(latest_c))
print("manifest-declared among population", collections.Counter(r[8] or "none" for r in rows).most_common(5))

# ---- second hit: raw lines, event-id key
by_study = collections.defaultdict(list)
for line in open(LEDGER, encoding="utf-8"):
    if '"contemporaneous_receipt"' not in line:
        continue
    d = json.loads(line)
    m = re.match(r"FTR-\d{8}-(.+)-[0-9A-Za-z]+$", d["event_id"])
    by_study[m.group(1) if m else d["event_id"]].append((d["event_at"], d["event_id"], d.get("evidence_depth")))
tok_latest = {k: max(v)[2] for k, v in by_study.items()}
tok_best = collections.Counter(min((x[2] for x in v if x[2] in RANK), key=RANK.index, default="other") for v in by_study.values())
print("second hit: studies by event-id token", len(by_study), "latest partial", sum(1 for v in tok_latest.values() if v == "partial_fulltext_read"))
print("second hit best-state", dict(tok_best))
