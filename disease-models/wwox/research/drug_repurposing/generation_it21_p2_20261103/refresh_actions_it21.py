#!/usr/bin/env python3
"""IT21 P2 step B1: rebuild the compound-side action table of the generator with the IT19/IT20 guards, through the EXISTING builder.

  refresh_actions_it21.py run --out DIR [--guards on|off] [--catalog PATH]
  refresh_actions_it21.py diff --old DIR --new DIR --out FILE.tsv

Problem. The v3/v4 generation engine reads `family_actions.tsv.gz`, built in IT9 by `generation_it9_p2_20261030/v3/build_actions_v3.py` from
`usable_census.row_usability`. That function predates the guards the active search layer (`framework/scripts/repurposing_search.py`) gained in
IT19/IT20: the group-transfer guard (a ChEMBL mechanism curated on a protein FAMILY / COMPLEX GROUP does not resolve its single action to one
member gene), the republished-claim guard (a DGIdb row that is a copy of a ChEMBL record, carrying neither the record id nor its level), and the
documented-level waiver (`target_level_documented:` rows of coverage/source_artefacts.tsv, e.g. bepridil on CACNA1H). A generator that ignores
them re-introduces, as apparent novelty, exactly the directions those guards withdrew.

This file is a THIN ADAPTER, not a second builder: it loads the v3 builder unchanged and wraps `row_usability` with calls to the search-layer
functions themselves (`group_transfer_unresolved`, `claim_provenance`, `republished_transfer_unresolved`, `documented_level_waiver`). The rule is
therefore the search layer's, in one place. What the guards withhold keeps its association (`family_targets_any`) and loses only its sign
(unknown is not negative); a waived (family, gene) pair is added back with the flag DOCUMENTED_LEVEL_WAIVER and is specific to that gene.
`--guards off` runs the unchanged builder (the control that separates catalogue drift since IT9 from the effect of the guards).
Offline and deterministic; standard library only.
"""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help")):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, contextlib, csv, gzip, importlib.util, io, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = HERE.parents[4]
V3 = DR / "generation_it9_p2_20261030" / "v3"
sys.path.insert(0, str(REPO / "framework/scripts"))

ABSTENTION_CLASSES = ("group_record_mostly_outside_module_targets", "republished_claim_level_not_carried", "action_conflict_or_glue_modulator")

# P8-fix finding 1 (IT21 verifier C1). The search layer has no guard for these two cases, so they are added HERE, in the one adapter, as pure functions:
#  * a family whose records disagree on the action at one gene (INHIBITOR on one salt record, MODULATOR on another; or up against down) has no sign;
#  * a MODULATOR action is a glue/recruiter-type statement (lenalidomide-class: the drug recruits neosubstrates to CRBN, it does not lower CRBN activity),
#    and the CRBN/DCAF15-type substrate receptors carry no sign for any compound: an 'inhibitor' sign there predicts the wrong direction on the substrate.
GLUE_RECEPTOR_GENES = frozenset({"CRBN", "DCAF15"})
MODULATOR_ACTIONS = frozenset({"MODULATOR"})


def reason_class(reason):
    for c in ABSTENTION_CLASSES:
        if reason.startswith(c):
            return c
    return ABSTENTION_CLASSES[0]


def row_genes(t):
    return [g for g in ((t.get("gene_symbols") or []) if (t.get("source") or "").startswith("ChEMBL") else [t.get("gene") or ""]) if g]


def family_members(idx, e):
    """The catalogue records of e's family (the record itself when the index carries no family map)."""
    fam, mem = getattr(idx, "family", None), getattr(idx, "members", None)
    return (mem.get(fam[e["id"]], [e]) if fam and mem and e["id"] in fam else [e])


