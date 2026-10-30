#!/usr/bin/env python3
"""Convert the IT9 P1 question-specific seed table (seeds.tsv + process_ids.tsv + hgnc_check.tsv) into engine seed tables, one per question and readout level.

Rules (all counted in the manifest; nothing is dropped silently):
  * only rows with usable_for_generation = yes AND reserved_for_evaluation = no; the engine refuses reserved/held-out classes anyway;
  * gene or protein entities with an HGNC symbol become gene seeds; process rows enter only when process_ids.tsv lists member symbols (SET:... and GO:0004739; members are taken as declared by P1 and audited against the graph at run time);
    GO terms, ChEBI, STATE: and wildcard sets without a member list have no gene-level representation and are COUNTED, not used;
  * direction 'unchanged' is not a seed (a null observation) and is counted; 'uncertain' stays uncertain (conditional arms); P1 gives no magnitude, so level = 1.0 for every
    gene (a process spreads 1/sqrt(n) over its members) - equal weights, stated, not a finding;
  * gene rows typed 'pathology' (cell counts, area fractions) are not gene-level seeds and are counted; phospho-site rows are written with direction uncertain (a phospho site is not kinase activity); guard_tag is carried per set (a tag may not be lost: asserted);
  * several rows on one gene in one set: all same direction -> defined; opposing or any uncertain -> uncertain (a conflict is never resolved by summing);
  * readout levels are never merged: expression, protein and phospho rows go to separate sets; function/pathology/activity rows on genes are separate sets too;
  * non-human rows (gene or every member of a set) need an HGNC ortholog link in hgnc_check.tsv (mgd_id_ortholog_link) and are written with that mapping; rows without it are dropped and counted; fly rows (tier D) are dropped.

  p1_adapter.py --p1 DIR --out DIR [--tiers A,B]
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, hashlib, json
from pathlib import Path

ap = argparse.ArgumentParser(); ap.add_argument("--p1", required=True); ap.add_argument("--out", required=True); ap.add_argument("--tiers", default="A,B")
a = ap.parse_args()
P1, OUT = Path(a.p1), Path(a.out); OUT.mkdir(parents=True, exist_ok=True)
tiers = set(a.tiers.split(","))
rd = lambda p: list(csv.DictReader(open(p, encoding="utf-8", newline=""), delimiter="\t"))
seeds = rd(P1 / "seeds.tsv")
proc = {r["process_id"]: r for r in rd(P1 / "process_ids.tsv")}
hg = {r["symbol"].upper(): r for r in rd(P1 / "hgnc_check.tsv")}
sha = hashlib.sha256((P1 / "seeds.tsv").read_bytes()).hexdigest()
COLS = ["seed_id", "gene", "kind", "members", "direction", "level", "direction_status", "readout_level", "evidence_class", "species", "ortholog_map", "source_ref", "note", "guard_tag"]
EVCLASS = {"expression": "transcript_contrast", "protein": "protein_state", "phospho": "protein_state", "activity": "activity_state", "function": "phenotype_state", "pathology": "phenotype_state"}
counts = collections.defaultdict(collections.Counter)
groups = collections.defaultdict(lambda: collections.defaultdict(list))   # set -> key -> rows
for r in seeds:
    q = r["question_id"]
    if r["usable_for_generation"] != "yes" or r["reserved_for_evaluation"] != "no":
        counts[q]["not_usable_or_reserved"] += 1; continue
    counts[q]["usable_rows"] += 1
    if r["context_tier"] not in tiers:
        counts[q]["tier_not_selected"] += 1; continue
    if r["direction"] == "unchanged":
        counts[q]["unchanged_null_observation_not_a_seed"] += 1; continue
    if r["level"] == "pathology" and r["entity_type"] in ("gene", "protein") and not r["process_id"]:
        counts[q]["pathology_level_gene_row_not_a_gene_seed"] += 1; continue
    sp = r["species_observed"]
    sym = r["entity_symbol"].strip().upper() if r["entity_symbol"] else ""
    pid = r["process_id"].strip()
    members = []
    if pid:
        mem = proc.get(pid, {}).get("members_hgnc", "")
        if pid.startswith(("SET:", "GO:")) and mem and "*" not in mem and "(" not in mem:
            members = [x.strip().upper() for x in mem.split(",") if x.strip() and not x.strip().startswith("(")]
            members = [x.split(" ")[0] for x in members]
        if not members:
            counts[q]["process_or_state_without_gene_members_not_representable"] += 1; continue
        key = pid; kind = "process"
    else:
        if r["entity_type"] in ("state",) or not sym or sym.startswith(("STATE:", "GO:", "CHEBI:", "SET:")):
            counts[q]["state_or_nongene_not_representable"] += 1; continue
        key = sym; kind = "gene"
    names = members if kind == "process" else [sym]
    bad = [x for x in (names if kind == "gene" else []) if x not in hg or hg[x]["status"] != "Approved"]
    if bad:
        counts[q]["symbol_not_hgnc_approved_dropped"] += 1; continue
    orth = ""
    if sp != "human":
        if sp == "fly" or r["context_tier"] == "D":
            counts[q]["fly_or_tier_D_dropped"] += 1; continue
        links = [hg[x]["mgd_id_ortholog_link"] if x in hg else "" for x in names]
        if not all(links):
            counts[q]["no_hgnc_ortholog_link_dropped"] += 1; continue
        orth = "HGNC approved symbol with HGNC mgd ortholog link (" + ";".join(sorted(set(links))[:3]) + "); 1:1 assumed from a single link"
    lvl = r["level"]
    setname = f"{q}_{lvl}_tiers{''.join(sorted(tiers))}"
    groups[setname][(kind, key)].append((r, sp, orth, names))
    counts[q]["rows_placed"] += 1
manifest = []
for sn, g in sorted(groups.items()):
    rows = []
    for (kind, key), lst in sorted(g.items()):
        dirs = {r["direction"] for r, *_ in lst}
        status = "defined" if len(dirs) == 1 and dirs <= {"up", "down"} else "uncertain"
        phospho = any(r["level"] == "phospho" for r, *_ in lst)
        if phospho:
            status = "uncertain"   # a phospho-site change is not a change in kinase activity (Amendment 4)
        tags = sorted({t for r, *_ in lst for t in (r.get("guard_tag") or "").split(";") if t})
        d = dirs.pop() if status == "defined" else "uncertain"
        r0, sp0, orth0, names0 = lst[0]
        sps = sorted({x[1] for x in lst})
        orth = orth0 if any(x[2] for x in lst) else ""
        rows.append(dict(seed_id=f"{sn}:{key}", gene=key if kind == "gene" else key, kind=kind, members=";".join(names0) if kind == "process" else "", direction=d, level="1.0",
                         direction_status=status, readout_level=r0["level"],
                         evidence_class=EVCLASS[r0["level"]], species="human" if sps == ["human"] else "/".join(sps), ortholog_map=orth,
                         source_ref=";".join(sorted({x[0]["seed_id"] for x in lst})), note=f"directions seen: {sorted({x[0]['direction'] for x in lst})}; tiers {sorted({x[0]['context_tier'] for x in lst})}; P1 gives no magnitude (equal weight)" + ("; phospho-site row: direction treated as uncertain for activity" if phospho else ""), guard_tag=";".join(tags)))
    placed_tags = {t for (_, _), lst in g.items() for r, *_ in lst for t in (r.get("guard_tag") or "").split(";") if t}
    out_tags = {t for x in rows for t in x["guard_tag"].split(";") if t}
    assert placed_tags == out_tags, ("guard tag lost", sn, placed_tags, out_tags)
    with open(OUT / f"{sn}.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", lineterminator="\n"); w.writeheader(); [w.writerow(x) for x in rows]
    manifest.append(dict(set=sn, seed_rows=len(rows), defined=sum(1 for x in rows if x["direction_status"] == "defined"), uncertain=sum(1 for x in rows if x["direction_status"] == "uncertain"),
                         gene_units=sum(len(x["members"].split(";")) if x["kind"] == "process" else 1 for x in rows)))
with open(OUT / "manifest.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["set", "seed_rows", "defined", "uncertain", "gene_units"], delimiter="\t", lineterminator="\n"); w.writeheader(); [w.writerow(x) for x in manifest]
(OUT / "adapter_counts.json").write_text(json.dumps({"p1_seeds_sha256": sha, "tiers": sorted(tiers), "per_question": {k: dict(v) for k, v in sorted(counts.items())}}, indent=1) + "\n")
print(json.dumps({"p1_seeds_sha256": sha, "sets": manifest}, indent=1))
