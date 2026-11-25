"""ADV-272 step 1: rank the not-held partials (held_studies.py --rows not-held) by consumer units, ADV-265 method.

Usage: python3 rank_not_held_adv272.py <repo root> <root checkout> <not-held json> <out folder>
Print and write-to-folder only; no network. Rule frozen in PREREG_ADV272_SCI_20261125.md.
"""
import sys

if len(sys.argv) != 5 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import collections, csv, glob, importlib.util, os, re, subprocess

repo, held_root, nh_json, out = sys.argv[1:5]
import json
A219 = os.path.join(repo, "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/"
                          "adv219_receipt_label_audit_sci_20261124/labelling_flags_adv219.py")
spec = importlib.util.spec_from_file_location("a219", A219)
a219 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a219)
W = os.path.join(repo, "disease-models/wwox")
latest, events = a219.load_ledger(os.path.join(W, "registries/fulltext_read_receipts.jsonl"))
idx = a219.index_files([os.path.join(held_root, "files/fulltext"), os.path.join(held_root, "files/deepening_downloads")])

# ---- population: studies whose latest receipt is partial and that are not held (HE's held_studies.py)
nh = json.load(open(nh_json))
pop = {k: [""] for k, v in nh["rows"].items() if v["held"] == "no" and k in latest and latest[k].get("evidence_depth") == "partial_fulltext_read"}
print("not-held rows in json", len(nh["rows"]), "population used", len(pop))

# ---- registry ids
ids = collections.defaultdict(set)
for fn in ("registries/paper_registry_current.md", "registries/literature_tracking_log_current.md"):
    for unit in re.split(r"(?m)^(?=## )", open(os.path.join(W, fn), errors="replace").read()):
        head = re.match(r"## (PAPER \d+)", unit)  # amendment 1: no CORPUS or LIT ids
        if not head:
            continue
        own = set()
        for line in unit.split("\n"):
            if "Identifier" in line:
                own |= set(re.findall(r"(?:PMID\W{0,4}|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{6,8})", line))
                own |= set(re.findall(r"(10\.\d{4,9}/[^\s)\]>*`|]+)", line))
        for p in own:
            ids[p.rstrip(".,;")].add(head.group(1))

SURF = [("claim", "registries/claim_registry_current.md"), ("model", "registries/working_model_current.md"),
        ("model", "disease_model.md"), ("lead", "research/discovery_ledger_current.md"),
        ("hypothesis", "research/therapeutic_hypotheses_ledger_current.md"),
        ("card", "research/drug_repurposing/cards*/*.json"),
        ("portfolio", "research/drug_repurposing/research_portfolio.tsv"),
        ("ranking", "research/drug_repurposing/ranking*/investigations*.tsv")]
units = []
for kind, pat in SURF:
    for f in sorted(glob.glob(os.path.join(W, pat))):
        t = open(f, errors="replace").read()
        rel = os.path.relpath(f, W)
        if f.endswith(".json"):
            units.append((kind, rel, os.path.basename(f).split("_")[0], t))
        elif f.endswith(".tsv"):
            units += [(kind, rel, line.split("\t")[0], line) for line in t.split("\n")[1:] if line]
        else:
            units += [(kind, rel, p.split("\n")[0].lstrip("# ")[:60] or "preamble", p) for p in re.split(r"(?m)^(?=#{2,4} )", t)]
files_by_kind = {}
for kind, pat in SURF:
    files_by_kind.setdefault(kind, []).append("disease-models/wwox/" + pat)
all_paths = sorted({"disease-models/wwox/" + p for _, p in SURF})


def terms_for(key, units_level=True):
    t = {key} | (ids.get(key, set()) if units_level else set())
    return {x for x in t if x}


def rx_for(key):
    alts = []
    for t in sorted(terms_for(key), key=len, reverse=True):
        if re.fullmatch(r"\d{5,9}", t):
            alts.append(r"(?<![\d.])%s(?!\d)" % t)
        elif t.startswith(("PAPER", "CORPUS", "LIT")):
            alts.append(re.escape(t).replace(r"\ ", r"[ _#]?") + r"(?!\d)")
        else:
            alts.append(re.escape(t))
    return re.compile("|".join(alts), re.I)


UNREAD = {"not_read", "captions_only"}
CLASSES = ["discussion", "figures", "tables", "supplementary", "limitations"]
rows = []
for key in sorted(pop):
    evs = events[key]
    states = {s: a219.best_state(evs, s) for s in CLASSES + ["methods", "results"]}
    unread = [s for s in CLASSES if states[s] in UNREAD]
    rx = rx_for(key)
    r2 = sorted({"%s:%s:%s" % (kind, rel.split("/")[-1], name) for kind, rel, name, body in units if rx.search(body)})
    terms = sorted(terms_for(key, units_level=False))  # route 1: PMID and DOI only
    cmd = ["git", "-C", repo, "grep", "-l", "-I", "-i", "-w", "-F"] + sum([["-e", t] for t in terms], []) + ["--"] + all_paths
    res = subprocess.run(cmd, capture_output=True, text=True)
    r1 = sorted({l.split("/")[-1] for l in res.stdout.split("\n") if l})
    kinds = collections.Counter(u.split(":")[0] for u in r2)
    rows.append((key, len(r2), len(r1), ";".join(unread) or "-", len(unread),
                 sum(1 for s in unread if s in ("tables", "figures", "supplementary")), 1 if "discussion" in unread else 0,
                 ",".join("%s%d" % (k, v) for k, v in sorted(kinds.items())) or "-", "; ".join(r2)[:300] or "-",
                 pop[key][0].replace(held_root + "/", "")[:120], latest[key]["event_id"]))
rows.sort(key=lambda r: (-r[1], -r[2], r[0]))
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "ranking_adv272.tsv"), "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("study_key consumers_route2 files_route1 unread_classes n_unread n_data_unread discussion_unread kinds units held_file latest_event".split())
    w.writerows(rows)
elig = rows
print("population", len(pop), "consumers>0", sum(1 for r in rows if r[1] > 0))
disagree = [r for r in rows if (r[1] > 0) != (r[2] > 0)]
print("route disagreement (one route zero, other not):", len(disagree), [d[0] for d in disagree[:10]])
for r in elig[:30]:
    print(r[0], "c2=%d c1=%d" % (r[1], r[2]), "unread:", r[3], "|", r[7], "|", r[9][-60:])
