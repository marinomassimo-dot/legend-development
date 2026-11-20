"""Mechanical scoring of the NP4G2 arms (recall on K sets, unique finds, held status). Written before the blind verifier runs."""
import csv, re, sys, pathlib, subprocess
N = pathlib.Path(sys.argv[1]); R = N / "run_20261120"
def load(p): return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
def norm(t): return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()
arms = {a: load(R / f"arm_{a}.tsv") for a in "BSM"}
since = "2024-11-20"
arms["Mw"] = [r for r in arms["M"] if (r["date"] or "")[:10] >= since and re.match(r"\d{4}", r["date"] or "")]
Ks = {"K": load(N / "K_record_ids.tsv"), "K_core": load(N / "K_core_record_ids.tsv"), "K_title": load(N / "K_title_record_ids.tsv")}
def hit(k, rows):
    pm = {r["pmid"] for r in rows if r["pmid"]}; tt = {norm(r["title"]) for r in rows}
    return (k["pmid"] and k["pmid"] in pm) or (norm(k["full_title"])[:60] in " | ".join(t[:200] for t in tt) and len(norm(k["full_title"])) > 20 and any(norm(k["full_title"])[:60] in t for t in tt))
print("arm sizes", {a: len(r) for a, r in arms.items()})
for name, K in Ks.items():
    out = {}
    for a, rows in arms.items():
        h = [k["paper"] for k in K if hit(k, rows)]
        out[a] = f"{len(h)}/{len(K)}"
    print(name, out)
core_hits = {a: {k["paper"] for k in Ks["K_core"] if hit(k, rows)} for a, rows in arms.items()}
print("K_core hit by M and not B:", sorted(core_hits["M"] - core_hits["B"]))
print("K_core hit by S and not M:", sorted(core_hits["S"] - core_hits["M"]))
# records outside K (any set) : pmids in K
kp = {k["pmid"] for k in Ks["K"] if k["pmid"]}
reg = open("disease-models/wwox/registries/paper_registry_current.md", encoding="utf-8").read() + open("disease-models/wwox/registries/literature_tracking_log_current.md", encoding="utf-8").read()
def held(r): return bool(r["pmid"]) and r["pmid"] in reg
cand = {}
for a in ("B", "S", "M"):
    for r in arms[a]:
        if r["pmid"] in kp: continue
        if any(hit(k, [r]) for k in Ks["K"]): continue   # preprint or title-matched copy of a K record (PAPER 005, 011, 157 have no PMID or a preprint twin)
        e = cand.setdefault(r["key"], dict(r, arms=set()))
        e["arms"].add(a)
rows = sorted(cand.values(), key=lambda r: r["key"])
with open(N / "candidates_outside_K.tsv", "w", encoding="utf-8") as f:
    f.write("key\tpmid\tdate\tarms\theld_in_registry_or_log\ttitle\n")
    for r in rows: f.write("\t".join([r["key"], r["pmid"], r["date"], "".join(sorted(r["arms"])), "yes" if held(r) else "no", r["title"].replace("\t", " ")]) + "\n")
print("candidates outside K:", len(rows), "of which not held:", sum(1 for r in rows if not held(r)))
for a in ("B", "S", "M"):
    print(a, "outside-K:", sum(1 for r in rows if a in r["arms"]), "not held:", sum(1 for r in rows if a in r["arms"] and not held(r)), "unique to arm (not held):", sum(1 for r in rows if r["arms"] == {a} and not held(r)))