def conflict_or_glue(rs, members, t):
    """'' or the reason a signed row must lose its sign: the family's own records disagree at one of the row's genes (up v down, or a ChEMBL MODULATOR
    statement beside a signed one), or the gene is a glue substrate receptor. Pure on the catalogue entries of ONE family."""
    genes = {g.upper() for g in row_genes(t)}
    if genes & GLUE_RECEPTOR_GENES:
        return "action_conflict_or_glue_modulator: sign at a glue substrate receptor (" + ";".join(sorted(genes & GLUE_RECEPTOR_GENES)) + ")"
    cats = collections.defaultdict(set)
    for m in members:
        for t2 in m["targets"]:
            if not (t2.get("source") or "").startswith("ChEMBL"):
                continue                       # only the curated mechanisms disagree meaningfully; a DGIdb 'modulator' beside a ChEMBL inhibitor is source noise
            raw = t2.get("action_type") or ""
            c = rs.action_direction(raw)
            if raw.strip().upper() in MODULATOR_ACTIONS:
                c = "modulator"
            if c == "unresolved":
                continue
            for g in {x.upper() for x in row_genes(t2)} & genes:
                cats[g].add(c)
    for g, c in sorted(cats.items()):
        if {"up", "down"} <= c or ("modulator" in c and c & {"up", "down"}):
            return f"action_conflict_or_glue_modulator: records of the family disagree on the action at {g} ({'/'.join(sorted(c))})"
    return ""


def make_wrapper(orig, module_symbols, log):
    """Wrap usable_census.row_usability: withhold the sign when the search layer would abstain, record why, remember the waived genes."""
    def row_usability(rs, idx, e, t):
        u = orig(rs, idx, e, t)
        if not (u["stated"] and not u["excluded"] and u["sign"] in ("up", "down") and u["stable"]):
            return u
        src = t["source"]
        prov = rs.claim_provenance(e, t, idx.artefacts)
        transfer = rs.group_transfer_unresolved(src, t, module_symbols) or rs.republished_transfer_unresolved(prov, module_symbols)
        glue = "" if transfer else conflict_or_glue(rs, family_members(idx, e), t)
        transfer = transfer or glue
        if not transfer:
            return u
        chembl = src.startswith("ChEMBL")
        genes = list(t.get("gene_symbols") or []) if chembl else [t.get("gene") or ""]
        waived = [] if glue else [g for g in genes if g and rs.documented_level_waiver(e, t, g, u["sign"], idx.artefacts)]
        log.append(dict(record=e["id"], name=e.get("name"), source=src, claim_source=t.get("claim_source") or "",
                        target_level=rs.target_level(src, t), effective_level=(prov or {}).get("republished_record_level", ""),
                        chembl_target=t.get("target_id") or "", genes=";".join(genes), action=u["sign"],
                        reason_class=reason_class(transfer), waived_genes=";".join(waived), assertion_key=rs.assertion_key(e, src, t, prov)))
        return dict(u, sign="unresolved", it21_withheld=reason_class(transfer), it21_waived=waived)
    return row_usability


