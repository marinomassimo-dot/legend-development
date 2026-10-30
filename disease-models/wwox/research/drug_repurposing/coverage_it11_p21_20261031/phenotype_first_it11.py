#!/usr/bin/env python3
"""IT11 P2.1: three small extensions of the IT10 phenotype-first entry, written as a wrapper (nothing in generation_it10_p1_20261031 is edited).

  phenotype_first_it11.py run --out FILE      # writes the extended phenotype-first table (one row per lead)
  phenotype_first_it11.py --help

What the wrapper adds to dispose_it10.phenotype_first(v3_dir, dr, extra):
  1. graph_status read from the FULL seed-specific list (v3_seed_specific_all_nulls.tsv), not from the truncated candidate tables (top 50 opposes / 25 mimics per set). In IT10 the
     truncated tables made lithium look 'scored, never seed-specific'; the full list holds all four lithium salt families as seed-specific mimics in Q6 expression (all three nulls).
  2. a structural reachability code per lead (TARGETS_NOT_IN_NETWORK, TARGETS_SINK_ONLY, TARGETS_HAVE_OUT_EDGES, NO_SIGNED_TARGET): a target with no outgoing edge in the loaded
     network cannot receive an indirect score whatever the seeds are.
  3. the context of the WWOX result (system, genotype, species, endpoint, direction, depth, receipt) from the card packets, so that a candidate found by a target-class search can be
     compared against the SAME context, and class_mates(): other catalogue families that share a signed target and its sign with the lead. Class mates are a search list, not evidence:
     the lead's WWOX result is NOT transferred to them (different molecule, different exposure, different selectivity).
A compatible action is not a predicted benefit. Not medical advice.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, glob, gzip, importlib.util, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
IT10 = DR / "generation_it10_p1_20261031"
V3R = DR / "generation_it9_p2_20261030" / "v3" / "results"


def _load(name, path, argv):
    saved = list(sys.argv); sys.argv = list(argv)
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m)
    finally:
        sys.argv = saved
    return m


dz = _load("dispose_it10_w", IT10 / "dispose_it10.py", ("x", "run"))
v4 = _load("seed_engine_v4_w", IT10 / "engine_v4" / "seed_engine_v4.py", ("x", "selftest"))


def seed_specific_full(results_dir):
    """normalised family name -> sorted list of 'Q/arm' from the untruncated seed-specific list."""
    out = {}
    for r in dz.rd(Path(results_dir) / "v3_seed_specific_all_nulls.tsv"):
        out.setdefault(dz.norm(r["name"]), set()).add(f"{r['question']}/{r['arm']}")
    return out


def reachability(targets, edges):
    """structural code for a set of signed targets under a list of typed edges (source, target, sign, mode, ...)."""
    if not targets:
        return "NO_SIGNED_TARGET"
    out_d = {e[0] for e in edges}; in_d = {e[1] for e in edges}
    if not any(t in out_d or t in in_d for t in targets):
        return "TARGETS_NOT_IN_NETWORK"
    return "TARGETS_HAVE_OUT_EDGES" if any(t in out_d for t in targets) else "TARGETS_SINK_ONLY"


def class_mates(lead_targets, action_rows, exclude_names=(), top=10):
    """families (other than the lead's own name twins) sharing >=1 signed target WITH THE SAME SIGN; lead_targets = {gene: sign}. Search list only."""
    ex = {dz.norm(x) for x in exclude_names}; by = {}
    for r in action_rows:
        s = lead_targets.get(r["target_symbol"])
        if s is not None and float(r["mean_sign"]) * s > 0:
            by.setdefault(r["family_id"], set()).add(r["target_symbol"])
    return sorted(((f, sorted(g)) for f, g in by.items()), key=lambda x: (-len(x[1]), x[0]))[:top], ex


def contexts(dr):
    """assertion id -> context row, from the card packets (drug_assertions entries)."""
    out = {}
    def walk(x):
        if isinstance(x, dict):
            if x.get("id") and "direction" in x and "context" in x:
                c = x["context"]
                out[x["id"]] = dict(system=c.get("disease_id", ""), genotype=c.get("genotype", ""), species=c.get("species", ""), endpoint=x.get("endpoint", ""),
                                    direction=x.get("direction", ""), depth=x.get("reading_depth", ""), receipt=x.get("receipt", ""))
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    for f in glob.glob(str(dr / "cards" / "*.packet.json")) + glob.glob(str(dr / "cards_early" / "*.packet.json")):
        with open(f, encoding="utf-8") as fh:
            walk(json.load(fh))
    return out


def extended(v3_dir=IT10 / "results_v4", dr=DR, edges=None):
    rows = dz.phenotype_first(v3_dir, dr, None)
    full = seed_specific_full(v3_dir)
    me = {r["unit_id"]: r for r in dz.rd(dr / "ranking_it8_p9_20261029" / "member_evidence.tsv") if r["tested_in_wwox_system"].lower() == "yes"}
    ctx = contexts(dr)
    edges = edges if edges is not None else v4.read_edges4()
    acts = list(csv.DictReader(gzip.open(V3R / "actions" / "family_actions.tsv.gz", "rt"), delimiter="\t"))
    fnames = {m["family_id"]: dz.norm(m["name"]) for m in csv.DictReader(gzip.open(V3R / "actions" / "family_meta.tsv.gz", "rt"), delimiter="\t")}
    for r in rows:
        toks = [dz.norm(t) for t in dz.member_tokens(r["intervention"])]
        hit = sorted({s for n, ss in full.items() if any(n == t or n.startswith(t) for t in toks) for s in ss})
        r["seed_specific_full_list"] = ";".join(hit)
        if hit and not r["graph_status"].startswith("IN_SEED_SPECIFIC_ARM"):
            r["graph_status_it11"] = "IN_SEED_SPECIFIC_ARM:" + ";".join(hit)      # same label the patched dispose_it10.phenotype_first gives (proposed_patch_dispose_it10.diff)
        else:
            r["graph_status_it11"] = r["graph_status"]
        fams = [f for f, n in fnames.items() if any(n == t or (len(t) >= 6 and n.startswith(t)) for t in toks)]     # short aliases (apv) match exactly: APVO-436 is not d-APV
        tg = {}
        for a in acts:
            if a["family_id"] in fams:
                tg[a["target_symbol"]] = float(a["mean_sign"])
        r["signed_targets"] = ";".join(sorted(tg))
        r["reachability"] = reachability(set(tg), edges) if r["member_type"] in ("molecule", "tool_compound") else "NOT_APPLICABLE"
        for k in ("system", "genotype", "species", "endpoint", "direction", "depth", "receipt"):
            vals = sorted({ctx[i][k] for i in (me[r["unit_id"]]["assertion_ids"].split("; ") if r["unit_id"] in me else []) if i in ctx and ctx[i][k]})
            r["ctx_" + k] = " || ".join(vals)[:300]
        mates, _ = class_mates(tg, acts, [r["intervention"]]) if tg else ([], None)
        own = set(fams)
        r["class_mates_top"] = "; ".join(f"{f[8:]}[{','.join(g)}]" for f, g in mates if f not in own)[:400]
    return rows


if __name__ == "__main__":
    out = Path(sys.argv[sys.argv.index("--out") + 1])
    rows = extended()
    cols = sorted({k for r in rows for k in r})
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    for r in rows:
        print(r["intervention"][:30], "|", r["graph_status"], "->", r["graph_status_it11"], "|", r["reachability"])
