#!/usr/bin/env python3
"""IT21 P5: does WWOX-specific information add anything beyond direct target search? Arm comparison, measures and the decision rule.

Arms (what each removes, what each keeps, and which difference is measured):
  A1 direct search on need targets, external-only   the IT20 arm E (`hypotheses_it20_20261102/compare_universe.py`): a documented up/down action on a target of a need. Uses NO
                                                    WWOX observation. Also the direct hits on the seed genes (the engine's `direct_search` arm).
  A2 mechanistic indirect path, WWOX seeds           the IT21 P2 generator output: 992 seed-specific rows, 141 eligible, 13 handed over.
  A3 the same generator, WWOX seed identity removed  `decoy_arm.py`: every seed gene replaced by a degree-matched gene (coarse decile = the engine's own null; the 30 nearest genes in
                                                    degree; the 30 nearest in F5-admissible reach). Same engine, nulls, compound side, rules. Difference measured: what A2 has that a seed
                                                    set of the same size, direction, level and hub size does not.
  A4 phenotype-first                                 the 7 interventions with a recorded WWOX-system result (IT10) and the P3b units; reported, not simulated (n = 7).

The decision rule is fixed in `decide()` and is applied to the numbers, not tuned to them:
  C1 count     the real set has more seed-specific rows than the 95th percentile of the FINE-matched decoys (degree and reach designs) in at least 3 of the 5 sets
  C2 content   at least half of the real eligible rows are not generic: their (family, sign) occurs in <= 5 percent of the decoys of both fine designs
  C3 direct    the share of real seed-specific rows that are beyond direct search is above the decoy 95th percentile in at least 3 sets
  C4 needs     the share of real seed-specific rows whose main target is a need target is above the decoy 95th percentile in at least 3 sets
  informative addition  = C1 and C2 and (C3 or C4);  no advantage = not C1 and not C2;  inconclusive = anything else.

  compare_arms.py run --decoys results/decoy_rows.tsv.gz --out results [--skip-routed]
  compare_arms.py decide --summary results/summary_p5.json

A retrospective analysis and a synthetic perturbation test the properties of the method. They do not show prospective therapeutic benefit. Not medical advice. Public edition: the
subject is the WWOX-DEE reference genotype class. Zero spend, no network, no contact.
"""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help")):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, csv, gzip, importlib.util, json, re, statistics, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = DR.parents[3]
P2 = DR / "generation_it21_p2_20261103"
P3B = DR / "qualification_it21_p3b_20261103"
IT10 = DR / "generation_it10_p1_20261031"
SETS = ("Q2_expression_tiersAB", "Q4_expression_tiersAB", "Q5_expression_tiersAB", "Q6_expression_tiersAB", "Q6_protein_tiersAB")
FINE = ("deg", "reach")
VARIANTS = ("coarse", "deg", "reach")
GENERIC_FREQ = 0.05
sys.path.insert(0, str(REPO / "framework/scripts"))


def rd(p):
    with (gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def wr(path, rows, cols=None):
    cols = cols or (list(rows[0]) if rows else [])
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in cols})


def load_module(path, name, argv=None):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    saved = sys.argv
    sys.argv = argv or ["x", "run"]
    sys.modules[name] = m
    try:
        spec.loader.exec_module(m)
    finally:
        sys.argv = saved
    return m