def cmd_run(a):
    import repurposing_search as rs
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    log = []
    ms = rs.module_intervention_symbols(rs.load_needs()["needs"])
    orig_spec = importlib.util.module_from_spec
    seen = {}

    def patched_module_from_spec(spec):
        m = orig_spec(spec)
        if a.guards == "on" and spec.name == "usable_census":
            ex = spec.loader.exec_module

            def run_and_wrap(mod, _ex=ex):
                _ex(mod)
                mod.row_usability = make_wrapper(mod.row_usability, ms, log)
                seen["wrapped"] = True
            spec.loader.exec_module = run_and_wrap
        return m

    sys.argv = ["build_actions_v3.py", "--out", str(out), "--catalog", a.catalog]
    spec = importlib.util.spec_from_file_location("build_actions_v3", V3 / "build_actions_v3.py")
    b = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b)
    importlib.util.module_from_spec = patched_module_from_spec
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            b.main()
    finally:
        importlib.util.module_from_spec = orig_spec
    if a.guards == "on" and not seen.get("wrapped"):
        raise SystemExit("the guard wrapper was not installed: the v3 builder no longer loads usable_census the way this adapter expects")
    added = add_waived(out, log, b, a.catalog) if a.guards == "on" else 0
    summ = dict(guards=a.guards, module_intervention_symbols=len(ms), withheld_rows=len(log),
                withheld_by_class=dict(collections.Counter(r["reason_class"] for r in log)),
                waived_pairs_added=added, builder_funnel=json.loads((out / "build_funnel_v3.json").read_text())["counts"])
    (out / "refresh_summary.json").write_text(json.dumps(summ, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if log:
        with gzip.open(out / "withheld_rows.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(log[0]), delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerows(sorted(log, key=lambda r: (r["record"], r["chembl_target"], r["genes"], r["source"])))
    print(json.dumps({k: v for k, v in summ.items() if k != "builder_funnel"}, indent=1, sort_keys=True))


def add_waived(out, log, b, catalog):
    """Add back (family, gene) pairs whose record-level abstention is answered by a documented single-protein measurement. Gene-specific."""
    import compound_catalog as cc
    import repurposing_search as rs
    H = b.Hgnc()
    entries = cc.load(Path(catalog))
    fam = rs.families(entries)
    want = {}
    for r in log:
        for g in filter(None, r["waived_genes"].split(";")):
            sym = H.canon(g)
            if sym:
                want[(fam[r["record"]], sym.upper())] = (1.0 if r["action"] == "up" else -1.0, H.sym_to_id(g))
    rows = list(csv.reader(gzip.open(out / "family_actions.tsv.gz", "rt", encoding="utf-8"), delimiter="\t"))
    head, body = rows[0], rows[1:]
    have = {(r[0], r[1].upper()) for r in body}
    n = 0
    for (f, sym), (sign, hid) in sorted(want.items()):
        if (f, sym) in have:
            continue
        body.append([f, sym, f"{sign:.4f}", "1", "ChEMBL", "single_protein", hid, "DOCUMENTED_LEVEL_WAIVER"])
        n += 1
    body.sort(key=lambda r: (r[0], r[1]))
    with gzip.open(out / "family_actions.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(head)
        w.writerows(body)
    if n:
        meta = list(csv.reader(gzip.open(out / "family_meta.tsv.gz", "rt", encoding="utf-8"), delimiter="\t"))
        ui = meta[0].index("mnet_usable")
        act = {r[0] for r in body}
        for r in meta[1:]:
            r[ui] = "1" if r[0] in act else "0"
        with gzip.open(out / "family_meta.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
            csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(meta)
    return n


def read_actions(d):
    out = {}
    for r in csv.DictReader(gzip.open(Path(d) / "family_actions.tsv.gz", "rt", encoding="utf-8"), delimiter="\t"):
        out[(r["family_id"], r["target_symbol"].upper())] = float(r["mean_sign"])
    return out


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def cmd_diff(a):
    old, new = read_actions(a.old), read_actions(a.new)
    names = {}
    for d in (a.new, a.old):
        for r in csv.DictReader(gzip.open(Path(d) / "family_meta.tsv.gz", "rt", encoding="utf-8"), delimiter="\t"):
            names.setdefault(r["family_id"], r["name"])
    rows = []
    for k in sorted(set(old) | set(new)):
        o, n = old.get(k), new.get(k)
        st = "kept" if o is not None and n is not None and sign(o) == sign(n) else "sign_changed" if o is not None and n is not None else "lost" if n is None else "gained"
        if st != "kept":
            rows.append([k[0], names.get(k[0], ""), k[1], "" if o is None else f"{o:.3f}", "" if n is None else f"{n:.3f}", st])
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family_id", "name", "target_symbol", "mean_sign_old", "mean_sign_new", "status"])
        w.writerows(rows)
    c = collections.Counter(r[5] for r in rows)
    fo, fn = {k[0] for k in old}, {k[0] for k in new}
    print(json.dumps(dict(pairs_old=len(old), pairs_new=len(new), pairs_changed=dict(c), families_old=len(fo), families_new=len(fn),
                          families_lost=len(fo - fn), families_gained=len(fn - fo)), sort_keys=True))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    r = sp.add_parser("run")
    r.add_argument("--out", required=True)
    r.add_argument("--guards", choices=["on", "off"], default="on")
    r.add_argument("--catalog", default=str(DR / "catalog" / "catalog.jsonl.gz"))
    d = sp.add_parser("diff")
    d.add_argument("--old", required=True)
    d.add_argument("--new", required=True)
    d.add_argument("--out", required=True)
    a = ap.parse_args()
    {"run": cmd_run, "diff": cmd_diff}[a.cmd](a)