def pct(xs, q):
    xs = sorted(xs)
    if not xs:
        return None
    k = (len(xs) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (k - lo)


def upper_p(real, decoys):
    """One-sided empirical p that a decoy is at least as large as the real value (add-one rule)."""
    return (1 + sum(1 for d in decoys if d >= real)) / (1 + len(decoys))


# ---- context: catalogue, P2 helpers, the direct-search universe -----------------------------------------------------------------------------------------
class Context:
    def __init__(self):
        import compound_catalog as cc
        import repurposing_search as rs
        self.R = load_module(P2 / "run_generation_it21.py", "run_generation_it21", ["run_generation_it21.py", "propose"])
        self.D = self.R.load_dispose()
        self.roles = self.D.load_roles(IT10 / "question_roles.tsv")
        entries = cc.load(DR / "catalog" / "catalog.jsonl.gz")
        fam = rs.families(entries)
        modality = {}
        for e in entries:
            f = fam[e["id"]]
            if (e.get("ids") or {}).get("chembl") or f not in modality:
                modality[f] = e.get("modality")
        self.meta = {r["family_id"]: r for r in self.R.rd(P2 / "results" / "actions" / "family_meta.tsv.gz")}
        for f, m in self.meta.items():
            m["modality"] = modality.get(f)
        self.decisions = self.R.earlier_decisions()
        needs = rs.load_needs()["needs"]
        self.module_symbols = rs.module_intervention_symbols(needs)
        cu = load_module(DR / "hypotheses_it20_20261102" / "compare_universe.py", "compare_universe", ["compare_universe.py", "run"])
        idx = rs.Index(entries, rs.load_artefacts(), self.module_symbols)
        self.U = cu.build_universe(needs, idx, rs.load_roles())
        self.E_rows = cu.arm_external(self.U)
        base = self.R.base_name
        self.E_fam = {r["family"] for r in self.E_rows}
        self.E_base = {base(r["compound"]) for r in self.E_rows}
        self.U_fam = {a["family"] for a in self.U}
        self.U_base = {base(a["compound"]) for a in self.U}
        self.need_targets = {a["target"].upper() for a in self.U} | {s.upper() for s in self.module_symbols}
        self.corpus = self.R.corpus_text()
        self._state = {}

    def earlier(self, name):
        if name not in self._state:
            self._state[name] = self.R.earlier_state(name, self.decisions)
        return self._state[name]

    def classify(self, name, family, main_target, direct_hit):
        b = self.R.base_name(name)
        in_e = family in self.E_fam or b in self.E_base
        in_u = family in self.U_fam or b in self.U_base
        tn = (main_target or "").upper() in self.need_targets
        dh = str(direct_hit) in ("1", "True", "true")
        return dict(direct_on_seed=int(dh), in_arm_E=int(in_e), linked_to_a_need=int(in_u), target_is_need_target=int(tn),
                    beyond_direct=int(not dh and not in_e and not tn))

    def eligibility(self, question, sign, family, name, z_reach):
        """The P2 hand-over rule H1 to H4 (the same function), for a decoy or real row. Returns (ok, reason)."""
        arm = "opposes" if int(sign) > 0 else "mimics"
        row = dict(arm=arm, seed_specific_all_three_nulls="1", reach_z=z_reach, family_id=family, name=name)
        return self.R.eligible(row, self.roles[question], self.meta, self.decisions)


# ---- per-replicate metrics --------------------------------------------------------------------------------------------------------------------------
def capped(clusters_by_group, cap=3):
    return sum(min(cap, len(v)) for v in clusters_by_group.values())


def replicate_metrics(ctx, seed_set, rows, pool_by="set"):
    """rows: seed-specific rows of one replicate (dicts with family_id, name, sign, z_reach, reach_ok, main_target, direct_hit).
    Eligibility is P2's H1 to H4 (`eligible`) followed by H8 (a mechanism cluster with an earlier qualification record on ANY member is not handed over).
    The cluster is (seed set, hypothesis, main target); P2 pools the sets of one question, `pool_by="question"` reproduces that for the control."""
    q = seed_set.split("_")[0]
    scope = q if pool_by == "question" else seed_set
    out = collections.Counter()
    reasons = collections.Counter()
    tgts = collections.Counter()
    pending, decided = [], set()
    for r in rows:
        out["spec"] += 1
        sg = int(r["sign"])
        hyp = "H_HARM" if sg > 0 else "H_PROTECT"
        main = (r["main_target"] or "").upper()
        out["opposes" if sg > 0 else "mimics"] += 1
        c = ctx.classify(r["name"], r["family_id"], r["main_target"], r["direct_hit"])
        for k, v in c.items():
            out[k] += v
        tgts[main] += 1
        st = ctx.earlier(r["name"])
        if st:
            out["earlier_decision"] += 1
            out["earlier_" + st[0].split()[0]] += 1
            decided.add((scope, hyp, main))
        if int(r["reach_ok"]):
            out["reach_ok"] += 1
        ok, why = ctx.eligibility(q, sg, r["family_id"], r["name"], r["z_reach"])
        if ok:
            pending.append((scope, hyp, main, c))
        else:
            reasons[why] += 1
    clusters = collections.defaultdict(set)
    for scope_, hyp, main, c in pending:
        if (scope_, hyp, main) in decided:
            reasons["mechanism_cluster_examined_earlier"] += 1
            continue
        out["eligible"] += 1
        out["eligible_beyond_direct"] += c["beyond_direct"]
        out["eligible_target_is_need_target"] += c["target_is_need_target"]
        clusters[(scope_, hyp)].add(main)
    out["clusters"] = sum(len(v) for v in clusters.values())
    out["handover_capped_3"] = capped(clusters)
    top5 = sum(n for _, n in tgts.most_common(5))
    out["top5_main_target_share_x1000"] = round(1000 * top5 / out["spec"]) if out["spec"] else 0
    out["distinct_main_targets"] = len(tgts)
    return out, reasons, tgts


def p2_control(ctx, real):
    """The real rows through this code, pooled by question as P2 does: must give P2's 141 eligible rows, its 32 clusters and 13 handed over."""
    by_q = collections.defaultdict(list)
    for sn in SETS:
        by_q[sn.split("_")[0]] += [dict(r, _set=sn) for r in real[sn]]
    el = clu = cap = 0
    for q, rows in by_q.items():
        m, _, _ = replicate_metrics(ctx, q + "_pooled", rows, pool_by="question")
        el += m["eligible"]; clu += m["clusters"]; cap += m["handover_capped_3"]
    return dict(eligible=el, clusters=clu, capped=cap)


def load_decoys(path):
    by = collections.defaultdict(list)       # (set, variant, rep) -> rows
    for r in rd(path):
        by[(r["seed_set"], r["variant"], int(r["rep"]))].append(r)
    return by


def real_rows_from_engine():
    """The real seed sets through the same shape: the committed P2 seed-specific list joined with its reach z (control: equals decoy_arm.py rep 0)."""
    reach = {}
    for sn in SETS:
        p = P2 / "results" / "engine" / f"proposals_p1_{sn}_reach.tsv.gz"
        reach[sn] = {r["family_id"]: float(r["Z_ind_robust"]) for r in rd(p)}
    contrib = {}
    out = collections.defaultdict(list)
    for s in rd(P2 / "results" / "engine" / "v3_seed_specific_all_nulls.tsv"):
        sn = s["seed_set"]
        sign = 1 if s["arm"] == "opposes" else -1
        zr = reach[sn].get(s["family_id"])
        if sn not in contrib:
            cc_ = collections.defaultdict(list)
            for c in rd(P2 / "results" / "engine" / f"contributions_p1_{sn}.tsv.gz"):
                cc_[c["family_id"]].append(c)
            contrib[sn] = cc_
        cs = sorted(contrib[sn].get(s["family_id"], []), key=lambda c: -abs(float(c["contrib_total"])))
        main = ""
        if cs:
            c = cs[0]
            main = c["main_target_hop0"] if abs(float(c["contrib_hop0"])) > abs(float(c["contrib_hops1to3"])) else c["main_target_hops1to3"]
        out[sn].append(dict(seed_set=sn, family_id=s["family_id"], name=s["name"], sign=sign, z_reach="" if zr is None else zr,
                            reach_ok=int(zr is not None and zr * sign > 3), main_target=main, direct_hit=s["also_found_by_direct_search"]))
    return out


# ---- decision rule ----------------------------------------------------------------------------------------------------------------------------------
def decide(c1, c2, c3, c4):
    """Pure. c1..c4 are booleans (see the module docstring)."""
    if c1 and c2 and (c3 or c4):
        return "informative addition"
    if not c1 and not c2:
        return "no advantage"
    return "inconclusive"


def sets_above(real, dec_by_set, metric, variants):
    """Number of sets in which the real value exceeds the 95th percentile of the decoys pooled over the listed variants; and the per-set detail."""
    n, detail = 0, []
    for sn in SETS:
        ds = [m[metric] for v in variants for m in dec_by_set.get((sn, v), [])]
        if not ds:
            continue
        p95 = pct(ds, 0.95)
        above = real[sn][metric] > p95
        n += int(above)
        detail.append(dict(seed_set=sn, metric=metric, variants="+".join(variants), real=real[sn][metric], decoy_median=pct(ds, .5), decoy_p05=pct(ds, .05), decoy_p95=p95,
                           decoy_max=max(ds), n_decoys=len(ds), p_upper=round(upper_p(real[sn][metric], ds), 4), real_above_p95=int(above)))
    return n, detail


# ---- main analysis ----------------------------------------------------------------------------------------------------------------------------------
def share(m, num):
    return m[num] / m["spec"] if m["spec"] else 0.0


def cmd_run(a):
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    ctx = Context()
    real = real_rows_from_engine()
    dec = load_decoys(a.decoys)
    reps = collections.defaultdict(set)
    for (sn, v, k) in dec:
        reps[(sn, v)].add(k)
    # decoys with zero seed-specific rows produce no row at all: the replicate list comes from the run size, not from the rows
    k_nominal = a.k or max((k for (_, _, k) in dec), default=0)

    # per-replicate metrics
    real_m, dec_m = {}, collections.defaultdict(list)
    real_reasons, dec_reasons = {}, collections.defaultdict(collections.Counter)
    real_targets, dec_targets = {}, collections.defaultdict(collections.Counter)
    for sn in SETS:
        m, why, tg = replicate_metrics(ctx, sn, real[sn])
        real_m[sn], real_reasons[sn], real_targets[sn] = m, why, tg
        for v in VARIANTS:
            for k in range(1, k_nominal + 1):
                mm, ww, tt = replicate_metrics(ctx, sn, dec.get((sn, v, k), []))
                mm["rep"] = k
                dec_m[(sn, v)].append(mm)
                dec_reasons[(sn, v)].update(ww)
                dec_targets[(sn, v)].update(tt)
    # control: the committed P2 handover (13) and eligible (141) are reproduced by this code on the real rows
    tot_elig = sum(real_m[sn]["eligible"] for sn in SETS)
    ctrl = p2_control(ctx, real)

    metrics = ["spec", "reach_ok", "eligible", "clusters", "handover_capped_3", "beyond_direct", "eligible_beyond_direct", "target_is_need_target", "in_arm_E", "direct_on_seed",
               "linked_to_a_need", "earlier_decision", "earlier_REFERENCE", "distinct_main_targets", "top5_main_target_share_x1000"]
    per_rep = []
    for sn in SETS:
        r = dict(seed_set=sn, variant="real", rep=0)
        r.update({k: real_m[sn][k] for k in metrics})
        per_rep.append(r)
        for v in VARIANTS:
            for mm in dec_m[(sn, v)]:
                r = dict(seed_set=sn, variant=v, rep=mm["rep"])
                r.update({k: mm[k] for k in metrics})
                per_rep.append(r)
    wr(out / "per_replicate_p5.tsv", per_rep, ["seed_set", "variant", "rep"] + metrics)

    # counts table with empirical p
    rows = []
    for sn in SETS:
        for metric in metrics:
            row = dict(seed_set=sn, metric=metric, real=real_m[sn][metric])
            for v in VARIANTS:
                ds = [m[metric] for m in dec_m[(sn, v)]]
                row[f"{v}_median"] = pct(ds, .5)
                row[f"{v}_p05"] = pct(ds, .05)
                row[f"{v}_p95"] = pct(ds, .95)
                row[f"{v}_max"] = max(ds) if ds else ""
                row[f"{v}_p_upper"] = round(upper_p(real_m[sn][metric], ds), 4) if ds else ""
            rows.append(row)
    cols = ["seed_set", "metric", "real"] + [f"{v}_{s}" for v in VARIANTS for s in ("median", "p05", "p95", "max", "p_upper")]
    wr(out / "counts_vs_decoys_p5.tsv", rows, cols)

    # shares (beyond direct, need target) per replicate
    for sn in SETS:
        real_m[sn]["share_beyond_direct"] = share(real_m[sn], "beyond_direct")
        real_m[sn]["share_need_target"] = share(real_m[sn], "target_is_need_target")
        real_m[sn]["share_in_arm_E"] = share(real_m[sn], "in_arm_E")
        for v in VARIANTS:
            for mm in dec_m[(sn, v)]:
                mm["share_beyond_direct"] = share(mm, "beyond_direct")
                mm["share_need_target"] = share(mm, "target_is_need_target")
                mm["share_in_arm_E"] = share(mm, "in_arm_E")
    dec_by_set = {k: v for k, v in dec_m.items()}
    n_c1, d_c1 = sets_above(real_m, dec_by_set, "spec", FINE)
    n_c3, d_c3 = sets_above(real_m, dec_by_set, "share_beyond_direct", FINE)
    n_c4, d_c4 = sets_above(real_m, dec_by_set, "share_need_target", FINE)
    _, d_c1c = sets_above(real_m, dec_by_set, "spec", ("coarse",))
    _, d_el = sets_above(real_m, dec_by_set, "eligible", FINE)
    _, d_hc = sets_above(real_m, dec_by_set, "handover_capped_3", FINE)
    wr(out / "criteria_detail_p5.tsv", d_c1 + d_c1c + d_el + d_hc + d_c3 + d_c4)

    # C2: genericity of the real rows (frequency of the same (family, sign) in the decoys of the same set)
    freq = {}
    for (sn, v), ks in reps.items():
        pass
    cnt = collections.defaultdict(collections.Counter)        # (set, variant) -> (family, sign) -> number of decoys
    for (sn, v, k), rws in dec.items():
        for r in rws:
            cnt[(sn, v)][(r["family_id"], int(r["sign"]))] += 1
    real_rows_tab = []
    P = rd(P2 / "results" / "proposals_it21.tsv")
    handed = {h["proposal_id"] for h in rd(P2 / "results" / "handoff_it21.tsv")}
    prow = {}
    for r in P:
        sg = 1 if r["hypothesis"] == "H_HARM" else -1
        prow[(r["seed_set"], r["family_id"], sg)] = r
    decided_q = set()          # H8, pooled by question as P2 does
    for sn in SETS:
        for r in real[sn]:
            if ctx.earlier(r["name"]):
                decided_q.add((sn.split("_")[0], "H_HARM" if int(r["sign"]) > 0 else "H_PROTECT", (r["main_target"] or "").upper()))
    for sn in SETS:
        for r in real[sn]:
            sg = int(r["sign"])
            ok, why = ctx.eligibility(sn.split("_")[0], sg, r["family_id"], r["name"], r["z_reach"])
            if ok and (sn.split("_")[0], "H_HARM" if sg > 0 else "H_PROTECT", (r["main_target"] or "").upper()) in decided_q:
                ok, why = False, "mechanism_cluster_examined_earlier"
            pr = prow.get((sn, r["family_id"], sg), {})
            row = dict(seed_set=sn, family_id=r["family_id"], compound=r["name"], hypothesis="H_HARM" if sg > 0 else "H_PROTECT", main_target=r["main_target"],
                       eligible=int(ok), blocker="" if ok else why, handed_over=int(pr.get("proposal_id") in handed), proposal_id=pr.get("proposal_id", ""),
                       n_origins=pr.get("n_origins", ""), earlier_decision=(pr.get("earlier_decision") or "")[:40])
            row.update(ctx.classify(r["name"], r["family_id"], r["main_target"], r["direct_hit"]))
            for v in VARIANTS:
                row[f"decoy_freq_{v}"] = round(cnt[(sn, v)][(r["family_id"], sg)] / max(1, k_nominal), 3)
            row["generic_in_both_fine"] = int(all(row[f"decoy_freq_{v}"] > GENERIC_FREQ for v in FINE))
            row["generic_in_any_fine"] = int(any(row[f"decoy_freq_{v}"] > GENERIC_FREQ for v in FINE))
            real_rows_tab.append(row)
    wr(out / "real_rows_vs_decoy_frequency_p5.tsv", real_rows_tab)
    el = [r for r in real_rows_tab if r["eligible"]]
    ho = [r for r in real_rows_tab if r["handed_over"]]
    spec_rows = real_rows_tab

    def frac(rows, key, val=1):
        return round(sum(1 for r in rows if r[key] == val) / len(rows), 4) if rows else None
    c2_share = 1 - (sum(r["generic_in_any_fine"] for r in el) / len(el)) if el else 0.0
    c2 = c2_share >= 0.5

    # known-lead recovery, sign conflicts across sets, Jaccard between sets
    def jacc(a_, b_):
        return len(a_ & b_) / len(a_ | b_) if (a_ | b_) else 0.0
    pairs = [(x, y) for i, x in enumerate(SETS) for y in SETS[i + 1:]]
    real_sets = {sn: {(r["family_id"], int(r["sign"])) for r in real[sn]} for sn in SETS}
    real_j = statistics.mean(jacc(real_sets[x], real_sets[y]) for x, y in pairs)
    jac_dec = {}
    for v in VARIANTS:
        vals = []
        for k in range(1, k_nominal + 1):
            ss = {sn: {(r["family_id"], int(r["sign"])) for r in dec.get((sn, v, k), [])} for sn in SETS}
            vals.append(statistics.mean(jacc(ss[x], ss[y]) for x, y in pairs))
        jac_dec[v] = vals

    def sign_conflicts(sets_):
        fam = collections.defaultdict(set)
        for sn, s in sets_.items():
            for f, sg in s:
                fam[f].add(sg)
        return sum(1 for v in fam.values() if len(v) > 1), len(fam)
    real_conf = sign_conflicts(real_sets)
    conf_dec = {v: [sign_conflicts({sn: {(r["family_id"], int(r["sign"])) for r in dec.get((sn, v, k), [])} for sn in SETS}) for k in range(1, k_nominal + 1)] for v in VARIANTS}
    cross = [dict(measure="mean Jaccard of the (family, sign) sets over the 10 pairs of seed sets", real=round(real_j, 4),
                  **{f"{v}_median": round(pct(jac_dec[v], .5), 4) for v in VARIANTS}, **{f"{v}_p95": round(pct(jac_dec[v], .95), 4) for v in VARIANTS},
                  **{f"{v}_p_upper": round(upper_p(real_j, jac_dec[v]), 4) for v in VARIANTS}),
             dict(measure="families selected as opposes in one set and mimics in another (of all families selected anywhere)", real=f"{real_conf[0]} of {real_conf[1]}",
                  **{f"{v}_median": f"{pct([c[0] for c in conf_dec[v]], .5)} of {pct([c[1] for c in conf_dec[v]], .5)}" for v in VARIANTS})]
    wr(out / "cross_set_and_sign_p5.tsv", cross, ["measure", "real"] + [f"{v}_{s}" for v in VARIANTS for s in ("median", "p95", "p_upper")])

    # phenotype-first arm (A4): the interventions with a recorded WWOX-system result, searched by name in the seed-specific rows of the real sets and of the decoys
    pf = []
    for term in ("lithium", "ethosuximide", "vigabatrin", "apv"):
        for sn in SETS:
            row = dict(intervention=term, seed_set=sn, real_rows=sum(1 for r in real[sn] if term in r["name"].lower()),
                       real_arms=",".join(sorted({"opposes" if int(r["sign"]) > 0 else "mimics" for r in real[sn] if term in r["name"].lower()})))
            for v in VARIANTS:
                hits = sum(1 for k in range(1, k_nominal + 1) if any(term in r["name"].lower() for r in dec.get((sn, v, k), [])))
                row[f"{v}_share_of_decoys_with_a_hit"] = round(hits / max(1, k_nominal), 3)
            pf.append(row)
    wr(out / "phenotype_first_recovery_p5.tsv", pf)

    # hubs: main targets of the real rows that are also the main target in >= 25 percent of the decoys of that set
    hub = []
    for sn in SETS:
        for v in VARIANTS:
            tc = collections.Counter()
            for k in range(1, k_nominal + 1):
                for t in {(r["main_target"] or "").upper() for r in dec.get((sn, v, k), [])}:
                    tc[t] += 1
            frequent = {t for t, n in tc.items() if n / max(1, k_nominal) >= 0.25}
            rr = real[sn]
            n_in = sum(1 for r in rr if (r["main_target"] or "").upper() in frequent)
            hub.append(dict(seed_set=sn, variant=v, real_rows=len(rr), real_rows_on_a_target_frequent_in_decoys=n_in,
                            share=round(n_in / len(rr), 4) if rr else "", frequent_targets=len(frequent), top_real_targets="; ".join(f"{t}:{n}" for t, n in real_targets[sn].most_common(5)),
                            top_decoy_targets="; ".join(f"{t}:{n}" for t, n in dec_targets[(sn, v)].most_common(5))))
    wr(out / "hub_dependence_p5.tsv", hub)

    # blockers: real vs decoys (mean per replicate)
    blk = []
    keys = sorted({k for sn in SETS for k in real_reasons[sn]} | {k for kk in dec_reasons.values() for k in kk})
    for key in keys:
        row = dict(blocker=key, real=sum(real_reasons[sn][key] for sn in SETS))
        for v in VARIANTS:
            row[f"{v}_mean_per_replicate_over_5_sets"] = round(sum(dec_reasons[(sn, v)][key] for sn in SETS) / max(1, k_nominal), 1)
        blk.append(row)
    wr(out / "blockers_real_vs_decoys_p5.tsv", blk)

    # summary and decision
    c1 = n_c1 >= 3
    c3 = n_c3 >= 3
    c4 = n_c4 >= 3
    decision = decide(c1, c2, c3, c4)
    summary = dict(
        k_decoys_per_design=k_nominal, designs=list(VARIANTS), fine_designs=list(FINE),
        control=dict(pooled_by_question_like_P2=ctrl, p2_published=dict(eligible=141, clusters=32, handed_over=13), real_eligible_per_set_rule=tot_elig, real_spec_rows={sn: len(real[sn]) for sn in SETS}),
        criteria=dict(C1_count_sets_above_p95=n_c1, C1=c1, C2_share_not_generic_eligible=round(c2_share, 4), C2=c2, C3_sets_above_p95=n_c3, C3=c3, C4_sets_above_p95=n_c4, C4=c4),
        decision=decision,
        real_eligible=len(el), real_eligible_generic_in_any_fine=sum(r["generic_in_any_fine"] for r in el),
        handed_over=dict(n=len(ho), generic_in_any_fine=sum(r["generic_in_any_fine"] for r in ho), generic_in_both_fine=sum(r["generic_in_both_fine"] for r in ho),
                         beyond_direct=sum(r["beyond_direct"] for r in ho), target_is_need_target=sum(r["target_is_need_target"] for r in ho), in_arm_E=sum(r["in_arm_E"] for r in ho)),
        real_spec_rows=dict(n=len(spec_rows), beyond_direct=sum(r["beyond_direct"] for r in spec_rows), in_arm_E=sum(r["in_arm_E"] for r in spec_rows),
                            target_is_need_target=sum(r["target_is_need_target"] for r in spec_rows), direct_on_seed=sum(r["direct_on_seed"] for r in spec_rows),
                            linked_to_a_need=sum(r["linked_to_a_need"] for r in spec_rows),
                            generic_in_any_fine=sum(r["generic_in_any_fine"] for r in spec_rows), generic_in_both_fine=sum(r["generic_in_both_fine"] for r in spec_rows)),
        direct_search_universe=dict(arm_E_families=len(ctx.E_fam), need_targets=len(ctx.need_targets), associations=len(ctx.U)),
    )
    (out / "summary_p5.json").write_text(json.dumps(summary, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=1))
    return summary


def cmd_decide(a):
    s = json.loads(Path(a.summary).read_text())
    c = s["criteria"]
    print(decide(c["C1"], c["C2"], c["C3"], c["C4"]))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("--decoys", required=True); r.add_argument("--out", default=str(HERE / "results")); r.add_argument("--k", type=int, default=0)
    d = sub.add_parser("decide"); d.add_argument("--summary", required=True)
    a = ap.parse_args()
    {"run": cmd_run, "decide": cmd_decide}[a.cmd](a)


if __name__ == "__main__":
    main()
